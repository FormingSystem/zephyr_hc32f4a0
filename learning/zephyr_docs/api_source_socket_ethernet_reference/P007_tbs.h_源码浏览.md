---
id: learning.zephyr-docs.api-source-socket-ethernet-reference.page-7
title: tbs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_tbs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h.html)。

## 7.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
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
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00051"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00065"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="foldopen00255"></a>
<a id="l00255"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00447"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="foldopen00456"></a>
<a id="l00456"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="foldopen00548"></a>
<a id="l00548"></a>
<a id="l00550"></a>
<a id="l00552"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="foldopen00558"></a>
<a id="l00558"></a>
<a id="l00560"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00670"></a>
<a id="l00671"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="foldopen00680"></a>
<a id="l00680"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00691"></a>
<a id="l00693"></a>
<a id="l00694"></a>
<a id="l00695"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00699"></a>
<a id="l00701"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00713"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="l00724"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00727"></a>
<a id="l00729"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00741"></a>
<a id="l00742"></a>
<a id="l00743"></a>
<a id="l00745"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="l00756"></a>
<a id="l00757"></a>
<a id="l00759"></a>
<a id="l00760"></a>
<a id="l00762"></a>
<a id="l00763"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00774"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00786"></a>
<a id="l00787"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00858"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00888"></a>
<a id="l00889"></a>
<a id="l00890"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00918"></a>
<a id="l00919"></a>
<a id="l00920"></a>
<a id="l00932"></a>
<a id="l00933"></a>
<a id="l00945"></a>
<a id="l00946"></a>
<a id="l00958"></a>
<a id="l00959"></a>
<a id="l00971"></a>
<a id="l00972"></a>
<a id="l00973"></a>
<a id="l00985"></a>
<a id="l00986"></a>
<a id="l00987"></a>
<a id="l00999"></a>
<a id="l01000"></a>
<a id="l01012"></a>
<a id="l01013"></a>
<a id="l01025"></a>
<a id="l01026"></a>
<a id="l01038"></a>
<a id="l01039"></a>
<a id="l01048"></a>
<a id="l01049"></a>
<a id="l01061"></a>
<a id="l01062"></a>
<a id="l01074"></a>
<a id="l01075"></a>
<a id="l01087"></a>
<a id="l01088"></a>
<a id="l01089"></a>
<a id="l01099"></a>
<a id="l01100"></a>
<a id="l01112"></a>
<a id="l01113"></a>
<a id="l01114"></a>
<a id="l01123"></a>
<a id="l01124"></a>
<a id="l01125"></a>
<a id="l01126"></a>
<a id="l01127"></a>
<a id="l01128"></a>
<a id="l01130"></a>
<a id="l01131"></a>
<a id="aassigned__numbers_8h_html"></a>
<a id="aconn_8h_html"></a>
<a id="agroup__bt__assigned__numbers__audio_html_ga4bf3f820b493361a9a3b393d0282420f"></a>
<a id="agroup__bt__tbs_html_ga09a3e64040819b6b8b694b94d2f62ca0"></a>
<a id="agroup__bt__tbs_html_ga0aac704008ffc92ce6609d3ffffc4523"></a>
<a id="agroup__bt__tbs_html_ga1b942bcf8287641f9cd53824b4d6e77b"></a>
<a id="agroup__bt__tbs_html_ga1cc9e7140531b07bf6a8dedbc17f24c0"></a>
<a id="agroup__bt__tbs_html_ga2053a9eb7cf28f66febd365f0b682be0"></a>
<a id="agroup__bt__tbs_html_ga20c6780a4624707a537e905e889510ca"></a>
<a id="agroup__bt__tbs_html_ga23226d41e3b98a53ec9a9c2fa346c9ac"></a>
<a id="agroup__bt__tbs_html_ga23e825de6af71d4e456b63c3a621fb61"></a>
<a id="agroup__bt__tbs_html_ga25b803bb5cae2e1a8b0398bc48137d80"></a>
<a id="agroup__bt__tbs_html_ga262ca74b7ae2f0c52657066549fa4f92"></a>
<a id="agroup__bt__tbs_html_ga2fa85f3cd96f25f6bb4f449fc9210fa1"></a>
<a id="agroup__bt__tbs_html_ga38046c5c715d451b21a3076742268010"></a>
<a id="agroup__bt__tbs_html_ga3a71c51d464aa19fbfbd2d60fc4901bc"></a>
<a id="agroup__bt__tbs_html_ga40b8b3d1b318a1b5c5524877bbc2f90f"></a>
<a id="agroup__bt__tbs_html_ga4238a37b80b7d7ff611fe9b02b7cf54d"></a>
<a id="agroup__bt__tbs_html_ga47939f557e4d6503af9b7b85aff9d60f"></a>
<a id="agroup__bt__tbs_html_ga4d7632de7c2006e478880950076908a9"></a>
<a id="agroup__bt__tbs_html_ga5118db6b23b387956e75eda8aecd53d5"></a>
<a id="agroup__bt__tbs_html_ga52afc7b8a22b071dbac10057579f319c"></a>
<a id="agroup__bt__tbs_html_ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e"></a>
<a id="agroup__bt__tbs_html_ga600051910ed538a2da823554df23dd20"></a>
<a id="agroup__bt__tbs_html_ga60e9e143f247bb7e668293f0233ce300"></a>
<a id="agroup__bt__tbs_html_ga625fc73885c2bfd63f0f4b2d7f72eaef"></a>
<a id="agroup__bt__tbs_html_ga62f5008cbfba158fe399cfaf683d1d2e"></a>
<a id="agroup__bt__tbs_html_ga69e93b48b2a48e8a6552882660b791cc"></a>
<a id="agroup__bt__tbs_html_ga7684dbcb78e407f7002d44fbdb805e5d"></a>
<a id="agroup__bt__tbs_html_ga76f120dba549225a6f2c2c22be08edfc"></a>
<a id="agroup__bt__tbs_html_ga7b31e1c30fa96081a3ef38e1a481b64f"></a>
<a id="agroup__bt__tbs_html_ga82553640882ac74f9af84bfe09ff47ee"></a>
<a id="agroup__bt__tbs_html_ga838e51a85f9833e0822090cd3df09e00"></a>
<a id="agroup__bt__tbs_html_ga868b83450f7425e8a0c8cfb7c1de45d8"></a>
<a id="agroup__bt__tbs_html_ga895c7f54300e5452fb8d0c9d4b3306ae"></a>
<a id="agroup__bt__tbs_html_ga8edd4d31478ed9e0aedbd1a34bdfca96"></a>
<a id="agroup__bt__tbs_html_ga970c970bedd6e94aa4c92479183554e9"></a>
<a id="agroup__bt__tbs_html_ga99549dd6244580e157006fb17772fd8f"></a>
<a id="agroup__bt__tbs_html_ga9cac11cc696be9fb387f2f7685e0d8a7"></a>
<a id="agroup__bt__tbs_html_ga9fe91df1a31ce59401347fc0eac2b701"></a>
<a id="agroup__bt__tbs_html_gaa1dcb9908057d75a54fa447639826f3c"></a>
<a id="agroup__bt__tbs_html_gaa45b3f4837165d722c2df6f202a39058"></a>
<a id="agroup__bt__tbs_html_gaa77ea977fca9833d1755d5084a3f352c"></a>
<a id="agroup__bt__tbs_html_gaabe97df55817b8e36c79de4bf30fc83f"></a>
<a id="agroup__bt__tbs_html_gaadae501fa6f7771bb9661af829805a5f"></a>
<a id="agroup__bt__tbs_html_gaae1925deb0b5865af601aa8278ffb10a"></a>
<a id="agroup__bt__tbs_html_gab04f8355c32fce501bd757b75ee9d38a"></a>
<a id="agroup__bt__tbs_html_gab72044a1f5466114b5efb88dfcd2f097"></a>
<a id="agroup__bt__tbs_html_gab881b3caaaa4425e52afd84e53adee78"></a>
<a id="agroup__bt__tbs_html_gaba92039d3b44da9163a22400951fafa7"></a>
<a id="agroup__bt__tbs_html_gabbe194a63da0b95dc1dca0337560a585"></a>
<a id="agroup__bt__tbs_html_gabe2251d4ea88306793dc68ae683886bb"></a>
<a id="agroup__bt__tbs_html_gac070ec0590df5820b7721d579ceeeb15"></a>
<a id="agroup__bt__tbs_html_gac316adedf7fda441ee55feb9d24d1a94"></a>
<a id="agroup__bt__tbs_html_gac59f3dec092a14bdf234039e3dcd12eb"></a>
<a id="agroup__bt__tbs_html_gad0b45af09b82d6cd66a8481c0e67e04e"></a>
<a id="agroup__bt__tbs_html_gad19db25591c7ae5bd0b4c2bbaefc9bed"></a>
<a id="agroup__bt__tbs_html_gadeae51d7cecd80abcdcde1195bb1dfba"></a>
<a id="agroup__bt__tbs_html_gae413f94b141b6fa8233de15c36f6327a"></a>
<a id="agroup__bt__tbs_html_gaf504e1a11352d77a36aa087b587e4ba8"></a>
<a id="agroup__bt__tbs_html_gaf77231168e4444da7aef203cc9eaca95"></a>
<a id="agroup__bt__tbs_html_gafeaaaefb9d4eb773dd0cbdfebe26e0b7"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__conn_html"></a>
<a id="astructbt__tbs__cb_html"></a>
<a id="astructbt__tbs__cb_html_a566504bee9c7334c53a23223e544855f"></a>
<a id="astructbt__tbs__cb_html_a798c09c04a563800c4d9328c1d9e2de6"></a>
<a id="astructbt__tbs__cb_html_a8b76dd9243e97d22e0d6c2ac578aa383"></a>
<a id="astructbt__tbs__cb_html_ab065a5c58db19feb2a1d3013983ed5aa"></a>
<a id="astructbt__tbs__cb_html_ab7c859ffaebcf16db71c5d54bd4f5802"></a>
<a id="astructbt__tbs__cb_html_ac1a99a703687a3ef5ebc12eca5f6c2e7"></a>
<a id="astructbt__tbs__cb_html_ad543a2f26d1749eba0774e2352b53692"></a>
<a id="astructbt__tbs__client__call__state_html"></a>
<a id="astructbt__tbs__client__call__state_html_a3d6eb4dda7adcd16c04ebbd41242c292"></a>
<a id="astructbt__tbs__client__call__state_html_a3e758ad6d0b35f26f43584e50c9a9895"></a>
<a id="astructbt__tbs__client__call__state_html_a57ed9dd726faa3c219e1c858ad6659d9"></a>
<a id="astructbt__tbs__client__call_html"></a>
<a id="astructbt__tbs__client__call_html_a480279fea551db1bcb260de81edd6571"></a>
<a id="astructbt__tbs__client__call_html_af04f0576e786250526c12e1436a60c4e"></a>
<a id="astructbt__tbs__client__cb_html"></a>
<a id="astructbt__tbs__client__cb_html_a01426c4a84e71a9395cce2963e2e83a3"></a>
<a id="astructbt__tbs__client__cb_html_a0bc51181f188a1249407f2e50431d9fd"></a>
<a id="astructbt__tbs__client__cb_html_a10dc9404533db388b3ae1058542efd66"></a>
<a id="astructbt__tbs__client__cb_html_a15ccb7de457631620983e7d2d0372967"></a>
<a id="astructbt__tbs__client__cb_html_a2a5fb7de5c3c4aab290c0163c0b40858"></a>
<a id="astructbt__tbs__client__cb_html_a2d6b7acd90d05c61f60f27236ab6f1ee"></a>
<a id="astructbt__tbs__client__cb_html_a304a5fd373f1ba5ccb2eb77fcdbbd380"></a>
<a id="astructbt__tbs__client__cb_html_a354ba5d21376813adc5c9765a5da1a09"></a>
<a id="astructbt__tbs__client__cb_html_a36d8ea1717e57b9440e9b58e9411422a"></a>
<a id="astructbt__tbs__client__cb_html_a41242d76c976eef102d480965f977537"></a>
<a id="astructbt__tbs__client__cb_html_a596b31583975c416aa9cb6d64301c55f"></a>
<a id="astructbt__tbs__client__cb_html_a7f64cf8e3d0bc4ec21c44bd4fea6d7ee"></a>
<a id="astructbt__tbs__client__cb_html_a88cb69ef54c9399bceb5641202eeabce"></a>
<a id="astructbt__tbs__client__cb_html_a90acde153f8893b5cba891884529d86c"></a>
<a id="astructbt__tbs__client__cb_html_a91c61b29c16a43fd3f781fd7e0ab4618"></a>
<a id="astructbt__tbs__client__cb_html_a94c3bfc1e88518de9e29e947064ec8dc"></a>
<a id="astructbt__tbs__client__cb_html_a96df90461159f97f5dc8cbb72cd0cbc4"></a>
<a id="astructbt__tbs__client__cb_html_aa78425597fe7fd0db09d69c3ed757293"></a>
<a id="astructbt__tbs__client__cb_html_abfd4542a0781ff5676a191249f121e91"></a>
<a id="astructbt__tbs__client__cb_html_ad2089050db76453b7f9c51c3d2fa4d17"></a>
<a id="astructbt__tbs__client__cb_html_ae8e5cbe52cbb300e1cd919d24c85c4df"></a>
<a id="astructbt__tbs__client__cb_html_ae95494a76e1f3275f48204dcd4798712"></a>
<a id="astructbt__tbs__instance_html"></a>
<a id="astructbt__tbs__register__param_html"></a>
<a id="astructbt__tbs__register__param_html_a004fc8f70cff59acf0122135bdd27065"></a>
<a id="astructbt__tbs__register__param_html_a4ffe59cd6d00b9b45db304b17efa22b0"></a>
<a id="astructbt__tbs__register__param_html_a54352a512eeb209d0254a8f395647f87"></a>
<a id="astructbt__tbs__register__param_html_a8cf7713269e8bb193c61be01d6971922"></a>
<a id="astructbt__tbs__register__param_html_aa38a646b7121b555846f7acea9bc9365"></a>
<a id="astructbt__tbs__register__param_html_ab7a0dc41a9e4c898ffd1afaffdfae51d"></a>
<a id="astructbt__tbs__register__param_html_af88bfd0ac0e83f94e9e467064b4c6c32"></a>
<a id="autil__macro_8h_html"></a>

