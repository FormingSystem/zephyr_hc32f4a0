---
id: learning.zephyr-docs.api-source-network-reference.page-21
title: tee.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tee_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_tee.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tee_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tee_8h.html)。

## 21.1\_原始可见代码（Source Code）

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
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
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
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00141"></a>
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
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="foldopen00198"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="foldopen00207"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="foldopen00231"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="foldopen00241"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="foldopen00252"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00263"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="foldopen00342"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00364"></a>
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
<a id="l00473"></a>
<a id="l00474"></a>
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
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00531"></a>
<a id="l00532"></a>
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
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
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
<a id="l00674"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00681"></a>
<a id="l00682"></a>
<a id="l00683"></a>
<a id="l00684"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__tee__interface__backend_html_ga2ea18e713a101a6ca715baa04c2f4185"></a>
<a id="agroup__tee__interface__backend_html_ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20"></a>
<a id="agroup__tee__interface__backend_html_ga9e2807d34d580c012129a2fc1f5a425a"></a>
<a id="agroup__tee__interface__backend_html_gaae68677cbff1e831fadc3d188c8588ff"></a>
<a id="agroup__tee__interface__backend_html_gac3695e51dc8b08bb5e5c5d984c402b0e"></a>
<a id="agroup__tee__interface__backend_html_gac412f57a3da187e6e272857d5bdaaaeb"></a>
<a id="agroup__tee__interface__backend_html_gac533d9e85d65857c0d984506024a55b4"></a>
<a id="agroup__tee__interface__backend_html_gad4cd5b65cac3eb7b4338fd99eeb13a93"></a>
<a id="agroup__tee__interface__backend_html_gaf972199fcdbd892688dc141ddba6e6aa"></a>
<a id="agroup__tee__interface_html_ga1565c23104792203ede9d9cb388ff782"></a>
<a id="agroup__tee__interface_html_ga2213f63da1f080beaedc169e13531a37"></a>
<a id="agroup__tee__interface_html_ga2fac25b74105b1ddfb15db51598b89c8"></a>
<a id="agroup__tee__interface_html_ga346d8d67a18542c097f1254c0ace8726"></a>
<a id="agroup__tee__interface_html_ga34fbbfe48a07541041ffddb9e318332a"></a>
<a id="agroup__tee__interface_html_ga47f7403e2b136f755432159c7bd679a5"></a>
<a id="agroup__tee__interface_html_ga79ff2ca70757daf8e677b42002f4aeac"></a>
<a id="agroup__tee__interface_html_ga85fd3e6e6b596da02c97661a35c9814c"></a>
<a id="agroup__tee__interface_html_ga93cccfa446983be704f364760bf7567b"></a>
<a id="agroup__tee__interface_html_gacb1d58002378a11d92361a149d451241"></a>
<a id="agroup__tee__interface_html_gad7c66e32d5b02c42c698bd422cf43523"></a>
<a id="agroup__tee__interface_html_gadaaec6b6ea29d81f36943bbe5bcb305e"></a>
<a id="agroup__tee__interface_html_gade2c0e7d89e3594707637b62a1901bac"></a>
<a id="agroup__tee__interface_html_gade7fdbece8b0bd47f5d148572016c4ef"></a>
<a id="agroup__tee__interface_html_gae1337f293febcecc7dbc79ac064e7824"></a>
<a id="agroup__tee__interface_html_gaf53521a3e3a36a9827753716bef1434f"></a>
<a id="akernel_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructtee__driver__api_html"></a>
<a id="astructtee__driver__api_html_a04db5713f645416fa9cc015433941a94"></a>
<a id="astructtee__driver__api_html_a1db852ebd953c0c4ba5f88fcab9fdce9"></a>
<a id="astructtee__driver__api_html_a35c770c1dfb807bb461640a519fdabe5"></a>
<a id="astructtee__driver__api_html_a380a12c033c1c659d7169d0d16593f94"></a>
<a id="astructtee__driver__api_html_a5d2a33d8156fd56176f69e903da9204e"></a>
<a id="astructtee__driver__api_html_abd28ba23f09ce245a6346f7a241eb9cc"></a>
<a id="astructtee__driver__api_html_ac24f7f4d3f63145e8f687a37cad780ca"></a>
<a id="astructtee__driver__api_html_ac99f066bd644741df90d418ab9fe4198"></a>
<a id="astructtee__driver__api_html_acf8076d0cf2bb496d9c6143d6e5d2253"></a>
<a id="astructtee__invoke__func__arg_html"></a>
<a id="astructtee__invoke__func__arg_html_a17aa094ca0a6c6d9a72d2fae9c0c66ef"></a>
<a id="astructtee__invoke__func__arg_html_a457daf2221f9520aecb42667acc4ccd1"></a>
<a id="astructtee__invoke__func__arg_html_ae806e940e463321b3de31bad2e05bf60"></a>
<a id="astructtee__invoke__func__arg_html_af110327354b1ca48dedf22855c3a7afc"></a>
<a id="astructtee__invoke__func__arg_html_af63bd284a7397d4086ac17f83d6b1e93"></a>
<a id="astructtee__open__session__arg_html"></a>
<a id="astructtee__open__session__arg_html_a226c617eae1b959025a0232eed48aa41"></a>
<a id="astructtee__open__session__arg_html_a3be6d6ea6aeff1a8f27051fe30f21347"></a>
<a id="astructtee__open__session__arg_html_a5e28bb77990ce6d050a57daa419760e1"></a>
<a id="astructtee__open__session__arg_html_a73a7e82fb0b589eed327ab8f4217e6fc"></a>
<a id="astructtee__open__session__arg_html_a9f4c56fe45f5ad9313bdc1f457d31f9a"></a>
<a id="astructtee__open__session__arg_html_adf8bfaaf5059de617a7139b5f06a0ac6"></a>
<a id="astructtee__open__session__arg_html_aff38cc02e83936e23965ee2e4e44ff26"></a>
<a id="astructtee__param_html"></a>
<a id="astructtee__param_html_a22785fe00950c3a7d6353c39b12d72a8"></a>
<a id="astructtee__param_html_a79b39571785949e32629216742e34d72"></a>
<a id="astructtee__param_html_ac8ced719ce993735e22d68ca50f54e5b"></a>
<a id="astructtee__param_html_aea8916d1bc24ab5a56f59fa4608f1a38"></a>
<a id="astructtee__shm_html"></a>
<a id="astructtee__shm_html_a02fe0fd69f1e8d5650cfa116136ea9ca"></a>
<a id="astructtee__shm_html_a65446310f73319aa5f8e100e4d83198e"></a>
<a id="astructtee__shm_html_ab761c1d3d5e64c21725eff97521b4b86"></a>
<a id="astructtee__shm_html_ac2738d87cbe439f093cad67a375c2807"></a>
<a id="astructtee__version__info_html"></a>
<a id="astructtee__version__info_html_a56a3c50a69f125428dfbf7a867cb7177"></a>
<a id="astructtee__version__info_html_a6cbf12676e5cfc1bdf4221a8188bf055"></a>
<a id="astructtee__version__info_html_aaf74a1ff5fb899a0675724669a7d7e36"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2023 EPAM Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */


