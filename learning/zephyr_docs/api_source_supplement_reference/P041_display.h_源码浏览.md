---
id: learning.zephyr-docs.api-source-supplement-reference.page-41
title: display.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2display_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_display.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2display_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2display_8h.html)。

## 41.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
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
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="foldopen00278"></a>
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
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="foldopen00299"></a>
<a id="l00299"></a>
<a id="l00304"></a>
<a id="l00309"></a>
<a id="l00313"></a>
<a id="l00317"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="foldopen00327"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="foldopen00337"></a>
<a id="l00337"></a>
<a id="l00339"></a>
<a id="l00341"></a>
<a id="l00343"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="foldopen00351"></a>
<a id="l00351"></a>
<a id="l00353"></a>
<a id="l00355"></a>
<a id="l00357"></a>
<a id="l00359"></a>
<a id="l00361"></a>
<a id="l00363"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="foldopen00373"></a>
<a id="l00373"></a>
<a id="l00375"></a>
<a id="l00377"></a>
<a id="l00379"></a>
<a id="l00381"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="foldopen00387"></a>
<a id="l00387"></a>
<a id="l00391"></a>
<a id="l00393"></a>
<a id="l00395"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="foldopen00402"></a>
<a id="l00402"></a>
<a id="l00404"></a>
<a id="l00406"></a>
<a id="l00408"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="foldopen00416"></a>
<a id="l00416"></a>
<a id="l00418"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00449"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="foldopen00548"></a>
<a id="l00548"></a>
<a id="l00552"></a>
<a id="l00556"></a>
<a id="l00560"></a>
<a id="l00564"></a>
<a id="l00568"></a>
<a id="l00572"></a>
<a id="l00576"></a>
<a id="l00580"></a>
<a id="l00584"></a>
<a id="l00588"></a>
<a id="l00592"></a>
<a id="l00596"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00605"></a>
<a id="foldopen00622"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="foldopen00645"></a>
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
<a id="foldopen00667"></a>
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
<a id="foldopen00687"></a>
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
<a id="foldopen00718"></a>
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
<a id="foldopen00742"></a>
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
<a id="foldopen00766"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="foldopen00790"></a>
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
<a id="foldopen00807"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00814"></a>
<a id="l00815"></a>
<a id="l00829"></a>
<a id="foldopen00830"></a>
<a id="l00830"></a>
<a id="l00831"></a>
<a id="l00832"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00836"></a>
<a id="l00837"></a>
<a id="l00838"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="foldopen00853"></a>
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
<a id="foldopen00890"></a>
<a id="l00890"></a>
<a id="l00891"></a>
<a id="l00892"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00896"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="l00899"></a>
<a id="l00900"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00903"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00907"></a>
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="foldopen00926"></a>
<a id="l00926"></a>
<a id="l00927"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="l00933"></a>
<a id="l00934"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="l00938"></a>
<a id="l00939"></a>
<a id="l00940"></a>
<a id="l00941"></a>
<a id="l00942"></a>
<a id="l00943"></a>
<a id="l00944"></a>
<a id="l00948"></a>
<a id="l00949"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__display__interface__backend_html_ga2637286cf3a97c2b532bb33f22263303"></a>
<a id="agroup__display__interface__backend_html_ga474f85a33aef019dddb1c720ea23f3fb"></a>
<a id="agroup__display__interface__backend_html_ga5cab904b24062fdea531f450a8e5c367"></a>
<a id="agroup__display__interface__backend_html_ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a"></a>
<a id="agroup__display__interface__backend_html_ga6dd281032ad400d3adc7f5f812c5fe12"></a>
<a id="agroup__display__interface__backend_html_ga9ed51d3f666f747d9fb7f1f7746611b3"></a>
<a id="agroup__display__interface__backend_html_gab23bbd9305792d6e37d2e4ff91a2b175"></a>
<a id="agroup__display__interface__backend_html_gac0a36d044e4663ab5ee61d1e11d645d0"></a>
<a id="agroup__display__interface__backend_html_gacf66a054396ccd8e178591b8fc98ff4d"></a>
<a id="agroup__display__interface__backend_html_gadd468c71193663072489f32885bc30e5"></a>
<a id="agroup__display__interface__backend_html_gadf115352908f94b0a0bf225dbdd8ee85"></a>
<a id="agroup__display__interface__backend_html_gaf42820ae69452788bf51f37512ca8586"></a>
<a id="agroup__display__interface__backend_html_gaff3b76a6601cf176782be940139ccb48"></a>
<a id="agroup__display__interface_html_ga0042f460c729a5b11ed59f4aac609212"></a>
<a id="agroup__display__interface_html_ga23030b6c27446c4579103fe38e821341"></a>
<a id="agroup__display__interface_html_ga3a5114b4537039fc4d3258678b82cd18"></a>
<a id="agroup__display__interface_html_ga3f497776520b0eac16b8aea80ccbbcfc"></a>
<a id="agroup__display__interface_html_ga4b66d380e46909caaa7317857f84a9e8"></a>
<a id="agroup__display__interface_html_ga4d9e288891a6bde679c3aa00b9913e1d"></a>
<a id="agroup__display__interface_html_ga4e0a4dc2e434144874af014b8e7c4394"></a>
<a id="agroup__display__interface_html_ga5c3bcf15b62c66c1677e51a10451efe5"></a>
<a id="agroup__display__interface_html_ga62a6cd9e338aa07f789de60e64d3b3c4"></a>
<a id="agroup__display__interface_html_ga6a13e42773be13b141ebd8f047f8db50"></a>
<a id="agroup__display__interface_html_ga7ede828663090760c2558a231d9f2150"></a>
<a id="agroup__display__interface_html_ga855c72f72238b25f23e95e50546e2f27"></a>
<a id="agroup__display__interface_html_ga99b7e7da6b85bee97398a8a9b161c777"></a>
<a id="agroup__display__interface_html_gaa4e433439206bc426db363c64882a395"></a>
<a id="agroup__display__interface_html_gac346bc56771052a8fe919c3ec23d7c9c"></a>
<a id="agroup__display__interface_html_gac59b091a3ed39431ab97a5f19fdc4855"></a>
<a id="agroup__display__interface_html_gac6ad1f33067165e4c3bf7c0c345bb4e4"></a>
<a id="agroup__display__interface_html_gad5cdeb245d17c8d680a5843b3cce1f8c"></a>
<a id="agroup__display__interface_html_gadca2fe10ecb27b5e82309bbab5e886ee"></a>
<a id="agroup__display__interface_html_gga0042f460c729a5b11ed59f4aac609212a456bc992ffdf5604828b7280f94dd649"></a>
<a id="agroup__display__interface_html_gga0042f460c729a5b11ed59f4aac609212a4aecf6d165ca2ec432297cc5664c24a6"></a>
<a id="agroup__display__interface_html_gga0042f460c729a5b11ed59f4aac609212abd4e3c24f05c2484137855349d6cf794"></a>
<a id="agroup__display__interface_html_gga0042f460c729a5b11ed59f4aac609212acb5772017ec3e4d6677fee78295a379c"></a>
<a id="agroup__display__interface_html_gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1"></a>
<a id="agroup__display__interface_html_gga23030b6c27446c4579103fe38e821341ac65e80206de09cb63e871ce18deefb85"></a>
<a id="agroup__display__interface_html_gga23030b6c27446c4579103fe38e821341ad22c69026d0b4573aaebe0b3ef274842"></a>
<a id="agroup__display__interface_html_gga23030b6c27446c4579103fe38e821341ade1ec91a372b3b2208ebf5729184b804"></a>
<a id="agroup__display__interface_html_gga23030b6c27446c4579103fe38e821341ade5bb2006e547450bac0edaa2a8b9c7d"></a>
<a id="agroup__display__interface_html_gga5c3bcf15b62c66c1677e51a10451efe5abc630229e82e4e5d7ef50ec4c8e6aff7"></a>
<a id="agroup__display__interface_html_gga5c3bcf15b62c66c1677e51a10451efe5ad79be33d4e885b6745feebebc3636dfc"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9ca015155116919cac3eff289764e9574d8"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9ca049f2930dfd1efadfb17a113ba0d879d"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9ca0d12a0b6fd3df29b0a607eedf7671809"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9ca142784152249100847b0e5c6d656191c"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9ca14f33dfec4a630f5be50622a535434df"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9ca20bb97558d4acdf225a157c40d9058ab"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9ca4625a834a26894db2da3547635a6e172"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9ca5c905dcfaca35e58c14513f2e3a61091"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9ca92f4901daf73e26c4290e656e7afeb2f"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9ca9de42e120e50119c2df1c503ed2e7a28"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a"></a>
<a id="agroup__display__interface_html_ggac346bc56771052a8fe919c3ec23d7c9cacaed33ee4be17042d45cf238ac49df6a"></a>
<a id="agroup__display__interface_html_ggac59b091a3ed39431ab97a5f19fdc4855a632483591b572c0945df3f65cb4e52bc"></a>
<a id="agroup__display__interface_html_ggac59b091a3ed39431ab97a5f19fdc4855a7f71ba80f09d5b17f7cdfa7456ed0e29"></a>
<a id="agroup__display__interface_html_ggac59b091a3ed39431ab97a5f19fdc4855adb3975e2caf6c28374e20a5e0ac26ed2"></a>
<a id="agroup__display__interface_html_ggac59b091a3ed39431ab97a5f19fdc4855af81128a85915f41c22bc0581f51455b4"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="apanel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astring_8h_html_a4137694174d4ca2fad886a1db355015c"></a>
<a id="astructdevice_html"></a>
<a id="astructdisplay__buffer__descriptor_html"></a>
<a id="astructdisplay__buffer__descriptor_html_a00d7d8da4e61f404ad353b9a8f49b2eb"></a>
<a id="astructdisplay__buffer__descriptor_html_a29e49359561cc0c601196eb9cf1f93b7"></a>
<a id="astructdisplay__buffer__descriptor_html_a572c6560903553b6853360fd29631b95"></a>
<a id="astructdisplay__buffer__descriptor_html_aa35cf372266199308211d28dae789be3"></a>
<a id="astructdisplay__buffer__descriptor_html_aee9f34a6944b8e28622ab06d6907d40a"></a>
<a id="astructdisplay__capabilities_html"></a>
<a id="astructdisplay__capabilities_html_a07548bdd9671dd696b38a5bcf1599412"></a>
<a id="astructdisplay__capabilities_html_a09fa14e2c53126d5602cb7b51e21145f"></a>
<a id="astructdisplay__capabilities_html_a13d647aa8d6331f17cbc567970b159e7"></a>
<a id="astructdisplay__capabilities_html_a18986f5d2c385766d5ad3d68edd85887"></a>
<a id="astructdisplay__capabilities_html_a2cacb194139aaff90fd56b469f6de4a9"></a>
<a id="astructdisplay__capabilities_html_ac4a9098db4c2f721fa550c6142f541a9"></a>
<a id="astructdisplay__capabilities_html_ad9a0b9f3cf2ffcb8a768071f4211cf3c"></a>
<a id="astructdisplay__capabilities_html_aed51c9efdc76972fecfa8a733c2a8d0c"></a>
<a id="astructdisplay__driver__api_html"></a>
<a id="astructdisplay__driver__api_html_a128c1324f4bfab707adc93aaff0f3371"></a>
<a id="astructdisplay__driver__api_html_a162599eece01dd31b2095048b15a42a9"></a>
<a id="astructdisplay__driver__api_html_a28801ba7578b9ab725c62b5f0d9f2c65"></a>
<a id="astructdisplay__driver__api_html_a431f765057a70e5d11ceaf93e8cc119a"></a>
<a id="astructdisplay__driver__api_html_a4cbccfaafeb2f24c473bd967b9bc5f14"></a>
<a id="astructdisplay__driver__api_html_a535221c00caef6f24dc75c919826a889"></a>
<a id="astructdisplay__driver__api_html_a736ece063a8a1a575aa28c53ed160193"></a>
<a id="astructdisplay__driver__api_html_a913e21f2f3cdf6c20d0b3d00ec698b12"></a>
<a id="astructdisplay__driver__api_html_aa40c04701b60f56c8998da55c2b254a8"></a>
<a id="astructdisplay__driver__api_html_aa7843031d91003dc458be4146503b7f0"></a>
<a id="astructdisplay__driver__api_html_aafdd79a11b46d4fa9288ddf3ed994c18"></a>
<a id="astructdisplay__driver__api_html_ace3a2eae73f639da890b6798bd215b29"></a>
<a id="astructdisplay__driver__api_html_acfdf1662c0b362d5a35a137c903a40ba"></a>
<a id="astructdisplay__event__data_html"></a>
<a id="astructdisplay__event__data_html_a2b3fd531cffae409845be4ee04d87c68"></a>
<a id="astructdisplay__event__data_html_a3fd29164cf76ef5f2fee818ac61af747"></a>
<a id="astructdisplay__event__data_html_a6bf7995a2713fbda0638c56a950b915a"></a>
<a id="astructdisplay__event__data_html_a7267cf1133ae4f076f4b927f0a3a4ced"></a>
<a id="astructdisplay__palette__color_html"></a>
<a id="astructdisplay__palette__color_html_a054840180d6a2417262bd87f3dca3c30"></a>
<a id="astructdisplay__palette__color_html_a246ca83b0bdfdef20d93f9439c8cfe19"></a>
<a id="astructdisplay__palette__color_html_ab443cff44dce74c21ad348875b45efe5"></a>
<a id="astructdisplay__palette__color_html_ab72b5252ecef18ff4fca49a196b10d1c"></a>

