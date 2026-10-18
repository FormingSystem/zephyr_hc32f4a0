---
id: learning.zephyr-docs.api-source-supplement-reference.page-15
title: arch_interface.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_arch\_interface.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html)。

## 15.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00055"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00093"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00202"></a>
<a id="l00207"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00283"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00328"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00589"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00657"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00661"></a>
<a id="l00678"></a>
<a id="l00679"></a>
<a id="l00680"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00689"></a>
<a id="l00694"></a>
<a id="l00696"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="l00718"></a>
<a id="l00719"></a>
<a id="l00725"></a>
<a id="l00726"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="l00737"></a>
<a id="l00738"></a>
<a id="l00739"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00751"></a>
<a id="l00752"></a>
<a id="l00757"></a>
<a id="l00781"></a>
<a id="l00782"></a>
<a id="l00784"></a>
<a id="l00790"></a>
<a id="l00791"></a>
<a id="l00792"></a>
<a id="l00793"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00827"></a>
<a id="l00828"></a>
<a id="l00829"></a>
<a id="l00841"></a>
<a id="l00842"></a>
<a id="l00843"></a>
<a id="l00856"></a>
<a id="l00857"></a>
<a id="l00858"></a>
<a id="l00859"></a>
<a id="l00873"></a>
<a id="l00874"></a>
<a id="l00875"></a>
<a id="l00876"></a>
<a id="l00891"></a>
<a id="l00892"></a>
<a id="l00893"></a>
<a id="l00894"></a>
<a id="l00895"></a>
<a id="l00911"></a>
<a id="l00912"></a>
<a id="l00913"></a>
<a id="l00914"></a>
<a id="l00915"></a>
<a id="l00921"></a>
<a id="l00922"></a>
<a id="l00928"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00952"></a>
<a id="l00953"></a>
<a id="l00954"></a>
<a id="l00972"></a>
<a id="l00973"></a>
<a id="l00974"></a>
<a id="l00992"></a>
<a id="l00993"></a>
<a id="l01008"></a>
<a id="l01009"></a>
<a id="l01027"></a>
<a id="l01028"></a>
<a id="l01029"></a>
<a id="l01042"></a>
<a id="l01043"></a>
<a id="l01044"></a>
<a id="l01045"></a>
<a id="l01074"></a>
<a id="l01075"></a>
<a id="l01091"></a>
<a id="l01092"></a>
<a id="l01111"></a>
<a id="l01112"></a>
<a id="l01113"></a>
<a id="l01128"></a>
<a id="l01129"></a>
<a id="l01142"></a>
<a id="l01143"></a>
<a id="l01144"></a>
<a id="l01185"></a>
<a id="foldopen01186"></a>
<a id="l01186"></a>
<a id="l01187"></a>
<a id="l01188"></a>
<a id="l01189"></a>
<a id="l01190"></a>
<a id="l01191"></a>
<a id="l01192"></a>
<a id="l01193"></a>
<a id="l01194"></a>
<a id="l01195"></a>
<a id="l01197"></a>
<a id="l01203"></a>
<a id="l01204"></a>
<a id="l01205"></a>
<a id="l01206"></a>
<a id="l01212"></a>
<a id="l01213"></a>
<a id="l01219"></a>
<a id="l01220"></a>
<a id="l01226"></a>
<a id="l01227"></a>
<a id="l01241"></a>
<a id="l01242"></a>
<a id="l01256"></a>
<a id="l01257"></a>
<a id="l01272"></a>
<a id="l01273"></a>
<a id="l01274"></a>
<a id="l01289"></a>
<a id="l01290"></a>
<a id="l01291"></a>
<a id="l01304"></a>
<a id="l01305"></a>
<a id="l01306"></a>
<a id="l01319"></a>
<a id="l01320"></a>
<a id="l01321"></a>
<a id="l01329"></a>
<a id="l01330"></a>
<a id="l01331"></a>
<a id="l01333"></a>
<a id="l01334"></a>
<a id="l01335"></a>
<a id="l01336"></a>
<a id="l01347"></a>
<a id="l01355"></a>
<a id="l01356"></a>
<a id="l01369"></a>
<a id="l01370"></a>
<a id="l01383"></a>
<a id="l01384"></a>
<a id="l01411"></a>
<a id="l01412"></a>
<a id="l01427"></a>
<a id="l01428"></a>
<a id="l01429"></a>
<a id="l01437"></a>
<a id="l01438"></a>
<a id="l01447"></a>
<a id="l01448"></a>
<a id="l01458"></a>
<a id="l01459"></a>
<a id="l01467"></a>
<a id="l01468"></a>
<a id="l01470"></a>
<a id="l01471"></a>
<a id="l01472"></a>
<a id="l01473"></a>
<a id="l01474"></a>
<a id="l01475"></a>
<a id="l01476"></a>
<a id="l01477"></a>
<a id="l01487"></a>
<a id="l01488"></a>
<a id="l01489"></a>
<a id="l01490"></a>
<a id="l01501"></a>
<a id="l01502"></a>
<a id="l01503"></a>
<a id="l01504"></a>
<a id="l01505"></a>
<a id="l01506"></a>
<a id="l01507"></a>
<a id="l01516"></a>
<a id="l01517"></a>
<a id="l01529"></a>
<a id="l01537"></a>
<a id="l01538"></a>
<a id="l01554"></a>
<a id="l01555"></a>
<a id="l01556"></a>
<a id="l01558"></a>
<a id="l01559"></a>
<a id="l01560"></a>
<a id="l01561"></a>
<a id="l01562"></a>
<a id="l01563"></a>
<a id="l01564"></a>
<a id="l01565"></a>
<a id="l01566"></a>
<a id="l01567"></a>
<a id="aarch_2cpu_8h_html"></a>
<a id="aarch_2syscall_8h_html"></a>
<a id="aarch__inlines_8h_html"></a>
<a id="aarch__interface_8h_html_a3707e886593b0a8b4995309e4230b717"></a>
<a id="aarch__interface_8h_html_a9932b29bc0c3b86e4f8cbd6708ef5d9c"></a>
<a id="aarch__interface_8h_html_a9fc2dce533bd7b8cb1fdd4bdbb2b62b1"></a>
<a id="agroup__arch-gdbstub_html_ga0ef78d7e193e98549d9665632e53d5ca"></a>
<a id="agroup__arch-gdbstub_html_ga21c8a32d35c4d267b8306d595ff1d726"></a>
<a id="agroup__arch-gdbstub_html_ga2aa577d5e55c8b739e2be6187336aaf0"></a>
<a id="agroup__arch-gdbstub_html_ga5317106a8022bea2a0d42af0789cc016"></a>
<a id="agroup__arch-gdbstub_html_ga734041433f69030ad98439d10ef56ad6"></a>
<a id="agroup__arch-gdbstub_html_ga9c130421feeee919651828511743b346"></a>
<a id="agroup__arch-gdbstub_html_gaa3216e9f381f974c374a6399af5cdba5"></a>
<a id="agroup__arch-gdbstub_html_gab1111c30383cbf30d5eb66711c326642"></a>
<a id="agroup__arch-gdbstub_html_gab6f42110cf2340132bf2b3916810c01d"></a>
<a id="agroup__arch-gdbstub_html_gad717b520d774294bbda78a56cddcaeff"></a>
<a id="agroup__arch-irq_html_ga1b827afafc622d412962f568b78726dc"></a>
<a id="agroup__arch-irq_html_ga216d692e87bfba955a60f8e570e127df"></a>
<a id="agroup__arch-irq_html_ga25bca3069cb999b6d4f924b87bf7de38"></a>
<a id="agroup__arch-irq_html_ga3bd8e963a124421bb372dab4bdc6cd83"></a>
<a id="agroup__arch-irq_html_ga41483a9fc1090d96d066e107a74ee38c"></a>
<a id="agroup__arch-irq_html_ga5c85d7bf54a83190ed27587dc5a01de5"></a>
<a id="agroup__arch-irq_html_ga5f0942bd035c50c9d2d91ada472f37c4"></a>
<a id="agroup__arch-irq_html_ga6f5e4f7795c23586b13c5f6eaecac54d"></a>
<a id="agroup__arch-irq_html_gaa278d630653b33cb339621d725ed295a"></a>
<a id="agroup__arch-irq_html_gaa2b2745d8e99b8730b44805f4d3bbf05"></a>
<a id="agroup__arch-irq_html_gaa45f7cc9823e3a3b5f760ffc02323516"></a>
<a id="agroup__arch-irq_html_gaa4d733913e12a12e104dc4781cca7308"></a>
<a id="agroup__arch-irq_html_gaac8f60e7dfc5ce3222372798e96316ae"></a>
<a id="agroup__arch-irq_html_gaad2c939389164d483a472d4f6d201ce0"></a>
<a id="agroup__arch-irq_html_gab7c91d90ed8ccfce15c8bd040496f9ac"></a>
<a id="agroup__arch-irq_html_gae2a76360ce4ddcd461c06602ef16ba32"></a>
<a id="agroup__arch-mmu_html_gaa31a233dab4ad575a9a969de10965200"></a>
<a id="agroup__arch-pm_html_ga4d0297717c23a3cc5df434549e26924d"></a>
<a id="agroup__arch-pm_html_ga6ce051203e6cc091d0fb42a15f662a48"></a>
<a id="agroup__arch-pm_html_gab5e5f1690ef60723890b3d0b40b126d7"></a>
<a id="agroup__arch-pm_html_gadc25c1301f4fa3496361d0750c09cf4f"></a>
<a id="agroup__arch-smp_html_ga078e9bf1a4a557d1321ddc4848092cbe"></a>
<a id="agroup__arch-smp_html_ga32b7e543ce51498200c368c39c900bc8"></a>
<a id="agroup__arch-smp_html_ga4a9ac90ba7cc7c403472bfdaf3369ed2"></a>
<a id="agroup__arch-smp_html_ga5a7f0198ee061551c300129bffe64717"></a>
<a id="agroup__arch-smp_html_ga6ffc01f86f4541d1092ee4b277a07ac6"></a>
<a id="agroup__arch-smp_html_ga8fe90cec57c56993df14c0d545106ca3"></a>
<a id="agroup__arch-smp_html_gad42138d41dff6a4aad8abf7d77fcd8b2"></a>
<a id="agroup__arch-smp_html_gad628c89816128546501e3c26eaaf9dea"></a>
<a id="agroup__arch-smp_html_gadebac82c1ed0a8a08adb297738d2633e"></a>
<a id="agroup__arch-stackwalk_html_ga7129c254277cfa162cd9c5778a7662c2"></a>
<a id="agroup__arch-stackwalk_html_gaec9949df614728aa6d677f9f1fafd844"></a>
<a id="agroup__arch-timing_html_ga9ee9f897ec750957de45bf8d43349d5e"></a>
<a id="agroup__arch-timing_html_gacc1ed8d949f694a1d39e389334caf971"></a>
<a id="agroup__arch-userspace_html_ga0ba3ae2290827385b226ebdbf3de3b53"></a>
<a id="agroup__arch-userspace_html_ga13053a9233b86d5cd19dc3cea5804a16"></a>
<a id="agroup__arch-userspace_html_ga174c4f356fe315c523cefbf513858c9c"></a>
<a id="agroup__arch-userspace_html_ga1e78f1022aaf10e88727b142b56d4ef0"></a>
<a id="agroup__arch-userspace_html_ga306e9d0e5f8094cb75686f1c43d068a9"></a>
<a id="agroup__arch-userspace_html_ga447daa0454a90a7a3a247de01e522567"></a>
<a id="agroup__arch-userspace_html_ga48be2412ba65ec550ded63e2f1a0470f"></a>
<a id="agroup__arch-userspace_html_ga4cfb3b2b38e5afca889e8b9765d6c3df"></a>
<a id="agroup__arch-userspace_html_ga5e9ab24b9c980e327903fbe3f5bd97f3"></a>
<a id="agroup__arch-userspace_html_ga71542fcc679a94ad9ea60d7ac46da361"></a>
<a id="agroup__arch-userspace_html_ga89ab53a218add419e37f89c1f5fd955f"></a>
<a id="agroup__arch-userspace_html_ga9971c78bc8f579a0dadf84225dc0c3ff"></a>
<a id="agroup__arch-userspace_html_gaacb1c66a1b7bf2293fea269f6b5e1c7e"></a>
<a id="agroup__arch-userspace_html_gab5f05c76b315b6a8d1c3fd68abb8d594"></a>
<a id="agroup__arch-userspace_html_gac6cae2197637993a86b6ec6803b5742b"></a>
<a id="agroup__arch-userspace_html_gad53908f229d7e2c333574b009493644b"></a>
<a id="agroup__pcie__host__msi__interface_html_ga9ede6a7a472ee62f0975256a1b5f1231"></a>
<a id="agroup__timing__api__arch_html_ga026409e1dc323ceddb82b2a6f1cc7ca2"></a>
<a id="agroup__timing__api__arch_html_ga1f7bfb9ce0588f3b423c2a63933d40eb"></a>
<a id="agroup__timing__api__arch_html_ga44d3a7bd8b7008c9cd6c0524e97f128c"></a>
<a id="agroup__timing__api__arch_html_ga566483c64f5c5d2f0465e3f969303fd3"></a>
<a id="agroup__timing__api__arch_html_ga5d9923569b40437c28879ff4b3ff77c2"></a>
<a id="agroup__timing__api__arch_html_ga8424bc96c05dcae34b7ffd445e2916fe"></a>
<a id="agroup__timing__api__arch_html_ga925b4caff80f1dbac36531b479b24364"></a>
<a id="agroup__timing__api__arch_html_gad7a709477650c8596a96fe080f583fdd"></a>
<a id="agroup__timing__api__arch_html_gaf8cd88e81c2104b5eb0fbe42967b7834"></a>
<a id="ainclude_2zephyr_2timing_2types_8h_html"></a>
<a id="ainclude_2zephyr_2timing_2types_8h_html_a08ae2ef7b1cd6f125db0cb548ea1f0e2"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="airq__offload_8h_html"></a>
<a id="airq__offload_8h_html_a5bcf9956ddbf5ea75619f0cef91e1214"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructk__mem__domain_html"></a>
<a id="astructk__thread_html"></a>
<a id="astructmsi__vector_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2019 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ARCH_ARCH_INTERFACE_H_
#define ZEPHYR_INCLUDE_ARCH_ARCH_INTERFACE_H_