```c


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_TBS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_TBS_H_


#include <stdint.h>
#include <stdbool.h>

#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_TBS_ERR_VAL_CHANGED 0x80U

#define BT_TBS_CALL_STATE_INCOMING                      0x00U
#define BT_TBS_CALL_STATE_DIALING                       0x01U
#define BT_TBS_CALL_STATE_ALERTING                      0x02U
#define BT_TBS_CALL_STATE_ACTIVE                        0x03U
#define BT_TBS_CALL_STATE_LOCALLY_HELD                  0x04U
#define BT_TBS_CALL_STATE_REMOTELY_HELD                 0x05U
#define BT_TBS_CALL_STATE_LOCALLY_AND_REMOTELY_HELD     0x06U

#define BT_TBS_REASON_BAD_REMOTE_URI                    0x00U
#define BT_TBS_REASON_CALL_FAILED                       0x01U
#define BT_TBS_REASON_REMOTE_ENDED_CALL                 0x02U
#define BT_TBS_REASON_SERVER_ENDED_CALL                 0x03U
#define BT_TBS_REASON_LINE_BUSY                         0x04U
#define BT_TBS_REASON_NETWORK_CONGESTED                 0x05U
#define BT_TBS_REASON_CLIENT_TERMINATED                 0x06U
#define BT_TBS_REASON_NO_SERVICE                        0x07U
#define BT_TBS_REASON_NO_ANSWER                         0x08U
#define BT_TBS_REASON_UNSPECIFIED                       0x09U

#define BT_TBS_RESULT_CODE_SUCCESS                0x00U
#define BT_TBS_RESULT_CODE_OPCODE_NOT_SUPPORTED   0x01U
#define BT_TBS_RESULT_CODE_OPERATION_NOT_POSSIBLE 0x02U
#define BT_TBS_RESULT_CODE_INVALID_CALL_INDEX     0x03U
#define BT_TBS_RESULT_CODE_STATE_MISMATCH         0x04U
#define BT_TBS_RESULT_CODE_OUT_OF_RESOURCES       0x05U
#define BT_TBS_RESULT_CODE_INVALID_URI            0x06U

#define BT_TBS_OPTIONAL_OPCODE_HOLD BIT(0U)
#define BT_TBS_OPTIONAL_OPCODE_JOIN BIT(1U)
#define BT_TBS_OPTIONAL_OPCODE_ALL  (BT_TBS_OPTIONAL_OPCODE_HOLD | BT_TBS_OPTIONAL_OPCODE_JOIN)

#define BT_TBS_SIGNAL_STRENGTH_NO_SERVICE               0U
#define BT_TBS_SIGNAL_STRENGTH_MAX                      100U
#define BT_TBS_SIGNAL_STRENGTH_UNKNOWN                  255U

#define BT_TBS_STATUS_FLAG_INBAND_RINGTONE BIT(0U)
#define BT_TBS_STATUS_FLAG_SILENT_MOD      BIT(1U)

#define BT_TBS_CALL_FLAG_OUTGOING            BIT(0U)
#define BT_TBS_CALL_FLAG_WITHHELD            BIT(1U)
#define BT_TBS_CALL_FLAG_WITHHELD_BY_NETWORK BIT(2U)

#define BT_TBS_GTBS_INDEX 0xFFU

#define BT_TBS_MAX_UCI_SIZE 6U

struct bt_tbs_instance;

typedef bool (*bt_tbs_originate_call_cb)(struct bt_conn *conn,
                                         uint8_t call_index,
                                         const char *uri);

typedef void (*bt_tbs_terminate_call_cb)(struct bt_conn *conn,
                                         uint8_t call_index,
                                         uint8_t reason);

typedef void (*bt_tbs_join_calls_cb)(struct bt_conn *conn,
                                     uint8_t call_index_count,
                                     const uint8_t *call_indexes);

typedef void (*bt_tbs_call_change_cb)(struct bt_conn *conn,
                                      uint8_t call_index);

typedef bool (*bt_tbs_authorize_cb)(struct bt_conn *conn);

struct bt_tbs_cb {
        bt_tbs_originate_call_cb      originate_call;
        bt_tbs_terminate_call_cb      terminate_call;
        bt_tbs_call_change_cb         hold_call;
        bt_tbs_call_change_cb         accept_call;
        bt_tbs_call_change_cb         retrieve_call;
        bt_tbs_join_calls_cb          join_calls;
        bt_tbs_authorize_cb           authorize;
};

int bt_tbs_accept(uint8_t call_index);

int bt_tbs_hold(uint8_t call_index);

int bt_tbs_retrieve(uint8_t call_index);

int bt_tbs_terminate(uint8_t call_index);

int bt_tbs_originate(uint8_t bearer_index, char *uri, uint8_t *call_index);

int bt_tbs_join(uint8_t call_index_cnt, uint8_t *call_indexes);

int bt_tbs_remote_answer(uint8_t call_index);

int bt_tbs_remote_hold(uint8_t call_index);

int bt_tbs_remote_retrieve(uint8_t call_index);

int bt_tbs_remote_terminate(uint8_t call_index);

int bt_tbs_remote_incoming(uint8_t bearer_index, const char *to,
                           const char *from, const char *friendly_name);

int bt_tbs_set_bearer_provider_name(uint8_t bearer_index, const char *name);

int bt_tbs_set_bearer_technology(uint8_t bearer_index, enum bt_bearer_tech new_technology);

int bt_tbs_set_signal_strength(uint8_t bearer_index,
                               uint8_t new_signal_strength);

int bt_tbs_set_status_flags(uint8_t bearer_index, uint16_t status_flags);

int bt_tbs_set_uri_scheme_list(uint8_t bearer_index, const char *uri_scheme_list);
void bt_tbs_register_cb(struct bt_tbs_cb *cbs);

struct bt_tbs_register_param {
        char *provider_name;

        char *uci;

        char *uri_schemes_supported;

        enum bt_bearer_tech technology;

        bool gtbs;

        bool authorization_required;

        uint16_t optional_opcodes;
};

int bt_tbs_register_bearer(const struct bt_tbs_register_param *param);

int bt_tbs_unregister_bearer(uint8_t bearer_index);

void bt_tbs_dbg_print_calls(void);

struct bt_tbs_client_call_state {
        uint8_t index;
        uint8_t state;
        uint8_t flags;
} __packed;

struct bt_tbs_client_call {
        struct bt_tbs_client_call_state call_info;
        char *remote_uri;
};

typedef void (*bt_tbs_client_discover_cb)(struct bt_conn *conn, int err,
                                          uint8_t tbs_count, bool gtbs_found);

typedef void (*bt_tbs_client_write_value_cb)(struct bt_conn *conn, int err,
                                             uint8_t inst_index);

typedef void (*bt_tbs_client_cp_cb)(struct bt_conn *conn, int err,
                                    uint8_t inst_index, uint8_t call_index);

typedef void (*bt_tbs_client_read_string_cb)(struct bt_conn *conn, int err,
                                             uint8_t inst_index,
                                             const char *value);

typedef void (*bt_tbs_client_read_value_cb)(struct bt_conn *conn, int err,
                                            uint8_t inst_index, uint32_t value);

typedef void (*bt_tbs_client_termination_reason_cb)(struct bt_conn *conn,
                                                    int err, uint8_t inst_index,
                                                    uint8_t call_index,
                                                    uint8_t reason);

typedef void (*bt_tbs_client_current_calls_cb)(struct bt_conn *conn, int err,
                                               uint8_t inst_index,
                                               uint8_t call_count,
                                               const struct bt_tbs_client_call *calls);

typedef void (*bt_tbs_client_call_states_cb)(struct bt_conn *conn, int err,
                                             uint8_t inst_index,
                                             uint8_t call_count,
                                             const struct bt_tbs_client_call_state *call_states);

struct bt_tbs_client_cb {
        bt_tbs_client_discover_cb            discover;
#if defined(CONFIG_BT_TBS_CLIENT_ORIGINATE_CALL) || defined(__DOXYGEN__)
        bt_tbs_client_cp_cb                  originate_call;
#endif /* defined(CONFIG_BT_TBS_CLIENT_ORIGINATE_CALL) */
#if defined(CONFIG_BT_TBS_CLIENT_TERMINATE_CALL) || defined(__DOXYGEN__)
        bt_tbs_client_cp_cb                  terminate_call;
#endif /* defined(CONFIG_BT_TBS_CLIENT_TERMINATE_CALL) */
#if defined(CONFIG_BT_TBS_CLIENT_HOLD_CALL) || defined(__DOXYGEN__)
        bt_tbs_client_cp_cb                  hold_call;
#endif /* defined(CONFIG_BT_TBS_CLIENT_HOLD_CALL) */
#if defined(CONFIG_BT_TBS_CLIENT_ACCEPT_CALL) || defined(__DOXYGEN__)
        bt_tbs_client_cp_cb                  accept_call;
#endif /* defined(CONFIG_BT_TBS_CLIENT_ACCEPT_CALL) */
#if defined(CONFIG_BT_TBS_CLIENT_RETRIEVE_CALL) || defined(__DOXYGEN__)
        bt_tbs_client_cp_cb                  retrieve_call;
#endif /* defined(CONFIG_BT_TBS_CLIENT_RETRIEVE_CALL) */
#if defined(CONFIG_BT_TBS_CLIENT_JOIN_CALLS) || defined(__DOXYGEN__)
        bt_tbs_client_cp_cb                  join_calls;
#endif /* defined(CONFIG_BT_TBS_CLIENT_JOIN_CALLS) */
#if defined(CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME) || defined(__DOXYGEN__)
        bt_tbs_client_read_string_cb         bearer_provider_name;
#endif /* defined(CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME) */
#if defined(CONFIG_BT_TBS_CLIENT_BEARER_UCI) || defined(__DOXYGEN__)
        bt_tbs_client_read_string_cb         bearer_uci;
#endif /* defined(CONFIG_BT_TBS_CLIENT_BEARER_UCI) */
#if defined(CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY) || defined(__DOXYGEN__)
        void (*technology)(struct bt_conn *conn, int err, uint8_t inst_index,
                           enum bt_bearer_tech tech);
#endif /* defined(CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY) */
#if defined(CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST) || defined(__DOXYGEN__)
        bt_tbs_client_read_string_cb         uri_list;
#endif /* defined(CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST) */
#if defined(CONFIG_BT_TBS_CLIENT_BEARER_SIGNAL_STRENGTH) || defined(__DOXYGEN__)
        bt_tbs_client_read_value_cb          signal_strength;
#endif /* defined(CONFIG_BT_TBS_CLIENT_BEARER_SIGNAL_STRENGTH) */
#if defined(CONFIG_BT_TBS_CLIENT_READ_BEARER_SIGNAL_INTERVAL) || defined(__DOXYGEN__)
        bt_tbs_client_read_value_cb          signal_interval;
#endif /* defined(CONFIG_BT_TBS_CLIENT_READ_BEARER_SIGNAL_INTERVAL) */
#if defined(CONFIG_BT_TBS_CLIENT_BEARER_LIST_CURRENT_CALLS) || defined(__DOXYGEN__)
        bt_tbs_client_current_calls_cb       current_calls;
#endif /* defined(CONFIG_BT_TBS_CLIENT_BEARER_LIST_CURRENT_CALLS) */
#if defined(CONFIG_BT_TBS_CLIENT_CCID) || defined(__DOXYGEN__)
        bt_tbs_client_read_value_cb          ccid;
#endif /* defined(CONFIG_BT_TBS_CLIENT_CCID) */
#if defined(CONFIG_BT_TBS_CLIENT_INCOMING_URI) || defined(__DOXYGEN__)
        bt_tbs_client_read_string_cb         call_uri;
#endif /* defined(CONFIG_BT_TBS_CLIENT_INCOMING_URI) */
#if defined(CONFIG_BT_TBS_CLIENT_STATUS_FLAGS) || defined(__DOXYGEN__)
        bt_tbs_client_read_value_cb          status_flags;
#endif /* defined(CONFIG_BT_TBS_CLIENT_STATUS_FLAGS) */
        bt_tbs_client_call_states_cb         call_state;
#if defined(CONFIG_BT_TBS_CLIENT_OPTIONAL_OPCODES) || defined(__DOXYGEN__)
        bt_tbs_client_read_value_cb          optional_opcodes;
#endif /* defined(CONFIG_BT_TBS_CLIENT_OPTIONAL_OPCODES) */
        bt_tbs_client_termination_reason_cb  termination_reason;
#if defined(CONFIG_BT_TBS_CLIENT_INCOMING_CALL) || defined(__DOXYGEN__)
        bt_tbs_client_read_string_cb         remote_uri;
#endif /* defined(CONFIG_BT_TBS_CLIENT_INCOMING_CALL) */
#if defined(CONFIG_BT_TBS_CLIENT_CALL_FRIENDLY_NAME) || defined(__DOXYGEN__)
        bt_tbs_client_read_string_cb         friendly_name;
#endif /* defined(CONFIG_BT_TBS_CLIENT_CALL_FRIENDLY_NAME) */

        sys_snode_t _node;
};

int bt_tbs_client_discover(struct bt_conn *conn);

int bt_tbs_client_set_outgoing_uri(struct bt_conn *conn, uint8_t inst_index,
                                   const char *uri);

int bt_tbs_client_set_signal_strength_interval(struct bt_conn *conn,
                                               uint8_t inst_index,
                                               uint8_t interval);

int bt_tbs_client_originate_call(struct bt_conn *conn, uint8_t inst_index,
                                 const char *uri);

int bt_tbs_client_terminate_call(struct bt_conn *conn, uint8_t inst_index,
                                 uint8_t call_index);

int bt_tbs_client_hold_call(struct bt_conn *conn, uint8_t inst_index,
                            uint8_t call_index);

int bt_tbs_client_accept_call(struct bt_conn *conn, uint8_t inst_index,
                              uint8_t call_index);

int bt_tbs_client_retrieve_call(struct bt_conn *conn, uint8_t inst_index,
                                uint8_t call_index);

int bt_tbs_client_join_calls(struct bt_conn *conn, uint8_t inst_index,
                             const uint8_t *call_indexes, uint8_t count);

int bt_tbs_client_read_bearer_provider_name(struct bt_conn *conn,
                                            uint8_t inst_index);

int bt_tbs_client_read_bearer_uci(struct bt_conn *conn, uint8_t inst_index);

int bt_tbs_client_read_technology(struct bt_conn *conn, uint8_t inst_index);

int bt_tbs_client_read_uri_list(struct bt_conn *conn, uint8_t inst_index);

int bt_tbs_client_read_signal_strength(struct bt_conn *conn,
                                       uint8_t inst_index);

int bt_tbs_client_read_signal_interval(struct bt_conn *conn,
                                       uint8_t inst_index);

int bt_tbs_client_read_current_calls(struct bt_conn *conn, uint8_t inst_index);

int bt_tbs_client_read_ccid(struct bt_conn *conn, uint8_t inst_index);

int bt_tbs_client_read_call_uri(struct bt_conn *conn, uint8_t inst_index);

int bt_tbs_client_read_status_flags(struct bt_conn *conn, uint8_t inst_index);

int bt_tbs_client_read_call_state(struct bt_conn *conn, uint8_t inst_index);

int bt_tbs_client_read_remote_uri(struct bt_conn *conn, uint8_t inst_index);

int bt_tbs_client_read_friendly_name(struct bt_conn *conn, uint8_t inst_index);

int bt_tbs_client_read_optional_opcodes(struct bt_conn *conn,
                                        uint8_t inst_index);

int bt_tbs_client_register_cb(struct bt_tbs_client_cb *cbs);

struct bt_tbs_instance *bt_tbs_client_get_by_ccid(const struct bt_conn *conn,
                                                  uint8_t ccid);

struct bt_tbs_instance *bt_tbs_client_get_by_index(const struct bt_conn *conn, uint8_t index);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_TBS_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 686 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_ORIGINATE_CALL)`。

