---
id: learning.zephyr-docs.api-source-reference.page-701
title: regulator.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/regulator_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第701章\_regulator.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/regulator_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../power/P082_稳压器头文件.md)。

## 701.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
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
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00103"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="foldopen00120"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="foldopen00238"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00264"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00274"></a>
<a id="l00276"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00289"></a>
<a id="l00291"></a>
<a id="l00293"></a>
<a id="l00295"></a>
<a id="l00297"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00308"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00317"></a>
<a id="l00319"></a>
<a id="l00321"></a>
<a id="l00323"></a>
<a id="l00325"></a>
<a id="l00327"></a>
<a id="l00329"></a>
<a id="l00331"></a>
<a id="l00333"></a>
<a id="l00335"></a>
<a id="l00337"></a>
<a id="l00339"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00496"></a>
<a id="l00502"></a>
<a id="foldopen00521"></a>
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
<a id="l00532"></a>
<a id="foldopen00546"></a>
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
<a id="l00558"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="foldopen00612"></a>
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
<a id="foldopen00638"></a>
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
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00662"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="foldopen00692"></a>
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
<a id="l00703"></a>
<a id="foldopen00715"></a>
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
<a id="foldopen00741"></a>
<a id="l00741"></a>
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
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="foldopen00781"></a>
<a id="l00781"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="l00787"></a>
<a id="l00788"></a>
<a id="l00789"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="foldopen00819"></a>
<a id="l00819"></a>
<a id="l00820"></a>
<a id="l00821"></a>
<a id="l00822"></a>
<a id="l00823"></a>
<a id="l00824"></a>
<a id="l00825"></a>
<a id="l00826"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00830"></a>
<a id="foldopen00840"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00844"></a>
<a id="l00845"></a>
<a id="l00846"></a>
<a id="l00847"></a>
<a id="l00848"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="foldopen00861"></a>
<a id="l00861"></a>
<a id="l00862"></a>
<a id="l00863"></a>
<a id="l00864"></a>
<a id="l00865"></a>
<a id="l00866"></a>
<a id="l00867"></a>
<a id="l00868"></a>
<a id="l00869"></a>
<a id="l00870"></a>
<a id="l00871"></a>
<a id="l00872"></a>
<a id="foldopen00882"></a>
<a id="l00882"></a>
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
<a id="foldopen00908"></a>
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00914"></a>
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
<a id="l00926"></a>
<a id="l00927"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adevicetree_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__regulator__interface__backend_html_ga04294f2fd8c407a1a02cd638ec16d45a"></a>
<a id="agroup__regulator__interface__backend_html_ga0c853ff39ff2917d88c10bd977628e1b"></a>
<a id="agroup__regulator__interface__backend_html_ga1ace8d15380b1fca67b548e3c2c0405c"></a>
<a id="agroup__regulator__interface__backend_html_ga3693adfe8e04fcf9bdce57ba01bc34b3"></a>
<a id="agroup__regulator__interface__backend_html_ga43024f6b46b8848ef6e71de3371602d9"></a>
<a id="agroup__regulator__interface__backend_html_ga4e89c959579f7ec7f0a6cba603c50c89"></a>
<a id="agroup__regulator__interface__backend_html_ga80065f9f5047a6c2ef7e5d8ee24eb38f"></a>
<a id="agroup__regulator__interface__backend_html_ga91e98af520b227d40398b8650db333ae"></a>
<a id="agroup__regulator__interface__backend_html_gaa163eb9b3a1349d5041db5772b982dec"></a>
<a id="agroup__regulator__interface__backend_html_gaadb2a63751a32597956553b6adad7fa7"></a>
<a id="agroup__regulator__interface__backend_html_gac32c41a87d721bc1b40dc0d7227f6500"></a>
<a id="agroup__regulator__interface__backend_html_gacbdbc2b57156375be8df792504fdc405"></a>
<a id="agroup__regulator__interface__backend_html_gada21d0f316c2717d497b4366adbe4cea"></a>
<a id="agroup__regulator__interface__backend_html_gadaadd2c07a557631a3dbebc609b6cccc"></a>
<a id="agroup__regulator__interface__backend_html_gadbfc2002a32b833e8eb115c8fa7e315f"></a>
<a id="agroup__regulator__interface__backend_html_gae3e867ce3ef2d819fb7f5ad9a22ccf39"></a>
<a id="agroup__regulator__interface__backend_html_gae7b3f6d6e0df901aeb0b8102482d3124"></a>
<a id="agroup__regulator__interface__backend_html_gaeeb7b0d0f864de9314ae0d5a11eb9a00"></a>
<a id="agroup__regulator__interface_html_ga00b6235e23061028c45cf7160773677d"></a>
<a id="agroup__regulator__interface_html_ga06e3109b9607521fe07686c6d601e460"></a>
<a id="agroup__regulator__interface_html_ga1877bac62c2b81ee37deb86bfae302af"></a>
<a id="agroup__regulator__interface_html_ga1971bd21b504979a0cecab16048a0d03"></a>
<a id="agroup__regulator__interface_html_ga27de51302b5222f860457c5b8bd494d6"></a>
<a id="agroup__regulator__interface_html_ga28744a6cabadfe5a22bc96792c8ad124"></a>
<a id="agroup__regulator__interface_html_ga2c2b345da9029013edbf59fd8c565d85"></a>
<a id="agroup__regulator__interface_html_ga2ccf66175b37754e2c21f341ecb2acbd"></a>
<a id="agroup__regulator__interface_html_ga31b42ddfe94fee47158632f355ad864c"></a>
<a id="agroup__regulator__interface_html_ga31dae130509d28ee41602ab16ab31a90"></a>
<a id="agroup__regulator__interface_html_ga58d9e06c6da52a9733b3979d72915ab3"></a>
<a id="agroup__regulator__interface_html_ga62d9ea1d7dc2987101cf31b324ca7c51"></a>
<a id="agroup__regulator__interface_html_ga88c3ddeed962b5368713ad8fef0e7d7a"></a>
<a id="agroup__regulator__interface_html_ga8fb061502d0e94c4fe7a18c5a84d4af3"></a>
<a id="agroup__regulator__interface_html_ga9133662844a20eaf703d6d075347c62f"></a>
<a id="agroup__regulator__interface_html_ga96bf136ff2deca774931ca27300b03a6"></a>
<a id="agroup__regulator__interface_html_ga9a15a21a532e497713724f42052b1dbd"></a>
<a id="agroup__regulator__interface_html_ga9bc0fc7ba4bd2ed2548bff25cf4badfe"></a>
<a id="agroup__regulator__interface_html_gaa0114ee43a137ee98f98f5bce93d8579"></a>
<a id="agroup__regulator__interface_html_gaac417fbf6e30bbbfbd5ea5029a8ef298"></a>
<a id="agroup__regulator__interface_html_gad21aa12c6df397ee4f6591b8f6266763"></a>
<a id="agroup__regulator__interface_html_gad63e752a30ec12edc6a12e5d08c573dd"></a>
<a id="agroup__regulator__interface_html_gaf12002954c6fc0ab9689f4dd2ec39518"></a>
<a id="agroup__regulator__interface_html_ggad21aa12c6df397ee4f6591b8f6266763a27703e597bfb6cc290eeaac9442776a1"></a>
<a id="agroup__regulator__interface_html_ggad21aa12c6df397ee4f6591b8f6266763ab919a4157612a42cfff33616802c2e9b"></a>
<a id="agroup__regulator__parent__interface_html_ga980feabe8415a9643eb66c8566d700bf"></a>
<a id="agroup__regulator__parent__interface_html_gaa65d0a8d792256818a2ba06ad67a4f02"></a>
<a id="agroup__system__errno_html_ga03e689f378f643d16ea7537918528a48"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="akernel_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a181807730d4a375f848ba139813ce04f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a688eb21a22db27c2b2bd5836943cdcbe"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_aca2d801eb15996cf1c74dc65cfa651fc"></a>
<a id="astructregulator__driver__api_html"></a>
<a id="astructregulator__driver__api_html_a109db0dcdd1a68eaa134e721229e2056"></a>
<a id="astructregulator__driver__api_html_a4e4cd7fef63c83a705941109e63b67d0"></a>
<a id="astructregulator__driver__api_html_a518274ecff0d8721a3b883bc344151e6"></a>
<a id="astructregulator__driver__api_html_a67b1aeea6bfb4301972e87564a8656f6"></a>
<a id="astructregulator__driver__api_html_a7daeba7b79bc27d99bf30fb05ef056a0"></a>
<a id="astructregulator__driver__api_html_a85efb04e9271af38d8ed23a83202fccc"></a>
<a id="astructregulator__driver__api_html_a89613fef0b8adb6de371e8edc178442a"></a>
<a id="astructregulator__driver__api_html_a8a79e7f2e12e0b4d2da3511367f8aa30"></a>
<a id="astructregulator__driver__api_html_a9146d14c422bf5b6406b0e6b87b8df01"></a>
<a id="astructregulator__driver__api_html_a939d4cf6e496739e3b4ddc6eb1da4008"></a>
<a id="astructregulator__driver__api_html_a98796a09c441bf201e333452de21662f"></a>
<a id="astructregulator__driver__api_html_a9b696b7edb797460b7b3de1e9319c4e3"></a>
<a id="astructregulator__driver__api_html_abb3f66fa87c23a9508e1b7f693c2fd97"></a>
<a id="astructregulator__driver__api_html_ace034f3b7b9fe74dbcbb5d9ead0497d0"></a>
<a id="astructregulator__driver__api_html_adcb93913bceff8c766355a7d79217597"></a>
<a id="astructregulator__driver__api_html_afcc032c8173f75f789c65ccf517fdb28"></a>
<a id="astructregulator__event_html"></a>
<a id="astructregulator__event_html_ac2aeb7b44893bc89f217170e76cc11c7"></a>
<a id="astructregulator__parent__driver__api_html"></a>
<a id="astructregulator__parent__driver__api_html_a52f314a95ce64485240b1d3cc46dac05"></a>
<a id="astructregulator__parent__driver__api_html_aa0d54ca393956b0c6213217c678308a4"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2019-2020 Peter Bigot Consulting, LLC
 * Copyright (c) 2021 NXP
 * Copyright (c) 2022 Nordic Semiconductor ASA
 * Copyright (c) 2023 EPAM Systems
 * Copyright (c) 2023 Meta Platforms
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_REGULATOR_H_
#define ZEPHYR_INCLUDE_DRIVERS_REGULATOR_H_


