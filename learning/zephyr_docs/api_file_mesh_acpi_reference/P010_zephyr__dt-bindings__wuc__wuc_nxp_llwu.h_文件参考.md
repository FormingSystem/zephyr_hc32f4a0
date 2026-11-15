---
id: learning.zephyr-docs.api-file-mesh-acpi-reference.page-10
title: zephyr__dt-bindings__wuc__wuc_nxp_llwu.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wuc__nxp__llwu_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_dt-bindings\_\_wuc\_\_wuc\_nxp\_llwu.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wuc__nxp__llwu_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP低漏电唤醒单元（LLWU）的唤醒源编码。

查看此文件的源码。

<a id="details"></a>

NXP低漏电唤醒单元（LLWU）的唤醒源编码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="r_a38681f799daefdff2df71fbd7600eff0"></a>

```c
#define NXP_LLWU_PIN_WAKEUP(pin_index, edge_type)
```

相关声明：[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)。

编码引脚唤醒源（PIN Wakeup Source）。

<a id="r_a42f98709320b42c357242cc34907e07f"></a>

```c
#define NXP_LLWU_MODULE_WAKEUP(module_index)
```

相关声明：[NXP_LLWU_MODULE_WAKEUP](#a42f98709320b42c357242cc34907e07f)。

编码模块唤醒源（MODULE Wakeup Source）。

<a id="define-members-0"></a>

### 唤醒源类型编码（Wakeup Source Type Encodings）

唤醒源编码布局（Wakeup Source Encoding Layout）。

位 `[31]`：0 表示引脚（PIN），1 表示模块（MODULE）。

对于引脚（PIN，位 `[31] = 0`）：

对于模块（MODULE，位 `[31] = 1`）：

<a id="r_a913770f517306b614c047ac04cb5c060"></a>

```c
#define NXP_LLWU_WAKEUP_SOURCE_TYPE_PIN (0U << 31)
```

相关声明：[NXP_LLWU_WAKEUP_SOURCE_TYPE_PIN](#a913770f517306b614c047ac04cb5c060)。

引脚源（PIN Source）的唤醒源类型编码（Wakeup Source Type Encoding）。

<a id="r_ad737cbcb7fc898d2e0710c1cfdecebe9"></a>

```c
#define NXP_LLWU_WAKEUP_SOURCE_TYPE_MODULE (1U << 31)
```

相关声明：[NXP_LLWU_WAKEUP_SOURCE_TYPE_MODULE](#ad737cbcb7fc898d2e0710c1cfdecebe9)。

模块源（MODULE Source）的唤醒源类型编码（Wakeup Source Type Encoding）。

<a id="define-members-1"></a>

### 引脚边沿编码（PIN Edge Encodings）

<a id="r_aee7a4ceedbe0e43e21d060349c20f081"></a>

```c
#define NXP_LLWU_PIN_EDGE_RISING 1
```

相关声明：[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

上升沿（Rising Edge）的引脚边沿编码（PIN Edge Encoding）。

<a id="r_acf26a7cf25898931d83ea9b76f2691f1"></a>

```c
#define NXP_LLWU_PIN_EDGE_FALLING 2
```

相关声明：[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

下降沿（Falling Edge）的引脚边沿编码（PIN Edge Encoding）。

<a id="r_a02aec7b13ec302b9c4cc4fab57f7f0e1"></a>

```c
#define NXP_LLWU_PIN_EDGE_ANY 3
```

相关声明：[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

任意边沿（Any Edge）的引脚边沿编码（PIN Edge Encoding）。

<a id="define-members-2"></a>

### 引脚唤醒源（PIN Wakeup Sources，PIN 0–15）

<a id="r_a22b1ef0b1254105352d47cc498d71bdb"></a>

```c
#define NXP_LLWU_PIN_0_RISING NXP_LLWU_PIN_WAKEUP(1, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_0_RISING](#a22b1ef0b1254105352d47cc498d71bdb)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）0 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_a45fe5784d5b7cca2489900995e786aa5"></a>

```c
#define NXP_LLWU_PIN_0_FALLING NXP_LLWU_PIN_WAKEUP(1, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_0_FALLING](#a45fe5784d5b7cca2489900995e786aa5)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）0 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_a980e9e02e626a2a8add3979cab3f1332"></a>

```c
#define NXP_LLWU_PIN_0_ANY NXP_LLWU_PIN_WAKEUP(1, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_0_ANY](#a980e9e02e626a2a8add3979cab3f1332)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）0 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_afcc50892ef15c6d2aa6f4ef07039b00e"></a>

```c
#define NXP_LLWU_PIN_1_RISING NXP_LLWU_PIN_WAKEUP(2, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_1_RISING](#afcc50892ef15c6d2aa6f4ef07039b00e)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）1 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_a4ed3943d19a76686e66b9bb344f4a908"></a>

```c
#define NXP_LLWU_PIN_1_FALLING NXP_LLWU_PIN_WAKEUP(2, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_1_FALLING](#a4ed3943d19a76686e66b9bb344f4a908)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）1 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_a06dd86435aeb5787ab49e892f02f54a8"></a>

```c
#define NXP_LLWU_PIN_1_ANY NXP_LLWU_PIN_WAKEUP(2, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_1_ANY](#a06dd86435aeb5787ab49e892f02f54a8)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）1 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_a294bc086cea15dd19a9a1b3c88af8267"></a>

```c
#define NXP_LLWU_PIN_2_RISING NXP_LLWU_PIN_WAKEUP(3, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_2_RISING](#a294bc086cea15dd19a9a1b3c88af8267)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）2 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_a996c8f9d240ab171b1b7824e0b2b495a"></a>

```c
#define NXP_LLWU_PIN_2_FALLING NXP_LLWU_PIN_WAKEUP(3, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_2_FALLING](#a996c8f9d240ab171b1b7824e0b2b495a)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）2 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_acfb6fcfc63c21ac44a2027d357525b5c"></a>

```c
#define NXP_LLWU_PIN_2_ANY NXP_LLWU_PIN_WAKEUP(3, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_2_ANY](#acfb6fcfc63c21ac44a2027d357525b5c)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）2 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_a5b5564e04d931ac894040816fd2b3836"></a>

```c
#define NXP_LLWU_PIN_3_RISING NXP_LLWU_PIN_WAKEUP(4, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_3_RISING](#a5b5564e04d931ac894040816fd2b3836)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）3 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_a340d0e5b52e8ba7b2c52a034fc119955"></a>

```c
#define NXP_LLWU_PIN_3_FALLING NXP_LLWU_PIN_WAKEUP(4, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_3_FALLING](#a340d0e5b52e8ba7b2c52a034fc119955)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）3 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_a06646d29c8f8363a2ec79d5c806e7f8f"></a>

```c
#define NXP_LLWU_PIN_3_ANY NXP_LLWU_PIN_WAKEUP(4, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_3_ANY](#a06646d29c8f8363a2ec79d5c806e7f8f)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）3 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_ade64cbebab222bd4d3a5191f1f6ea996"></a>

```c
#define NXP_LLWU_PIN_4_RISING NXP_LLWU_PIN_WAKEUP(5, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_4_RISING](#ade64cbebab222bd4d3a5191f1f6ea996)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）4 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_a18dd9a8c12a6b00b5a2728e30422f7cb"></a>

```c
#define NXP_LLWU_PIN_4_FALLING NXP_LLWU_PIN_WAKEUP(5, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_4_FALLING](#a18dd9a8c12a6b00b5a2728e30422f7cb)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）4 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_aeb3a101789e90b59759c3a73825c3b05"></a>

```c
#define NXP_LLWU_PIN_4_ANY NXP_LLWU_PIN_WAKEUP(5, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_4_ANY](#aeb3a101789e90b59759c3a73825c3b05)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）4 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_a6b42990f9dd099943da7cf010bf3dfd9"></a>

```c
#define NXP_LLWU_PIN_5_RISING NXP_LLWU_PIN_WAKEUP(6, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_5_RISING](#a6b42990f9dd099943da7cf010bf3dfd9)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）5 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_a425be15f35fd7a8f606f709282b08029"></a>

```c
#define NXP_LLWU_PIN_5_FALLING NXP_LLWU_PIN_WAKEUP(6, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_5_FALLING](#a425be15f35fd7a8f606f709282b08029)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）5 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_a566eb44389dc80ae8c54181980e1edb7"></a>

```c
#define NXP_LLWU_PIN_5_ANY NXP_LLWU_PIN_WAKEUP(6, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_5_ANY](#a566eb44389dc80ae8c54181980e1edb7)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）5 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_a5406e8b3cdfc0ffa2745ca751683a1f1"></a>

```c
#define NXP_LLWU_PIN_6_RISING NXP_LLWU_PIN_WAKEUP(7, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_6_RISING](#a5406e8b3cdfc0ffa2745ca751683a1f1)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）6 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_a9b68e1035813ce8b3a169f3ac0fcd40c"></a>

```c
#define NXP_LLWU_PIN_6_FALLING NXP_LLWU_PIN_WAKEUP(7, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_6_FALLING](#a9b68e1035813ce8b3a169f3ac0fcd40c)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）6 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_a8a8b4f5eb6d6eb1ae1dd5da52b43d955"></a>

```c
#define NXP_LLWU_PIN_6_ANY NXP_LLWU_PIN_WAKEUP(7, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_6_ANY](#a8a8b4f5eb6d6eb1ae1dd5da52b43d955)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）6 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_a73259733dcf1332c36a3f4c985e8c821"></a>

```c
#define NXP_LLWU_PIN_7_RISING NXP_LLWU_PIN_WAKEUP(8, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_7_RISING](#a73259733dcf1332c36a3f4c985e8c821)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）7 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_af37b9fed47d8d39e73c38653e6f2ec07"></a>

```c
#define NXP_LLWU_PIN_7_FALLING NXP_LLWU_PIN_WAKEUP(8, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_7_FALLING](#af37b9fed47d8d39e73c38653e6f2ec07)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）7 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_a1a478e2b3fb681c9d4a0aeafd22a3a70"></a>

```c
#define NXP_LLWU_PIN_7_ANY NXP_LLWU_PIN_WAKEUP(8, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_7_ANY](#a1a478e2b3fb681c9d4a0aeafd22a3a70)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）7 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_a4545f103ce2b50e55a87a3002f7c29ca"></a>

```c
#define NXP_LLWU_PIN_8_RISING NXP_LLWU_PIN_WAKEUP(9, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_8_RISING](#a4545f103ce2b50e55a87a3002f7c29ca)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）8 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_af8d39ccb96fad92a57289f010c7718c6"></a>

```c
#define NXP_LLWU_PIN_8_FALLING NXP_LLWU_PIN_WAKEUP(9, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_8_FALLING](#af8d39ccb96fad92a57289f010c7718c6)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）8 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_a14fa6ee01a2b19075a47233667d2bfa8"></a>

```c
#define NXP_LLWU_PIN_8_ANY NXP_LLWU_PIN_WAKEUP(9, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_8_ANY](#a14fa6ee01a2b19075a47233667d2bfa8)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）8 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_a9a0af00768b95c706a5c46c5ddbd2855"></a>

```c
#define NXP_LLWU_PIN_9_RISING NXP_LLWU_PIN_WAKEUP(10, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_9_RISING](#a9a0af00768b95c706a5c46c5ddbd2855)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）9 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_a6bd22f657dd21231cd15e9ec3505e09e"></a>

```c
#define NXP_LLWU_PIN_9_FALLING NXP_LLWU_PIN_WAKEUP(10, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_9_FALLING](#a6bd22f657dd21231cd15e9ec3505e09e)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）9 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_a15db4a9eea60578699381615d8b5ae4b"></a>

```c
#define NXP_LLWU_PIN_9_ANY NXP_LLWU_PIN_WAKEUP(10, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_9_ANY](#a15db4a9eea60578699381615d8b5ae4b)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）9 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_ad87fff5279065c83c505ca8862f5ce43"></a>

```c
#define NXP_LLWU_PIN_10_RISING NXP_LLWU_PIN_WAKEUP(11, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_10_RISING](#ad87fff5279065c83c505ca8862f5ce43)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）10 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_aae37151a99975e603145519c9269aebd"></a>

```c
#define NXP_LLWU_PIN_10_FALLING NXP_LLWU_PIN_WAKEUP(11, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_10_FALLING](#aae37151a99975e603145519c9269aebd)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）10 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_a75bedf07680f4c67c3a0bcf08a996246"></a>

```c
#define NXP_LLWU_PIN_10_ANY NXP_LLWU_PIN_WAKEUP(11, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_10_ANY](#a75bedf07680f4c67c3a0bcf08a996246)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）10 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_a6de54c9d9fe7142734c1b652b42e6dff"></a>

```c
#define NXP_LLWU_PIN_11_RISING NXP_LLWU_PIN_WAKEUP(12, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_11_RISING](#a6de54c9d9fe7142734c1b652b42e6dff)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）11 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_a27205ae6b21f46a6d0c873eaddb5cf07"></a>

```c
#define NXP_LLWU_PIN_11_FALLING NXP_LLWU_PIN_WAKEUP(12, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_11_FALLING](#a27205ae6b21f46a6d0c873eaddb5cf07)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）11 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_a1738c695813210ae8f27eabd8d97e253"></a>

```c
#define NXP_LLWU_PIN_11_ANY NXP_LLWU_PIN_WAKEUP(12, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_11_ANY](#a1738c695813210ae8f27eabd8d97e253)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）11 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_a494dd477f710fe6af73b6fd37d5cd55c"></a>

```c
#define NXP_LLWU_PIN_12_RISING NXP_LLWU_PIN_WAKEUP(13, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_12_RISING](#a494dd477f710fe6af73b6fd37d5cd55c)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）12 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_abe891cd82b0d5a7052f14c13c5b9ab33"></a>

```c
#define NXP_LLWU_PIN_12_FALLING NXP_LLWU_PIN_WAKEUP(13, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_12_FALLING](#abe891cd82b0d5a7052f14c13c5b9ab33)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）12 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_ad37b9013e5921c3d633f13c8e3178b08"></a>

```c
#define NXP_LLWU_PIN_12_ANY NXP_LLWU_PIN_WAKEUP(13, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_12_ANY](#ad37b9013e5921c3d633f13c8e3178b08)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）12 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_a4f510ce70552461c108644bac9502fb2"></a>

```c
#define NXP_LLWU_PIN_13_RISING NXP_LLWU_PIN_WAKEUP(14, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_13_RISING](#a4f510ce70552461c108644bac9502fb2)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）13 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_acd6e7cdf10048850c4c7459b33fd362c"></a>

```c
#define NXP_LLWU_PIN_13_FALLING NXP_LLWU_PIN_WAKEUP(14, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_13_FALLING](#acd6e7cdf10048850c4c7459b33fd362c)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）13 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_ac129adccc27a78cdedd33d9ac3422744"></a>

```c
#define NXP_LLWU_PIN_13_ANY NXP_LLWU_PIN_WAKEUP(14, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_13_ANY](#ac129adccc27a78cdedd33d9ac3422744)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）13 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_ac782572eb1fa31053985047cffde22f8"></a>

```c
#define NXP_LLWU_PIN_14_RISING NXP_LLWU_PIN_WAKEUP(15, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_14_RISING](#ac782572eb1fa31053985047cffde22f8)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）14 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_a5eb28cf71d130ddb470305516a3c89a9"></a>

```c
#define NXP_LLWU_PIN_14_FALLING NXP_LLWU_PIN_WAKEUP(15, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_14_FALLING](#a5eb28cf71d130ddb470305516a3c89a9)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）14 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_a1420832d18e0fee76ab56659e17e60c4"></a>

```c
#define NXP_LLWU_PIN_14_ANY NXP_LLWU_PIN_WAKEUP(15, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_14_ANY](#a1420832d18e0fee76ab56659e17e60c4)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）14 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="r_ae2836bde65b62a025124a12e216a77dd"></a>

```c
#define NXP_LLWU_PIN_15_RISING NXP_LLWU_PIN_WAKEUP(16, NXP_LLWU_PIN_EDGE_RISING)
```

相关声明：[NXP_LLWU_PIN_15_RISING](#ae2836bde65b62a025124a12e216a77dd)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_RISING](#aee7a4ceedbe0e43e21d060349c20f081)。

引脚（PIN）15 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="r_a804bf1905ef87f4342352e9c2964523a"></a>

```c
#define NXP_LLWU_PIN_15_FALLING NXP_LLWU_PIN_WAKEUP(16, NXP_LLWU_PIN_EDGE_FALLING)
```

相关声明：[NXP_LLWU_PIN_15_FALLING](#a804bf1905ef87f4342352e9c2964523a)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_FALLING](#acf26a7cf25898931d83ea9b76f2691f1)。

引脚（PIN）15 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="r_a36d3145d6f7416718e85d7d39ddc4222"></a>

```c
#define NXP_LLWU_PIN_15_ANY NXP_LLWU_PIN_WAKEUP(16, NXP_LLWU_PIN_EDGE_ANY)
```

相关声明：[NXP_LLWU_PIN_15_ANY](#a36d3145d6f7416718e85d7d39ddc4222)、[NXP_LLWU_PIN_WAKEUP](#a38681f799daefdff2df71fbd7600eff0)、[NXP_LLWU_PIN_EDGE_ANY](#a02aec7b13ec302b9c4cc4fab57f7f0e1)。

引脚（PIN）15 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="define-members-3"></a>

### 模块唤醒源（MODULE Wakeup Sources，MODULE 0–7）

<a id="r_af11371936f2c65bdc2b8a8238856be79"></a>

```c
#define NXP_LLWU_MODULE_0 NXP_LLWU_MODULE_WAKEUP(1)
```

相关声明：[NXP_LLWU_MODULE_0](#af11371936f2c65bdc2b8a8238856be79)、[NXP_LLWU_MODULE_WAKEUP](#a42f98709320b42c357242cc34907e07f)。

模块（MODULE）0 唤醒源（Wakeup Source）。

<a id="r_a46c14dc1f55ee0b4e878af6b54838a41"></a>

```c
#define NXP_LLWU_MODULE_1 NXP_LLWU_MODULE_WAKEUP(2)
```

相关声明：[NXP_LLWU_MODULE_1](#a46c14dc1f55ee0b4e878af6b54838a41)、[NXP_LLWU_MODULE_WAKEUP](#a42f98709320b42c357242cc34907e07f)。

模块（MODULE）1 唤醒源（Wakeup Source）。

<a id="r_a77573e26df2580d83c39f2f8bcaa45fc"></a>

```c
#define NXP_LLWU_MODULE_2 NXP_LLWU_MODULE_WAKEUP(3)
```

相关声明：[NXP_LLWU_MODULE_2](#a77573e26df2580d83c39f2f8bcaa45fc)、[NXP_LLWU_MODULE_WAKEUP](#a42f98709320b42c357242cc34907e07f)。

模块（MODULE）2 唤醒源（Wakeup Source）。

<a id="r_a0b9fb27b28bf3371d7e7e6d61dfbf1bb"></a>

```c
#define NXP_LLWU_MODULE_3 NXP_LLWU_MODULE_WAKEUP(4)
```

相关声明：[NXP_LLWU_MODULE_3](#a0b9fb27b28bf3371d7e7e6d61dfbf1bb)、[NXP_LLWU_MODULE_WAKEUP](#a42f98709320b42c357242cc34907e07f)。

模块（MODULE）3 唤醒源（Wakeup Source）。

<a id="r_a45cb21fe5351cbb071784c521d5d8ae3"></a>

```c
#define NXP_LLWU_MODULE_4 NXP_LLWU_MODULE_WAKEUP(5)
```

相关声明：[NXP_LLWU_MODULE_4](#a45cb21fe5351cbb071784c521d5d8ae3)、[NXP_LLWU_MODULE_WAKEUP](#a42f98709320b42c357242cc34907e07f)。

模块（MODULE）4 唤醒源（Wakeup Source）。

<a id="r_aa79bbe27e253758a3ebd2d1adb34c96a"></a>

```c
#define NXP_LLWU_MODULE_5 NXP_LLWU_MODULE_WAKEUP(6)
```

相关声明：[NXP_LLWU_MODULE_5](#aa79bbe27e253758a3ebd2d1adb34c96a)、[NXP_LLWU_MODULE_WAKEUP](#a42f98709320b42c357242cc34907e07f)。

模块（MODULE）5 唤醒源（Wakeup Source）。

<a id="r_a8bdca3adfb7b576ad8be483f535bc0c9"></a>

```c
#define NXP_LLWU_MODULE_6 NXP_LLWU_MODULE_WAKEUP(7)
```

相关声明：[NXP_LLWU_MODULE_6](#a8bdca3adfb7b576ad8be483f535bc0c9)、[NXP_LLWU_MODULE_WAKEUP](#a42f98709320b42c357242cc34907e07f)。

模块（MODULE）6 唤醒源（Wakeup Source）。

<a id="r_ad613fb79d2cba1fb24bdeb0e53bd9f32"></a>

```c
#define NXP_LLWU_MODULE_7 NXP_LLWU_MODULE_WAKEUP(8)
```

相关声明：[NXP_LLWU_MODULE_7](#ad613fb79d2cba1fb24bdeb0e53bd9f32)、[NXP_LLWU_MODULE_WAKEUP](#a42f98709320b42c357242cc34907e07f)。

模块（MODULE）7 唤醒源（Wakeup Source）。

<a id="define-members-4"></a>

### 唤醒源字段辅助宏（Wakeup Source Field Helpers）

<a id="r_a8ccc2e70929f01d427c6568b9abf70d9"></a>

```c
#define NXP_LLWU_IS_PIN_SOURCE(source)
```

相关声明：[NXP_LLWU_IS_PIN_SOURCE](#a8ccc2e70929f01d427c6568b9abf70d9)。

检查唤醒源（Wakeup Source）是否编码了引脚源（PIN Source）。

<a id="r_ab4ec11c4caedbff22a0a8f08d288b2cd"></a>

```c
#define NXP_LLWU_IS_MODULE_SOURCE(source)
```

相关声明：[NXP_LLWU_IS_MODULE_SOURCE](#ab4ec11c4caedbff22a0a8f08d288b2cd)。

检查唤醒源（Wakeup Source）是否编码了模块源（MODULE Source）。

<a id="r_ade18bf0a8df1938e626cb9fbce76552f"></a>

```c
#define NXP_LLWU_GET_PIN_INDEX(source)
```

相关声明：[NXP_LLWU_GET_PIN_INDEX](#ade18bf0a8df1938e626cb9fbce76552f)。

从唤醒源（Wakeup Source）中提取引脚索引（PIN Index）。

<a id="r_afe28acabdb8e492e7c9884545e1b5430"></a>

```c
#define NXP_LLWU_GET_PIN_EDGE(source)
```

相关声明：[NXP_LLWU_GET_PIN_EDGE](#afe28acabdb8e492e7c9884545e1b5430)。

从唤醒源（Wakeup Source）中提取引脚边沿编码（PIN Edge Encoding）。

<a id="r_aea787ad697ec0f90a99bebe75b24d605"></a>

```c
#define NXP_LLWU_GET_MODULE_INDEX(source)
```

相关声明：[NXP_LLWU_GET_MODULE_INDEX](#aea787ad697ec0f90a99bebe75b24d605)。

从唤醒源（Wakeup Source）中提取模块索引（MODULE Index）。

## 10.2\_详细说明（Detailed Documentation）

<a id="aea787ad697ec0f90a99bebe75b24d605"></a>

### `NXP_LLWU_GET_MODULE_INDEX`

```c
#define NXP_LLWU_GET_MODULE_INDEX ( source)
```

展开值（Value）：

```c
((source) & 0xFF)
```

从唤醒源（Wakeup Source）中提取模块索引（MODULE Index）。

<a id="afe28acabdb8e492e7c9884545e1b5430"></a>

### `NXP_LLWU_GET_PIN_EDGE`

```c
#define NXP_LLWU_GET_PIN_EDGE ( source)
```

展开值（Value）：

```c
(((source) >> 8) & 0x3)
```

从唤醒源（Wakeup Source）中提取引脚边沿编码（PIN Edge Encoding）。

<a id="ade18bf0a8df1938e626cb9fbce76552f"></a>

### `NXP_LLWU_GET_PIN_INDEX`

```c
#define NXP_LLWU_GET_PIN_INDEX ( source)
```

展开值（Value）：

```c
((source) & 0xFF)
```

从唤醒源（Wakeup Source）中提取引脚索引（PIN Index）。

<a id="ab4ec11c4caedbff22a0a8f08d288b2cd"></a>

### `NXP_LLWU_IS_MODULE_SOURCE`

```c
#define NXP_LLWU_IS_MODULE_SOURCE ( source)
```

展开值（Value）：

```c
(((source) & (1U << 31)) != 0)
```

检查唤醒源（Wakeup Source）是否编码了模块源（MODULE Source）。

<a id="a8ccc2e70929f01d427c6568b9abf70d9"></a>

### `NXP_LLWU_IS_PIN_SOURCE`

```c
#define NXP_LLWU_IS_PIN_SOURCE ( source)
```

展开值（Value）：

```c
(((source) & (1U << 31)) == 0)
```

检查唤醒源（Wakeup Source）是否编码了引脚源（PIN Source）。

<a id="af11371936f2c65bdc2b8a8238856be79"></a>

### `NXP_LLWU_MODULE_0`

```c
#define NXP_LLWU_MODULE_0 NXP_LLWU_MODULE_WAKEUP(1)
```

模块（MODULE）0 唤醒源（Wakeup Source）。

<a id="a46c14dc1f55ee0b4e878af6b54838a41"></a>

### `NXP_LLWU_MODULE_1`

```c
#define NXP_LLWU_MODULE_1 NXP_LLWU_MODULE_WAKEUP(2)
```

模块（MODULE）1 唤醒源（Wakeup Source）。

<a id="a77573e26df2580d83c39f2f8bcaa45fc"></a>

### `NXP_LLWU_MODULE_2`

```c
#define NXP_LLWU_MODULE_2 NXP_LLWU_MODULE_WAKEUP(3)
```

模块（MODULE）2 唤醒源（Wakeup Source）。

<a id="a0b9fb27b28bf3371d7e7e6d61dfbf1bb"></a>

### `NXP_LLWU_MODULE_3`

```c
#define NXP_LLWU_MODULE_3 NXP_LLWU_MODULE_WAKEUP(4)
```

模块（MODULE）3 唤醒源（Wakeup Source）。

<a id="a45cb21fe5351cbb071784c521d5d8ae3"></a>

### `NXP_LLWU_MODULE_4`

```c
#define NXP_LLWU_MODULE_4 NXP_LLWU_MODULE_WAKEUP(5)
```

模块（MODULE）4 唤醒源（Wakeup Source）。

<a id="aa79bbe27e253758a3ebd2d1adb34c96a"></a>

### `NXP_LLWU_MODULE_5`

```c
#define NXP_LLWU_MODULE_5 NXP_LLWU_MODULE_WAKEUP(6)
```

模块（MODULE）5 唤醒源（Wakeup Source）。

<a id="a8bdca3adfb7b576ad8be483f535bc0c9"></a>

### `NXP_LLWU_MODULE_6`

```c
#define NXP_LLWU_MODULE_6 NXP_LLWU_MODULE_WAKEUP(7)
```

模块（MODULE）6 唤醒源（Wakeup Source）。

<a id="ad613fb79d2cba1fb24bdeb0e53bd9f32"></a>

### `NXP_LLWU_MODULE_7`

```c
#define NXP_LLWU_MODULE_7 NXP_LLWU_MODULE_WAKEUP(8)
```

模块（MODULE）7 唤醒源（Wakeup Source）。

<a id="a42f98709320b42c357242cc34907e07f"></a>

### `NXP_LLWU_MODULE_WAKEUP`

```c
#define NXP_LLWU_MODULE_WAKEUP ( module_index)
```

展开值（Value）：

```c
(NXP_LLWU_WAKEUP_SOURCE_TYPE_MODULE | ((module_index) & 0xFF))
```

编码模块唤醒源（MODULE Wakeup Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `module_index` | 模块索引（Module Index），范围为 0–255。 |

<a id="a980e9e02e626a2a8add3979cab3f1332"></a>

### `NXP_LLWU_PIN_0_ANY`

```c
#define NXP_LLWU_PIN_0_ANY NXP_LLWU_PIN_WAKEUP(1, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）0 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="a45fe5784d5b7cca2489900995e786aa5"></a>

### `NXP_LLWU_PIN_0_FALLING`

```c
#define NXP_LLWU_PIN_0_FALLING NXP_LLWU_PIN_WAKEUP(1, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）0 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="a22b1ef0b1254105352d47cc498d71bdb"></a>

### `NXP_LLWU_PIN_0_RISING`

```c
#define NXP_LLWU_PIN_0_RISING NXP_LLWU_PIN_WAKEUP(1, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）0 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="a75bedf07680f4c67c3a0bcf08a996246"></a>

### `NXP_LLWU_PIN_10_ANY`

```c
#define NXP_LLWU_PIN_10_ANY NXP_LLWU_PIN_WAKEUP(11, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）10 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="aae37151a99975e603145519c9269aebd"></a>

### `NXP_LLWU_PIN_10_FALLING`

```c
#define NXP_LLWU_PIN_10_FALLING NXP_LLWU_PIN_WAKEUP(11, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）10 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="ad87fff5279065c83c505ca8862f5ce43"></a>

### `NXP_LLWU_PIN_10_RISING`

```c
#define NXP_LLWU_PIN_10_RISING NXP_LLWU_PIN_WAKEUP(11, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）10 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="a1738c695813210ae8f27eabd8d97e253"></a>

### `NXP_LLWU_PIN_11_ANY`

```c
#define NXP_LLWU_PIN_11_ANY NXP_LLWU_PIN_WAKEUP(12, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）11 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="a27205ae6b21f46a6d0c873eaddb5cf07"></a>

### `NXP_LLWU_PIN_11_FALLING`

```c
#define NXP_LLWU_PIN_11_FALLING NXP_LLWU_PIN_WAKEUP(12, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）11 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="a6de54c9d9fe7142734c1b652b42e6dff"></a>

### `NXP_LLWU_PIN_11_RISING`

```c
#define NXP_LLWU_PIN_11_RISING NXP_LLWU_PIN_WAKEUP(12, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）11 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="ad37b9013e5921c3d633f13c8e3178b08"></a>

### `NXP_LLWU_PIN_12_ANY`

```c
#define NXP_LLWU_PIN_12_ANY NXP_LLWU_PIN_WAKEUP(13, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）12 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="abe891cd82b0d5a7052f14c13c5b9ab33"></a>

### `NXP_LLWU_PIN_12_FALLING`

```c
#define NXP_LLWU_PIN_12_FALLING NXP_LLWU_PIN_WAKEUP(13, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）12 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="a494dd477f710fe6af73b6fd37d5cd55c"></a>

### `NXP_LLWU_PIN_12_RISING`

```c
#define NXP_LLWU_PIN_12_RISING NXP_LLWU_PIN_WAKEUP(13, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）12 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="ac129adccc27a78cdedd33d9ac3422744"></a>

### `NXP_LLWU_PIN_13_ANY`

```c
#define NXP_LLWU_PIN_13_ANY NXP_LLWU_PIN_WAKEUP(14, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）13 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="acd6e7cdf10048850c4c7459b33fd362c"></a>

### `NXP_LLWU_PIN_13_FALLING`

```c
#define NXP_LLWU_PIN_13_FALLING NXP_LLWU_PIN_WAKEUP(14, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）13 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="a4f510ce70552461c108644bac9502fb2"></a>

### `NXP_LLWU_PIN_13_RISING`

```c
#define NXP_LLWU_PIN_13_RISING NXP_LLWU_PIN_WAKEUP(14, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）13 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="a1420832d18e0fee76ab56659e17e60c4"></a>

### `NXP_LLWU_PIN_14_ANY`

```c
#define NXP_LLWU_PIN_14_ANY NXP_LLWU_PIN_WAKEUP(15, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）14 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="a5eb28cf71d130ddb470305516a3c89a9"></a>

### `NXP_LLWU_PIN_14_FALLING`

```c
#define NXP_LLWU_PIN_14_FALLING NXP_LLWU_PIN_WAKEUP(15, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）14 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="ac782572eb1fa31053985047cffde22f8"></a>

### `NXP_LLWU_PIN_14_RISING`

```c
#define NXP_LLWU_PIN_14_RISING NXP_LLWU_PIN_WAKEUP(15, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）14 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="a36d3145d6f7416718e85d7d39ddc4222"></a>

### `NXP_LLWU_PIN_15_ANY`

```c
#define NXP_LLWU_PIN_15_ANY NXP_LLWU_PIN_WAKEUP(16, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）15 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="a804bf1905ef87f4342352e9c2964523a"></a>

### `NXP_LLWU_PIN_15_FALLING`

```c
#define NXP_LLWU_PIN_15_FALLING NXP_LLWU_PIN_WAKEUP(16, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）15 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="ae2836bde65b62a025124a12e216a77dd"></a>

### `NXP_LLWU_PIN_15_RISING`

```c
#define NXP_LLWU_PIN_15_RISING NXP_LLWU_PIN_WAKEUP(16, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）15 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="a06dd86435aeb5787ab49e892f02f54a8"></a>

### `NXP_LLWU_PIN_1_ANY`

```c
#define NXP_LLWU_PIN_1_ANY NXP_LLWU_PIN_WAKEUP(2, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）1 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="a4ed3943d19a76686e66b9bb344f4a908"></a>

### `NXP_LLWU_PIN_1_FALLING`

```c
#define NXP_LLWU_PIN_1_FALLING NXP_LLWU_PIN_WAKEUP(2, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）1 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="afcc50892ef15c6d2aa6f4ef07039b00e"></a>

### `NXP_LLWU_PIN_1_RISING`

```c
#define NXP_LLWU_PIN_1_RISING NXP_LLWU_PIN_WAKEUP(2, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）1 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="acfb6fcfc63c21ac44a2027d357525b5c"></a>

### `NXP_LLWU_PIN_2_ANY`

```c
#define NXP_LLWU_PIN_2_ANY NXP_LLWU_PIN_WAKEUP(3, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）2 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="a996c8f9d240ab171b1b7824e0b2b495a"></a>

### `NXP_LLWU_PIN_2_FALLING`

```c
#define NXP_LLWU_PIN_2_FALLING NXP_LLWU_PIN_WAKEUP(3, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）2 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="a294bc086cea15dd19a9a1b3c88af8267"></a>

### `NXP_LLWU_PIN_2_RISING`

```c
#define NXP_LLWU_PIN_2_RISING NXP_LLWU_PIN_WAKEUP(3, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）2 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="a06646d29c8f8363a2ec79d5c806e7f8f"></a>

### `NXP_LLWU_PIN_3_ANY`

```c
#define NXP_LLWU_PIN_3_ANY NXP_LLWU_PIN_WAKEUP(4, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）3 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="a340d0e5b52e8ba7b2c52a034fc119955"></a>

### `NXP_LLWU_PIN_3_FALLING`

```c
#define NXP_LLWU_PIN_3_FALLING NXP_LLWU_PIN_WAKEUP(4, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）3 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="a5b5564e04d931ac894040816fd2b3836"></a>

### `NXP_LLWU_PIN_3_RISING`

```c
#define NXP_LLWU_PIN_3_RISING NXP_LLWU_PIN_WAKEUP(4, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）3 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="aeb3a101789e90b59759c3a73825c3b05"></a>

### `NXP_LLWU_PIN_4_ANY`

```c
#define NXP_LLWU_PIN_4_ANY NXP_LLWU_PIN_WAKEUP(5, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）4 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="a18dd9a8c12a6b00b5a2728e30422f7cb"></a>

### `NXP_LLWU_PIN_4_FALLING`

```c
#define NXP_LLWU_PIN_4_FALLING NXP_LLWU_PIN_WAKEUP(5, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）4 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="ade64cbebab222bd4d3a5191f1f6ea996"></a>

### `NXP_LLWU_PIN_4_RISING`

```c
#define NXP_LLWU_PIN_4_RISING NXP_LLWU_PIN_WAKEUP(5, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）4 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="a566eb44389dc80ae8c54181980e1edb7"></a>

### `NXP_LLWU_PIN_5_ANY`

```c
#define NXP_LLWU_PIN_5_ANY NXP_LLWU_PIN_WAKEUP(6, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）5 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="a425be15f35fd7a8f606f709282b08029"></a>

### `NXP_LLWU_PIN_5_FALLING`

```c
#define NXP_LLWU_PIN_5_FALLING NXP_LLWU_PIN_WAKEUP(6, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）5 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="a6b42990f9dd099943da7cf010bf3dfd9"></a>

### `NXP_LLWU_PIN_5_RISING`

```c
#define NXP_LLWU_PIN_5_RISING NXP_LLWU_PIN_WAKEUP(6, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）5 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="a8a8b4f5eb6d6eb1ae1dd5da52b43d955"></a>

### `NXP_LLWU_PIN_6_ANY`

```c
#define NXP_LLWU_PIN_6_ANY NXP_LLWU_PIN_WAKEUP(7, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）6 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="a9b68e1035813ce8b3a169f3ac0fcd40c"></a>

### `NXP_LLWU_PIN_6_FALLING`

```c
#define NXP_LLWU_PIN_6_FALLING NXP_LLWU_PIN_WAKEUP(7, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）6 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="a5406e8b3cdfc0ffa2745ca751683a1f1"></a>

### `NXP_LLWU_PIN_6_RISING`

```c
#define NXP_LLWU_PIN_6_RISING NXP_LLWU_PIN_WAKEUP(7, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）6 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="a1a478e2b3fb681c9d4a0aeafd22a3a70"></a>

### `NXP_LLWU_PIN_7_ANY`

```c
#define NXP_LLWU_PIN_7_ANY NXP_LLWU_PIN_WAKEUP(8, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）7 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="af37b9fed47d8d39e73c38653e6f2ec07"></a>

### `NXP_LLWU_PIN_7_FALLING`

```c
#define NXP_LLWU_PIN_7_FALLING NXP_LLWU_PIN_WAKEUP(8, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）7 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="a73259733dcf1332c36a3f4c985e8c821"></a>

### `NXP_LLWU_PIN_7_RISING`

```c
#define NXP_LLWU_PIN_7_RISING NXP_LLWU_PIN_WAKEUP(8, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）7 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="a14fa6ee01a2b19075a47233667d2bfa8"></a>

### `NXP_LLWU_PIN_8_ANY`

```c
#define NXP_LLWU_PIN_8_ANY NXP_LLWU_PIN_WAKEUP(9, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）8 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="af8d39ccb96fad92a57289f010c7718c6"></a>

### `NXP_LLWU_PIN_8_FALLING`

```c
#define NXP_LLWU_PIN_8_FALLING NXP_LLWU_PIN_WAKEUP(9, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）8 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="a4545f103ce2b50e55a87a3002f7c29ca"></a>

### `NXP_LLWU_PIN_8_RISING`

```c
#define NXP_LLWU_PIN_8_RISING NXP_LLWU_PIN_WAKEUP(9, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）8 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="a15db4a9eea60578699381615d8b5ae4b"></a>

### `NXP_LLWU_PIN_9_ANY`

```c
#define NXP_LLWU_PIN_9_ANY NXP_LLWU_PIN_WAKEUP(10, NXP_LLWU_PIN_EDGE_ANY)
```

引脚（PIN）9 的任意边沿（Any Edge）唤醒源（Wakeup Source）。

<a id="a6bd22f657dd21231cd15e9ec3505e09e"></a>

### `NXP_LLWU_PIN_9_FALLING`

```c
#define NXP_LLWU_PIN_9_FALLING NXP_LLWU_PIN_WAKEUP(10, NXP_LLWU_PIN_EDGE_FALLING)
```

引脚（PIN）9 的下降沿（Falling Edge）唤醒源（Wakeup Source）。

<a id="a9a0af00768b95c706a5c46c5ddbd2855"></a>

### `NXP_LLWU_PIN_9_RISING`

```c
#define NXP_LLWU_PIN_9_RISING NXP_LLWU_PIN_WAKEUP(10, NXP_LLWU_PIN_EDGE_RISING)
```

引脚（PIN）9 的上升沿（Rising Edge）唤醒源（Wakeup Source）。

<a id="a02aec7b13ec302b9c4cc4fab57f7f0e1"></a>

### `NXP_LLWU_PIN_EDGE_ANY`

```c
#define NXP_LLWU_PIN_EDGE_ANY 3
```

任意边沿（Any Edge）的引脚边沿编码（PIN Edge Encoding）。

<a id="acf26a7cf25898931d83ea9b76f2691f1"></a>

### `NXP_LLWU_PIN_EDGE_FALLING`

```c
#define NXP_LLWU_PIN_EDGE_FALLING 2
```

下降沿（Falling Edge）的引脚边沿编码（PIN Edge Encoding）。

<a id="aee7a4ceedbe0e43e21d060349c20f081"></a>

### `NXP_LLWU_PIN_EDGE_RISING`

```c
#define NXP_LLWU_PIN_EDGE_RISING 1
```

上升沿（Rising Edge）的引脚边沿编码（PIN Edge Encoding）。

<a id="a38681f799daefdff2df71fbd7600eff0"></a>

### `NXP_LLWU_PIN_WAKEUP`

```c
#define NXP_LLWU_PIN_WAKEUP ( pin_index, edge_type )
```

展开值（Value）：

```c
(NXP_LLWU_WAKEUP_SOURCE_TYPE_PIN | (((edge_type) & 0x3) << 8) | ((pin_index) & 0xFF))
```

编码引脚唤醒源（PIN Wakeup Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin_index` | 引脚索引（PIN Index），范围为 0–255。 |
| `edge_type` | 边沿编码（Edge Encoding），参见 `NXP_LLWU_PIN_EDGE_*`。 |

<a id="ad737cbcb7fc898d2e0710c1cfdecebe9"></a>

### `NXP_LLWU_WAKEUP_SOURCE_TYPE_MODULE`

```c
#define NXP_LLWU_WAKEUP_SOURCE_TYPE_MODULE (1U << 31)
```

模块源（MODULE Source）的唤醒源类型编码（Wakeup Source Type Encoding）。

<a id="a913770f517306b614c047ac04cb5c060"></a>

### `NXP_LLWU_WAKEUP_SOURCE_TYPE_PIN`

```c
#define NXP_LLWU_WAKEUP_SOURCE_TYPE_PIN (0U << 31)
```

引脚源（PIN Source）的唤醒源类型编码（Wakeup Source Type Encoding）。


## 10.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P930_wuc_nxp_llwu.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="awuc__nxp__llwu_8h_html_ad737cbcb7fc898d2e0710c1cfdecebe9"></a>
<a id="awuc__nxp__llwu_8h_html_a913770f517306b614c047ac04cb5c060"></a>

---

[上一章](P009_zephyr__net__wifi_mgmt.h_文件参考.md) · [返回大纲](大纲.md)
