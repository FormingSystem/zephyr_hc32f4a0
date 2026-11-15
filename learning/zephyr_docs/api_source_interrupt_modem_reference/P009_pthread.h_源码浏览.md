---
id: learning.zephyr-docs.api-source-interrupt-modem-reference.page-9
title: pthread.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_pthread.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html)。

## 9.1\_原始可见代码（Source Code）

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
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00149"></a>
<a id="l00150"></a>
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
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00270"></a>
<a id="l00271"></a>
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
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00330"></a>
<a id="l00331"></a>
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
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
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
<a id="foldopen00471"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="foldopen00476"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="akernel_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aposix_2sched_8h_html"></a>
<a id="aposix__signal_8h_html_ab3f45e72c67ecc7866d14ab09b3367e7"></a>
<a id="aposix__time_8h_html_a6bb3206700910111f26e946bfbf0f2af"></a>
<a id="aposix__types_8h_html_a1b893f49dfdf497be09c04a0e40f425e"></a>
<a id="aposix__types_8h_html_a1d9c308dd59bf38ff0a7a45020d0aefa"></a>
<a id="aposix__types_8h_html_a2489174ff5737a33443b0959f4278765"></a>
<a id="aposix__types_8h_html_a24d58850626c8022bf4bbd5d2628615b"></a>
<a id="aposix__types_8h_html_a2603a6fda916554839174bc7d8849297"></a>
<a id="aposix__types_8h_html_a465eb2b962de164efdc8ce957025de7e"></a>
<a id="aposix__types_8h_html_a4e92e3fbb4be682babbb6796af90b50f"></a>
<a id="aposix__types_8h_html_a8fd226393057ab7a8b17ac1c8b061911"></a>
<a id="aposix__types_8h_html_a9f62774a7a4e1634e60fb611765251f1"></a>
<a id="aposix__types_8h_html_acd12f65541fede33b6226f646e900ea6"></a>
<a id="aposix__types_8h_html_aeb637552f63e4c249e7aaeb2905f3db2"></a>
<a id="apthread_8h_html_a01159da320b2317ee286a7e92d713f16"></a>
<a id="apthread_8h_html_a02a3c64dac70730e226c31c0e7dbb45c"></a>
<a id="apthread_8h_html_a065b618f7b786ed9bc7dddef4490cefb"></a>
<a id="apthread_8h_html_a0b85ebb1e3aac081a4c0a5e85ae3cbe9"></a>
<a id="apthread_8h_html_a1596a13569ec35ee66cc867586fd643d"></a>
<a id="apthread_8h_html_a16c935f2f6146a95f9adbca71e0455e7"></a>
<a id="apthread_8h_html_a18b9aa91fe20481a25650df20c567ff5"></a>
<a id="apthread_8h_html_a200fcbc9157e6183376f83bc0e5937dd"></a>
<a id="apthread_8h_html_a2187333dd46ce08d9d2e044f79fad705"></a>
<a id="apthread_8h_html_a2321aabf58224b06021185708d0f9658"></a>
<a id="apthread_8h_html_a2a460fe3d4e4518057366f6ead455f4a"></a>
<a id="apthread_8h_html_a319a61cdb25d069c9d4504e8225fd0c3"></a>
<a id="apthread_8h_html_a32dd5d2994c5ca7dd33294ce8cbd13bf"></a>
<a id="apthread_8h_html_a37075410fbbaad7ee93c95375fc86e0e"></a>
<a id="apthread_8h_html_a391c34da42e68ddd24f5ee0c070d5c4f"></a>
<a id="apthread_8h_html_a46064892e8c4622e0a3ebe22d9792b92"></a>
<a id="apthread_8h_html_a4a15369dee1898e5bb06c538c66aca7a"></a>
<a id="apthread_8h_html_a4bcdbf47c17c7dcc51e9f05f5cb56d81"></a>
<a id="apthread_8h_html_a4c4f5f3b4f8f45d9d897847d53b11aaa"></a>
<a id="apthread_8h_html_a532b31c11a9d87663053c5342400758c"></a>
<a id="apthread_8h_html_a54e367403c0524680115b780ccfbc586"></a>
<a id="apthread_8h_html_a5ca1dea9ea7d3cfb34a9c8561e47cf02"></a>
<a id="apthread_8h_html_a5ddd4cc028257f9baa9e23c2337abe3b"></a>
<a id="apthread_8h_html_a5e27d4773f3d0552e36f2ff3b922a988"></a>
<a id="apthread_8h_html_a61a1bf88d32de361e82ef4ea99b47322"></a>
<a id="apthread_8h_html_a66a8f4bac5afe05538794218ff7c85ea"></a>
<a id="apthread_8h_html_a6d8d320a882ba044a064975dddcf9ced"></a>
<a id="apthread_8h_html_a6e4d503c2b358be5c98330f9006b3417"></a>
<a id="apthread_8h_html_a742eefdf61f97bf1607d15a4fa2a3173"></a>
<a id="apthread_8h_html_a77376b018eec6db2986939b847915a3c"></a>
<a id="apthread_8h_html_a78a54e67f0afe2601dbda0a904fa0bdf"></a>
<a id="apthread_8h_html_a7948bc0ea8a33439aece34d0fb3daf8b"></a>
<a id="apthread_8h_html_a79839f0f4f4a768bf6d218faf377c209"></a>
<a id="apthread_8h_html_a79a77b688c30213e5e52e6be178cde4e"></a>
<a id="apthread_8h_html_a79b4c9e71486a87ef3014f1c660b33eb"></a>
<a id="apthread_8h_html_a7a23cbcfc21a4e3edf531ed65f022370"></a>
<a id="apthread_8h_html_a7c275c509c26566b6dd95a2de1668a2f"></a>
<a id="apthread_8h_html_a7d3b987d99117fc10c4ef97230011983"></a>
<a id="apthread_8h_html_a7f064a4db96a009a5a9a7c7e5cc03599"></a>
<a id="apthread_8h_html_a80008474c3d68e9880da960a53d2f430"></a>
<a id="apthread_8h_html_a812a9a455ae2ef2bb0dca4fff201a281"></a>
<a id="apthread_8h_html_a8387c80e660e9426f801ac0217ecfae5"></a>
<a id="apthread_8h_html_a8d44e4eae235f675bbab1b9163a3bc1d"></a>
<a id="apthread_8h_html_a8d55a60492c979991dc1a361b5453813"></a>
<a id="apthread_8h_html_a91ff7fff67462ce9216d299c89683119"></a>
<a id="apthread_8h_html_a94ede89b99a3a4fa17e516d30aaf3409"></a>
<a id="apthread_8h_html_a9d831af0179ed16d1b6cbeba0304810b"></a>
<a id="apthread_8h_html_aa21465e084e7185bfbb94bb50d60cd08"></a>
<a id="apthread_8h_html_aa9c3c335f5bcf702fe85a1c12dcdc70e"></a>
<a id="apthread_8h_html_aab579bcfcf0662a0c1e35fd82162e61d"></a>
<a id="apthread_8h_html_aae52fb1d3e6d03b18fa5731d0b49d197"></a>
<a id="apthread_8h_html_ab05ae13769e61dea9c53ca7894743c8f"></a>
<a id="apthread_8h_html_ab9a027122b38833e8c2e1c0e733da3e6"></a>
<a id="apthread_8h_html_abbec44a62531009629601fbb34f1027c"></a>
<a id="apthread_8h_html_abcd67baa86ff65d7ce65985d8b50d579"></a>
<a id="apthread_8h_html_abee3ae43d1f00b597111f6f82b0416a1"></a>
<a id="apthread_8h_html_ac0b4f6d49deeab0ddb269a23ee303156"></a>
<a id="apthread_8h_html_ac60393667965dbd06670d3d280b65757"></a>
<a id="apthread_8h_html_acc16fb32464b480d31bc69cce4e206c9"></a>
<a id="apthread_8h_html_acc1ccbaf3d76572da85a8030bba1ede4"></a>
<a id="apthread_8h_html_acdf9f73a16ea40eba1bc174d38e76ca5"></a>
<a id="apthread_8h_html_ad3fe01698c4fad85bb5cc3f9a2e82ea3"></a>
<a id="apthread_8h_html_ad437fe8caa3ef9f0cb7d69f6f6479df9"></a>
<a id="apthread_8h_html_ad540451ab679ace869b51c7cbb7b8486"></a>
<a id="apthread_8h_html_ad791558625e69852e4a435b7c1580468"></a>
<a id="apthread_8h_html_ad8e89d31b56c88d632ba9aeb956fa043"></a>
<a id="apthread_8h_html_adcf534f63e3c1e209befc503d5a3db74"></a>
<a id="apthread_8h_html_add1fea97e50755b5dbf4bd9a83b710dd"></a>
<a id="apthread_8h_html_ae23600d4670359ab12bfba20db2c9a37"></a>
<a id="apthread_8h_html_ae6550aa6aede71f618bb7457f3e50524"></a>
<a id="apthread_8h_html_ae6ee78c307d8467b34a9b0c330993a54"></a>
<a id="apthread_8h_html_ae7e6584c2b2cf9b9ff061115d2342bb5"></a>
<a id="apthread_8h_html_aec19ad460995a9fe8aeb4eaf2bb1ed1d"></a>
<a id="apthread_8h_html_aecc6c99901aac517072970e153863296"></a>
<a id="apthread_8h_html_aecea498fbd2df02942790e5ccd7d78b2"></a>
<a id="apthread_8h_html_aee96306dc79294927ee840bb4de2244b"></a>
<a id="apthread_8h_html_af032906f326f3c209c7eed6bb248ebee"></a>
<a id="apthread_8h_html_af1c95282ab2bea25f0888a19652cd41f"></a>
<a id="apthread_8h_html_af37eaf73f0d83989d8efc06e676909f1"></a>
<a id="apthread_8h_html_af786372165ba080986ae4143928c5436"></a>
<a id="apthread_8h_html_af89d9cfa300f33b46720a96eac83d175"></a>
<a id="apthread_8h_html_af98f6b6c483077a39d1400b1de1577b8"></a>
<a id="apthread_8h_html_afb4344ea91774ba279ea5df3cb656ebc"></a>
<a id="apthread_8h_html_afd70d6f2c50e22b996c926fb9d6ad291"></a>
<a id="astdlib_8h_html"></a>
<a id="astring_8h_html"></a>
<a id="astructpthread__attr__t_html"></a>
<a id="astructpthread__once_html"></a>
<a id="astructtimespec_html"></a>
<a id="aunistd_8h_html"></a>