/*
 * Copyright (c) 2015-2016, Linaro Limited
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice,
 * this list of conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */
#ifndef ZEPHYR_INCLUDE_DRIVERS_TEE_H_
#define ZEPHYR_INCLUDE_DRIVERS_TEE_H_

#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/util.h>


#ifdef __cplusplus
extern "C" {
#endif
#define TEE_UUID_LEN 16

#define TEE_GEN_CAP_GP          BIT(0) /* GlobalPlatform compliant TEE */
#define TEE_GEN_CAP_PRIVILEGED  BIT(1) /* Privileged device (for supplicant) */
#define TEE_GEN_CAP_REG_MEM     BIT(2) /* Supports registering shared memory */
#define TEE_GEN_CAP_MEMREF_NULL BIT(3) /* Support NULL MemRef */

#define TEE_SHM_REGISTER        BIT(0)
#define TEE_SHM_ALLOC           BIT(1)

#define TEE_PARAM_ATTR_TYPE_NONE                0 /* parameter not used */
#define TEE_PARAM_ATTR_TYPE_VALUE_INPUT         1
#define TEE_PARAM_ATTR_TYPE_VALUE_OUTPUT        2
#define TEE_PARAM_ATTR_TYPE_VALUE_INOUT         3 /* input and output */
#define TEE_PARAM_ATTR_TYPE_MEMREF_INPUT        5
#define TEE_PARAM_ATTR_TYPE_MEMREF_OUTPUT       6
#define TEE_PARAM_ATTR_TYPE_MEMREF_INOUT        7 /* input and output */
#define TEE_PARAM_ATTR_TYPE_MASK                0xff
#define TEE_PARAM_ATTR_META                     0x100
#define TEE_PARAM_ATTR_MASK                     (TEE_PARAM_ATTR_TYPE_MASK | TEE_PARAM_ATTR_META)

#define TEEC_ORIGIN_API         0x00000001
#define TEEC_ORIGIN_COMMS       0x00000002
#define TEEC_ORIGIN_TEE         0x00000003
#define TEEC_ORIGIN_TRUSTED_APP 0x00000004


#define TEEC_SUCCESS                            0x00000000
#define TEEC_ERROR_STORAGE_NOT_AVAILABLE        0xF0100003
#define TEEC_ERROR_GENERIC                      0xFFFF0000
#define TEEC_ERROR_ACCESS_DENIED                0xFFFF0001
#define TEEC_ERROR_CANCEL                       0xFFFF0002
#define TEEC_ERROR_ACCESS_CONFLICT              0xFFFF0003
#define TEEC_ERROR_EXCESS_DATA                  0xFFFF0004
#define TEEC_ERROR_BAD_FORMAT                   0xFFFF0005
#define TEEC_ERROR_BAD_PARAMETERS               0xFFFF0006
#define TEEC_ERROR_BAD_STATE                    0xFFFF0007
#define TEEC_ERROR_ITEM_NOT_FOUND               0xFFFF0008
#define TEEC_ERROR_NOT_IMPLEMENTED              0xFFFF0009
#define TEEC_ERROR_NOT_SUPPORTED                0xFFFF000A
#define TEEC_ERROR_NO_DATA                      0xFFFF000B
#define TEEC_ERROR_OUT_OF_MEMORY                0xFFFF000C
#define TEEC_ERROR_BUSY                         0xFFFF000D
#define TEEC_ERROR_COMMUNICATION                0xFFFF000E
#define TEEC_ERROR_SECURITY                     0xFFFF000F
#define TEEC_ERROR_SHORT_BUFFER                 0xFFFF0010
#define TEEC_ERROR_EXTERNAL_CANCEL              0xFFFF0011
#define TEEC_ERROR_TARGET_DEAD                  0xFFFF3024
#define TEEC_ERROR_STORAGE_NO_SPACE             0xFFFF3041

#define TEEC_LOGIN_PUBLIC               0x00000000
#define TEEC_LOGIN_USER                 0x00000001
#define TEEC_LOGIN_GROUP                0x00000002
#define TEEC_LOGIN_APPLICATION          0x00000004
#define TEEC_LOGIN_USER_APPLICATION     0x00000005
#define TEEC_LOGIN_GROUP_APPLICATION    0x00000006

struct tee_version_info {
        uint32_t impl_id;
        uint32_t impl_caps;
        uint32_t gen_caps;
};

struct tee_open_session_arg {
        uint8_t uuid[TEE_UUID_LEN];
        uint8_t clnt_uuid[TEE_UUID_LEN];
        uint32_t clnt_login;
        uint32_t cancel_id;
        uint32_t session;
        uint32_t ret;
        uint32_t ret_origin;
};

struct tee_param {
        uint64_t attr;
        uint64_t a;
        uint64_t b;
        uint64_t c;
};

struct tee_invoke_func_arg {
        uint32_t func;
        uint32_t session;
        uint32_t cancel_id;
        uint32_t ret;
        uint32_t ret_origin;
};

struct tee_shm {
        const struct device *dev;
        void *addr;
        uint64_t size;
        uint32_t flags;
};


typedef int (*tee_get_version_t)(const struct device *dev, struct tee_version_info *info);

typedef int (*tee_open_session_t)(const struct device *dev, struct tee_open_session_arg *arg,
                                  unsigned int num_param, struct tee_param *param,
                                  uint32_t *session_id);
typedef int (*tee_close_session_t)(const struct device *dev, uint32_t session_id);

typedef int (*tee_cancel_t)(const struct device *dev, uint32_t session_id, uint32_t cancel_id);

typedef int (*tee_invoke_func_t)(const struct device *dev, struct tee_invoke_func_arg *arg,
                                 unsigned int num_param, struct tee_param *param);
typedef int (*tee_shm_register_t)(const struct device *dev, struct tee_shm *shm);

typedef int (*tee_shm_unregister_t)(const struct device *dev, struct tee_shm *shm);

typedef int (*tee_suppl_recv_t)(const struct device *dev, uint32_t *func, unsigned int *num_params,
                                struct tee_param *param);

typedef int (*tee_suppl_send_t)(const struct device *dev, unsigned int ret, unsigned int num_params,
                                struct tee_param *param);

__subsystem struct tee_driver_api {
        tee_get_version_t get_version;
        tee_open_session_t open_session;
        tee_close_session_t close_session;
        tee_cancel_t cancel;
        tee_invoke_func_t invoke_func;
        tee_shm_register_t shm_register;
        tee_shm_unregister_t shm_unregister;
        tee_suppl_recv_t suppl_recv;
        tee_suppl_send_t suppl_send;
};


__syscall int tee_get_version(const struct device *dev, struct tee_version_info *info);

static inline int z_impl_tee_get_version(const struct device *dev, struct tee_version_info *info)
{
        const struct tee_driver_api *api = DEVICE_API_GET(tee, dev);

        if (!api->get_version) {
                return -ENOSYS;
        }

        return api->get_version(dev, info);
}

__syscall int tee_open_session(const struct device *dev, struct tee_open_session_arg *arg,
                               unsigned int num_param, struct tee_param *param,
                               uint32_t *session_id);

static inline int z_impl_tee_open_session(const struct device *dev,
                                          struct tee_open_session_arg *arg,
                                          unsigned int num_param, struct tee_param *param,
                                          uint32_t *session_id)
{
        const struct tee_driver_api *api = DEVICE_API_GET(tee, dev);

        if (!api->open_session) {
                return -ENOSYS;
        }

        return api->open_session(dev, arg, num_param, param, session_id);
}

__syscall int tee_close_session(const struct device *dev, uint32_t session_id);

static inline int z_impl_tee_close_session(const struct device *dev, uint32_t session_id)
{
        const struct tee_driver_api *api = DEVICE_API_GET(tee, dev);

        if (!api->close_session) {
                return -ENOSYS;
        }

        return api->close_session(dev, session_id);
}

__syscall int tee_cancel(const struct device *dev, uint32_t session_id, uint32_t cancel_id);

static inline int z_impl_tee_cancel(const struct device *dev, uint32_t session_id,
                                    uint32_t cancel_id)
{
        const struct tee_driver_api *api = DEVICE_API_GET(tee, dev);

        if (!api->cancel) {
                return -ENOSYS;
        }

        return api->cancel(dev, session_id, cancel_id);
}

__syscall int tee_invoke_func(const struct device *dev, struct tee_invoke_func_arg *arg,
                              unsigned int num_param, struct tee_param *param);

static inline int z_impl_tee_invoke_func(const struct device *dev, struct tee_invoke_func_arg *arg,
                                         unsigned int num_param, struct tee_param *param)
{
        const struct tee_driver_api *api = DEVICE_API_GET(tee, dev);

        if (!api->invoke_func) {
                return -ENOSYS;
        }

        return api->invoke_func(dev, arg, num_param, param);
}

int tee_add_shm(const struct device *dev, void *addr, size_t align, size_t size, uint32_t flags,
                struct tee_shm **shmp);

int tee_rm_shm(const struct device *dev, struct tee_shm *shm);

__syscall int tee_shm_register(const struct device *dev, void *addr, size_t size,
                               uint32_t flags, struct tee_shm **shm);

static inline int z_impl_tee_shm_register(const struct device *dev, void *addr, size_t size,
                                          uint32_t flags, struct tee_shm **shm)
{
        flags &= ~TEE_SHM_ALLOC;
        return tee_add_shm(dev, addr, 0, size, flags | TEE_SHM_REGISTER, shm);
}

__syscall int tee_shm_unregister(const struct device *dev, struct tee_shm *shm);

static inline int z_impl_tee_shm_unregister(const struct device *dev, struct tee_shm *shm)
{
        return tee_rm_shm(dev, shm);
}

__syscall int tee_shm_alloc(const struct device *dev, size_t size, uint32_t flags,
                            struct tee_shm **shm);

static inline int z_impl_tee_shm_alloc(const struct device *dev, size_t size, uint32_t flags,
                                       struct tee_shm **shm)
{
        return tee_add_shm(dev, NULL, 0, size, flags | TEE_SHM_ALLOC | TEE_SHM_REGISTER, shm);
}

__syscall int tee_shm_free(const struct device *dev, struct tee_shm *shm);

static inline int z_impl_tee_shm_free(const struct device *dev, struct tee_shm *shm)
{
        return tee_rm_shm(dev, shm);
}

__syscall int tee_suppl_recv(const struct device *dev, uint32_t *func, unsigned int *num_params,
                             struct tee_param *param);

static inline int z_impl_tee_suppl_recv(const struct device *dev, uint32_t *func,
                                        unsigned int *num_params, struct tee_param *param)
{
        const struct tee_driver_api *api = DEVICE_API_GET(tee, dev);

        if (!api->suppl_recv) {
                return -ENOSYS;
        }

        return api->suppl_recv(dev, func, num_params, param);
}

__syscall int tee_suppl_send(const struct device *dev, unsigned int ret, unsigned int num_params,
                             struct tee_param *param);

static inline int z_impl_tee_suppl_send(const struct device *dev, unsigned int ret,
                                        unsigned int num_params, struct tee_param *param)
{
        const struct tee_driver_api *api = DEVICE_API_GET(tee, dev);

        if (!api->suppl_send) {
                return -ENOSYS;
        }

        return api->suppl_send(dev, ret, num_params, param);
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/tee.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_TEE_H_ */
```

## 21.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 EPAM Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 13 行

版权所有（Copyright）© 2015–2016 Linaro Limited。保留所有权利。

允许以源代码和二进制形式重新分发和使用本软件，无论是否修改，但必须满足以下条件：

1. 重新分发源代码时，必须保留上述版权声明、本条件列表以及以下免责声明。
2. 以二进制形式重新分发时，必须在随分发提供的文档和/或其他材料中重现上述版权声明、本条件列表以及以下免责声明。

本软件由版权所有者及贡献者按“原样”（AS IS）提供，不提供任何明示或默示保证，包括但不限于适销性及特定用途适用性的默示保证。对于以任何方式因使用本软件而产生的任何直接、间接、附带、特殊、惩罚性或后果性损害（包括但不限于采购替代商品或服务、使用权损失、数据或利润损失，或业务中断），无论其原因如何，也无论依据何种责任理论——合同责任、严格责任或侵权责任（包括疏忽或其他情形）——即使已被告知此类损害的可能性，版权所有者及贡献者也均不承担责任。

### 注释 3：原第 76 行

符合 GlobalPlatform 规范的可信执行环境（Trusted Execution Environment，TEE）。

### 注释 4：原第 77 行

特权设备（privileged device），供辅助服务（supplicant）使用。

### 注释 5：原第 78 行

支持注册共享内存（shared memory）。

### 注释 6：原第 79 行

支持空内存引用（NULL MemRef）。

### 注释 7：原第 84 行

未使用的参数（parameter）。

### 注释 8：原第 87 行

输入和输出（input and output）。

### 注释 9：原第 90 行

输入和输出（input and output）。

### 注释 10：原第 684 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_TEE_H_`。

## 21.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tee_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [tee_version_info](../platform_security_model_reference/P063_tee_version_info_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [impl_id](../platform_security_model_reference/P063_tee_version_info_结构体.md#aaf74a1ff5fb899a0675724669a7d7e36)
- [impl_caps](../platform_security_model_reference/P063_tee_version_info_结构体.md#a6cbf12676e5cfc1bdf4221a8188bf055)
- [gen_caps](../platform_security_model_reference/P063_tee_version_info_结构体.md#a56a3c50a69f125428dfbf7a867cb7177)
- [tee_open_session_arg](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uuid](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#a9f4c56fe45f5ad9313bdc1f457d31f9a)
- [TEE_UUID_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga79ff2ca70757daf8e677b42002f4aeac)
- [clnt_uuid](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#aff38cc02e83936e23965ee2e4e44ff26)
- [clnt_login](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#a226c617eae1b959025a0232eed48aa41)
- [cancel_id](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#adf8bfaaf5059de617a7139b5f06a0ac6)
- [session](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#a5e28bb77990ce6d050a57daa419760e1)
- [ret](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#a3be6d6ea6aeff1a8f27051fe30f21347)
- [ret_origin](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#a73a7e82fb0b589eed327ab8f4217e6fc)
- [tee_param](../platform_security_model_reference/P061_tee_param_结构体.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [attr](../platform_security_model_reference/P061_tee_param_结构体.md#ac8ced719ce993735e22d68ca50f54e5b)
- [a](../platform_security_model_reference/P061_tee_param_结构体.md#aea8916d1bc24ab5a56f59fa4608f1a38)
- [b](../platform_security_model_reference/P061_tee_param_结构体.md#a22785fe00950c3a7d6353c39b12d72a8)
- [c](../platform_security_model_reference/P061_tee_param_结构体.md#a79b39571785949e32629216742e34d72)
- [tee_invoke_func_arg](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md)
- [func](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md#a17aa094ca0a6c6d9a72d2fae9c0c66ef)
- [session](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md#af110327354b1ca48dedf22855c3a7afc)
- [cancel_id](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md#a457daf2221f9520aecb42667acc4ccd1)
- [ret](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md#af63bd284a7397d4086ac17f83d6b1e93)
- [ret_origin](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md#ae806e940e463321b3de31bad2e05bf60)
- [tee_shm](../platform_security_model_reference/P062_tee_shm_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../platform_security_model_reference/P062_tee_shm_结构体.md#ab761c1d3d5e64c21725eff97521b4b86)
- [addr](../platform_security_model_reference/P062_tee_shm_结构体.md#a65446310f73319aa5f8e100e4d83198e)
- [size](../platform_security_model_reference/P062_tee_shm_结构体.md#a02fe0fd69f1e8d5650cfa116136ea9ca)
- [flags](../platform_security_model_reference/P062_tee_shm_结构体.md#ac2738d87cbe439f093cad67a375c2807)
- [tee_get_version_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gac533d9e85d65857c0d984506024a55b4)
- [tee_open_session_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gaf972199fcdbd892688dc141ddba6e6aa)
- [tee_close_session_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gac412f57a3da187e6e272857d5bdaaaeb)
- [tee_cancel_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gad4cd5b65cac3eb7b4338fd99eeb13a93)
- [tee_invoke_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gac3695e51dc8b08bb5e5c5d984c402b0e)
- [tee_shm_register_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#ga9e2807d34d580c012129a2fc1f5a425a)
- [tee_shm_unregister_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#ga2ea18e713a101a6ca715baa04c2f4185)
- [tee_suppl_recv_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#gaae68677cbff1e831fadc3d188c8588ff)
- [tee_suppl_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface__backend.html#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20)
- [tee_driver_api](../platform_security_model_reference/P058_tee_driver_api_结构体.md)
- [get_version](../platform_security_model_reference/P058_tee_driver_api_结构体.md#ac99f066bd644741df90d418ab9fe4198)
- [open_session](../platform_security_model_reference/P058_tee_driver_api_结构体.md#acf8076d0cf2bb496d9c6143d6e5d2253)
- [close_session](../platform_security_model_reference/P058_tee_driver_api_结构体.md#a380a12c033c1c659d7169d0d16593f94)
- [cancel](../platform_security_model_reference/P058_tee_driver_api_结构体.md#a04db5713f645416fa9cc015433941a94)
- [invoke_func](../platform_security_model_reference/P058_tee_driver_api_结构体.md#a5d2a33d8156fd56176f69e903da9204e)
- [shm_register](../platform_security_model_reference/P058_tee_driver_api_结构体.md#a1db852ebd953c0c4ba5f88fcab9fdce9)
- [shm_unregister](../platform_security_model_reference/P058_tee_driver_api_结构体.md#ac24f7f4d3f63145e8f687a37cad780ca)
- [suppl_recv](../platform_security_model_reference/P058_tee_driver_api_结构体.md#a35c770c1dfb807bb461640a519fdabe5)
- [suppl_send](../platform_security_model_reference/P058_tee_driver_api_结构体.md#abd28ba23f09ce245a6346f7a241eb9cc)
- [tee_get_version](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gadaaec6b6ea29d81f36943bbe5bcb305e)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [tee_open_session](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gad7c66e32d5b02c42c698bd422cf43523)
- [tee_close_session](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gacb1d58002378a11d92361a149d451241)
- [tee_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga34fbbfe48a07541041ffddb9e318332a)
- [tee_invoke_func](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gae1337f293febcecc7dbc79ac064e7824)
- [tee_add_shm](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gade7fdbece8b0bd47f5d148572016c4ef)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [tee_rm_shm](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gaf53521a3e3a36a9827753716bef1434f)
- [tee_shm_register](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga1565c23104792203ede9d9cb388ff782)
- [~TEE_SHM_ALLOC](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga85fd3e6e6b596da02c97661a35c9814c)
- [TEE_SHM_REGISTER](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga2fac25b74105b1ddfb15db51598b89c8)
- [tee_shm_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#gade2c0e7d89e3594707637b62a1901bac)
- [tee_shm_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga47f7403e2b136f755432159c7bd679a5)
- [TEE_SHM_ALLOC](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga85fd3e6e6b596da02c97661a35c9814c)
- [tee_shm_free](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga346d8d67a18542c097f1254c0ace8726)
- [tee_suppl_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga2213f63da1f080beaedc169e13531a37)
- [tee_suppl_send](https://docs.zephyrproject.org/latest/doxygen/html/group__tee__interface.html#ga93cccfa446983be704f364760bf7567b)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [tee_driver_api::cancel](../platform_security_model_reference/P058_tee_driver_api_结构体.md#a04db5713f645416fa9cc015433941a94)
- [tee_driver_api::shm_register](../platform_security_model_reference/P058_tee_driver_api_结构体.md#a1db852ebd953c0c4ba5f88fcab9fdce9)
- [tee_driver_api::suppl_recv](../platform_security_model_reference/P058_tee_driver_api_结构体.md#a35c770c1dfb807bb461640a519fdabe5)
- [tee_driver_api::close_session](../platform_security_model_reference/P058_tee_driver_api_结构体.md#a380a12c033c1c659d7169d0d16593f94)
- [tee_driver_api::invoke_func](../platform_security_model_reference/P058_tee_driver_api_结构体.md#a5d2a33d8156fd56176f69e903da9204e)
- [tee_driver_api::suppl_send](../platform_security_model_reference/P058_tee_driver_api_结构体.md#abd28ba23f09ce245a6346f7a241eb9cc)
- [tee_driver_api::shm_unregister](../platform_security_model_reference/P058_tee_driver_api_结构体.md#ac24f7f4d3f63145e8f687a37cad780ca)
- [tee_driver_api::get_version](../platform_security_model_reference/P058_tee_driver_api_结构体.md#ac99f066bd644741df90d418ab9fe4198)
- [tee_driver_api::open_session](../platform_security_model_reference/P058_tee_driver_api_结构体.md#acf8076d0cf2bb496d9c6143d6e5d2253)
- [tee_invoke_func_arg::func](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md#a17aa094ca0a6c6d9a72d2fae9c0c66ef)
- [tee_invoke_func_arg::cancel_id](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md#a457daf2221f9520aecb42667acc4ccd1)
- [tee_invoke_func_arg::ret_origin](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md#ae806e940e463321b3de31bad2e05bf60)
- [tee_invoke_func_arg::session](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md#af110327354b1ca48dedf22855c3a7afc)
- [tee_invoke_func_arg::ret](../platform_security_model_reference/P059_tee_invoke_func_arg_结构体.md#af63bd284a7397d4086ac17f83d6b1e93)
- [tee_open_session_arg::clnt_login](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#a226c617eae1b959025a0232eed48aa41)
- [tee_open_session_arg::ret](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#a3be6d6ea6aeff1a8f27051fe30f21347)
- [tee_open_session_arg::session](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#a5e28bb77990ce6d050a57daa419760e1)
- [tee_open_session_arg::ret_origin](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#a73a7e82fb0b589eed327ab8f4217e6fc)
- [tee_open_session_arg::uuid](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#a9f4c56fe45f5ad9313bdc1f457d31f9a)
- [tee_open_session_arg::cancel_id](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#adf8bfaaf5059de617a7139b5f06a0ac6)
- [tee_open_session_arg::clnt_uuid](../platform_security_model_reference/P060_tee_open_session_arg_结构体.md#aff38cc02e83936e23965ee2e4e44ff26)
- [tee_param::b](../platform_security_model_reference/P061_tee_param_结构体.md#a22785fe00950c3a7d6353c39b12d72a8)
- [tee_param::c](../platform_security_model_reference/P061_tee_param_结构体.md#a79b39571785949e32629216742e34d72)
- [tee_param::attr](../platform_security_model_reference/P061_tee_param_结构体.md#ac8ced719ce993735e22d68ca50f54e5b)
- [tee_param::a](../platform_security_model_reference/P061_tee_param_结构体.md#aea8916d1bc24ab5a56f59fa4608f1a38)
- [tee_shm::size](../platform_security_model_reference/P062_tee_shm_结构体.md#a02fe0fd69f1e8d5650cfa116136ea9ca)
- [tee_shm::addr](../platform_security_model_reference/P062_tee_shm_结构体.md#a65446310f73319aa5f8e100e4d83198e)
- [tee_shm::dev](../platform_security_model_reference/P062_tee_shm_结构体.md#ab761c1d3d5e64c21725eff97521b4b86)
- [tee_shm::flags](../platform_security_model_reference/P062_tee_shm_结构体.md#ac2738d87cbe439f093cad67a375c2807)
- [tee_version_info::gen_caps](../platform_security_model_reference/P063_tee_version_info_结构体.md#a56a3c50a69f125428dfbf7a867cb7177)
- [tee_version_info::impl_caps](../platform_security_model_reference/P063_tee_version_info_结构体.md#a6cbf12676e5cfc1bdf4221a8188bf055)
- [tee_version_info::impl_id](../platform_security_model_reference/P063_tee_version_info_结构体.md#aaf74a1ff5fb899a0675724669a7d7e36)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P020_stm32h7_clock.h_源码浏览.md) · [返回大纲](大纲.md)
