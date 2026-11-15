---
id: learning.zephyr-docs.api-source-reference.page-890
title: usbc_pd.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第890章\_usbc\_pd.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h.html)。

## 890.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00061"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00083"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="foldopen00321"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00325"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00331"></a>
<a id="l00333"></a>
<a id="l00335"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="foldopen00354"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00362"></a>
<a id="l00364"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00376"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="foldopen00386"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00390"></a>
<a id="l00392"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="foldopen00431"></a>
<a id="l00431"></a>
<a id="l00433"></a>
<a id="l00435"></a>
<a id="l00437"></a>
<a id="l00439"></a>
<a id="l00441"></a>
<a id="l00443"></a>
<a id="l00445"></a>
<a id="l00447"></a>
<a id="l00449"></a>
<a id="l00451"></a>
<a id="l00453"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="foldopen00464"></a>
<a id="l00464"></a>
<a id="l00466"></a>
<a id="l00468"></a>
<a id="l00470"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="foldopen00479"></a>
<a id="l00479"></a>
<a id="l00481"></a>
<a id="l00483"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="l00489"></a>
<a id="l00491"></a>
<a id="l00493"></a>
<a id="l00495"></a>
<a id="l00497"></a>
<a id="l00499"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="foldopen00539"></a>
<a id="l00539"></a>
<a id="l00541"></a>
<a id="l00543"></a>
<a id="l00545"></a>
<a id="l00547"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="foldopen00559"></a>
<a id="l00559"></a>
<a id="l00561"></a>
<a id="l00563"></a>
<a id="l00565"></a>
<a id="l00567"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="foldopen00607"></a>
<a id="l00607"></a>
<a id="l00609"></a>
<a id="l00611"></a>
<a id="l00613"></a>
<a id="l00615"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="foldopen00627"></a>
<a id="l00627"></a>
<a id="l00629"></a>
<a id="l00631"></a>
<a id="l00633"></a>
<a id="l00635"></a>
<a id="l00637"></a>
<a id="l00638"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00655"></a>
<a id="l00656"></a>
<a id="l00662"></a>
<a id="l00663"></a>
<a id="l00669"></a>
<a id="l00670"></a>
<a id="foldopen00675"></a>
<a id="l00675"></a>
<a id="l00677"></a>
<a id="l00679"></a>
<a id="l00681"></a>
<a id="l00683"></a>
<a id="l00685"></a>
<a id="l00687"></a>
<a id="l00689"></a>
<a id="l00691"></a>
<a id="l00697"></a>
<a id="l00699"></a>
<a id="l00700"></a>
<a id="l00702"></a>
<a id="l00703"></a>
<a id="l00704"></a>
<a id="foldopen00709"></a>
<a id="l00709"></a>
<a id="l00711"></a>
<a id="l00713"></a>
<a id="l00715"></a>
<a id="l00717"></a>
<a id="l00719"></a>
<a id="l00721"></a>
<a id="l00723"></a>
<a id="l00729"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="foldopen00742"></a>
<a id="l00742"></a>
<a id="l00747"></a>
<a id="l00755"></a>
<a id="l00757"></a>
<a id="l00759"></a>
<a id="l00761"></a>
<a id="l00763"></a>
<a id="l00765"></a>
<a id="l00767"></a>
<a id="l00769"></a>
<a id="l00771"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00780"></a>
<a id="l00788"></a>
<a id="l00790"></a>
<a id="l00792"></a>
<a id="l00794"></a>
<a id="l00796"></a>
<a id="l00798"></a>
<a id="l00800"></a>
<a id="l00802"></a>
<a id="l00804"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00813"></a>
<a id="l00815"></a>
<a id="l00817"></a>
<a id="l00819"></a>
<a id="l00821"></a>
<a id="l00823"></a>
<a id="l00825"></a>
<a id="l00827"></a>
<a id="l00829"></a>
<a id="l00831"></a>
<a id="l00833"></a>
<a id="l00834"></a>
<a id="l00835"></a>
<a id="l00840"></a>
<a id="l00842"></a>
<a id="l00844"></a>
<a id="l00846"></a>
<a id="l00848"></a>
<a id="l00850"></a>
<a id="l00852"></a>
<a id="l00854"></a>
<a id="l00856"></a>
<a id="l00858"></a>
<a id="l00860"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="foldopen00871"></a>
<a id="l00871"></a>
<a id="l00873"></a>
<a id="l00875"></a>
<a id="l00877"></a>
<a id="l00878"></a>
<a id="l00879"></a>
<a id="foldopen00885"></a>
<a id="l00885"></a>
<a id="l00887"></a>
<a id="l00889"></a>
<a id="l00891"></a>
<a id="l00893"></a>
<a id="l00895"></a>
<a id="l00897"></a>
<a id="l00899"></a>
<a id="l00901"></a>
<a id="l00902"></a>
<a id="l00904"></a>
<a id="l00905"></a>
<a id="l00906"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="foldopen00916"></a>
<a id="l00916"></a>
<a id="l00918"></a>
<a id="l00920"></a>
<a id="l00922"></a>
<a id="l00924"></a>
<a id="l00926"></a>
<a id="l00928"></a>
<a id="l00930"></a>
<a id="l00932"></a>
<a id="l00934"></a>
<a id="l00936"></a>
<a id="l00938"></a>
<a id="l00940"></a>
<a id="l00942"></a>
<a id="l00944"></a>
<a id="l00945"></a>
<a id="l00947"></a>
<a id="l00949"></a>
<a id="l00951"></a>
<a id="l00953"></a>
<a id="l00955"></a>
<a id="l00957"></a>
<a id="l00959"></a>
<a id="l00961"></a>
<a id="l00963"></a>
<a id="l00965"></a>
<a id="l00967"></a>
<a id="l00969"></a>
<a id="l00970"></a>
<a id="l00972"></a>
<a id="l00974"></a>
<a id="l00975"></a>
<a id="l00976"></a>
<a id="foldopen00981"></a>
<a id="l00981"></a>
<a id="l00983"></a>
<a id="l00985"></a>
<a id="l00987"></a>
<a id="l00989"></a>
<a id="l00991"></a>
<a id="l00993"></a>
<a id="l00995"></a>
<a id="l00997"></a>
<a id="l00998"></a>
<a id="l01000"></a>
<a id="l01002"></a>
<a id="l01004"></a>
<a id="l01006"></a>
<a id="l01008"></a>
<a id="l01010"></a>
<a id="l01012"></a>
<a id="l01013"></a>
<a id="l01015"></a>
<a id="l01016"></a>
<a id="l01017"></a>
<a id="foldopen01022"></a>
<a id="l01022"></a>
<a id="l01024"></a>
<a id="l01026"></a>
<a id="l01028"></a>
<a id="l01030"></a>
<a id="l01032"></a>
<a id="l01034"></a>
<a id="l01036"></a>
<a id="l01038"></a>
<a id="l01040"></a>
<a id="l01042"></a>
<a id="l01044"></a>
<a id="l01046"></a>
<a id="l01048"></a>
<a id="l01050"></a>
<a id="l01052"></a>
<a id="l01054"></a>
<a id="l01056"></a>
<a id="l01058"></a>
<a id="l01060"></a>
<a id="l01061"></a>
<a id="l01063"></a>
<a id="l01065"></a>
<a id="l01066"></a>
<a id="l01068"></a>
<a id="l01070"></a>
<a id="l01071"></a>
<a id="l01072"></a>
<a id="foldopen01076"></a>
<a id="l01076"></a>
<a id="l01078"></a>
<a id="l01080"></a>
<a id="l01081"></a>
<a id="l01082"></a>
<a id="foldopen01086"></a>
<a id="l01086"></a>
<a id="l01088"></a>
<a id="l01090"></a>
<a id="l01092"></a>
<a id="l01094"></a>
<a id="l01095"></a>
<a id="l01096"></a>
<a id="l01100"></a>
<a id="l01101"></a>
<a id="l01102"></a>
<a id="l01103"></a>
<a id="l01104"></a>
<a id="l01105"></a>
<a id="agroup__usb__power__delivery__pdo_html_ga9fa615ab7f38385c21277d4e9e6a1441"></a>
<a id="agroup__usb__power__delivery_html_ga316dca7ed0b85f1aa224d7a767896328"></a>
<a id="agroup__usb__power__delivery_html_ga457308d50365e0a2440e94e41a316cbf"></a>
<a id="agroup__usb__power__delivery_html_ga48b33240e19524ea003052103d310358"></a>
<a id="agroup__usb__power__delivery_html_ga4c7862a3e953fb22534123223c942f9a"></a>
<a id="agroup__usb__power__delivery_html_ga8239651864b4cb0e1fc89ba2d7e59462"></a>
<a id="agroup__usb__power__delivery_html_gab68c6b6e33449c5ceadfc9217dd7a700"></a>
<a id="agroup__usb__power__delivery_html_gabdb041542baaf2277e054dd9e3928b16"></a>
<a id="agroup__usb__power__delivery_html_gad2df13a24f0365198d37b10af608376b"></a>
<a id="agroup__usb__power__delivery_html_gaee2fe2128557939404c62e8104269bbf"></a>
<a id="agroup__usb__power__delivery_html_gga316dca7ed0b85f1aa224d7a767896328a1726efca9ece0ff017cc4aaf05ce9624"></a>
<a id="agroup__usb__power__delivery_html_gga316dca7ed0b85f1aa224d7a767896328a63f4fb7a4d2f7e265fd49be07966fbaa"></a>
<a id="agroup__usb__power__delivery_html_gga316dca7ed0b85f1aa224d7a767896328adb8478434cc1622e98bc22f4081dff1e"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfa0544591815d3b3666db44d5cff561f83"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfa0f62aa3774995018514dcd2f75ac1c1f"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfa20d43a6bdbd425d8f17c01d6e6cbcce3"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfa2a7b6a78cf3fd87a86f060f927b566af"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfa4fe2d7028fa2bdf594cb8c87ac05fe67"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfa500d77f178123eab8073058dd9308ea6"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfa51c03e44c3fe1bb59445bbc452ea7199"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfa77ff801aa819461f0f5ff44546370bd7"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfa7d04da3fdb96eac97200d11eb2dbe083"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfa836130da5307aed6160deadadf2f4f3f"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfa84ef06f718993e00134040d427b93591"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfa9c50488735d7723c3cc30f176c221e40"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfaa21adc92574ed1261b6c13df3592601b"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfac8fc4c3c64fb3eaba8cb61bd999c7033"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfacb6e48382233e62151ab1a1fd845d429"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfad002882e8bce9cdfdb0864cd6a3e79a7"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfae569507687c904dc65827c6a737012a5"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfae69b4a8ddba29bc6cd69d50c946bc658"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfae7f7b3f7233bb5cf600338b4a2c601c0"></a>
<a id="agroup__usb__power__delivery_html_gga457308d50365e0a2440e94e41a316cbfaf3cdbd6af73a63879a5985e8db1e0d7f"></a>
<a id="agroup__usb__power__delivery_html_gga48b33240e19524ea003052103d310358a4cd44f89f225f8869bfd901e7ea79aed"></a>
<a id="agroup__usb__power__delivery_html_gga48b33240e19524ea003052103d310358a99ab2afc15809b5e89e3fb7106be37ba"></a>
<a id="agroup__usb__power__delivery_html_gga48b33240e19524ea003052103d310358acac5008ded87d7a20b0b3b272075e4c1"></a>
<a id="agroup__usb__power__delivery_html_gga48b33240e19524ea003052103d310358acbf2bf3ae21ff1ea51d7fd2b823ce726"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa03f9886881aa493fb0f9bfac16713e7a"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa189edfda108af04877adc2025cabb1eb"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa1c597b5f953e6e1791aa869025b98b24"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa23287276ee22241906828515f38fedef"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa27caca37f9522045bc8612f7536cd792"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa28bd36a3d8c92ba6ea2943b0617fe6af"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa3b6fc49b1ae0bb343d39476350b59c90"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa4aba967f7e363dbbadcc9a9ecf0c7ae4"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa4ba7f63cdcbe766a34047e06145a591e"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa56df68ed627b56bbcfc20900ec5d2e5d"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa676239b098266cbec7c448dbaeebfa6c"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa677ebc41b4b67de6ee93b5e446af702e"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa68820e99ce9c1c73180734372e5ede2b"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa8177040ca8a1f71dde67fc59060c35ed"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa9324307526500683ae265e9cb0063929"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aa9dd7b559e78a99639056325a7be14d81"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aaaa0a5bba9a9f1573952141c4f8f77318"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aaaf5c221569a9108bdbc36545dcb37495"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aab0ca2628b144d092116b461703176eaa"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aab82efb96b1f8f7dae3c76e362ae1715a"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aabfea5fdf0263fdf4c924bd603ee7256f"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aade67c4fb153e5ba87b6d6643f99260f9"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aadeb12ed01ec54ee55588bfb796dd0c11"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aae0895be53e5a1e54731e9608a8e0c6c9"></a>
<a id="agroup__usb__power__delivery_html_gga4c7862a3e953fb22534123223c942f9aafc449fc3dc39f2495494507cc97f53ad"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462a1a0829560f9f82182f7587fd8787a846"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462a4cf30dcbce3fdf8076713e45d242b39a"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462a5352e00ba0ae91b14a8ecff9107e1bca"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462a648d1d50d51c5999e053ddcee92c30db"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462a7c4bc907fb81082da05c64797854be9f"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462a7e3368e1c7bde4c6bb3136cb80209bb6"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462a83d7098236e97972cf24b900f7e5e069"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462a881fcbc2dc5f8b1de7c97522df46242d"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462aaea7d41eb22db0a06d676714d0598ee0"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462abd9d5984a02b719e3d9599d0228aa99e"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462ad493f01ffc4c3c164f874eb202f8adb0"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462ad8b62eecdf3b574585d259bb6cb34564"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462ad9a0cf16cfa852111ea0ed3434b35dfc"></a>
<a id="agroup__usb__power__delivery_html_gga8239651864b4cb0e1fc89ba2d7e59462ad9c920f987e2578b030cc08f2e69998a"></a>
<a id="agroup__usb__power__delivery_html_ggab68c6b6e33449c5ceadfc9217dd7a700a1d9b4c553f44dccdc67e4edb554557b9"></a>
<a id="agroup__usb__power__delivery_html_ggab68c6b6e33449c5ceadfc9217dd7a700a22c122b1d30a3ab96fffd5dfa6bfb9ae"></a>
<a id="agroup__usb__power__delivery_html_ggab68c6b6e33449c5ceadfc9217dd7a700af3770bcbcf6feaaab272c022d7a57c7a"></a>
<a id="agroup__usb__power__delivery_html_ggad2df13a24f0365198d37b10af608376ba0bede6a56c24b06fdf56cf1dc386bb14"></a>
<a id="agroup__usb__power__delivery_html_ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1"></a>
<a id="agroup__usb__power__delivery_html_ggad2df13a24f0365198d37b10af608376ba531ebc6013984b81e6fb550618d6b4a8"></a>
<a id="agroup__usb__power__delivery_html_ggad2df13a24f0365198d37b10af608376ba55bb88e5955992170bee96ddbe8a7437"></a>
<a id="agroup__usb__power__delivery_html_ggad2df13a24f0365198d37b10af608376ba5ecd663a9eecefcf965f605125d5188c"></a>
<a id="agroup__usb__power__delivery_html_ggad2df13a24f0365198d37b10af608376ba63b2200ebaf016d06437f3586d15171d"></a>
<a id="agroup__usb__power__delivery_html_ggad2df13a24f0365198d37b10af608376baa5cd066e86fd55727c3625cd16633f73"></a>
<a id="agroup__usb__power__delivery_html_ggad2df13a24f0365198d37b10af608376bae3a5f99242ab24a34706170101b38ef8"></a>
<a id="agroup__usb__power__delivery_html_ggad2df13a24f0365198d37b10af608376bafcd21cc6b1ae6c58b86c0619d687e8fc"></a>
<a id="agroup__usb__power__delivery_html_ggaee2fe2128557939404c62e8104269bbfa53a0a6ba0212b9cbb407522e7f35648e"></a>
<a id="agroup__usb__power__delivery_html_ggaee2fe2128557939404c62e8104269bbfa59a0ed05c4e99acebaa11080dbbe7694"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructpd__msg_html"></a>
<a id="astructpd__msg_html_aa03ec4ce6d2f0d16a829394ff0ed2688"></a>
<a id="astructpd__msg_html_ad6fd282617b5f6dfeeef6cf4598883ee"></a>
<a id="astructpd__msg_html_ae6f1fa8a1fb006e3d90e75cd834e6d05"></a>
<a id="astructpd__msg_html_af9f676afd2c2824fb9f01a08d8339231"></a>
<a id="aunionpd__augmented__supply__pdo__sink_html"></a>
<a id="aunionpd__augmented__supply__pdo__sink_html_a0a5da0df48dff5fae42159026c91c7af"></a>
<a id="aunionpd__augmented__supply__pdo__sink_html_a22e63fa7e83af25d9822dcf3d9b35f40"></a>
<a id="aunionpd__augmented__supply__pdo__sink_html_a2f1f6094af7449619ab626476fa51698"></a>
<a id="aunionpd__augmented__supply__pdo__sink_html_a3320455a4c7673d3db95f585b07cc319"></a>
<a id="aunionpd__augmented__supply__pdo__sink_html_aa800bd5299c535e5de98d57aec1b2fff"></a>
<a id="aunionpd__augmented__supply__pdo__sink_html_ad83710136d9dcad3644ec36c1eee9cb0"></a>
<a id="aunionpd__augmented__supply__pdo__sink_html_adfa0b8ab656255cfecc9ca5e1ee05d49"></a>
<a id="aunionpd__augmented__supply__pdo__sink_html_ae28a74642ffcdf1100f37e3542e1ca96"></a>
<a id="aunionpd__augmented__supply__pdo__sink_html_af5eca8ab38a3eaaaecd10cdc1092ce3c"></a>
<a id="aunionpd__augmented__supply__pdo__source_html"></a>
<a id="aunionpd__augmented__supply__pdo__source_html_a093a674e538dcc2541ff86f50d0156df"></a>
<a id="aunionpd__augmented__supply__pdo__source_html_a56e1af2acda73fee7e40449b7c39745d"></a>
<a id="aunionpd__augmented__supply__pdo__source_html_a7ef0b26951ce2683c9c4ca0f19b73d6d"></a>
<a id="aunionpd__augmented__supply__pdo__source_html_aa59ad8a8eb4e2343c14bbe54937aa93d"></a>
<a id="aunionpd__augmented__supply__pdo__source_html_ab5868f6ba91821d56ddb419e895a05fa"></a>
<a id="aunionpd__augmented__supply__pdo__source_html_aba6df91a8c5da92517f885fa89af8747"></a>
<a id="aunionpd__augmented__supply__pdo__source_html_abfac34ee5da0b1700b784c7bfe925c19"></a>
<a id="aunionpd__augmented__supply__pdo__source_html_ac046ddf128416ecbb8f3a26185d03e03"></a>
<a id="aunionpd__augmented__supply__pdo__source_html_ae064d7413ede09780ad7314ce31caaa1"></a>
<a id="aunionpd__augmented__supply__pdo__source_html_ae79eb7473040058c0b8572cfe4fa4dce"></a>
<a id="aunionpd__battery__supply__pdo__sink_html"></a>
<a id="aunionpd__battery__supply__pdo__sink_html_a3f1072c4ca168aaedd13257f01f410aa"></a>
<a id="aunionpd__battery__supply__pdo__sink_html_a515f6958ba647dc77a30414732afd82b"></a>
<a id="aunionpd__battery__supply__pdo__sink_html_a5a588a46ae8bef2dc10445c2f5422246"></a>
<a id="aunionpd__battery__supply__pdo__sink_html_a858efb23a0c143917b88e5596b899c79"></a>
<a id="aunionpd__battery__supply__pdo__sink_html_aa973b26972c1e1a96c7e0c09dbed08f3"></a>
<a id="aunionpd__battery__supply__pdo__source_html"></a>
<a id="aunionpd__battery__supply__pdo__source_html_a00ea9931d839cf83b56513f77aa7d5b9"></a>
<a id="aunionpd__battery__supply__pdo__source_html_a1e775dc0082b531216c154724be360b0"></a>
<a id="aunionpd__battery__supply__pdo__source_html_a673ea076da8810bc694b2dc82bbede67"></a>
<a id="aunionpd__battery__supply__pdo__source_html_ac7157c3fbae86d34e2c7d82bf9af3a3f"></a>
<a id="aunionpd__battery__supply__pdo__source_html_afa2335788e7fde01b90afd95bccf6d5f"></a>
<a id="aunionpd__ext__header_html"></a>
<a id="aunionpd__ext__header_html_a180ccc6854c1341e638ca338e6eb1cd8"></a>
<a id="aunionpd__ext__header_html_a36a65a1e52875721758d1273b0e76279"></a>
<a id="aunionpd__ext__header_html_a4a7a948d3463ddfbebf1d75faeda293e"></a>
<a id="aunionpd__ext__header_html_a8a1d0f0d38b3a5c4aa3a80586e7a1e8f"></a>
<a id="aunionpd__ext__header_html_aae09d0399c0a121e3c216047e908b9ec"></a>
<a id="aunionpd__ext__header_html_aced0489c4e2462652c0d91187c07b27e"></a>
<a id="aunionpd__fixed__supply__pdo__sink_html"></a>
<a id="aunionpd__fixed__supply__pdo__sink_html_a0559272067e2d0c33f52274fb59ea18d"></a>
<a id="aunionpd__fixed__supply__pdo__sink_html_a22f9763652560dbd215324f1bb878a96"></a>
<a id="aunionpd__fixed__supply__pdo__sink_html_a2ac4005b0cf3e28ade8f508d2c6f5e20"></a>
<a id="aunionpd__fixed__supply__pdo__sink_html_a3086d57313f05b8bc91fb3590e51c657"></a>
<a id="aunionpd__fixed__supply__pdo__sink_html_a3945768e406175b51f9c4b8c3d0e9848"></a>
<a id="aunionpd__fixed__supply__pdo__sink_html_a5c6bfb21c4d8e70a04895dd31a58885e"></a>
<a id="aunionpd__fixed__supply__pdo__sink_html_a7a26a084dd6004f9121c8493a0c520f6"></a>
<a id="aunionpd__fixed__supply__pdo__sink_html_aad255dbee3452bf3276464c59f113cb2"></a>
<a id="aunionpd__fixed__supply__pdo__sink_html_ab406f1f36e5fe6f7acb9abc91991a803"></a>
<a id="aunionpd__fixed__supply__pdo__sink_html_ac47dcf98dfca90eb0e6013a3e1c5eb18"></a>
<a id="aunionpd__fixed__supply__pdo__sink_html_aebdeb854bcac0d20efcbe3be56dcc9f8"></a>
<a id="aunionpd__fixed__supply__pdo__source_html"></a>
<a id="aunionpd__fixed__supply__pdo__source_html_a2c4b27407245da04b67e9524173d39bc"></a>
<a id="aunionpd__fixed__supply__pdo__source_html_a440ff92d2bd533e3ddd6c65f9ac21772"></a>
<a id="aunionpd__fixed__supply__pdo__source_html_a55003edba55a920a386cc04cbc7a72a0"></a>
<a id="aunionpd__fixed__supply__pdo__source_html_a66f55e177b6f2bc76b392707e39fa4fe"></a>
<a id="aunionpd__fixed__supply__pdo__source_html_a6b0e04acd43c9b18bd1dea80508a8817"></a>
<a id="aunionpd__fixed__supply__pdo__source_html_a6c1bcf37a1fc9a348cf19e16fbe01dac"></a>
<a id="aunionpd__fixed__supply__pdo__source_html_a7b89666e3753966001caf7602c796147"></a>
<a id="aunionpd__fixed__supply__pdo__source_html_a86664d945f65f19f7b96da1148700640"></a>
<a id="aunionpd__fixed__supply__pdo__source_html_a9227629f6c97357b71ea20e4e0572cf2"></a>
<a id="aunionpd__fixed__supply__pdo__source_html_a9fc10f3ec4126c063f5dd99e8f3e2723"></a>
<a id="aunionpd__fixed__supply__pdo__source_html_af96673f1ac078436a9eca0973e1bdef9"></a>
<a id="aunionpd__fixed__supply__pdo__source_html_aff4c1e7eab502a68e80013b4010aff76"></a>
<a id="aunionpd__header_html"></a>
<a id="aunionpd__header_html_a20ac99d9738c9d278a78e8ccfc401902"></a>
<a id="aunionpd__header_html_a5750b964c12c3bc2d2523a64cb9eb7d0"></a>
<a id="aunionpd__header_html_a63d89119f0918ba7d6eb9e01fa1ed406"></a>
<a id="aunionpd__header_html_a70768acc6a6bc9ebb9249df7ed635a94"></a>
<a id="aunionpd__header_html_a85cce1728afe0d62bb29f618a1cf70e1"></a>
<a id="aunionpd__header_html_ae4a0a5695e73fd3e1b7e3f38cd2a758c"></a>
<a id="aunionpd__header_html_af1b027c9c57497421117b290dcb6ac66"></a>
<a id="aunionpd__header_html_afa6c6699be5fe95bcb4962396e33e35d"></a>
<a id="aunionpd__rdo_html"></a>
<a id="aunionpd__rdo_html_a0b7502c79b0976b8e0d118cae3950191"></a>
<a id="aunionpd__rdo_html_a30f6044378cad6f277f8694df5611230"></a>
<a id="aunionpd__rdo_html_a41d023e9308e6d252f0bc8412a6c6184"></a>
<a id="aunionpd__rdo_html_a477cf38b68b9386e950c085a1ce4f336"></a>
<a id="aunionpd__rdo_html_a5838022e249981be50aee897c16ce56e"></a>
<a id="aunionpd__rdo_html_a5f8b64ce53d9881a007405a986b6b490"></a>
<a id="aunionpd__rdo_html_a63dd2a9e94f3a61205b95efc0cf79f13"></a>
<a id="aunionpd__rdo_html_a82e1adf30b6fc476b794b94cfb379214"></a>
<a id="aunionpd__rdo_html_a8c11df4b75772cda511bd94e5a297128"></a>
<a id="aunionpd__rdo_html_aa0ddbfb3c345b671f97d4b4e760168b4"></a>
<a id="aunionpd__rdo_html_aa5af5685e6d9c3d8a7ec3a40d25b43ba"></a>
<a id="aunionpd__rdo_html_ab4065aee18c3a68df38592122f607343"></a>
<a id="aunionpd__rdo_html_ab59da7098c1d33c9269f66dd3ac3fc5b"></a>
<a id="aunionpd__rdo_html_ad6b45a879e689dcd05bf9e07aedc4d20"></a>
<a id="aunionpd__rdo_html_ad7a98411aad054f1161b4ce32ef3ee33"></a>
<a id="aunionpd__rdo_html_ae5ae5d3c823254ab895becc3b01761fe"></a>
<a id="aunionpd__rdo_html_ae71e9abde3d69211c7bcfc7b80d18c41"></a>
<a id="aunionpd__rdo_html_ae90a23cc166373f7bb3c35be0c3967f2"></a>
<a id="aunionpd__rdo_html_afd24863b120085c57e77b8d246effd54"></a>
<a id="aunionpd__rdo_html_aff1b20a6e4905ac714ab5e7af7ff9593"></a>
<a id="aunionpd__variable__supply__pdo__sink_html"></a>
<a id="aunionpd__variable__supply__pdo__sink_html_a2ff80c049f98ab090b100b7f9877bffb"></a>
<a id="aunionpd__variable__supply__pdo__sink_html_aaaa1cf3f08208966fb00093f910f70ab"></a>
<a id="aunionpd__variable__supply__pdo__sink_html_ab7472487f253f5c2cb4d69eb805ede46"></a>
<a id="aunionpd__variable__supply__pdo__sink_html_ad648f2400a495b37d8b9f995556419d0"></a>
<a id="aunionpd__variable__supply__pdo__sink_html_ae360e7c2335a4f6cf5d267c8c82fdc45"></a>
<a id="aunionpd__variable__supply__pdo__source_html"></a>
<a id="aunionpd__variable__supply__pdo__source_html_a008cf5201ea6d3e238d547b738570c45"></a>
<a id="aunionpd__variable__supply__pdo__source_html_a67d86c71997a7c0605b8a199cd51c920"></a>
<a id="aunionpd__variable__supply__pdo__source_html_a8193ca96084db5901bb30195113ff01f"></a>
<a id="aunionpd__variable__supply__pdo__source_html_aabd59b2c5f4bfbbbd5d70adfb009eaf7"></a>
<a id="aunionpd__variable__supply__pdo__source_html_af00512126f128bf1cf31e802652af1bf"></a>