```c
/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_POSIX_PTHREAD_H_
#define ZEPHYR_INCLUDE_POSIX_PTHREAD_H_

#include <stdlib.h>
#include <string.h>
#include <time.h>

#include <zephyr/kernel.h>
#include <zephyr/posix/unistd.h>
#include <zephyr/posix/sched.h>

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Pthread detach/joinable
 * Undefine possibly predefined values by external toolchain headers
 */
#undef PTHREAD_CREATE_DETACHED
#define PTHREAD_CREATE_DETACHED 1
#undef PTHREAD_CREATE_JOINABLE
#define PTHREAD_CREATE_JOINABLE 0

/* Pthread resource visibility */
#define PTHREAD_PROCESS_PRIVATE 0
#define PTHREAD_PROCESS_SHARED  1

/* Pthread cancellation */
#define PTHREAD_CANCELED       ((void *)-1)
#define PTHREAD_CANCEL_ENABLE  0
#define PTHREAD_CANCEL_DISABLE 1
#define PTHREAD_CANCEL_DEFERRED     0
#define PTHREAD_CANCEL_ASYNCHRONOUS 1

/* Pthread scope */
#undef PTHREAD_SCOPE_PROCESS
#define PTHREAD_SCOPE_PROCESS    1
#undef PTHREAD_SCOPE_SYSTEM
#define PTHREAD_SCOPE_SYSTEM     0

/* Pthread inherit scheduler */
#undef PTHREAD_INHERIT_SCHED
#define PTHREAD_INHERIT_SCHED  0
#undef PTHREAD_EXPLICIT_SCHED
#define PTHREAD_EXPLICIT_SCHED 1

/* Passed to pthread_once */
#define PTHREAD_ONCE_INIT {0}

/* The minimum allowable stack size */
#define PTHREAD_STACK_MIN K_KERNEL_STACK_LEN(0)

#define PTHREAD_COND_INITIALIZER (-1)

int pthread_cond_init(pthread_cond_t *cv, const pthread_condattr_t *att);

int pthread_cond_destroy(pthread_cond_t *cv);

int pthread_cond_signal(pthread_cond_t *cv);

int pthread_cond_broadcast(pthread_cond_t *cv);

int pthread_cond_wait(pthread_cond_t *cv, pthread_mutex_t *mut);

int pthread_cond_timedwait(pthread_cond_t *cv, pthread_mutex_t *mut,
                           const struct timespec *abstime);

int pthread_condattr_init(pthread_condattr_t *att);

int pthread_condattr_destroy(pthread_condattr_t *att);

int pthread_condattr_getclock(const pthread_condattr_t *ZRESTRICT att,
                clockid_t *ZRESTRICT clock_id);


int pthread_condattr_setclock(pthread_condattr_t *att, clockid_t clock_id);

#define PTHREAD_MUTEX_INITIALIZER (-1)

#define PTHREAD_RWLOCK_INITIALIZER (-1)

/*
 *  Mutex attributes - type
 *
 *  PTHREAD_MUTEX_NORMAL: Owner of mutex cannot relock it. Attempting
 *      to relock will cause deadlock.
 *  PTHREAD_MUTEX_RECURSIVE: Owner can relock the mutex.
 *  PTHREAD_MUTEX_ERRORCHECK: If owner attempts to relock the mutex, an
 *      error is returned.
 *
 */
#define PTHREAD_MUTEX_NORMAL        0
#define PTHREAD_MUTEX_RECURSIVE     1
#define PTHREAD_MUTEX_ERRORCHECK    2
#define PTHREAD_MUTEX_DEFAULT       PTHREAD_MUTEX_NORMAL

/*
 *  Mutex attributes - protocol
 *
 *  PTHREAD_PRIO_NONE: Ownership of mutex does not affect priority.
 *  PTHREAD_PRIO_INHERIT: Owner's priority is boosted to the priority of
 *      highest priority thread blocked on the mutex.
 *  PTHREAD_PRIO_PROTECT:  Mutex has a priority ceiling.  The owner's
 *      priority is boosted to the highest priority ceiling of all mutexes
 *      owned (regardless of whether or not other threads are blocked on
 *      any of these mutexes).
 *  FIXME: Only PRIO_NONE is supported. Implement other protocols.
 */
#define PTHREAD_PRIO_NONE           0
#define PTHREAD_PRIO_INHERIT        1
#define PTHREAD_PRIO_PROTECT        2

int pthread_mutex_destroy(pthread_mutex_t *m);

int pthread_mutex_lock(pthread_mutex_t *m);

int pthread_mutex_unlock(pthread_mutex_t *m);


int pthread_mutex_timedlock(pthread_mutex_t *m,
                            const struct timespec *abstime);

int pthread_mutex_trylock(pthread_mutex_t *m);

int pthread_mutex_init(pthread_mutex_t *m,
                                     const pthread_mutexattr_t *att);

int pthread_mutexattr_setprotocol(pthread_mutexattr_t *attr, int protocol);

int pthread_mutexattr_settype(pthread_mutexattr_t *attr, int type);

int pthread_mutexattr_getprotocol(const pthread_mutexattr_t *attr,
                                  int *protocol);

int pthread_mutexattr_gettype(const pthread_mutexattr_t *attr, int *type);

int pthread_mutexattr_init(pthread_mutexattr_t *attr);

int pthread_mutexattr_destroy(pthread_mutexattr_t *attr);

#define PTHREAD_BARRIER_SERIAL_THREAD 1

/*
 *  Barrier attributes - type
 */
#define PTHREAD_PROCESS_PRIVATE         0
#define PTHREAD_PROCESS_PUBLIC          1

int pthread_barrier_wait(pthread_barrier_t *b);

int pthread_barrier_init(pthread_barrier_t *b, const pthread_barrierattr_t *attr,
                         unsigned int count);

int pthread_barrier_destroy(pthread_barrier_t *b);

int pthread_barrierattr_init(pthread_barrierattr_t *b);

int pthread_barrierattr_destroy(pthread_barrierattr_t *b);

int pthread_barrierattr_setpshared(pthread_barrierattr_t *attr, int pshared);

int pthread_barrierattr_getpshared(const pthread_barrierattr_t *ZRESTRICT attr,
                                   int *ZRESTRICT pshared);

/* Predicates and setters for various pthread attribute values that we
 * don't support (or always support: the "process shared" attribute
 * can only be true given the way Zephyr implements these
 * objects). Leave these undefined for simplicity instead of defining
 * stubs to return an error that would have to be logged and
 * interpreted just to figure out that we didn't support it in the
 * first place. These APIs are very rarely used even in production
 * Unix code.  Leave the declarations here so they can be easily
 * uncommented and implemented as needed.

int pthread_condattr_getpshared(const pthread_condattr_t * int *);
int pthread_condattr_setpshared(pthread_condattr_t *, int);
int pthread_mutex_consistent(pthread_mutex_t *);
int pthread_mutexattr_getpshared(const pthread_mutexattr_t * int *);
int pthread_mutexattr_getrobust(const pthread_mutexattr_t * int *);
int pthread_mutexattr_setpshared(pthread_mutexattr_t *, int);
int pthread_mutexattr_setrobust(pthread_mutexattr_t *, int);
*/

#ifdef CONFIG_POSIX_THREAD_PRIO_PROTECT
int pthread_mutex_getprioceiling(const pthread_mutex_t *ZRESTRICT mutex,
                                 int *ZRESTRICT prioceiling);
int pthread_mutex_setprioceiling(pthread_mutex_t *ZRESTRICT mutex, int prioceiling,
                                 int *ZRESTRICT old_ceiling);
int pthread_mutexattr_getprioceiling(const pthread_mutexattr_t *ZRESTRICT attr,
                                     int *ZRESTRICT prioceiling);
int pthread_mutexattr_setprioceiling(pthread_mutexattr_t *attr, int prioceiling);
#endif /* CONFIG_POSIX_THREAD_PRIO_PROTECT */

/* Base Pthread related APIs */

pthread_t pthread_self(void);

int pthread_equal(pthread_t pt1, pthread_t pt2);

int pthread_rwlockattr_destroy(pthread_rwlockattr_t *attr);

int pthread_rwlockattr_init(pthread_rwlockattr_t *attr);

int pthread_rwlockattr_getpshared(const pthread_rwlockattr_t *ZRESTRICT attr,
                                  int *ZRESTRICT pshared);
int pthread_rwlockattr_setpshared(pthread_rwlockattr_t *attr, int pshared);

int pthread_attr_getguardsize(const pthread_attr_t *ZRESTRICT attr, size_t *ZRESTRICT guardsize);
int pthread_attr_getstacksize(const pthread_attr_t *attr, size_t *stacksize);
int pthread_attr_setguardsize(pthread_attr_t *attr, size_t guardsize);
int pthread_attr_setstacksize(pthread_attr_t *attr, size_t stacksize);
int pthread_attr_setschedpolicy(pthread_attr_t *attr, int policy);
int pthread_attr_getschedpolicy(const pthread_attr_t *attr, int *policy);
int pthread_attr_setdetachstate(pthread_attr_t *attr, int detachstate);
int pthread_attr_getdetachstate(const pthread_attr_t *attr, int *detachstate);
int pthread_attr_init(pthread_attr_t *attr);
int pthread_attr_destroy(pthread_attr_t *attr);
int pthread_attr_getschedparam(const pthread_attr_t *attr,
                               struct sched_param *schedparam);
int pthread_getschedparam(pthread_t pthread, int *policy,
                          struct sched_param *param);
int pthread_attr_getstack(const pthread_attr_t *attr,
                          void **stackaddr, size_t *stacksize);
int pthread_attr_setstack(pthread_attr_t *attr, void *stackaddr,
                          size_t stacksize);
int pthread_attr_getscope(const pthread_attr_t *attr, int *contentionscope);
int pthread_attr_setscope(pthread_attr_t *attr, int contentionscope);
int pthread_attr_getinheritsched(const pthread_attr_t *attr, int *inheritsched);
int pthread_attr_setinheritsched(pthread_attr_t *attr, int inheritsched);
#ifdef CONFIG_POSIX_THREADS
int pthread_once(pthread_once_t *once, void (*initFunc)(void));
#endif
FUNC_NORETURN void pthread_exit(void *retval);
int pthread_timedjoin_np(pthread_t thread, void **status, const struct timespec *abstime);
int pthread_tryjoin_np(pthread_t thread, void **status);
int pthread_join(pthread_t thread, void **status);
int pthread_cancel(pthread_t pthread);
int pthread_detach(pthread_t thread);
int pthread_create(pthread_t *newthread, const pthread_attr_t *attr,
                   void *(*threadroutine)(void *arg), void *arg);
int pthread_setcancelstate(int state, int *oldstate);
int pthread_setcanceltype(int type, int *oldtype);
void pthread_testcancel(void);
int pthread_attr_setschedparam(pthread_attr_t *attr,
                               const struct sched_param *schedparam);
int pthread_setschedparam(pthread_t pthread, int policy,
                          const struct sched_param *param);
int pthread_setschedprio(pthread_t thread, int prio);
int pthread_rwlock_destroy(pthread_rwlock_t *rwlock);
int pthread_rwlock_init(pthread_rwlock_t *rwlock,
                        const pthread_rwlockattr_t *attr);
int pthread_rwlock_rdlock(pthread_rwlock_t *rwlock);
int pthread_rwlock_timedrdlock(pthread_rwlock_t *rwlock,
                               const struct timespec *abstime);
int pthread_rwlock_timedwrlock(pthread_rwlock_t *rwlock,
                               const struct timespec *abstime);
int pthread_rwlock_tryrdlock(pthread_rwlock_t *rwlock);
int pthread_rwlock_trywrlock(pthread_rwlock_t *rwlock);
int pthread_rwlock_unlock(pthread_rwlock_t *rwlock);
int pthread_rwlock_wrlock(pthread_rwlock_t *rwlock);
int pthread_key_create(pthread_key_t *key,
                void (*destructor)(void *value));
int pthread_key_delete(pthread_key_t key);
int pthread_setspecific(pthread_key_t key, const void *value);
void *pthread_getspecific(pthread_key_t key);
int pthread_atfork(void (*prepare)(void), void (*parent)(void), void (*child)(void));
int pthread_getconcurrency(void);
int pthread_setconcurrency(int new_level);

void __z_pthread_cleanup_push(void *cleanup[3], void (*routine)(void *arg), void *arg);
void __z_pthread_cleanup_pop(int execute);

#define pthread_cleanup_push(_rtn, _arg)                                                           \
        do /* enforce '{'-like behaviour */ {                                                      \
                void *_z_pthread_cleanup[3];                                                       \
                __z_pthread_cleanup_push(_z_pthread_cleanup, _rtn, _arg)

#define pthread_cleanup_pop(_ex)                                                                   \
                __z_pthread_cleanup_pop(_ex);                                                      \
        } /* enforce '}'-like behaviour */ while (0)

/* Glibc / Oracle Extension Functions */

int pthread_setname_np(pthread_t thread, const char *name);

int pthread_getname_np(pthread_t thread, char *name, size_t len);

#ifdef CONFIG_POSIX_THREADS

int pthread_spin_destroy(pthread_spinlock_t *lock);

int pthread_spin_init(pthread_spinlock_t *lock, int pshared);

int pthread_spin_lock(pthread_spinlock_t *lock);

int pthread_spin_trylock(pthread_spinlock_t *lock);

int pthread_spin_unlock(pthread_spinlock_t *lock);

#endif

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_PTHREAD_H_ */
```

