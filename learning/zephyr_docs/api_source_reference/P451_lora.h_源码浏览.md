---
id: learning.zephyr-docs.api-source-reference.page-451
title: lora.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lora_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第451章\_lora.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lora_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lora_8h.html)。

## 451.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="foldopen00040"></a>
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
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="foldopen00099"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="foldopen00133"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="foldopen00227"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00280"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00306"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="foldopen00441"></a>
<a id="l00441"></a>
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
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00471"></a>
<a id="foldopen00482"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="foldopen00499"></a>
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
<a id="foldopen00520"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="foldopen00537"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="foldopen00559"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="foldopen00582"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="foldopen00604"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="foldopen00626"></a>
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
<a id="foldopen00651"></a>
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
<a id="foldopen00680"></a>
<a id="l00680"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="l00714"></a>
<a id="l00715"></a>
<a id="foldopen00738"></a>
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
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00753"></a>
<a id="l00754"></a>
<a id="foldopen00773"></a>
<a id="l00773"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00781"></a>
<a id="l00782"></a>
<a id="l00783"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="foldopen00799"></a>
<a id="l00799"></a>
<a id="l00800"></a>
<a id="l00801"></a>
<a id="l00802"></a>
<a id="l00803"></a>
<a id="l00804"></a>
<a id="l00805"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00809"></a>
<a id="l00810"></a>
<a id="l00811"></a>
<a id="l00812"></a>
<a id="l00813"></a>
<a id="l00814"></a>
<a id="l00818"></a>
<a id="l00819"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__lora__interface__backend_html_ga02edec1bd6925622926b3fc8833c8bec"></a>
<a id="agroup__lora__interface__backend_html_ga166896d4f655cc2630e5951b1ad45c01"></a>
<a id="agroup__lora__interface__backend_html_ga185dba9fc898f2c9407b9a9461695b8e"></a>
<a id="agroup__lora__interface__backend_html_ga1dafc39726315c7921d7dd6b1e0caac4"></a>
<a id="agroup__lora__interface__backend_html_ga604500a11fa03edae97862c29b233ed1"></a>
<a id="agroup__lora__interface__backend_html_ga73606f1fdbea0b408315b9cbb28a4e19"></a>
<a id="agroup__lora__interface__backend_html_ga796b75a4b27b9331d78f1916e36ea1d2"></a>
<a id="agroup__lora__interface__backend_html_ga7fd50273b9463b602a4f457129d5c17f"></a>
<a id="agroup__lora__interface__backend_html_ga8993b902d31eac8870eb3a7f27a255cd"></a>
<a id="agroup__lora__interface__backend_html_ga8ad83577ede3ca3c7d4b037c95e039e3"></a>
<a id="agroup__lora__interface__backend_html_gabc8cba7c3f81961eac289adc40d3c8e1"></a>
<a id="agroup__lora__interface__backend_html_gad3bac89281cbf6cc79f2f4df6f4b4329"></a>
<a id="agroup__lora__interface__backend_html_gaddff151212a432c1dbf00c3665033eb0"></a>
<a id="agroup__lora__interface__backend_html_gaf308b8431762462eb172f4e0bdfce99f"></a>
<a id="agroup__lora__interface__backend_html_gafac86253dce5dbe9286683f565663971"></a>
<a id="agroup__lora__interface_html_ga0b6af528164f65b590295882590e7c7f"></a>
<a id="agroup__lora__interface_html_ga2192d812e6203f6361b8beaeb1d7361c"></a>
<a id="agroup__lora__interface_html_ga22c381e69be5cc630e283e8f5dfa940a"></a>
<a id="agroup__lora__interface_html_ga27d78168c737d56f9f7f3bbdacb808fb"></a>
<a id="agroup__lora__interface_html_ga28005c24ab1c13eb311bc05c3454a8f6"></a>
<a id="agroup__lora__interface_html_ga30bfeb2e6f4e35869996b597b614becb"></a>
<a id="agroup__lora__interface_html_ga35e79551b8cdb160e74d3759a76f2db4"></a>
<a id="agroup__lora__interface_html_ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b"></a>
<a id="agroup__lora__interface_html_ga497bf93cfe42ce6a6d48a4b463b52c21"></a>
<a id="agroup__lora__interface_html_ga5af378491814d0d3a059cd6cd39265c8"></a>
<a id="agroup__lora__interface_html_ga5d1802eed6067734ca45c70e3114b272"></a>
<a id="agroup__lora__interface_html_ga6b74d80debd5a629af29aedc7b174118"></a>
<a id="agroup__lora__interface_html_ga75d2c701f482d35cfbdd94906b8799c9"></a>
<a id="agroup__lora__interface_html_gabb5feb9d1a2bb160d9b55939efb17136"></a>
<a id="agroup__lora__interface_html_gac5db659ac5d4ce04dc3d2e69c1ecea22"></a>
<a id="agroup__lora__interface_html_gacf4c29b613fc525cfdc0b961c39981b4"></a>
<a id="agroup__lora__interface_html_gad893b49a74e350bb05f42f863af31446"></a>
<a id="agroup__lora__interface_html_gad99239be6aeda56b859ca571514806b9"></a>
<a id="agroup__lora__interface_html_gaedf7847838b1e2b83bde8fc7bf735cf6"></a>
<a id="agroup__lora__interface_html_gaf0419dcdf8ec56d9e1bfaaa35c1533c4"></a>
<a id="agroup__lora__interface_html_gafeae6fa9d81508023665705bf16b6435"></a>
<a id="agroup__lora__interface_html_gga0b6af528164f65b590295882590e7c7fa22aea3f5c73603f35bd51cbbbafd6590"></a>
<a id="agroup__lora__interface_html_gga0b6af528164f65b590295882590e7c7fa603d0a74c25b399add7f77cdc58aaa36"></a>
<a id="agroup__lora__interface_html_gga0b6af528164f65b590295882590e7c7fa926ae987d41f1452b6b0d719b87d3a48"></a>
<a id="agroup__lora__interface_html_gga0b6af528164f65b590295882590e7c7fa926e49c1ff792223c18d7df2ebf540df"></a>
<a id="agroup__lora__interface_html_gga0b6af528164f65b590295882590e7c7fa944e8a714e86128d6eddf190a7968337"></a>
<a id="agroup__lora__interface_html_gga22c381e69be5cc630e283e8f5dfa940aa2351cc0d7d91be6c59ad8dfa24cdb834"></a>
<a id="agroup__lora__interface_html_gga22c381e69be5cc630e283e8f5dfa940aaab23feb65836b44af2684a5ae920abbd"></a>
<a id="agroup__lora__interface_html_gga22c381e69be5cc630e283e8f5dfa940aabe60002b7a1a80111d380cd34a7afb80"></a>
<a id="agroup__lora__interface_html_gga30bfeb2e6f4e35869996b597b614becba88305a6b5aedf285c153266b13f94a73"></a>
<a id="agroup__lora__interface_html_gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958"></a>
<a id="agroup__lora__interface_html_gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e"></a>
<a id="agroup__lora__interface_html_gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407"></a>
<a id="agroup__lora__interface_html_gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6"></a>
<a id="agroup__lora__interface_html_gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc"></a>
<a id="agroup__lora__interface_html_gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d"></a>
<a id="agroup__lora__interface_html_gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608"></a>
<a id="agroup__lora__interface_html_gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18"></a>
<a id="agroup__lora__interface_html_gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e"></a>
<a id="agroup__lora__interface_html_gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42"></a>
<a id="agroup__lora__interface_html_gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943"></a>
<a id="agroup__lora__interface_html_gga6b74d80debd5a629af29aedc7b174118a150063c466edc7c5646608bdc0420bd6"></a>
<a id="agroup__lora__interface_html_gga6b74d80debd5a629af29aedc7b174118a3178ad418e312e33a7375407b3e6e834"></a>
<a id="agroup__lora__interface_html_gga6b74d80debd5a629af29aedc7b174118a39352f92f030e4eccffe6c772fe0b47f"></a>
<a id="agroup__lora__interface_html_gga6b74d80debd5a629af29aedc7b174118a777fcfa7786fded4d242c4bd85496586"></a>
<a id="agroup__lora__interface_html_gga6b74d80debd5a629af29aedc7b174118aefd2af106e02a78d3b1c6e6b410b91b8"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136a0ba99c3fe74214f3b58ad36c0b27213f"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136a1857aa53428a54c025f7af8addd92bf5"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136a316c5c1a9b09dda806ab803753f3bd6f"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136a7db7146160c9d714c9ecb1b57671b43f"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136a83d98f1ab54b76c438b411d8de561aef"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136a85ebe31f96c03865427027ba1b9fc1de"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136ab8bc5b1003950a7129df125eaa5231dc"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136abc146b2fff61f782b2cb22c54113e46d"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136ae1aaba3f8e379b7cbdd8fd44b63e5ca5"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136af3b5a702fd61a6c4b393a4b612064ad4"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136af3d00abffcee270d17533c78b26490d4"></a>
<a id="agroup__lora__interface_html_ggabb5feb9d1a2bb160d9b55939efb17136afdf65a32c9d8eeee1345a455e057fcc6"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructk__poll__signal_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructlora__driver__api_html"></a>
<a id="astructlora__driver__api_html_a1e2d0208c52e6fe0ec6c51484537f033"></a>
<a id="astructlora__driver__api_html_a255ba5321ad6423de1b613b2c3520334"></a>
<a id="astructlora__driver__api_html_a30296d89ea10356fd1ded3dcbcae7618"></a>
<a id="astructlora__driver__api_html_a83a2e31b05a17ddf82de6bb6e55c1381"></a>
<a id="astructlora__driver__api_html_a8c579d89e40f1b9374711d5d3bef148b"></a>
<a id="astructlora__driver__api_html_a98fc632a4e30079bc08b94b9d5dbbb1c"></a>
<a id="astructlora__driver__api_html_aa2b7d4975ed91b4c0898842aa9e271fd"></a>
<a id="astructlora__driver__api_html_aa8600981dbaa6eaf35da02fb586828ab"></a>
<a id="astructlora__driver__api_html_ab5ac6d906cc2429f065d720e3af1ceaf"></a>
<a id="astructlora__driver__api_html_ad37a8cdd8801b9c0036259dde6bc1a93"></a>
<a id="astructlora__driver__api_html_ad582af08f38b4c2fc83588e7108bef6b"></a>
<a id="astructlora__driver__api_html_ae5fc4c8418225f44a220b6b4d223f114"></a>
<a id="astructlora__driver__api_html_afc1eb7fabc1e59b224317ddd912f4d77"></a>
<a id="astructlora__modem__config__gfsk_html"></a>
<a id="astructlora__modem__config__gfsk_html_a24e0dd59c6b63672c546a52a54066186"></a>
<a id="astructlora__modem__config__gfsk_html_a2868bdf2650e0e1082bac10357d8ab67"></a>
<a id="astructlora__modem__config__gfsk_html_a2a8b2df70532bb82920431e2e013b5b0"></a>
<a id="astructlora__modem__config__gfsk_html_a5ae2b2c3e7e12db26a7ebc95b8146dcd"></a>
<a id="astructlora__modem__config__gfsk_html_a5c6b50a264eef09a4198e2116908f8b8"></a>
<a id="astructlora__modem__config__gfsk_html_a93b6c16da78ca973ba20549bc5ca833e"></a>
<a id="astructlora__modem__config__gfsk_html_a9b816ff8b4f215761399b5f7cd3b9f1e"></a>
<a id="astructlora__modem__config__gfsk_html_a9dd764760623f5ee04ea608cbc180c00"></a>
<a id="astructlora__modem__config__gfsk_html_a9fdc015f243dfe7bae02c69ae4028258"></a>
<a id="astructlora__modem__config__gfsk_html_aadc6d35654c3158932080d4e7b5b5f9f"></a>
<a id="astructlora__modem__config__gfsk_html_ab290c324797465c551e903df15a8eee3"></a>
<a id="astructlora__modem__config__gfsk_html_ad5ba923fe733374b23e1e67918d1fc5a"></a>
<a id="astructlora__modem__config__gfsk_html_aee3775468ec73b8cfa8347996a897445"></a>
<a id="astructlora__modem__config__gfsk_html_afd0fe3012874bfb460283dbd6cba0a72"></a>
<a id="astructlora__modem__config_html"></a>
<a id="astructlora__modem__config_html_a05681aa7e1423be4b0582164bc1b02a6"></a>
<a id="astructlora__modem__config_html_a08209a2dabc5111025810fc8e141c2df"></a>
<a id="astructlora__modem__config_html_a0c6a90e31b4a97d962af3dbd0ee8e885"></a>
<a id="astructlora__modem__config_html_a10b12a2092712050bdd64c6250c8731f"></a>
<a id="astructlora__modem__config_html_a3c9f32935f253df5e1ee67c5aab7795c"></a>
<a id="astructlora__modem__config_html_a41a194d62e1e3e1b142e194a75efb8a1"></a>
<a id="astructlora__modem__config_html_a43d01b02bfc4e1a801ea04aa3d0f0518"></a>
<a id="astructlora__modem__config_html_a5737749b3bd29515887bb0b8c48c8bd1"></a>
<a id="astructlora__modem__config_html_a8e47a8506265562c7b118fab72cceb10"></a>
<a id="astructlora__modem__config_html_a9d0795c5be6ae0042babaa05615cf7f2"></a>
<a id="astructlora__modem__config_html_ad12a48ff7aaa815a34e888aff839c389"></a>
<a id="astructlora__modem__config_html_adc1f228bbba786608fbb66df2b34aa51"></a>
<a id="astructlora__modem__config_html_ae438c1c223f12fc6c3747d4297ec61ba"></a>
<a id="astructlora__modem__config_html_ae9442b595916150367086e93e833aa68"></a>
<a id="astructlora__modem__config_html_af5ef0c5e3443a011d2ed6af3c95cc4db"></a>
<a id="astructlora__modem__config_html_af97fde1f5f40a4d702c0140872728e86"></a>