#ifndef _ASMLANGUAGE
#include <zephyr/toolchain.h>
#include <stddef.h>
#include <zephyr/types.h>
#include <zephyr/arch/cpu.h>
#include <zephyr/irq_offload.h>

#ifdef __cplusplus
extern "C" {
#endif

/* NOTE: We cannot pull in kernel.h here, need some forward declarations  */
struct arch_esf;
struct k_thread;
struct k_mem_domain;

typedef struct z_thread_stack_element k_thread_stack_t;

typedef void (*k_thread_entry_t)(void *p1, void *p2, void *p3);


static inline uint32_t arch_k_cycle_get_32(void);

static inline uint64_t arch_k_cycle_get_64(void);




#ifdef __DOXYGEN__
#define ARCH_THREAD_STACK_RESERVED
#endif

#ifdef __DOXYGEN__
#define ARCH_STACK_PTR_ALIGN
#endif

#ifdef __DOXYGEN__
#define ARCH_THREAD_STACK_OBJ_ALIGN(size)
#endif

#ifdef __DOXYGEN__
#define ARCH_THREAD_STACK_SIZE_ADJUST(size)
#endif

#ifdef __DOXYGEN__
#define ARCH_KERNEL_STACK_RESERVED
#endif

#ifdef __DOXYGEN__
#define ARCH_KERNEL_STACK_OBJ_ALIGN(size)
#endif



void arch_cpu_idle(void);

void arch_cpu_atomic_idle(unsigned int key);

unsigned int arch_pm_state_set_prepare(void);

void arch_pm_state_set_finish(unsigned int key);



typedef void (*arch_cpustart_t)(void *data);

void arch_cpu_start(int cpu_num, k_thread_stack_t *stack, int sz,
                    arch_cpustart_t fn, void *arg);

bool arch_cpu_active(int cpu_num);




static inline unsigned int arch_irq_lock(void);

static inline void arch_irq_unlock(unsigned int key);

static inline bool arch_irq_unlocked(unsigned int key);

static inline bool arch_cpu_irqs_are_enabled(void);

#ifdef CONFIG_ZERO_LATENCY_IRQS

static inline unsigned int arch_zli_lock(void);

static inline void arch_zli_unlock(unsigned int key);

#endif

void arch_irq_disable(unsigned int irq);

void arch_irq_enable(unsigned int irq);

int arch_irq_is_enabled(unsigned int irq);

#if defined(CONFIG_ARCH_HAS_IRQ_PENDING_OPS) || defined(__DOXYGEN__)
void arch_irq_clear_pending(unsigned int irq);

void arch_irq_set_pending(unsigned int irq);

bool arch_irq_is_pending(unsigned int irq);
#endif

#if defined(CONFIG_ARCH_HAS_IRQ_GET_ACTIVE) || defined(__DOXYGEN__)
unsigned int arch_irq_get_active(void);
#endif

int arch_irq_connect_dynamic(unsigned int irq, unsigned int priority,
                             void (*routine)(const void *parameter),
                             const void *parameter, uint32_t flags);

int arch_irq_disconnect_dynamic(unsigned int irq, unsigned int priority,
                                void (*routine)(const void *parameter),
                                const void *parameter, uint32_t flags);

#ifdef __DOXYGEN__
#define ARCH_IRQ_CONNECT(irq, pri, isr, arg, flags)
#endif

#ifdef __DOXYGEN__
#define ARCH_PCIE_IRQ_CONNECT(bdf, irq, pri, isr, arg, flags)
#endif

#ifdef __DOXYGEN__
#define ARCH_IRQ_DIRECT_CONNECT(irq_p, priority_p, isr_p, flags_p)
#endif

#ifdef __DOXYGEN__
#define ARCH_ISR_DIRECT_PM()
#endif

#ifdef __DOXYGEN__
#define ARCH_ISR_DIRECT_HEADER()
#endif

#ifdef __DOXYGEN__
#define ARCH_ISR_DIRECT_FOOTER(swap)
#endif

#ifdef __DOXYGEN__
#define ARCH_ISR_DIRECT_DECLARE(name)
#endif

unsigned int arch_irq_allocate(void);

void arch_irq_set_used(unsigned int irq);

bool arch_irq_is_used(unsigned int irq);

#ifdef __DOXYGEN__
#define ARCH_EXCEPT(reason_p)
#endif

#ifdef CONFIG_IRQ_OFFLOAD
void arch_irq_offload(irq_offload_routine_t routine, const void *parameter);


void arch_irq_offload_init(void);

#endif /* CONFIG_IRQ_OFFLOAD */


#ifdef CONFIG_SMP
static inline struct _cpu *arch_curr_cpu(void);


static inline uint32_t arch_proc_id(void);

void arch_sched_broadcast_ipi(void);

void arch_sched_directed_ipi(uint32_t cpu_bitmap);

int arch_smp_init(void);

#endif /* CONFIG_SMP */

static inline unsigned int arch_num_cpus(void);




int arch_page_phys_get(void *virt, uintptr_t *phys);



#ifdef CONFIG_USERSPACE
#include <zephyr/arch/syscall.h>

static inline uintptr_t arch_syscall_invoke0(uintptr_t call_id);

static inline uintptr_t arch_syscall_invoke1(uintptr_t arg1,
                                             uintptr_t call_id);

static inline uintptr_t arch_syscall_invoke2(uintptr_t arg1, uintptr_t arg2,
                                             uintptr_t call_id);

static inline uintptr_t arch_syscall_invoke3(uintptr_t arg1, uintptr_t arg2,
                                             uintptr_t arg3,
                                             uintptr_t call_id);

static inline uintptr_t arch_syscall_invoke4(uintptr_t arg1, uintptr_t arg2,
                                             uintptr_t arg3, uintptr_t arg4,
                                             uintptr_t call_id);

static inline uintptr_t arch_syscall_invoke5(uintptr_t arg1, uintptr_t arg2,
                                             uintptr_t arg3, uintptr_t arg4,
                                             uintptr_t arg5,
                                             uintptr_t call_id);

static inline uintptr_t arch_syscall_invoke6(uintptr_t arg1, uintptr_t arg2,
                                             uintptr_t arg3, uintptr_t arg4,
                                             uintptr_t arg5, uintptr_t arg6,
                                             uintptr_t call_id);

static inline bool arch_is_user_context(void);

int arch_mem_domain_max_partitions_get(void);

#ifdef CONFIG_ARCH_MEM_DOMAIN_DATA
int arch_mem_domain_init(struct k_mem_domain *domain);
#endif /* CONFIG_ARCH_MEM_DOMAIN_DATA */

int arch_mem_domain_deinit(struct k_mem_domain *domain);

#ifdef CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API
int arch_mem_domain_thread_add(struct k_thread *thread);

int arch_mem_domain_thread_remove(struct k_thread *thread);

int arch_mem_domain_partition_remove(struct k_mem_domain *domain,
                                     uint32_t partition_id);

int arch_mem_domain_partition_add(struct k_mem_domain *domain,
                                  uint32_t partition_id);
#endif /* CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API */

int arch_buffer_validate(const void *addr, size_t size, int write);

size_t arch_virt_region_align(uintptr_t phys, size_t size);

FUNC_NORETURN void arch_user_mode_enter(k_thread_entry_t user_entry,
                                        void *p1, void *p2, void *p3);

FUNC_NORETURN void arch_syscall_oops(void *ssf);

size_t arch_user_string_nlen(const char *s, size_t maxsize, int *err);
#endif /* CONFIG_USERSPACE */

#ifndef CONFIG_KERNEL_COHERENCE
static inline void arch_cohere_stacks(struct k_thread *old_thread,
                                      void *old_switch_handle,
                                      struct k_thread *new_thread)
{
        ARG_UNUSED(old_thread);
        ARG_UNUSED(old_switch_handle);
        ARG_UNUSED(new_thread);
}
#endif



#ifdef CONFIG_GDBSTUB
struct gdb_ctx;

void arch_gdb_init(void);

void arch_gdb_continue(void);

void arch_gdb_step(void);

size_t arch_gdb_reg_readall(struct gdb_ctx *ctx, uint8_t *buf, size_t buflen);

size_t arch_gdb_reg_writeall(struct gdb_ctx *ctx, uint8_t *hex, size_t hexlen);

size_t arch_gdb_reg_readone(struct gdb_ctx *ctx, uint8_t *buf, size_t buflen,
                            uint32_t regno);

size_t arch_gdb_reg_writeone(struct gdb_ctx *ctx, uint8_t *hex, size_t hexlen,
                             uint32_t regno);

int arch_gdb_add_breakpoint(struct gdb_ctx *ctx, uint8_t type,
                            uintptr_t addr, uint32_t kind);

int arch_gdb_remove_breakpoint(struct gdb_ctx *ctx, uint8_t type,
                               uintptr_t addr, uint32_t kind);

void arch_gdb_post_memory_write(uintptr_t addr, size_t len, uint8_t align);

#endif

#ifdef CONFIG_TIMING_FUNCTIONS
#include <zephyr/timing/types.h>


void arch_timing_init(void);

void arch_timing_start(void);

void arch_timing_stop(void);

timing_t arch_timing_counter_get(void);

uint64_t arch_timing_cycles_get(volatile timing_t *const start,
                                volatile timing_t *const end);

uint64_t arch_timing_freq_get(void);

uint64_t arch_timing_cycles_to_ns(uint64_t cycles);

uint64_t arch_timing_cycles_to_ns_avg(uint64_t cycles, uint32_t count);

uint32_t arch_timing_freq_get_mhz(void);


#endif /* CONFIG_TIMING_FUNCTIONS */

#ifdef CONFIG_PCIE_MSI_MULTI_VECTOR

struct msi_vector;
typedef struct msi_vector msi_vector_t;

uint8_t arch_pcie_msi_vectors_allocate(unsigned int priority,
                                       msi_vector_t *vectors,
                                       uint8_t n_vector);

bool arch_pcie_msi_vector_connect(msi_vector_t *vector,
                                  void (*routine)(const void *parameter),
                                  const void *parameter,
                                  uint32_t flags);

#endif /* CONFIG_PCIE_MSI_MULTI_VECTOR */

void arch_spin_relax(void);


typedef bool (*stack_trace_callback_fn)(void *cookie, unsigned long addr);

void arch_stack_walk(stack_trace_callback_fn callback_fn, void *cookie,
                     const struct k_thread *thread, const struct arch_esf *esf);


#ifdef __cplusplus
}
#endif /* __cplusplus */