## 9.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 22 行

POSIX 线程（Pthread）的分离／可连接状态（detach/joinable）。取消外部工具链头文件可能已预定义的值。

### 注释 3：原第 31 行

POSIX 线程（Pthread）的资源可见性（resource visibility）。

### 注释 4：原第 35 行

POSIX 线程取消（Pthread cancellation）。

### 注释 5：原第 42 行

POSIX 线程作用域（Pthread scope）。

### 注释 6：原第 48 行

POSIX 线程继承调度器（Pthread inherit scheduler）。

### 注释 7：原第 54 行

传给 `pthread_once` 的值。

### 注释 8：原第 57 行

允许的最小栈大小（minimum stack size）。

### 注释 9：原第 158 行

互斥锁属性：类型（Mutex attributes — type）。

- `PTHREAD_MUTEX_NORMAL`：拥有者不能再次锁定此互斥锁；尝试重新加锁会造成死锁（deadlock）。
- `PTHREAD_MUTEX_RECURSIVE`：拥有者可以再次锁定此互斥锁。
- `PTHREAD_MUTEX_ERRORCHECK`：拥有者尝试重新加锁时返回错误。

### 注释 10：原第 173 行

互斥锁属性：协议（Mutex attributes — protocol）。

- `PTHREAD_PRIO_NONE`：持有互斥锁不影响优先级。
- `PTHREAD_PRIO_INHERIT`：拥有者的优先级提升至阻塞在此锁上的最高优先级线程的优先级。
- `PTHREAD_PRIO_PROTECT`：互斥锁具有优先级上限（priority ceiling）；拥有者的优先级提升至其持有的全部互斥锁中最高的优先级上限，无论其他线程是否阻塞在这些锁上。

