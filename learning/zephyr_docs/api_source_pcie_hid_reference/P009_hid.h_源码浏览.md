---
id: learning.zephyr-docs.api-source-pcie-hid-reference.page-9
title: hid.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb_2class_2hid_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_hid.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usb_2class_2hid_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usb_2class_2hid_8h.html)。

## 9.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00031"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00198"></a>
<a id="l00203"></a>
<a id="foldopen00212"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="foldopen00224"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="foldopen00235"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="foldopen00244"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="foldopen00256"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="foldopen00267"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="foldopen00279"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="foldopen00288"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="foldopen00300"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="foldopen00312"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="foldopen00322"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="foldopen00332"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="foldopen00344"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="foldopen00356"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="foldopen00368"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="foldopen00377"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="foldopen00389"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="foldopen00401"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="foldopen00410"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="foldopen00422"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="foldopen00434"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="foldopen00447"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="foldopen00460"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00475"></a>
<a id="l00480"></a>
<a id="foldopen00486"></a>
<a id="l00486"></a>
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
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="foldopen00525"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
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
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
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
<a id="foldopen00574"></a>
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
<a id="l00664"></a>
<a id="l00665"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="foldopen00677"></a>
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
<a id="foldopen00692"></a>
<a id="l00692"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00703"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="agroup__usb__hid__mk__report__desc_html_ga12f11556b697518b00fa86eb040f9eb8"></a>
<a id="agroup__usb__hid__mk__report__desc_html_ga4f2bb15109c64695f852afd6bd99e3bf"></a>
<a id="agroup__usb__hid__mk__report__desc_html_ga8cef56ba216d0a01c6cc89f723d1740b"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga12f11556b697518b00fa86eb040f9eb8a1b4b75cd0364824cbfc80dfc68e294dd"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga12f11556b697518b00fa86eb040f9eb8a4df663509a05599fd66657cfc90a37c7"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga12f11556b697518b00fa86eb040f9eb8a718c92a2d0ca9dd6603825b97a99fc77"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga12f11556b697518b00fa86eb040f9eb8a79b0eb4f485bedb745180f1b8798c603"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga12f11556b697518b00fa86eb040f9eb8a829d884291b546c0e276afa4ad92ac18"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga12f11556b697518b00fa86eb040f9eb8a85ce29a6ab9feef68350deca92001db2"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga12f11556b697518b00fa86eb040f9eb8a8e346c0e9c7d5b58e4b8748380423a92"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga12f11556b697518b00fa86eb040f9eb8aba69ca183306d3d1427b66666803e57f"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga12f11556b697518b00fa86eb040f9eb8affdba298e8860b000a0916be7495c2dc"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa02f14e6303b4d2e4e46747324d649dda"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa037de00c763ae6b270895b7a5f0f57a7"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa039ced168420140b97e2d0676e1bb12a"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa05fb920f8129f57dd350036f17fbe519"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa0d57ce7c99d06ee9b15fef880af075eb"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa17019d72e84302486f72f7d8101baca5"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa1761228849d7dc2b84d0565d3337b2e2"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa1905733a0fe81f78e0752e3b0bb99c69"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa1b8d299d56a0289ae15cbf8c67e36a7c"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa1e191017084fadf830a7394de0e1cc05"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa1e1c320cea0644c3dc38da06c865837b"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa1e2eabf8b9fa6cbfea613696b2c4122a"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa1eadd56346bbd64b1c33fa5393f65bda"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa2468ac3b37d38b6158cd989ed54bcd8c"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa24c2c93a1c895745828311affc011dea"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa25ba5457bc128593b1624d95ec536182"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa2a78196208c634941d63429cd1e1df7a"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa2cb7852467d2ebd785e2f7556383a883"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa3743f920856a12e726e1be05932c7411"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa403fe927ebb0014e2c1b3dc25e1d9779"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa4210f9a5ae469c8b863b28b9b2d8189d"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa44e83040efab214dcfe462ac0d338e0c"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa48eefeeb48a942eaaa0726bd4a2df01d"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa4ae4af2b06f6f2585a598353bfef9af7"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa4b07b1bbe7695f2f67ce9df298c1d3c7"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa4bfc341fccde664ec9267af6e705ba0c"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa4c203feb452e3212089e8246b8d75f6c"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa4ca2ebe26c09f2400a8ebc0aa445ce89"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa4ceddaaaa90d84f0afb3e1ee9a35a976"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa4d40549a59fdcfdd0b2d592a6675bc89"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa4f8174feca1eb72901576c4e24c8f8a9"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa5092add2863231d273ba60cd583ebe33"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa5413afa6a28a21dd52f07db101f2d139"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa5887a1854f7d0787121bd75034cdd726"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa5a09deabde1a3a44378b7de44dad27b6"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa5a6c79e8ea85f6593c06d19098d69a03"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa5fc1127fe9014018f4831cbf272c883b"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa68db65e7002e7cc599394a7eea116e3c"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa6fb35c78b12ae434cb7a7280501886e9"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa7325a5bd52e9dc0cc38a85609b1c55ab"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa758aec2540a6a2153702d6905c44ce52"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa763b39fe76a92c4cc1fc32f47d2a760a"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa76adde1d9295cf62e7efb35e27911a1e"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa76bb35a0f71733b0a0f1bd7e3837064c"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa7eea75b0eb4b4f0306daa3e6fccf09e4"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa856ca663233681e789ef4aa94c44ebaf"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa893799f48b30c438349335556a0e15b6"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa8b84c64da5b8c5f5d99b86c1cfe09ffc"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa8f933f0f6e5a1a3c3cdc1819ffcdce63"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa90f2c51ad42e335a474061c4d5e4e5a9"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa932c610512cc99157654c3997bc2b922"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa9642163abbbad8aa5c7088c8529aadd7"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa9ce331f5f41ba3e3e05f485bc2d4138e"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa9e2597c2a109abda1c63c8d5ca5376b3"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa9f26dd9d2aaa5d328481715764dbb1b9"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfa9f3b8bb63f6628db9a1678b72ec12b6d"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaa59864204064d3e8fac5271b69a7da23"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaa5cd01ad23ede98de1ae176920b8fc8f"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaa81aa5b3424f02fdf02295de47b11b19"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaa9956a2b95afe1a05fda65db5cc66467"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfab3c7c9f3a73e83623c651cdfddddeb05"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfab44ba4426c1574f4b296794b7bfe2172"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfab4d202043e8b0b7a8c2d4c519fd1eb07"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfab5b923992d0bdc176f716cd8ace3a66e"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfabb0b25fe8c201dc75b72c7b078f745d6"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfabc172093417a4c40a7443eee551e9700"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfabc92147e725c8108c18f4e03005afbdc"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfac232473666b21ca772c84b68be6c1f3d"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfac2c4a3aec85b4d8171de4429ccabbe19"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfac8d82858905175ba79c24b0be1b1b1a8"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaca0480331288d15eccec9f072f123817"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfacc002ca9f0f3bdc01b4de42d00e5560b"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bface8d41615c6afd45724f4b6d16238c36"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bface9e8d409d981f193f69fc5b29f38ca7"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfad8884ef7e77722099e6bd61265f6564c"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfadd7c795e2c9c212a4adeaba904bda447"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfadf81a88f3f92f15e2abec83911bf3732"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfae16b76c1bf9f7aa58a1b1c556a6b6022"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfae16bd57629c7aba96a554d0446e83d98"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfae5405b62cb20962cb5864ba6e90a4ab2"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfae6a84e8474b6c3e8f9f7d344408cfa0b"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfae8f5051cb476c3e9253b008094c431fc"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfae98dd71460def5e66fcf32e9783b96ea"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaeeab6ddad27c449cbc44ca2458912a75"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaef692bd882621d292255cb99d4697513"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaf32ab36da2e30066c9ed2816596011c8"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaf4fc3d7b4b86f9f095cec624d190ebec"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaf58d848786f8d2dfac702f7fae178311"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaf5de66adc9eb2aa183eab1e23f977894"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaf5fe431b55adf16d82604e0fc2239090"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaf7615ff4f608d64ae20a61540d939065"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaf7d3c678a8ac31916068a0c5aff54d4b"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfafcd25dc5bba218f7097698f8f49fdc45"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfafd6cf6a44966d518b173df4ed57ae720"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfafec8c71efd5ee9decd156f0d33739fbe"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaff47eb8157a7118183573e3aefb7df08"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga4f2bb15109c64695f852afd6bd99e3bfaff7192b9ddd4228e02c44b6fb2d7bf85"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga8cef56ba216d0a01c6cc89f723d1740ba6cb2e1acb52cc5bab8dd3aa6ef6ac01b"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga8cef56ba216d0a01c6cc89f723d1740ba6ea943f59b98680aefd0d5be4ef22e36"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga8cef56ba216d0a01c6cc89f723d1740baa17e5130bd8c45eb21661d8783517266"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga8cef56ba216d0a01c6cc89f723d1740bad62692e71ae45351311c8bf2ce13e3c9"></a>
<a id="agroup__usb__hid__mk__report__desc_html_gga8cef56ba216d0a01c6cc89f723d1740bafd5d599c1955bdb1c62c7b17286b37f1"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 * Copyright (c) 2018,2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_USB_CLASS_HID_H_
#define ZEPHYR_INCLUDE_USB_CLASS_HID_H_

