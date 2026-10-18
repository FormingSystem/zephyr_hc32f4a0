---
id: learning.zephyr-docs.api-source-reference.page-262
title: fido2_types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第262章\_fido2\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html)。

## 262.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="foldopen00089"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="foldopen00139"></a>
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
<a id="foldopen00191"></a>
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
<a id="foldopen00203"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="foldopen00213"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="foldopen00221"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00241"></a>
<a id="l00243"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="foldopen00257"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00275"></a>
<a id="l00277"></a>
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
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00292"></a>
<a id="l00294"></a>
<a id="l00296"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca020a5895146a35c2dedace5e0ff96112"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05bb5e1370a3e46ef1a2f2545cf5675c"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05c0bff840ed8b7e85c147876792760f"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca0ca1a5d18e501d446c58ddcc4f8fbc05"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca128911647928193e076041834e398e75"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca17c4a70a8f87425c4d849585d28280d4"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca1ece48887496a5962823530201eaf48c"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca336c3e439e0a1b3eb24cf3edc38455e1"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca3521d75934cddcd0d009279541381c41"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca356a92621e9d79fd5d599f1c13a7da93"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca376b899ff97c4d39f201f20e03a36ed7"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca39355da927952f311dd8cdf9fe5cced8"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca43b6e71c8f000bb2eccfc8a45c4591d3"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca4c53af9f0ad3e857bf86efea60b9370f"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca507f5ded749fdba95d6b16d859052d43"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca53aa4e296d54d24d7aab0bfc7747d893"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca57a9754a770796bdb303ec5503222060"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5c952ab01843550e24d3aa672f05fec9"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5dfe38f41a7863bc04928d7c566568b7"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca620c7a76e1481401e9dce1a5a75c8ee8"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca63548371fe576d03e00a2d428bf2501b"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca69c9ebc7f40bcc26641eaa910a84f7e4"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca6eb4c3a5f51db1d0232ef8ca21d194e6"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca739a74cd005fc1b3b8853f7aa2db7e3e"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca809431ef12cd0ba7094a80c39d6bdc2d"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8406e112b928b9f556cced2f0c391cfe"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8d108ee70faea78aa0669a90081dd05c"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fca935a727495553c4bf584a92c39d780b7"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa08efc6dee799b3e1fb8490bc64bd1cf"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa28ed4a202b7c8eca14a727b708b0d50"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaad5b849ccb37209d531444bb346e3158"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab263ae4a933b875d54a86d4a6da8dc4e"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab4382a900e27d13b5043241f2f6dc2fe"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab52bc5933983ff9464292f4a470e0217"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab59eee02a04da8ca4bf54ceba81794d0"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcabe9d8c984a0c0a62616a4a94af655a78"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac36b384a558597d72980f2425008c7b6"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac804a5a070c6552d89d403ffc953c00d"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacb6d4da143bbd72b7d361a7a4e38b1da"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacbaf6656b7eac960f4bc0e561de47011"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacc4208f8ab39ba6b67c9358df6b88797"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacf7163e857eb9b8b6ddef1e7ff2b7351"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcad19e5127b17b8e0abee8bfe7d1ae595f"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaeb3d5db8b9e7ad3123df8d2a76ed4bfe"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaee29e086a2af8e697b6467c9667cb327"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaf713403e6582ce02cace5d29f45405af"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcafcbd15f2df2744ed0afd3613540ad6a3"></a>
<a id="afido2__types_8h_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaffdba1168067976851629c2111f46f6a"></a>
<a id="afido2__types_8h_html_ga86aa0e78a95ea9e399c3831348fe8684a21d965a84070571fb2e0d475cf27043d"></a>
<a id="afido2__types_8h_html_ga86aa0e78a95ea9e399c3831348fe8684a386cd8a5baf42b49b2271d655645b103"></a>
<a id="afido2__types_8h_html_ga86aa0e78a95ea9e399c3831348fe8684a94ae94ce511d5898c12059766adf95c3"></a>
<a id="afido2__types_8h_html_ga86aa0e78a95ea9e399c3831348fe8684ad2a327ca6649f0abd4153dee72952167"></a>
<a id="afido2__types_8h_html_gae9411b5f6c2596cf49f7ebcf04fd7955a07603aa0b0598319d504ca9e23e76078"></a>
<a id="afido2__types_8h_html_gae9411b5f6c2596cf49f7ebcf04fd7955a2299549abdae08cd0e71c7db3d918ca6"></a>
<a id="afido2__types_8h_html_gae9411b5f6c2596cf49f7ebcf04fd7955aef0d3d870129fc9e72138d309c641be6"></a>
<a id="afido2__types_8h_html_gaec9e2106f2d776266909f5e2baf924d9a2419f886d7fcfe8e4e77a4b5f21d5bfc"></a>
<a id="afido2__types_8h_html_gaec9e2106f2d776266909f5e2baf924d9a327a6fbfb22651dfed6d1d1ded574ab7"></a>
<a id="afido2__types_8h_html_gaec9e2106f2d776266909f5e2baf924d9a4984d83c6210b1855106ff39b413e614"></a>
<a id="afido2__types_8h_html_gaec9e2106f2d776266909f5e2baf924d9a64758dfc5b08bccc58369e97ecd8eae0"></a>
<a id="afido2__types_8h_html_gaec9e2106f2d776266909f5e2baf924d9a6b7d85b947ad93ab5159ffe7f2934948"></a>
<a id="afido2__types_8h_html_gaec9e2106f2d776266909f5e2baf924d9aacffe603fa91c1102164c1d022bcd678"></a>
<a id="afido2__types_8h_html_gaec9e2106f2d776266909f5e2baf924d9aca44c6fcf4ff9f7d43693607a4ea178a"></a>
<a id="afido2__types_8h_html_gaec9e2106f2d776266909f5e2baf924d9adc26ad4d923d58ca0f33d63c9dae1c27"></a>
<a id="agroup__fido2_html_ga15f94b65bca9940f1a535e6ec1339fdf"></a>
<a id="agroup__fido2_html_ga57628d326e2f62b318908af69485dbb8"></a>
<a id="agroup__fido2_html_ga6060501b6c00b076fc705276464050ab"></a>
<a id="agroup__fido2_html_ga624b79a13eb53f43594b5c24332725fa"></a>
<a id="agroup__fido2_html_ga6b3b79c7ef54b3ebbe686d4f67aaf7fc"></a>
<a id="agroup__fido2_html_ga7fe764c73ecb327210eb080aa5b32a92"></a>
<a id="agroup__fido2_html_ga7ff8f1d8d389b44e2a656b3ebe20f778"></a>
<a id="agroup__fido2_html_ga86aa0e78a95ea9e399c3831348fe8684"></a>
<a id="agroup__fido2_html_ga99da0bebb5865edd2e163a31da966618"></a>
<a id="agroup__fido2_html_gaa4111c61a7446d3cb5efa41bf492d930"></a>
<a id="agroup__fido2_html_gae9411b5f6c2596cf49f7ebcf04fd7955"></a>
<a id="agroup__fido2_html_gaead02ba380ab3899742dfbf41edc4a98"></a>
<a id="agroup__fido2_html_gaec9e2106f2d776266909f5e2baf924d9"></a>
<a id="agroup__fido2_html_gaf5eb8fcafd96dd1d3eec5424aff9748c"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructfido2__credential_html"></a>
<a id="astructfido2__credential_html_a0d3ac4d5515fae39f06c13c37aa385f7"></a>
<a id="astructfido2__credential_html_a194b53ed392542e1214e4289fe76d033"></a>
<a id="astructfido2__credential_html_a1dde5d1541f18260df49175047c883df"></a>
<a id="astructfido2__credential_html_a2a097ffa153fc969e73850627654c97f"></a>
<a id="astructfido2__credential_html_a5472886ee94fd507f4facf8681b62882"></a>
<a id="astructfido2__credential_html_a6a0e84bb3432eaccdd85a7b9d72ed91d"></a>
<a id="astructfido2__credential_html_a71a46e60f2e8204a83aaecd2dfb44e40"></a>
<a id="astructfido2__credential_html_a7b7c2b9ba8ea5dea3428132e5e0462b7"></a>
<a id="astructfido2__credential_html_a8951d380f675d378e7fcb584f87561cd"></a>
<a id="astructfido2__credential_html_aad709e654b5a0ebb6a2ee7d1a1e1c6a2"></a>
<a id="astructfido2__credential_html_aaf5c0b6a289e51c49e5c9e065fb28a7a"></a>
<a id="astructfido2__credential_html_ae95bda862fcc760ffa5d723dfb3ff8aa"></a>
<a id="astructfido2__credential_html_af2e3794720dbad041de08aaba6dbd925"></a>
<a id="astructfido2__credential_html_af523edcf94f7a9f9cbbd7ea87bbe673a"></a>
<a id="astructfido2__device__info_html"></a>
<a id="astructfido2__device__info_html_a12d5e2334b2608bac80175cefa117481"></a>
<a id="astructfido2__device__info_html_a1f73e8e29f134a69529fd5f4061d28db"></a>
<a id="astructfido2__device__info_html_a1f9daa2e0dfb4b2a9caf79b5a478f7c8"></a>
<a id="astructfido2__device__info_html_a23b57e04315b12e64a5fcfae8b3f3738"></a>
<a id="astructfido2__device__info_html_a278775ff0bdc201889e104fe0b61f41d"></a>
<a id="astructfido2__device__info_html_a45da1b425879bc623bdd7651a81b9470"></a>
<a id="astructfido2__device__info_html_a67b8b3a2c27cafaf66c3d0ae6f339668"></a>
<a id="astructfido2__device__info_html_a74739097a2ef4a6beeb6edfce5836884"></a>
<a id="astructfido2__device__info_html_a7f59a4d2e3fd26bd6bfc9193276816c0"></a>
<a id="astructfido2__device__info_html_a8ddee975f649f1a8c1c91022c57259ec"></a>
<a id="astructfido2__device__info_html_a9a8944dc4fb8b56aa8bf94077c8663fa"></a>
<a id="astructfido2__device__info_html_aa69757cebdc3631d1b3c15b62d273f70"></a>
<a id="astructfido2__device__info_html_aa72be5c8dc8d34043467c91526bdb93a"></a>
<a id="astructfido2__device__info_html_aa788eed12e5e1629ece697ea372ee5a6"></a>
<a id="astructfido2__device__info_html_ab3b443cf0183568dc4c6cb34784a5588"></a>
<a id="astructfido2__device__info_html_abb11da815f9a176c8ae12c1474d1bcc7"></a>
<a id="astructfido2__device__info_html_abd1b7b2b922ddae9d89ccf10cc679ad8"></a>
<a id="astructfido2__device__info_html_abfab9809f2f6cb195fa232895e526d29"></a>
<a id="astructfido2__device__info_html_ac0bc83f02cbf76bb5fcb2fcca33a9a3e"></a>
<a id="astructfido2__device__info_html_ac2c2d357d5a472b7164378aa097c86f9"></a>
<a id="astructfido2__device__info_html_acc1c4bff7028f3a78d233861386bd88e"></a>
<a id="astructfido2__device__info_html_ad2c8042b987fed875fc7198f4e7c4c94"></a>
<a id="astructfido2__device__info_html_ae0efb9db99d6d5c1575ffa0a336deab5"></a>
<a id="astructfido2__device__info_html_ae3e5fadc6f5a03ce1d6782c650399c39"></a>
<a id="astructfido2__device__info_html_af127645cf37845b41479e3a84941cf67"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Siratul Islam <email@sirat.me>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_TYPES_H_
#define ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_TYPES_H_

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/sys/util.h>