```c
/*
 * Copyright 2022 The Chromium OS Authors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_PD_H_
#define ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_PD_H_


#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

#define PD_MAX_EXTENDED_MSG_LEGACY_LEN   26

#define PD_MAX_EXTENDED_MSG_LEN    260

#define PD_MAX_EXTENDED_MSG_CHUNK_LEN    26


#define PD_N_CAPS_COUNT 50

#define PD_N_HARD_RESET_COUNT 2



#define PD_T_NO_RESPONSE_MIN_MS 4500

#define PD_T_NO_RESPONSE_MAX_MS 5500

#define PD_T_PS_HARD_RESET_MIN_MS 25

#define PD_T_PS_HARD_RESET_MAX_MS 35

#define PD_T_SINK_TX_MIN_MS 16

#define PD_T_SINK_TX_MAX_MS 20

#define PD_T_TYPEC_SEND_SOURCE_CAP_MIN_MS 100

#define PD_T_TYPEC_SEND_SOURCE_CAP_MAX_MS 200


#define PD_T_TYPEC_SINK_WAIT_CAP_MIN_MS 310

#define PD_T_TYPEC_SINK_WAIT_CAP_MAX_MS 620

#define PD_V_SAFE_0V_MAX_MV 800

#define PD_V_SAFE_5V_MIN_MV 4750

#define PD_T_SAFE_0V_MAX_MS  650

#define PD_T_SAFE_5V_MAX_MS  275

#define PD_T_TX_TIMEOUT_MS 100

#define PD_T_HARD_RESET_COMPLETE_MIN_MS 4

#define PD_T_HARD_RESET_COMPLETE_MAX_MS 5

#define PD_T_SENDER_RESPONSE_MIN_MS 24

#define PD_T_SENDER_RESPONSE_NOM_MS 27

#define PD_T_SENDER_RESPONSE_MAX_MS 30

#define PD_T_SPR_PS_TRANSITION_MIN_MS 450

#define PD_T_SPR_PS_TRANSITION_NOM_MS 500

#define PD_T_SPR_PS_TRANSITION_MAX_MS 550

#define PD_T_EPR_PS_TRANSITION_MIN_MS 830

#define PD_T_EPR_PS_TRANSITION_NOM_MS 925

#define PD_T_EPR_PS_TRANSITION_MAX_MS 1020

#define PD_T_SINK_REQUEST_MIN_MS 100

#define PD_T_CHUNKING_NOT_SUPPORTED_MIN_MS 40

#define PD_T_CHUNKING_NOT_SUPPORTED_NOM_MS 45

#define PD_T_CHUNKING_NOT_SUPPORTED_MAX_MS 50

#define PD_CONVERT_BYTES_TO_PD_HEADER_COUNT(c) ((c) >> 2)

#define PD_CONVERT_PD_HEADER_COUNT_TO_BYTES(c) ((c) << 2)

#define SINK_TX_OK TC_RP_3A0

#define SINK_TX_NG TC_RP_1A5

union pd_header {
        struct {
                uint16_t message_type : 5;
                uint16_t port_data_role : 1;
                uint16_t specification_revision : 2;
                uint16_t port_power_role : 1;
                uint16_t message_id : 3;
                uint16_t number_of_data_objects : 3;
                uint16_t extended : 1;
        };
        uint16_t raw_value;
};

#define PD_GET_EXT_HEADER(c) ((c) & 0xffff)

union pd_ext_header {
        struct {
                uint16_t data_size : 9;
                uint16_t reserved0 : 1;
                uint16_t request_chunk : 1;
                uint16_t chunk_number : 4;
                uint16_t chunked : 1;
        };
        uint16_t raw_value;
};


#define PDO_MAX_DATA_OBJECTS 7

enum pdo_type {
        PDO_FIXED       = 0,
        PDO_BATTERY     = 1,
        PDO_VARIABLE    = 2,
        PDO_AUGMENTED   = 3
};

#define PD_CONVERT_MA_TO_FIXED_PDO_CURRENT(c) ((c) / 10)

#define PD_CONVERT_MV_TO_FIXED_PDO_VOLTAGE(v) ((v) / 50)

#define PD_CONVERT_FIXED_PDO_CURRENT_TO_MA(c) ((c) * 10)

#define PD_CONVERT_FIXED_PDO_VOLTAGE_TO_MV(v) ((v) * 50)

union pd_fixed_supply_pdo_source {
        struct {
                uint32_t max_current : 10;
                uint32_t voltage : 10;
                uint32_t peak_current : 2;
                uint32_t reserved0 : 2;
                uint32_t unchunked_ext_msg_supported : 1;
                uint32_t dual_role_data : 1;
                uint32_t usb_comms_capable : 1;
                uint32_t unconstrained_power : 1;
                uint32_t usb_suspend_supported : 1;
                uint32_t dual_role_power : 1;
                uint32_t type : 2;
        };
        uint32_t raw_value;
};

enum pd_frs_type {
        FRS_NOT_SUPPORTED,
        FRS_DEFAULT_USB_POWER,
        FRS_1P5A_5V,
        FRS_3P0A_5V
};

union pd_fixed_supply_pdo_sink {
        struct {
                uint32_t operational_current : 10;
                uint32_t voltage : 10;
                uint32_t reserved0 : 3;
                uint32_t frs_required : 2;
                uint32_t dual_role_data : 1;
                uint32_t usb_comms_capable : 1;
                uint32_t unconstrained_power : 1;
                uint32_t higher_capability : 1;
                uint32_t dual_role_power : 1;
                uint32_t type : 2;
        };
        uint32_t raw_value;
};

#define PD_CONVERT_MA_TO_VARIABLE_PDO_CURRENT(c) ((c) / 10)

#define PD_CONVERT_MV_TO_VARIABLE_PDO_VOLTAGE(v) ((v) / 50)

#define PD_CONVERT_VARIABLE_PDO_CURRENT_TO_MA(c) ((c) * 10)

#define PD_CONVERT_VARIABLE_PDO_VOLTAGE_TO_MV(v) ((v) * 50)

union pd_variable_supply_pdo_source {
        struct {
                uint32_t max_current : 10;
                uint32_t min_voltage : 10;
                uint32_t max_voltage : 10;
                uint32_t type : 2;
        };
        uint32_t raw_value;
};

union pd_variable_supply_pdo_sink {
        struct {
                uint32_t operational_current : 10;
                uint32_t min_voltage : 10;
                uint32_t max_voltage : 10;
                uint32_t type : 2;
        };
        uint32_t raw_value;
};

#define PD_CONVERT_MW_TO_BATTERY_PDO_POWER(c) ((c) / 250)

#define PD_CONVERT_MV_TO_BATTERY_PDO_VOLTAGE(v) ((v) / 50)

#define PD_CONVERT_BATTERY_PDO_POWER_TO_MW(c) ((c) * 250)

#define PD_CONVERT_BATTERY_PDO_VOLTAGE_TO_MV(v) ((v) * 50)

union pd_battery_supply_pdo_source {
        struct {
                uint32_t max_power : 10;
                uint32_t min_voltage : 10;
                uint32_t max_voltage : 10;
                uint32_t type : 2;
        };
        uint32_t raw_value;
};

union pd_battery_supply_pdo_sink {
        struct {
                uint32_t operational_power : 10;
                uint32_t min_voltage : 10;
                uint32_t max_voltage : 10;
                uint32_t type : 2;
        };
        uint32_t raw_value;
};

#define PD_CONVERT_MA_TO_AUGMENTED_PDO_CURRENT(c) ((c) / 50)

#define PD_CONVERT_MV_TO_AUGMENTED_PDO_VOLTAGE(v) ((v) / 100)

#define PD_CONVERT_AUGMENTED_PDO_CURRENT_TO_MA(c) ((c) * 50)

#define PD_CONVERT_AUGMENTED_PDO_VOLTAGE_TO_MV(v) ((v) * 100)

union pd_augmented_supply_pdo_source {
        struct {
                uint32_t max_current : 7;
                uint32_t reserved0 : 1;
                uint32_t min_voltage : 8;
                uint32_t reserved1 : 1;
                uint32_t max_voltage : 8;
                uint32_t reserved2 : 2;
                uint32_t pps_power_limited : 1;
                uint32_t reserved3 : 2;
                uint32_t type : 2;
        };
        uint32_t raw_value;
};

union pd_augmented_supply_pdo_sink {
        struct {
                uint32_t max_current : 7;
                uint32_t reserved0 : 1;
                uint32_t min_voltage : 8;
                uint32_t reserved1 : 1;
                uint32_t max_voltage : 8;
                uint32_t reserved2 : 3;
                uint32_t reserved3 : 2;
                uint32_t type : 2;
        };
        uint32_t raw_value;
};

union pd_rdo {
        struct {
                uint32_t min_or_max_operating_current : 10;
                uint32_t operating_current : 10;
                uint32_t reserved0 : 3;
                uint32_t unchunked_ext_msg_supported : 1;
                uint32_t no_usb_suspend : 1;
                uint32_t usb_comm_capable : 1;
                uint32_t cap_mismatch : 1;
                uint32_t giveback : 1;
                uint32_t object_pos : 3;
                uint32_t reserved1 : 1;
        } fixed;

        struct {
                uint32_t min_or_max_operating_current : 10;
                uint32_t operating_current : 10;
                uint32_t reserved0 : 3;
                uint32_t unchunked_ext_msg_supported : 1;
                uint32_t no_usb_suspend : 1;
                uint32_t usb_comm_capable : 1;
                uint32_t cap_mismatch : 1;
                uint32_t giveback : 1;
                uint32_t object_pos : 3;
                uint32_t reserved1 : 1;
        } variable;

        struct {
                uint32_t min_operating_power : 10;
                uint32_t operating_power : 10;
                uint32_t reserved0 : 3;
                uint32_t unchunked_ext_msg_supported : 1;
                uint32_t no_usb_suspend : 1;
                uint32_t usb_comm_capable : 1;
                uint32_t cap_mismatch : 1;
                uint32_t giveback : 1;
                uint32_t object_pos : 3;
                uint32_t reserved1 : 1;
        } battery;

        struct {
                uint32_t operating_current : 7;
                uint32_t reserved0 : 2;
                uint32_t output_voltage : 11;
                uint32_t reserved1 : 3;
                uint32_t unchunked_ext_msg_supported : 1;
                uint32_t no_usb_suspend : 1;
                uint32_t usb_comm_capable : 1;
                uint32_t cap_mismatch : 1;
                uint32_t reserved2 : 1;
                uint32_t object_pos : 3;
                uint32_t reserved3 : 1;
        } augmented;
        uint32_t raw_value;
};

enum pd_rev_type {
        PD_REV10        = 0,
        PD_REV20        = 1,
        PD_REV30        = 2,
};

enum pd_packet_type {
        PD_PACKET_SOP                   = 0,
        PD_PACKET_SOP_PRIME             = 1,
        PD_PACKET_PRIME_PRIME           = 2,
        PD_PACKET_DEBUG_PRIME           = 3,
        PD_PACKET_DEBUG_PRIME_PRIME     = 4,
        PD_PACKET_TX_HARD_RESET         = 5,
        PD_PACKET_CABLE_RESET           = 6,
        PD_PACKET_TX_BIST_MODE_2        = 7,

        PD_PACKET_MSG_INVALID           = 0xf
};

#define NUM_SOP_STAR_TYPES (PD_PACKET_DEBUG_PRIME_PRIME + 1)

enum pd_ctrl_msg_type {

        PD_CTRL_GOOD_CRC        = 1,
        PD_CTRL_GOTO_MIN        = 2,
        PD_CTRL_ACCEPT          = 3,
        PD_CTRL_REJECT          = 4,
        PD_CTRL_PING            = 5,
        PD_CTRL_PS_RDY          = 6,
        PD_CTRL_GET_SOURCE_CAP  = 7,
        PD_CTRL_GET_SINK_CAP    = 8,
        PD_CTRL_DR_SWAP         = 9,
        PD_CTRL_PR_SWAP         = 10,
        PD_CTRL_VCONN_SWAP      = 11,
        PD_CTRL_WAIT            = 12,
        PD_CTRL_SOFT_RESET      = 13,


        PD_CTRL_DATA_RESET              = 14,
        PD_CTRL_DATA_RESET_COMPLETE     = 15,
        PD_CTRL_NOT_SUPPORTED           = 16,
        PD_CTRL_GET_SOURCE_CAP_EXT      = 17,
        PD_CTRL_GET_STATUS              = 18,
        PD_CTRL_FR_SWAP                 = 19,
        PD_CTRL_GET_PPS_STATUS          = 20,
        PD_CTRL_GET_COUNTRY_CODES       = 21,
        PD_CTRL_GET_SINK_CAP_EXT        = 22,
        PD_CTRL_GET_SOURCE_INFO         = 23,
        PD_CTRL_GET_REVISION            = 24,


        PD_CTRL_MSG_COUNT
};

enum pd_data_msg_type {

        PD_DATA_SOURCE_CAP              = 1,
        PD_DATA_REQUEST                 = 2,
        PD_DATA_BIST                    = 3,
        PD_DATA_SINK_CAP                = 4,
        PD_DATA_BATTERY_STATUS          = 5,
        PD_DATA_ALERT                   = 6,
        PD_DATA_GET_COUNTRY_INFO        = 7,


        PD_DATA_ENTER_USB       = 8,
        PD_DATA_EPR_REQUEST     = 9,
        PD_DATA_EPR_MODE        = 10,
        PD_DATA_SOURCE_INFO     = 11,
        PD_DATA_REVISION        = 12,
        PD_DATA_VENDOR_DEF      = 15,

        PD_DATA_MSG_COUNT
};

enum pd_ext_msg_type {

        PD_EXT_SOURCE_CAP               = 1,
        PD_EXT_STATUS                   = 2,
        PD_EXT_GET_BATTERY_CAP          = 3,
        PD_EXT_GET_BATTERY_STATUS       = 4,
        PD_EXT_BATTERY_CAP              = 5,
        PD_EXT_GET_MANUFACTURER_INFO    = 6,
        PD_EXT_MANUFACTURER_INFO        = 7,
        PD_EXT_SECURITY_REQUEST         = 8,
        PD_EXT_SECURITY_RESPONSE        = 9,
        PD_EXT_FIRMWARE_UPDATE_REQUEST  = 10,
        PD_EXT_FIRMWARE_UPDATE_RESPONSE = 11,
        PD_EXT_PPS_STATUS               = 12,
        PD_EXT_COUNTRY_INFO             = 13,
        PD_EXT_COUNTRY_CODES            = 14,
        PD_EXT_SINK_CAP                 = 15,
        PD_EXT_EXTENDED_CONTROL         = 16,
        PD_EXT_EPR_SOURCE_CAP           = 17,
        PD_EXT_EPR_SINK_CAP             = 18,


        PD_EXT_VENDOR_DEFINED           = 30,


        PD_EXT_MSG_COUNT
};

enum usbpd_cc_pin {
        USBPD_CC_PIN_1  = 0,
        USBPD_CC_PIN_2  = 1,
};

struct pd_msg {
        enum pd_packet_type type;
        union pd_header header;
        uint32_t len;
        uint8_t data[PD_MAX_EXTENDED_MSG_LEN];
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_PD_H_ */
```