#include <zephyr/arch/arch_inlines.h>

#endif /* _ASMLANGUAGE */

#endif /* ZEPHYR_INCLUDE_ARCH_ARCH_INTERFACE_H_ */
```

## 15.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 41 行

注意（NOTE）：此处不能包含 `kernel.h`，需要使用一些前向声明（Forward declarations）。

### 注释 3：原第 686 行

条件编译配置（Configuration）标记：`CONFIG_IRQ_OFFLOAD`。

### 注释 4：原第 738 行

条件编译配置（Configuration）标记：`CONFIG_SMP`。

### 注释 5：原第 953 行

条件编译配置（Configuration）标记：`CONFIG_ARCH_MEM_DOMAIN_DATA`。

### 注释 6：原第 1044 行

条件编译配置（Configuration）标记：`CONFIG_ARCH_MEM_DOMAIN_SYNCHRONOUS_API`。

### 注释 7：原第 1143 行

条件编译配置（Configuration）标记：`CONFIG_USERSPACE`。

### 注释 8：原第 1471 行

条件编译配置（Configuration）标记：`CONFIG_TIMING_FUNCTIONS`。

### 注释 9：原第 1506 行

条件编译配置（Configuration）标记：`CONFIG_PCIE_MSI_MULTI_VECTOR`。

### 注释 10：原第 1561 行

条件编译标记：`__cplusplus`。

### 注释 11：原第 1565 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 12：原第 1567 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_ARCH_INTERFACE_H_`。

