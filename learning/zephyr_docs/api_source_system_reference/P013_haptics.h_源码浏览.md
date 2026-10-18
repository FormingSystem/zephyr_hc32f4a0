---
id: learning.zephyr-docs.api-source-system-reference.page-13
title: haptics.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/haptics_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_haptics.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/haptics_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/haptics_8h.html)。

## 13.1\_原始可见代码（Source Code）

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
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00071"></a>
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
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="foldopen00116"></a>
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
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="foldopen00141"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="foldopen00163"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00185"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="foldopen00266"></a>
<a id="l00266"></a>
<a id="l00270"></a>
<a id="l00274"></a>
<a id="l00278"></a>
<a id="l00282"></a>
<a id="l00286"></a>
<a id="l00290"></a>
<a id="l00294"></a>
<a id="l00298"></a>
<a id="l00302"></a>
<a id="l00306"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00316"></a>
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
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
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
<a id="foldopen00420"></a>
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
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00519"></a>
<a id="l00520"></a>
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
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
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
<a id="l00557"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00630"></a>
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
<a id="l00648"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00651"></a>
<a id="l00652"></a>
<a id="l00653"></a>
<a id="l00654"></a>
<a id="l00655"></a>
<a id="acodec_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__audio__codec__interface_html_ga147094be4c7c5d62df695673d293f12d"></a>
<a id="agroup__haptics__interface__backend_html_ga10f61b0a2084b083f6ecf5b5901b4e90"></a>
<a id="agroup__haptics__interface__backend_html_ga31d60fbee3f7137540ecb7b318d05621"></a>
<a id="agroup__haptics__interface__backend_html_ga469bd3e86ed9b71732cd5103988827a2"></a>
<a id="agroup__haptics__interface__backend_html_ga5b0c848d0677600ab873c37f9e73770e"></a>
<a id="agroup__haptics__interface__backend_html_ga6d174ac558915159e501abecebc3e327"></a>
<a id="agroup__haptics__interface__backend_html_gaa6c2ff4b8ed7ae83e4006eb735f61a46"></a>
<a id="agroup__haptics__interface__backend_html_gab5616b157b07df317b3447c9536de1d6"></a>
<a id="agroup__haptics__interface__backend_html_gab6747d8671126a14fcfd54212ffa54bc"></a>
<a id="agroup__haptics__interface__backend_html_gae34e538c40e259967f5791cc5ebd2707"></a>
<a id="agroup__haptics__interface__backend_html_gaedbe20cc622fa0556f7f42ad2013c896"></a>
<a id="agroup__haptics__interface__backend_html_gaf595a1038d42d991eaacacfd1946dcf8"></a>
<a id="agroup__haptics__interface_html_ga26851a2c1eafd8da31a3087b0219c6bf"></a>
<a id="agroup__haptics__interface_html_ga2a801a325778cfa22765d68bd6f97b2f"></a>
<a id="agroup__haptics__interface_html_ga42a5fc7e6b6247316cdf356573dbbb33"></a>
<a id="agroup__haptics__interface_html_ga72bcc5e6627d6079f81ad8488439f7e4"></a>
<a id="agroup__haptics__interface_html_ga891fa4c05a4844a658603651e8aabfc5"></a>
<a id="agroup__haptics__interface_html_ga94b7c216edd6adf14a354b64dbc8a396"></a>
<a id="agroup__haptics__interface_html_ga96e0b0fad35d6535adad7536a9411f44"></a>
<a id="agroup__haptics__interface_html_gaa8a7f36b4b37f7512f9f46133d9f4d1b"></a>
<a id="agroup__haptics__interface_html_gaae134ab4f57a7301dbc16cb379f08192"></a>
<a id="agroup__haptics__interface_html_gabd96eff4adc560173e4e887e09dcb34b"></a>
<a id="agroup__haptics__interface_html_gabf1e580def265fe9bf95f2116d30e6b2"></a>
<a id="agroup__haptics__interface_html_gace3de1e9bf3ad759a618405649a5537a"></a>
<a id="agroup__haptics__interface_html_gad379139afa8aff76647f180c80706f79"></a>
<a id="agroup__haptics__interface_html_gae0ec52bbeb07c255044a4257df43a396"></a>
<a id="agroup__haptics__interface_html_gaef1b0ecdbeb529f7f10704d259f2f98f"></a>
<a id="agroup__haptics__interface_html_gaf86396239e200ecf8ea00fe339e416ca"></a>
<a id="agroup__haptics__interface_html_gafb18ed221c2ae5e5b643130bc3d3c8ec"></a>
<a id="agroup__haptics__interface_html_gga2a801a325778cfa22765d68bd6f97b2fa1f8b833f578dc7dd10edea6e016eb9dd"></a>
<a id="agroup__haptics__interface_html_gga2a801a325778cfa22765d68bd6f97b2fa1feeab298cfcabb1d64c87c20042c58f"></a>
<a id="agroup__haptics__interface_html_gga2a801a325778cfa22765d68bd6f97b2fa566edc86e881aad6de91333d281eefcb"></a>
<a id="agroup__haptics__interface_html_gga2a801a325778cfa22765d68bd6f97b2fa72c99e1f6a03ac2cbb7a9bcfa6a2f0a2"></a>
<a id="agroup__haptics__interface_html_gga2a801a325778cfa22765d68bd6f97b2faa7fcff3f46d5e8046bd4282b94808870"></a>
<a id="agroup__haptics__interface_html_gga2a801a325778cfa22765d68bd6f97b2fab5a60de2ff470c8f5f6d4801b8ae10d8"></a>
<a id="agroup__haptics__interface_html_gga2a801a325778cfa22765d68bd6f97b2fac578fe2b443ef37c969febca703923c0"></a>
<a id="agroup__haptics__interface_html_gga2a801a325778cfa22765d68bd6f97b2fac7864ee15f177bb81bc38fbdd001b4c0"></a>
<a id="agroup__haptics__interface_html_gga2a801a325778cfa22765d68bd6f97b2fae5e1578253a6fa38331bc8b9949c01f8"></a>
<a id="agroup__haptics__interface_html_gga2a801a325778cfa22765d68bd6f97b2fae9bf20d60ee4f05ec7829ad91d33349a"></a>
<a id="agroup__haptics__interface_html_gga72bcc5e6627d6079f81ad8488439f7e4a0b43851947d20791b1103513117d0ac6"></a>
<a id="agroup__haptics__interface_html_gga72bcc5e6627d6079f81ad8488439f7e4a3ad50c248973caf8995ba4d405b51e49"></a>
<a id="agroup__haptics__interface_html_gga72bcc5e6627d6079f81ad8488439f7e4a7f190ed6633f9fff3c12052037b44075"></a>
<a id="agroup__haptics__interface_html_gga72bcc5e6627d6079f81ad8488439f7e4a8fc4dfbe457b0fcda56a9758c1421824"></a>
<a id="agroup__haptics__interface_html_gga72bcc5e6627d6079f81ad8488439f7e4aa8b3a9045924dc3205977bb262151c45"></a>
<a id="agroup__haptics__interface_html_gga72bcc5e6627d6079f81ad8488439f7e4af8ccf96195a0abdd5d162001e57c583c"></a>
<a id="agroup__haptics__interface_html_gga72bcc5e6627d6079f81ad8488439f7e4afc9e4ce7acf06b4283ccbfe9f72f1083"></a>
<a id="agroup__haptics__interface_html_ggabd96eff4adc560173e4e887e09dcb34ba16d6ece3fd9764d2c79dae48248d53cb"></a>
<a id="agroup__haptics__interface_html_ggabd96eff4adc560173e4e887e09dcb34ba24be8785a5d6b554be611c730465ea52"></a>
<a id="agroup__haptics__interface_html_ggabd96eff4adc560173e4e887e09dcb34ba594bd6df974f1028b103d60d43ad6554"></a>
<a id="agroup__haptics__interface_html_ggabd96eff4adc560173e4e887e09dcb34ba78d963de3dd4a1c03284e02e8aac5e6d"></a>
<a id="agroup__haptics__interface_html_ggabd96eff4adc560173e4e887e09dcb34bae4a997dc3493948814e3dbec94f4dc61"></a>
<a id="agroup__haptics__interface_html_ggace3de1e9bf3ad759a618405649a5537aa1149ae71af655549c1037cd79d5cee75"></a>
<a id="agroup__haptics__interface_html_ggace3de1e9bf3ad759a618405649a5537aa7ad80e7ab92d1deac3df573b1a76b331"></a>
<a id="agroup__haptics__interface_html_ggace3de1e9bf3ad759a618405649a5537aaa7f4e50aaa2dae83fae9a5931fa4be8f"></a>
<a id="agroup__haptics__interface_html_ggace3de1e9bf3ad759a618405649a5537aac25c879fce04b01e1476e64f4f3cc2cf"></a>
<a id="agroup__haptics__interface_html_ggace3de1e9bf3ad759a618405649a5537aaddb6c50258c48229f27cb77a01116087"></a>
<a id="agroup__haptics__interface_html_ggaf86396239e200ecf8ea00fe339e416caa5e17304e155cc4478f21a938a90e1955"></a>
<a id="agroup__haptics__interface_html_ggaf86396239e200ecf8ea00fe339e416caa6fc1b297a872e0c72a8e4e4c21a153b7"></a>
<a id="agroup__haptics__interface_html_ggaf86396239e200ecf8ea00fe339e416caa9e2eb231c9a49e1a482c921c1943ac1a"></a>
<a id="agroup__haptics__interface_html_ggaf86396239e200ecf8ea00fe339e416caae3c79a961c91ce44d9238a3a7c8a066a"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="asensor_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructhaptics__driver__api_html"></a>
<a id="astructhaptics__driver__api_html_a09656cbd384b35baf2a671700c7a1b8f"></a>
<a id="astructhaptics__driver__api_html_a0dd05cce20499944df6917d1b0da1ff0"></a>
<a id="astructhaptics__driver__api_html_a230bffd452291154f0ad463278836709"></a>
<a id="astructhaptics__driver__api_html_a244f4d6a7eebaef51743c7ed26779550"></a>
<a id="astructhaptics__driver__api_html_a269102034face9a4ac30d01a6412cc4d"></a>
<a id="astructhaptics__driver__api_html_a50f1036d6cbce31880e9d223a1721fb2"></a>
<a id="astructhaptics__driver__api_html_a5489147ccfe08d917766bfcb328fa310"></a>
<a id="astructhaptics__driver__api_html_a56961eced0227d3c4dddba5dd28c24b5"></a>
<a id="astructhaptics__driver__api_html_a59e4e1ed8c0d81118e16e829a5bb2a75"></a>
<a id="astructhaptics__driver__api_html_aa4297942556ccd525ebd4cc7dfa4fa85"></a>
<a id="astructhaptics__driver__api_html_aadbec92f633f42a86458627ecf41a129"></a>
<a id="astructsensor__value_html"></a>
<a id="aunionaudio__dai__cfg__t_html"></a>
<a id="aunionhaptics__config_html"></a>
<a id="aunionhaptics__config_html_a69acebb965540a2e65e8d96d13712801"></a>
<a id="aunionhaptics__config_html_a7e769e0d9946082ce59001e22fce9abc"></a>
<a id="aunionhaptics__config_html_a95f9bcd56601626b8c97d2e98a3e2abf"></a>
<a id="aunionhaptics__config_html_aa74e48e60acd1bdbdacd1cff8b3a3ebd"></a>