#include <errno.h>
#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#ifdef CONFIG_REGULATOR_THREAD_SAFE_REFCNT
#include <zephyr/kernel.h>
#endif
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef uint8_t regulator_dvs_state_t;

typedef uint8_t regulator_mode_t;

typedef uint8_t regulator_error_flags_t;


#define REGULATOR_ERROR_OVER_VOLTAGE BIT(0)
#define REGULATOR_ERROR_OVER_CURRENT BIT(1)
#define REGULATOR_ERROR_OVER_TEMP    BIT(2)


enum regulator_event_type {
        REGULATOR_VOLTAGE_DETECTED,
        REGULATOR_VOLTAGE_REMOVED,
};

struct regulator_event {
        enum regulator_event_type type;
};

typedef void (*regulator_callback_t)(const struct device *dev,
                                     const struct regulator_event *const evt,
                                     const void *const user_data);


typedef int (*regulator_dvs_state_set_t)(const struct device *dev,
                                         regulator_dvs_state_t state);

typedef int (*regulator_ship_mode_t)(const struct device *dev);

__subsystem struct regulator_parent_driver_api {
        regulator_dvs_state_set_t dvs_state_set;
        regulator_ship_mode_t ship_mode;
};

typedef int (*regulator_enable_t)(const struct device *dev);