```c
/*
 * Copyright (c) 2019 Manivannan Sadhasivam
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_LORA_H_
#define ZEPHYR_INCLUDE_DRIVERS_LORA_H_


#include <stdint.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

enum lora_signal_bandwidth {
        BW_7_KHZ = 7,
        BW_10_KHZ = 10,
        BW_15_KHZ = 15,
        BW_20_KHZ = 20,
        BW_31_KHZ = 31,
        BW_41_KHZ = 41,
        BW_62_KHZ = 62,
        BW_125_KHZ = 125,
        BW_200_KHZ = 200,
        BW_250_KHZ = 250,
        BW_400_KHZ = 400,
        BW_500_KHZ = 500,
        BW_800_KHZ = 800,
        BW_1000_KHZ = 1000,
        BW_1600_KHZ = 1600,
};

enum lora_datarate {
        SF_5 = 5,
        SF_6 = 6,
        SF_7 = 7,
        SF_8 = 8,
        SF_9 = 9,
        SF_10 = 10,
        SF_11 = 11,
        SF_12 = 12,
};

enum lora_coding_rate {
        CR_4_5 = 1,
        CR_4_6 = 2,
        CR_4_7 = 3,
        CR_4_8 = 4,
};

enum lora_cad_symbol_num {
        LORA_CAD_SYMB_1 = 1,
        LORA_CAD_SYMB_2 = 2,
        LORA_CAD_SYMB_4 = 4,
        LORA_CAD_SYMB_8 = 8,
        LORA_CAD_SYMB_16 = 16,
};

enum lora_cad_mode {
        LORA_CAD_MODE_NONE = 0,

        LORA_CAD_MODE_RX,

        LORA_CAD_MODE_LBT,
};

enum lora_gfsk_pulse_shape {
        LORA_GFSK_PULSE_SHAPE_NONE,
        LORA_GFSK_PULSE_SHAPE_BT_0_3,
        LORA_GFSK_PULSE_SHAPE_BT_0_5,
        LORA_GFSK_PULSE_SHAPE_BT_0_7,
        LORA_GFSK_PULSE_SHAPE_BT_1_0,
};

#define LORA_GFSK_SYNC_WORD_MAX 8

#define LORA_GFSK_PREAMBLE_MAX (UINT16_MAX / BITS_PER_BYTE)

struct lora_modem_config_gfsk {
        uint32_t frequency;

        uint32_t bitrate;

        uint32_t freq_deviation;

        uint32_t bandwidth;

        enum lora_gfsk_pulse_shape pulse_shape;

        uint8_t sync_word[LORA_GFSK_SYNC_WORD_MAX];

        uint8_t sync_word_len;

        uint16_t preamble_len;

        int8_t tx_power;

        bool tx;

        bool whitening;

        bool fixed_len;

        uint8_t payload_len;

        bool packet_crc_disable;
};

struct lora_modem_config {
        uint32_t frequency;

        enum lora_signal_bandwidth bandwidth;

        enum lora_datarate datarate;

        enum lora_coding_rate coding_rate;

        uint16_t preamble_len;

        int8_t tx_power;

        uint8_t sync_word;

        bool tx;

        bool iq_inverted;

        bool public_network;

        bool packet_crc_disable;

        struct {
                enum lora_cad_mode mode;

                enum lora_cad_symbol_num symbol_num;

                uint8_t detection_peak;

                uint8_t detection_minimum;
        } cad;
};


typedef void (*lora_recv_cb)(const struct device *dev, uint8_t *data, uint16_t size,
                             int16_t rssi, int8_t snr, void *user_data);

typedef void (*lora_cad_cb)(const struct device *dev, bool activity_detected,
                            void *user_data);

typedef int (*lora_api_config)(const struct device *dev,
                               const struct lora_modem_config *config);

typedef int (*lora_api_config_gfsk)(const struct device *dev,
                                    const struct lora_modem_config_gfsk *config);

typedef uint32_t (*lora_api_airtime)(const struct device *dev, uint32_t data_len);

typedef int (*lora_api_send)(const struct device *dev,
                             uint8_t *data, uint32_t data_len);

typedef int (*lora_api_send_async)(const struct device *dev,
                                   uint8_t *data, uint32_t data_len,
                                   struct k_poll_signal *async);

typedef int (*lora_api_recv)(const struct device *dev, uint8_t *data,
                             uint8_t size,
                             k_timeout_t timeout, int16_t *rssi, int8_t *snr);

typedef int (*lora_api_recv_async)(const struct device *dev, lora_recv_cb cb,
                             void *user_data);

typedef int (*lora_api_cad)(const struct device *dev, k_timeout_t timeout);

typedef int (*lora_api_cad_async)(const struct device *dev, lora_cad_cb cb,
                                  void *user_data);

typedef int (*lora_api_rssi)(const struct device *dev, int16_t *rssi);

typedef int (*lora_api_recv_duty_cycle)(const struct device *dev,
                                        k_timeout_t rx_period,
                                        k_timeout_t sleep_period,
                                        uint8_t *data, uint8_t size,
                                        k_timeout_t timeout,
                                        int16_t *rssi, int8_t *snr);

typedef int (*lora_api_recv_duty_cycle_async)(const struct device *dev,
                                              k_timeout_t rx_period,
                                              k_timeout_t sleep_period,
                                              lora_recv_cb cb, void *user_data);

typedef int (*lora_api_test_cw)(const struct device *dev, uint32_t frequency,
                                int8_t tx_power, uint16_t duration);

__subsystem struct lora_driver_api {
        lora_api_config config;
        lora_api_config_gfsk config_gfsk;
        lora_api_airtime airtime;
        lora_api_send send;
        lora_api_send_async send_async;
        lora_api_recv recv;
        lora_api_recv_async recv_async;
        lora_api_cad cad;
        lora_api_cad_async cad_async;
        lora_api_rssi rssi;
        lora_api_recv_duty_cycle_async recv_duty_cycle_async;
        lora_api_recv_duty_cycle recv_duty_cycle;
        lora_api_test_cw test_cw;
};


static inline int lora_config(const struct device *dev,
                              const struct lora_modem_config *config)
{
        return DEVICE_API_GET(lora, dev)->config(dev, config);
}

static inline int lora_config_gfsk(const struct device *dev,
                                   const struct lora_modem_config_gfsk *config)
{
        const struct lora_driver_api *api = DEVICE_API_GET(lora, dev);

        if (api->config_gfsk == NULL) {
                return -ENOSYS;
        }

        return api->config_gfsk(dev, config);
}

static inline uint32_t lora_airtime(const struct device *dev, uint32_t data_len)
{
        return DEVICE_API_GET(lora, dev)->airtime(dev, data_len);
}

static inline int lora_send(const struct device *dev,
                            uint8_t *data, uint32_t data_len)
{
        return DEVICE_API_GET(lora, dev)->send(dev, data, data_len);
}

static inline int lora_send_async(const struct device *dev,
                                  uint8_t *data, uint32_t data_len,
                                  struct k_poll_signal *async)
{
        return DEVICE_API_GET(lora, dev)->send_async(dev, data, data_len, async);
}

static inline int lora_recv(const struct device *dev, uint8_t *data,
                            uint8_t size,
                            k_timeout_t timeout, int16_t *rssi, int8_t *snr)
{
        return DEVICE_API_GET(lora, dev)->recv(dev, data, size, timeout, rssi, snr);
}

static inline int lora_recv_async(const struct device *dev, lora_recv_cb cb,
                               void *user_data)
{
        return DEVICE_API_GET(lora, dev)->recv_async(dev, cb, user_data);
}

static inline int lora_cad(const struct device *dev, k_timeout_t timeout)
{
        const struct lora_driver_api *api = DEVICE_API_GET(lora, dev);

        if (api->cad == NULL) {
                return -ENOSYS;
        }

        return api->cad(dev, timeout);
}

static inline int lora_cad_async(const struct device *dev, lora_cad_cb cb,
                                 void *user_data)
{
        const struct lora_driver_api *api = DEVICE_API_GET(lora, dev);

        if (api->cad_async == NULL) {
                return -ENOSYS;
        }

        return api->cad_async(dev, cb, user_data);
}

static inline int lora_rssi(const struct device *dev, int16_t *rssi)
{
        const struct lora_driver_api *api = DEVICE_API_GET(lora, dev);

        if (api->rssi == NULL) {
                return -ENOSYS;
        }

        return api->rssi(dev, rssi);
}

int lora_energy_detect(const struct device *dev, int16_t rssi_threshold, k_timeout_t duration);

static inline int lora_recv_duty_cycle(const struct device *dev,
                                       k_timeout_t rx_period,
                                       k_timeout_t sleep_period,
                                       uint8_t *data, uint8_t size,
                                       k_timeout_t timeout,
                                       int16_t *rssi, int8_t *snr)
{
        const struct lora_driver_api *api = DEVICE_API_GET(lora, dev);

        if (api->recv_duty_cycle == NULL) {
                return -ENOSYS;
        }

        return api->recv_duty_cycle(dev, rx_period, sleep_period,
                                    data, size, timeout, rssi, snr);
}

static inline int lora_recv_duty_cycle_async(const struct device *dev,
                                             k_timeout_t rx_period,
                                             k_timeout_t sleep_period,
                                             lora_recv_cb cb, void *user_data)
{
        const struct lora_driver_api *api = DEVICE_API_GET(lora, dev);

        if (api->recv_duty_cycle_async == NULL) {
                return -ENOSYS;
        }

        return api->recv_duty_cycle_async(dev, rx_period, sleep_period, cb, user_data);
}

static inline int lora_test_cw(const struct device *dev, uint32_t frequency,
                               int8_t tx_power, uint16_t duration)
{
        const struct lora_driver_api *api = DEVICE_API_GET(lora, dev);

        if (api->test_cw == NULL) {
                return -ENOSYS;
        }

        return api->test_cw(dev, frequency, tx_power, duration);
}

#ifdef __cplusplus
}
#endif


#endif  /* ZEPHYR_INCLUDE_DRIVERS_LORA_H_ */
```