```c
/*
 * Copyright 2024 Cirrus Logic, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_HAPTICS_H_
#define ZEPHYR_INCLUDE_DRIVERS_HAPTICS_H_


#include <zephyr/audio/codec.h>
#include <zephyr/device.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/sys/__assert.h>

#ifdef __cplusplus
extern "C" {
#endif

enum haptics_error_type {
        HAPTICS_ERROR_OVERCURRENT = BIT(0),
        HAPTICS_ERROR_OVERTEMPERATURE = BIT(1),
        HAPTICS_ERROR_UNDERVOLTAGE = BIT(2),
        HAPTICS_ERROR_OVERVOLTAGE = BIT(3),
        HAPTICS_ERROR_DC = BIT(4),

        /* Device-specific error codes can follow, refer to the device’s header file */
        HAPTICS_ERROR_PRIV_START = BIT(5),
};

enum haptics_monitor {
        HAPTICS_MONITOR_BEMF,
        HAPTICS_MONITOR_CURRENT,
        HAPTICS_MONITOR_F0,
        HAPTICS_MONITOR_RE,
        HAPTICS_MONITOR_AMBIENT_TEMP,
        HAPTICS_MONITOR_DIE_TEMP,
        HAPTICS_MONITOR_VBAT,
        HAPTICS_MONITOR_VBST,
        HAPTICS_MONITOR_VOUT,
        HAPTICS_MONITOR_ALL,

        /* Device-specific sensing options, refer to the device's header file */
        HAPTICS_MONITOR_PRIV_START,
};

enum haptics_monitor_type {
        HAPTICS_MONITOR_TYPE_MIN,
        HAPTICS_MONITOR_TYPE_MAX,
        HAPTICS_MONITOR_TYPE_MEAN,
        HAPTICS_MONITOR_TYPE_SINGLE,

        /* Device-specific monitor sample types, refer to the device's header file */
        HAPTICS_MONITOR_TYPE_PRIV_START,
};

enum haptics_source {
        HAPTICS_SOURCE_ROM,
        HAPTICS_SOURCE_RAM,
        HAPTICS_SOURCE_DAI,
        HAPTICS_SOURCE_ANALOG,
        HAPTICS_SOURCE_PWM,
        HAPTICS_SOURCE_CONTROL_PORT,
        HAPTICS_SOURCE_ALL,

        /* Device-specific playback sources, refer to the device’s header file */
        HAPTICS_SOURCE_PRIV_START,
};

enum haptics_trigger_type {
        HAPTICS_TRIGGER_NONE,
        HAPTICS_TRIGGER_RISING = BIT(0),
        HAPTICS_TRIGGER_FALLING = BIT(1),
        HAPTICS_TRIGGER_HIGH = BIT(2),
        HAPTICS_TRIGGER_LOW = BIT(3),

        /* Device-specific GPIO trigger options can follow, refer to the device’s header file */
        HAPTICS_TRIGGER_PRIV_START = BIT(4),
};

union haptics_config {
        uint32_t idx;
        struct {
                audio_dai_type_t type;
                audio_dai_cfg_t cfg;
        } dai;
};

typedef void (*haptics_error_callback_t)(const struct device *dev, const uint32_t errors,
                                         void *const user_data);


typedef int (*haptics_calibrate_t)(const struct device *dev, const uint32_t routine);

typedef int (*haptics_monitor_get_t)(const struct device *dev, const enum haptics_monitor monitor,
                                     const enum haptics_monitor_type type,
                                     struct sensor_value *const val);

typedef int (*haptics_monitor_set_t)(const struct device *dev, const enum haptics_monitor monitor,
                                     const bool enable);

typedef int (*haptics_register_error_callback_t)(const struct device *dev,
                                                 haptics_error_callback_t cb,
                                                 void *const user_data);

typedef int (*haptics_select_source_t)(const struct device *dev, const enum haptics_source src,
                                       const union haptics_config *const cfg);

typedef int (*haptics_set_level_t)(const struct device *dev, const enum haptics_source src,
                                   const union haptics_config *const cfg, const uint32_t level);

typedef int (*haptics_set_trigger_t)(const struct device *dev, const uint32_t trigger,
                                     const uint32_t types, const enum haptics_source src,
                                     const union haptics_config *const cfg, const uint32_t level);

typedef int (*haptics_start_output_t)(const struct device *dev);

typedef int (*haptics_stop_output_t)(const struct device *dev);

typedef int (*haptics_stream_samples_t)(const struct device *dev, const uint8_t *const samples,
                                        const size_t len);

typedef int (*haptics_trigger_t)(const struct device *dev, const uint32_t trigger,
                                 const enum haptics_trigger_type type);

__subsystem struct haptics_driver_api {
        haptics_calibrate_t calibrate;
        haptics_monitor_get_t monitor_get;
        haptics_monitor_set_t monitor_set;
        haptics_register_error_callback_t register_error_callback;
        haptics_select_source_t select_source;
        haptics_set_level_t set_level;
        haptics_set_trigger_t set_trigger;
        haptics_start_output_t start_output;
        haptics_stop_output_t stop_output;
        haptics_stream_samples_t stream_samples;
        haptics_trigger_t trigger;
};


__syscall int haptics_calibrate(const struct device *dev, const uint32_t routine);

static inline int z_impl_haptics_calibrate(const struct device *dev, const uint32_t routine)
{
        const struct haptics_driver_api *api = DEVICE_API_GET(haptics, dev);

        if (api->calibrate == NULL) {
                return -ENOSYS;
        }

        return api->calibrate(dev, routine);
}

__syscall int haptics_monitor_get(const struct device *dev, const enum haptics_monitor monitor,
                                  const enum haptics_monitor_type type,
                                  struct sensor_value *const val);

static inline int z_impl_haptics_monitor_get(const struct device *dev,
                                             const enum haptics_monitor monitor,
                                             const enum haptics_monitor_type type,
                                             struct sensor_value *const val)
{
        const struct haptics_driver_api *api = DEVICE_API_GET(haptics, dev);

        if (api->monitor_get == NULL) {
                return -ENOSYS;
        }

        __ASSERT_NO_MSG(monitor != HAPTICS_MONITOR_ALL);
        __ASSERT_NO_MSG(val != NULL);

        return api->monitor_get(dev, monitor, type, val);
}

__syscall int haptics_monitor_set(const struct device *dev, const enum haptics_monitor monitor,
                                  const bool enable);

static inline int z_impl_haptics_monitor_set(const struct device *dev,
                                             const enum haptics_monitor monitor, const bool enable)
{
        const struct haptics_driver_api *api = DEVICE_API_GET(haptics, dev);

        if (api->monitor_set == NULL) {
                return -ENOSYS;
        }

        return api->monitor_set(dev, monitor, enable);
}

static inline int haptics_register_error_callback(const struct device *dev,
                                                  haptics_error_callback_t cb,
                                                  void *const user_data)
{
        const struct haptics_driver_api *api = DEVICE_API_GET(haptics, dev);

        if (api->register_error_callback == NULL) {
                return -ENOSYS;
        }

        __ASSERT_NO_MSG(cb != NULL);

        return api->register_error_callback(dev, cb, user_data);
}

__syscall int haptics_select_source(const struct device *dev, const enum haptics_source src,
                                    const union haptics_config *const cfg);

static inline int z_impl_haptics_select_source(const struct device *dev,
                                               const enum haptics_source src,
                                               const union haptics_config *const cfg)
{
        const struct haptics_driver_api *api = DEVICE_API_GET(haptics, dev);

        __ASSERT_NO_MSG(api->select_source != NULL);

        return api->select_source(dev, src, cfg);
}

__syscall int haptics_set_level(const struct device *dev, const enum haptics_source src,
                                const union haptics_config *const cfg, const uint32_t level);

static inline int z_impl_haptics_set_level(const struct device *dev, const enum haptics_source src,
                                           const union haptics_config *const cfg,
                                           const uint32_t level)
{
        const struct haptics_driver_api *api = DEVICE_API_GET(haptics, dev);

        if (api->set_level == NULL) {
                return -ENOSYS;
        }

        return api->set_level(dev, src, cfg, level);
}

__syscall int haptics_set_trigger(const struct device *dev, const uint32_t trigger,
                                  const uint32_t types, const enum haptics_source src,
                                  const union haptics_config *const cfg, const uint32_t level);

static inline int z_impl_haptics_set_trigger(const struct device *dev, const uint32_t trigger,
                                             const uint32_t types, const enum haptics_source src,
                                             const union haptics_config *const cfg,
                                             const uint32_t level)
{
        const struct haptics_driver_api *api = DEVICE_API_GET(haptics, dev);

        if (api->set_trigger == NULL) {
                return -ENOSYS;
        }

        return api->set_trigger(dev, trigger, types, src, cfg, level);
}

__syscall int haptics_start_output(const struct device *dev);

static inline int z_impl_haptics_start_output(const struct device *dev)
{
        const struct haptics_driver_api *api = DEVICE_API_GET(haptics, dev);

        __ASSERT_NO_MSG(api->start_output != NULL);

        return api->start_output(dev);
}

__syscall int haptics_stop_output(const struct device *dev);

static inline int z_impl_haptics_stop_output(const struct device *dev)
{
        const struct haptics_driver_api *api = DEVICE_API_GET(haptics, dev);

        __ASSERT_NO_MSG(api->stop_output != NULL);

        return api->stop_output(dev);
}

__syscall int haptics_stream_samples(const struct device *dev, const uint8_t *const samples,
                                     const size_t len);

static inline int z_impl_haptics_stream_samples(const struct device *dev,
                                                const uint8_t *const samples, const size_t len)
{
        const struct haptics_driver_api *api = DEVICE_API_GET(haptics, dev);

        if (api->stream_samples == NULL) {
                return -ENOSYS;
        }

        __ASSERT_NO_MSG(samples != NULL);

        return api->stream_samples(dev, samples, len);
}

__syscall int haptics_trigger(const struct device *dev, const uint32_t trigger,
                              const enum haptics_trigger_type type);

static inline int z_impl_haptics_trigger(const struct device *dev, const uint32_t trigger,
                                         const enum haptics_trigger_type type)
{
        const struct haptics_driver_api *api = DEVICE_API_GET(haptics, dev);

        if (api->trigger == NULL) {
                return -ENOSYS;
        }

        return api->trigger(dev, trigger, type);
}


#ifdef __cplusplus
}
#endif /* __cplusplus */

#include <zephyr/syscalls/haptics.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_HAPTICS_H_ */
```