#ifdef __cplusplus
extern "C" {
#endif



#define USB_HID_VERSION                 0x0111

#define USB_DESC_HID                    0x21
#define USB_DESC_HID_REPORT             0x22
#define USB_DESC_HID_PHYSICAL           0x23

#define USB_HID_GET_REPORT              0x01
#define USB_HID_GET_IDLE                0x02
#define USB_HID_GET_PROTOCOL            0x03
#define USB_HID_SET_REPORT              0x09
#define USB_HID_SET_IDLE                0x0A
#define USB_HID_SET_PROTOCOL            0x0B

#define HID_BOOT_IFACE_CODE_NONE        0
#define HID_BOOT_IFACE_CODE_KEYBOARD    1
#define HID_BOOT_IFACE_CODE_MOUSE       2

#define HID_PROTOCOL_BOOT               0
#define HID_PROTOCOL_REPORT             1

#define HID_ITEM_TYPE_MAIN              0x0
#define HID_ITEM_TYPE_GLOBAL            0x1
#define HID_ITEM_TYPE_LOCAL             0x2

#define HID_ITEM_TAG_INPUT              0x8
#define HID_ITEM_TAG_OUTPUT             0x9
#define HID_ITEM_TAG_COLLECTION         0xA
#define HID_ITEM_TAG_FEATURE            0xB
#define HID_ITEM_TAG_COLLECTION_END     0xC

#define HID_ITEM_TAG_USAGE_PAGE         0x0
#define HID_ITEM_TAG_LOGICAL_MIN        0x1
#define HID_ITEM_TAG_LOGICAL_MAX        0x2
#define HID_ITEM_TAG_PHYSICAL_MIN       0x3
#define HID_ITEM_TAG_PHYSICAL_MAX       0x4
#define HID_ITEM_TAG_UNIT_EXPONENT      0x5
#define HID_ITEM_TAG_UNIT               0x6
#define HID_ITEM_TAG_REPORT_SIZE        0x7
#define HID_ITEM_TAG_REPORT_ID          0x8
#define HID_ITEM_TAG_REPORT_COUNT       0x9

#define HID_ITEM_TAG_USAGE              0x0
#define HID_ITEM_TAG_USAGE_MIN          0x1
#define HID_ITEM_TAG_USAGE_MAX          0x2

#define HID_COLLECTION_PHYSICAL         0x00
#define HID_COLLECTION_APPLICATION      0x01
#define HID_COLLECTION_LOGICAL          0x02
#define HID_COLLECTION_REPORT           0x03
#define HID_COLLECTION_NAMED_ARRAY      0x04
#define HID_COLLECTION_USAGE_SWITCH     0x05
#define HID_COLLECTION_MODIFIER         0x06


/* Usage page and IDs from Universal Serial Bus HID Usage Tables */

#define HID_USAGE_GEN_DESKTOP           0x01
#define HID_USAGE_GEN_KEYBOARD          0x07
#define HID_USAGE_GEN_LEDS              0x08
#define HID_USAGE_GEN_BUTTON            0x09
#define HID_USAGE_SENSORS               0x20

#define HID_USAGE_GEN_DESKTOP_UNDEFINED 0x00
#define HID_USAGE_GEN_DESKTOP_POINTER   0x01
#define HID_USAGE_GEN_DESKTOP_MOUSE     0x02
#define HID_USAGE_GEN_DESKTOP_JOYSTICK  0x04
#define HID_USAGE_GEN_DESKTOP_GAMEPAD   0x05
#define HID_USAGE_GEN_DESKTOP_KEYBOARD  0x06
#define HID_USAGE_GEN_DESKTOP_KEYPAD    0x07
#define HID_USAGE_GEN_DESKTOP_X         0x30
#define HID_USAGE_GEN_DESKTOP_Y         0x31
#define HID_USAGE_GEN_DESKTOP_WHEEL     0x38

#define HID_USAGE_SENSOR_TYPE_COLLECTION                        0x001
#define HID_USAGE_SENSORS_TYPE_ENVIRONMENTAL_TEMPERATURE        0x033
#define HID_USAGE_SENSORS_EVENT_SENSOR_STATE                    0x201
#define HID_USAGE_SENSORS_PROPERTY_FRIENDLY_NAME                0x301
#define HID_USAGE_SENSORS_DATA_ENVIRONMENTAL_TEMPERATURE        0x434
#define HID_USAGE_SENSORS_PROPERTY_TIMESTAMP                    0x529
#define HID_USAGE_SENSORS_SENSOR_STATE_UNDEFINED                0x800
#define HID_USAGE_SENSORS_SENSOR_STATE_READY                    0x801
#define HID_USAGE_SENSORS_SENSOR_STATE_NOT_AVAILABLE            0x802
#define HID_USAGE_SENSORS_SENSOR_STATE_NO_DATA                  0x803
#define HID_USAGE_SENSORS_SENSOR_STATE_INITIALIZING             0x804
#define HID_USAGE_SENSORS_SENSOR_STATE_ACCESS_DENIED            0x805
#define HID_USAGE_SENSORS_SENSOR_STATE_ERROR                    0x806



#define HID_ITEM(bTag, bType, bSize)    (((bTag & 0xF) << 4) | \
                                         ((bType & 0x3) << 2) | (bSize & 0x3))

