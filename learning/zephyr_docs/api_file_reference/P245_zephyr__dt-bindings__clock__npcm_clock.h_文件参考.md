---
id: learning.zephyr-docs.api-file-reference.page-245
title: zephyr__dt-bindings__clock__npcm_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npcm__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第245章\_zephyr\_\_dt-bindings\_\_clock\_\_npcm\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/npcm__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 245.1\_宏定义（Macros）

<a id="r_aedf3c4059e2dba237097428dd3d17c86"></a>

```c
#define NPCM_CLOCK_GROUP_OFFSET(N)
```

相关声明：[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a63e02592f717f0575db06065c5abf7f9"></a>

```c
#define NPCM_CLOCK_PWM_I (NPCM_CLOCK_GROUP_OFFSET(0) + 0)
```

相关声明：[NPCM_CLOCK_PWM_I](#a63e02592f717f0575db06065c5abf7f9)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a34ece572167371f620570db82dc99a0e"></a>

```c
#define NPCM_CLOCK_PWM_J (NPCM_CLOCK_GROUP_OFFSET(0) + 1)
```

相关声明：[NPCM_CLOCK_PWM_J](#a34ece572167371f620570db82dc99a0e)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a67cdf00a70f0ba34a91540895c2b0e77"></a>

```c
#define NPCM_CLOCK_I3CI (NPCM_CLOCK_GROUP_OFFSET(0) + 2)
```

相关声明：[NPCM_CLOCK_I3CI](#a67cdf00a70f0ba34a91540895c2b0e77)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a8070523598b622f82e7c4aa61fa113a2"></a>

```c
#define NPCM_CLOCK_UART3 (NPCM_CLOCK_GROUP_OFFSET(0) + 5)
```

相关声明：[NPCM_CLOCK_UART3](#a8070523598b622f82e7c4aa61fa113a2)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a2595c240f8bd2e046a8b4e06834289bb"></a>

```c
#define NPCM_CLOCK_UART2 (NPCM_CLOCK_GROUP_OFFSET(0) + 6)
```

相关声明：[NPCM_CLOCK_UART2](#a2595c240f8bd2e046a8b4e06834289bb)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a2f2f35b3ac73ed602668b418dbbc6076"></a>

```c
#define NPCM_CLOCK_SPIM (NPCM_CLOCK_GROUP_OFFSET(1) + 0)
```

相关声明：[NPCM_CLOCK_SPIM](#a2f2f35b3ac73ed602668b418dbbc6076)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a7b00badf4c99ff49e9babf170f6213a0"></a>

```c
#define NPCM_CLOCK_FIU (NPCM_CLOCK_GROUP_OFFSET(1) + 2)
```

相关声明：[NPCM_CLOCK_FIU](#a7b00badf4c99ff49e9babf170f6213a0)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_afb2fb08d08717664793a3179e87a96c8"></a>

```c
#define NPCM_CLOCK_USB20 (NPCM_CLOCK_GROUP_OFFSET(1) + 3)
```

相关声明：[NPCM_CLOCK_USB20](#afb2fb08d08717664793a3179e87a96c8)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a94aa8507b21fc4fd4d9fd14844f03153"></a>

```c
#define NPCM_CLOCK_UART (NPCM_CLOCK_GROUP_OFFSET(1) + 4)
```

相关声明：[NPCM_CLOCK_UART](#a94aa8507b21fc4fd4d9fd14844f03153)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a32de4522569dae6c3b8d5c7d8ea1f705"></a>

```c
#define NPCM_CLOCK_MFT1 (NPCM_CLOCK_GROUP_OFFSET(1) + 5)
```

相关声明：[NPCM_CLOCK_MFT1](#a32de4522569dae6c3b8d5c7d8ea1f705)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a011119434180ff4f782a1dada942f1fd"></a>

```c
#define NPCM_CLOCK_MFT2 (NPCM_CLOCK_GROUP_OFFSET(1) + 6)
```

相关声明：[NPCM_CLOCK_MFT2](#a011119434180ff4f782a1dada942f1fd)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_ae6526a686b1a3761dcde981f19469476"></a>

```c
#define NPCM_CLOCK_MFT3 (NPCM_CLOCK_GROUP_OFFSET(1) + 7)
```

相关声明：[NPCM_CLOCK_MFT3](#ae6526a686b1a3761dcde981f19469476)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_ae57d8b61165a095ec4b19aaa67b02156"></a>

```c
#define NPCM_CLOCK_PWM_A (NPCM_CLOCK_GROUP_OFFSET(2) + 0)
```

相关声明：[NPCM_CLOCK_PWM_A](#ae57d8b61165a095ec4b19aaa67b02156)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_acf2e8eefaf16ae166307b5cb0c9706d0"></a>

```c
#define NPCM_CLOCK_PWM_B (NPCM_CLOCK_GROUP_OFFSET(2) + 1)
```

相关声明：[NPCM_CLOCK_PWM_B](#acf2e8eefaf16ae166307b5cb0c9706d0)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a22bd19514fb8140afb3652c1cc131e81"></a>

```c
#define NPCM_CLOCK_PWM_C (NPCM_CLOCK_GROUP_OFFSET(2) + 2)
```

相关声明：[NPCM_CLOCK_PWM_C](#a22bd19514fb8140afb3652c1cc131e81)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_afb2ca7ea81c2f43e7576ff80e0aa2b0b"></a>

```c
#define NPCM_CLOCK_PWM_D (NPCM_CLOCK_GROUP_OFFSET(2) + 3)
```

相关声明：[NPCM_CLOCK_PWM_D](#afb2ca7ea81c2f43e7576ff80e0aa2b0b)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_afd75d18a0f1f0743625b8114fea9d8dd"></a>

```c
#define NPCM_CLOCK_PWM_E (NPCM_CLOCK_GROUP_OFFSET(2) + 4)
```

相关声明：[NPCM_CLOCK_PWM_E](#afd75d18a0f1f0743625b8114fea9d8dd)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_ae2357132f9cb282171562e8a022c444f"></a>

```c
#define NPCM_CLOCK_PWM_F (NPCM_CLOCK_GROUP_OFFSET(2) + 5)
```

相关声明：[NPCM_CLOCK_PWM_F](#ae2357132f9cb282171562e8a022c444f)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a9e3a29585ee19d46f0a59cbd821e1f04"></a>

```c
#define NPCM_CLOCK_PWM_G (NPCM_CLOCK_GROUP_OFFSET(2) + 6)
```

相关声明：[NPCM_CLOCK_PWM_G](#a9e3a29585ee19d46f0a59cbd821e1f04)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a2573f4ffb1e16de8e68cd0ed4da20085"></a>

```c
#define NPCM_CLOCK_PWM_H (NPCM_CLOCK_GROUP_OFFSET(2) + 7)
```

相关声明：[NPCM_CLOCK_PWM_H](#a2573f4ffb1e16de8e68cd0ed4da20085)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_aaba6ccd3affdf2d2e423e8be6f5b4fee"></a>

```c
#define NPCM_CLOCK_SMB1 (NPCM_CLOCK_GROUP_OFFSET(3) + 0)
```

相关声明：[NPCM_CLOCK_SMB1](#aaba6ccd3affdf2d2e423e8be6f5b4fee)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a029f41a64d84585ee2fc8f80d9fc30fb"></a>

```c
#define NPCM_CLOCK_SMB2 (NPCM_CLOCK_GROUP_OFFSET(3) + 1)
```

相关声明：[NPCM_CLOCK_SMB2](#a029f41a64d84585ee2fc8f80d9fc30fb)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a556e5bde2edcaacacdfd6cd82fe03efa"></a>

```c
#define NPCM_CLOCK_SMB3 (NPCM_CLOCK_GROUP_OFFSET(3) + 2)
```

相关声明：[NPCM_CLOCK_SMB3](#a556e5bde2edcaacacdfd6cd82fe03efa)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_acd9b598f8757e298bdbef6b13114099e"></a>

```c
#define NPCM_CLOCK_SMB4 (NPCM_CLOCK_GROUP_OFFSET(3) + 3)
```

相关声明：[NPCM_CLOCK_SMB4](#acd9b598f8757e298bdbef6b13114099e)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a934ed236e7462eedf1e58f98c5e90dfb"></a>

```c
#define NPCM_CLOCK_SMB5 (NPCM_CLOCK_GROUP_OFFSET(3) + 4)
```

相关声明：[NPCM_CLOCK_SMB5](#a934ed236e7462eedf1e58f98c5e90dfb)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a49989ff0da3f5807b7e1a045b1568429"></a>

```c
#define NPCM_CLOCK_SMB6 (NPCM_CLOCK_GROUP_OFFSET(3) + 5)
```

相关声明：[NPCM_CLOCK_SMB6](#a49989ff0da3f5807b7e1a045b1568429)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_af437c95f765f9060b061ca3511c89dd7"></a>

```c
#define NPCM_CLOCK_GDMA (NPCM_CLOCK_GROUP_OFFSET(3) + 7)
```

相关声明：[NPCM_CLOCK_GDMA](#af437c95f765f9060b061ca3511c89dd7)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_adc9d8de8a2f2847c66288050cd30a6fd"></a>

```c
#define NPCM_CLOCK_ITIM1 (NPCM_CLOCK_GROUP_OFFSET(4) + 0)
```

相关声明：[NPCM_CLOCK_ITIM1](#adc9d8de8a2f2847c66288050cd30a6fd)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a51720bbd7c55c99fbc72adb80a707617"></a>

```c
#define NPCM_CLOCK_ITIM2 (NPCM_CLOCK_GROUP_OFFSET(4) + 1)
```

相关声明：[NPCM_CLOCK_ITIM2](#a51720bbd7c55c99fbc72adb80a707617)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a41bb9d31b946f991f8c1970674174601"></a>

```c
#define NPCM_CLOCK_ITIM3 (NPCM_CLOCK_GROUP_OFFSET(4) + 2)
```

相关声明：[NPCM_CLOCK_ITIM3](#a41bb9d31b946f991f8c1970674174601)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_af96d5c1e939aa5fa9128173d4f545081"></a>

```c
#define NPCM_CLOCK_SMB_DMA (NPCM_CLOCK_GROUP_OFFSET(4) + 3)
```

相关声明：[NPCM_CLOCK_SMB_DMA](#af96d5c1e939aa5fa9128173d4f545081)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_adf45628a0f330eb1b4d74aab9e9a9ef8"></a>

```c
#define NPCM_CLOCK_ADC (NPCM_CLOCK_GROUP_OFFSET(4) + 4)
```

相关声明：[NPCM_CLOCK_ADC](#adf45628a0f330eb1b4d74aab9e9a9ef8)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_ae38fb3273e3a5fcabac782e65533734a"></a>

```c
#define NPCM_CLOCK_PECI (NPCM_CLOCK_GROUP_OFFSET(4) + 5)
```

相关声明：[NPCM_CLOCK_PECI](#ae38fb3273e3a5fcabac782e65533734a)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a8b3833a37e4e09cc75dbdbcfa045d358"></a>

```c
#define NPCM_CLOCK_SPIP1 (NPCM_CLOCK_GROUP_OFFSET(4) + 7)
```

相关声明：[NPCM_CLOCK_SPIP1](#a8b3833a37e4e09cc75dbdbcfa045d358)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a1c86b295d71f8fd761f3c8fefd86d3e5"></a>

```c
#define NPCM_CLOCK_UART4 (NPCM_CLOCK_GROUP_OFFSET(5) + 0)
```

相关声明：[NPCM_CLOCK_UART4](#a1c86b295d71f8fd761f3c8fefd86d3e5)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_aa832699b710f1cd9923a76d955ec1339"></a>

```c
#define NPCM_CLOCK_C2HACC (NPCM_CLOCK_GROUP_OFFSET(5) + 3)
```

相关声明：[NPCM_CLOCK_C2HACC](#aa832699b710f1cd9923a76d955ec1339)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a443a40fca1ed3567c0c01e3ff339921b"></a>

```c
#define NPCM_CLOCK_SHM_REG (NPCM_CLOCK_GROUP_OFFSET(5) + 4)
```

相关声明：[NPCM_CLOCK_SHM_REG](#a443a40fca1ed3567c0c01e3ff339921b)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_adf9c6f59ed292bec420e09a27e9f1dcf"></a>

```c
#define NPCM_CLOCK_SHM (NPCM_CLOCK_GROUP_OFFSET(5) + 5)
```

相关声明：[NPCM_CLOCK_SHM](#adf9c6f59ed292bec420e09a27e9f1dcf)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a24df8c7fe6d010cf4fc2105d7f9be99f"></a>

```c
#define NPCM_CLOCK_DP80 (NPCM_CLOCK_GROUP_OFFSET(5) + 6)
```

相关声明：[NPCM_CLOCK_DP80](#a24df8c7fe6d010cf4fc2105d7f9be99f)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a3c3df6e489aeb633b6108e1972071495"></a>

```c
#define NPCM_CLOCK_MSWC (NPCM_CLOCK_GROUP_OFFSET(5) + 7)
```

相关声明：[NPCM_CLOCK_MSWC](#a3c3df6e489aeb633b6108e1972071495)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a673d71f42575f480d596e2d75c72694d"></a>

```c
#define NPCM_CLOCK_ITIM4 (NPCM_CLOCK_GROUP_OFFSET(6) + 0)
```

相关声明：[NPCM_CLOCK_ITIM4](#a673d71f42575f480d596e2d75c72694d)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a142e5fd523ea4e5a88539e2c90d4cb3a"></a>

```c
#define NPCM_CLOCK_ITIM5 (NPCM_CLOCK_GROUP_OFFSET(6) + 1)
```

相关声明：[NPCM_CLOCK_ITIM5](#a142e5fd523ea4e5a88539e2c90d4cb3a)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_ae8d5a71630b1727200508fa785030184"></a>

```c
#define NPCM_CLOCK_ITIM6 (NPCM_CLOCK_GROUP_OFFSET(6) + 2)
```

相关声明：[NPCM_CLOCK_ITIM6](#ae8d5a71630b1727200508fa785030184)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_aa4641068fa6c9aca20589f682c7e36a8"></a>

```c
#define NPCM_CLOCK_RNG (NPCM_CLOCK_GROUP_OFFSET(6) + 3)
```

相关声明：[NPCM_CLOCK_RNG](#aa4641068fa6c9aca20589f682c7e36a8)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_adec2955e9224587cdaa61aa20c6a1b7d"></a>

```c
#define NPCM_CLOCK_SHA (NPCM_CLOCK_GROUP_OFFSET(6) + 5)
```

相关声明：[NPCM_CLOCK_SHA](#adec2955e9224587cdaa61aa20c6a1b7d)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_ac24765ff08e97f4747aa34b03e94eab6"></a>

```c
#define NPCM_CLOCK_ESPI (NPCM_CLOCK_GROUP_OFFSET(6) + 7)
```

相关声明：[NPCM_CLOCK_ESPI](#ac24765ff08e97f4747aa34b03e94eab6)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a5361334cef2fe6f4a0f93316c9fba60e"></a>

```c
#define NPCM_CLOCK_SMB7 (NPCM_CLOCK_GROUP_OFFSET(7) + 0)
```

相关声明：[NPCM_CLOCK_SMB7](#a5361334cef2fe6f4a0f93316c9fba60e)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_afa82d31834ccfb0e1766b4645174aa1b"></a>

```c
#define NPCM_CLOCK_SMB8 (NPCM_CLOCK_GROUP_OFFSET(7) + 1)
```

相关声明：[NPCM_CLOCK_SMB8](#afa82d31834ccfb0e1766b4645174aa1b)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_af6b642aababfe104bdd8bb6a5b6a0673"></a>

```c
#define NPCM_CLOCK_SMB9 (NPCM_CLOCK_GROUP_OFFSET(7) + 2)
```

相关声明：[NPCM_CLOCK_SMB9](#af6b642aababfe104bdd8bb6a5b6a0673)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a4124b07f5ae3f17d7bb2e8f3b12ca6e7"></a>

```c
#define NPCM_CLOCK_SMB10 (NPCM_CLOCK_GROUP_OFFSET(7) + 3)
```

相关声明：[NPCM_CLOCK_SMB10](#a4124b07f5ae3f17d7bb2e8f3b12ca6e7)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a290a1b7f611034ada1a8acff7ab7b9f5"></a>

```c
#define NPCM_CLOCK_SMB11 (NPCM_CLOCK_GROUP_OFFSET(7) + 4)
```

相关声明：[NPCM_CLOCK_SMB11](#a290a1b7f611034ada1a8acff7ab7b9f5)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_aab56086cca52095241274b00809516fa"></a>

```c
#define NPCM_CLOCK_SMB12 (NPCM_CLOCK_GROUP_OFFSET(7) + 5)
```

相关声明：[NPCM_CLOCK_SMB12](#aab56086cca52095241274b00809516fa)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a19a8155a21eae0ee40333fda238d537c"></a>

```c
#define NPCM_CLOCK_SIOX2 (NPCM_CLOCK_GROUP_OFFSET(7) + 6)
```

相关声明：[NPCM_CLOCK_SIOX2](#a19a8155a21eae0ee40333fda238d537c)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_ae308b41f2790143c822d731a8be49d95"></a>

```c
#define NPCM_CLOCK_SIOX1 (NPCM_CLOCK_GROUP_OFFSET(7) + 7)
```

相关声明：[NPCM_CLOCK_SIOX1](#ae308b41f2790143c822d731a8be49d95)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a39eca824a82d5d5f0e702b530670ce31"></a>

```c
#define NPCM_CLOCK_I3CI2 (NPCM_CLOCK_GROUP_OFFSET(8) + 0)
```

相关声明：[NPCM_CLOCK_I3CI2](#a39eca824a82d5d5f0e702b530670ce31)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a0fc3291804815adf6f6d1597dfc8e6da"></a>

```c
#define NPCM_CLOCK_I3CI3 (NPCM_CLOCK_GROUP_OFFSET(8) + 1)
```

相关声明：[NPCM_CLOCK_I3CI3](#a0fc3291804815adf6f6d1597dfc8e6da)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a28ec70f9e4b74d67e0c752bf3a6f2a46"></a>

```c
#define NPCM_CLOCK_I3CI4 (NPCM_CLOCK_GROUP_OFFSET(8) + 2)
```

相关声明：[NPCM_CLOCK_I3CI4](#a28ec70f9e4b74d67e0c752bf3a6f2a46)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_a838cf34ea43962d47e970ca40bb2b02f"></a>

```c
#define NPCM_CLOCK_I3CI5 (NPCM_CLOCK_GROUP_OFFSET(8) + 3)
```

相关声明：[NPCM_CLOCK_I3CI5](#a838cf34ea43962d47e970ca40bb2b02f)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

<a id="r_af4f55aeda364edb025307aea4fff3431"></a>

```c
#define NPCM_CLOCK_I3CI6 (NPCM_CLOCK_GROUP_OFFSET(8) + 4)
```

相关声明：[NPCM_CLOCK_I3CI6](#af4f55aeda364edb025307aea4fff3431)、[NPCM_CLOCK_GROUP_OFFSET](#aedf3c4059e2dba237097428dd3d17c86)。

## 245.2\_详细说明（Detailed Documentation）

<a id="adf45628a0f330eb1b4d74aab9e9a9ef8"></a>

### `NPCM_CLOCK_ADC`

```c
#define NPCM_CLOCK_ADC (NPCM_CLOCK_GROUP_OFFSET(4) + 4)
```

<a id="aa832699b710f1cd9923a76d955ec1339"></a>

### `NPCM_CLOCK_C2HACC`

```c
#define NPCM_CLOCK_C2HACC (NPCM_CLOCK_GROUP_OFFSET(5) + 3)
```

<a id="a24df8c7fe6d010cf4fc2105d7f9be99f"></a>

### `NPCM_CLOCK_DP80`

```c
#define NPCM_CLOCK_DP80 (NPCM_CLOCK_GROUP_OFFSET(5) + 6)
```

<a id="ac24765ff08e97f4747aa34b03e94eab6"></a>

### `NPCM_CLOCK_ESPI`

```c
#define NPCM_CLOCK_ESPI (NPCM_CLOCK_GROUP_OFFSET(6) + 7)
```

<a id="a7b00badf4c99ff49e9babf170f6213a0"></a>

### `NPCM_CLOCK_FIU`

```c
#define NPCM_CLOCK_FIU (NPCM_CLOCK_GROUP_OFFSET(1) + 2)
```

<a id="af437c95f765f9060b061ca3511c89dd7"></a>

### `NPCM_CLOCK_GDMA`

```c
#define NPCM_CLOCK_GDMA (NPCM_CLOCK_GROUP_OFFSET(3) + 7)
```

<a id="aedf3c4059e2dba237097428dd3d17c86"></a>

### `NPCM_CLOCK_GROUP_OFFSET`

```c
#define NPCM_CLOCK_GROUP_OFFSET ( N)
```

展开值（Value）：

```c
((N) << 3)
```

<a id="a67cdf00a70f0ba34a91540895c2b0e77"></a>

### `NPCM_CLOCK_I3CI`

```c
#define NPCM_CLOCK_I3CI (NPCM_CLOCK_GROUP_OFFSET(0) + 2)
```

<a id="a39eca824a82d5d5f0e702b530670ce31"></a>

### `NPCM_CLOCK_I3CI2`

```c
#define NPCM_CLOCK_I3CI2 (NPCM_CLOCK_GROUP_OFFSET(8) + 0)
```

<a id="a0fc3291804815adf6f6d1597dfc8e6da"></a>

### `NPCM_CLOCK_I3CI3`

```c
#define NPCM_CLOCK_I3CI3 (NPCM_CLOCK_GROUP_OFFSET(8) + 1)
```

<a id="a28ec70f9e4b74d67e0c752bf3a6f2a46"></a>

### `NPCM_CLOCK_I3CI4`

```c
#define NPCM_CLOCK_I3CI4 (NPCM_CLOCK_GROUP_OFFSET(8) + 2)
```

<a id="a838cf34ea43962d47e970ca40bb2b02f"></a>

### `NPCM_CLOCK_I3CI5`

```c
#define NPCM_CLOCK_I3CI5 (NPCM_CLOCK_GROUP_OFFSET(8) + 3)
```

<a id="af4f55aeda364edb025307aea4fff3431"></a>

### `NPCM_CLOCK_I3CI6`

```c
#define NPCM_CLOCK_I3CI6 (NPCM_CLOCK_GROUP_OFFSET(8) + 4)
```

<a id="adc9d8de8a2f2847c66288050cd30a6fd"></a>

### `NPCM_CLOCK_ITIM1`

```c
#define NPCM_CLOCK_ITIM1 (NPCM_CLOCK_GROUP_OFFSET(4) + 0)
```

<a id="a51720bbd7c55c99fbc72adb80a707617"></a>

### `NPCM_CLOCK_ITIM2`

```c
#define NPCM_CLOCK_ITIM2 (NPCM_CLOCK_GROUP_OFFSET(4) + 1)
```

<a id="a41bb9d31b946f991f8c1970674174601"></a>

### `NPCM_CLOCK_ITIM3`

```c
#define NPCM_CLOCK_ITIM3 (NPCM_CLOCK_GROUP_OFFSET(4) + 2)
```

<a id="a673d71f42575f480d596e2d75c72694d"></a>

### `NPCM_CLOCK_ITIM4`

```c
#define NPCM_CLOCK_ITIM4 (NPCM_CLOCK_GROUP_OFFSET(6) + 0)
```

<a id="a142e5fd523ea4e5a88539e2c90d4cb3a"></a>

### `NPCM_CLOCK_ITIM5`

```c
#define NPCM_CLOCK_ITIM5 (NPCM_CLOCK_GROUP_OFFSET(6) + 1)
```

<a id="ae8d5a71630b1727200508fa785030184"></a>

### `NPCM_CLOCK_ITIM6`

```c
#define NPCM_CLOCK_ITIM6 (NPCM_CLOCK_GROUP_OFFSET(6) + 2)
```

<a id="a32de4522569dae6c3b8d5c7d8ea1f705"></a>

### `NPCM_CLOCK_MFT1`

```c
#define NPCM_CLOCK_MFT1 (NPCM_CLOCK_GROUP_OFFSET(1) + 5)
```

<a id="a011119434180ff4f782a1dada942f1fd"></a>

### `NPCM_CLOCK_MFT2`

```c
#define NPCM_CLOCK_MFT2 (NPCM_CLOCK_GROUP_OFFSET(1) + 6)
```

<a id="ae6526a686b1a3761dcde981f19469476"></a>

### `NPCM_CLOCK_MFT3`

```c
#define NPCM_CLOCK_MFT3 (NPCM_CLOCK_GROUP_OFFSET(1) + 7)
```

<a id="a3c3df6e489aeb633b6108e1972071495"></a>

### `NPCM_CLOCK_MSWC`

```c
#define NPCM_CLOCK_MSWC (NPCM_CLOCK_GROUP_OFFSET(5) + 7)
```

<a id="ae38fb3273e3a5fcabac782e65533734a"></a>

### `NPCM_CLOCK_PECI`

```c
#define NPCM_CLOCK_PECI (NPCM_CLOCK_GROUP_OFFSET(4) + 5)
```

<a id="ae57d8b61165a095ec4b19aaa67b02156"></a>

### `NPCM_CLOCK_PWM_A`

```c
#define NPCM_CLOCK_PWM_A (NPCM_CLOCK_GROUP_OFFSET(2) + 0)
```

<a id="acf2e8eefaf16ae166307b5cb0c9706d0"></a>

### `NPCM_CLOCK_PWM_B`

```c
#define NPCM_CLOCK_PWM_B (NPCM_CLOCK_GROUP_OFFSET(2) + 1)
```

<a id="a22bd19514fb8140afb3652c1cc131e81"></a>

### `NPCM_CLOCK_PWM_C`

```c
#define NPCM_CLOCK_PWM_C (NPCM_CLOCK_GROUP_OFFSET(2) + 2)
```

<a id="afb2ca7ea81c2f43e7576ff80e0aa2b0b"></a>

### `NPCM_CLOCK_PWM_D`

```c
#define NPCM_CLOCK_PWM_D (NPCM_CLOCK_GROUP_OFFSET(2) + 3)
```

<a id="afd75d18a0f1f0743625b8114fea9d8dd"></a>

### `NPCM_CLOCK_PWM_E`

```c
#define NPCM_CLOCK_PWM_E (NPCM_CLOCK_GROUP_OFFSET(2) + 4)
```

<a id="ae2357132f9cb282171562e8a022c444f"></a>

### `NPCM_CLOCK_PWM_F`

```c
#define NPCM_CLOCK_PWM_F (NPCM_CLOCK_GROUP_OFFSET(2) + 5)
```

<a id="a9e3a29585ee19d46f0a59cbd821e1f04"></a>

### `NPCM_CLOCK_PWM_G`

```c
#define NPCM_CLOCK_PWM_G (NPCM_CLOCK_GROUP_OFFSET(2) + 6)
```

<a id="a2573f4ffb1e16de8e68cd0ed4da20085"></a>

### `NPCM_CLOCK_PWM_H`

```c
#define NPCM_CLOCK_PWM_H (NPCM_CLOCK_GROUP_OFFSET(2) + 7)
```

<a id="a63e02592f717f0575db06065c5abf7f9"></a>

### `NPCM_CLOCK_PWM_I`

```c
#define NPCM_CLOCK_PWM_I (NPCM_CLOCK_GROUP_OFFSET(0) + 0)
```

<a id="a34ece572167371f620570db82dc99a0e"></a>

### `NPCM_CLOCK_PWM_J`

```c
#define NPCM_CLOCK_PWM_J (NPCM_CLOCK_GROUP_OFFSET(0) + 1)
```

<a id="aa4641068fa6c9aca20589f682c7e36a8"></a>

### `NPCM_CLOCK_RNG`

```c
#define NPCM_CLOCK_RNG (NPCM_CLOCK_GROUP_OFFSET(6) + 3)
```

<a id="adec2955e9224587cdaa61aa20c6a1b7d"></a>

### `NPCM_CLOCK_SHA`

```c
#define NPCM_CLOCK_SHA (NPCM_CLOCK_GROUP_OFFSET(6) + 5)
```

<a id="adf9c6f59ed292bec420e09a27e9f1dcf"></a>

### `NPCM_CLOCK_SHM`

```c
#define NPCM_CLOCK_SHM (NPCM_CLOCK_GROUP_OFFSET(5) + 5)
```

<a id="a443a40fca1ed3567c0c01e3ff339921b"></a>

### `NPCM_CLOCK_SHM_REG`

```c
#define NPCM_CLOCK_SHM_REG (NPCM_CLOCK_GROUP_OFFSET(5) + 4)
```

<a id="ae308b41f2790143c822d731a8be49d95"></a>

### `NPCM_CLOCK_SIOX1`

```c
#define NPCM_CLOCK_SIOX1 (NPCM_CLOCK_GROUP_OFFSET(7) + 7)
```

<a id="a19a8155a21eae0ee40333fda238d537c"></a>

### `NPCM_CLOCK_SIOX2`

```c
#define NPCM_CLOCK_SIOX2 (NPCM_CLOCK_GROUP_OFFSET(7) + 6)
```

<a id="aaba6ccd3affdf2d2e423e8be6f5b4fee"></a>

### `NPCM_CLOCK_SMB1`

```c
#define NPCM_CLOCK_SMB1 (NPCM_CLOCK_GROUP_OFFSET(3) + 0)
```

<a id="a4124b07f5ae3f17d7bb2e8f3b12ca6e7"></a>

### `NPCM_CLOCK_SMB10`

```c
#define NPCM_CLOCK_SMB10 (NPCM_CLOCK_GROUP_OFFSET(7) + 3)
```

<a id="a290a1b7f611034ada1a8acff7ab7b9f5"></a>

### `NPCM_CLOCK_SMB11`

```c
#define NPCM_CLOCK_SMB11 (NPCM_CLOCK_GROUP_OFFSET(7) + 4)
```

<a id="aab56086cca52095241274b00809516fa"></a>

### `NPCM_CLOCK_SMB12`

```c
#define NPCM_CLOCK_SMB12 (NPCM_CLOCK_GROUP_OFFSET(7) + 5)
```

<a id="a029f41a64d84585ee2fc8f80d9fc30fb"></a>

### `NPCM_CLOCK_SMB2`

```c
#define NPCM_CLOCK_SMB2 (NPCM_CLOCK_GROUP_OFFSET(3) + 1)
```

<a id="a556e5bde2edcaacacdfd6cd82fe03efa"></a>

### `NPCM_CLOCK_SMB3`

```c
#define NPCM_CLOCK_SMB3 (NPCM_CLOCK_GROUP_OFFSET(3) + 2)
```

<a id="acd9b598f8757e298bdbef6b13114099e"></a>

### `NPCM_CLOCK_SMB4`

```c
#define NPCM_CLOCK_SMB4 (NPCM_CLOCK_GROUP_OFFSET(3) + 3)
```

<a id="a934ed236e7462eedf1e58f98c5e90dfb"></a>

### `NPCM_CLOCK_SMB5`

```c
#define NPCM_CLOCK_SMB5 (NPCM_CLOCK_GROUP_OFFSET(3) + 4)
```

<a id="a49989ff0da3f5807b7e1a045b1568429"></a>

### `NPCM_CLOCK_SMB6`

```c
#define NPCM_CLOCK_SMB6 (NPCM_CLOCK_GROUP_OFFSET(3) + 5)
```

<a id="a5361334cef2fe6f4a0f93316c9fba60e"></a>

### `NPCM_CLOCK_SMB7`

```c
#define NPCM_CLOCK_SMB7 (NPCM_CLOCK_GROUP_OFFSET(7) + 0)
```

<a id="afa82d31834ccfb0e1766b4645174aa1b"></a>

### `NPCM_CLOCK_SMB8`

```c
#define NPCM_CLOCK_SMB8 (NPCM_CLOCK_GROUP_OFFSET(7) + 1)
```

<a id="af6b642aababfe104bdd8bb6a5b6a0673"></a>

### `NPCM_CLOCK_SMB9`

```c
#define NPCM_CLOCK_SMB9 (NPCM_CLOCK_GROUP_OFFSET(7) + 2)
```

<a id="af96d5c1e939aa5fa9128173d4f545081"></a>

### `NPCM_CLOCK_SMB_DMA`

```c
#define NPCM_CLOCK_SMB_DMA (NPCM_CLOCK_GROUP_OFFSET(4) + 3)
```

<a id="a2f2f35b3ac73ed602668b418dbbc6076"></a>

### `NPCM_CLOCK_SPIM`

```c
#define NPCM_CLOCK_SPIM (NPCM_CLOCK_GROUP_OFFSET(1) + 0)
```

<a id="a8b3833a37e4e09cc75dbdbcfa045d358"></a>

### `NPCM_CLOCK_SPIP1`

```c
#define NPCM_CLOCK_SPIP1 (NPCM_CLOCK_GROUP_OFFSET(4) + 7)
```

<a id="a94aa8507b21fc4fd4d9fd14844f03153"></a>

### `NPCM_CLOCK_UART`

```c
#define NPCM_CLOCK_UART (NPCM_CLOCK_GROUP_OFFSET(1) + 4)
```

<a id="a2595c240f8bd2e046a8b4e06834289bb"></a>

### `NPCM_CLOCK_UART2`

```c
#define NPCM_CLOCK_UART2 (NPCM_CLOCK_GROUP_OFFSET(0) + 6)
```

<a id="a8070523598b622f82e7c4aa61fa113a2"></a>

### `NPCM_CLOCK_UART3`

```c
#define NPCM_CLOCK_UART3 (NPCM_CLOCK_GROUP_OFFSET(0) + 5)
```

<a id="a1c86b295d71f8fd761f3c8fefd86d3e5"></a>

### `NPCM_CLOCK_UART4`

```c
#define NPCM_CLOCK_UART4 (NPCM_CLOCK_GROUP_OFFSET(5) + 0)
```

<a id="afb2fb08d08717664793a3179e87a96c8"></a>

### `NPCM_CLOCK_USB20`

```c
#define NPCM_CLOCK_USB20 (NPCM_CLOCK_GROUP_OFFSET(1) + 3)
```


## 245.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P128_npcm_clock.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P244_zephyr__dt-bindings__misc__nordic-owner-id-nrf9230.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P246_zephyr__dt-bindings__i2c__npcx-i2c.h_文件参考.md)