typedef int (*regulator_disable_t)(const struct device *dev);

typedef unsigned int (*regulator_count_voltages_t)(const struct device *dev);

typedef int (*regulator_list_voltage_t)(const struct device *dev,
                                        unsigned int idx, int32_t *volt_uv);

typedef int (*regulator_set_voltage_t)(const struct device *dev, int32_t min_uv,
                                       int32_t max_uv);

typedef int (*regulator_get_voltage_t)(const struct device *dev,
                                       int32_t *volt_uv);

typedef unsigned int (*regulator_count_current_limits_t)(const struct device *dev);

typedef int (*regulator_list_current_limit_t)(const struct device *dev,
                                              unsigned int idx, int32_t *current_ua);

typedef int (*regulator_set_current_limit_t)(const struct device *dev,
                                             int32_t min_ua, int32_t max_ua);

typedef int (*regulator_get_current_limit_t)(const struct device *dev,
                                             int32_t *curr_ua);

typedef int (*regulator_set_mode_t)(const struct device *dev,
                                    regulator_mode_t mode);

typedef int (*regulator_get_mode_t)(const struct device *dev,
                                    regulator_mode_t *mode);

typedef int (*regulator_set_active_discharge_t)(const struct device *dev,
                                    bool active_discharge);

typedef int (*regulator_get_active_discharge_t)(const struct device *dev,
                                    bool *active_discharge);