#define HID_INPUT(a)                    \
        HID_ITEM(HID_ITEM_TAG_INPUT, HID_ITEM_TYPE_MAIN, 1), a

#define HID_OUTPUT(a)                   \
        HID_ITEM(HID_ITEM_TAG_OUTPUT, HID_ITEM_TYPE_MAIN, 1), a

#define HID_FEATURE(a)                  \
        HID_ITEM(HID_ITEM_TAG_FEATURE, HID_ITEM_TYPE_MAIN, 1), a

#define HID_COLLECTION(a)               \
        HID_ITEM(HID_ITEM_TAG_COLLECTION, HID_ITEM_TYPE_MAIN, 1), a

#define HID_END_COLLECTION              \
        HID_ITEM(HID_ITEM_TAG_COLLECTION_END, HID_ITEM_TYPE_MAIN, 0)

#define HID_USAGE_PAGE(page)            \
        HID_ITEM(HID_ITEM_TAG_USAGE_PAGE, HID_ITEM_TYPE_GLOBAL, 1), page

#define HID_USAGE_PAGE16(page)          \
        HID_ITEM(HID_ITEM_TAG_USAGE_PAGE, HID_ITEM_TYPE_GLOBAL, 2), (uint8_t)page, (page >> 8)

#define HID_LOGICAL_MIN8(a)             \
        HID_ITEM(HID_ITEM_TAG_LOGICAL_MIN, HID_ITEM_TYPE_GLOBAL, 1), a

#define HID_LOGICAL_MAX8(a)             \
        HID_ITEM(HID_ITEM_TAG_LOGICAL_MAX, HID_ITEM_TYPE_GLOBAL, 1), a

#define HID_LOGICAL_MIN16(a, b)         \
        HID_ITEM(HID_ITEM_TAG_LOGICAL_MIN, HID_ITEM_TYPE_GLOBAL, 2), a, b