```c
/*
 * Copyright (c) 2017 Jan Van Winkel <jan.van_winkel@dxplore.eu>
 * SPDX-FileCopyrightText: 2026 Abderrahmane JARMOUNI
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_DISPLAY_H_
#define ZEPHYR_INCLUDE_DRIVERS_DISPLAY_H_


#include <zephyr/device.h>
#include <errno.h>
#include <stddef.h>
#include <zephyr/types.h>
#include <zephyr/dt-bindings/display/panel.h>

#ifdef __cplusplus
extern "C" {
#endif

enum display_pixel_format {
        PIXEL_FORMAT_RGB_888            = BIT(0),

        PIXEL_FORMAT_MONO01             = BIT(1),
        PIXEL_FORMAT_MONO10             = BIT(2),

        PIXEL_FORMAT_ARGB_8888          = BIT(3),

        PIXEL_FORMAT_RGB_565            = BIT(4),

        PIXEL_FORMAT_RGB_565X           = BIT(5),

        PIXEL_FORMAT_L_8                = BIT(6),

        PIXEL_FORMAT_AL_88              = BIT(7),

        PIXEL_FORMAT_XRGB_8888 = BIT(8),

        PIXEL_FORMAT_BGR_888 = BIT(9),

        PIXEL_FORMAT_ABGR_8888 = BIT(10),

        PIXEL_FORMAT_RGBA_8888 = BIT(11),

        PIXEL_FORMAT_BGRA_8888 = BIT(12),

        PIXEL_FORMAT_I_4 = BIT(13),

        PIXEL_FORMAT_L_4 = BIT(14),

        PIXEL_FORMAT_YUYV = BIT(15),
};

#define DISPLAY_BITS_PER_PIXEL(fmt)                                             \
        ((((fmt & PIXEL_FORMAT_RGB_888) >> 0) * 24U) +                          \
        (((fmt & PIXEL_FORMAT_MONO01) >> 1) * 1U) +                             \
        (((fmt & PIXEL_FORMAT_MONO10) >> 2) * 1U) +                             \
        (((fmt & PIXEL_FORMAT_ARGB_8888) >> 3) * 32U) +                         \
        (((fmt & PIXEL_FORMAT_RGB_565) >> 4) * 16U) +                           \
        (((fmt & PIXEL_FORMAT_RGB_565X) >> 5) * 16U) +                          \
        (((fmt & PIXEL_FORMAT_L_8) >> 6) * 8U) +                                \
        (((fmt & PIXEL_FORMAT_AL_88) >> 7) * 16U) +                             \
        (((fmt & PIXEL_FORMAT_XRGB_8888) >> 8) * 32U) +                         \
        (((fmt & PIXEL_FORMAT_BGR_888) >> 9) * 24U) +                           \
        (((fmt & PIXEL_FORMAT_ABGR_8888) >> 10) * 32U) +                        \
        (((fmt & PIXEL_FORMAT_RGBA_8888) >> 11) * 32U) +                        \
        (((fmt & PIXEL_FORMAT_BGRA_8888) >> 12) * 32U) +                        \
        (((fmt & PIXEL_FORMAT_I_4) >> 13) * 4U) +                               \
        (((fmt & PIXEL_FORMAT_L_4) >> 14) * 4U) +                               \
        (((fmt & PIXEL_FORMAT_YUYV) >> 15) * 16U))

enum display_screen_info {
        SCREEN_INFO_MONO_VTILED         = BIT(0),
        SCREEN_INFO_MONO_MSB_FIRST      = BIT(1),
        SCREEN_INFO_EPD                 = BIT(2),
        SCREEN_INFO_DOUBLE_BUFFER       = BIT(3),
        SCREEN_INFO_X_ALIGNMENT_WIDTH   = BIT(4),
};

enum display_orientation {
        DISPLAY_ORIENTATION_NORMAL,
        DISPLAY_ORIENTATION_ROTATED_90,
        DISPLAY_ORIENTATION_ROTATED_180,
        DISPLAY_ORIENTATION_ROTATED_270,
};

#if defined(CONFIG_DISPLAY_COLOR_PALETTE) || defined(__DOXYGEN__)

struct display_palette_color {
        uint8_t b;
        uint8_t g;
        uint8_t r;
        uint8_t a;
};

#endif /* defined(CONFIG_DISPLAY_COLOR_PALETTE) || defined(__DOXYGEN__) */

struct display_capabilities {
        uint16_t x_resolution;
        uint16_t y_resolution;
        uint32_t supported_pixel_formats;
        uint32_t screen_info;
        enum display_pixel_format current_pixel_format;
        enum display_orientation current_orientation;
        uint32_t supported_events;
#if defined(CONFIG_DISPLAY_COLOR_PALETTE) || defined(__DOXYGEN__)
        struct display_palette_color color_palette[CONFIG_DISPLAY_COLOR_PALETTE_MAX_SIZE];
#endif /* defined(CONFIG_DISPLAY_COLOR_PALETTE) || defined(__DOXYGEN__) */
};

struct display_buffer_descriptor {
        uint32_t buf_size;
        uint16_t width;
        uint16_t height;
        uint16_t pitch;
        bool frame_incomplete;
};

struct display_event_data {
        uint64_t timestamp;
        union {
                int line;
                int buffer_id;
        } info;
};

enum display_event {
        DISPLAY_EVENT_LINE_INT = BIT(0),
        DISPLAY_EVENT_VSYNC = BIT(1),
        DISPLAY_EVENT_FRAME_DONE = BIT(2),
        DISPLAY_EVENT_FIFO_UNDERFLOW = BIT(3),
};

enum display_event_result {
        DISPLAY_EVENT_RESULT_CONTINUE = 0,
        DISPLAY_EVENT_RESULT_HANDLED = 1,
};

typedef enum display_event_result (*display_event_cb_t)(const struct device *dev,
                                  uint32_t evt,
                                  const struct display_event_data *data,
                                  void *user_data);


typedef int (*display_blanking_on_api)(const struct device *dev);

typedef int (*display_blanking_off_api)(const struct device *dev);

typedef int (*display_write_api)(const struct device *dev, const uint16_t x,
                                 const uint16_t y,
                                 const struct display_buffer_descriptor *desc,
                                 const void *buf);

typedef int (*display_read_api)(const struct device *dev, const uint16_t x,
                                const uint16_t y,
                                const struct display_buffer_descriptor *desc,
                                void *buf);

typedef int (*display_clear_api)(const struct device *dev);

typedef void *(*display_get_framebuffer_api)(const struct device *dev);

typedef int (*display_set_brightness_api)(const struct device *dev,
                                          const uint8_t brightness);

typedef int (*display_set_contrast_api)(const struct device *dev,
                                        const uint8_t contrast);

typedef void (*display_get_capabilities_api)(const struct device *dev,
                                             struct display_capabilities *
                                             capabilities);

typedef int (*display_set_pixel_format_api)(const struct device *dev,
                                            const enum display_pixel_format
                                            pixel_format);

typedef int (*display_set_orientation_api)(const struct device *dev,
                                           const enum display_orientation
                                           orientation);

typedef int (*display_register_event_cb_api)(const struct device *dev,
                                             display_event_cb_t cb, void *user_data,
                                             uint32_t event_mask, bool in_isr,
                                             uint32_t *out_reg_handle);

typedef int (*display_unregister_event_cb_api)(const struct device *dev, uint32_t reg_handle);

__subsystem struct display_driver_api {
        display_blanking_on_api blanking_on;
        display_blanking_off_api blanking_off;
        display_write_api write;
        display_read_api read;
        display_clear_api clear;
        display_get_framebuffer_api get_framebuffer;
        display_set_brightness_api set_brightness;
        display_set_contrast_api set_contrast;
        display_get_capabilities_api get_capabilities;
        display_set_pixel_format_api set_pixel_format;
        display_set_orientation_api set_orientation;
        display_register_event_cb_api register_event_cb;
        display_unregister_event_cb_api unregister_event_cb;
};


static inline int display_write(const struct device *dev, const uint16_t x,
                                const uint16_t y,
                                const struct display_buffer_descriptor *desc,
                                const void *buf)
{
        return DEVICE_API_GET(display, dev)->write(dev, x, y, desc, buf);
}

static inline int display_read(const struct device *dev, const uint16_t x,
                               const uint16_t y,
                               const struct display_buffer_descriptor *desc,
                               void *buf)
{
        const struct display_driver_api *api = DEVICE_API_GET(display, dev);

        if (api->read == NULL) {
                return -ENOSYS;
        }

        return api->read(dev, x, y, desc, buf);
}

static inline int display_clear(const struct device *dev)
{
        const struct display_driver_api *api = DEVICE_API_GET(display, dev);

        if (api->clear == NULL) {
                return -ENOSYS;
        }

        return api->clear(dev);
}

static inline void *display_get_framebuffer(const struct device *dev)
{
        const struct display_driver_api *api = DEVICE_API_GET(display, dev);

        if (api->get_framebuffer == NULL) {
                return NULL;
        }

        return api->get_framebuffer(dev);
}

static inline int display_blanking_on(const struct device *dev)
{
        const struct display_driver_api *api = DEVICE_API_GET(display, dev);

        if (api->blanking_on == NULL) {
                return -ENOSYS;
        }

        return api->blanking_on(dev);
}

static inline int display_blanking_off(const struct device *dev)
{
        const struct display_driver_api *api = DEVICE_API_GET(display, dev);

        if (api->blanking_off == NULL) {
                return -ENOSYS;
        }

        return api->blanking_off(dev);
}

static inline int display_set_brightness(const struct device *dev,
                                         uint8_t brightness)
{
        const struct display_driver_api *api = DEVICE_API_GET(display, dev);

        if (api->set_brightness == NULL) {
                return -ENOSYS;
        }

        return api->set_brightness(dev, brightness);
}

static inline int display_set_contrast(const struct device *dev, uint8_t contrast)
{
        const struct display_driver_api *api = DEVICE_API_GET(display, dev);

        if (api->set_contrast == NULL) {
                return -ENOSYS;
        }

        return api->set_contrast(dev, contrast);
}

static inline void display_get_capabilities(const struct device *dev,
                                            struct display_capabilities *
                                            capabilities)
{
        __ASSERT(capabilities != NULL, "display_capabilities struct is NULL");
        memset(capabilities, 0, sizeof(struct display_capabilities));
        DEVICE_API_GET(display, dev)->get_capabilities(dev, capabilities);
}

static inline int
display_set_pixel_format(const struct device *dev,
                         const enum display_pixel_format pixel_format)
{
        const struct display_driver_api *api = DEVICE_API_GET(display, dev);

        if (api->set_pixel_format == NULL) {
                return -ENOSYS;
        }

        return api->set_pixel_format(dev, pixel_format);
}

static inline int display_set_orientation(const struct device *dev,
                                          const enum display_orientation
                                          orientation)
{
        const struct display_driver_api *api = DEVICE_API_GET(display, dev);

        if (api->set_orientation == NULL) {
                return -ENOSYS;
        }

        return api->set_orientation(dev, orientation);
}

static inline int display_register_event_cb(const struct device *dev,
                                            display_event_cb_t cb, void *user_data,
                                            uint32_t event_mask, bool in_isr,
                                            uint32_t *out_reg_handle)
{
        __ASSERT(cb != NULL, "Registration failed: callback function pointer is NULL");

        const struct display_driver_api *api = DEVICE_API_GET(display, dev);
        struct display_capabilities caps;

        if (api->register_event_cb == NULL) {
                return -ENOSYS;
        }

        display_get_capabilities(dev, &caps);
        if (!caps.supported_events) {
                return -ENOSYS;
        }
        if (event_mask == 0 || (~caps.supported_events & event_mask)) {
                return -EINVAL;
        }

        return api->register_event_cb(dev, cb, user_data, event_mask, in_isr, out_reg_handle);
}

static inline int display_unregister_event_cb(const struct device *dev, uint32_t reg_handle)
{
        const struct display_driver_api *api = DEVICE_API_GET(display, dev);

        if (api->unregister_event_cb == NULL || api->register_event_cb == NULL) {
                return -ENOSYS;
        }

        if (reg_handle == 0U) {
                return -EINVAL;
        }

        return api->unregister_event_cb(dev, reg_handle);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_DISPLAY_H_ */
```