typedef int (*regulator_get_error_flags_t)(
        const struct device *dev, regulator_error_flags_t *flags);

typedef int (*regulator_set_callback_t)(const struct device *dev,
        regulator_callback_t cb, const void *const user_data);

__subsystem struct regulator_driver_api {
        regulator_enable_t enable;
        regulator_disable_t disable;
        regulator_count_voltages_t count_voltages;
        regulator_list_voltage_t list_voltage;
        regulator_set_voltage_t set_voltage;
        regulator_get_voltage_t get_voltage;
        regulator_count_current_limits_t count_current_limits;
        regulator_list_current_limit_t list_current_limit;
        regulator_set_current_limit_t set_current_limit;
        regulator_get_current_limit_t get_current_limit;
        regulator_set_mode_t set_mode;
        regulator_get_mode_t get_mode;
        regulator_set_active_discharge_t set_active_discharge;
        regulator_get_active_discharge_t get_active_discharge;
        regulator_get_error_flags_t get_error_flags;
        regulator_set_callback_t set_callback;
};



#define REGULATOR_ALWAYS_ON                BIT(0)
#define REGULATOR_BOOT_ON                  BIT(1)
#define REGULATOR_INIT_ENABLED             (REGULATOR_ALWAYS_ON | REGULATOR_BOOT_ON)
#define REGULATOR_ACTIVE_DISCHARGE_MASK    GENMASK(3, 2)
#define REGULATOR_ACTIVE_DISCHARGE_POS     2
#define REGULATOR_ACTIVE_DISCHARGE_DISABLE 0
#define REGULATOR_ACTIVE_DISCHARGE_ENABLE  1
#define REGULATOR_ACTIVE_DISCHARGE_DEFAULT 2
#define REGULATOR_ACTIVE_DISCHARGE_SET_BITS(x) \
        (((x) << REGULATOR_ACTIVE_DISCHARGE_POS) & REGULATOR_ACTIVE_DISCHARGE_MASK)
#define REGULATOR_ACTIVE_DISCHARGE_GET_BITS(x) \
        (((x) & REGULATOR_ACTIVE_DISCHARGE_MASK) >> REGULATOR_ACTIVE_DISCHARGE_POS)
#define REGULATOR_BOOT_OFF BIT(4)


#define REGULATOR_INITIAL_MODE_UNKNOWN UINT8_MAX

struct regulator_common_config {
        int32_t min_uv;
        int32_t max_uv;
        int32_t init_uv;
        int32_t min_ua;
        int32_t max_ua;
        int32_t init_ua;
        uint32_t startup_delay_us;
        uint32_t off_on_delay_us;
        const regulator_mode_t *allowed_modes;
        uint8_t allowed_modes_cnt;
        regulator_mode_t initial_mode;
        uint8_t flags;
};