#define HID_LOGICAL_MAX16(a, b)         \
        HID_ITEM(HID_ITEM_TAG_LOGICAL_MAX, HID_ITEM_TYPE_GLOBAL, 2), a, b

#define HID_LOGICAL_MIN32(a, b, c, d)   \
        HID_ITEM(HID_ITEM_TAG_LOGICAL_MIN, HID_ITEM_TYPE_GLOBAL, 3), a, b, c, d

#define HID_LOGICAL_MAX32(a, b, c, d)   \
        HID_ITEM(HID_ITEM_TAG_LOGICAL_MAX, HID_ITEM_TYPE_GLOBAL, 3), a, b, c, d

#define HID_REPORT_SIZE(size)           \
        HID_ITEM(HID_ITEM_TAG_REPORT_SIZE, HID_ITEM_TYPE_GLOBAL, 1), size

#define HID_REPORT_ID(id)               \
        HID_ITEM(HID_ITEM_TAG_REPORT_ID, HID_ITEM_TYPE_GLOBAL, 1), id

#define HID_REPORT_COUNT(count)         \
        HID_ITEM(HID_ITEM_TAG_REPORT_COUNT, HID_ITEM_TYPE_GLOBAL, 1), count

#define HID_USAGE(idx)                  \
        HID_ITEM(HID_ITEM_TAG_USAGE, HID_ITEM_TYPE_LOCAL, 1), idx

#define HID_USAGE16(idx)                \
        HID_ITEM(HID_ITEM_TAG_USAGE, HID_ITEM_TYPE_LOCAL, 2), (uint8_t)idx, (idx >> 8)

#define HID_USAGE_MIN8(a)               \
        HID_ITEM(HID_ITEM_TAG_USAGE_MIN, HID_ITEM_TYPE_LOCAL, 1), a

#define HID_USAGE_MAX8(a)               \
        HID_ITEM(HID_ITEM_TAG_USAGE_MAX, HID_ITEM_TYPE_LOCAL, 1), a

#define HID_USAGE_MIN16(a, b)           \
        HID_ITEM(HID_ITEM_TAG_USAGE_MIN, HID_ITEM_TYPE_LOCAL, 2), a, b

#define HID_USAGE_MAX16(a, b)           \
        HID_ITEM(HID_ITEM_TAG_USAGE_MAX, HID_ITEM_TYPE_LOCAL, 2), a, b

#define HID_UNIT_EXPONENT(exp) HID_ITEM(HID_ITEM_TAG_UNIT_EXPONENT, HID_ITEM_TYPE_GLOBAL, 1), exp



#define HID_MOUSE_REPORT_DESC(bcnt) {                           \
        HID_USAGE_PAGE(HID_USAGE_GEN_DESKTOP),                  \
        HID_USAGE(HID_USAGE_GEN_DESKTOP_MOUSE),                 \
        HID_COLLECTION(HID_COLLECTION_APPLICATION),             \
                HID_USAGE(HID_USAGE_GEN_DESKTOP_POINTER),       \
                HID_COLLECTION(HID_COLLECTION_PHYSICAL),        \
                        /* Bits used for button signalling */   \
                        HID_USAGE_PAGE(HID_USAGE_GEN_BUTTON),   \
                        HID_USAGE_MIN8(1),                      \
                        HID_USAGE_MAX8(bcnt),                   \
                        HID_LOGICAL_MIN8(0),                    \
                        HID_LOGICAL_MAX8(1),                    \
                        HID_REPORT_SIZE(1),                     \
                        HID_REPORT_COUNT(bcnt),                 \
                        /* HID_INPUT (Data,Var,Abs) */          \
                        HID_INPUT(0x02),                        \
                        /* Unused bits */                       \
                        HID_REPORT_SIZE(8 - bcnt),              \
                        HID_REPORT_COUNT(1),                    \
                        /* HID_INPUT (Cnst,Ary,Abs) */          \
                        HID_INPUT(1),                           \
                        /* X and Y axis, scroll */              \
                        HID_USAGE_PAGE(HID_USAGE_GEN_DESKTOP),  \
                        HID_USAGE(HID_USAGE_GEN_DESKTOP_X),     \
                        HID_USAGE(HID_USAGE_GEN_DESKTOP_Y),     \
                        HID_USAGE(HID_USAGE_GEN_DESKTOP_WHEEL), \
                        HID_LOGICAL_MIN8(-127),                 \
                        HID_LOGICAL_MAX8(127),                  \
                        HID_REPORT_SIZE(8),                     \
                        HID_REPORT_COUNT(3),                    \
                        /* HID_INPUT (Data,Var,Rel) */          \
                        HID_INPUT(0x06),                        \
                HID_END_COLLECTION,                             \
        HID_END_COLLECTION,                                     \
}