待修复（FIXME）：目前仅支持 `PRIO_NONE`，还需实现其他协议。

### 注释 11：原第 283 行

屏障属性：类型（Barrier attributes — type）。

### 注释 12：原第 340 行

以下函数用于查询和设置各种 pthread 属性值，而这些属性目前不受支持，或者始终受支持：根据 Zephyr 实现这些对象的方式，“进程共享”（process shared）属性只能为真。为简化处理，保留这些函数为未定义状态，而不提供返回错误的桩函数（stubs），以免调用方还需要记录和解释错误，才能得知原本就不支持这些功能。即使在生产环境的 Unix 代码中，这些 API 也很少使用。此处保留声明，方便按需取消注释并实现。下方保留原始声明。

```c
int pthread_condattr_getpshared(const pthread_condattr_t * int *);
int pthread_condattr_setpshared(pthread_condattr_t *, int);
int pthread_mutex_consistent(pthread_mutex_t *);
int pthread_mutexattr_getpshared(const pthread_mutexattr_t * int *);
int pthread_mutexattr_getrobust(const pthread_mutexattr_t * int *);
int pthread_mutexattr_setpshared(pthread_mutexattr_t *, int);
int pthread_mutexattr_setrobust(pthread_mutexattr_t *, int);
```

### 注释 13：原第 367 行