#define REGULATOR_DT_COMMON_CONFIG_INIT(node_id)                               \
        {                                                                      \
                .min_uv = DT_PROP_OR(node_id, regulator_min_microvolt,         \
                                     INT32_MIN),                               \
                .max_uv = DT_PROP_OR(node_id, regulator_max_microvolt,         \
                                     INT32_MAX),                               \
                .init_uv = DT_PROP_OR(node_id, regulator_init_microvolt,       \
                                      INT32_MIN),                              \
                .min_ua = DT_PROP_OR(node_id, regulator_min_microamp,          \
                                     INT32_MIN),                               \
                .max_ua = DT_PROP_OR(node_id, regulator_max_microamp,          \
                                     INT32_MAX),                               \
                .init_ua = DT_PROP_OR(node_id, regulator_init_microamp,       \
                                      INT32_MIN),                              \
                .startup_delay_us = DT_PROP_OR(node_id, startup_delay_us, 0),  \
                .off_on_delay_us = DT_PROP_OR(node_id, off_on_delay_us, 0),    \
                .allowed_modes = (const regulator_mode_t [])                   \
                        DT_PROP_OR(node_id, regulator_allowed_modes, {}),      \
                .allowed_modes_cnt =                                           \
                        DT_PROP_LEN_OR(node_id, regulator_allowed_modes, 0),   \
                .initial_mode = DT_PROP_OR(node_id, regulator_initial_mode,    \
                                           REGULATOR_INITIAL_MODE_UNKNOWN),    \
                .flags = ((DT_PROP_OR(node_id, regulator_always_on, 0U) *      \
                           REGULATOR_ALWAYS_ON) |                              \
                          (DT_PROP_OR(node_id, regulator_boot_on, 0U) *        \
                           REGULATOR_BOOT_ON) |                                \
                          (REGULATOR_ACTIVE_DISCHARGE_SET_BITS(                \
                           DT_PROP_OR(node_id, regulator_active_discharge,     \
                           REGULATOR_ACTIVE_DISCHARGE_DEFAULT))) |             \
                          (DT_PROP_OR(node_id, regulator_boot_off, 0U) *       \
                           REGULATOR_BOOT_OFF)),                               \
        }

#define REGULATOR_DT_INST_COMMON_CONFIG_INIT(inst)                             \
        REGULATOR_DT_COMMON_CONFIG_INIT(DT_DRV_INST(inst))

struct regulator_common_data {
#if defined(CONFIG_REGULATOR_THREAD_SAFE_REFCNT) || defined(__DOXYGEN__)
        struct k_mutex lock;
#endif
        int refcnt;
};

void regulator_common_data_init(const struct device *dev);

int regulator_common_init(const struct device *dev, bool is_enabled);

static inline bool regulator_common_is_init_enabled(const struct device *dev)
{
        const struct regulator_common_config *config =
                (const struct regulator_common_config *)dev->config;

        return (config->flags & REGULATOR_INIT_ENABLED) != 0U;
}

static inline int regulator_common_get_min_voltage(const struct device *dev, int32_t *min_uv)
{
        const struct regulator_common_config *config =
                (const struct regulator_common_config *)dev->config;

        if (config->min_uv == INT32_MIN) {
                return -ENOENT;
        }

        *min_uv = config->min_uv;
        return 0;
}

static inline int regulator_common_get_max_voltage(const struct device *dev, int32_t *max_uv)
{
        const struct regulator_common_config *config =
                (const struct regulator_common_config *)dev->config;

        if (config->max_uv == INT32_MAX) {
                return -ENOENT;
        }

        *max_uv = config->max_uv;
        return 0;
}



static inline int regulator_parent_dvs_state_set(const struct device *dev,
                                                 regulator_dvs_state_t state)
{
        const struct regulator_parent_driver_api *api = DEVICE_API_GET(regulator_parent, dev);

        if (api->dvs_state_set == NULL) {
                return -ENOSYS;
        }

        return api->dvs_state_set(dev, state);
}

static inline int regulator_parent_ship_mode(const struct device *dev)
{
        const struct regulator_parent_driver_api *api = DEVICE_API_GET(regulator_parent, dev);

        if (api->ship_mode == NULL) {
                return -ENOSYS;
        }

        return api->ship_mode(dev);
}


int regulator_enable(const struct device *dev);

bool regulator_is_enabled(const struct device *dev);

int regulator_disable(const struct device *dev);

static inline unsigned int regulator_count_voltages(const struct device *dev)
{
        const struct regulator_driver_api *api = DEVICE_API_GET(regulator, dev);

        if (api->count_voltages == NULL) {
                return 0U;
        }

        return api->count_voltages(dev);
}