#define HID_KEYBOARD_REPORT_DESC() {                            \
        HID_USAGE_PAGE(HID_USAGE_GEN_DESKTOP),                  \
        HID_USAGE(HID_USAGE_GEN_DESKTOP_KEYBOARD),              \
        HID_COLLECTION(HID_COLLECTION_APPLICATION),             \
                HID_USAGE_PAGE(HID_USAGE_GEN_DESKTOP_KEYPAD),   \
                /* HID_USAGE_MINIMUM(Keyboard LeftControl) */   \
                HID_USAGE_MIN8(0xE0),                           \
                /* HID_USAGE_MAXIMUM(Keyboard Right GUI) */     \
                HID_USAGE_MAX8(0xE7),                           \
                HID_LOGICAL_MIN8(0),                            \
                HID_LOGICAL_MAX8(1),                            \
                HID_REPORT_SIZE(1),                             \
                HID_REPORT_COUNT(8),                            \
                /* HID_INPUT(Data,Var,Abs) */                   \
                HID_INPUT(0x02),                                \
                HID_REPORT_SIZE(8),                             \
                HID_REPORT_COUNT(1),                            \
                /* HID_INPUT(Cnst,Var,Abs) */                   \
                HID_INPUT(0x03),                                \
                HID_REPORT_SIZE(1),                             \
                HID_REPORT_COUNT(5),                            \
                HID_USAGE_PAGE(HID_USAGE_GEN_LEDS),             \
                /* HID_USAGE_MINIMUM(Num Lock) */               \
                HID_USAGE_MIN8(1),                              \
                /* HID_USAGE_MAXIMUM(Kana) */                   \
                HID_USAGE_MAX8(5),                              \
                /* HID_OUTPUT(Data,Var,Abs) */                  \
                HID_OUTPUT(0x02),                               \
                HID_REPORT_SIZE(3),                             \
                HID_REPORT_COUNT(1),                            \
                /* HID_OUTPUT(Cnst,Var,Abs) */                  \
                HID_OUTPUT(0x03),                               \
                HID_REPORT_SIZE(8),                             \
                HID_REPORT_COUNT(6),                            \
                HID_LOGICAL_MIN8(0),                            \
                HID_LOGICAL_MAX8(101),                          \
                HID_USAGE_PAGE(HID_USAGE_GEN_DESKTOP_KEYPAD),   \
                /* HID_USAGE_MIN8(Reserved) */                  \
                HID_USAGE_MIN8(0),                              \
                /* HID_USAGE_MAX8(Keyboard Application) */      \
                HID_USAGE_MAX8(101),                            \
                /* HID_INPUT (Data,Ary,Abs) */                  \
                HID_INPUT(0x00),                                \
        HID_END_COLLECTION,                                     \
}

enum hid_kbd_code {
        HID_KEY_A               = 4,
        HID_KEY_B               = 5,
        HID_KEY_C               = 6,
        HID_KEY_D               = 7,
        HID_KEY_E               = 8,
        HID_KEY_F               = 9,
        HID_KEY_G               = 10,
        HID_KEY_H               = 11,
        HID_KEY_I               = 12,
        HID_KEY_J               = 13,
        HID_KEY_K               = 14,
        HID_KEY_L               = 15,
        HID_KEY_M               = 16,
        HID_KEY_N               = 17,
        HID_KEY_O               = 18,
        HID_KEY_P               = 19,
        HID_KEY_Q               = 20,
        HID_KEY_R               = 21,
        HID_KEY_S               = 22,
        HID_KEY_T               = 23,
        HID_KEY_U               = 24,
        HID_KEY_V               = 25,
        HID_KEY_W               = 26,
        HID_KEY_X               = 27,
        HID_KEY_Y               = 28,
        HID_KEY_Z               = 29,
        HID_KEY_1               = 30,
        HID_KEY_2               = 31,
        HID_KEY_3               = 32,
        HID_KEY_4               = 33,
        HID_KEY_5               = 34,
        HID_KEY_6               = 35,
        HID_KEY_7               = 36,
        HID_KEY_8               = 37,
        HID_KEY_9               = 38,
        HID_KEY_0               = 39,
        HID_KEY_ENTER           = 40,
        HID_KEY_ESC             = 41,
        HID_KEY_BACKSPACE       = 42,
        HID_KEY_TAB             = 43,
        HID_KEY_SPACE           = 44,
        HID_KEY_MINUS           = 45,
        HID_KEY_EQUAL           = 46,
        HID_KEY_LEFTBRACE       = 47,
        HID_KEY_RIGHTBRACE      = 48,
        HID_KEY_BACKSLASH       = 49,
        HID_KEY_HASH            = 50, /* Non-US # and ~ */
        HID_KEY_SEMICOLON       = 51,
        HID_KEY_APOSTROPHE      = 52,
        HID_KEY_GRAVE           = 53,
        HID_KEY_COMMA           = 54,
        HID_KEY_DOT             = 55,
        HID_KEY_SLASH           = 56,
        HID_KEY_CAPSLOCK        = 57,
        HID_KEY_F1              = 58,
        HID_KEY_F2              = 59,
        HID_KEY_F3              = 60,
        HID_KEY_F4              = 61,
        HID_KEY_F5              = 62,
        HID_KEY_F6              = 63,
        HID_KEY_F7              = 64,
        HID_KEY_F8              = 65,
        HID_KEY_F9              = 66,
        HID_KEY_F10             = 67,
        HID_KEY_F11             = 68,
        HID_KEY_F12             = 69,
        HID_KEY_SYSRQ           = 70, /* PRINTSCREEN */
        HID_KEY_SCROLLLOCK      = 71,
        HID_KEY_PAUSE           = 72,
        HID_KEY_INSERT          = 73,
        HID_KEY_HOME            = 74,
        HID_KEY_PAGEUP          = 75,
        HID_KEY_DELETE          = 76,
        HID_KEY_END             = 77,
        HID_KEY_PAGEDOWN        = 78,
        HID_KEY_RIGHT           = 79,
        HID_KEY_LEFT            = 80,
        HID_KEY_DOWN            = 81,
        HID_KEY_UP              = 82,
        HID_KEY_NUMLOCK         = 83,
        HID_KEY_KPSLASH         = 84, /* NUMPAD DIVIDE */
        HID_KEY_KPASTERISK      = 85, /* NUMPAD MULTIPLY */
        HID_KEY_KPMINUS         = 86,
        HID_KEY_KPPLUS          = 87,
        HID_KEY_KPENTER         = 88,
        HID_KEY_KP_1            = 89,
        HID_KEY_KP_2            = 90,
        HID_KEY_KP_3            = 91,
        HID_KEY_KP_4            = 92,
        HID_KEY_KP_5            = 93,
        HID_KEY_KP_6            = 94,
        HID_KEY_KP_7            = 95,
        HID_KEY_KP_8            = 96,
        HID_KEY_KP_9            = 97,
        HID_KEY_KP_0            = 98,
        HID_KEY_KPDOT           = 99,
        HID_KEY_MENU            = 101,
};