## 15.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/arch/cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/arch_2cpu_8h.html)
- [zephyr/irq_offload.h](../fatal_irq_reference/P009_中断卸载头文件参考.md)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_mem_domain](../memory_domain_reference/P004_内存域结构.md)
- [k_thread_stack_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9fc2dce533bd7b8cb1fdd4bdbb2b62b1)
- [k_thread_entry_t](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a3707e886593b0a8b4995309e4230b717)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [arch_k_cycle_get_32](../timing_reference/P009_架构计数周期接口.md#ga9ee9f897ec750957de45bf8d43349d5e)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [arch_k_cycle_get_64](../timing_reference/P009_架构计数周期接口.md#gacc1ed8d949f694a1d39e389334caf971)
- [arch_cpu_idle](../arch_core_reference/P006_架构电源管理接口.md#ga6ce051203e6cc091d0fb42a15f662a48)
- [arch_cpu_atomic_idle](../arch_core_reference/P006_架构电源管理接口.md#ga4d0297717c23a3cc5df434549e26924d)
- [arch_pm_state_set_prepare](../arch_core_reference/P006_架构电源管理接口.md#gab5e5f1690ef60723890b3d0b40b126d7)
- [arch_pm_state_set_finish](../arch_core_reference/P006_架构电源管理接口.md#gadc25c1301f4fa3496361d0750c09cf4f)
- [arch_cpustart_t](../arch_core_reference/P005_架构多处理器接口.md#ga4a9ac90ba7cc7c403472bfdaf3369ed2)
- [arch_cpu_start](../arch_core_reference/P005_架构多处理器接口.md#ga32b7e543ce51498200c368c39c900bc8)
- [arch_cpu_active](../arch_core_reference/P005_架构多处理器接口.md#ga5a7f0198ee061551c300129bffe64717)
- [arch_irq_lock](../fatal_irq_reference/P008_架构中断接口.md#ga25bca3069cb999b6d4f924b87bf7de38)
- [arch_irq_unlock](../fatal_irq_reference/P008_架构中断接口.md#gaa2b2745d8e99b8730b44805f4d3bbf05)
- [arch_irq_unlocked](../fatal_irq_reference/P008_架构中断接口.md#ga1b827afafc622d412962f568b78726dc)
- [arch_cpu_irqs_are_enabled](../fatal_irq_reference/P008_架构中断接口.md#gab7c91d90ed8ccfce15c8bd040496f9ac)
- [arch_irq_disable](../fatal_irq_reference/P008_架构中断接口.md#ga216d692e87bfba955a60f8e570e127df)
- [arch_irq_enable](../fatal_irq_reference/P008_架构中断接口.md#gaa278d630653b33cb339621d725ed295a)
- [arch_irq_is_enabled](../fatal_irq_reference/P008_架构中断接口.md#ga3bd8e963a124421bb372dab4bdc6cd83)
- [arch_irq_clear_pending](../fatal_irq_reference/P008_架构中断接口.md#ga6f5e4f7795c23586b13c5f6eaecac54d)
- [arch_irq_set_pending](../fatal_irq_reference/P008_架构中断接口.md#gaad2c939389164d483a472d4f6d201ce0)
- [arch_irq_is_pending](../fatal_irq_reference/P008_架构中断接口.md#gaa45f7cc9823e3a3b5f760ffc02323516)
- [arch_irq_get_active](../fatal_irq_reference/P008_架构中断接口.md#gae2a76360ce4ddcd461c06602ef16ba32)
- [arch_irq_connect_dynamic](../fatal_irq_reference/P008_架构中断接口.md#gaa4d733913e12a12e104dc4781cca7308)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [arch_irq_disconnect_dynamic](../fatal_irq_reference/P008_架构中断接口.md#ga41483a9fc1090d96d066e107a74ee38c)
- [arch_irq_allocate](../fatal_irq_reference/P008_架构中断接口.md#gaac8f60e7dfc5ce3222372798e96316ae)
- [arch_irq_set_used](../fatal_irq_reference/P008_架构中断接口.md#ga5f0942bd035c50c9d2d91ada472f37c4)
- [arch_irq_is_used](../fatal_irq_reference/P008_架构中断接口.md#ga5c85d7bf54a83190ed27587dc5a01de5)
- [irq_offload_routine_t](../fatal_irq_reference/P009_中断卸载头文件参考.md#a5bcf9956ddbf5ea75619f0cef91e1214)
- [arch_curr_cpu](../arch_core_reference/P005_架构多处理器接口.md#gad42138d41dff6a4aad8abf7d77fcd8b2)
- [arch_proc_id](../arch_core_reference/P005_架构多处理器接口.md#gad628c89816128546501e3c26eaaf9dea)
- [arch_sched_broadcast_ipi](../arch_core_reference/P005_架构多处理器接口.md#ga8fe90cec57c56993df14c0d545106ca3)
- [arch_sched_directed_ipi](../arch_core_reference/P005_架构多处理器接口.md#gadebac82c1ed0a8a08adb297738d2633e)
- [arch_smp_init](../arch_core_reference/P005_架构多处理器接口.md#ga6ffc01f86f4541d1092ee4b277a07ac6)
- [arch_num_cpus](../arch_core_reference/P005_架构多处理器接口.md#ga078e9bf1a4a557d1321ddc4848092cbe)
- [arch_page_phys_get](../arch_core_reference/P003_架构内存映射接口.md#gaa31a233dab4ad575a9a969de10965200)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [zephyr/arch/syscall.h](../syscall_boot_reference/P006_架构系统调用头文件参考.md)
- [arch_syscall_invoke0](../arch_core_reference/P004_架构用户空间接口.md#ga5e9ab24b9c980e327903fbe3f5bd97f3)
- [arch_syscall_invoke1](../arch_core_reference/P004_架构用户空间接口.md#ga4cfb3b2b38e5afca889e8b9765d6c3df)
- [arch_syscall_invoke2](../arch_core_reference/P004_架构用户空间接口.md#ga1e78f1022aaf10e88727b142b56d4ef0)
- [arch_syscall_invoke3](../arch_core_reference/P004_架构用户空间接口.md#gaacb1c66a1b7bf2293fea269f6b5e1c7e)
- [arch_syscall_invoke4](../arch_core_reference/P004_架构用户空间接口.md#ga0ba3ae2290827385b226ebdbf3de3b53)
- [arch_syscall_invoke5](../arch_core_reference/P004_架构用户空间接口.md#ga9971c78bc8f579a0dadf84225dc0c3ff)
- [arch_syscall_invoke6](../arch_core_reference/P004_架构用户空间接口.md#gac6cae2197637993a86b6ec6803b5742b)
- [arch_is_user_context](../arch_core_reference/P004_架构用户空间接口.md#ga89ab53a218add419e37f89c1f5fd955f)
- [arch_mem_domain_max_partitions_get](../arch_core_reference/P004_架构用户空间接口.md#ga71542fcc679a94ad9ea60d7ac46da361)
- [arch_mem_domain_deinit](../arch_core_reference/P004_架构用户空间接口.md#gab5f05c76b315b6a8d1c3fd68abb8d594)
- [arch_buffer_validate](../arch_core_reference/P004_架构用户空间接口.md#ga13053a9233b86d5cd19dc3cea5804a16)
- [arch_virt_region_align](../arch_core_reference/P004_架构用户空间接口.md#ga48be2412ba65ec550ded63e2f1a0470f)
- [arch_user_mode_enter](../arch_core_reference/P004_架构用户空间接口.md#ga447daa0454a90a7a3a247de01e522567)
- [arch_syscall_oops](../arch_core_reference/P004_架构用户空间接口.md#gad53908f229d7e2c333574b009493644b)
- [arch_user_string_nlen](../arch_core_reference/P004_架构用户空间接口.md#ga174c4f356fe315c523cefbf513858c9c)
- [arch_cohere_stacks](../arch_core_reference/P004_架构用户空间接口.md#ga306e9d0e5f8094cb75686f1c43d068a9)
- [arch_gdb_init](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga21c8a32d35c4d267b8306d595ff1d726)
- [arch_gdb_continue](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga9c130421feeee919651828511743b346)
- [arch_gdb_step](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga2aa577d5e55c8b739e2be6187336aaf0)
- [arch_gdb_reg_readall](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga5317106a8022bea2a0d42af0789cc016)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [arch_gdb_reg_writeall](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga0ef78d7e193e98549d9665632e53d5ca)
- [arch_gdb_reg_readone](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#gaa3216e9f381f974c374a6399af5cdba5)
- [arch_gdb_reg_writeone](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#gad717b520d774294bbda78a56cddcaeff)
- [arch_gdb_add_breakpoint](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#gab6f42110cf2340132bf2b3916810c01d)
- [arch_gdb_remove_breakpoint](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#ga734041433f69030ad98439d10ef56ad6)
- [arch_gdb_post_memory_write](https://docs.zephyrproject.org/latest/doxygen/html/group__arch-gdbstub.html#gab1111c30383cbf30d5eb66711c326642)
- [zephyr/timing/types.h](../timing_reference/P007_计时类型头文件参考.md)
- [arch_timing_init](../timing_reference/P002_架构计时接口.md#ga5d9923569b40437c28879ff4b3ff77c2)
- [arch_timing_start](../timing_reference/P002_架构计时接口.md#gaf8cd88e81c2104b5eb0fbe42967b7834)
- [arch_timing_stop](../timing_reference/P002_架构计时接口.md#ga566483c64f5c5d2f0465e3f969303fd3)
- [timing_t](../timing_reference/P007_计时类型头文件参考.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2)
- [arch_timing_counter_get](../timing_reference/P002_架构计时接口.md#gad7a709477650c8596a96fe080f583fdd)
- [arch_timing_cycles_get](../timing_reference/P002_架构计时接口.md#ga44d3a7bd8b7008c9cd6c0524e97f128c)
- [arch_timing_freq_get](../timing_reference/P002_架构计时接口.md#ga026409e1dc323ceddb82b2a6f1cc7ca2)
- [arch_timing_cycles_to_ns](../timing_reference/P002_架构计时接口.md#ga8424bc96c05dcae34b7ffd445e2916fe)
- [arch_timing_cycles_to_ns_avg](../timing_reference/P002_架构计时接口.md#ga925b4caff80f1dbac36531b479b24364)
- [arch_timing_freq_get_mhz](../timing_reference/P002_架构计时接口.md#ga1f7bfb9ce0588f3b423c2a63933d40eb)
- [msi_vector](../platform_security_model_reference/P018_msi_vector_结构体.md)
- [msi_vector_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga9ede6a7a472ee62f0975256a1b5f1231)
- [arch_spin_relax](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html#a9932b29bc0c3b86e4f8cbd6708ef5d9c)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [stack_trace_callback_fn](../thread_stack_reference/P005_架构栈遍历接口.md#gaec9949df614728aa6d677f9f1fafd844)
- [arch_stack_walk](../thread_stack_reference/P005_架构栈遍历接口.md#ga7129c254277cfa162cd9c5778a7662c2)
- [zephyr/arch/arch_inlines.h](https://docs.zephyrproject.org/latest/doxygen/html/arch__inlines_8h.html)
- [cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/arch_2cpu_8h.html)
- [syscall.h](../syscall_boot_reference/P006_架构系统调用头文件参考.md)
- [arch_inlines.h](https://docs.zephyrproject.org/latest/doxygen/html/arch__inlines_8h.html)
- [types.h](../timing_reference/P007_计时类型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [irq_offload.h](../fatal_irq_reference/P009_中断卸载头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P014_arch_inlines.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P016_arm-gic.h_源码浏览.md)