static inline int regulator_list_voltage(const struct device *dev,
                                         unsigned int idx, int32_t *volt_uv)
{
        const struct regulator_driver_api *api = DEVICE_API_GET(regulator, dev);

        if (api->list_voltage == NULL) {
                return -EINVAL;
        }

        return api->list_voltage(dev, idx, volt_uv);
}

bool regulator_is_supported_voltage(const struct device *dev, int32_t min_uv,
                                    int32_t max_uv);

int regulator_set_voltage(const struct device *dev, int32_t min_uv,
                          int32_t max_uv);

static inline int regulator_get_voltage(const struct device *dev,
                                        int32_t *volt_uv)
{
        const struct regulator_driver_api *api = DEVICE_API_GET(regulator, dev);

        if (api->get_voltage == NULL) {
                return -ENOSYS;
        }

        return api->get_voltage(dev, volt_uv);
}

static inline unsigned int regulator_count_current_limits(const struct device *dev)
{
        const struct regulator_driver_api *api = DEVICE_API_GET(regulator, dev);

        if (api->count_current_limits == NULL) {
                return 0U;
        }

        return api->count_current_limits(dev);
}

static inline int regulator_list_current_limit(const struct device *dev,
                                               unsigned int idx, int32_t *current_ua)
{
        const struct regulator_driver_api *api = DEVICE_API_GET(regulator, dev);

        if (api->list_current_limit == NULL) {
                return -EINVAL;
        }

        return api->list_current_limit(dev, idx, current_ua);
}

int regulator_set_current_limit(const struct device *dev, int32_t min_ua,
                                int32_t max_ua);

static inline int regulator_get_current_limit(const struct device *dev,
                                              int32_t *curr_ua)
{
        const struct regulator_driver_api *api = DEVICE_API_GET(regulator, dev);

        if (api->get_current_limit == NULL) {
                return -ENOSYS;
        }

        return api->get_current_limit(dev, curr_ua);
}

int regulator_set_mode(const struct device *dev, regulator_mode_t mode);

static inline int regulator_get_mode(const struct device *dev,
                                     regulator_mode_t *mode)
{
        const struct regulator_driver_api *api = DEVICE_API_GET(regulator, dev);

        if (api->get_mode == NULL) {
                return -ENOSYS;
        }

        return api->get_mode(dev, mode);
}

static inline int regulator_set_active_discharge(const struct device *dev,
                                     bool active_discharge)
{
        const struct regulator_driver_api *api = DEVICE_API_GET(regulator, dev);

        if (api->set_active_discharge == NULL) {
                return -ENOSYS;
        }

        return api->set_active_discharge(dev, active_discharge);
}

static inline int regulator_get_active_discharge(const struct device *dev,
                                     bool *active_discharge)
{
        const struct regulator_driver_api *api = DEVICE_API_GET(regulator, dev);

        if (api->get_active_discharge == NULL) {
                return -ENOSYS;
        }

        return api->get_active_discharge(dev, active_discharge);
}

static inline int regulator_get_error_flags(const struct device *dev,
                                            regulator_error_flags_t *flags)
{
        const struct regulator_driver_api *api = DEVICE_API_GET(regulator, dev);

        if (api->get_error_flags == NULL) {
                return -ENOSYS;
        }

        return api->get_error_flags(dev, flags);
}