## 41.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Jan Van Winkel <jan.van_winkel@dxplore.eu>。

SPDX 文件版权声明（FileCopyrightText）：2026 Abderrahmane JARMOUNI。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 348 行

条件编译表达式：`defined(CONFIG_DISPLAY_COLOR_PALETTE) || defined(__DOXYGEN__)`。

### 注释 3：原第 369 行

条件编译表达式：`defined(CONFIG_DISPLAY_COLOR_PALETTE) || defined(__DOXYGEN__)`。

### 注释 4：原第 949 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DISPLAY_H_`。

## 41.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2display_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/dt-bindings/display/panel.h](https://docs.zephyrproject.org/latest/doxygen/html/panel_8h.html)
- [display_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac346bc56771052a8fe919c3ec23d7c9c)
- [PIXEL_FORMAT_RGB_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cac99044ebc0258de7ab8f4ef46edeb44a)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [PIXEL_FORMAT_MONO01](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cabb19ccb2fad2d8f809819dd0a94b1d9c)
- [PIXEL_FORMAT_MONO10](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca4ab51591eb10fe72365f703d70bc7b6c)
- [PIXEL_FORMAT_ARGB_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca90eeb0d7507e2872774d0026eb100ee9)
- [PIXEL_FORMAT_RGB_565](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cac0ae1813354b024a4806f5012c5c4e16)
- [PIXEL_FORMAT_RGB_565X](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca0d12a0b6fd3df29b0a607eedf7671809)
- [PIXEL_FORMAT_L_8](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca14f33dfec4a630f5be50622a535434df)
- [PIXEL_FORMAT_AL_88](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca92f4901daf73e26c4290e656e7afeb2f)
- [PIXEL_FORMAT_XRGB_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca20bb97558d4acdf225a157c40d9058ab)
- [PIXEL_FORMAT_BGR_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca4625a834a26894db2da3547635a6e172)
- [PIXEL_FORMAT_ABGR_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca049f2930dfd1efadfb17a113ba0d879d)
- [PIXEL_FORMAT_RGBA_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca9de42e120e50119c2df1c503ed2e7a28)
- [PIXEL_FORMAT_BGRA_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca142784152249100847b0e5c6d656191c)
- [PIXEL_FORMAT_I_4](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9cacaed33ee4be17042d45cf238ac49df6a)
- [PIXEL_FORMAT_L_4](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca015155116919cac3eff289764e9574d8)
- [PIXEL_FORMAT_YUYV](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac346bc56771052a8fe919c3ec23d7c9ca5c905dcfaca35e58c14513f2e3a61091)
- [display_screen_info](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga23030b6c27446c4579103fe38e821341)
- [SCREEN_INFO_MONO_VTILED](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341ade1ec91a372b3b2208ebf5729184b804)
- [SCREEN_INFO_MONO_MSB_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341ade5bb2006e547450bac0edaa2a8b9c7d)
- [SCREEN_INFO_EPD](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341ac65e80206de09cb63e871ce18deefb85)
- [SCREEN_INFO_DOUBLE_BUFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341ad22c69026d0b4573aaebe0b3ef274842)
- [SCREEN_INFO_X_ALIGNMENT_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga23030b6c27446c4579103fe38e821341a1c51db66639919571af38bbc91eb28c1)
- [display_orientation](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac59b091a3ed39431ab97a5f19fdc4855)
- [DISPLAY_ORIENTATION_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac59b091a3ed39431ab97a5f19fdc4855adb3975e2caf6c28374e20a5e0ac26ed2)
- [DISPLAY_ORIENTATION_ROTATED_90](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac59b091a3ed39431ab97a5f19fdc4855a632483591b572c0945df3f65cb4e52bc)
- [DISPLAY_ORIENTATION_ROTATED_180](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac59b091a3ed39431ab97a5f19fdc4855a7f71ba80f09d5b17f7cdfa7456ed0e29)
- [DISPLAY_ORIENTATION_ROTATED_270](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ggac59b091a3ed39431ab97a5f19fdc4855af81128a85915f41c22bc0581f51455b4)
- [display_palette_color](../hardware/P218_显示调色板颜色.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [b](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__palette__color.html#a246ca83b0bdfdef20d93f9439c8cfe19)
- [g](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__palette__color.html#ab72b5252ecef18ff4fca49a196b10d1c)
- [r](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__palette__color.html#a054840180d6a2417262bd87f3dca3c30)
- [a](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__palette__color.html#ab443cff44dce74c21ad348875b45efe5)
- [display_capabilities](../hardware/P216_显示能力结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [x_resolution](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#a09fa14e2c53126d5602cb7b51e21145f)
- [y_resolution](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#a2cacb194139aaff90fd56b469f6de4a9)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [supported_pixel_formats](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#a07548bdd9671dd696b38a5bcf1599412)
- [screen_info](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#ac4a9098db4c2f721fa550c6142f541a9)
- [current_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#aed51c9efdc76972fecfa8a733c2a8d0c)
- [current_orientation](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#a18986f5d2c385766d5ad3d68edd85887)
- [supported_events](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#a13d647aa8d6331f17cbc567970b159e7)
- [color_palette](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#ad9a0b9f3cf2ffcb8a768071f4211cf3c)
- [display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)
- [buf_size](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__buffer__descriptor.html#aee9f34a6944b8e28622ab06d6907d40a)
- [width](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__buffer__descriptor.html#aa35cf372266199308211d28dae789be3)
- [height](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__buffer__descriptor.html#a572c6560903553b6853360fd29631b95)
- [pitch](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__buffer__descriptor.html#a00d7d8da4e61f404ad353b9a8f49b2eb)
- [frame_incomplete](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__buffer__descriptor.html#a29e49359561cc0c601196eb9cf1f93b7)
- [display_event_data](../hardware/P217_显示事件数据.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [timestamp](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__event__data.html#a2b3fd531cffae409845be4ee04d87c68)
- [line](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__event__data.html#a7267cf1133ae4f076f4b927f0a3a4ced)
- [buffer_id](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__event__data.html#a6bf7995a2713fbda0638c56a950b915a)
- [info](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__event__data.html#a3fd29164cf76ef5f2fee818ac61af747)
- [display_event](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga0042f460c729a5b11ed59f4aac609212)
- [DISPLAY_EVENT_LINE_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga0042f460c729a5b11ed59f4aac609212a4aecf6d165ca2ec432297cc5664c24a6)
- [DISPLAY_EVENT_VSYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga0042f460c729a5b11ed59f4aac609212acb5772017ec3e4d6677fee78295a379c)
- [DISPLAY_EVENT_FRAME_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga0042f460c729a5b11ed59f4aac609212abd4e3c24f05c2484137855349d6cf794)
- [DISPLAY_EVENT_FIFO_UNDERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga0042f460c729a5b11ed59f4aac609212a456bc992ffdf5604828b7280f94dd649)
- [display_event_result](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga5c3bcf15b62c66c1677e51a10451efe5)
- [DISPLAY_EVENT_RESULT_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga5c3bcf15b62c66c1677e51a10451efe5abc630229e82e4e5d7ef50ec4c8e6aff7)
- [DISPLAY_EVENT_RESULT_HANDLED](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gga5c3bcf15b62c66c1677e51a10451efe5ad79be33d4e885b6745feebebc3636dfc)
- [display_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gadca2fe10ecb27b5e82309bbab5e886ee)
- [device](../device_reference/P002_设备对象结构.md)
- [display_blanking_on_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gacf66a054396ccd8e178591b8fc98ff4d)
- [display_blanking_off_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gab23bbd9305792d6e37d2e4ff91a2b175)
- [display_write_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga5cab904b24062fdea531f450a8e5c367)
- [display_read_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga9ed51d3f666f747d9fb7f1f7746611b3)
- [display_clear_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gaf42820ae69452788bf51f37512ca8586)
- [display_set_brightness_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga6b2abfa8c8fca9bdf77b5b87bd8c2c7a)
- [display_set_contrast_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gadf115352908f94b0a0bf225dbdd8ee85)
- [display_get_capabilities_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga474f85a33aef019dddb1c720ea23f3fb)
- [display_set_pixel_format_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga2637286cf3a97c2b532bb33f22263303)
- [display_set_orientation_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gaff3b76a6601cf176782be940139ccb48)
- [display_register_event_cb_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gac0a36d044e4663ab5ee61d1e11d645d0)
- [display_unregister_event_cb_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#gadd468c71193663072489f32885bc30e5)
- [display_driver_api](../hardware/P220_显示驱动函数表.md)
- [blanking_on](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#aafdd79a11b46d4fa9288ddf3ed994c18)
- [blanking_off](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a128c1324f4bfab707adc93aaff0f3371)
- [write](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a535221c00caef6f24dc75c919826a889)
- [read](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a431f765057a70e5d11ceaf93e8cc119a)
- [clear](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a913e21f2f3cdf6c20d0b3d00ec698b12)
- [display_get_framebuffer_api](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface__backend.html#ga6dd281032ad400d3adc7f5f812c5fe12)
- [get_framebuffer](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#aa7843031d91003dc458be4146503b7f0)
- [set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#aa40c04701b60f56c8998da55c2b254a8)
- [set_contrast](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#acfdf1662c0b362d5a35a137c903a40ba)
- [get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#ace3a2eae73f639da890b6798bd215b29)
- [set_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a28801ba7578b9ab725c62b5f0d9f2c65)
- [set_orientation](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a4cbccfaafeb2f24c473bd967b9bc5f14)
- [register_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a162599eece01dd31b2095048b15a42a9)
- [unregister_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a736ece063a8a1a575aa28c53ed160193)
- [display_write](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga3a5114b4537039fc4d3258678b82cd18)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [display_read](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga3f497776520b0eac16b8aea80ccbbcfc)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [display_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga62a6cd9e338aa07f789de60e64d3b3c4)
- [display_get_framebuffer](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga4b66d380e46909caaa7317857f84a9e8)
- [display_blanking_on](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gac6ad1f33067165e4c3bf7c0c345bb4e4)
- [display_blanking_off](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga4d9e288891a6bde679c3aa00b9913e1d)
- [display_set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gad5cdeb245d17c8d680a5843b3cce1f8c)
- [display_set_contrast](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga855c72f72238b25f23e95e50546e2f27)
- [display_get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga6a13e42773be13b141ebd8f047f8db50)
- [memset](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a4137694174d4ca2fad886a1db355015c)
- [display_set_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga7ede828663090760c2558a231d9f2150)
- [display_set_orientation](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga4e0a4dc2e434144874af014b8e7c4394)
- [display_register_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#ga99b7e7da6b85bee97398a8a9b161c777)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [display_unregister_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html#gaa4e433439206bc426db363c64882a395)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [panel.h](https://docs.zephyrproject.org/latest/doxygen/html/panel_8h.html)
- [display_buffer_descriptor::pitch](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__buffer__descriptor.html#a00d7d8da4e61f404ad353b9a8f49b2eb)
- [display_buffer_descriptor::frame_incomplete](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__buffer__descriptor.html#a29e49359561cc0c601196eb9cf1f93b7)
- [display_buffer_descriptor::height](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__buffer__descriptor.html#a572c6560903553b6853360fd29631b95)
- [display_buffer_descriptor::width](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__buffer__descriptor.html#aa35cf372266199308211d28dae789be3)
- [display_buffer_descriptor::buf_size](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__buffer__descriptor.html#aee9f34a6944b8e28622ab06d6907d40a)
- [display_capabilities::supported_pixel_formats](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#a07548bdd9671dd696b38a5bcf1599412)
- [display_capabilities::x_resolution](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#a09fa14e2c53126d5602cb7b51e21145f)
- [display_capabilities::supported_events](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#a13d647aa8d6331f17cbc567970b159e7)
- [display_capabilities::current_orientation](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#a18986f5d2c385766d5ad3d68edd85887)
- [display_capabilities::y_resolution](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#a2cacb194139aaff90fd56b469f6de4a9)
- [display_capabilities::screen_info](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#ac4a9098db4c2f721fa550c6142f541a9)
- [display_capabilities::color_palette](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#ad9a0b9f3cf2ffcb8a768071f4211cf3c)
- [display_capabilities::current_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__capabilities.html#aed51c9efdc76972fecfa8a733c2a8d0c)
- [display_driver_api::blanking_off](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a128c1324f4bfab707adc93aaff0f3371)
- [display_driver_api::register_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a162599eece01dd31b2095048b15a42a9)
- [display_driver_api::set_pixel_format](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a28801ba7578b9ab725c62b5f0d9f2c65)
- [display_driver_api::read](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a431f765057a70e5d11ceaf93e8cc119a)
- [display_driver_api::set_orientation](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a4cbccfaafeb2f24c473bd967b9bc5f14)
- [display_driver_api::write](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a535221c00caef6f24dc75c919826a889)
- [display_driver_api::unregister_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a736ece063a8a1a575aa28c53ed160193)
- [display_driver_api::clear](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#a913e21f2f3cdf6c20d0b3d00ec698b12)
- [display_driver_api::set_brightness](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#aa40c04701b60f56c8998da55c2b254a8)
- [display_driver_api::get_framebuffer](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#aa7843031d91003dc458be4146503b7f0)
- [display_driver_api::blanking_on](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#aafdd79a11b46d4fa9288ddf3ed994c18)
- [display_driver_api::get_capabilities](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#ace3a2eae73f639da890b6798bd215b29)
- [display_driver_api::set_contrast](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__driver__api.html#acfdf1662c0b362d5a35a137c903a40ba)
- [display_event_data::timestamp](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__event__data.html#a2b3fd531cffae409845be4ee04d87c68)
- [display_event_data::info](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__event__data.html#a3fd29164cf76ef5f2fee818ac61af747)
- [display_event_data::buffer_id](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__event__data.html#a6bf7995a2713fbda0638c56a950b915a)
- [display_event_data::line](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__event__data.html#a7267cf1133ae4f076f4b927f0a3a4ced)
- [display_palette_color::r](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__palette__color.html#a054840180d6a2417262bd87f3dca3c30)
- [display_palette_color::b](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__palette__color.html#a246ca83b0bdfdef20d93f9439c8cfe19)
- [display_palette_color::a](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__palette__color.html#ab443cff44dce74c21ad348875b45efe5)
- [display_palette_color::g](https://docs.zephyrproject.org/latest/doxygen/html/structdisplay__palette__color.html#ab72b5252ecef18ff4fca49a196b10d1c)

---

[上一章](P040_dmic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P042_led.h_源码浏览.md)