条件编译配置（Configuration）标记：`CONFIG_POSIX_THREAD_PRIO_PROTECT`。

### 注释 14：原第 369 行

基本 POSIX 线程相关 API（Base Pthread related APIs）。

### 注释 15：原第 472 行

强制实现类似 `{` 的行为。

### 注释 16：原第 478 行

强制实现类似 `}` 的行为。

### 注释 17：原第 480 行

Glibc／Oracle 扩展函数（Extension Functions）。

### 注释 18：原第 558 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_PTHREAD_H_`。

## 9.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html)
- [stdlib.h](../api_file_reference/P410_____w__zephyr__zephyr__lib__libc__minimal__include__stdlib.h_文件参考.md)
- [string.h](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/posix/unistd.h](../api_file_reference/P492_zephyr__posix__unistd.h_文件参考.md)
- [zephyr/posix/sched.h](../api_file_configuration_reference/P061_zephyr__posix__sched.h_文件参考.md)
- [pthread_cond_init](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a319a61cdb25d069c9d4504e8225fd0c3)
- [pthread_cond_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a1b893f49dfdf497be09c04a0e40f425e)
- [pthread_condattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a9f62774a7a4e1634e60fb611765251f1)
- [pthread_cond_destroy](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a8d44e4eae235f675bbab1b9163a3bc1d)
- [pthread_cond_signal](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#add1fea97e50755b5dbf4bd9a83b710dd)
- [pthread_cond_broadcast](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a91ff7fff67462ce9216d299c89683119)
- [pthread_cond_wait](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a61a1bf88d32de361e82ef4ea99b47322)
- [pthread_mutex_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a465eb2b962de164efdc8ce957025de7e)
- [pthread_cond_timedwait](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#aecea498fbd2df02942790e5ccd7d78b2)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [pthread_condattr_init](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a01159da320b2317ee286a7e92d713f16)
- [pthread_condattr_destroy](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#af37eaf73f0d83989d8efc06e676909f1)
- [pthread_condattr_getclock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a77376b018eec6db2986939b847915a3c)
- [clockid_t](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a6bb3206700910111f26e946bfbf0f2af)
- [pthread_condattr_setclock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ac0b4f6d49deeab0ddb269a23ee303156)
- [pthread_mutex_destroy](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#af89d9cfa300f33b46720a96eac83d175)
- [pthread_mutex_lock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#afd70d6f2c50e22b996c926fb9d6ad291)
- [pthread_mutex_unlock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a02a3c64dac70730e226c31c0e7dbb45c)
- [pthread_mutex_timedlock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#abbec44a62531009629601fbb34f1027c)
- [pthread_mutex_trylock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#acc1ccbaf3d76572da85a8030bba1ede4)
- [pthread_mutex_init](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a7948bc0ea8a33439aece34d0fb3daf8b)
- [pthread_mutexattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a2489174ff5737a33443b0959f4278765)
- [pthread_mutexattr_setprotocol](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ae7e6584c2b2cf9b9ff061115d2342bb5)
- [pthread_mutexattr_settype](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a8387c80e660e9426f801ac0217ecfae5)
- [pthread_mutexattr_getprotocol](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a200fcbc9157e6183376f83bc0e5937dd)
- [pthread_mutexattr_gettype](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a7f064a4db96a009a5a9a7c7e5cc03599)
- [pthread_mutexattr_init](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#af98f6b6c483077a39d1400b1de1577b8)
- [pthread_mutexattr_destroy](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a2321aabf58224b06021185708d0f9658)
- [pthread_barrier_wait](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#af786372165ba080986ae4143928c5436)
- [pthread_barrier_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#aeb637552f63e4c249e7aaeb2905f3db2)
- [pthread_barrier_init](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#aecc6c99901aac517072970e153863296)
- [pthread_barrierattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a24d58850626c8022bf4bbd5d2628615b)
- [pthread_barrier_destroy](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ab05ae13769e61dea9c53ca7894743c8f)
- [pthread_barrierattr_init](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ad540451ab679ace869b51c7cbb7b8486)
- [pthread_barrierattr_destroy](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a5e27d4773f3d0552e36f2ff3b922a988)
- [pthread_barrierattr_setpshared](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#aa9c3c335f5bcf702fe85a1c12dcdc70e)
- [pthread_barrierattr_getpshared](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a54e367403c0524680115b780ccfbc586)
- [pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)
- [pthread_self](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a4c4f5f3b4f8f45d9d897847d53b11aaa)
- [pthread_equal](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a2a460fe3d4e4518057366f6ead455f4a)
- [pthread_rwlockattr_destroy](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a78a54e67f0afe2601dbda0a904fa0bdf)
- [pthread_rwlockattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a4e92e3fbb4be682babbb6796af90b50f)
- [pthread_rwlockattr_init](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a9d831af0179ed16d1b6cbeba0304810b)
- [pthread_rwlockattr_getpshared](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a5ca1dea9ea7d3cfb34a9c8561e47cf02)
- [pthread_rwlockattr_setpshared](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ae6550aa6aede71f618bb7457f3e50524)
- [pthread_attr_getguardsize](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#abee3ae43d1f00b597111f6f82b0416a1)
- [pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)
- [pthread_attr_getstacksize](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ae23600d4670359ab12bfba20db2c9a37)
- [pthread_attr_setguardsize](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a532b31c11a9d87663053c5342400758c)
- [pthread_attr_setstacksize](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a812a9a455ae2ef2bb0dca4fff201a281)
- [pthread_attr_setschedpolicy](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a79b4c9e71486a87ef3014f1c660b33eb)
- [pthread_attr_getschedpolicy](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#af032906f326f3c209c7eed6bb248ebee)
- [pthread_attr_setdetachstate](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ae6ee78c307d8467b34a9b0c330993a54)
- [pthread_attr_getdetachstate](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a391c34da42e68ddd24f5ee0c070d5c4f)
- [pthread_attr_init](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a0b85ebb1e3aac081a4c0a5e85ae3cbe9)
- [pthread_attr_destroy](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a4bcdbf47c17c7dcc51e9f05f5cb56d81)
- [pthread_attr_getschedparam](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#abcd67baa86ff65d7ce65985d8b50d579)
- [pthread_getschedparam](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ac60393667965dbd06670d3d280b65757)
- [pthread_attr_getstack](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#aec19ad460995a9fe8aeb4eaf2bb1ed1d)
- [pthread_attr_setstack](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a94ede89b99a3a4fa17e516d30aaf3409)
- [pthread_attr_getscope](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ad3fe01698c4fad85bb5cc3f9a2e82ea3)
- [pthread_attr_setscope](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a6d8d320a882ba044a064975dddcf9ced)
- [pthread_attr_getinheritsched](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a79a77b688c30213e5e52e6be178cde4e)
- [pthread_attr_setinheritsched](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ad437fe8caa3ef9f0cb7d69f6f6479df9)
- [pthread_once](../posix_system_model_reference/P015_pthread_once_结构体.md)
- [pthread_once_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a2603a6fda916554839174bc7d8849297)
- [pthread_exit](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ab9a027122b38833e8c2e1c0e733da3e6)
- [pthread_timedjoin_np](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a742eefdf61f97bf1607d15a4fa2a3173)
- [pthread_tryjoin_np](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a32dd5d2994c5ca7dd33294ce8cbd13bf)
- [pthread_join](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a6e4d503c2b358be5c98330f9006b3417)
- [pthread_cancel](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a66a8f4bac5afe05538794218ff7c85ea)
- [pthread_detach](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a7c275c509c26566b6dd95a2de1668a2f)
- [pthread_create](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#adcf534f63e3c1e209befc503d5a3db74)
- [pthread_setcancelstate](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a37075410fbbaad7ee93c95375fc86e0e)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [pthread_setcanceltype](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#aab579bcfcf0662a0c1e35fd82162e61d)
- [pthread_testcancel](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#af1c95282ab2bea25f0888a19652cd41f)
- [pthread_attr_setschedparam](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a18b9aa91fe20481a25650df20c567ff5)
- [pthread_setschedparam](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ad8e89d31b56c88d632ba9aeb956fa043)
- [pthread_setschedprio](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a7a23cbcfc21a4e3edf531ed65f022370)
- [pthread_rwlock_destroy](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a79839f0f4f4a768bf6d218faf377c209)
- [pthread_rwlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#acd12f65541fede33b6226f646e900ea6)
- [pthread_rwlock_init](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a1596a13569ec35ee66cc867586fd643d)
- [pthread_rwlock_rdlock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#acc16fb32464b480d31bc69cce4e206c9)
- [pthread_rwlock_timedrdlock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#ad791558625e69852e4a435b7c1580468)
- [pthread_rwlock_timedwrlock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a16c935f2f6146a95f9adbca71e0455e7)
- [pthread_rwlock_tryrdlock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#aae52fb1d3e6d03b18fa5731d0b49d197)
- [pthread_rwlock_trywrlock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a065b618f7b786ed9bc7dddef4490cefb)
- [pthread_rwlock_unlock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a7d3b987d99117fc10c4ef97230011983)
- [pthread_rwlock_wrlock](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a5ddd4cc028257f9baa9e23c2337abe3b)
- [pthread_key_create](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a4a15369dee1898e5bb06c538c66aca7a)
- [pthread_key_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a8fd226393057ab7a8b17ac1c8b061911)
- [pthread_key_delete](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#aee96306dc79294927ee840bb4de2244b)
- [pthread_setspecific](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a2187333dd46ce08d9d2e044f79fad705)
- [pthread_getspecific](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#acdf9f73a16ea40eba1bc174d38e76ca5)
- [pthread_atfork](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a80008474c3d68e9880da960a53d2f430)
- [pthread_getconcurrency](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#afb4344ea91774ba279ea5df3cb656ebc)
- [pthread_setconcurrency](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a46064892e8c4622e0a3ebe22d9792b92)
- [pthread_setname_np](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#aa21465e084e7185bfbb94bb50d60cd08)
- [pthread_getname_np](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html#a8d55a60492c979991dc1a361b5453813)
- [pthread_spinlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a1d9c308dd59bf38ff0a7a45020d0aefa)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [sched.h](../api_file_configuration_reference/P061_zephyr__posix__sched.h_文件参考.md)
- [unistd.h](../api_file_reference/P492_zephyr__posix__unistd.h_文件参考.md)

---

[上一章](P008_numicro_m48x_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P010_renesas_rztn_clock.h_源码浏览.md)