## 451.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Manivannan Sadhasivam。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 819 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_LORA_H_`。

## 451.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lora_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [lora_signal_bandwidth](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gabb5feb9d1a2bb160d9b55939efb17136)
- [BW_7_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136abc146b2fff61f782b2cb22c54113e46d)
- [BW_10_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a1857aa53428a54c025f7af8addd92bf5)
- [BW_15_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136af3b5a702fd61a6c4b393a4b612064ad4)
- [BW_20_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136af3d00abffcee270d17533c78b26490d4)
- [BW_31_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a316c5c1a9b09dda806ab803753f3bd6f)
- [BW_41_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a85ebe31f96c03865427027ba1b9fc1de)
- [BW_62_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136ab8bc5b1003950a7129df125eaa5231dc)
- [BW_125_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a7063f98723dcd69d0ed77ed170de33b1)
- [BW_200_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a0ba99c3fe74214f3b58ad36c0b27213f)
- [BW_250_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a0ff445d6d4eb5a739066846266b54411)
- [BW_400_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a7db7146160c9d714c9ecb1b57671b43f)
- [BW_500_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136aa9eaeb7000fef12712d0a9b8a6f52cd9)
- [BW_800_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136a83d98f1ab54b76c438b411d8de561aef)
- [BW_1000_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136afdf65a32c9d8eeee1345a455e057fcc6)
- [BW_1600_KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ggabb5feb9d1a2bb160d9b55939efb17136ae1aaba3f8e379b7cbdd8fd44b63e5ca5)
- [lora_datarate](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga30bfeb2e6f4e35869996b597b614becb)
- [SF_5](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becba88305a6b5aedf285c153266b13f94a73)
- [SF_6](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbadc160c3873902e6a7ff18f29609a581d)
- [SF_7](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbafc25fa7076b5bcdaf238050e3dd79608)
- [SF_8](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbaa60158fdc7a0a26f11c23ffbf08dd46e)
- [SF_9](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbacf92fc5af2cf440e944c36c1e5b19fbc)
- [SF_10](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbac96090aac549ab1ae88b701c8ac866f6)
- [SF_11](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becbab87b9b8222f9a4daff607c88d436b407)
- [SF_12](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga30bfeb2e6f4e35869996b597b614becba9d6cac0c0efcb738149456d143bc6958)
- [lora_coding_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga5af378491814d0d3a059cd6cd39265c8)
- [CR_4_5](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga5af378491814d0d3a059cd6cd39265c8a43f3ee8c5a099f26a2b1e74ab80b5d18)
- [CR_4_6](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga5af378491814d0d3a059cd6cd39265c8a63e7039c12c59913fe195a9cda8e842e)
- [CR_4_7](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga5af378491814d0d3a059cd6cd39265c8afaec525569c1f205b98228986604a943)
- [CR_4_8](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga5af378491814d0d3a059cd6cd39265c8ad79275b6ea8d47cac828b698617afe42)
- [lora_cad_symbol_num](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga0b6af528164f65b590295882590e7c7f)
- [LORA_CAD_SYMB_1](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa944e8a714e86128d6eddf190a7968337)
- [LORA_CAD_SYMB_2](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa926ae987d41f1452b6b0d719b87d3a48)
- [LORA_CAD_SYMB_4](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa926e49c1ff792223c18d7df2ebf540df)
- [LORA_CAD_SYMB_8](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa22aea3f5c73603f35bd51cbbbafd6590)
- [LORA_CAD_SYMB_16](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga0b6af528164f65b590295882590e7c7fa603d0a74c25b399add7f77cdc58aaa36)
- [lora_cad_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga22c381e69be5cc630e283e8f5dfa940a)
- [LORA_CAD_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga22c381e69be5cc630e283e8f5dfa940aaab23feb65836b44af2684a5ae920abbd)
- [LORA_CAD_MODE_RX](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga22c381e69be5cc630e283e8f5dfa940aa2351cc0d7d91be6c59ad8dfa24cdb834)
- [LORA_CAD_MODE_LBT](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga22c381e69be5cc630e283e8f5dfa940aabe60002b7a1a80111d380cd34a7afb80)
- [lora_gfsk_pulse_shape](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga6b74d80debd5a629af29aedc7b174118)
- [LORA_GFSK_PULSE_SHAPE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118aefd2af106e02a78d3b1c6e6b410b91b8)
- [LORA_GFSK_PULSE_SHAPE_BT_0_3](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118a3178ad418e312e33a7375407b3e6e834)
- [LORA_GFSK_PULSE_SHAPE_BT_0_5](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118a150063c466edc7c5646608bdc0420bd6)
- [LORA_GFSK_PULSE_SHAPE_BT_0_7](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118a39352f92f030e4eccffe6c772fe0b47f)
- [LORA_GFSK_PULSE_SHAPE_BT_1_0](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gga6b74d80debd5a629af29aedc7b174118a777fcfa7786fded4d242c4bd85496586)
- [lora_modem_config_gfsk](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [frequency](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a9dd764760623f5ee04ea608cbc180c00)
- [bitrate](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a24e0dd59c6b63672c546a52a54066186)
- [freq_deviation](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a2a8b2df70532bb82920431e2e013b5b0)
- [bandwidth](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a9fdc015f243dfe7bae02c69ae4028258)
- [pulse_shape](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#ab290c324797465c551e903df15a8eee3)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sync_word](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#aee3775468ec73b8cfa8347996a897445)
- [LORA_GFSK_SYNC_WORD_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gaf0419dcdf8ec56d9e1bfaaa35c1533c4)
- [sync_word_len](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a5c6b50a264eef09a4198e2116908f8b8)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [preamble_len](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a9b816ff8b4f215761399b5f7cd3b9f1e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [tx_power](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#aadc6d35654c3158932080d4e7b5b5f9f)
- [tx](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a93b6c16da78ca973ba20549bc5ca833e)
- [whitening](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a2868bdf2650e0e1082bac10357d8ab67)
- [fixed_len](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#afd0fe3012874bfb460283dbd6cba0a72)
- [payload_len](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a5ae2b2c3e7e12db26a7ebc95b8146dcd)
- [packet_crc_disable](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#ad5ba923fe733374b23e1e67918d1fc5a)
- [lora_modem_config](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md)
- [frequency](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a08209a2dabc5111025810fc8e141c2df)
- [bandwidth](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a0c6a90e31b4a97d962af3dbd0ee8e885)
- [datarate](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#ae438c1c223f12fc6c3747d4297ec61ba)
- [coding_rate](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a8e47a8506265562c7b118fab72cceb10)
- [preamble_len](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a9d0795c5be6ae0042babaa05615cf7f2)
- [tx_power](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a41a194d62e1e3e1b142e194a75efb8a1)
- [sync_word](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#af5ef0c5e3443a011d2ed6af3c95cc4db)
- [tx](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a10b12a2092712050bdd64c6250c8731f)
- [iq_inverted](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a5737749b3bd29515887bb0b8c48c8bd1)
- [public_network](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#af97fde1f5f40a4d702c0140872728e86)
- [packet_crc_disable](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a3c9f32935f253df5e1ee67c5aab7795c)
- [mode](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#adc1f228bbba786608fbb66df2b34aa51)
- [symbol_num](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#ad12a48ff7aaa815a34e888aff839c389)
- [detection_peak](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a43d01b02bfc4e1a801ea04aa3d0f0518)
- [detection_minimum](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#ae9442b595916150367086e93e833aa68)
- [cad](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a05681aa7e1423be4b0582164bc1b02a6)
- [lora_recv_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga7fd50273b9463b602a4f457129d5c17f)
- [device](../device_reference/P002_设备对象结构.md)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [lora_cad_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga73606f1fdbea0b408315b9cbb28a4e19)
- [lora_api_config](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gabc8cba7c3f81961eac289adc40d3c8e1)
- [lora_api_config_gfsk](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga8993b902d31eac8870eb3a7f27a255cd)
- [lora_api_airtime](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga02edec1bd6925622926b3fc8833c8bec)
- [lora_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gaddff151212a432c1dbf00c3665033eb0)
- [lora_api_send_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga1dafc39726315c7921d7dd6b1e0caac4)
- [k_poll_signal](../eventpoll_reference/P005_轮询信号结构.md)
- [lora_api_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga166896d4f655cc2630e5951b1ad45c01)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [lora_api_recv_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gad3bac89281cbf6cc79f2f4df6f4b4329)
- [lora_api_cad](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gaf308b8431762462eb172f4e0bdfce99f)
- [lora_api_cad_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga604500a11fa03edae97862c29b233ed1)
- [lora_api_rssi](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga185dba9fc898f2c9407b9a9461695b8e)
- [lora_api_recv_duty_cycle](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga8ad83577ede3ca3c7d4b037c95e039e3)
- [lora_api_recv_duty_cycle_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#gafac86253dce5dbe9286683f565663971)
- [lora_api_test_cw](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface__backend.html#ga796b75a4b27b9331d78f1916e36ea1d2)
- [lora_driver_api](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md)
- [config](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#ae5fc4c8418225f44a220b6b4d223f114)
- [config_gfsk](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#a83a2e31b05a17ddf82de6bb6e55c1381)
- [airtime](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#aa8600981dbaa6eaf35da02fb586828ab)
- [send](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#ad37a8cdd8801b9c0036259dde6bc1a93)
- [send_async](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#ab5ac6d906cc2429f065d720e3af1ceaf)
- [recv](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#a30296d89ea10356fd1ded3dcbcae7618)
- [recv_async](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#aa2b7d4975ed91b4c0898842aa9e271fd)
- [cad](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#a98fc632a4e30079bc08b94b9d5dbbb1c)
- [cad_async](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#a8c579d89e40f1b9374711d5d3bef148b)
- [rssi](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#afc1eb7fabc1e59b224317ddd912f4d77)
- [recv_duty_cycle_async](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#a255ba5321ad6423de1b613b2c3520334)
- [recv_duty_cycle](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#a1e2d0208c52e6fe0ec6c51484537f033)
- [test_cw](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#ad582af08f38b4c2fc83588e7108bef6b)
- [lora_config](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gad99239be6aeda56b859ca571514806b9)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [lora_config_gfsk](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gac5db659ac5d4ce04dc3d2e69c1ecea22)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [lora_airtime](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gaedf7847838b1e2b83bde8fc7bf735cf6)
- [lora_send](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gad893b49a74e350bb05f42f863af31446)
- [lora_send_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga3788cb51c9e8d9ad7e0e8fb5ddc3a26b)
- [lora_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga28005c24ab1c13eb311bc05c3454a8f6)
- [lora_recv_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gafeae6fa9d81508023665705bf16b6435)
- [lora_cad](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga497bf93cfe42ce6a6d48a4b463b52c21)
- [lora_cad_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga35e79551b8cdb160e74d3759a76f2db4)
- [lora_rssi](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga75d2c701f482d35cfbdd94906b8799c9)
- [lora_energy_detect](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#gacf4c29b613fc525cfdc0b961c39981b4)
- [lora_recv_duty_cycle](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga5d1802eed6067734ca45c70e3114b272)
- [lora_recv_duty_cycle_async](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga2192d812e6203f6361b8beaeb1d7361c)
- [lora_test_cw](https://docs.zephyrproject.org/latest/doxygen/html/group__lora__interface.html#ga27d78168c737d56f9f7f3bbdacb808fb)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [lora_driver_api::recv_duty_cycle](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#a1e2d0208c52e6fe0ec6c51484537f033)
- [lora_driver_api::recv_duty_cycle_async](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#a255ba5321ad6423de1b613b2c3520334)
- [lora_driver_api::recv](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#a30296d89ea10356fd1ded3dcbcae7618)
- [lora_driver_api::config_gfsk](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#a83a2e31b05a17ddf82de6bb6e55c1381)
- [lora_driver_api::cad_async](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#a8c579d89e40f1b9374711d5d3bef148b)
- [lora_driver_api::cad](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#a98fc632a4e30079bc08b94b9d5dbbb1c)
- [lora_driver_api::recv_async](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#aa2b7d4975ed91b4c0898842aa9e271fd)
- [lora_driver_api::airtime](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#aa8600981dbaa6eaf35da02fb586828ab)
- [lora_driver_api::send_async](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#ab5ac6d906cc2429f065d720e3af1ceaf)
- [lora_driver_api::send](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#ad37a8cdd8801b9c0036259dde6bc1a93)
- [lora_driver_api::test_cw](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#ad582af08f38b4c2fc83588e7108bef6b)
- [lora_driver_api::config](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#ae5fc4c8418225f44a220b6b4d223f114)
- [lora_driver_api::rssi](../modem_wireless_model_reference/P028_lora_driver_api_结构体.md#afc1eb7fabc1e59b224317ddd912f4d77)
- [lora_modem_config_gfsk::bitrate](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a24e0dd59c6b63672c546a52a54066186)
- [lora_modem_config_gfsk::whitening](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a2868bdf2650e0e1082bac10357d8ab67)
- [lora_modem_config_gfsk::freq_deviation](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a2a8b2df70532bb82920431e2e013b5b0)
- [lora_modem_config_gfsk::payload_len](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a5ae2b2c3e7e12db26a7ebc95b8146dcd)
- [lora_modem_config_gfsk::sync_word_len](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a5c6b50a264eef09a4198e2116908f8b8)
- [lora_modem_config_gfsk::tx](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a93b6c16da78ca973ba20549bc5ca833e)
- [lora_modem_config_gfsk::preamble_len](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a9b816ff8b4f215761399b5f7cd3b9f1e)
- [lora_modem_config_gfsk::frequency](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a9dd764760623f5ee04ea608cbc180c00)
- [lora_modem_config_gfsk::bandwidth](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#a9fdc015f243dfe7bae02c69ae4028258)
- [lora_modem_config_gfsk::tx_power](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#aadc6d35654c3158932080d4e7b5b5f9f)
- [lora_modem_config_gfsk::pulse_shape](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#ab290c324797465c551e903df15a8eee3)
- [lora_modem_config_gfsk::packet_crc_disable](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#ad5ba923fe733374b23e1e67918d1fc5a)
- [lora_modem_config_gfsk::sync_word](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#aee3775468ec73b8cfa8347996a897445)
- [lora_modem_config_gfsk::fixed_len](../modem_wireless_model_reference/P030_lora_modem_config_gfsk_结构体.md#afd0fe3012874bfb460283dbd6cba0a72)
- [lora_modem_config::cad](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a05681aa7e1423be4b0582164bc1b02a6)
- [lora_modem_config::frequency](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a08209a2dabc5111025810fc8e141c2df)
- [lora_modem_config::bandwidth](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a0c6a90e31b4a97d962af3dbd0ee8e885)
- [lora_modem_config::tx](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a10b12a2092712050bdd64c6250c8731f)
- [lora_modem_config::packet_crc_disable](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a3c9f32935f253df5e1ee67c5aab7795c)
- [lora_modem_config::tx_power](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a41a194d62e1e3e1b142e194a75efb8a1)
- [lora_modem_config::detection_peak](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a43d01b02bfc4e1a801ea04aa3d0f0518)
- [lora_modem_config::iq_inverted](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a5737749b3bd29515887bb0b8c48c8bd1)
- [lora_modem_config::coding_rate](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a8e47a8506265562c7b118fab72cceb10)
- [lora_modem_config::preamble_len](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#a9d0795c5be6ae0042babaa05615cf7f2)
- [lora_modem_config::symbol_num](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#ad12a48ff7aaa815a34e888aff839c389)
- [lora_modem_config::mode](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#adc1f228bbba786608fbb66df2b34aa51)
- [lora_modem_config::datarate](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#ae438c1c223f12fc6c3747d4297ec61ba)
- [lora_modem_config::detection_minimum](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#ae9442b595916150367086e93e833aa68)
- [lora_modem_config::sync_word](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#af5ef0c5e3443a011d2ed6af3c95cc4db)
- [lora_modem_config::public_network](../modem_wireless_model_reference/P029_lora_modem_config_结构体.md#af97fde1f5f40a4d702c0140872728e86)

---

[上一章](P450_loopback_disk.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P452_emul.h_源码浏览.md)
