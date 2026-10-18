---
id: learning.zephyr-docs.api-file-reference.page-157
title: zephyr__dt-bindings__power__imx_spc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx__spc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第157章\_zephyr\_\_dt-bindings\_\_power\_\_imx\_spc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/imx__spc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 157.1\_宏定义（Macros）

<a id="r_a0346f0daeb276b819f045132114c74da"></a>

```c
#define IMX_GPC_RUN 0x0
```

相关声明：[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_a1f32dc4faba3158ab48cee77563a5a92"></a>

```c
#define IMX_GPC_WAIT 0x1
```

相关声明：[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_a0bd3da16de75240efaa9dbacc7abc1a9"></a>

```c
#define IMX_GPC_STOP 0x2
```

相关声明：[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a75a363ea77fdfa2a8f922869baf9cae5"></a>

```c
#define IMX_GPC_SUSPEND 0x3
```

相关声明：[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_ac16b45dfd6df94cad425dd8bf2eb0119"></a>

```c
#define IMX_SPC_MASK 0xF0
```

相关声明：[IMX_SPC_MASK](#ac16b45dfd6df94cad425dd8bf2eb0119)。

<a id="r_a626b183ac785be3b2cc9d2e8cbb841f4"></a>

```c
#define IMX_SPC_SHIFT 4
```

相关声明：[IMX_SPC_SHIFT](#a626b183ac785be3b2cc9d2e8cbb841f4)。

<a id="r_a8468498e09c899056ea9f77e686c867a"></a>

```c
#define IMX_GPC_MODE_MASK 0xF
```

相关声明：[IMX_GPC_MODE_MASK](#a8468498e09c899056ea9f77e686c867a)。

<a id="r_ada6ec38357d6bf3ce7f4102744e79bbc"></a>

```c
#define IMX_SPC(x)
```

相关声明：[IMX_SPC](#ada6ec38357d6bf3ce7f4102744e79bbc)。

<a id="r_ae9feac62ff35ec0fef30e75ae0a88bee"></a>

```c
#define IMX_GPC_MODE(x)
```

相关声明：[IMX_GPC_MODE](#ae9feac62ff35ec0fef30e75ae0a88bee)。

<a id="r_a2b91ceadf0b08f329ca48e459be4b8cf"></a>

```c
#define IMX_SPC_0 0x00
```

相关声明：[IMX_SPC_0](#a2b91ceadf0b08f329ca48e459be4b8cf)。

<a id="r_ac01b3b94d1a06a7870a48b3366edee55"></a>

```c
#define IMX_SPC_1 0x10
```

相关声明：[IMX_SPC_1](#ac01b3b94d1a06a7870a48b3366edee55)。

<a id="r_a214286102c951b04eb1a18aed412cd98"></a>

```c
#define IMX_SPC_2 0x20
```

相关声明：[IMX_SPC_2](#a214286102c951b04eb1a18aed412cd98)。

<a id="r_af88f9b163c2a831198506bfc42455a54"></a>

```c
#define IMX_SPC_3 0x30
```

相关声明：[IMX_SPC_3](#af88f9b163c2a831198506bfc42455a54)。

<a id="r_ac36951bfc1258656226275d6eb9bd7da"></a>

```c
#define IMX_SPC_4 0x40
```

相关声明：[IMX_SPC_4](#ac36951bfc1258656226275d6eb9bd7da)。

<a id="r_a0ca2082bf7718bba8a4cbd3cae1e8491"></a>

```c
#define IMX_SPC_5 0x50
```

相关声明：[IMX_SPC_5](#a0ca2082bf7718bba8a4cbd3cae1e8491)。

<a id="r_a97af1d082a356f5ac275fc84c0ca21c7"></a>

```c
#define IMX_SPC_6 0x60
```

相关声明：[IMX_SPC_6](#a97af1d082a356f5ac275fc84c0ca21c7)。

<a id="r_ac73c19b933caae5626297572ee3ff022"></a>

```c
#define IMX_SPC_7 0x70
```

相关声明：[IMX_SPC_7](#ac73c19b933caae5626297572ee3ff022)。

<a id="r_a1d8798b3f2081e9ff647b92e8515cd14"></a>

```c
#define IMX_SPC_8 0x80
```

相关声明：[IMX_SPC_8](#a1d8798b3f2081e9ff647b92e8515cd14)。

<a id="r_a8cde5e61745d8e2b5641f50ab2ceed14"></a>

```c
#define IMX_SPC_9 0x90
```

相关声明：[IMX_SPC_9](#a8cde5e61745d8e2b5641f50ab2ceed14)。

<a id="r_a7b8f4911506984f1ac3fb2b91983a351"></a>

```c
#define IMX_SPC_10 0xA0
```

相关声明：[IMX_SPC_10](#a7b8f4911506984f1ac3fb2b91983a351)。

<a id="r_ac518e5c9a79447934ee3d0f35b3c334b"></a>

```c
#define IMX_SPC_11 0xB0
```

相关声明：[IMX_SPC_11](#ac518e5c9a79447934ee3d0f35b3c334b)。

<a id="r_ab6ceb05e36ef4c24d3a776ddadf2a17b"></a>

```c
#define IMX_SPC_12 0xC0
```

相关声明：[IMX_SPC_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b)。

<a id="r_a5bc88e7c7ec8e9bcda35ad60f671bef5"></a>

```c
#define IMX_SPC_13 0xD0
```

相关声明：[IMX_SPC_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5)。

<a id="r_a11b0cee3cc0d34591c11e1da6aa3e586"></a>

```c
#define IMX_SPC_14 0xE0
```

相关声明：[IMX_SPC_14](#a11b0cee3cc0d34591c11e1da6aa3e586)。

<a id="r_a89c2348f26960a938b7126a631ff4440"></a>

```c
#define IMX_SPC_15 0xF0
```

相关声明：[IMX_SPC_15](#a89c2348f26960a938b7126a631ff4440)。

<a id="r_a2513b235eb5c1d2eef874cde812d66e2"></a>

```c
#define IMX_SPC_SET_POINT_0_RUN (IMX_SPC_0 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_0_RUN](#a2513b235eb5c1d2eef874cde812d66e2)、[IMX_SPC_0](#a2b91ceadf0b08f329ca48e459be4b8cf)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_a655eb9644e0f6edf17055c43beb8bc78"></a>

```c
#define IMX_SPC_SET_POINT_0_WAIT (IMX_SPC_0 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_0_WAIT](#a655eb9644e0f6edf17055c43beb8bc78)、[IMX_SPC_0](#a2b91ceadf0b08f329ca48e459be4b8cf)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_ac0bcab370462ec48cc65c2ad72673e25"></a>

```c
#define IMX_SPC_SET_POINT_0_STOP (IMX_SPC_0 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_0_STOP](#ac0bcab370462ec48cc65c2ad72673e25)、[IMX_SPC_0](#a2b91ceadf0b08f329ca48e459be4b8cf)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_ad9a6bdc024c700869ba4b2a226449498"></a>

```c
#define IMX_SPC_SET_POINT_0_SUSPEND (IMX_SPC_0 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_0_SUSPEND](#ad9a6bdc024c700869ba4b2a226449498)、[IMX_SPC_0](#a2b91ceadf0b08f329ca48e459be4b8cf)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_a675487df773ccd4a478c0ed74ffc1b8d"></a>

```c
#define IMX_SPC_SET_POINT_1_RUN (IMX_SPC_1 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_1_RUN](#a675487df773ccd4a478c0ed74ffc1b8d)、[IMX_SPC_1](#ac01b3b94d1a06a7870a48b3366edee55)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_ad70a5fc9fa6991d212e251223f69845c"></a>

```c
#define IMX_SPC_SET_POINT_1_WAIT (IMX_SPC_1 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_1_WAIT](#ad70a5fc9fa6991d212e251223f69845c)、[IMX_SPC_1](#ac01b3b94d1a06a7870a48b3366edee55)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_abc74b52dbaec59ed1a437a6012737dcb"></a>

```c
#define IMX_SPC_SET_POINT_1_STOP (IMX_SPC_1 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_1_STOP](#abc74b52dbaec59ed1a437a6012737dcb)、[IMX_SPC_1](#ac01b3b94d1a06a7870a48b3366edee55)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a27bb5318452f3bdd359ea77a937ffe51"></a>

```c
#define IMX_SPC_SET_POINT_1_SUSPEND (IMX_SPC_1 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_1_SUSPEND](#a27bb5318452f3bdd359ea77a937ffe51)、[IMX_SPC_1](#ac01b3b94d1a06a7870a48b3366edee55)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_a212b8780e33e35edc68463cbbb656f47"></a>

```c
#define IMX_SPC_SET_POINT_2_RUN (IMX_SPC_2 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_2_RUN](#a212b8780e33e35edc68463cbbb656f47)、[IMX_SPC_2](#a214286102c951b04eb1a18aed412cd98)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_a3e890fdf63a58fd42a0139812550d370"></a>

```c
#define IMX_SPC_SET_POINT_2_WAIT (IMX_SPC_2 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_2_WAIT](#a3e890fdf63a58fd42a0139812550d370)、[IMX_SPC_2](#a214286102c951b04eb1a18aed412cd98)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_aea99f181628c69b96ea093698b4c91fd"></a>

```c
#define IMX_SPC_SET_POINT_2_STOP (IMX_SPC_2 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_2_STOP](#aea99f181628c69b96ea093698b4c91fd)、[IMX_SPC_2](#a214286102c951b04eb1a18aed412cd98)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a0db51a91cb50008bbdc8baf9621ae55c"></a>

```c
#define IMX_SPC_SET_POINT_2_SUSPEND (IMX_SPC_2 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_2_SUSPEND](#a0db51a91cb50008bbdc8baf9621ae55c)、[IMX_SPC_2](#a214286102c951b04eb1a18aed412cd98)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_a955a3993640e5f07be6dbdbac6b2887b"></a>

```c
#define IMX_SPC_SET_POINT_3_RUN (IMX_SPC_3 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_3_RUN](#a955a3993640e5f07be6dbdbac6b2887b)、[IMX_SPC_3](#af88f9b163c2a831198506bfc42455a54)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_a77917334bf2072b01ee996b8b3cdbd0a"></a>

```c
#define IMX_SPC_SET_POINT_3_WAIT (IMX_SPC_3 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_3_WAIT](#a77917334bf2072b01ee996b8b3cdbd0a)、[IMX_SPC_3](#af88f9b163c2a831198506bfc42455a54)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_a0fa20de0d1a6d4b59fb236467ed6eed8"></a>

```c
#define IMX_SPC_SET_POINT_3_STOP (IMX_SPC_3 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_3_STOP](#a0fa20de0d1a6d4b59fb236467ed6eed8)、[IMX_SPC_3](#af88f9b163c2a831198506bfc42455a54)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a320b1171760941ca6220ae445027b2bb"></a>

```c
#define IMX_SPC_SET_POINT_3_SUSPEND (IMX_SPC_3 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_3_SUSPEND](#a320b1171760941ca6220ae445027b2bb)、[IMX_SPC_3](#af88f9b163c2a831198506bfc42455a54)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_a3a875a06de64389b17942fe7096e533b"></a>

```c
#define IMX_SPC_SET_POINT_4_RUN (IMX_SPC_4 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_4_RUN](#a3a875a06de64389b17942fe7096e533b)、[IMX_SPC_4](#ac36951bfc1258656226275d6eb9bd7da)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_a53d8e05a6545202e55c12b9e19723141"></a>

```c
#define IMX_SPC_SET_POINT_4_WAIT (IMX_SPC_4 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_4_WAIT](#a53d8e05a6545202e55c12b9e19723141)、[IMX_SPC_4](#ac36951bfc1258656226275d6eb9bd7da)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_a6f2e970fea0a5b9713a98e6cb5b31060"></a>

```c
#define IMX_SPC_SET_POINT_4_STOP (IMX_SPC_4 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_4_STOP](#a6f2e970fea0a5b9713a98e6cb5b31060)、[IMX_SPC_4](#ac36951bfc1258656226275d6eb9bd7da)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a8b2c95d1accb75acb84d074c6f9554b4"></a>

```c
#define IMX_SPC_SET_POINT_4_SUSPEND (IMX_SPC_4 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_4_SUSPEND](#a8b2c95d1accb75acb84d074c6f9554b4)、[IMX_SPC_4](#ac36951bfc1258656226275d6eb9bd7da)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_a08e368e7fbccdf9910ef41f8054e6ac7"></a>

```c
#define IMX_SPC_SET_POINT_5_RUN (IMX_SPC_5 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_5_RUN](#a08e368e7fbccdf9910ef41f8054e6ac7)、[IMX_SPC_5](#a0ca2082bf7718bba8a4cbd3cae1e8491)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_ab8b90420137da04a8ce432c1b0385613"></a>

```c
#define IMX_SPC_SET_POINT_5_WAIT (IMX_SPC_5 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_5_WAIT](#ab8b90420137da04a8ce432c1b0385613)、[IMX_SPC_5](#a0ca2082bf7718bba8a4cbd3cae1e8491)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_a2111e4b8468791f5062bc1fafba1e871"></a>

```c
#define IMX_SPC_SET_POINT_5_STOP (IMX_SPC_5 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_5_STOP](#a2111e4b8468791f5062bc1fafba1e871)、[IMX_SPC_5](#a0ca2082bf7718bba8a4cbd3cae1e8491)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a14047d119208c1c188d28e3fef2286cf"></a>

```c
#define IMX_SPC_SET_POINT_5_SUSPEND (IMX_SPC_5 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_5_SUSPEND](#a14047d119208c1c188d28e3fef2286cf)、[IMX_SPC_5](#a0ca2082bf7718bba8a4cbd3cae1e8491)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_ae667a3617c9389bef9d08f3d4a639731"></a>

```c
#define IMX_SPC_SET_POINT_6_RUN (IMX_SPC_6 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_6_RUN](#ae667a3617c9389bef9d08f3d4a639731)、[IMX_SPC_6](#a97af1d082a356f5ac275fc84c0ca21c7)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_aaf448cdd4b85f7c7417e5de766361035"></a>

```c
#define IMX_SPC_SET_POINT_6_WAIT (IMX_SPC_6 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_6_WAIT](#aaf448cdd4b85f7c7417e5de766361035)、[IMX_SPC_6](#a97af1d082a356f5ac275fc84c0ca21c7)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_ab8f1fe76f07af84111d2532d4205a01c"></a>

```c
#define IMX_SPC_SET_POINT_6_STOP (IMX_SPC_6 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_6_STOP](#ab8f1fe76f07af84111d2532d4205a01c)、[IMX_SPC_6](#a97af1d082a356f5ac275fc84c0ca21c7)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_ae977b643f59534d5df555e6aa283a82d"></a>

```c
#define IMX_SPC_SET_POINT_6_SUSPEND (IMX_SPC_6 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_6_SUSPEND](#ae977b643f59534d5df555e6aa283a82d)、[IMX_SPC_6](#a97af1d082a356f5ac275fc84c0ca21c7)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_a4edbee6f04031c2c8f2b835d0e100bf3"></a>

```c
#define IMX_SPC_SET_POINT_7_RUN (IMX_SPC_7 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_7_RUN](#a4edbee6f04031c2c8f2b835d0e100bf3)、[IMX_SPC_7](#ac73c19b933caae5626297572ee3ff022)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_a78e453e0425752c8bb636cd45e9f66a5"></a>

```c
#define IMX_SPC_SET_POINT_7_WAIT (IMX_SPC_7 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_7_WAIT](#a78e453e0425752c8bb636cd45e9f66a5)、[IMX_SPC_7](#ac73c19b933caae5626297572ee3ff022)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_a996d39beaa9490adf49c602f325ebe04"></a>

```c
#define IMX_SPC_SET_POINT_7_STOP (IMX_SPC_7 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_7_STOP](#a996d39beaa9490adf49c602f325ebe04)、[IMX_SPC_7](#ac73c19b933caae5626297572ee3ff022)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a9b90dd5fd6f801e27a95e02f6e7614d7"></a>

```c
#define IMX_SPC_SET_POINT_7_SUSPEND (IMX_SPC_7 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_7_SUSPEND](#a9b90dd5fd6f801e27a95e02f6e7614d7)、[IMX_SPC_7](#ac73c19b933caae5626297572ee3ff022)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_acbfdb5f70d7f4aee7435f5ca6d014596"></a>

```c
#define IMX_SPC_SET_POINT_8_RUN (IMX_SPC_8 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_8_RUN](#acbfdb5f70d7f4aee7435f5ca6d014596)、[IMX_SPC_8](#a1d8798b3f2081e9ff647b92e8515cd14)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_a402e534a33588b1f3b31d0a7284d32ab"></a>

```c
#define IMX_SPC_SET_POINT_8_WAIT (IMX_SPC_8 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_8_WAIT](#a402e534a33588b1f3b31d0a7284d32ab)、[IMX_SPC_8](#a1d8798b3f2081e9ff647b92e8515cd14)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_a4f2f29f9e4bb420436d881b8233a43b5"></a>

```c
#define IMX_SPC_SET_POINT_8_STOP (IMX_SPC_8 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_8_STOP](#a4f2f29f9e4bb420436d881b8233a43b5)、[IMX_SPC_8](#a1d8798b3f2081e9ff647b92e8515cd14)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a686e1a2d26bc3df4d465614da82bae08"></a>

```c
#define IMX_SPC_SET_POINT_8_SUSPEND (IMX_SPC_8 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_8_SUSPEND](#a686e1a2d26bc3df4d465614da82bae08)、[IMX_SPC_8](#a1d8798b3f2081e9ff647b92e8515cd14)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_ab591869ecb6606cdf1e73cc3849f611d"></a>

```c
#define IMX_SPC_SET_POINT_9_RUN (IMX_SPC_9 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_9_RUN](#ab591869ecb6606cdf1e73cc3849f611d)、[IMX_SPC_9](#a8cde5e61745d8e2b5641f50ab2ceed14)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_ad234e9dd6516742f9d8869fda039a5c1"></a>

```c
#define IMX_SPC_SET_POINT_9_WAIT (IMX_SPC_9 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_9_WAIT](#ad234e9dd6516742f9d8869fda039a5c1)、[IMX_SPC_9](#a8cde5e61745d8e2b5641f50ab2ceed14)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_a9696110f23d443b540cbfa8aedd25e9b"></a>

```c
#define IMX_SPC_SET_POINT_9_STOP (IMX_SPC_9 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_9_STOP](#a9696110f23d443b540cbfa8aedd25e9b)、[IMX_SPC_9](#a8cde5e61745d8e2b5641f50ab2ceed14)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a8e6427bd9509ffb3b51f18b62753340c"></a>

```c
#define IMX_SPC_SET_POINT_9_SUSPEND (IMX_SPC_9 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_9_SUSPEND](#a8e6427bd9509ffb3b51f18b62753340c)、[IMX_SPC_9](#a8cde5e61745d8e2b5641f50ab2ceed14)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_a7be6d85aa76e65805716c2bf20553fae"></a>

```c
#define IMX_SPC_SET_POINT_10_RUN (IMX_SPC_10 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_10_RUN](#a7be6d85aa76e65805716c2bf20553fae)、[IMX_SPC_10](#a7b8f4911506984f1ac3fb2b91983a351)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_a57e3cbbf5409c9b634a67d381f81b36c"></a>

```c
#define IMX_SPC_SET_POINT_10_WAIT (IMX_SPC_10 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_10_WAIT](#a57e3cbbf5409c9b634a67d381f81b36c)、[IMX_SPC_10](#a7b8f4911506984f1ac3fb2b91983a351)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_a61e070d9c04cea7c4e0f7fb3ff703718"></a>

```c
#define IMX_SPC_SET_POINT_10_STOP (IMX_SPC_10 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_10_STOP](#a61e070d9c04cea7c4e0f7fb3ff703718)、[IMX_SPC_10](#a7b8f4911506984f1ac3fb2b91983a351)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a2d6aecb9ac2033ca89ca673c6786fe61"></a>

```c
#define IMX_SPC_SET_POINT_10_SUSPEND (IMX_SPC_10 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_10_SUSPEND](#a2d6aecb9ac2033ca89ca673c6786fe61)、[IMX_SPC_10](#a7b8f4911506984f1ac3fb2b91983a351)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_ade582b07da3be853835863e2c4efd1fe"></a>

```c
#define IMX_SPC_SET_POINT_11_RUN (IMX_SPC_11 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_11_RUN](#ade582b07da3be853835863e2c4efd1fe)、[IMX_SPC_11](#ac518e5c9a79447934ee3d0f35b3c334b)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_ad81fd8b58c73dd88f869fbe99e45af62"></a>

```c
#define IMX_SPC_SET_POINT_11_WAIT (IMX_SPC_11 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_11_WAIT](#ad81fd8b58c73dd88f869fbe99e45af62)、[IMX_SPC_11](#ac518e5c9a79447934ee3d0f35b3c334b)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_af328d05fc2f3084025426bcfa8e07acb"></a>

```c
#define IMX_SPC_SET_POINT_11_STOP (IMX_SPC_11 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_11_STOP](#af328d05fc2f3084025426bcfa8e07acb)、[IMX_SPC_11](#ac518e5c9a79447934ee3d0f35b3c334b)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_aa84a574b06d37679035c9e160794103b"></a>

```c
#define IMX_SPC_SET_POINT_11_SUSPEND (IMX_SPC_11 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_11_SUSPEND](#aa84a574b06d37679035c9e160794103b)、[IMX_SPC_11](#ac518e5c9a79447934ee3d0f35b3c334b)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_aa4b08d6e86e2a0786aa4b8467063e744"></a>

```c
#define IMX_SPC_SET_POINT_12_RUN (IMX_SPC_12 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_12_RUN](#aa4b08d6e86e2a0786aa4b8467063e744)、[IMX_SPC_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_a06f577fcd7a7039930f5cd60f10dbdbb"></a>

```c
#define IMX_SPC_SET_POINT_12_WAIT (IMX_SPC_12 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_12_WAIT](#a06f577fcd7a7039930f5cd60f10dbdbb)、[IMX_SPC_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_a82f472da9010bb1de1a74837d1b2eae7"></a>

```c
#define IMX_SPC_SET_POINT_12_STOP (IMX_SPC_12 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_12_STOP](#a82f472da9010bb1de1a74837d1b2eae7)、[IMX_SPC_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a393fdb54cd063085108b8d600653e3a3"></a>

```c
#define IMX_SPC_SET_POINT_12_SUSPEND (IMX_SPC_12 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_12_SUSPEND](#a393fdb54cd063085108b8d600653e3a3)、[IMX_SPC_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_aa62f55fa30c7fe258eb5bce336914b74"></a>

```c
#define IMX_SPC_SET_POINT_13_RUN (IMX_SPC_13 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_13_RUN](#aa62f55fa30c7fe258eb5bce336914b74)、[IMX_SPC_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_a9603a1be5b8faf232c06f39526052992"></a>

```c
#define IMX_SPC_SET_POINT_13_WAIT (IMX_SPC_13 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_13_WAIT](#a9603a1be5b8faf232c06f39526052992)、[IMX_SPC_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_a1c1e481a627910fee5786560815a7442"></a>

```c
#define IMX_SPC_SET_POINT_13_STOP (IMX_SPC_13 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_13_STOP](#a1c1e481a627910fee5786560815a7442)、[IMX_SPC_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a2e56fe135af350c5ebd92196cdca8067"></a>

```c
#define IMX_SPC_SET_POINT_13_SUSPEND (IMX_SPC_13 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_13_SUSPEND](#a2e56fe135af350c5ebd92196cdca8067)、[IMX_SPC_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_a23f38fd1002d77d327a84ad8ca5e3d22"></a>

```c
#define IMX_SPC_SET_POINT_14_RUN (IMX_SPC_14 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_14_RUN](#a23f38fd1002d77d327a84ad8ca5e3d22)、[IMX_SPC_14](#a11b0cee3cc0d34591c11e1da6aa3e586)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_abbda3ffc097e0cbba6f4a529215899f0"></a>

```c
#define IMX_SPC_SET_POINT_14_WAIT (IMX_SPC_14 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_14_WAIT](#abbda3ffc097e0cbba6f4a529215899f0)、[IMX_SPC_14](#a11b0cee3cc0d34591c11e1da6aa3e586)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_addc192b8864a96a935e983021fd6991b"></a>

```c
#define IMX_SPC_SET_POINT_14_STOP (IMX_SPC_14 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_14_STOP](#addc192b8864a96a935e983021fd6991b)、[IMX_SPC_14](#a11b0cee3cc0d34591c11e1da6aa3e586)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_adabea62f128c40438f1edb29d597accd"></a>

```c
#define IMX_SPC_SET_POINT_14_SUSPEND (IMX_SPC_14 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_14_SUSPEND](#adabea62f128c40438f1edb29d597accd)、[IMX_SPC_14](#a11b0cee3cc0d34591c11e1da6aa3e586)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

<a id="r_a0efa4fa53bce64f0c89f9d4eb07ba27d"></a>

```c
#define IMX_SPC_SET_POINT_15_RUN (IMX_SPC_15 | IMX_GPC_RUN)
```

相关声明：[IMX_SPC_SET_POINT_15_RUN](#a0efa4fa53bce64f0c89f9d4eb07ba27d)、[IMX_SPC_15](#a89c2348f26960a938b7126a631ff4440)、[IMX_GPC_RUN](#a0346f0daeb276b819f045132114c74da)。

<a id="r_af691cffe687076e6ac2f03db06f9b48f"></a>

```c
#define IMX_SPC_SET_POINT_15_WAIT (IMX_SPC_15 | IMX_GPC_WAIT)
```

相关声明：[IMX_SPC_SET_POINT_15_WAIT](#af691cffe687076e6ac2f03db06f9b48f)、[IMX_SPC_15](#a89c2348f26960a938b7126a631ff4440)、[IMX_GPC_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)。

<a id="r_a6a24e7b3e0e9e3a1ba0dd2984bd9fde6"></a>

```c
#define IMX_SPC_SET_POINT_15_STOP (IMX_SPC_15 | IMX_GPC_STOP)
```

相关声明：[IMX_SPC_SET_POINT_15_STOP](#a6a24e7b3e0e9e3a1ba0dd2984bd9fde6)、[IMX_SPC_15](#a89c2348f26960a938b7126a631ff4440)、[IMX_GPC_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)。

<a id="r_a1eade5203e39d0892c2f9eba8fd023f9"></a>

```c
#define IMX_SPC_SET_POINT_15_SUSPEND (IMX_SPC_15 | IMX_GPC_SUSPEND)
```

相关声明：[IMX_SPC_SET_POINT_15_SUSPEND](#a1eade5203e39d0892c2f9eba8fd023f9)、[IMX_SPC_15](#a89c2348f26960a938b7126a631ff4440)、[IMX_GPC_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)。

## 157.2\_详细说明（Detailed Documentation）

<a id="ae9feac62ff35ec0fef30e75ae0a88bee"></a>

### `IMX_GPC_MODE`

```c
#define IMX_GPC_MODE ( x)
```

展开值（Value）：

```c
(x & IMX_GPC_MODE_MASK)
```

<a id="a8468498e09c899056ea9f77e686c867a"></a>

### `IMX_GPC_MODE_MASK`

```c
#define IMX_GPC_MODE_MASK 0xF
```

<a id="a0346f0daeb276b819f045132114c74da"></a>

### `IMX_GPC_RUN`

```c
#define IMX_GPC_RUN 0x0
```

<a id="a0bd3da16de75240efaa9dbacc7abc1a9"></a>

### `IMX_GPC_STOP`

```c
#define IMX_GPC_STOP 0x2
```

<a id="a75a363ea77fdfa2a8f922869baf9cae5"></a>

### `IMX_GPC_SUSPEND`

```c
#define IMX_GPC_SUSPEND 0x3
```

<a id="a1f32dc4faba3158ab48cee77563a5a92"></a>

### `IMX_GPC_WAIT`

```c
#define IMX_GPC_WAIT 0x1
```

<a id="ada6ec38357d6bf3ce7f4102744e79bbc"></a>

### `IMX_SPC`

```c
#define IMX_SPC ( x)
```

展开值（Value）：

```c
((x & IMX_SPC_MASK) >> IMX_SPC_SHIFT)
```

<a id="a2b91ceadf0b08f329ca48e459be4b8cf"></a>

### `IMX_SPC_0`

```c
#define IMX_SPC_0 0x00
```

<a id="ac01b3b94d1a06a7870a48b3366edee55"></a>

### `IMX_SPC_1`

```c
#define IMX_SPC_1 0x10
```

<a id="a7b8f4911506984f1ac3fb2b91983a351"></a>

### `IMX_SPC_10`

```c
#define IMX_SPC_10 0xA0
```

<a id="ac518e5c9a79447934ee3d0f35b3c334b"></a>

### `IMX_SPC_11`

```c
#define IMX_SPC_11 0xB0
```

<a id="ab6ceb05e36ef4c24d3a776ddadf2a17b"></a>

### `IMX_SPC_12`

```c
#define IMX_SPC_12 0xC0
```

<a id="a5bc88e7c7ec8e9bcda35ad60f671bef5"></a>

### `IMX_SPC_13`

```c
#define IMX_SPC_13 0xD0
```

<a id="a11b0cee3cc0d34591c11e1da6aa3e586"></a>

### `IMX_SPC_14`

```c
#define IMX_SPC_14 0xE0
```

<a id="a89c2348f26960a938b7126a631ff4440"></a>

### `IMX_SPC_15`

```c
#define IMX_SPC_15 0xF0
```

<a id="a214286102c951b04eb1a18aed412cd98"></a>

### `IMX_SPC_2`

```c
#define IMX_SPC_2 0x20
```

<a id="af88f9b163c2a831198506bfc42455a54"></a>

### `IMX_SPC_3`

```c
#define IMX_SPC_3 0x30
```

<a id="ac36951bfc1258656226275d6eb9bd7da"></a>

### `IMX_SPC_4`

```c
#define IMX_SPC_4 0x40
```

<a id="a0ca2082bf7718bba8a4cbd3cae1e8491"></a>

### `IMX_SPC_5`

```c
#define IMX_SPC_5 0x50
```

<a id="a97af1d082a356f5ac275fc84c0ca21c7"></a>

### `IMX_SPC_6`

```c
#define IMX_SPC_6 0x60
```

<a id="ac73c19b933caae5626297572ee3ff022"></a>

### `IMX_SPC_7`

```c
#define IMX_SPC_7 0x70
```

<a id="a1d8798b3f2081e9ff647b92e8515cd14"></a>

### `IMX_SPC_8`

```c
#define IMX_SPC_8 0x80
```

<a id="a8cde5e61745d8e2b5641f50ab2ceed14"></a>

### `IMX_SPC_9`

```c
#define IMX_SPC_9 0x90
```

<a id="ac16b45dfd6df94cad425dd8bf2eb0119"></a>

### `IMX_SPC_MASK`

```c
#define IMX_SPC_MASK 0xF0
```

<a id="a2513b235eb5c1d2eef874cde812d66e2"></a>

### `IMX_SPC_SET_POINT_0_RUN`

```c
#define IMX_SPC_SET_POINT_0_RUN (IMX_SPC_0 | IMX_GPC_RUN)
```

<a id="ac0bcab370462ec48cc65c2ad72673e25"></a>

### `IMX_SPC_SET_POINT_0_STOP`

```c
#define IMX_SPC_SET_POINT_0_STOP (IMX_SPC_0 | IMX_GPC_STOP)
```

<a id="ad9a6bdc024c700869ba4b2a226449498"></a>

### `IMX_SPC_SET_POINT_0_SUSPEND`

```c
#define IMX_SPC_SET_POINT_0_SUSPEND (IMX_SPC_0 | IMX_GPC_SUSPEND)
```

<a id="a655eb9644e0f6edf17055c43beb8bc78"></a>

### `IMX_SPC_SET_POINT_0_WAIT`

```c
#define IMX_SPC_SET_POINT_0_WAIT (IMX_SPC_0 | IMX_GPC_WAIT)
```

<a id="a7be6d85aa76e65805716c2bf20553fae"></a>

### `IMX_SPC_SET_POINT_10_RUN`

```c
#define IMX_SPC_SET_POINT_10_RUN (IMX_SPC_10 | IMX_GPC_RUN)
```

<a id="a61e070d9c04cea7c4e0f7fb3ff703718"></a>

### `IMX_SPC_SET_POINT_10_STOP`

```c
#define IMX_SPC_SET_POINT_10_STOP (IMX_SPC_10 | IMX_GPC_STOP)
```

<a id="a2d6aecb9ac2033ca89ca673c6786fe61"></a>

### `IMX_SPC_SET_POINT_10_SUSPEND`

```c
#define IMX_SPC_SET_POINT_10_SUSPEND (IMX_SPC_10 | IMX_GPC_SUSPEND)
```

<a id="a57e3cbbf5409c9b634a67d381f81b36c"></a>

### `IMX_SPC_SET_POINT_10_WAIT`

```c
#define IMX_SPC_SET_POINT_10_WAIT (IMX_SPC_10 | IMX_GPC_WAIT)
```

<a id="ade582b07da3be853835863e2c4efd1fe"></a>

### `IMX_SPC_SET_POINT_11_RUN`

```c
#define IMX_SPC_SET_POINT_11_RUN (IMX_SPC_11 | IMX_GPC_RUN)
```

<a id="af328d05fc2f3084025426bcfa8e07acb"></a>

### `IMX_SPC_SET_POINT_11_STOP`

```c
#define IMX_SPC_SET_POINT_11_STOP (IMX_SPC_11 | IMX_GPC_STOP)
```

<a id="aa84a574b06d37679035c9e160794103b"></a>

### `IMX_SPC_SET_POINT_11_SUSPEND`

```c
#define IMX_SPC_SET_POINT_11_SUSPEND (IMX_SPC_11 | IMX_GPC_SUSPEND)
```

<a id="ad81fd8b58c73dd88f869fbe99e45af62"></a>

### `IMX_SPC_SET_POINT_11_WAIT`

```c
#define IMX_SPC_SET_POINT_11_WAIT (IMX_SPC_11 | IMX_GPC_WAIT)
```

<a id="aa4b08d6e86e2a0786aa4b8467063e744"></a>

### `IMX_SPC_SET_POINT_12_RUN`

```c
#define IMX_SPC_SET_POINT_12_RUN (IMX_SPC_12 | IMX_GPC_RUN)
```

<a id="a82f472da9010bb1de1a74837d1b2eae7"></a>

### `IMX_SPC_SET_POINT_12_STOP`

```c
#define IMX_SPC_SET_POINT_12_STOP (IMX_SPC_12 | IMX_GPC_STOP)
```

<a id="a393fdb54cd063085108b8d600653e3a3"></a>

### `IMX_SPC_SET_POINT_12_SUSPEND`

```c
#define IMX_SPC_SET_POINT_12_SUSPEND (IMX_SPC_12 | IMX_GPC_SUSPEND)
```

<a id="a06f577fcd7a7039930f5cd60f10dbdbb"></a>

### `IMX_SPC_SET_POINT_12_WAIT`

```c
#define IMX_SPC_SET_POINT_12_WAIT (IMX_SPC_12 | IMX_GPC_WAIT)
```

<a id="aa62f55fa30c7fe258eb5bce336914b74"></a>

### `IMX_SPC_SET_POINT_13_RUN`

```c
#define IMX_SPC_SET_POINT_13_RUN (IMX_SPC_13 | IMX_GPC_RUN)
```

<a id="a1c1e481a627910fee5786560815a7442"></a>

### `IMX_SPC_SET_POINT_13_STOP`

```c
#define IMX_SPC_SET_POINT_13_STOP (IMX_SPC_13 | IMX_GPC_STOP)
```

<a id="a2e56fe135af350c5ebd92196cdca8067"></a>

### `IMX_SPC_SET_POINT_13_SUSPEND`

```c
#define IMX_SPC_SET_POINT_13_SUSPEND (IMX_SPC_13 | IMX_GPC_SUSPEND)
```

<a id="a9603a1be5b8faf232c06f39526052992"></a>

### `IMX_SPC_SET_POINT_13_WAIT`

```c
#define IMX_SPC_SET_POINT_13_WAIT (IMX_SPC_13 | IMX_GPC_WAIT)
```

<a id="a23f38fd1002d77d327a84ad8ca5e3d22"></a>

### `IMX_SPC_SET_POINT_14_RUN`

```c
#define IMX_SPC_SET_POINT_14_RUN (IMX_SPC_14 | IMX_GPC_RUN)
```

<a id="addc192b8864a96a935e983021fd6991b"></a>

### `IMX_SPC_SET_POINT_14_STOP`

```c
#define IMX_SPC_SET_POINT_14_STOP (IMX_SPC_14 | IMX_GPC_STOP)
```

<a id="adabea62f128c40438f1edb29d597accd"></a>

### `IMX_SPC_SET_POINT_14_SUSPEND`

```c
#define IMX_SPC_SET_POINT_14_SUSPEND (IMX_SPC_14 | IMX_GPC_SUSPEND)
```

<a id="abbda3ffc097e0cbba6f4a529215899f0"></a>

### `IMX_SPC_SET_POINT_14_WAIT`

```c
#define IMX_SPC_SET_POINT_14_WAIT (IMX_SPC_14 | IMX_GPC_WAIT)
```

<a id="a0efa4fa53bce64f0c89f9d4eb07ba27d"></a>

### `IMX_SPC_SET_POINT_15_RUN`

```c
#define IMX_SPC_SET_POINT_15_RUN (IMX_SPC_15 | IMX_GPC_RUN)
```

<a id="a6a24e7b3e0e9e3a1ba0dd2984bd9fde6"></a>

### `IMX_SPC_SET_POINT_15_STOP`

```c
#define IMX_SPC_SET_POINT_15_STOP (IMX_SPC_15 | IMX_GPC_STOP)
```

<a id="a1eade5203e39d0892c2f9eba8fd023f9"></a>

### `IMX_SPC_SET_POINT_15_SUSPEND`

```c
#define IMX_SPC_SET_POINT_15_SUSPEND (IMX_SPC_15 | IMX_GPC_SUSPEND)
```

<a id="af691cffe687076e6ac2f03db06f9b48f"></a>

### `IMX_SPC_SET_POINT_15_WAIT`

```c
#define IMX_SPC_SET_POINT_15_WAIT (IMX_SPC_15 | IMX_GPC_WAIT)
```

<a id="a675487df773ccd4a478c0ed74ffc1b8d"></a>

### `IMX_SPC_SET_POINT_1_RUN`

```c
#define IMX_SPC_SET_POINT_1_RUN (IMX_SPC_1 | IMX_GPC_RUN)
```

<a id="abc74b52dbaec59ed1a437a6012737dcb"></a>

### `IMX_SPC_SET_POINT_1_STOP`

```c
#define IMX_SPC_SET_POINT_1_STOP (IMX_SPC_1 | IMX_GPC_STOP)
```

<a id="a27bb5318452f3bdd359ea77a937ffe51"></a>

### `IMX_SPC_SET_POINT_1_SUSPEND`

```c
#define IMX_SPC_SET_POINT_1_SUSPEND (IMX_SPC_1 | IMX_GPC_SUSPEND)
```

<a id="ad70a5fc9fa6991d212e251223f69845c"></a>

### `IMX_SPC_SET_POINT_1_WAIT`

```c
#define IMX_SPC_SET_POINT_1_WAIT (IMX_SPC_1 | IMX_GPC_WAIT)
```

<a id="a212b8780e33e35edc68463cbbb656f47"></a>

### `IMX_SPC_SET_POINT_2_RUN`

```c
#define IMX_SPC_SET_POINT_2_RUN (IMX_SPC_2 | IMX_GPC_RUN)
```

<a id="aea99f181628c69b96ea093698b4c91fd"></a>

### `IMX_SPC_SET_POINT_2_STOP`

```c
#define IMX_SPC_SET_POINT_2_STOP (IMX_SPC_2 | IMX_GPC_STOP)
```

<a id="a0db51a91cb50008bbdc8baf9621ae55c"></a>

### `IMX_SPC_SET_POINT_2_SUSPEND`

```c
#define IMX_SPC_SET_POINT_2_SUSPEND (IMX_SPC_2 | IMX_GPC_SUSPEND)
```

<a id="a3e890fdf63a58fd42a0139812550d370"></a>

### `IMX_SPC_SET_POINT_2_WAIT`

```c
#define IMX_SPC_SET_POINT_2_WAIT (IMX_SPC_2 | IMX_GPC_WAIT)
```

<a id="a955a3993640e5f07be6dbdbac6b2887b"></a>

### `IMX_SPC_SET_POINT_3_RUN`

```c
#define IMX_SPC_SET_POINT_3_RUN (IMX_SPC_3 | IMX_GPC_RUN)
```

<a id="a0fa20de0d1a6d4b59fb236467ed6eed8"></a>

### `IMX_SPC_SET_POINT_3_STOP`

```c
#define IMX_SPC_SET_POINT_3_STOP (IMX_SPC_3 | IMX_GPC_STOP)
```

<a id="a320b1171760941ca6220ae445027b2bb"></a>

### `IMX_SPC_SET_POINT_3_SUSPEND`

```c
#define IMX_SPC_SET_POINT_3_SUSPEND (IMX_SPC_3 | IMX_GPC_SUSPEND)
```

<a id="a77917334bf2072b01ee996b8b3cdbd0a"></a>

### `IMX_SPC_SET_POINT_3_WAIT`

```c
#define IMX_SPC_SET_POINT_3_WAIT (IMX_SPC_3 | IMX_GPC_WAIT)
```

<a id="a3a875a06de64389b17942fe7096e533b"></a>

### `IMX_SPC_SET_POINT_4_RUN`

```c
#define IMX_SPC_SET_POINT_4_RUN (IMX_SPC_4 | IMX_GPC_RUN)
```

<a id="a6f2e970fea0a5b9713a98e6cb5b31060"></a>

### `IMX_SPC_SET_POINT_4_STOP`

```c
#define IMX_SPC_SET_POINT_4_STOP (IMX_SPC_4 | IMX_GPC_STOP)
```

<a id="a8b2c95d1accb75acb84d074c6f9554b4"></a>

### `IMX_SPC_SET_POINT_4_SUSPEND`

```c
#define IMX_SPC_SET_POINT_4_SUSPEND (IMX_SPC_4 | IMX_GPC_SUSPEND)
```

<a id="a53d8e05a6545202e55c12b9e19723141"></a>

### `IMX_SPC_SET_POINT_4_WAIT`

```c
#define IMX_SPC_SET_POINT_4_WAIT (IMX_SPC_4 | IMX_GPC_WAIT)
```

<a id="a08e368e7fbccdf9910ef41f8054e6ac7"></a>

### `IMX_SPC_SET_POINT_5_RUN`

```c
#define IMX_SPC_SET_POINT_5_RUN (IMX_SPC_5 | IMX_GPC_RUN)
```

<a id="a2111e4b8468791f5062bc1fafba1e871"></a>

### `IMX_SPC_SET_POINT_5_STOP`

```c
#define IMX_SPC_SET_POINT_5_STOP (IMX_SPC_5 | IMX_GPC_STOP)
```

<a id="a14047d119208c1c188d28e3fef2286cf"></a>

### `IMX_SPC_SET_POINT_5_SUSPEND`

```c
#define IMX_SPC_SET_POINT_5_SUSPEND (IMX_SPC_5 | IMX_GPC_SUSPEND)
```

<a id="ab8b90420137da04a8ce432c1b0385613"></a>

### `IMX_SPC_SET_POINT_5_WAIT`

```c
#define IMX_SPC_SET_POINT_5_WAIT (IMX_SPC_5 | IMX_GPC_WAIT)
```

<a id="ae667a3617c9389bef9d08f3d4a639731"></a>

### `IMX_SPC_SET_POINT_6_RUN`

```c
#define IMX_SPC_SET_POINT_6_RUN (IMX_SPC_6 | IMX_GPC_RUN)
```

<a id="ab8f1fe76f07af84111d2532d4205a01c"></a>

### `IMX_SPC_SET_POINT_6_STOP`

```c
#define IMX_SPC_SET_POINT_6_STOP (IMX_SPC_6 | IMX_GPC_STOP)
```

<a id="ae977b643f59534d5df555e6aa283a82d"></a>

### `IMX_SPC_SET_POINT_6_SUSPEND`

```c
#define IMX_SPC_SET_POINT_6_SUSPEND (IMX_SPC_6 | IMX_GPC_SUSPEND)
```

<a id="aaf448cdd4b85f7c7417e5de766361035"></a>

### `IMX_SPC_SET_POINT_6_WAIT`

```c
#define IMX_SPC_SET_POINT_6_WAIT (IMX_SPC_6 | IMX_GPC_WAIT)
```

<a id="a4edbee6f04031c2c8f2b835d0e100bf3"></a>

### `IMX_SPC_SET_POINT_7_RUN`

```c
#define IMX_SPC_SET_POINT_7_RUN (IMX_SPC_7 | IMX_GPC_RUN)
```

<a id="a996d39beaa9490adf49c602f325ebe04"></a>

### `IMX_SPC_SET_POINT_7_STOP`

```c
#define IMX_SPC_SET_POINT_7_STOP (IMX_SPC_7 | IMX_GPC_STOP)
```

<a id="a9b90dd5fd6f801e27a95e02f6e7614d7"></a>

### `IMX_SPC_SET_POINT_7_SUSPEND`

```c
#define IMX_SPC_SET_POINT_7_SUSPEND (IMX_SPC_7 | IMX_GPC_SUSPEND)
```

<a id="a78e453e0425752c8bb636cd45e9f66a5"></a>

### `IMX_SPC_SET_POINT_7_WAIT`

```c
#define IMX_SPC_SET_POINT_7_WAIT (IMX_SPC_7 | IMX_GPC_WAIT)
```

<a id="acbfdb5f70d7f4aee7435f5ca6d014596"></a>

### `IMX_SPC_SET_POINT_8_RUN`

```c
#define IMX_SPC_SET_POINT_8_RUN (IMX_SPC_8 | IMX_GPC_RUN)
```

<a id="a4f2f29f9e4bb420436d881b8233a43b5"></a>

### `IMX_SPC_SET_POINT_8_STOP`

```c
#define IMX_SPC_SET_POINT_8_STOP (IMX_SPC_8 | IMX_GPC_STOP)
```

<a id="a686e1a2d26bc3df4d465614da82bae08"></a>

### `IMX_SPC_SET_POINT_8_SUSPEND`

```c
#define IMX_SPC_SET_POINT_8_SUSPEND (IMX_SPC_8 | IMX_GPC_SUSPEND)
```

<a id="a402e534a33588b1f3b31d0a7284d32ab"></a>

### `IMX_SPC_SET_POINT_8_WAIT`

```c
#define IMX_SPC_SET_POINT_8_WAIT (IMX_SPC_8 | IMX_GPC_WAIT)
```

<a id="ab591869ecb6606cdf1e73cc3849f611d"></a>

### `IMX_SPC_SET_POINT_9_RUN`

```c
#define IMX_SPC_SET_POINT_9_RUN (IMX_SPC_9 | IMX_GPC_RUN)
```

<a id="a9696110f23d443b540cbfa8aedd25e9b"></a>

### `IMX_SPC_SET_POINT_9_STOP`

```c
#define IMX_SPC_SET_POINT_9_STOP (IMX_SPC_9 | IMX_GPC_STOP)
```

<a id="a8e6427bd9509ffb3b51f18b62753340c"></a>

### `IMX_SPC_SET_POINT_9_SUSPEND`

```c
#define IMX_SPC_SET_POINT_9_SUSPEND (IMX_SPC_9 | IMX_GPC_SUSPEND)
```

<a id="ad234e9dd6516742f9d8869fda039a5c1"></a>

### `IMX_SPC_SET_POINT_9_WAIT`

```c
#define IMX_SPC_SET_POINT_9_WAIT (IMX_SPC_9 | IMX_GPC_WAIT)
```

<a id="a626b183ac785be3b2cc9d2e8cbb841f4"></a>

### `IMX_SPC_SHIFT`

```c
#define IMX_SPC_SHIFT 4
```


## 157.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P092_imx_spc.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aimx__spc_8h_html_a8468498e09c899056ea9f77e686c867a"></a>
<a id="aimx__spc_8h_html_a626b183ac785be3b2cc9d2e8cbb841f4"></a>
<a id="aimx__spc_8h_html_ac16b45dfd6df94cad425dd8bf2eb0119"></a>

---

[上一章](P156_zephyr__dt-bindings__power__imx_scu_rsrc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P158_zephyr__posix__netinet__in.h_文件参考.md)