enum hid_kbd_modifier {
        HID_KBD_MODIFIER_NONE           = 0x00,
        HID_KBD_MODIFIER_LEFT_CTRL      = 0x01,
        HID_KBD_MODIFIER_LEFT_SHIFT     = 0x02,
        HID_KBD_MODIFIER_LEFT_ALT       = 0x04,
        HID_KBD_MODIFIER_LEFT_UI        = 0x08,
        HID_KBD_MODIFIER_RIGHT_CTRL     = 0x10,
        HID_KBD_MODIFIER_RIGHT_SHIFT    = 0x20,
        HID_KBD_MODIFIER_RIGHT_ALT      = 0x40,
        HID_KBD_MODIFIER_RIGHT_UI       = 0x80,
};

enum hid_kbd_led {
        HID_KBD_LED_NUM_LOCK    = 0x01,
        HID_KBD_LED_CAPS_LOCK   = 0x02,
        HID_KBD_LED_SCROLL_LOCK = 0x04,
        HID_KBD_LED_COMPOSE     = 0x08,
        HID_KBD_LED_KANA        = 0x10,
};



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_USB_CLASS_HID_H_ */
```

## 9.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

版权（Copyright）：© 2018,2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 134 行

通用串行总线（USB）HID 用法表（Usage Tables）中的用法页（Usage Page）及标识。

### 注释 3：原第 492 行

用于按钮信号（Button Signalling）的位。

### 注释 4：原第 500 行

`HID_INPUT (Data,Var,Abs)`：输入项，数据（Data）、变量（Variable）、绝对值（Absolute）。

### 注释 5：原第 502 行

未使用的位（Unused Bits）。

### 注释 6：原第 505 行

`HID_INPUT (Cnst,Ary,Abs)`：输入项，常量（Constant）、数组（Array）、绝对值（Absolute）。

### 注释 7：原第 507 行

X 轴、Y 轴及滚动（Scroll）。

### 注释 8：原第 516 行

`HID_INPUT (Data,Var,Rel)`：输入项，数据（Data）、变量（Variable）、相对值（Relative）。

### 注释 9：原第 530 行

`HID_USAGE_MINIMUM(Keyboard LeftControl)`：最小用法为键盘左 Control 键。

### 注释 10：原第 532 行

`HID_USAGE_MAXIMUM(Keyboard Right GUI)`：最大用法为键盘右 GUI 键。

### 注释 11：原第 538 行

`HID_INPUT(Data,Var,Abs)`：输入项，数据（Data）、变量（Variable）、绝对值（Absolute）。

### 注释 12：原第 542 行

`HID_INPUT(Cnst,Var,Abs)`：输入项，常量（Constant）、变量（Variable）、绝对值（Absolute）。

### 注释 13：原第 547 行

`HID_USAGE_MINIMUM(Num Lock)`：最小用法为数字锁定（Num Lock）。

### 注释 14：原第 549 行

`HID_USAGE_MAXIMUM(Kana)`：最大用法为假名（Kana）。

### 注释 15：原第 551 行

`HID_OUTPUT(Data,Var,Abs)`：输出项，数据（Data）、变量（Variable）、绝对值（Absolute）。

### 注释 16：原第 555 行

`HID_OUTPUT(Cnst,Var,Abs)`：输出项，常量（Constant）、变量（Variable）、绝对值（Absolute）。

### 注释 17：原第 562 行

`HID_USAGE_MIN8(Reserved)`：8 位最小用法为保留值（Reserved）。

### 注释 18：原第 564 行

`HID_USAGE_MAX8(Keyboard Application)`：8 位最大用法为键盘应用程序键（Keyboard Application）。

### 注释 19：原第 566 行

`HID_INPUT (Data,Ary,Abs)`：输入项，数据（Data）、数组（Array）、绝对值（Absolute）。

### 注释 20：原第 621 行

非美式键盘的 `#` 和 `~`（Non-US # and ~）。

### 注释 21：原第 641 行

打印屏幕键（Print Screen）。

### 注释 22：原第 655 行

数字小键盘除号键（Numpad Divide）。

### 注释 23：原第 656 行

数字小键盘乘号键（Numpad Multiply）。

### 注释 24：原第 712 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_USB_CLASS_HID_H_`。

