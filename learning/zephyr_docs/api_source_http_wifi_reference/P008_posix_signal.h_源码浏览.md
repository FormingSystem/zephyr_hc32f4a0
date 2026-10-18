---
id: learning.zephyr-docs.api-source-http-wifi-reference.page-8
title: posix_signal.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_posix\_signal.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html)。

## 8.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
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
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
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
<a id="foldopen00053"></a>
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
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00073"></a>
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
<a id="foldopen00089"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="foldopen00112"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00136"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
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
<a id="foldopen00158"></a>
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
<a id="l00190"></a>
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
<a id="foldopen00201"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="foldopen00211"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
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
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
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
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="a__timespec_8h_html_aa17c461cd5eca7fc12a66daa803c7fd7"></a>
<a id="agroup__sys-util_html_ga2f660aa23a5dbc0f4b8df48b4302b8c3"></a>
<a id="agroup__sys-util_html_gae664e7492e37d324831caf2321ddda37"></a>
<a id="agroup__toolchain_html_ga1f08471f8dba6ce2a3e0f38bea73d7b5"></a>
<a id="agroup__toolchain_html_ga5365fdbb6323f48ddca9ab4149e9a561"></a>
<a id="agroup__toolchain_html_gae917ae1adad468956fa5d28a50d10670"></a>
<a id="aposix__signal_8h_html_a1034c4dceaeebeee401fbf7c5e4396ed"></a>
<a id="aposix__signal_8h_html_a114f9c2461df851d2ad00aad8dcfa3f7"></a>
<a id="aposix__signal_8h_html_a16972ede9065cb2709fcfc6a84272116"></a>
<a id="aposix__signal_8h_html_a16efce9e80266d0db1ed9a3ef281ad2b"></a>
<a id="aposix__signal_8h_html_a4539db972bcf3dd8c8b429af0dc3789d"></a>
<a id="aposix__signal_8h_html_a4949c54b6d058d6fd166c59b7e7aac24"></a>
<a id="aposix__signal_8h_html_a4ba25c1b785eb5c68e93ee2a73fd7a34"></a>
<a id="aposix__signal_8h_html_a5336d2c76af22b10373e3dd28fb3b0f0"></a>
<a id="aposix__signal_8h_html_a5858057ae172789da253b6b281d49875"></a>
<a id="aposix__signal_8h_html_a5925352f90eb589393274fa0376d7def"></a>
<a id="aposix__signal_8h_html_a5aafacc071cdfafd0eb992004dee3e62"></a>
<a id="aposix__signal_8h_html_a5d5adc4eb4b54c2ce456db2c36905322"></a>
<a id="aposix__signal_8h_html_a5dabd0b7783afd0e4cab78446436e25c"></a>
<a id="aposix__signal_8h_html_a5eaaad0671fbdba01a60ab5b1c8649be"></a>
<a id="aposix__signal_8h_html_a651e913fac32255355993a3d7ca193c8"></a>
<a id="aposix__signal_8h_html_a6e6b04897703c43b2ad10013041ad152"></a>
<a id="aposix__signal_8h_html_a7b91eecad5998acd6162fde3ab530d7a"></a>
<a id="aposix__signal_8h_html_a87cd503247b3afbb79788256ac093ad5"></a>
<a id="aposix__signal_8h_html_a88d7bbc77ea1569ee21c90db549ea023"></a>
<a id="aposix__signal_8h_html_a8a0e594afe61149ff3f4e48c722c46b1"></a>
<a id="aposix__signal_8h_html_a8f2faa6ea120d4cb0cc916f46d3731a7"></a>
<a id="aposix__signal_8h_html_a8f5732f547a8cd36485e3e08490757f2"></a>
<a id="aposix__signal_8h_html_aa11e3a8419c84b5af84dad8e7663a670"></a>
<a id="aposix__signal_8h_html_aa9255939ddcf0bdcd925f1fca741238c"></a>
<a id="aposix__signal_8h_html_ab3f45e72c67ecc7866d14ab09b3367e7"></a>
<a id="aposix__signal_8h_html_aba080a9ab72ac6d079ff0bf8ac9b23f4"></a>
<a id="aposix__signal_8h_html_ae29ee6133f77ce4ef463a7bb9734716f"></a>
<a id="aposix__signal_8h_html_af1e91276412ec4c5ed1d4ae71fc0bdb4"></a>
<a id="aposix__signal_8h_html_af2a9e8d53e783f7ad3343ac36ecc74b0"></a>
<a id="aposix__signal_8h_html_afa550831803d7395d8ac098d6be59242"></a>
<a id="aposix__signal_8h_html_afc544433253791fc5f87b8203c9b6e63"></a>
<a id="astructmcontext__t_html"></a>
<a id="astructmcontext__t_html_a3dbbd980d01e9f843e842f09217c522d"></a>
<a id="astructmcontext__t_html_ae2977e51fe658ca375e4f2ee8994bdcb"></a>
<a id="astructpthread__attr__t_html"></a>
<a id="astructpthread__attr__t_html_a24c790e83123e988fc8fdeb7c7ad9325"></a>
<a id="astructpthread__attr__t_html_a83d718349c0b2f1d93e103fa7cc1dac4"></a>
<a id="astructsigaction_html"></a>
<a id="astructsigaction_html_a1830265abeb7454d61dbf1104bdef231"></a>
<a id="astructsigaction_html_a684e70081d03d46ce70af097ea5cfd49"></a>
<a id="astructsigaction_html_ac794783ce745372a2cd61fd0ec93b4d7"></a>
<a id="astructsigaction_html_aea0dabe7a03641c8b426521f4406b425"></a>
<a id="astructsigevent_html"></a>
<a id="astructsigevent_html_a0b3b43507546409ccc399a918942aba5"></a>
<a id="astructsigevent_html_a5a687d2092b237d76eb08e2d46a5115f"></a>
<a id="astructsigevent_html_a5c645ec1d12bb46efc3f4097c52b665d"></a>
<a id="astructsigevent_html_a757af1e34b87e3f66bbc08c514017a2c"></a>
<a id="astructsigevent_html_aae9a19d879c38e0c4e8a9bf738c5081e"></a>
<a id="astructsiginfo__t_html"></a>
<a id="astructsiginfo__t_html_a0dd36ae3e9df589f5755f88c93671c2d"></a>
<a id="astructsiginfo__t_html_a1574f7a20201b3f6bf64c5091fd14845"></a>
<a id="astructsiginfo__t_html_a238821f6eb15317d3d7b10efef80b9c7"></a>
<a id="astructsiginfo__t_html_a6053bfd6db1f12a9678cf53ebfeae45d"></a>
<a id="astructsiginfo__t_html_a6ce15e0f745b97a19ccbd075e9a6ce7d"></a>
<a id="astructsiginfo__t_html_accaf16ba75f1d4efd2e76f1991dc2b56"></a>
<a id="astructsiginfo__t_html_ad1b72421321261362dfc00d180d8de69"></a>
<a id="astructsiginfo__t_html_ae840a8f2824bab1693577f19f4d0432d"></a>
<a id="astructsiginfo__t_html_aea6512792c4af9f46ba221e454b6e0a7"></a>
<a id="astructsigset__t_html"></a>
<a id="astructsigset__t_html_a0017a77af9e5cdca8f1e0ffd4b7e086e"></a>
<a id="astructstack__t_html"></a>
<a id="astructstack__t_html_a4e768ba748dc571d736f38cbb138f8e6"></a>
<a id="astructstack__t_html_a72825bf6898b7e0bc0b916b220440d9e"></a>
<a id="astructstack__t_html_ae3df42e1671d5e8861bca62318fb063f"></a>
<a id="astructtimespec_html"></a>
<a id="astructtimespec_html_ae3c7510dafa8cbcaede866ed13c99683"></a>
<a id="astructtimespec_html_afc3302668d7cb5952f590da69fdd4955"></a>
<a id="astructucontext__t_html"></a>
<a id="astructucontext__t_html_a2dc143fa6b3f0fa8d0f27acbfaed0d9e"></a>
<a id="astructucontext__t_html_a7210eb8a464c276b9c68e749b3aa28f1"></a>
<a id="astructucontext__t_html_a7f8c7406758045ea8be9dd61831f16f2"></a>
<a id="astructucontext__t_html_aabde4c64c7bcf764e937361d8c341504"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>
<a id="aunionsigval_html"></a>
<a id="aunionsigval_html_a4668f1bd7463de7b70bd0022207e26ac"></a>
<a id="aunionsigval_html_a560393252ee7edc37df44bf1c11bdbdd"></a>