### 注释 2：原第 690 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_TERMINATE_CALL)`。

### 注释 3：原第 694 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_HOLD_CALL)`。

### 注释 4：原第 698 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_ACCEPT_CALL)`。

### 注释 5：原第 702 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_RETRIEVE_CALL)`。

### 注释 6：原第 706 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_JOIN_CALLS)`。

### 注释 7：原第 710 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_BEARER_PROVIDER_NAME)`。

### 注释 8：原第 714 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_BEARER_UCI)`。

### 注释 9：原第 726 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_BEARER_TECHNOLOGY)`。

### 注释 10：原第 730 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_BEARER_URI_SCHEMES_SUPPORTED_LIST)`。

### 注释 11：原第 734 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_BEARER_SIGNAL_STRENGTH)`。

### 注释 12：原第 738 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_READ_BEARER_SIGNAL_INTERVAL)`。

### 注释 13：原第 742 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_BEARER_LIST_CURRENT_CALLS)`。

### 注释 14：原第 746 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_CCID)`。

### 注释 15：原第 750 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_INCOMING_URI)`。

### 注释 16：原第 754 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_STATUS_FLAGS)`。

### 注释 17：原第 760 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_OPTIONAL_OPCODES)`。

### 注释 18：原第 766 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_INCOMING_CALL)`。