## 9.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usb_2class_2hid_8h.html)
- [hid_kbd_code](../usb/P050_HID报告描述符构造宏.md#ga4f2bb15109c64695f852afd6bd99e3bf)
- [HID_KEY_A](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5413afa6a28a21dd52f07db101f2d139)
- [HID_KEY_B](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfabb0b25fe8c201dc75b72c7b078f745d6)
- [HID_KEY_C](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa932c610512cc99157654c3997bc2b922)
- [HID_KEY_D](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfabc172093417a4c40a7443eee551e9700)
- [HID_KEY_E](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaff7192b9ddd4228e02c44b6fb2d7bf85)
- [HID_KEY_F](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfacc002ca9f0f3bdc01b4de42d00e5560b)
- [HID_KEY_G](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1eadd56346bbd64b1c33fa5393f65bda)
- [HID_KEY_H](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4bfc341fccde664ec9267af6e705ba0c)
- [HID_KEY_I](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfafcd25dc5bba218f7097698f8f49fdc45)
- [HID_KEY_J](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa2a78196208c634941d63429cd1e1df7a)
- [HID_KEY_K](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ceddaaaa90d84f0afb3e1ee9a35a976)
- [HID_KEY_L](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5de66adc9eb2aa183eab1e23f977894)
- [HID_KEY_M](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4f8174feca1eb72901576c4e24c8f8a9)
- [HID_KEY_N](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab4d202043e8b0b7a8c2d4c519fd1eb07)
- [HID_KEY_O](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfad8884ef7e77722099e6bd61265f6564c)
- [HID_KEY_P](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaca0480331288d15eccec9f072f123817)
- [HID_KEY_Q](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa05fb920f8129f57dd350036f17fbe519)
- [HID_KEY_R](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa037de00c763ae6b270895b7a5f0f57a7)
- [HID_KEY_S](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae6a84e8474b6c3e8f9f7d344408cfa0b)
- [HID_KEY_T](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa893799f48b30c438349335556a0e15b6)
- [HID_KEY_U](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab3c7c9f3a73e83623c651cdfddddeb05)
- [HID_KEY_V](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa02f14e6303b4d2e4e46747324d649dda)
- [HID_KEY_W](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfadf81a88f3f92f15e2abec83911bf3732)
- [HID_KEY_X](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9f3b8bb63f6628db9a1678b72ec12b6d)
- [HID_KEY_Y](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ca2ebe26c09f2400a8ebc0aa445ce89)
- [HID_KEY_Z](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa5cd01ad23ede98de1ae176920b8fc8f)
- [HID_KEY_1](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa039ced168420140b97e2d0676e1bb12a)
- [HID_KEY_2](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae98dd71460def5e66fcf32e9783b96ea)
- [HID_KEY_3](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf58d848786f8d2dfac702f7fae178311)
- [HID_KEY_4](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa17019d72e84302486f72f7d8101baca5)
- [HID_KEY_5](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf32ab36da2e30066c9ed2816596011c8)
- [HID_KEY_6](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae16b76c1bf9f7aa58a1b1c556a6b6022)
- [HID_KEY_7](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5887a1854f7d0787121bd75034cdd726)
- [HID_KEY_8](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1761228849d7dc2b84d0565d3337b2e2)
- [HID_KEY_9](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa758aec2540a6a2153702d6905c44ce52)
- [HID_KEY_0](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa856ca663233681e789ef4aa94c44ebaf)
- [HID_KEY_ENTER](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaeeab6ddad27c449cbc44ca2458912a75)
- [HID_KEY_ESC](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa763b39fe76a92c4cc1fc32f47d2a760a)
- [HID_KEY_BACKSPACE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfafd6cf6a44966d518b173df4ed57ae720)
- [HID_KEY_TAB](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a6c79e8ea85f6593c06d19098d69a03)
- [HID_KEY_SPACE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf4fc3d7b4b86f9f095cec624d190ebec)
- [HID_KEY_MINUS](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa59864204064d3e8fac5271b69a7da23)
- [HID_KEY_EQUAL](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfac8d82858905175ba79c24b0be1b1b1a8)
- [HID_KEY_LEFTBRACE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfac232473666b21ca772c84b68be6c1f3d)
- [HID_KEY_RIGHTBRACE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaef692bd882621d292255cb99d4697513)
- [HID_KEY_BACKSLASH](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa25ba5457bc128593b1624d95ec536182)
- [HID_KEY_HASH](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa0d57ce7c99d06ee9b15fef880af075eb)
- [HID_KEY_SEMICOLON](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa3743f920856a12e726e1be05932c7411)
- [HID_KEY_APOSTROPHE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa7325a5bd52e9dc0cc38a85609b1c55ab)
- [HID_KEY_GRAVE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa8b84c64da5b8c5f5d99b86c1cfe09ffc)
- [HID_KEY_COMMA](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa81aa5b3424f02fdf02295de47b11b19)
- [HID_KEY_DOT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa403fe927ebb0014e2c1b3dc25e1d9779)
- [HID_KEY_SLASH](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa24c2c93a1c895745828311affc011dea)
- [HID_KEY_CAPSLOCK](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4d40549a59fdcfdd0b2d592a6675bc89)
- [HID_KEY_F1](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9642163abbbad8aa5c7088c8529aadd7)
- [HID_KEY_F2](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9ce331f5f41ba3e3e05f485bc2d4138e)
- [HID_KEY_F3](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa76adde1d9295cf62e7efb35e27911a1e)
- [HID_KEY_F4](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaa9956a2b95afe1a05fda65db5cc66467)
- [HID_KEY_F5](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bface9e8d409d981f193f69fc5b29f38ca7)
- [HID_KEY_F6](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfabc92147e725c8108c18f4e03005afbdc)
- [HID_KEY_F7](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e2eabf8b9fa6cbfea613696b2c4122a)
- [HID_KEY_F8](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5092add2863231d273ba60cd583ebe33)
- [HID_KEY_F9](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5a09deabde1a3a44378b7de44dad27b6)
- [HID_KEY_F10](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfac2c4a3aec85b4d8171de4429ccabbe19)
- [HID_KEY_F11](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa76bb35a0f71733b0a0f1bd7e3837064c)
- [HID_KEY_F12](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab44ba4426c1574f4b296794b7bfe2172)
- [HID_KEY_SYSRQ](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae5405b62cb20962cb5864ba6e90a4ab2)
- [HID_KEY_SCROLLLOCK](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae16bd57629c7aba96a554d0446e83d98)
- [HID_KEY_PAUSE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1905733a0fe81f78e0752e3b0bb99c69)
- [HID_KEY_INSERT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e1c320cea0644c3dc38da06c865837b)
- [HID_KEY_HOME](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa5fc1127fe9014018f4831cbf272c883b)
- [HID_KEY_PAGEUP](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa2468ac3b37d38b6158cd989ed54bcd8c)
- [HID_KEY_DELETE](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfae8f5051cb476c3e9253b008094c431fc)
- [HID_KEY_END](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa8f933f0f6e5a1a3c3cdc1819ffcdce63)
- [HID_KEY_PAGEDOWN](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7615ff4f608d64ae20a61540d939065)
- [HID_KEY_RIGHT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4c203feb452e3212089e8246b8d75f6c)
- [HID_KEY_LEFT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf7d3c678a8ac31916068a0c5aff54d4b)
- [HID_KEY_DOWN](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9e2597c2a109abda1c63c8d5ca5376b3)
- [HID_KEY_UP](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaf5fe431b55adf16d82604e0fc2239090)
- [HID_KEY_NUMLOCK](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfafec8c71efd5ee9decd156f0d33739fbe)
- [HID_KEY_KPSLASH](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa44e83040efab214dcfe462ac0d338e0c)
- [HID_KEY_KPASTERISK](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfaff47eb8157a7118183573e3aefb7df08)
- [HID_KEY_KPMINUS](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa6fb35c78b12ae434cb7a7280501886e9)
- [HID_KEY_KPPLUS](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa2cb7852467d2ebd785e2f7556383a883)
- [HID_KEY_KPENTER](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfab5b923992d0bdc176f716cd8ace3a66e)
- [HID_KEY_KP_1](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa7eea75b0eb4b4f0306daa3e6fccf09e4)
- [HID_KEY_KP_2](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa68db65e7002e7cc599394a7eea116e3c)
- [HID_KEY_KP_3](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4210f9a5ae469c8b863b28b9b2d8189d)
- [HID_KEY_KP_4](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa48eefeeb48a942eaaa0726bd4a2df01d)
- [HID_KEY_KP_5](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1b8d299d56a0289ae15cbf8c67e36a7c)
- [HID_KEY_KP_6](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa90f2c51ad42e335a474061c4d5e4e5a9)
- [HID_KEY_KP_7](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa1e191017084fadf830a7394de0e1cc05)
- [HID_KEY_KP_8](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfadd7c795e2c9c212a4adeaba904bda447)
- [HID_KEY_KP_9](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bface8d41615c6afd45724f4b6d16238c36)
- [HID_KEY_KP_0](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4ae4af2b06f6f2585a598353bfef9af7)
- [HID_KEY_KPDOT](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa9f26dd9d2aaa5d328481715764dbb1b9)
- [HID_KEY_MENU](../usb/P050_HID报告描述符构造宏.md#gga4f2bb15109c64695f852afd6bd99e3bfa4b07b1bbe7695f2f67ce9df298c1d3c7)
- [hid_kbd_modifier](../usb/P050_HID报告描述符构造宏.md#ga12f11556b697518b00fa86eb040f9eb8)
- [HID_KBD_MODIFIER_NONE](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a79b0eb4f485bedb745180f1b8798c603)
- [HID_KBD_MODIFIER_LEFT_CTRL](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a4df663509a05599fd66657cfc90a37c7)
- [HID_KBD_MODIFIER_LEFT_SHIFT](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8aba69ca183306d3d1427b66666803e57f)
- [HID_KBD_MODIFIER_LEFT_ALT](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a829d884291b546c0e276afa4ad92ac18)
- [HID_KBD_MODIFIER_LEFT_UI](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a718c92a2d0ca9dd6603825b97a99fc77)
- [HID_KBD_MODIFIER_RIGHT_CTRL](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a8e346c0e9c7d5b58e4b8748380423a92)
- [HID_KBD_MODIFIER_RIGHT_SHIFT](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8affdba298e8860b000a0916be7495c2dc)
- [HID_KBD_MODIFIER_RIGHT_ALT](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a85ce29a6ab9feef68350deca92001db2)
- [HID_KBD_MODIFIER_RIGHT_UI](../usb/P050_HID报告描述符构造宏.md#gga12f11556b697518b00fa86eb040f9eb8a1b4b75cd0364824cbfc80dfc68e294dd)
- [hid_kbd_led](../usb/P050_HID报告描述符构造宏.md#ga8cef56ba216d0a01c6cc89f723d1740b)
- [HID_KBD_LED_NUM_LOCK](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740ba6cb2e1acb52cc5bab8dd3aa6ef6ac01b)
- [HID_KBD_LED_CAPS_LOCK](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740baa17e5130bd8c45eb21661d8783517266)
- [HID_KBD_LED_SCROLL_LOCK](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740ba6ea943f59b98680aefd0d5be4ef22e36)
- [HID_KBD_LED_COMPOSE](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740bad62692e71ae45351311c8bf2ce13e3c9)
- [HID_KBD_LED_KANA](../usb/P050_HID报告描述符构造宏.md#gga8cef56ba216d0a01c6cc89f723d1740bafd5d599c1955bdb1c62c7b17286b37f1)

---

[上一章](P008_sip_svc_controller.h_源码浏览.md) · [返回大纲](大纲.md)