## 13.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 Cirrus Logic, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 57 行

后续可添加设备专用错误码（Device-Specific Error Codes），参见该设备的头文件。

### 注释 3：原第 83 行

设备专用感测选项（Device-Specific Sensing Options），参见该设备的头文件。

### 注释 4：原第 102 行

设备专用监测采样类型（Device-Specific Monitor Sample Types），参见该设备的头文件。

### 注释 5：原第 125 行

设备专用播放源（Device-Specific Playback Sources），参见该设备的头文件。

### 注释 6：原第 148 行

后续可添加设备专用 GPIO 触发选项（Trigger Options），参见该设备的头文件。

### 注释 7：原第 651 行

条件编译标记：`__cplusplus`。

### 注释 8：原第 655 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_HAPTICS_H_`。

## 13.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/haptics_8h.html)
- [zephyr/audio/codec.h](https://docs.zephyrproject.org/latest/doxygen/html/codec_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [haptics_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gace3de1e9bf3ad759a618405649a5537a)
- [HAPTICS_ERROR_OVERCURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aaa7f4e50aaa2dae83fae9a5931fa4be8f)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [HAPTICS_ERROR_OVERTEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aaddb6c50258c48229f27cb77a01116087)
- [HAPTICS_ERROR_UNDERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aac25c879fce04b01e1476e64f4f3cc2cf)
- [HAPTICS_ERROR_OVERVOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aa1149ae71af655549c1037cd79d5cee75)
- [HAPTICS_ERROR_DC](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggace3de1e9bf3ad759a618405649a5537aa7ad80e7ab92d1deac3df573b1a76b331)
- [haptics_monitor](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga2a801a325778cfa22765d68bd6f97b2f)
- [HAPTICS_MONITOR_BEMF](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fa1feeab298cfcabb1d64c87c20042c58f)
- [HAPTICS_MONITOR_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fa1f8b833f578dc7dd10edea6e016eb9dd)
- [HAPTICS_MONITOR_F0](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2faa7fcff3f46d5e8046bd4282b94808870)
- [HAPTICS_MONITOR_RE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fac7864ee15f177bb81bc38fbdd001b4c0)
- [HAPTICS_MONITOR_AMBIENT_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fae9bf20d60ee4f05ec7829ad91d33349a)
- [HAPTICS_MONITOR_DIE_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fab5a60de2ff470c8f5f6d4801b8ae10d8)
- [HAPTICS_MONITOR_VBAT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fa566edc86e881aad6de91333d281eefcb)
- [HAPTICS_MONITOR_VBST](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fac578fe2b443ef37c969febca703923c0)
- [HAPTICS_MONITOR_VOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fa72c99e1f6a03ac2cbb7a9bcfa6a2f0a2)
- [HAPTICS_MONITOR_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga2a801a325778cfa22765d68bd6f97b2fae5e1578253a6fa38331bc8b9949c01f8)
- [haptics_monitor_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaf86396239e200ecf8ea00fe339e416ca)
- [HAPTICS_MONITOR_TYPE_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggaf86396239e200ecf8ea00fe339e416caae3c79a961c91ce44d9238a3a7c8a066a)
- [HAPTICS_MONITOR_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggaf86396239e200ecf8ea00fe339e416caa6fc1b297a872e0c72a8e4e4c21a153b7)
- [HAPTICS_MONITOR_TYPE_MEAN](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggaf86396239e200ecf8ea00fe339e416caa5e17304e155cc4478f21a938a90e1955)
- [HAPTICS_MONITOR_TYPE_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggaf86396239e200ecf8ea00fe339e416caa9e2eb231c9a49e1a482c921c1943ac1a)
- [haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga72bcc5e6627d6079f81ad8488439f7e4)
- [HAPTICS_SOURCE_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4af8ccf96195a0abdd5d162001e57c583c)
- [HAPTICS_SOURCE_RAM](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4a3ad50c248973caf8995ba4d405b51e49)
- [HAPTICS_SOURCE_DAI](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4afc9e4ce7acf06b4283ccbfe9f72f1083)
- [HAPTICS_SOURCE_ANALOG](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4a8fc4dfbe457b0fcda56a9758c1421824)
- [HAPTICS_SOURCE_PWM](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4a0b43851947d20791b1103513117d0ac6)
- [HAPTICS_SOURCE_CONTROL_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4a7f190ed6633f9fff3c12052037b44075)
- [HAPTICS_SOURCE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gga72bcc5e6627d6079f81ad8488439f7e4aa8b3a9045924dc3205977bb262151c45)
- [haptics_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gabd96eff4adc560173e4e887e09dcb34b)
- [HAPTICS_TRIGGER_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34ba24be8785a5d6b554be611c730465ea52)
- [HAPTICS_TRIGGER_RISING](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34bae4a997dc3493948814e3dbec94f4dc61)
- [HAPTICS_TRIGGER_FALLING](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34ba78d963de3dd4a1c03284e02e8aac5e6d)
- [HAPTICS_TRIGGER_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34ba594bd6df974f1028b103d60d43ad6554)
- [HAPTICS_TRIGGER_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ggabd96eff4adc560173e4e887e09dcb34ba16d6ece3fd9764d2c79dae48248d53cb)
- [haptics_config](../hardware/P151_触觉源配置联合体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [idx](https://docs.zephyrproject.org/latest/doxygen/html/unionhaptics__config.html#a69acebb965540a2e65e8d96d13712801)
- [audio_dai_type_t](https://docs.zephyrproject.org/latest/doxygen/html/group__audio__codec__interface.html#ga147094be4c7c5d62df695673d293f12d)
- [type](https://docs.zephyrproject.org/latest/doxygen/html/unionhaptics__config.html#a7e769e0d9946082ce59001e22fce9abc)
- [audio_dai_cfg_t](../audio_video_model_reference/P066_audio_dai_cfg_t_联合体.md)
- [cfg](https://docs.zephyrproject.org/latest/doxygen/html/unionhaptics__config.html#aa74e48e60acd1bdbdacd1cff8b3a3ebd)
- [dai](https://docs.zephyrproject.org/latest/doxygen/html/unionhaptics__config.html#a95f9bcd56601626b8c97d2e98a3e2abf)
- [haptics_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gae0ec52bbeb07c255044a4257df43a396)
- [device](../device_reference/P002_设备对象结构.md)
- [haptics_calibrate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga6d174ac558915159e501abecebc3e327)
- [haptics_monitor_get_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga31d60fbee3f7137540ecb7b318d05621)
- [sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)
- [haptics_monitor_set_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga469bd3e86ed9b71732cd5103988827a2)
- [haptics_register_error_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga10f61b0a2084b083f6ecf5b5901b4e90)
- [haptics_select_source_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#ga5b0c848d0677600ab873c37f9e73770e)
- [haptics_set_level_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gaedbe20cc622fa0556f7f42ad2013c896)
- [haptics_set_trigger_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gab5616b157b07df317b3447c9536de1d6)
- [haptics_start_output_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gaa6c2ff4b8ed7ae83e4006eb735f61a46)
- [haptics_stop_output_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gae34e538c40e259967f5791cc5ebd2707)
- [haptics_stream_samples_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gaf595a1038d42d991eaacacfd1946dcf8)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [haptics_trigger_t](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface__backend.html#gab6747d8671126a14fcfd54212ffa54bc)
- [haptics_driver_api](../hardware/P149_触觉驱动操作表.md)
- [calibrate](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#aa4297942556ccd525ebd4cc7dfa4fa85)
- [monitor_get](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a244f4d6a7eebaef51743c7ed26779550)
- [monitor_set](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a56961eced0227d3c4dddba5dd28c24b5)
- [register_error_callback](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a269102034face9a4ac30d01a6412cc4d)
- [select_source](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a0dd05cce20499944df6917d1b0da1ff0)
- [set_level](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a50f1036d6cbce31880e9d223a1721fb2)
- [set_trigger](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a09656cbd384b35baf2a671700c7a1b8f)
- [start_output](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a5489147ccfe08d917766bfcb328fa310)
- [stop_output](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#aadbec92f633f42a86458627ecf41a129)
- [stream_samples](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a230bffd452291154f0ad463278836709)
- [trigger](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a59e4e1ed8c0d81118e16e829a5bb2a75)
- [haptics_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaa8a7f36b4b37f7512f9f46133d9f4d1b)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [haptics_monitor_get](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gabf1e580def265fe9bf95f2116d30e6b2)
- [haptics_monitor_set](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gad379139afa8aff76647f180c80706f79)
- [haptics_register_error_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaef1b0ecdbeb529f7f10704d259f2f98f)
- [haptics_select_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga891fa4c05a4844a658603651e8aabfc5)
- [haptics_set_level](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gaae134ab4f57a7301dbc16cb379f08192)
- [haptics_set_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga26851a2c1eafd8da31a3087b0219c6bf)
- [haptics_start_output](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga96e0b0fad35d6535adad7536a9411f44)
- [haptics_stop_output](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga42a5fc7e6b6247316cdf356573dbbb33)
- [haptics_stream_samples](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga94b7c216edd6adf14a354b64dbc8a396)
- [haptics_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#gafb18ed221c2ae5e5b643130bc3d3c8ec)
- [codec.h](https://docs.zephyrproject.org/latest/doxygen/html/codec_8h.html)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [haptics_driver_api::set_trigger](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a09656cbd384b35baf2a671700c7a1b8f)
- [haptics_driver_api::select_source](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a0dd05cce20499944df6917d1b0da1ff0)
- [haptics_driver_api::stream_samples](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a230bffd452291154f0ad463278836709)
- [haptics_driver_api::monitor_get](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a244f4d6a7eebaef51743c7ed26779550)
- [haptics_driver_api::register_error_callback](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a269102034face9a4ac30d01a6412cc4d)
- [haptics_driver_api::set_level](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a50f1036d6cbce31880e9d223a1721fb2)
- [haptics_driver_api::start_output](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a5489147ccfe08d917766bfcb328fa310)
- [haptics_driver_api::monitor_set](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a56961eced0227d3c4dddba5dd28c24b5)
- [haptics_driver_api::trigger](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#a59e4e1ed8c0d81118e16e829a5bb2a75)
- [haptics_driver_api::calibrate](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#aa4297942556ccd525ebd4cc7dfa4fa85)
- [haptics_driver_api::stop_output](https://docs.zephyrproject.org/latest/doxygen/html/structhaptics__driver__api.html#aadbec92f633f42a86458627ecf41a129)
- [haptics_config::idx](https://docs.zephyrproject.org/latest/doxygen/html/unionhaptics__config.html#a69acebb965540a2e65e8d96d13712801)
- [haptics_config::type](https://docs.zephyrproject.org/latest/doxygen/html/unionhaptics__config.html#a7e769e0d9946082ce59001e22fce9abc)
- [haptics_config::dai](https://docs.zephyrproject.org/latest/doxygen/html/unionhaptics__config.html#a95f9bcd56601626b8c97d2e98a3e2abf)
- [haptics_config::cfg](https://docs.zephyrproject.org/latest/doxygen/html/unionhaptics__config.html#aa74e48e60acd1bdbdacd1cff8b3a3ebd)

---

[上一章](P012_fs_interface.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P014_irq.h_源码浏览.md)