```c
/*
 * Copyright (c) 2025 The Zephyr Contributors
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_POSIX_SIGNAL_H_
#define ZEPHYR_INCLUDE_POSIX_POSIX_SIGNAL_H_

#if defined(_POSIX_C_SOURCE) || defined(__DOXYGEN__)

#include <zephyr/toolchain.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif

/* SIG_DFL must be defined by the libc signal.h */
/* SIG_ERR must be defined by the libc signal.h */

#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
#define SIG_HOLD ((void *)-2)
#endif

/* SIG_IGN must be defined by the libc signal.h */

#if defined(_POSIX_THREADS) || defined(__DOXYGEN__)

#if !defined(_PTHREAD_T_DECLARED) && !defined(__pthread_t_defined)
typedef unsigned int pthread_t;
#define _PTHREAD_T_DECLARED
#define __pthread_t_defined
#endif

#endif /* defined(_POSIX_THREADS) || defined(__DOXYGEN__) */

/* size_t must be defined by the libc stddef.h */
#include <stddef.h>

#if !defined(_UID_T_DECLARED) && !defined(__uid_t_defined)
typedef int uid_t;
#define _UID_T_DECLARED
#define __uid_t_defined
#endif

/* time_t must be defined by the libc time.h */
#include <time.h>

#if __STDC_VERSION__ >= 201112L
/* struct timespec must be defined in the libc time.h */
#else
#if !defined(_TIMESPEC_DECLARED) && !defined(__timespec_defined)
struct timespec {
        time_t tv_sec;
        long tv_nsec;
};
#define _TIMESPEC_DECLARED
#define __timespec_defined
#endif
#endif

/* sig_atomic_t must be defined by the libc signal.h */

#define SIGRTMIN 32
#if defined(_POSIX_REALTIME_SIGNALS) || defined(__DOXYGEN__)
BUILD_ASSERT(CONFIG_POSIX_RTSIG_MAX >= 0);
#define SIGRTMAX (SIGRTMIN + CONFIG_POSIX_RTSIG_MAX)
#else
#define SIGRTMAX SIGRTMIN
#endif

#if !defined(_SIGSET_T_DECLARED) && !defined(__sigset_t_defined)
typedef struct {
        unsigned long sig[DIV_ROUND_UP(SIGRTMAX + 1, BITS_PER_LONG)];
} sigset_t;
#define _SIGSET_T_DECLARED
#define __sigset_t_defined
#endif

#if !defined(_PID_T_DECLARED) && !defined(__pid_t_defined)
typedef long pid_t;
#define _PID_T_DECLARED
#define __pid_t_defined
#endif

#if defined(_POSIX_THREADS) || defined(__DOXYGEN__)

#if !defined(_PTHREAD_ATTR_T_DECLARED) && !defined(__pthread_attr_t_defined)
typedef struct {
        void *stack;
        unsigned int details[2];
} pthread_attr_t;
#define _PTHREAD_ATTR_T_DECLARED
#define __pthread_attr_t_defined
#endif

#endif

#if defined(_POSIX_REALTIME_SIGNALS) || defined(__DOXYGEN__)

/* slightly out of order w.r.t. the specification */
#if !defined(_SIGVAL_DECLARED) && !defined(__sigval_defined)
union sigval {
        int sival_int;
        void *sival_ptr;
};
#define _SIGVAL_DECLARED
#define __sigval_defined
#endif

#if !defined(_SIGEVENT_DECLARED) && !defined(__sigevent_defined)
struct sigevent {
#if defined(_POSIX_THREADS) || defined(__DOXYGEN__)
        pthread_attr_t *sigev_notify_attributes;
        void (*sigev_notify_function)(union sigval value);
#endif
        union sigval sigev_value;
        int sigev_notify;
        int sigev_signo;
};
#define _SIGEVENT_DECLARED
#define __sigevent_defined
#endif

#define SIGEV_NONE   1
#define SIGEV_SIGNAL 2
#define SIGEV_THREAD 3

/* Signal constants are defined below */

#endif /* defined(_POSIX_REALTIME_SIGNALS) || defined(__DOXYGEN__) */

/* SIGRTMIN and SIGRTMAX defined above */

#if !defined(_SIGINFO_T_DECLARED) && !defined(__siginfo_t_defined)
typedef struct {
        void *si_addr;
#if defined(_XOPEN_STREAMS) || defined(__DOXYGEN__)
        long si_band;
#endif
        union sigval si_value;
        pid_t si_pid;
        uid_t si_uid;
        int si_signo;
        int si_code;
#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
        int si_errno;
#endif
        int si_status;
} siginfo_t;
#define _SIGINFO_T_DECLARED
#define __siginfo_t_defined
#endif

#if defined(_POSIX_REALTIME_SIGNALS) || defined(__DOXYGEN__)

#if !defined(_SIGACTION_DECLARED) && !defined(__sigaction_defined)
struct sigaction {
        union {
                void (*sa_handler)(int sig);
                void (*sa_sigaction)(int sig, siginfo_t *info, void *context);
        };
        sigset_t sa_mask;
        int sa_flags;
};
#define _SIGACTION_DECLARED
#define __sigaction_defined
#endif

#define SIG_BLOCK   1
#define SIG_UNBLOCK 2
#define SIG_SETMASK 0

#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
#define SA_NOCLDSTOP 0x00000001
#define SA_ONSTACK   0x00000002
#endif
#define SA_RESETHAND 0x00000004
#define SA_RESTART   0x00000008
#define SA_SIGINFO   0x00000010
#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
#define SA_NOCLDWAIT 0x00000020
#endif
#define SA_NODEFER  0x00000040
#define SS_ONSTACK  0x00000001
#define SS_DISABLE  0x00000002
#define MINSIGSTKSZ 4096
#define SIGSTKSZ    4096

#if !defined(_MCONTEXT_T_DECLARED) && !defined(__mcontext_t_defined)
typedef struct {
        /* FIXME: there should be a much better Zephyr-specific structure that can be used here */
        unsigned long gregs[32];
        unsigned long flags;
} mcontext_t;
#define _MCONTEXT_T_DECLARED
#define __mcontext_defined
#endif

#if !defined(_STACK_T_DECLARED) && !defined(__stack_t_defined)
typedef struct {
        void *ss_sp;
        size_t ss_size;
        int ss_flags;
} stack_t;
#define _STACK_T_DECLARED
#define __stack_t_defined
#endif

#if !defined(_UCONTEXT_T_DECLARED) && !defined(__ucontext_t_defined)
typedef struct {
        struct ucontext *uc_link;
        sigset_t uc_sigmask;
        stack_t uc_stack;
        mcontext_t uc_mcontext;
} ucontext_t;
#define _UCONTEXT_T_DECLARED
#define __ucontext_defined
#endif

#endif /* defined(_POSIX_REALTIME_SIGNALS) || defined(__DOXYGEN__) */

/* Siginfo codes are defined below */

#if !defined(_SIGHANDLER_T_DECLARED) && !defined(__sighandler_t_defined)
typedef void (*sighandler_t)(int sig);
#define _SIGHANDLER_T_DECLARED
#define __sighandler_t_defined
#endif

int kill(pid_t pid, int sig);
#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
int killpg(pid_t pgrp, int sig);
#endif
void psiginfo(const siginfo_t *info, const char *message);
void psignal(int sig, const char *message);
#if defined(_POSIX_THREADS) || defined(__DOXYGEN__)
int pthread_kill(pthread_t thread, int sig);
int pthread_sigmask(int how, const sigset_t *ZRESTRICT set, sigset_t *ZRESTRICT oset);
#endif
/* raise() must be defined by the libc signal.h */
#if defined(_POSIX_REALTIME_SIGNALS) || defined(__DOXYGEN__)
TOOLCHAIN_DISABLE_WARNING(TOOLCHAIN_WARNING_SHADOW);
int sigaction(int sig, const struct sigaction *ZRESTRICT act, struct sigaction *ZRESTRICT oact);
TOOLCHAIN_ENABLE_WARNING(TOOLCHAIN_WARNING_SHADOW);
#endif
int sigaddset(sigset_t *set, int sig);
#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
int sigaltstack(const stack_t *ZRESTRICT ss, stack_t *ZRESTRICT oss);
#endif
int sigdelset(sigset_t *set, int sig);
int sigemptyset(sigset_t *set);
int sigfillset(sigset_t *set);
#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
int sighold(int sig);
int sigignore(int sig);
int siginterrupt(int sig, int flag);
#endif
int sigismember(const sigset_t *set, int sig);
/* signal() must be defined by the libc signal.h */
#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
int sigpause(int sig);
#endif
int sigpending(sigset_t *set);
int sigprocmask(int how, const sigset_t *ZRESTRICT set, sigset_t *ZRESTRICT oset);
#if defined(_POSIX_REALTIME_SIGNALS) || defined(__DOXYGEN__)
int sigqueue(pid_t pid, int sig, union sigval value);
#endif
#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
int sigrelse(int sig);
sighandler_t sigset(int sig, sighandler_t disp);
#endif
int sigsuspend(const sigset_t *set);
#if defined(_POSIX_REALTIME_SIGNALS) || defined(__DOXYGEN__)
int sigtimedwait(const sigset_t *ZRESTRICT set, siginfo_t *ZRESTRICT info,
                 const struct timespec *ZRESTRICT timeout);
#endif
int sigwait(const sigset_t *ZRESTRICT set, int *ZRESTRICT sig);
#if defined(_POSIX_REALTIME_SIGNALS) || defined(__DOXYGEN__)
int sigwaitinfo(const sigset_t *ZRESTRICT set, siginfo_t *ZRESTRICT info);
#endif

/* Note: only ANSI / ISO C signals are guarded below */

#define SIGHUP 1
#if !defined(SIGINT) || defined(__DOXYGEN__)
#define SIGINT 2
#endif
#define SIGQUIT 3
#if !defined(SIGILL) || defined(__DOXYGEN__)
#define SIGILL 4
#endif
#define SIGTRAP 5
#if !defined(SIGABRT) || defined(__DOXYGEN__)
#define SIGABRT 6
#endif
#define SIGBUS 7
#if !defined(SIGFPE) || defined(__DOXYGEN__)
#define SIGFPE 8
#endif
#define SIGKILL 9
#define SIGUSR1 10
#if !defined(SIGSEGV) || defined(__DOXYGEN__)
#define SIGSEGV 11
#endif
#define SIGUSR2 12
#define SIGPIPE 13
#define SIGALRM 14
#if !defined(SIGTERM) || defined(__DOXYGEN__)
#define SIGTERM 15
#endif
/* 16 not used */
#define SIGCHLD   17
#define SIGCONT   18
#define SIGSTOP   19
#define SIGTSTP   20
#define SIGTTIN   21
#define SIGTTOU   22
#define SIGURG    23
#define SIGXCPU   24
#define SIGXFSZ   25
#define SIGVTALRM 26
#define SIGPROF   27
/* 28 not used */
#define SIGPOLL   29
/* 30 not used */
#define SIGSYS    31

#if defined(_POSIX_REALTIME_SIGNALS) || defined(__DOXYGEN__)

/* SIGILL */
#define ILL_ILLOPC 1
#define ILL_ILLOPN 2
#define ILL_ILLADR 3
#define ILL_ILLTRP 4
#define ILL_PRVOPC 5
#define ILL_PRVREG 6
#define ILL_COPROC 7
#define ILL_BADSTK 8

/* SIGFPE */
#define FPE_INTDIV 9
#define FPE_INTOVF 10
#define FPE_FLTDIV 11
#define FPE_FLTOVF 12
#define FPE_FLTUND 13
#define FPE_FLTRES 15
#define FPE_FLTINV 16
#define FPE_FLTSUB 17

/* SIGSEGV */
#define SEGV_MAPERR 18
#define SEGV_ACCERR 19

/* SIGBUS */
#define BUS_ADRALN 20
#define BUS_ADRERR 21
#define BUS_OBJERR 22

#if defined(_XOPEN_SOURCE) || defined(__DOXYGEN__)
/* SIGTRAP */
#define TRAP_BRKPT 23
#define TRAP_TRACE 24
#endif

/* SIGCHLD */
#define CLD_EXITED    25
#define CLD_KILLED    26
#define CLD_DUMPED    27
#define CLD_TRAPPED   28
#define CLD_STOPPED   29
#define CLD_CONTINUED 30

#if defined(_XOPEN_STREAMS) || defined(__DOXYGEN__)
/* SIGPOLL */
#define POLL_IN  31
#define POLL_OUT 32
#define POLL_MSG 33
#define POLL_ERR 34
#define POLL_PRI 35
#define POLL_HUP 36
#endif

/* Any */
#define SI_USER    37
#define SI_QUEUE   38
#define SI_TIMER   39
#define SI_ASYNCIO 40
#define SI_MESGQ   41

#endif

#ifdef __cplusplus
}
#endif

#endif /* defined(_POSIX_C_SOURCE) || defined(__DOXYGEN__) */

#endif /* ZEPHYR_INCLUDE_POSIX_POSIX_SIGNAL_H_ */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 The Zephyr Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 18 行

`SIG_DFL` 必须由 C 库（libc）的 `signal.h` 定义。

### 注释 3：原第 19 行

`SIG_ERR` 必须由 C 库（libc）的 `signal.h` 定义。

### 注释 4：原第 25 行

`SIG_IGN` 必须由 C 库（libc）的 `signal.h` 定义。

### 注释 5：原第 35 行

条件编译标记：`defined(_POSIX_THREADS) || defined(__DOXYGEN__)`。

### 注释 6：原第 37 行

`size_t` 必须由 C 库（libc）的 `stddef.h` 定义。

### 注释 7：原第 46 行

`time_t` 必须由 C 库（libc）的 `time.h` 定义。

### 注释 8：原第 50 行

必须在 libc 的 `time.h` 中定义 `struct timespec`。

### 注释 9：原第 62 行

`sig_atomic_t` 必须由 C 库（libc）的 `signal.h` 定义。

### 注释 10：原第 101 行

排列顺序与规范（Specification）稍有不同。

### 注释 11：原第 129 行

信号常量（Signal Constants）定义在下方。

### 注释 12：原第 131 行

条件编译标记：`defined(_POSIX_REALTIME_SIGNALS) || defined(__DOXYGEN__)`。

### 注释 13：原第 133 行

`SIGRTMIN` 和 `SIGRTMAX` 已在上方定义。

### 注释 14：原第 192 行

**待修复（FIXME）：**此处应有更合适的 Zephyr 专用结构体可供使用。

### 注释 15：原第 221 行

条件编译标记：`defined(_POSIX_REALTIME_SIGNALS) || defined(__DOXYGEN__)`。

### 注释 16：原第 223 行

信号信息代码（Siginfo Codes）定义在下方。

### 注释 17：原第 241 行

`raise()` 必须由 C 库（libc）的 `signal.h` 定义。

### 注释 18：原第 260 行

`signal()` 必须由 C 库（libc）的 `signal.h` 定义。

### 注释 19：原第 283 行

注意：下方仅对 ANSI／ISO C 信号（Signals）设置条件保护。

### 注释 20：原第 312 行

16 未使用（Not Used）。

### 注释 21：原第 324 行

28 未使用（Not Used）。

### 注释 22：原第 326 行

30 未使用（Not Used）。

### 注释 23：原第 331 行

非法指令信号（SIGILL）。

### 注释 24：原第 341 行

算术异常信号（SIGFPE）。

### 注释 25：原第 351 行

无效内存访问信号（SIGSEGV）。

### 注释 26：原第 355 行

总线错误信号（SIGBUS）。

### 注释 27：原第 361 行

跟踪／断点陷阱信号（SIGTRAP）。

### 注释 28：原第 366 行

子进程状态变化信号（SIGCHLD）。

### 注释 29：原第 375 行

可轮询事件信号（SIGPOLL）。

### 注释 30：原第 384 行

任意（Any）。

### 注释 31：原第 397 行

条件表达式：`defined(_POSIX_C_SOURCE) || defined(__DOXYGEN__)`。

### 注释 32：原第 399 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_POSIX_SIGNAL_H_`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)
- [uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [tv_sec](../time_headers_reference/P005_timespec时间结构.md#afc3302668d7cb5952f590da69fdd4955)
- [tv_nsec](../time_headers_reference/P005_timespec时间结构.md#ae3c7510dafa8cbcaede866ed13c99683)
- [sig](../posix_system_model_reference/P020_sigset_t_结构体.md#a0017a77af9e5cdca8f1e0ffd4b7e086e)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [SIGRTMAX](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a5336d2c76af22b10373e3dd28fb3b0f0)
- [BITS_PER_LONG](../util_reference/P001_通用工具公共接口.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)
- [sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)
- [pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)
- [stack](../posix_system_model_reference/P011_pthread_attr_t_结构体.md#a24c790e83123e988fc8fdeb7c7ad9325)
- [details](../posix_system_model_reference/P011_pthread_attr_t_结构体.md#a83d718349c0b2f1d93e103fa7cc1dac4)
- [pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)
- [sigval](../posix_system_model_reference/P035_sigval_联合体.md)
- [sival_int](../posix_system_model_reference/P035_sigval_联合体.md#a560393252ee7edc37df44bf1c11bdbdd)
- [sival_ptr](../posix_system_model_reference/P035_sigval_联合体.md#a4668f1bd7463de7b70bd0022207e26ac)
- [sigevent](../posix_system_model_reference/P018_sigevent_结构体.md)
- [sigev_notify_attributes](../posix_system_model_reference/P018_sigevent_结构体.md#a5a687d2092b237d76eb08e2d46a5115f)
- [sigev_notify_function](../posix_system_model_reference/P018_sigevent_结构体.md#a0b3b43507546409ccc399a918942aba5)
- [sigev_value](../posix_system_model_reference/P018_sigevent_结构体.md#a757af1e34b87e3f66bbc08c514017a2c)
- [sigev_notify](../posix_system_model_reference/P018_sigevent_结构体.md#aae9a19d879c38e0c4e8a9bf738c5081e)
- [sigev_signo](../posix_system_model_reference/P018_sigevent_结构体.md#a5c645ec1d12bb46efc3f4097c52b665d)
- [si_addr](../posix_system_model_reference/P019_siginfo_t_结构体.md#ad1b72421321261362dfc00d180d8de69)
- [si_band](../posix_system_model_reference/P019_siginfo_t_结构体.md#a6ce15e0f745b97a19ccbd075e9a6ce7d)
- [si_value](../posix_system_model_reference/P019_siginfo_t_结构体.md#aea6512792c4af9f46ba221e454b6e0a7)
- [si_pid](../posix_system_model_reference/P019_siginfo_t_结构体.md#a6053bfd6db1f12a9678cf53ebfeae45d)
- [si_uid](../posix_system_model_reference/P019_siginfo_t_结构体.md#a1574f7a20201b3f6bf64c5091fd14845)
- [si_signo](../posix_system_model_reference/P019_siginfo_t_结构体.md#a238821f6eb15317d3d7b10efef80b9c7)
- [si_code](../posix_system_model_reference/P019_siginfo_t_结构体.md#a0dd36ae3e9df589f5755f88c93671c2d)
- [si_errno](../posix_system_model_reference/P019_siginfo_t_结构体.md#ae840a8f2824bab1693577f19f4d0432d)
- [si_status](../posix_system_model_reference/P019_siginfo_t_结构体.md#accaf16ba75f1d4efd2e76f1991dc2b56)
- [siginfo_t](../posix_system_model_reference/P019_siginfo_t_结构体.md)
- [sigaction](../posix_system_model_reference/P017_sigaction_结构体.md)
- [sa_handler](../posix_system_model_reference/P017_sigaction_结构体.md#ac794783ce745372a2cd61fd0ec93b4d7)
- [sa_sigaction](../posix_system_model_reference/P017_sigaction_结构体.md#a1830265abeb7454d61dbf1104bdef231)
- [sa_mask](../posix_system_model_reference/P017_sigaction_结构体.md#a684e70081d03d46ce70af097ea5cfd49)
- [sa_flags](../posix_system_model_reference/P017_sigaction_结构体.md#aea0dabe7a03641c8b426521f4406b425)
- [gregs](../platform_security_model_reference/P017_mcontext_t_结构体.md#ae2977e51fe658ca375e4f2ee8994bdcb)
- [flags](../platform_security_model_reference/P017_mcontext_t_结构体.md#a3dbbd980d01e9f843e842f09217c522d)
- [mcontext_t](../platform_security_model_reference/P017_mcontext_t_结构体.md)
- [ss_sp](../posix_system_model_reference/P021_stack_t_结构体.md#a4e768ba748dc571d736f38cbb138f8e6)
- [ss_size](../posix_system_model_reference/P021_stack_t_结构体.md#ae3df42e1671d5e8861bca62318fb063f)
- [ss_flags](../posix_system_model_reference/P021_stack_t_结构体.md#a72825bf6898b7e0bc0b916b220440d9e)
- [stack_t](../posix_system_model_reference/P021_stack_t_结构体.md)
- [uc_link](../posix_system_model_reference/P027_ucontext_t_结构体.md#a7210eb8a464c276b9c68e749b3aa28f1)
- [uc_sigmask](../posix_system_model_reference/P027_ucontext_t_结构体.md#aabde4c64c7bcf764e937361d8c341504)
- [uc_stack](../posix_system_model_reference/P027_ucontext_t_结构体.md#a2dc143fa6b3f0fa8d0f27acbfaed0d9e)
- [uc_mcontext](../posix_system_model_reference/P027_ucontext_t_结构体.md#a7f8c7406758045ea8be9dd61831f16f2)
- [ucontext_t](../posix_system_model_reference/P027_ucontext_t_结构体.md)
- [sighandler_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a87cd503247b3afbb79788256ac093ad5)
- [kill](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a4539db972bcf3dd8c8b429af0dc3789d)
- [killpg](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a4ba25c1b785eb5c68e93ee2a73fd7a34)
- [psiginfo](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#aa9255939ddcf0bdcd925f1fca741238c)
- [psignal](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afa550831803d7395d8ac098d6be59242)
- [pthread_kill](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a5aafacc071cdfafd0eb992004dee3e62)
- [pthread_sigmask](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a16972ede9065cb2709fcfc6a84272116)
- [TOOLCHAIN_DISABLE_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga1f08471f8dba6ce2a3e0f38bea73d7b5)
- [TOOLCHAIN_WARNING_SHADOW](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gae917ae1adad468956fa5d28a50d10670)
- [sigaction](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a5dabd0b7783afd0e4cab78446436e25c)
- [TOOLCHAIN_ENABLE_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga5365fdbb6323f48ddca9ab4149e9a561)
- [sigaddset](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#aba080a9ab72ac6d079ff0bf8ac9b23f4)
- [sigaltstack](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#af2a9e8d53e783f7ad3343ac36ecc74b0)
- [sigdelset](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a16efce9e80266d0db1ed9a3ef281ad2b)
- [sigemptyset](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a5925352f90eb589393274fa0376d7def)
- [sigfillset](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a88d7bbc77ea1569ee21c90db549ea023)
- [sighold](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a8f2faa6ea120d4cb0cc916f46d3731a7)
- [sigignore](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a1034c4dceaeebeee401fbf7c5e4396ed)
- [siginterrupt](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a5d5adc4eb4b54c2ce456db2c36905322)
- [sigismember](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a5eaaad0671fbdba01a60ab5b1c8649be)
- [sigpause](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#aa11e3a8419c84b5af84dad8e7663a670)
- [sigpending](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a7b91eecad5998acd6162fde3ab530d7a)
- [sigprocmask](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a6e6b04897703c43b2ad10013041ad152)
- [sigqueue](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a4949c54b6d058d6fd166c59b7e7aac24)
- [sigrelse](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a8a0e594afe61149ff3f4e48c722c46b1)
- [sigset](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#af1e91276412ec4c5ed1d4ae71fc0bdb4)
- [sigsuspend](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a651e913fac32255355993a3d7ca193c8)
- [sigtimedwait](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a5858057ae172789da253b6b281d49875)
- [sigwait](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a8f5732f547a8cd36485e3e08490757f2)
- [sigwaitinfo](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ae29ee6133f77ce4ef463a7bb9734716f)
- [mcontext_t::flags](../platform_security_model_reference/P017_mcontext_t_结构体.md#a3dbbd980d01e9f843e842f09217c522d)
- [mcontext_t::gregs](../platform_security_model_reference/P017_mcontext_t_结构体.md#ae2977e51fe658ca375e4f2ee8994bdcb)
- [pthread_attr_t::stack](../posix_system_model_reference/P011_pthread_attr_t_结构体.md#a24c790e83123e988fc8fdeb7c7ad9325)
- [pthread_attr_t::details](../posix_system_model_reference/P011_pthread_attr_t_结构体.md#a83d718349c0b2f1d93e103fa7cc1dac4)
- [sigaction::sa_sigaction](../posix_system_model_reference/P017_sigaction_结构体.md#a1830265abeb7454d61dbf1104bdef231)
- [sigaction::sa_mask](../posix_system_model_reference/P017_sigaction_结构体.md#a684e70081d03d46ce70af097ea5cfd49)
- [sigaction::sa_handler](../posix_system_model_reference/P017_sigaction_结构体.md#ac794783ce745372a2cd61fd0ec93b4d7)
- [sigaction::sa_flags](../posix_system_model_reference/P017_sigaction_结构体.md#aea0dabe7a03641c8b426521f4406b425)
- [sigevent::sigev_notify_function](../posix_system_model_reference/P018_sigevent_结构体.md#a0b3b43507546409ccc399a918942aba5)
- [sigevent::sigev_notify_attributes](../posix_system_model_reference/P018_sigevent_结构体.md#a5a687d2092b237d76eb08e2d46a5115f)
- [sigevent::sigev_signo](../posix_system_model_reference/P018_sigevent_结构体.md#a5c645ec1d12bb46efc3f4097c52b665d)
- [sigevent::sigev_value](../posix_system_model_reference/P018_sigevent_结构体.md#a757af1e34b87e3f66bbc08c514017a2c)
- [sigevent::sigev_notify](../posix_system_model_reference/P018_sigevent_结构体.md#aae9a19d879c38e0c4e8a9bf738c5081e)
- [siginfo_t::si_code](../posix_system_model_reference/P019_siginfo_t_结构体.md#a0dd36ae3e9df589f5755f88c93671c2d)
- [siginfo_t::si_uid](../posix_system_model_reference/P019_siginfo_t_结构体.md#a1574f7a20201b3f6bf64c5091fd14845)
- [siginfo_t::si_signo](../posix_system_model_reference/P019_siginfo_t_结构体.md#a238821f6eb15317d3d7b10efef80b9c7)
- [siginfo_t::si_pid](../posix_system_model_reference/P019_siginfo_t_结构体.md#a6053bfd6db1f12a9678cf53ebfeae45d)
- [siginfo_t::si_band](../posix_system_model_reference/P019_siginfo_t_结构体.md#a6ce15e0f745b97a19ccbd075e9a6ce7d)
- [siginfo_t::si_status](../posix_system_model_reference/P019_siginfo_t_结构体.md#accaf16ba75f1d4efd2e76f1991dc2b56)
- [siginfo_t::si_addr](../posix_system_model_reference/P019_siginfo_t_结构体.md#ad1b72421321261362dfc00d180d8de69)
- [siginfo_t::si_errno](../posix_system_model_reference/P019_siginfo_t_结构体.md#ae840a8f2824bab1693577f19f4d0432d)
- [siginfo_t::si_value](../posix_system_model_reference/P019_siginfo_t_结构体.md#aea6512792c4af9f46ba221e454b6e0a7)
- [sigset_t::sig](../posix_system_model_reference/P020_sigset_t_结构体.md#a0017a77af9e5cdca8f1e0ffd4b7e086e)
- [stack_t::ss_sp](../posix_system_model_reference/P021_stack_t_结构体.md#a4e768ba748dc571d736f38cbb138f8e6)
- [stack_t::ss_flags](../posix_system_model_reference/P021_stack_t_结构体.md#a72825bf6898b7e0bc0b916b220440d9e)
- [stack_t::ss_size](../posix_system_model_reference/P021_stack_t_结构体.md#ae3df42e1671d5e8861bca62318fb063f)
- [timespec::tv_nsec](../time_headers_reference/P005_timespec时间结构.md#ae3c7510dafa8cbcaede866ed13c99683)
- [timespec::tv_sec](../time_headers_reference/P005_timespec时间结构.md#afc3302668d7cb5952f590da69fdd4955)
- [ucontext_t::uc_stack](../posix_system_model_reference/P027_ucontext_t_结构体.md#a2dc143fa6b3f0fa8d0f27acbfaed0d9e)
- [ucontext_t::uc_link](../posix_system_model_reference/P027_ucontext_t_结构体.md#a7210eb8a464c276b9c68e749b3aa28f1)
- [ucontext_t::uc_mcontext](../posix_system_model_reference/P027_ucontext_t_结构体.md#a7f8c7406758045ea8be9dd61831f16f2)
- [ucontext_t::uc_sigmask](../posix_system_model_reference/P027_ucontext_t_结构体.md#aabde4c64c7bcf764e937361d8c341504)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [sigval::sival_ptr](../posix_system_model_reference/P035_sigval_联合体.md#a4668f1bd7463de7b70bd0022207e26ac)
- [sigval::sival_int](../posix_system_model_reference/P035_sigval_联合体.md#a560393252ee7edc37df44bf1c11bdbdd)

---

[上一章](P007_parser.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P009_wifi_mgmt.h_源码浏览.md)