static inline int regulator_set_callback(const struct device *dev,
                                         regulator_callback_t cb,
                                         const void *const user_data)
{
        const struct regulator_driver_api *api = DEVICE_API_GET(regulator, dev);

        if (api->set_callback == NULL) {
                return -ENOSYS;
        }

        return api->set_callback(dev, cb, user_data);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_REGULATOR_H_ */
```

## 701.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019-2020 Peter Bigot Consulting, LLC。

版权（Copyright）：© 2021 NXP。

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

版权（Copyright）：© 2023 EPAM Systems。

版权（Copyright）：© 2023 Meta Platforms。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 927 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_REGULATOR_H_`。

## 701.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../power/P082_稳压器头文件.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [regulator_dvs_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga9a15a21a532e497713724f42052b1dbd)
- [regulator_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga1971bd21b504979a0cecab16048a0d03)
- [regulator_error_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga31dae130509d28ee41602ab16ab31a90)
- [regulator_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#gad21aa12c6df397ee4f6591b8f6266763)
- [REGULATOR_VOLTAGE_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ggad21aa12c6df397ee4f6591b8f6266763a27703e597bfb6cc290eeaac9442776a1)
- [REGULATOR_VOLTAGE_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ggad21aa12c6df397ee4f6591b8f6266763ab919a4157612a42cfff33616802c2e9b)
- [regulator_event](../power/P080_稳压器事件结构.md)
- [type](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__event.html#ac2aeb7b44893bc89f217170e76cc11c7)
- [regulator_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga00b6235e23061028c45cf7160773677d)
- [device](../device_reference/P002_设备对象结构.md)
- [regulator_dvs_state_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#gada21d0f316c2717d497b4366adbe4cea)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [regulator_ship_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#gacbdbc2b57156375be8df792504fdc405)
- [regulator_parent_driver_api](../power/P079_父级稳压器驱动操作表.md)
- [dvs_state_set](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__parent__driver__api.html#a52f314a95ce64485240b1d3cc46dac05)
- [ship_mode](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__parent__driver__api.html#aa0d54ca393956b0c6213217c678308a4)
- [regulator_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#gadbfc2002a32b833e8eb115c8fa7e315f)
- [regulator_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#gadaadd2c07a557631a3dbebc609b6cccc)
- [regulator_count_voltages_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#gae3e867ce3ef2d819fb7f5ad9a22ccf39)
- [regulator_list_voltage_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#gaeeb7b0d0f864de9314ae0d5a11eb9a00)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [regulator_set_voltage_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#ga0c853ff39ff2917d88c10bd977628e1b)
- [regulator_get_voltage_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#gaadb2a63751a32597956553b6adad7fa7)
- [regulator_count_current_limits_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#ga80065f9f5047a6c2ef7e5d8ee24eb38f)
- [regulator_list_current_limit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#ga1ace8d15380b1fca67b548e3c2c0405c)
- [regulator_set_current_limit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#gac32c41a87d721bc1b40dc0d7227f6500)
- [regulator_get_current_limit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#ga43024f6b46b8848ef6e71de3371602d9)
- [regulator_set_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#gaa163eb9b3a1349d5041db5772b982dec)
- [regulator_get_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#ga4e89c959579f7ec7f0a6cba603c50c89)
- [regulator_set_active_discharge_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#ga3693adfe8e04fcf9bdce57ba01bc34b3)
- [regulator_get_active_discharge_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#ga04294f2fd8c407a1a02cd638ec16d45a)
- [regulator_get_error_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#ga91e98af520b227d40398b8650db333ae)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [regulator_set_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface__backend.html#gae7b3f6d6e0df901aeb0b8102482d3124)
- [regulator_driver_api](../power/P078_稳压器驱动操作表.md)
- [enable](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a518274ecff0d8721a3b883bc344151e6)
- [disable](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#ace034f3b7b9fe74dbcbb5d9ead0497d0)
- [count_voltages](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a7daeba7b79bc27d99bf30fb05ef056a0)
- [list_voltage](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a89613fef0b8adb6de371e8edc178442a)
- [set_voltage](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a67b1aeea6bfb4301972e87564a8656f6)
- [get_voltage](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#abb3f66fa87c23a9508e1b7f693c2fd97)
- [count_current_limits](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#afcc032c8173f75f789c65ccf517fdb28)
- [list_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a4e4cd7fef63c83a705941109e63b67d0)
- [set_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a109db0dcdd1a68eaa134e721229e2056)
- [get_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#adcb93913bceff8c766355a7d79217597)
- [set_mode](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a98796a09c441bf201e333452de21662f)
- [get_mode](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a9146d14c422bf5b6406b0e6b87b8df01)
- [set_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a8a79e7f2e12e0b4d2da3511367f8aa30)
- [get_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a9b696b7edb797460b7b3de1e9319c4e3)
- [get_error_flags](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a85efb04e9271af38d8ed23a83202fccc)
- [set_callback](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a939d4cf6e496739e3b4ddc6eb1da4008)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)
- [INT32_MIN](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a688eb21a22db27c2b2bd5836943cdcbe)
- [ENOENT](../error_reference/P003_系统错误号公共接口.md#ga03e689f378f643d16ea7537918528a48)
- [INT32_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a181807730d4a375f848ba139813ce04f)
- [regulator_parent_dvs_state_set](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__interface.html#ga980feabe8415a9643eb66c8566d700bf)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [regulator_parent_ship_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__parent__interface.html#gaa65d0a8d792256818a2ba06ad67a4f02)
- [regulator_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga06e3109b9607521fe07686c6d601e460)
- [regulator_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga28744a6cabadfe5a22bc96792c8ad124)
- [regulator_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#gaac417fbf6e30bbbfbd5ea5029a8ef298)
- [regulator_count_voltages](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga96bf136ff2deca774931ca27300b03a6)
- [regulator_list_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga62d9ea1d7dc2987101cf31b324ca7c51)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [regulator_is_supported_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga31b42ddfe94fee47158632f355ad864c)
- [regulator_set_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga2c2b345da9029013edbf59fd8c565d85)
- [regulator_get_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#gaa0114ee43a137ee98f98f5bce93d8579)
- [regulator_count_current_limits](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga27de51302b5222f860457c5b8bd494d6)
- [regulator_list_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#gaf12002954c6fc0ab9689f4dd2ec39518)
- [regulator_set_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga2ccf66175b37754e2c21f341ecb2acbd)
- [regulator_get_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga88c3ddeed962b5368713ad8fef0e7d7a)
- [regulator_set_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga1877bac62c2b81ee37deb86bfae302af)
- [regulator_get_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga9bc0fc7ba4bd2ed2548bff25cf4badfe)
- [regulator_set_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga8fb061502d0e94c4fe7a18c5a84d4af3)
- [regulator_get_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga58d9e06c6da52a9733b3979d72915ab3)
- [regulator_get_error_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#ga9133662844a20eaf703d6d075347c62f)
- [regulator_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__regulator__interface.html#gad63e752a30ec12edc6a12e5d08c573dd)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [device::config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)
- [regulator_driver_api::set_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a109db0dcdd1a68eaa134e721229e2056)
- [regulator_driver_api::list_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a4e4cd7fef63c83a705941109e63b67d0)
- [regulator_driver_api::enable](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a518274ecff0d8721a3b883bc344151e6)
- [regulator_driver_api::set_voltage](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a67b1aeea6bfb4301972e87564a8656f6)
- [regulator_driver_api::count_voltages](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a7daeba7b79bc27d99bf30fb05ef056a0)
- [regulator_driver_api::get_error_flags](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a85efb04e9271af38d8ed23a83202fccc)
- [regulator_driver_api::list_voltage](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a89613fef0b8adb6de371e8edc178442a)
- [regulator_driver_api::set_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a8a79e7f2e12e0b4d2da3511367f8aa30)
- [regulator_driver_api::get_mode](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a9146d14c422bf5b6406b0e6b87b8df01)
- [regulator_driver_api::set_callback](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a939d4cf6e496739e3b4ddc6eb1da4008)
- [regulator_driver_api::set_mode](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a98796a09c441bf201e333452de21662f)
- [regulator_driver_api::get_active_discharge](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#a9b696b7edb797460b7b3de1e9319c4e3)
- [regulator_driver_api::get_voltage](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#abb3f66fa87c23a9508e1b7f693c2fd97)
- [regulator_driver_api::disable](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#ace034f3b7b9fe74dbcbb5d9ead0497d0)
- [regulator_driver_api::get_current_limit](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#adcb93913bceff8c766355a7d79217597)
- [regulator_driver_api::count_current_limits](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__driver__api.html#afcc032c8173f75f789c65ccf517fdb28)
- [regulator_event::type](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__event.html#ac2aeb7b44893bc89f217170e76cc11c7)
- [regulator_parent_driver_api::dvs_state_set](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__parent__driver__api.html#a52f314a95ce64485240b1d3cc46dac05)
- [regulator_parent_driver_api::ship_mode](https://docs.zephyrproject.org/latest/doxygen/html/structregulator__parent__driver__api.html#aa0d54ca393956b0c6213217c678308a4)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P700_regset_target_lib.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P702_renesas-rtk0eg0019b01002bj.h_源码浏览.md)