## 890.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 The Chromium OS Authors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 1105 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_USB_C_USBC_PD_H_`。

## 890.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [pd_header](../device_power_control_model_reference/P114_pd_header_联合体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [message_type](../device_power_control_model_reference/P114_pd_header_联合体.md#a70768acc6a6bc9ebb9249df7ed635a94)
- [port_data_role](../device_power_control_model_reference/P114_pd_header_联合体.md#af1b027c9c57497421117b290dcb6ac66)
- [specification_revision](../device_power_control_model_reference/P114_pd_header_联合体.md#a85cce1728afe0d62bb29f618a1cf70e1)
- [port_power_role](../device_power_control_model_reference/P114_pd_header_联合体.md#a20ac99d9738c9d278a78e8ccfc401902)
- [message_id](../device_power_control_model_reference/P114_pd_header_联合体.md#ae4a0a5695e73fd3e1b7e3f38cd2a758c)
- [number_of_data_objects](../device_power_control_model_reference/P114_pd_header_联合体.md#a63d89119f0918ba7d6eb9e01fa1ed406)
- [extended](../device_power_control_model_reference/P114_pd_header_联合体.md#a5750b964c12c3bc2d2523a64cb9eb7d0)
- [raw_value](../device_power_control_model_reference/P114_pd_header_联合体.md#afa6c6699be5fe95bcb4962396e33e35d)
- [pd_ext_header](../device_power_control_model_reference/P111_pd_ext_header_联合体.md)
- [data_size](../device_power_control_model_reference/P111_pd_ext_header_联合体.md#a4a7a948d3463ddfbebf1d75faeda293e)
- [reserved0](../device_power_control_model_reference/P111_pd_ext_header_联合体.md#aae09d0399c0a121e3c216047e908b9ec)
- [request_chunk](../device_power_control_model_reference/P111_pd_ext_header_联合体.md#a36a65a1e52875721758d1273b0e76279)
- [chunk_number](../device_power_control_model_reference/P111_pd_ext_header_联合体.md#aced0489c4e2462652c0d91187c07b27e)
- [chunked](../device_power_control_model_reference/P111_pd_ext_header_联合体.md#a180ccc6854c1341e638ca338e6eb1cd8)
- [raw_value](../device_power_control_model_reference/P111_pd_ext_header_联合体.md#a8a1d0f0d38b3a5c4aa3a80586e7a1e8f)
- [pdo_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga316dca7ed0b85f1aa224d7a767896328)
- [PDO_FIXED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery__pdo.html#ga9fa615ab7f38385c21277d4e9e6a1441)
- [PDO_BATTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga316dca7ed0b85f1aa224d7a767896328a63f4fb7a4d2f7e265fd49be07966fbaa)
- [PDO_VARIABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga316dca7ed0b85f1aa224d7a767896328a1726efca9ece0ff017cc4aaf05ce9624)
- [PDO_AUGMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga316dca7ed0b85f1aa224d7a767896328adb8478434cc1622e98bc22f4081dff1e)
- [pd_fixed_supply_pdo_source](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [max_current](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a86664d945f65f19f7b96da1148700640)
- [voltage](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a66f55e177b6f2bc76b392707e39fa4fe)
- [peak_current](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a2c4b27407245da04b67e9524173d39bc)
- [reserved0](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a6b0e04acd43c9b18bd1dea80508a8817)
- [unchunked_ext_msg_supported](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a440ff92d2bd533e3ddd6c65f9ac21772)
- [dual_role_data](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a7b89666e3753966001caf7602c796147)
- [usb_comms_capable](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a6c1bcf37a1fc9a348cf19e16fbe01dac)
- [unconstrained_power](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a9fc10f3ec4126c063f5dd99e8f3e2723)
- [usb_suspend_supported](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a55003edba55a920a386cc04cbc7a72a0)
- [dual_role_power](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#af96673f1ac078436a9eca0973e1bdef9)
- [type](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#aff4c1e7eab502a68e80013b4010aff76)
- [raw_value](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a9227629f6c97357b71ea20e4e0572cf2)
- [pd_frs_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga48b33240e19524ea003052103d310358)
- [FRS_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga48b33240e19524ea003052103d310358acbf2bf3ae21ff1ea51d7fd2b823ce726)
- [FRS_DEFAULT_USB_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga48b33240e19524ea003052103d310358a4cd44f89f225f8869bfd901e7ea79aed)
- [FRS_1P5A_5V](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga48b33240e19524ea003052103d310358acac5008ded87d7a20b0b3b272075e4c1)
- [FRS_3P0A_5V](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga48b33240e19524ea003052103d310358a99ab2afc15809b5e89e3fb7106be37ba)
- [pd_fixed_supply_pdo_sink](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md)
- [operational_current](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a2ac4005b0cf3e28ade8f508d2c6f5e20)
- [voltage](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#ac47dcf98dfca90eb0e6013a3e1c5eb18)
- [reserved0](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a22f9763652560dbd215324f1bb878a96)
- [frs_required](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a7a26a084dd6004f9121c8493a0c520f6)
- [dual_role_data](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a5c6bfb21c4d8e70a04895dd31a58885e)
- [usb_comms_capable](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a0559272067e2d0c33f52274fb59ea18d)
- [unconstrained_power](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#ab406f1f36e5fe6f7acb9abc91991a803)
- [higher_capability](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a3086d57313f05b8bc91fb3590e51c657)
- [dual_role_power](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#aad255dbee3452bf3276464c59f113cb2)
- [type](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a3945768e406175b51f9c4b8c3d0e9848)
- [raw_value](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#aebdeb854bcac0d20efcbe3be56dcc9f8)
- [pd_variable_supply_pdo_source](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md)
- [max_current](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md#a8193ca96084db5901bb30195113ff01f)
- [min_voltage](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md#a67d86c71997a7c0605b8a199cd51c920)
- [max_voltage](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md#a008cf5201ea6d3e238d547b738570c45)
- [type](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md#aabd59b2c5f4bfbbbd5d70adfb009eaf7)
- [raw_value](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md#af00512126f128bf1cf31e802652af1bf)
- [pd_variable_supply_pdo_sink](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md)
- [operational_current](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md#ad648f2400a495b37d8b9f995556419d0)
- [min_voltage](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md#aaaa1cf3f08208966fb00093f910f70ab)
- [max_voltage](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md#ae360e7c2335a4f6cf5d267c8c82fdc45)
- [type](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md#ab7472487f253f5c2cb4d69eb805ede46)
- [raw_value](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md#a2ff80c049f98ab090b100b7f9877bffb)
- [pd_battery_supply_pdo_source](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md)
- [max_power](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md#a00ea9931d839cf83b56513f77aa7d5b9)
- [min_voltage](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md#afa2335788e7fde01b90afd95bccf6d5f)
- [max_voltage](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md#a673ea076da8810bc694b2dc82bbede67)
- [type](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md#ac7157c3fbae86d34e2c7d82bf9af3a3f)
- [raw_value](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md#a1e775dc0082b531216c154724be360b0)
- [pd_battery_supply_pdo_sink](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md)
- [operational_power](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md#a3f1072c4ca168aaedd13257f01f410aa)
- [min_voltage](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md#a5a588a46ae8bef2dc10445c2f5422246)
- [max_voltage](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md#a858efb23a0c143917b88e5596b899c79)
- [type](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md#a515f6958ba647dc77a30414732afd82b)
- [raw_value](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md#aa973b26972c1e1a96c7e0c09dbed08f3)
- [pd_augmented_supply_pdo_source](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md)
- [max_current](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#a7ef0b26951ce2683c9c4ca0f19b73d6d)
- [reserved0](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#ac046ddf128416ecbb8f3a26185d03e03)
- [min_voltage](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#a56e1af2acda73fee7e40449b7c39745d)
- [reserved1](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#ae79eb7473040058c0b8572cfe4fa4dce)
- [max_voltage](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#aba6df91a8c5da92517f885fa89af8747)
- [reserved2](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#ab5868f6ba91821d56ddb419e895a05fa)
- [pps_power_limited](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#abfac34ee5da0b1700b784c7bfe925c19)
- [reserved3](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#aa59ad8a8eb4e2343c14bbe54937aa93d)
- [type](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#ae064d7413ede09780ad7314ce31caaa1)
- [raw_value](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#a093a674e538dcc2541ff86f50d0156df)
- [pd_augmented_supply_pdo_sink](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md)
- [max_current](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#a0a5da0df48dff5fae42159026c91c7af)
- [reserved0](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#a3320455a4c7673d3db95f585b07cc319)
- [min_voltage](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#ad83710136d9dcad3644ec36c1eee9cb0)
- [reserved1](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#a2f1f6094af7449619ab626476fa51698)
- [max_voltage](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#af5eca8ab38a3eaaaecd10cdc1092ce3c)
- [reserved2](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#adfa0b8ab656255cfecc9ca5e1ee05d49)
- [reserved3](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#a22e63fa7e83af25d9822dcf3d9b35f40)
- [type](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#aa800bd5299c535e5de98d57aec1b2fff)
- [raw_value](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#ae28a74642ffcdf1100f37e3542e1ca96)
- [pd_rdo](../device_power_control_model_reference/P115_pd_rdo_联合体.md)
- [min_or_max_operating_current](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a41d023e9308e6d252f0bc8412a6c6184)
- [operating_current](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a8c11df4b75772cda511bd94e5a297128)
- [reserved0](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ab4065aee18c3a68df38592122f607343)
- [unchunked_ext_msg_supported](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ae71e9abde3d69211c7bcfc7b80d18c41)
- [no_usb_suspend](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ae90a23cc166373f7bb3c35be0c3967f2)
- [usb_comm_capable](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a30f6044378cad6f277f8694df5611230)
- [cap_mismatch](../device_power_control_model_reference/P115_pd_rdo_联合体.md#afd24863b120085c57e77b8d246effd54)
- [giveback](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ae5ae5d3c823254ab895becc3b01761fe)
- [object_pos](../device_power_control_model_reference/P115_pd_rdo_联合体.md#aff1b20a6e4905ac714ab5e7af7ff9593)
- [reserved1](../device_power_control_model_reference/P115_pd_rdo_联合体.md#aa5af5685e6d9c3d8a7ec3a40d25b43ba)
- [fixed](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a0b7502c79b0976b8e0d118cae3950191)
- [variable](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a82e1adf30b6fc476b794b94cfb379214)
- [min_operating_power](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ab59da7098c1d33c9269f66dd3ac3fc5b)
- [operating_power](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a63dd2a9e94f3a61205b95efc0cf79f13)
- [battery](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a5838022e249981be50aee897c16ce56e)
- [output_voltage](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ad7a98411aad054f1161b4ce32ef3ee33)
- [reserved2](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a5f8b64ce53d9881a007405a986b6b490)
- [reserved3](../device_power_control_model_reference/P115_pd_rdo_联合体.md#aa0ddbfb3c345b671f97d4b4e760168b4)
- [augmented](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ad6b45a879e689dcd05bf9e07aedc4d20)
- [raw_value](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a477cf38b68b9386e950c085a1ce4f336)
- [pd_rev_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gab68c6b6e33449c5ceadfc9217dd7a700)
- [PD_REV10](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggab68c6b6e33449c5ceadfc9217dd7a700a1d9b4c553f44dccdc67e4edb554557b9)
- [PD_REV20](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggab68c6b6e33449c5ceadfc9217dd7a700a22c122b1d30a3ab96fffd5dfa6bfb9ae)
- [PD_REV30](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggab68c6b6e33449c5ceadfc9217dd7a700af3770bcbcf6feaaab272c022d7a57c7a)
- [pd_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad2df13a24f0365198d37b10af608376b)
- [PD_PACKET_SOP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba0bede6a56c24b06fdf56cf1dc386bb14)
- [PD_PACKET_SOP_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376bae3a5f99242ab24a34706170101b38ef8)
- [PD_PACKET_PRIME_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba5ecd663a9eecefcf965f605125d5188c)
- [PD_PACKET_DEBUG_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba63b2200ebaf016d06437f3586d15171d)
- [PD_PACKET_DEBUG_PRIME_PRIME](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba4ffb0f82eaca719f7db5fa9180ce46d1)
- [PD_PACKET_TX_HARD_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376baa5cd066e86fd55727c3625cd16633f73)
- [PD_PACKET_CABLE_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba531ebc6013984b81e6fb550618d6b4a8)
- [PD_PACKET_TX_BIST_MODE_2](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376bafcd21cc6b1ae6c58b86c0619d687e8fc)
- [PD_PACKET_MSG_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggad2df13a24f0365198d37b10af608376ba55bb88e5955992170bee96ddbe8a7437)
- [pd_ctrl_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga4c7862a3e953fb22534123223c942f9a)
- [PD_CTRL_GOOD_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aae0895be53e5a1e54731e9608a8e0c6c9)
- [PD_CTRL_GOTO_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa4ba7f63cdcbe766a34047e06145a591e)
- [PD_CTRL_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa56df68ed627b56bbcfc20900ec5d2e5d)
- [PD_CTRL_REJECT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa9dd7b559e78a99639056325a7be14d81)
- [PD_CTRL_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa8177040ca8a1f71dde67fc59060c35ed)
- [PD_CTRL_PS_RDY](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aafc449fc3dc39f2495494507cc97f53ad)
- [PD_CTRL_GET_SOURCE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa9324307526500683ae265e9cb0063929)
- [PD_CTRL_GET_SINK_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aaaf5c221569a9108bdbc36545dcb37495)
- [PD_CTRL_DR_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa4aba967f7e363dbbadcc9a9ecf0c7ae4)
- [PD_CTRL_PR_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aade67c4fb153e5ba87b6d6643f99260f9)
- [PD_CTRL_VCONN_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa68820e99ce9c1c73180734372e5ede2b)
- [PD_CTRL_WAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa3b6fc49b1ae0bb343d39476350b59c90)
- [PD_CTRL_SOFT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aadeb12ed01ec54ee55588bfb796dd0c11)
- [PD_CTRL_DATA_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa03f9886881aa493fb0f9bfac16713e7a)
- [PD_CTRL_DATA_RESET_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa27caca37f9522045bc8612f7536cd792)
- [PD_CTRL_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aabfea5fdf0263fdf4c924bd603ee7256f)
- [PD_CTRL_GET_SOURCE_CAP_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aab0ca2628b144d092116b461703176eaa)
- [PD_CTRL_GET_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa23287276ee22241906828515f38fedef)
- [PD_CTRL_FR_SWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa1c597b5f953e6e1791aa869025b98b24)
- [PD_CTRL_GET_PPS_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aab82efb96b1f8f7dae3c76e362ae1715a)
- [PD_CTRL_GET_COUNTRY_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa677ebc41b4b67de6ee93b5e446af702e)
- [PD_CTRL_GET_SINK_CAP_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aaaa0a5bba9a9f1573952141c4f8f77318)
- [PD_CTRL_GET_SOURCE_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa28bd36a3d8c92ba6ea2943b0617fe6af)
- [PD_CTRL_GET_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa189edfda108af04877adc2025cabb1eb)
- [PD_CTRL_MSG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga4c7862a3e953fb22534123223c942f9aa676239b098266cbec7c448dbaeebfa6c)
- [pd_data_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga8239651864b4cb0e1fc89ba2d7e59462)
- [PD_DATA_SOURCE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462ad9a0cf16cfa852111ea0ed3434b35dfc)
- [PD_DATA_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462ad9c920f987e2578b030cc08f2e69998a)
- [PD_DATA_BIST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a7c4bc907fb81082da05c64797854be9f)
- [PD_DATA_SINK_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a4cf30dcbce3fdf8076713e45d242b39a)
- [PD_DATA_BATTERY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462ad493f01ffc4c3c164f874eb202f8adb0)
- [PD_DATA_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a7e3368e1c7bde4c6bb3136cb80209bb6)
- [PD_DATA_GET_COUNTRY_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a83d7098236e97972cf24b900f7e5e069)
- [PD_DATA_ENTER_USB](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a1a0829560f9f82182f7587fd8787a846)
- [PD_DATA_EPR_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a5352e00ba0ae91b14a8ecff9107e1bca)
- [PD_DATA_EPR_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462ad8b62eecdf3b574585d259bb6cb34564)
- [PD_DATA_SOURCE_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462abd9d5984a02b719e3d9599d0228aa99e)
- [PD_DATA_REVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462aaea7d41eb22db0a06d676714d0598ee0)
- [PD_DATA_VENDOR_DEF](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a881fcbc2dc5f8b1de7c97522df46242d)
- [PD_DATA_MSG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga8239651864b4cb0e1fc89ba2d7e59462a648d1d50d51c5999e053ddcee92c30db)
- [pd_ext_msg_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ga457308d50365e0a2440e94e41a316cbf)
- [PD_EXT_SOURCE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa51c03e44c3fe1bb59445bbc452ea7199)
- [PD_EXT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa836130da5307aed6160deadadf2f4f3f)
- [PD_EXT_GET_BATTERY_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa9c50488735d7723c3cc30f176c221e40)
- [PD_EXT_GET_BATTERY_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa77ff801aa819461f0f5ff44546370bd7)
- [PD_EXT_BATTERY_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfae7f7b3f7233bb5cf600338b4a2c601c0)
- [PD_EXT_GET_MANUFACTURER_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfac8fc4c3c64fb3eaba8cb61bd999c7033)
- [PD_EXT_MANUFACTURER_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa500d77f178123eab8073058dd9308ea6)
- [PD_EXT_SECURITY_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa0f62aa3774995018514dcd2f75ac1c1f)
- [PD_EXT_SECURITY_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfad002882e8bce9cdfdb0864cd6a3e79a7)
- [PD_EXT_FIRMWARE_UPDATE_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa2a7b6a78cf3fd87a86f060f927b566af)
- [PD_EXT_FIRMWARE_UPDATE_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa4fe2d7028fa2bdf594cb8c87ac05fe67)
- [PD_EXT_PPS_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa7d04da3fdb96eac97200d11eb2dbe083)
- [PD_EXT_COUNTRY_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfaa21adc92574ed1261b6c13df3592601b)
- [PD_EXT_COUNTRY_CODES](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfae69b4a8ddba29bc6cd69d50c946bc658)
- [PD_EXT_SINK_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa84ef06f718993e00134040d427b93591)
- [PD_EXT_EXTENDED_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfaf3cdbd6af73a63879a5985e8db1e0d7f)
- [PD_EXT_EPR_SOURCE_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa0544591815d3b3666db44d5cff561f83)
- [PD_EXT_EPR_SINK_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfae569507687c904dc65827c6a737012a5)
- [PD_EXT_VENDOR_DEFINED](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfa20d43a6bdbd425d8f17c01d6e6cbcce3)
- [PD_EXT_MSG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gga457308d50365e0a2440e94e41a316cbfacb6e48382233e62151ab1a1fd845d429)
- [usbpd_cc_pin](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gaee2fe2128557939404c62e8104269bbf)
- [USBPD_CC_PIN_1](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggaee2fe2128557939404c62e8104269bbfa59a0ed05c4e99acebaa11080dbbe7694)
- [USBPD_CC_PIN_2](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#ggaee2fe2128557939404c62e8104269bbfa53a0a6ba0212b9cbb407522e7f35648e)
- [pd_msg](../device_power_control_model_reference/P055_pd_msg_结构体.md)
- [type](../device_power_control_model_reference/P055_pd_msg_结构体.md#af9f676afd2c2824fb9f01a08d8339231)
- [header](../device_power_control_model_reference/P055_pd_msg_结构体.md#ae6f1fa8a1fb006e3d90e75cd834e6d05)
- [len](../device_power_control_model_reference/P055_pd_msg_结构体.md#aa03ec4ce6d2f0d16a829394ff0ed2688)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../device_power_control_model_reference/P055_pd_msg_结构体.md#ad6fd282617b5f6dfeeef6cf4598883ee)
- [PD_MAX_EXTENDED_MSG_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gabdb041542baaf2277e054dd9e3928b16)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [pd_msg::len](../device_power_control_model_reference/P055_pd_msg_结构体.md#aa03ec4ce6d2f0d16a829394ff0ed2688)
- [pd_msg::data](../device_power_control_model_reference/P055_pd_msg_结构体.md#ad6fd282617b5f6dfeeef6cf4598883ee)
- [pd_msg::header](../device_power_control_model_reference/P055_pd_msg_结构体.md#ae6f1fa8a1fb006e3d90e75cd834e6d05)
- [pd_msg::type](../device_power_control_model_reference/P055_pd_msg_结构体.md#af9f676afd2c2824fb9f01a08d8339231)
- [pd_augmented_supply_pdo_sink::max_current](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#a0a5da0df48dff5fae42159026c91c7af)
- [pd_augmented_supply_pdo_sink::reserved3](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#a22e63fa7e83af25d9822dcf3d9b35f40)
- [pd_augmented_supply_pdo_sink::reserved1](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#a2f1f6094af7449619ab626476fa51698)
- [pd_augmented_supply_pdo_sink::reserved0](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#a3320455a4c7673d3db95f585b07cc319)
- [pd_augmented_supply_pdo_sink::type](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#aa800bd5299c535e5de98d57aec1b2fff)
- [pd_augmented_supply_pdo_sink::min_voltage](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#ad83710136d9dcad3644ec36c1eee9cb0)
- [pd_augmented_supply_pdo_sink::reserved2](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#adfa0b8ab656255cfecc9ca5e1ee05d49)
- [pd_augmented_supply_pdo_sink::raw_value](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#ae28a74642ffcdf1100f37e3542e1ca96)
- [pd_augmented_supply_pdo_sink::max_voltage](../device_power_control_model_reference/P107_pd_augmented_supply_pdo_sink_联合体.md#af5eca8ab38a3eaaaecd10cdc1092ce3c)
- [pd_augmented_supply_pdo_source::raw_value](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#a093a674e538dcc2541ff86f50d0156df)
- [pd_augmented_supply_pdo_source::min_voltage](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#a56e1af2acda73fee7e40449b7c39745d)
- [pd_augmented_supply_pdo_source::max_current](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#a7ef0b26951ce2683c9c4ca0f19b73d6d)
- [pd_augmented_supply_pdo_source::reserved3](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#aa59ad8a8eb4e2343c14bbe54937aa93d)
- [pd_augmented_supply_pdo_source::reserved2](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#ab5868f6ba91821d56ddb419e895a05fa)
- [pd_augmented_supply_pdo_source::max_voltage](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#aba6df91a8c5da92517f885fa89af8747)
- [pd_augmented_supply_pdo_source::pps_power_limited](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#abfac34ee5da0b1700b784c7bfe925c19)
- [pd_augmented_supply_pdo_source::reserved0](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#ac046ddf128416ecbb8f3a26185d03e03)
- [pd_augmented_supply_pdo_source::type](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#ae064d7413ede09780ad7314ce31caaa1)
- [pd_augmented_supply_pdo_source::reserved1](../device_power_control_model_reference/P108_pd_augmented_supply_pdo_source_联合体.md#ae79eb7473040058c0b8572cfe4fa4dce)
- [pd_battery_supply_pdo_sink::operational_power](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md#a3f1072c4ca168aaedd13257f01f410aa)
- [pd_battery_supply_pdo_sink::type](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md#a515f6958ba647dc77a30414732afd82b)
- [pd_battery_supply_pdo_sink::min_voltage](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md#a5a588a46ae8bef2dc10445c2f5422246)
- [pd_battery_supply_pdo_sink::max_voltage](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md#a858efb23a0c143917b88e5596b899c79)
- [pd_battery_supply_pdo_sink::raw_value](../device_power_control_model_reference/P109_pd_battery_supply_pdo_sink_联合体.md#aa973b26972c1e1a96c7e0c09dbed08f3)
- [pd_battery_supply_pdo_source::max_power](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md#a00ea9931d839cf83b56513f77aa7d5b9)
- [pd_battery_supply_pdo_source::raw_value](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md#a1e775dc0082b531216c154724be360b0)
- [pd_battery_supply_pdo_source::max_voltage](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md#a673ea076da8810bc694b2dc82bbede67)
- [pd_battery_supply_pdo_source::type](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md#ac7157c3fbae86d34e2c7d82bf9af3a3f)
- [pd_battery_supply_pdo_source::min_voltage](../device_power_control_model_reference/P110_pd_battery_supply_pdo_source_联合体.md#afa2335788e7fde01b90afd95bccf6d5f)
- [pd_ext_header::chunked](../device_power_control_model_reference/P111_pd_ext_header_联合体.md#a180ccc6854c1341e638ca338e6eb1cd8)
- [pd_ext_header::request_chunk](../device_power_control_model_reference/P111_pd_ext_header_联合体.md#a36a65a1e52875721758d1273b0e76279)
- [pd_ext_header::data_size](../device_power_control_model_reference/P111_pd_ext_header_联合体.md#a4a7a948d3463ddfbebf1d75faeda293e)
- [pd_ext_header::raw_value](../device_power_control_model_reference/P111_pd_ext_header_联合体.md#a8a1d0f0d38b3a5c4aa3a80586e7a1e8f)
- [pd_ext_header::reserved0](../device_power_control_model_reference/P111_pd_ext_header_联合体.md#aae09d0399c0a121e3c216047e908b9ec)
- [pd_ext_header::chunk_number](../device_power_control_model_reference/P111_pd_ext_header_联合体.md#aced0489c4e2462652c0d91187c07b27e)
- [pd_fixed_supply_pdo_sink::usb_comms_capable](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a0559272067e2d0c33f52274fb59ea18d)
- [pd_fixed_supply_pdo_sink::reserved0](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a22f9763652560dbd215324f1bb878a96)
- [pd_fixed_supply_pdo_sink::operational_current](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a2ac4005b0cf3e28ade8f508d2c6f5e20)
- [pd_fixed_supply_pdo_sink::higher_capability](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a3086d57313f05b8bc91fb3590e51c657)
- [pd_fixed_supply_pdo_sink::type](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a3945768e406175b51f9c4b8c3d0e9848)
- [pd_fixed_supply_pdo_sink::dual_role_data](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a5c6bfb21c4d8e70a04895dd31a58885e)
- [pd_fixed_supply_pdo_sink::frs_required](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#a7a26a084dd6004f9121c8493a0c520f6)
- [pd_fixed_supply_pdo_sink::dual_role_power](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#aad255dbee3452bf3276464c59f113cb2)
- [pd_fixed_supply_pdo_sink::unconstrained_power](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#ab406f1f36e5fe6f7acb9abc91991a803)
- [pd_fixed_supply_pdo_sink::voltage](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#ac47dcf98dfca90eb0e6013a3e1c5eb18)
- [pd_fixed_supply_pdo_sink::raw_value](../device_power_control_model_reference/P112_pd_fixed_supply_pdo_sink_联合体.md#aebdeb854bcac0d20efcbe3be56dcc9f8)
- [pd_fixed_supply_pdo_source::peak_current](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a2c4b27407245da04b67e9524173d39bc)
- [pd_fixed_supply_pdo_source::unchunked_ext_msg_supported](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a440ff92d2bd533e3ddd6c65f9ac21772)
- [pd_fixed_supply_pdo_source::usb_suspend_supported](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a55003edba55a920a386cc04cbc7a72a0)
- [pd_fixed_supply_pdo_source::voltage](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a66f55e177b6f2bc76b392707e39fa4fe)
- [pd_fixed_supply_pdo_source::reserved0](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a6b0e04acd43c9b18bd1dea80508a8817)
- [pd_fixed_supply_pdo_source::usb_comms_capable](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a6c1bcf37a1fc9a348cf19e16fbe01dac)
- [pd_fixed_supply_pdo_source::dual_role_data](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a7b89666e3753966001caf7602c796147)
- [pd_fixed_supply_pdo_source::max_current](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a86664d945f65f19f7b96da1148700640)
- [pd_fixed_supply_pdo_source::raw_value](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a9227629f6c97357b71ea20e4e0572cf2)
- [pd_fixed_supply_pdo_source::unconstrained_power](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#a9fc10f3ec4126c063f5dd99e8f3e2723)
- [pd_fixed_supply_pdo_source::dual_role_power](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#af96673f1ac078436a9eca0973e1bdef9)
- [pd_fixed_supply_pdo_source::type](../device_power_control_model_reference/P113_pd_fixed_supply_pdo_source_联合体.md#aff4c1e7eab502a68e80013b4010aff76)
- [pd_header::port_power_role](../device_power_control_model_reference/P114_pd_header_联合体.md#a20ac99d9738c9d278a78e8ccfc401902)
- [pd_header::extended](../device_power_control_model_reference/P114_pd_header_联合体.md#a5750b964c12c3bc2d2523a64cb9eb7d0)
- [pd_header::number_of_data_objects](../device_power_control_model_reference/P114_pd_header_联合体.md#a63d89119f0918ba7d6eb9e01fa1ed406)
- [pd_header::message_type](../device_power_control_model_reference/P114_pd_header_联合体.md#a70768acc6a6bc9ebb9249df7ed635a94)
- [pd_header::specification_revision](../device_power_control_model_reference/P114_pd_header_联合体.md#a85cce1728afe0d62bb29f618a1cf70e1)
- [pd_header::message_id](../device_power_control_model_reference/P114_pd_header_联合体.md#ae4a0a5695e73fd3e1b7e3f38cd2a758c)
- [pd_header::port_data_role](../device_power_control_model_reference/P114_pd_header_联合体.md#af1b027c9c57497421117b290dcb6ac66)
- [pd_header::raw_value](../device_power_control_model_reference/P114_pd_header_联合体.md#afa6c6699be5fe95bcb4962396e33e35d)
- [pd_rdo::fixed](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a0b7502c79b0976b8e0d118cae3950191)
- [pd_rdo::usb_comm_capable](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a30f6044378cad6f277f8694df5611230)
- [pd_rdo::min_or_max_operating_current](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a41d023e9308e6d252f0bc8412a6c6184)
- [pd_rdo::raw_value](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a477cf38b68b9386e950c085a1ce4f336)
- [pd_rdo::battery](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a5838022e249981be50aee897c16ce56e)
- [pd_rdo::reserved2](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a5f8b64ce53d9881a007405a986b6b490)
- [pd_rdo::operating_power](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a63dd2a9e94f3a61205b95efc0cf79f13)
- [pd_rdo::variable](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a82e1adf30b6fc476b794b94cfb379214)
- [pd_rdo::operating_current](../device_power_control_model_reference/P115_pd_rdo_联合体.md#a8c11df4b75772cda511bd94e5a297128)
- [pd_rdo::reserved3](../device_power_control_model_reference/P115_pd_rdo_联合体.md#aa0ddbfb3c345b671f97d4b4e760168b4)
- [pd_rdo::reserved1](../device_power_control_model_reference/P115_pd_rdo_联合体.md#aa5af5685e6d9c3d8a7ec3a40d25b43ba)
- [pd_rdo::reserved0](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ab4065aee18c3a68df38592122f607343)
- [pd_rdo::min_operating_power](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ab59da7098c1d33c9269f66dd3ac3fc5b)
- [pd_rdo::augmented](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ad6b45a879e689dcd05bf9e07aedc4d20)
- [pd_rdo::output_voltage](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ad7a98411aad054f1161b4ce32ef3ee33)
- [pd_rdo::giveback](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ae5ae5d3c823254ab895becc3b01761fe)
- [pd_rdo::unchunked_ext_msg_supported](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ae71e9abde3d69211c7bcfc7b80d18c41)
- [pd_rdo::no_usb_suspend](../device_power_control_model_reference/P115_pd_rdo_联合体.md#ae90a23cc166373f7bb3c35be0c3967f2)
- [pd_rdo::cap_mismatch](../device_power_control_model_reference/P115_pd_rdo_联合体.md#afd24863b120085c57e77b8d246effd54)
- [pd_rdo::object_pos](../device_power_control_model_reference/P115_pd_rdo_联合体.md#aff1b20a6e4905ac714ab5e7af7ff9593)
- [pd_variable_supply_pdo_sink::raw_value](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md#a2ff80c049f98ab090b100b7f9877bffb)
- [pd_variable_supply_pdo_sink::min_voltage](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md#aaaa1cf3f08208966fb00093f910f70ab)
- [pd_variable_supply_pdo_sink::type](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md#ab7472487f253f5c2cb4d69eb805ede46)
- [pd_variable_supply_pdo_sink::operational_current](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md#ad648f2400a495b37d8b9f995556419d0)
- [pd_variable_supply_pdo_sink::max_voltage](../device_power_control_model_reference/P116_pd_variable_supply_pdo_sink_联合体.md#ae360e7c2335a4f6cf5d267c8c82fdc45)
- [pd_variable_supply_pdo_source::max_voltage](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md#a008cf5201ea6d3e238d547b738570c45)
- [pd_variable_supply_pdo_source::min_voltage](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md#a67d86c71997a7c0605b8a199cd51c920)
- [pd_variable_supply_pdo_source::max_current](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md#a8193ca96084db5901bb30195113ff01f)
- [pd_variable_supply_pdo_source::type](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md#aabd59b2c5f4bfbbbd5d70adfb009eaf7)
- [pd_variable_supply_pdo_source::raw_value](../device_power_control_model_reference/P117_pd_variable_supply_pdo_source_联合体.md#af00512126f128bf1cf31e802652af1bf)

---

[上一章](P889_usbc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P891_usbc_tc.h_源码浏览.md)