### 注释 19：原第 770 行

条件编译标记：`defined(CONFIG_BT_TBS_CLIENT_CALL_FRIENDLY_NAME)`。

### 注释 20：原第 1131 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_TBS_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [bt_tbs_instance](../bluetooth_service_model_reference/P176_bt_tbs_instance_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [bt_tbs_originate_call_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga60e9e143f247bb7e668293f0233ce300)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_tbs_terminate_call_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga69e93b48b2a48e8a6552882660b791cc)
- [bt_tbs_join_calls_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa45b3f4837165d722c2df6f202a39058)
- [bt_tbs_call_change_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga2fa85f3cd96f25f6bb4f449fc9210fa1)
- [bt_tbs_authorize_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga1cc9e7140531b07bf6a8dedbc17f24c0)
- [bt_tbs_cb](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md)
- [originate_call](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#a566504bee9c7334c53a23223e544855f)
- [terminate_call](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#ab065a5c58db19feb2a1d3013983ed5aa)
- [hold_call](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#a8b76dd9243e97d22e0d6c2ac578aa383)
- [accept_call](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#a798c09c04a563800c4d9328c1d9e2de6)
- [retrieve_call](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#ad543a2f26d1749eba0774e2352b53692)
- [join_calls](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#ac1a99a703687a3ef5ebc12eca5f6c2e7)
- [authorize](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#ab7c859ffaebcf16db71c5d54bd4f5802)
- [bt_tbs_accept](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga1b942bcf8287641f9cd53824b4d6e77b)
- [bt_tbs_hold](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab72044a1f5466114b5efb88dfcd2f097)
- [bt_tbs_retrieve](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gad0b45af09b82d6cd66a8481c0e67e04e)
- [bt_tbs_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga82553640882ac74f9af84bfe09ff47ee)
- [bt_tbs_originate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gadeae51d7cecd80abcdcde1195bb1dfba)
- [bt_tbs_join](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga23226d41e3b98a53ec9a9c2fa346c9ac)
- [bt_tbs_remote_answer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga868b83450f7425e8a0c8cfb7c1de45d8)
- [bt_tbs_remote_hold](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga5ffa1a3e3b548d90a3b6a07c6bb4fc7e)
- [bt_tbs_remote_retrieve](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga09a3e64040819b6b8b694b94d2f62ca0)
- [bt_tbs_remote_terminate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga52afc7b8a22b071dbac10057579f319c)
- [bt_tbs_remote_incoming](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga47939f557e4d6503af9b7b85aff9d60f)
- [bt_tbs_set_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga5118db6b23b387956e75eda8aecd53d5)
- [bt_tbs_set_bearer_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa77ea977fca9833d1755d5084a3f352c)
- [bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)
- [bt_tbs_set_signal_strength](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gac316adedf7fda441ee55feb9d24d1a94)
- [bt_tbs_set_status_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga838e51a85f9833e0822090cd3df09e00)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_tbs_set_uri_scheme_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gae413f94b141b6fa8233de15c36f6327a)
- [bt_tbs_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga76f120dba549225a6f2c2c22be08edfc)
- [bt_tbs_register_param](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md)
- [provider_name](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#a8cf7713269e8bb193c61be01d6971922)
- [uci](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#ab7a0dc41a9e4c898ffd1afaffdfae51d)
- [uri_schemes_supported](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#a4ffe59cd6d00b9b45db304b17efa22b0)
- [technology](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#a54352a512eeb209d0254a8f395647f87)
- [gtbs](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#aa38a646b7121b555846f7acea9bc9365)
- [authorization_required](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#af88bfd0ac0e83f94e9e467064b4c6c32)
- [optional_opcodes](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#a004fc8f70cff59acf0122135bdd27065)
- [bt_tbs_register_bearer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga970c970bedd6e94aa4c92479183554e9)
- [bt_tbs_unregister_bearer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga8edd4d31478ed9e0aedbd1a34bdfca96)
- [bt_tbs_dbg_print_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga62f5008cbfba158fe399cfaf683d1d2e)
- [bt_tbs_client_call_state](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md)
- [index](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md#a3d6eb4dda7adcd16c04ebbd41242c292)
- [state](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md#a3e758ad6d0b35f26f43584e50c9a9895)
- [flags](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md#a57ed9dd726faa3c219e1c858ad6659d9)
- [bt_tbs_client_call](../bluetooth_service_model_reference/P173_bt_tbs_client_call_结构体.md)
- [call_info](../bluetooth_service_model_reference/P173_bt_tbs_client_call_结构体.md#a480279fea551db1bcb260de81edd6571)
- [remote_uri](../bluetooth_service_model_reference/P173_bt_tbs_client_call_结构体.md#af04f0576e786250526c12e1436a60c4e)
- [bt_tbs_client_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga9cac11cc696be9fb387f2f7685e0d8a7)
- [bt_tbs_client_write_value_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaf77231168e4444da7aef203cc9eaca95)
- [bt_tbs_client_cp_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga40b8b3d1b318a1b5c5524877bbc2f90f)
- [bt_tbs_client_read_string_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4d7632de7c2006e478880950076908a9)
- [bt_tbs_client_read_value_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga600051910ed538a2da823554df23dd20)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_tbs_client_termination_reason_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab881b3caaaa4425e52afd84e53adee78)
- [bt_tbs_client_current_calls_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga7b31e1c30fa96081a3ef38e1a481b64f)
- [bt_tbs_client_call_states_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga262ca74b7ae2f0c52657066549fa4f92)
- [bt_tbs_client_cb](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md)
- [discover](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#abfd4542a0781ff5676a191249f121e91)
- [originate_call](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a0bc51181f188a1249407f2e50431d9fd)
- [terminate_call](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#aa78425597fe7fd0db09d69c3ed757293)
- [hold_call](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a304a5fd373f1ba5ccb2eb77fcdbbd380)
- [accept_call](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a41242d76c976eef102d480965f977537)
- [retrieve_call](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a2a5fb7de5c3c4aab290c0163c0b40858)
- [join_calls](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a2d6b7acd90d05c61f60f27236ab6f1ee)
- [bearer_provider_name](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a36d8ea1717e57b9440e9b58e9411422a)
- [bearer_uci](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a15ccb7de457631620983e7d2d0372967)
- [technology](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a596b31583975c416aa9cb6d64301c55f)
- [uri_list](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a7f64cf8e3d0bc4ec21c44bd4fea6d7ee)
- [signal_strength](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a96df90461159f97f5dc8cbb72cd0cbc4)
- [signal_interval](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a01426c4a84e71a9395cce2963e2e83a3)
- [current_calls](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a10dc9404533db388b3ae1058542efd66)
- [ccid](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a90acde153f8893b5cba891884529d86c)
- [call_uri](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#ae95494a76e1f3275f48204dcd4798712)
- [status_flags](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a94c3bfc1e88518de9e29e947064ec8dc)
- [call_state](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a88cb69ef54c9399bceb5641202eeabce)
- [optional_opcodes](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a91c61b29c16a43fd3f781fd7e0ab4618)
- [termination_reason](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#ae8e5cbe52cbb300e1cd919d24c85c4df)
- [remote_uri](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a354ba5d21376813adc5c9765a5da1a09)
- [friendly_name](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#ad2089050db76453b7f9c51c3d2fa4d17)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bt_tbs_client_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gac59f3dec092a14bdf234039e3dcd12eb)
- [bt_tbs_client_set_outgoing_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga3a71c51d464aa19fbfbd2d60fc4901bc)
- [bt_tbs_client_set_signal_strength_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa1dcb9908057d75a54fa447639826f3c)
- [bt_tbs_client_originate_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga0aac704008ffc92ce6609d3ffffc4523)
- [bt_tbs_client_terminate_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga25b803bb5cae2e1a8b0398bc48137d80)
- [bt_tbs_client_hold_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga23e825de6af71d4e456b63c3a621fb61)
- [bt_tbs_client_accept_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga625fc73885c2bfd63f0f4b2d7f72eaef)
- [bt_tbs_client_retrieve_call](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gabbe194a63da0b95dc1dca0337560a585)
- [bt_tbs_client_join_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaae1925deb0b5865af601aa8278ffb10a)
- [bt_tbs_client_read_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga2053a9eb7cf28f66febd365f0b682be0)
- [bt_tbs_client_read_bearer_uci](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaba92039d3b44da9163a22400951fafa7)
- [bt_tbs_client_read_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga7684dbcb78e407f7002d44fbdb805e5d)
- [bt_tbs_client_read_uri_list](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gad19db25591c7ae5bd0b4c2bbaefc9bed)
- [bt_tbs_client_read_signal_strength](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaabe97df55817b8e36c79de4bf30fc83f)
- [bt_tbs_client_read_signal_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga38046c5c715d451b21a3076742268010)
- [bt_tbs_client_read_current_calls](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga895c7f54300e5452fb8d0c9d4b3306ae)
- [bt_tbs_client_read_ccid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gac070ec0590df5820b7721d579ceeeb15)
- [bt_tbs_client_read_call_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga4238a37b80b7d7ff611fe9b02b7cf54d)
- [bt_tbs_client_read_status_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga9fe91df1a31ce59401347fc0eac2b701)
- [bt_tbs_client_read_call_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gafeaaaefb9d4eb773dd0cbdfebe26e0b7)
- [bt_tbs_client_read_remote_uri](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gab04f8355c32fce501bd757b75ee9d38a)
- [bt_tbs_client_read_friendly_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga99549dd6244580e157006fb17772fd8f)
- [bt_tbs_client_read_optional_opcodes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaf504e1a11352d77a36aa087b587e4ba8)
- [bt_tbs_client_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gabe2251d4ea88306793dc68ae683886bb)
- [bt_tbs_client_get_by_ccid](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaadae501fa6f7771bb9661af829805a5f)
- [bt_tbs_client_get_by_index](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga20c6780a4624707a537e905e889510ca)
- [assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [bt_tbs_cb::originate_call](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#a566504bee9c7334c53a23223e544855f)
- [bt_tbs_cb::accept_call](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#a798c09c04a563800c4d9328c1d9e2de6)
- [bt_tbs_cb::hold_call](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#a8b76dd9243e97d22e0d6c2ac578aa383)
- [bt_tbs_cb::terminate_call](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#ab065a5c58db19feb2a1d3013983ed5aa)
- [bt_tbs_cb::authorize](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#ab7c859ffaebcf16db71c5d54bd4f5802)
- [bt_tbs_cb::join_calls](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#ac1a99a703687a3ef5ebc12eca5f6c2e7)
- [bt_tbs_cb::retrieve_call](../bluetooth_service_model_reference/P172_bt_tbs_cb_结构体.md#ad543a2f26d1749eba0774e2352b53692)
- [bt_tbs_client_call_state::index](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md#a3d6eb4dda7adcd16c04ebbd41242c292)
- [bt_tbs_client_call_state::state](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md#a3e758ad6d0b35f26f43584e50c9a9895)
- [bt_tbs_client_call_state::flags](../bluetooth_service_model_reference/P174_bt_tbs_client_call_state_结构体.md#a57ed9dd726faa3c219e1c858ad6659d9)
- [bt_tbs_client_call::call_info](../bluetooth_service_model_reference/P173_bt_tbs_client_call_结构体.md#a480279fea551db1bcb260de81edd6571)
- [bt_tbs_client_call::remote_uri](../bluetooth_service_model_reference/P173_bt_tbs_client_call_结构体.md#af04f0576e786250526c12e1436a60c4e)
- [bt_tbs_client_cb::signal_interval](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a01426c4a84e71a9395cce2963e2e83a3)
- [bt_tbs_client_cb::originate_call](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a0bc51181f188a1249407f2e50431d9fd)
- [bt_tbs_client_cb::current_calls](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a10dc9404533db388b3ae1058542efd66)
- [bt_tbs_client_cb::bearer_uci](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a15ccb7de457631620983e7d2d0372967)
- [bt_tbs_client_cb::retrieve_call](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a2a5fb7de5c3c4aab290c0163c0b40858)
- [bt_tbs_client_cb::join_calls](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a2d6b7acd90d05c61f60f27236ab6f1ee)
- [bt_tbs_client_cb::hold_call](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a304a5fd373f1ba5ccb2eb77fcdbbd380)
- [bt_tbs_client_cb::remote_uri](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a354ba5d21376813adc5c9765a5da1a09)
- [bt_tbs_client_cb::bearer_provider_name](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a36d8ea1717e57b9440e9b58e9411422a)
- [bt_tbs_client_cb::accept_call](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a41242d76c976eef102d480965f977537)
- [bt_tbs_client_cb::technology](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a596b31583975c416aa9cb6d64301c55f)
- [bt_tbs_client_cb::uri_list](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a7f64cf8e3d0bc4ec21c44bd4fea6d7ee)
- [bt_tbs_client_cb::call_state](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a88cb69ef54c9399bceb5641202eeabce)
- [bt_tbs_client_cb::ccid](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a90acde153f8893b5cba891884529d86c)
- [bt_tbs_client_cb::optional_opcodes](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a91c61b29c16a43fd3f781fd7e0ab4618)
- [bt_tbs_client_cb::status_flags](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a94c3bfc1e88518de9e29e947064ec8dc)
- [bt_tbs_client_cb::signal_strength](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#a96df90461159f97f5dc8cbb72cd0cbc4)
- [bt_tbs_client_cb::terminate_call](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#aa78425597fe7fd0db09d69c3ed757293)
- [bt_tbs_client_cb::discover](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#abfd4542a0781ff5676a191249f121e91)
- [bt_tbs_client_cb::friendly_name](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#ad2089050db76453b7f9c51c3d2fa4d17)
- [bt_tbs_client_cb::termination_reason](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#ae8e5cbe52cbb300e1cd919d24c85c4df)
- [bt_tbs_client_cb::call_uri](../bluetooth_service_model_reference/P175_bt_tbs_client_cb_结构体.md#ae95494a76e1f3275f48204dcd4798712)
- [bt_tbs_register_param::optional_opcodes](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#a004fc8f70cff59acf0122135bdd27065)
- [bt_tbs_register_param::uri_schemes_supported](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#a4ffe59cd6d00b9b45db304b17efa22b0)
- [bt_tbs_register_param::technology](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#a54352a512eeb209d0254a8f395647f87)
- [bt_tbs_register_param::provider_name](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#a8cf7713269e8bb193c61be01d6971922)
- [bt_tbs_register_param::gtbs](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#aa38a646b7121b555846f7acea9bc9365)
- [bt_tbs_register_param::uci](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#ab7a0dc41a9e4c898ffd1afaffdfae51d)
- [bt_tbs_register_param::authorization_required](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md#af88bfd0ac0e83f94e9e467064b4c6c32)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P006_socket.h_源码浏览.md) · [返回大纲](大纲.md)