#ifdef __cplusplus
extern "C" {
#endif

#define FIDO2_CREDENTIAL_ID_MAX_SIZE 128

#define FIDO2_RP_ID_MAX_LEN 128

#define FIDO2_RP_NAME_MAX_LEN 64

#define FIDO2_USER_NAME_MAX_LEN 64

#define FIDO2_USER_DISPLAY_NAME_MAX_LEN 64

#define FIDO2_USER_ID_MAX_SIZE 64

#define FIDO2_AAGUID_SIZE 16

#define FIDO2_SHA256_SIZE 32

#define FIDO2_PIN_HASH_SIZE 16

#define FIDO2_PIN_HASH_ENC_MAX_SIZE 32

#define FIDO2_PIN_ENC_MAX_SIZE 80

#define FIDO2_PIN_AUTH_SIZE_P1 16

#define FIDO2_PIN_AUTH_SIZE_P2 32

#define FIDO2_PIN_AUTH_MAX_SIZE 32

#define FIDO2_PIN_PADDED_SIZE 64

#define FIDO2_PIN_TOKEN_ENC_MAX_SIZE 48

#define FIDO2_DISCOVERABLE_CRED_ID_SIZE 32

#define FIDO2_NON_DISCOVERABLE_CRED_ID_SIZE 64

#define FIDO2_AUTH_DATA_HEADER_SIZE 37

#define FIDO2_ATTESTED_CRED_DATA_MAX_SIZE                                                          \
        (FIDO2_AAGUID_SIZE + 2 + FIDO2_CREDENTIAL_ID_MAX_SIZE + FIDO2_COSE_KEY_MAX_SIZE)

#define FIDO2_AUTH_DATA_MAX_SIZE (FIDO2_AUTH_DATA_HEADER_SIZE + FIDO2_ATTESTED_CRED_DATA_MAX_SIZE)

#define FIDO2_MAX_EXTENSIONS 8

#define FIDO2_MAX_VERSIONS 4

#define FIDO2_P256_UNCOMPRESSED_KEY_SIZE 65

#define FIDO2_P256_COORD_SIZE 32

#define FIDO2_EC_POINT_UNCOMPRESSED 0x04

#define FIDO2_ECDSA_SIG_MAX_SIZE 72

#define FIDO2_EXT_HMAC_SECRET     BIT(0)
#define FIDO2_EXT_LARGE_BLOB_KEY  BIT(1)
#define FIDO2_EXT_CRED_BLOB       BIT(2)
#define FIDO2_EXT_THIRD_PARTY_PAY BIT(3)

#define FIDO2_TRANSPORT_USB BIT(0)
#define FIDO2_TRANSPORT_BLE BIT(1)
#define FIDO2_TRANSPORT_NFC BIT(2)

#define AUTH_DATA_FLAG_UP BIT(0)
#define AUTH_DATA_FLAG_UV BIT(2)
#define AUTH_DATA_FLAG_AT BIT(6)
#define AUTH_DATA_FLAG_ED BIT(7)

enum fido2_status {
        FIDO2_OK = 0x00,
        FIDO2_ERR_INVALID_COMMAND = 0x01,
        FIDO2_ERR_INVALID_PARAMETER = 0x02,
        FIDO2_ERR_INVALID_LENGTH = 0x03,
        FIDO2_ERR_INVALID_SEQ = 0x04,
        FIDO2_ERR_TIMEOUT = 0x05,
        FIDO2_ERR_CHANNEL_BUSY = 0x06,
        FIDO2_ERR_LOCK_REQUIRED = 0x0A,
        FIDO2_ERR_INVALID_CHANNEL = 0x0B,
        FIDO2_ERR_CBOR_UNEXPECTED_TYPE = 0x11,
        FIDO2_ERR_INVALID_CBOR = 0x12,
        FIDO2_ERR_MISSING_PARAMETER = 0x14,
        FIDO2_ERR_LIMIT_EXCEEDED = 0x15,
        FIDO2_ERR_UNSUPPORTED_EXTENSION = 0x16,
        FIDO2_ERR_FP_DATABASE_FULL = 0x17,
        FIDO2_ERR_LARGE_BLOB_STORAGE_FULL = 0x18,
        FIDO2_ERR_CREDENTIAL_EXCLUDED = 0x19,
        FIDO2_ERR_PROCESSING = 0x21,
        FIDO2_ERR_INVALID_CREDENTIAL = 0x22,
        FIDO2_ERR_USER_ACTION_PENDING = 0x23,
        FIDO2_ERR_OPERATION_PENDING = 0x24,
        FIDO2_ERR_NO_OPERATIONS = 0x25,
        FIDO2_ERR_UNSUPPORTED_ALGORITHM = 0x26,
        FIDO2_ERR_OPERATION_DENIED = 0x27,
        FIDO2_ERR_KEY_STORE_FULL = 0x28,
        FIDO2_ERR_UNSUPPORTED_OPTION = 0x2B,
        FIDO2_ERR_INVALID_OPTION = 0x2C,
        FIDO2_ERR_KEEPALIVE_CANCEL = 0x2D,
        FIDO2_ERR_NO_CREDENTIALS = 0x2E,
        FIDO2_ERR_USER_ACTION_TIMEOUT = 0x2F,
        FIDO2_ERR_NOT_ALLOWED = 0x30,
        FIDO2_ERR_PIN_INVALID = 0x31,
        FIDO2_ERR_PIN_BLOCKED = 0x32,
        FIDO2_ERR_PIN_AUTH_INVALID = 0x33,
        FIDO2_ERR_PIN_AUTH_BLOCKED = 0x34,
        FIDO2_ERR_PIN_NOT_SET = 0x35,
        FIDO2_ERR_PUAT_REQUIRED = 0x36,
        FIDO2_ERR_PIN_POLICY_VIOLATION = 0x37,
        FIDO2_ERR_RESERVED = 0x38,
        FIDO2_ERR_REQUEST_TOO_LARGE = 0x39,
        FIDO2_ERR_ACTION_TIMEOUT = 0x3A,
        FIDO2_ERR_UP_REQUIRED = 0x3B,
        FIDO2_ERR_UV_BLOCKED = 0x3C,
        FIDO2_ERR_INTEGRITY_FAILURE = 0x3D,
        FIDO2_ERR_INVALID_SUBCOMMAND = 0x3E,
        FIDO2_ERR_UV_INVALID = 0x3F,
        FIDO2_ERR_UNAUTHORIZED_PERMISSION = 0x40,
        FIDO2_ERR_OTHER = 0x7F,
};

enum fido2_cmd {
        FIDO2_CMD_MAKE_CREDENTIAL = 0x01,
        FIDO2_CMD_GET_ASSERTION = 0x02,
        FIDO2_CMD_GET_INFO = 0x04,
        FIDO2_CMD_CLIENT_PIN = 0x06,
        FIDO2_CMD_RESET = 0x07,
        FIDO2_CMD_GET_NEXT_ASSERTION = 0x08,
        FIDO2_CMD_CREDENTIAL_MGMT = 0x0A,
        FIDO2_CMD_SELECTION = 0x0B,
};

enum fido2_cred_protect {
        FIDO2_CRED_PROTECT_UV_OPTIONAL = 0x01,
        FIDO2_CRED_PROTECT_UV_OPTIONAL_WITH_LIST = 0x02,
        FIDO2_CRED_PROTECT_UV_REQUIRED = 0x03,
};

enum fido2_cose_alg {
        FIDO2_COSE_ES256 = -7,
        FIDO2_COSE_EDDSA = -8,
        FIDO2_COSE_ECDHES_HKDF256 = -25,
        FIDO2_COSE_RS256 = -257,
};

struct fido2_credential {
        uint8_t id[FIDO2_CREDENTIAL_ID_MAX_SIZE];
        uint16_t id_len;
        uint8_t rp_id_hash[FIDO2_SHA256_SIZE];
        char rp_id[FIDO2_RP_ID_MAX_LEN];
        char rp_name[FIDO2_RP_NAME_MAX_LEN];
        char user_name[FIDO2_USER_NAME_MAX_LEN];
        char user_display_name[FIDO2_USER_DISPLAY_NAME_MAX_LEN];
        uint8_t user_id[FIDO2_USER_ID_MAX_SIZE];
        uint16_t user_id_len;
        uint32_t key_id;
        uint32_t sign_count;
        uint32_t extensions;
        int32_t algorithm;
        bool discoverable;
        uint8_t cred_protect;
};

struct fido2_device_info {
        const char *versions[FIDO2_MAX_VERSIONS];
        uint8_t num_versions;
        const char *extensions[FIDO2_MAX_EXTENSIONS];
        uint8_t num_extensions;
        uint8_t aaguid[FIDO2_AAGUID_SIZE];
        uint16_t max_credential_count;
        uint16_t max_credential_id_length;
        uint16_t max_msg_size;
        uint8_t transports;
        struct {
                bool plat;
                bool rk;
                bool client_pin;
                bool up;
                bool uv;
                bool cred_mgmt;
                bool pin_uv_auth_token;
                bool make_cred_uv_not_rqd;
                bool always_uv;
                bool no_mc_ga_permissions_with_client_pin;
        } options;
        uint32_t firmware_version;
        uint8_t pin_uv_auth_protocols[2];
        uint8_t num_pin_uv_auth_protocols;
        uint8_t pin_retries;
        uint8_t min_pin_length;
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_TYPES_H_ */
```

## 262.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Siratul Islam <email@sirat.me>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 307 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_TYPES_H_`。

## 262.3\_原页交叉引用（Cross References）

> 译注：官方源码页部分 FIDO2 枚举值链接指向文件页，但该页未定义相应锚点。下列条目保留原链接，并补充官方文件页实际指向的 FIDO2 分组定位。

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [fido2_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fc)
- [FIDO2_OK](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa08efc6dee799b3e1fb8490bc64bd1cf) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa08efc6dee799b3e1fb8490bc64bd1cf)
- [FIDO2_ERR_INVALID_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab263ae4a933b875d54a86d4a6da8dc4e) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab263ae4a933b875d54a86d4a6da8dc4e)
- [FIDO2_ERR_INVALID_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab4382a900e27d13b5043241f2f6dc2fe) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab4382a900e27d13b5043241f2f6dc2fe)
- [FIDO2_ERR_INVALID_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacbaf6656b7eac960f4bc0e561de47011) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacbaf6656b7eac960f4bc0e561de47011)
- [FIDO2_ERR_INVALID_SEQ](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca809431ef12cd0ba7094a80c39d6bdc2d) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca809431ef12cd0ba7094a80c39d6bdc2d)
- [FIDO2_ERR_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaf713403e6582ce02cace5d29f45405af) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaf713403e6582ce02cace5d29f45405af)
- [FIDO2_ERR_CHANNEL_BUSY](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac36b384a558597d72980f2425008c7b6) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac36b384a558597d72980f2425008c7b6)
- [FIDO2_ERR_LOCK_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacf7163e857eb9b8b6ddef1e7ff2b7351) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacf7163e857eb9b8b6ddef1e7ff2b7351)
- [FIDO2_ERR_INVALID_CHANNEL](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca1ece48887496a5962823530201eaf48c) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca1ece48887496a5962823530201eaf48c)
- [FIDO2_ERR_CBOR_UNEXPECTED_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca17c4a70a8f87425c4d849585d28280d4) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca17c4a70a8f87425c4d849585d28280d4)
- [FIDO2_ERR_INVALID_CBOR](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac804a5a070c6552d89d403ffc953c00d) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcac804a5a070c6552d89d403ffc953c00d)
- [FIDO2_ERR_MISSING_PARAMETER](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcad19e5127b17b8e0abee8bfe7d1ae595f) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcad19e5127b17b8e0abee8bfe7d1ae595f)
- [FIDO2_ERR_LIMIT_EXCEEDED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaee29e086a2af8e697b6467c9667cb327) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaee29e086a2af8e697b6467c9667cb327)
- [FIDO2_ERR_UNSUPPORTED_EXTENSION](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcabe9d8c984a0c0a62616a4a94af655a78) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcabe9d8c984a0c0a62616a4a94af655a78)
- [FIDO2_ERR_FP_DATABASE_FULL](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacc4208f8ab39ba6b67c9358df6b88797) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacc4208f8ab39ba6b67c9358df6b88797)
- [FIDO2_ERR_LARGE_BLOB_STORAGE_FULL](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaffdba1168067976851629c2111f46f6a) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaffdba1168067976851629c2111f46f6a)
- [FIDO2_ERR_CREDENTIAL_EXCLUDED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5dfe38f41a7863bc04928d7c566568b7) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5dfe38f41a7863bc04928d7c566568b7)
- [FIDO2_ERR_PROCESSING](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca128911647928193e076041834e398e75) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca128911647928193e076041834e398e75)
- [FIDO2_ERR_INVALID_CREDENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca4c53af9f0ad3e857bf86efea60b9370f) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca4c53af9f0ad3e857bf86efea60b9370f)
- [FIDO2_ERR_USER_ACTION_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8d108ee70faea78aa0669a90081dd05c) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8d108ee70faea78aa0669a90081dd05c)
- [FIDO2_ERR_OPERATION_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca020a5895146a35c2dedace5e0ff96112) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca020a5895146a35c2dedace5e0ff96112)
- [FIDO2_ERR_NO_OPERATIONS](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca376b899ff97c4d39f201f20e03a36ed7) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca376b899ff97c4d39f201f20e03a36ed7)
- [FIDO2_ERR_UNSUPPORTED_ALGORITHM](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca3521d75934cddcd0d009279541381c41) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca3521d75934cddcd0d009279541381c41)
- [FIDO2_ERR_OPERATION_DENIED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca507f5ded749fdba95d6b16d859052d43) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca507f5ded749fdba95d6b16d859052d43)
- [FIDO2_ERR_KEY_STORE_FULL](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacb6d4da143bbd72b7d361a7a4e38b1da) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcacb6d4da143bbd72b7d361a7a4e38b1da)
- [FIDO2_ERR_UNSUPPORTED_OPTION](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaad5b849ccb37209d531444bb346e3158) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaad5b849ccb37209d531444bb346e3158)
- [FIDO2_ERR_INVALID_OPTION](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05bb5e1370a3e46ef1a2f2545cf5675c) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05bb5e1370a3e46ef1a2f2545cf5675c)
- [FIDO2_ERR_KEEPALIVE_CANCEL](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca336c3e439e0a1b3eb24cf3edc38455e1) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca336c3e439e0a1b3eb24cf3edc38455e1)
- [FIDO2_ERR_NO_CREDENTIALS](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcafcbd15f2df2744ed0afd3613540ad6a3) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcafcbd15f2df2744ed0afd3613540ad6a3)
- [FIDO2_ERR_USER_ACTION_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca39355da927952f311dd8cdf9fe5cced8) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca39355da927952f311dd8cdf9fe5cced8)
- [FIDO2_ERR_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca739a74cd005fc1b3b8853f7aa2db7e3e) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca739a74cd005fc1b3b8853f7aa2db7e3e)
- [FIDO2_ERR_PIN_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca6eb4c3a5f51db1d0232ef8ca21d194e6) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca6eb4c3a5f51db1d0232ef8ca21d194e6)
- [FIDO2_ERR_PIN_BLOCKED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05c0bff840ed8b7e85c147876792760f) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca05c0bff840ed8b7e85c147876792760f)
- [FIDO2_ERR_PIN_AUTH_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca63548371fe576d03e00a2d428bf2501b) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca63548371fe576d03e00a2d428bf2501b)
- [FIDO2_ERR_PIN_AUTH_BLOCKED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca57a9754a770796bdb303ec5503222060) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca57a9754a770796bdb303ec5503222060)
- [FIDO2_ERR_PIN_NOT_SET](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab59eee02a04da8ca4bf54ceba81794d0) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab59eee02a04da8ca4bf54ceba81794d0)
- [FIDO2_ERR_PUAT_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5c952ab01843550e24d3aa672f05fec9) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca5c952ab01843550e24d3aa672f05fec9)
- [FIDO2_ERR_PIN_POLICY_VIOLATION](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8406e112b928b9f556cced2f0c391cfe) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca8406e112b928b9f556cced2f0c391cfe)
- [FIDO2_ERR_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca935a727495553c4bf584a92c39d780b7) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca935a727495553c4bf584a92c39d780b7)
- [FIDO2_ERR_REQUEST_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca0ca1a5d18e501d446c58ddcc4f8fbc05) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca0ca1a5d18e501d446c58ddcc4f8fbc05)
- [FIDO2_ERR_ACTION_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca356a92621e9d79fd5d599f1c13a7da93) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca356a92621e9d79fd5d599f1c13a7da93)
- [FIDO2_ERR_UP_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa28ed4a202b7c8eca14a727b708b0d50) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaa28ed4a202b7c8eca14a727b708b0d50)
- [FIDO2_ERR_UV_BLOCKED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaeb3d5db8b9e7ad3123df8d2a76ed4bfe) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcaeb3d5db8b9e7ad3123df8d2a76ed4bfe)
- [FIDO2_ERR_INTEGRITY_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca43b6e71c8f000bb2eccfc8a45c4591d3) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca43b6e71c8f000bb2eccfc8a45c4591d3)
- [FIDO2_ERR_INVALID_SUBCOMMAND](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca53aa4e296d54d24d7aab0bfc7747d893) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca53aa4e296d54d24d7aab0bfc7747d893)
- [FIDO2_ERR_UV_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca620c7a76e1481401e9dce1a5a75c8ee8) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca620c7a76e1481401e9dce1a5a75c8ee8)
- [FIDO2_ERR_UNAUTHORIZED_PERMISSION](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca69c9ebc7f40bcc26641eaa910a84f7e4) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fca69c9ebc7f40bcc26641eaa910a84f7e4)
- [FIDO2_ERR_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab52bc5933983ff9464292f4a470e0217) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6b3b79c7ef54b3ebbe686d4f67aaf7fcab52bc5933983ff9464292f4a470e0217)
- [fido2_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9)
- [FIDO2_CMD_MAKE_CREDENTIAL](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#gaec9e2106f2d776266909f5e2baf924d9aca44c6fcf4ff9f7d43693607a4ea178a) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9aca44c6fcf4ff9f7d43693607a4ea178a)
- [FIDO2_CMD_GET_ASSERTION](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#gaec9e2106f2d776266909f5e2baf924d9a64758dfc5b08bccc58369e97ecd8eae0) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a64758dfc5b08bccc58369e97ecd8eae0)
- [FIDO2_CMD_GET_INFO](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#gaec9e2106f2d776266909f5e2baf924d9a2419f886d7fcfe8e4e77a4b5f21d5bfc) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a2419f886d7fcfe8e4e77a4b5f21d5bfc)
- [FIDO2_CMD_CLIENT_PIN](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#gaec9e2106f2d776266909f5e2baf924d9a6b7d85b947ad93ab5159ffe7f2934948) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a6b7d85b947ad93ab5159ffe7f2934948)
- [FIDO2_CMD_RESET](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#gaec9e2106f2d776266909f5e2baf924d9aacffe603fa91c1102164c1d022bcd678) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9aacffe603fa91c1102164c1d022bcd678)
- [FIDO2_CMD_GET_NEXT_ASSERTION](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#gaec9e2106f2d776266909f5e2baf924d9adc26ad4d923d58ca0f33d63c9dae1c27) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9adc26ad4d923d58ca0f33d63c9dae1c27)
- [FIDO2_CMD_CREDENTIAL_MGMT](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#gaec9e2106f2d776266909f5e2baf924d9a4984d83c6210b1855106ff39b413e614) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a4984d83c6210b1855106ff39b413e614)
- [FIDO2_CMD_SELECTION](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#gaec9e2106f2d776266909f5e2baf924d9a327a6fbfb22651dfed6d1d1ded574ab7) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaec9e2106f2d776266909f5e2baf924d9a327a6fbfb22651dfed6d1d1ded574ab7)
- [fido2_cred_protect](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9411b5f6c2596cf49f7ebcf04fd7955)
- [FIDO2_CRED_PROTECT_UV_OPTIONAL](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#gae9411b5f6c2596cf49f7ebcf04fd7955a07603aa0b0598319d504ca9e23e76078) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9411b5f6c2596cf49f7ebcf04fd7955a07603aa0b0598319d504ca9e23e76078)
- [FIDO2_CRED_PROTECT_UV_OPTIONAL_WITH_LIST](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#gae9411b5f6c2596cf49f7ebcf04fd7955a2299549abdae08cd0e71c7db3d918ca6) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9411b5f6c2596cf49f7ebcf04fd7955a2299549abdae08cd0e71c7db3d918ca6)
- [FIDO2_CRED_PROTECT_UV_REQUIRED](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#gae9411b5f6c2596cf49f7ebcf04fd7955aef0d3d870129fc9e72138d309c641be6) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae9411b5f6c2596cf49f7ebcf04fd7955aef0d3d870129fc9e72138d309c641be6)
- [fido2_cose_alg](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684)
- [FIDO2_COSE_ES256](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga86aa0e78a95ea9e399c3831348fe8684a94ae94ce511d5898c12059766adf95c3) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684a94ae94ce511d5898c12059766adf95c3)
- [FIDO2_COSE_EDDSA](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga86aa0e78a95ea9e399c3831348fe8684a21d965a84070571fb2e0d475cf27043d) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684a21d965a84070571fb2e0d475cf27043d)
- [FIDO2_COSE_ECDHES_HKDF256](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga86aa0e78a95ea9e399c3831348fe8684a386cd8a5baf42b49b2271d655645b103) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684a386cd8a5baf42b49b2271d655645b103)
- [FIDO2_COSE_RS256](https://docs.zephyrproject.org/latest/doxygen/html/fido2__types_8h.html#ga86aa0e78a95ea9e399c3831348fe8684ad2a327ca6649f0abd4153dee72952167) · [分组定位](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga86aa0e78a95ea9e399c3831348fe8684ad2a327ca6649f0abd4153dee72952167)
- [fido2_credential](../platform_security_model_reference/P007_fido2_credential_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [FIDO2_CREDENTIAL_ID_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga7ff8f1d8d389b44e2a656b3ebe20f778)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [id_len](../platform_security_model_reference/P007_fido2_credential_结构体.md#aaf5c0b6a289e51c49e5c9e065fb28a7a)
- [rp_id_hash](../platform_security_model_reference/P007_fido2_credential_结构体.md#a6a0e84bb3432eaccdd85a7b9d72ed91d)
- [FIDO2_SHA256_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaead02ba380ab3899742dfbf41edc4a98)
- [rp_id](../platform_security_model_reference/P007_fido2_credential_结构体.md#af523edcf94f7a9f9cbbd7ea87bbe673a)
- [FIDO2_RP_ID_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga57628d326e2f62b318908af69485dbb8)
- [rp_name](../platform_security_model_reference/P007_fido2_credential_结构体.md#a194b53ed392542e1214e4289fe76d033)
- [FIDO2_RP_NAME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga99da0bebb5865edd2e163a31da966618)
- [user_name](../platform_security_model_reference/P007_fido2_credential_结构体.md#ae95bda862fcc760ffa5d723dfb3ff8aa)
- [FIDO2_USER_NAME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga6060501b6c00b076fc705276464050ab)
- [user_display_name](../platform_security_model_reference/P007_fido2_credential_结构体.md#a2a097ffa153fc969e73850627654c97f)
- [FIDO2_USER_DISPLAY_NAME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaa4111c61a7446d3cb5efa41bf492d930)
- [user_id](../platform_security_model_reference/P007_fido2_credential_结构体.md#a0d3ac4d5515fae39f06c13c37aa385f7)
- [FIDO2_USER_ID_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaf5eb8fcafd96dd1d3eec5424aff9748c)
- [user_id_len](../platform_security_model_reference/P007_fido2_credential_结构体.md#af2e3794720dbad041de08aaba6dbd925)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [key_id](../platform_security_model_reference/P007_fido2_credential_结构体.md#aad709e654b5a0ebb6a2ee7d1a1e1c6a2)
- [sign_count](../platform_security_model_reference/P007_fido2_credential_结构体.md#a1dde5d1541f18260df49175047c883df)
- [extensions](../platform_security_model_reference/P007_fido2_credential_结构体.md#a8951d380f675d378e7fcb584f87561cd)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [algorithm](../platform_security_model_reference/P007_fido2_credential_结构体.md#a71a46e60f2e8204a83aaecd2dfb44e40)
- [discoverable](../platform_security_model_reference/P007_fido2_credential_结构体.md#a7b7c2b9ba8ea5dea3428132e5e0462b7)
- [cred_protect](../platform_security_model_reference/P007_fido2_credential_结构体.md#a5472886ee94fd507f4facf8681b62882)
- [fido2_device_info](../platform_security_model_reference/P008_fido2_device_info_结构体.md)
- [versions](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a67b8b3a2c27cafaf66c3d0ae6f339668)
- [FIDO2_MAX_VERSIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga15f94b65bca9940f1a535e6ec1339fdf)
- [num_versions](../platform_security_model_reference/P008_fido2_device_info_结构体.md#ae3e5fadc6f5a03ce1d6782c650399c39)
- [extensions](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a74739097a2ef4a6beeb6edfce5836884)
- [FIDO2_MAX_EXTENSIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga7fe764c73ecb327210eb080aa5b32a92)
- [num_extensions](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a12d5e2334b2608bac80175cefa117481)
- [aaguid](../platform_security_model_reference/P008_fido2_device_info_结构体.md#abfab9809f2f6cb195fa232895e526d29)
- [FIDO2_AAGUID_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga624b79a13eb53f43594b5c24332725fa)
- [max_credential_count](../platform_security_model_reference/P008_fido2_device_info_结构体.md#aa69757cebdc3631d1b3c15b62d273f70)
- [max_credential_id_length](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a8ddee975f649f1a8c1c91022c57259ec)
- [max_msg_size](../platform_security_model_reference/P008_fido2_device_info_结构体.md#ae0efb9db99d6d5c1575ffa0a336deab5)
- [transports](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a45da1b425879bc623bdd7651a81b9470)
- [plat](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a7f59a4d2e3fd26bd6bfc9193276816c0)
- [rk](../platform_security_model_reference/P008_fido2_device_info_结构体.md#acc1c4bff7028f3a78d233861386bd88e)
- [client_pin](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a1f73e8e29f134a69529fd5f4061d28db)
- [up](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a278775ff0bdc201889e104fe0b61f41d)
- [uv](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a23b57e04315b12e64a5fcfae8b3f3738)
- [cred_mgmt](../platform_security_model_reference/P008_fido2_device_info_结构体.md#ad2c8042b987fed875fc7198f4e7c4c94)
- [pin_uv_auth_token](../platform_security_model_reference/P008_fido2_device_info_结构体.md#abb11da815f9a176c8ae12c1474d1bcc7)
- [make_cred_uv_not_rqd](../platform_security_model_reference/P008_fido2_device_info_结构体.md#ac0bc83f02cbf76bb5fcb2fcca33a9a3e)
- [always_uv](../platform_security_model_reference/P008_fido2_device_info_结构体.md#ab3b443cf0183568dc4c6cb34784a5588)
- [no_mc_ga_permissions_with_client_pin](../platform_security_model_reference/P008_fido2_device_info_结构体.md#ac2c2d357d5a472b7164378aa097c86f9)
- [options](../platform_security_model_reference/P008_fido2_device_info_结构体.md#af127645cf37845b41479e3a84941cf67)
- [firmware_version](../platform_security_model_reference/P008_fido2_device_info_结构体.md#abd1b7b2b922ddae9d89ccf10cc679ad8)
- [pin_uv_auth_protocols](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a9a8944dc4fb8b56aa8bf94077c8663fa)
- [num_pin_uv_auth_protocols](../platform_security_model_reference/P008_fido2_device_info_结构体.md#aa788eed12e5e1629ece697ea372ee5a6)
- [pin_retries](../platform_security_model_reference/P008_fido2_device_info_结构体.md#aa72be5c8dc8d34043467c91526bdb93a)
- [min_pin_length](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a1f9daa2e0dfb4b2a9caf79b5a478f7c8)
- [fido2_credential::user_id](../platform_security_model_reference/P007_fido2_credential_结构体.md#a0d3ac4d5515fae39f06c13c37aa385f7)
- [fido2_credential::rp_name](../platform_security_model_reference/P007_fido2_credential_结构体.md#a194b53ed392542e1214e4289fe76d033)
- [fido2_credential::sign_count](../platform_security_model_reference/P007_fido2_credential_结构体.md#a1dde5d1541f18260df49175047c883df)
- [fido2_credential::user_display_name](../platform_security_model_reference/P007_fido2_credential_结构体.md#a2a097ffa153fc969e73850627654c97f)
- [fido2_credential::cred_protect](../platform_security_model_reference/P007_fido2_credential_结构体.md#a5472886ee94fd507f4facf8681b62882)
- [fido2_credential::rp_id_hash](../platform_security_model_reference/P007_fido2_credential_结构体.md#a6a0e84bb3432eaccdd85a7b9d72ed91d)
- [fido2_credential::algorithm](../platform_security_model_reference/P007_fido2_credential_结构体.md#a71a46e60f2e8204a83aaecd2dfb44e40)
- [fido2_credential::discoverable](../platform_security_model_reference/P007_fido2_credential_结构体.md#a7b7c2b9ba8ea5dea3428132e5e0462b7)
- [fido2_credential::extensions](../platform_security_model_reference/P007_fido2_credential_结构体.md#a8951d380f675d378e7fcb584f87561cd)
- [fido2_credential::key_id](../platform_security_model_reference/P007_fido2_credential_结构体.md#aad709e654b5a0ebb6a2ee7d1a1e1c6a2)
- [fido2_credential::id_len](../platform_security_model_reference/P007_fido2_credential_结构体.md#aaf5c0b6a289e51c49e5c9e065fb28a7a)
- [fido2_credential::user_name](../platform_security_model_reference/P007_fido2_credential_结构体.md#ae95bda862fcc760ffa5d723dfb3ff8aa)
- [fido2_credential::user_id_len](../platform_security_model_reference/P007_fido2_credential_结构体.md#af2e3794720dbad041de08aaba6dbd925)
- [fido2_credential::rp_id](../platform_security_model_reference/P007_fido2_credential_结构体.md#af523edcf94f7a9f9cbbd7ea87bbe673a)
- [fido2_device_info::num_extensions](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a12d5e2334b2608bac80175cefa117481)
- [fido2_device_info::client_pin](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a1f73e8e29f134a69529fd5f4061d28db)
- [fido2_device_info::min_pin_length](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a1f9daa2e0dfb4b2a9caf79b5a478f7c8)
- [fido2_device_info::uv](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a23b57e04315b12e64a5fcfae8b3f3738)
- [fido2_device_info::up](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a278775ff0bdc201889e104fe0b61f41d)
- [fido2_device_info::transports](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a45da1b425879bc623bdd7651a81b9470)
- [fido2_device_info::versions](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a67b8b3a2c27cafaf66c3d0ae6f339668)
- [fido2_device_info::extensions](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a74739097a2ef4a6beeb6edfce5836884)
- [fido2_device_info::plat](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a7f59a4d2e3fd26bd6bfc9193276816c0)
- [fido2_device_info::max_credential_id_length](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a8ddee975f649f1a8c1c91022c57259ec)
- [fido2_device_info::pin_uv_auth_protocols](../platform_security_model_reference/P008_fido2_device_info_结构体.md#a9a8944dc4fb8b56aa8bf94077c8663fa)
- [fido2_device_info::max_credential_count](../platform_security_model_reference/P008_fido2_device_info_结构体.md#aa69757cebdc3631d1b3c15b62d273f70)
- [fido2_device_info::pin_retries](../platform_security_model_reference/P008_fido2_device_info_结构体.md#aa72be5c8dc8d34043467c91526bdb93a)
- [fido2_device_info::num_pin_uv_auth_protocols](../platform_security_model_reference/P008_fido2_device_info_结构体.md#aa788eed12e5e1629ece697ea372ee5a6)
- [fido2_device_info::always_uv](../platform_security_model_reference/P008_fido2_device_info_结构体.md#ab3b443cf0183568dc4c6cb34784a5588)
- [fido2_device_info::pin_uv_auth_token](../platform_security_model_reference/P008_fido2_device_info_结构体.md#abb11da815f9a176c8ae12c1474d1bcc7)
- [fido2_device_info::firmware_version](../platform_security_model_reference/P008_fido2_device_info_结构体.md#abd1b7b2b922ddae9d89ccf10cc679ad8)
- [fido2_device_info::aaguid](../platform_security_model_reference/P008_fido2_device_info_结构体.md#abfab9809f2f6cb195fa232895e526d29)
- [fido2_device_info::make_cred_uv_not_rqd](../platform_security_model_reference/P008_fido2_device_info_结构体.md#ac0bc83f02cbf76bb5fcb2fcca33a9a3e)
- [fido2_device_info::no_mc_ga_permissions_with_client_pin](../platform_security_model_reference/P008_fido2_device_info_结构体.md#ac2c2d357d5a472b7164378aa097c86f9)
- [fido2_device_info::rk](../platform_security_model_reference/P008_fido2_device_info_结构体.md#acc1c4bff7028f3a78d233861386bd88e)
- [fido2_device_info::cred_mgmt](../platform_security_model_reference/P008_fido2_device_info_结构体.md#ad2c8042b987fed875fc7198f4e7c4c94)
- [fido2_device_info::max_msg_size](../platform_security_model_reference/P008_fido2_device_info_结构体.md#ae0efb9db99d6d5c1575ffa0a336deab5)
- [fido2_device_info::num_versions](../platform_security_model_reference/P008_fido2_device_info_结构体.md#ae3e5fadc6f5a03ce1d6782c650399c39)
- [fido2_device_info::options](../platform_security_model_reference/P008_fido2_device_info_结构体.md#af127645cf37845b41479e3a84941cf67)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P261_fido2_transport.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P263_fido2_up.h_源码浏览.md)
