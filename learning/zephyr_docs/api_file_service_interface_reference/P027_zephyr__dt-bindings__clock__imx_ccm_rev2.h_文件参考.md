---
id: learning.zephyr-docs.api-file-service-interface-reference.page-27
title: zephyr__dt-bindings__clock__imx_ccm_rev2.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm__rev2_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_dt-bindings\_\_clock\_\_imx\_ccm\_rev2.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm__rev2_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 27.1\_宏定义（Macros）

<a id="r_aa31bf3cf51ff3af717f0d4037eeaa1c9"></a>

```c
#define IMX_CCM_PERIPHERAL_MASK 0xFF00UL
```

相关声明：[IMX_CCM_PERIPHERAL_MASK](#aa31bf3cf51ff3af717f0d4037eeaa1c9)。

<a id="r_a30f30d268fb9aae738f27161e6028f73"></a>

```c
#define IMX_CCM_INSTANCE_MASK 0xFFUL
```

相关声明：[IMX_CCM_INSTANCE_MASK](#a30f30d268fb9aae738f27161e6028f73)。

<a id="r_ab1e95e431d7486c814c969d0d9c57559"></a>

```c
#define IMX_CCM_CORESYS_CLK 0
```

相关声明：[IMX_CCM_CORESYS_CLK](#ab1e95e431d7486c814c969d0d9c57559)。

<a id="r_afcda3a44b4029872bfa5d219f10dd506"></a>

```c
#define IMX_CCM_PLATFORM_CLK 0x1UL
```

相关声明：[IMX_CCM_PLATFORM_CLK](#afcda3a44b4029872bfa5d219f10dd506)。

<a id="r_a0f9e44ec176274d3792bb2dd3e21a28b"></a>

```c
#define IMX_CCM_BUS_CLK 0x2UL
```

相关声明：[IMX_CCM_BUS_CLK](#a0f9e44ec176274d3792bb2dd3e21a28b)。

<a id="r_adf198290939696f7902803f5597e12c3"></a>

```c
#define IMX_CCM_ARM_PLL_CLK 0x10UL
```

相关声明：[IMX_CCM_ARM_PLL_CLK](#adf198290939696f7902803f5597e12c3)。

<a id="r_a01fa41a7ad66c54b1c19455b6160bbc2"></a>

```c
#define IMX_CCM_LPUART_CLK 0x300UL
```

相关声明：[IMX_CCM_LPUART_CLK](#a01fa41a7ad66c54b1c19455b6160bbc2)。

<a id="r_a96e62b5b478ee548a1e52b7189a73817"></a>

```c
#define IMX_CCM_LPUART1_CLK 0x300UL
```

相关声明：[IMX_CCM_LPUART1_CLK](#a96e62b5b478ee548a1e52b7189a73817)。

<a id="r_a4459bcb9e8548ee79d6f870388cee030"></a>

```c
#define IMX_CCM_LPUART0102_CLK 0x300UL
```

相关声明：[IMX_CCM_LPUART0102_CLK](#a4459bcb9e8548ee79d6f870388cee030)。

<a id="r_a46255999d02ae6161981374872e065cf"></a>

```c
#define IMX_CCM_LPUART2_CLK 0x301UL
```

相关声明：[IMX_CCM_LPUART2_CLK](#a46255999d02ae6161981374872e065cf)。

<a id="r_ae5d1dfb25ea8f51fc5da0c320c4ee372"></a>

```c
#define IMX_CCM_LPUART0304_CLK 0x301UL
```

相关声明：[IMX_CCM_LPUART0304_CLK](#ae5d1dfb25ea8f51fc5da0c320c4ee372)。

<a id="r_a6676eb59f3d665c2a9bba7aae24228ca"></a>

```c
#define IMX_CCM_LPUART3_CLK 0x302UL
```

相关声明：[IMX_CCM_LPUART3_CLK](#a6676eb59f3d665c2a9bba7aae24228ca)。

<a id="r_a6bdd125cb6a16fc6f02dfc75a95585d5"></a>

```c
#define IMX_CCM_LPUART0506_CLK 0x302UL
```

相关声明：[IMX_CCM_LPUART0506_CLK](#a6bdd125cb6a16fc6f02dfc75a95585d5)。

<a id="r_a9647111e5a5af6e8e67e059009490974"></a>

```c
#define IMX_CCM_LPUART4_CLK 0x303UL
```

相关声明：[IMX_CCM_LPUART4_CLK](#a9647111e5a5af6e8e67e059009490974)。

<a id="r_ac6aa3928911070336e02949cc1461127"></a>

```c
#define IMX_CCM_LPUART0708_CLK 0x303UL
```

相关声明：[IMX_CCM_LPUART0708_CLK](#ac6aa3928911070336e02949cc1461127)。

<a id="r_acd84397a25a81c7f315c7740049d570a"></a>

```c
#define IMX_CCM_LPUART5_CLK 0x304UL
```

相关声明：[IMX_CCM_LPUART5_CLK](#acd84397a25a81c7f315c7740049d570a)。

<a id="r_a669759d71d3b5e52783182a9a5434e4e"></a>

```c
#define IMX_CCM_LPUART0910_CLK 0x304UL
```

相关声明：[IMX_CCM_LPUART0910_CLK](#a669759d71d3b5e52783182a9a5434e4e)。

<a id="r_a3c6916f6ff4fae75dc51177e25d51642"></a>

```c
#define IMX_CCM_LPUART6_CLK 0x305UL
```

相关声明：[IMX_CCM_LPUART6_CLK](#a3c6916f6ff4fae75dc51177e25d51642)。

<a id="r_af6a2a88b71cb02e35fce256aeb2989f2"></a>

```c
#define IMX_CCM_LPUART1112_CLK 0x305UL
```

相关声明：[IMX_CCM_LPUART1112_CLK](#af6a2a88b71cb02e35fce256aeb2989f2)。

<a id="r_a4f2f07925d50b73cdc218d1f99cedf98"></a>

```c
#define IMX_CCM_LPUART7_CLK 0x306UL
```

相关声明：[IMX_CCM_LPUART7_CLK](#a4f2f07925d50b73cdc218d1f99cedf98)。

<a id="r_a8db4fa3e674535ba490d89a52979cad0"></a>

```c
#define IMX_CCM_LPUART8_CLK 0x307UL
```

相关声明：[IMX_CCM_LPUART8_CLK](#a8db4fa3e674535ba490d89a52979cad0)。

<a id="r_a0a6f1a1a8141d825058fd5a2c2ca3914"></a>

```c
#define IMX_CCM_LPUART9_CLK 0x308UL
```

相关声明：[IMX_CCM_LPUART9_CLK](#a0a6f1a1a8141d825058fd5a2c2ca3914)。

<a id="r_a24307153d0dbf07b908ab1876ae1a4bc"></a>

```c
#define IMX_CCM_LPUART10_CLK 0x309UL
```

相关声明：[IMX_CCM_LPUART10_CLK](#a24307153d0dbf07b908ab1876ae1a4bc)。

<a id="r_af539f30a7a6cd9ee4aba7f2415b5b3e6"></a>

```c
#define IMX_CCM_LPUART11_CLK 0x30aUL
```

相关声明：[IMX_CCM_LPUART11_CLK](#af539f30a7a6cd9ee4aba7f2415b5b3e6)。

<a id="r_a68c212e56058fd3f59c8bb7bd7f25984"></a>

```c
#define IMX_CCM_LPUART12_CLK 0x30bUL
```

相关声明：[IMX_CCM_LPUART12_CLK](#a68c212e56058fd3f59c8bb7bd7f25984)。

<a id="r_ac970114caf03b14bf6d3f2ff04f548dc"></a>

```c
#define IMX_CCM_LPI2C_CLK 0x400UL
```

相关声明：[IMX_CCM_LPI2C_CLK](#ac970114caf03b14bf6d3f2ff04f548dc)。

<a id="r_aa9e61f731a664a0d34fdd2d861664984"></a>

```c
#define IMX_CCM_LPI2C0102_CLK 0x400UL
```

相关声明：[IMX_CCM_LPI2C0102_CLK](#aa9e61f731a664a0d34fdd2d861664984)。

<a id="r_a0868c0eeb69b0e67d6e2d022a9e55035"></a>

```c
#define IMX_CCM_LPI2C1_CLK 0x400UL
```

相关声明：[IMX_CCM_LPI2C1_CLK](#a0868c0eeb69b0e67d6e2d022a9e55035)。

<a id="r_a1a684ee49ada9866d61df70c8757bbf6"></a>

```c
#define IMX_CCM_LPI2C2_CLK 0x401UL
```

相关声明：[IMX_CCM_LPI2C2_CLK](#a1a684ee49ada9866d61df70c8757bbf6)。

<a id="r_a47f1911ab7ac9b94d1eec2c1c56cbae2"></a>

```c
#define IMX_CCM_LPI2C0304_CLK 0x401UL
```

相关声明：[IMX_CCM_LPI2C0304_CLK](#a47f1911ab7ac9b94d1eec2c1c56cbae2)。

<a id="r_a5d809939798eacedbbf59f38a57fb5ba"></a>

```c
#define IMX_CCM_LPI2C3_CLK 0x402UL
```

相关声明：[IMX_CCM_LPI2C3_CLK](#a5d809939798eacedbbf59f38a57fb5ba)。

<a id="r_aac755270370e533fb3f78e471f0efac7"></a>

```c
#define IMX_CCM_LPI2C4_CLK 0x403UL
```

相关声明：[IMX_CCM_LPI2C4_CLK](#aac755270370e533fb3f78e471f0efac7)。

<a id="r_ab630bdfa74efd8a0ec614a72ff54baa0"></a>

```c
#define IMX_CCM_LPI2C0506_CLK 0x402UL
```

相关声明：[IMX_CCM_LPI2C0506_CLK](#ab630bdfa74efd8a0ec614a72ff54baa0)。

<a id="r_a4a73ff0aa1615dfc1171689dbb76636b"></a>

```c
#define IMX_CCM_LPI2C5_CLK 0x404UL
```

相关声明：[IMX_CCM_LPI2C5_CLK](#a4a73ff0aa1615dfc1171689dbb76636b)。

<a id="r_a61d52e2b71b0eef06d76c8261df4ac1b"></a>

```c
#define IMX_CCM_LPI2C6_CLK 0x405UL
```

相关声明：[IMX_CCM_LPI2C6_CLK](#a61d52e2b71b0eef06d76c8261df4ac1b)。

<a id="r_a500f15ca8d67342db7c14d36344f1331"></a>

```c
#define IMX_CCM_LPI2C0708_CLK 0x403UL
```

相关声明：[IMX_CCM_LPI2C0708_CLK](#a500f15ca8d67342db7c14d36344f1331)。

<a id="r_a002cc9eac38583fca551917c1a1fa299"></a>

```c
#define IMX_CCM_LPI2C7_CLK 0x406UL
```

相关声明：[IMX_CCM_LPI2C7_CLK](#a002cc9eac38583fca551917c1a1fa299)。

<a id="r_ae7cecaf7c7b40bbc2654c3417ac729cc"></a>

```c
#define IMX_CCM_LPI2C8_CLK 0x407UL
```

相关声明：[IMX_CCM_LPI2C8_CLK](#ae7cecaf7c7b40bbc2654c3417ac729cc)。

<a id="r_a169487d4c020dee2492e36202fa39158"></a>

```c
#define IMX_CCM_LPSPI_CLK 0x500UL
```

相关声明：[IMX_CCM_LPSPI_CLK](#a169487d4c020dee2492e36202fa39158)。

<a id="r_a9bf00e2b9b23268f0ae8740fddab2a72"></a>

```c
#define IMX_CCM_LPSPI0102_CLK 0x500UL
```

相关声明：[IMX_CCM_LPSPI0102_CLK](#a9bf00e2b9b23268f0ae8740fddab2a72)。

<a id="r_aaa28d51204ece1b636cfb18ae1c40c36"></a>

```c
#define IMX_CCM_LPSPI1_CLK 0x500UL
```

相关声明：[IMX_CCM_LPSPI1_CLK](#aaa28d51204ece1b636cfb18ae1c40c36)。

<a id="r_af9033f72e88c27d5b423201a23ac8a31"></a>

```c
#define IMX_CCM_LPSPI2_CLK 0x501UL
```

相关声明：[IMX_CCM_LPSPI2_CLK](#af9033f72e88c27d5b423201a23ac8a31)。

<a id="r_a2b2b88ad7933da1cb04016da8ccf0a25"></a>

```c
#define IMX_CCM_LPSPI0304_CLK 0x501UL
```

相关声明：[IMX_CCM_LPSPI0304_CLK](#a2b2b88ad7933da1cb04016da8ccf0a25)。

<a id="r_a95f654b51e3b94c4f031734761b7db28"></a>

```c
#define IMX_CCM_LPSPI3_CLK 0x502UL
```

相关声明：[IMX_CCM_LPSPI3_CLK](#a95f654b51e3b94c4f031734761b7db28)。

<a id="r_a7ef7e62f3bc8b4dc6033628bb54d9f48"></a>

```c
#define IMX_CCM_LPSPI4_CLK 0x503UL
```

相关声明：[IMX_CCM_LPSPI4_CLK](#a7ef7e62f3bc8b4dc6033628bb54d9f48)。

<a id="r_a4f3bc494cbe43f46bc33111a64e6fcb1"></a>

```c
#define IMX_CCM_LPSPI0506_CLK 0x502UL
```

相关声明：[IMX_CCM_LPSPI0506_CLK](#a4f3bc494cbe43f46bc33111a64e6fcb1)。

<a id="r_ab77afa02a9375dac8d5241db2f6dcb1e"></a>

```c
#define IMX_CCM_LPSPI5_CLK 0x504UL
```

相关声明：[IMX_CCM_LPSPI5_CLK](#ab77afa02a9375dac8d5241db2f6dcb1e)。

<a id="r_aeaef0fae23329ccf26957f53414bb50e"></a>

```c
#define IMX_CCM_LPSPI6_CLK 0x505UL
```

相关声明：[IMX_CCM_LPSPI6_CLK](#aeaef0fae23329ccf26957f53414bb50e)。

<a id="r_a6d0905600641bf75064eb4c595e8137f"></a>

```c
#define IMX_CCM_LPSPI7_CLK 0x506UL
```

相关声明：[IMX_CCM_LPSPI7_CLK](#a6d0905600641bf75064eb4c595e8137f)。

<a id="r_a29897a97b6c47d61bc7e05785b54ea50"></a>

```c
#define IMX_CCM_LPSPI8_CLK 0x507UL
```

相关声明：[IMX_CCM_LPSPI8_CLK](#a29897a97b6c47d61bc7e05785b54ea50)。

<a id="r_a3f07127852de7ae5516c376589f1f780"></a>

```c
#define IMX_CCM_USDHC1_CLK 0x600UL
```

相关声明：[IMX_CCM_USDHC1_CLK](#a3f07127852de7ae5516c376589f1f780)。

<a id="r_a4596ce38e656971ec5330dab452bd04c"></a>

```c
#define IMX_CCM_USDHC2_CLK 0x601UL
```

相关声明：[IMX_CCM_USDHC2_CLK](#a4596ce38e656971ec5330dab452bd04c)。

<a id="r_ae57e6b058c2c473ecf41115506438252"></a>

```c
#define IMX_CCM_USDHC3_CLK 0x602UL
```

相关声明：[IMX_CCM_USDHC3_CLK](#ae57e6b058c2c473ecf41115506438252)。

uSDHC3 外设的时钟标识符（Clock Identifier）。

<a id="r_aa82ff051d04371deee96c754d93abb57"></a>

```c
#define IMX_CCM_EDMA_CLK 0x700UL
```

相关声明：[IMX_CCM_EDMA_CLK](#aa82ff051d04371deee96c754d93abb57)。

<a id="r_a6bd4f0c4c8fa888f986dedce8e0fc950"></a>

```c
#define IMX_CCM_EDMA_LPSR_CLK 0x701UL
```

相关声明：[IMX_CCM_EDMA_LPSR_CLK](#a6bd4f0c4c8fa888f986dedce8e0fc950)。

<a id="r_a88214a06aada868a5395adc0f198ac02"></a>

```c
#define IMX_CCM_EDMA3_CLK 0x700UL
```

相关声明：[IMX_CCM_EDMA3_CLK](#a88214a06aada868a5395adc0f198ac02)。

<a id="r_a975cdcdd652a63b64b2471ad332c557f"></a>

```c
#define IMX_CCM_EDMA4_CLK 0x701UL
```

相关声明：[IMX_CCM_EDMA4_CLK](#a975cdcdd652a63b64b2471ad332c557f)。

<a id="r_acbc9256c26bb1232c5ca0eb8bfe52c22"></a>

```c
#define IMX_CCM_PWM_CLK 0x800UL
```

相关声明：[IMX_CCM_PWM_CLK](#acbc9256c26bb1232c5ca0eb8bfe52c22)。

<a id="r_aded96aef4768dd5f01d14a163cd7487d"></a>

```c
#define IMX_CCM_CAN_CLK 0x900UL
```

相关声明：[IMX_CCM_CAN_CLK](#aded96aef4768dd5f01d14a163cd7487d)。

<a id="r_a8b4a233a49bf6b078b2b0b51883a49c7"></a>

```c
#define IMX_CCM_CAN1_CLK 0x900UL
```

相关声明：[IMX_CCM_CAN1_CLK](#a8b4a233a49bf6b078b2b0b51883a49c7)。

<a id="r_ae82e9c205254fb85adaedc423cfc7e27"></a>

```c
#define IMX_CCM_CAN2_CLK 0x901UL
```

相关声明：[IMX_CCM_CAN2_CLK](#ae82e9c205254fb85adaedc423cfc7e27)。

<a id="r_a16a7e40f69be4d33dd9a9e6aeff03d5e"></a>

```c
#define IMX_CCM_CAN3_CLK 0x902UL
```

相关声明：[IMX_CCM_CAN3_CLK](#a16a7e40f69be4d33dd9a9e6aeff03d5e)。

<a id="r_aadc28bb4c97c89e86a8a437262a3afad"></a>

```c
#define IMX_CCM_GPT_CLK 0x1000UL
```

相关声明：[IMX_CCM_GPT_CLK](#aadc28bb4c97c89e86a8a437262a3afad)。

<a id="r_a63ddd8dcc8dca4c5a206348d67c0b57d"></a>

```c
#define IMX_CCM_GPT1_CLK 0x1000UL
```

相关声明：[IMX_CCM_GPT1_CLK](#a63ddd8dcc8dca4c5a206348d67c0b57d)。

<a id="r_a8fafcbbe14088a3372e681d0f4071ac3"></a>

```c
#define IMX_CCM_GPT2_CLK 0x1001UL
```

相关声明：[IMX_CCM_GPT2_CLK](#a8fafcbbe14088a3372e681d0f4071ac3)。

<a id="r_a08cba39dbed192509df1e404d49625d0"></a>

```c
#define IMX_CCM_GPT3_CLK 0x1002UL
```

相关声明：[IMX_CCM_GPT3_CLK](#a08cba39dbed192509df1e404d49625d0)。

<a id="r_a454f61392489e49a6534b1c115e6e868"></a>

```c
#define IMX_CCM_GPT4_CLK 0x1003UL
```

相关声明：[IMX_CCM_GPT4_CLK](#a454f61392489e49a6534b1c115e6e868)。

<a id="r_a491b53b9f223744586578ea0c1db987f"></a>

```c
#define IMX_CCM_GPT5_CLK 0x1004UL
```

相关声明：[IMX_CCM_GPT5_CLK](#a491b53b9f223744586578ea0c1db987f)。

<a id="r_a5892393e285e3cb1b9fcb5a65e29b66e"></a>

```c
#define IMX_CCM_GPT6_CLK 0x1005UL
```

相关声明：[IMX_CCM_GPT6_CLK](#a5892393e285e3cb1b9fcb5a65e29b66e)。

<a id="r_a398527cf42962caf290b9ce1e5d7f9ac"></a>

```c
#define IMX_CCM_SAI1_CLK 0x1100UL
```

相关声明：[IMX_CCM_SAI1_CLK](#a398527cf42962caf290b9ce1e5d7f9ac)。

<a id="r_aae6ea492162692b3ae2dc6aed60cc08d"></a>

```c
#define IMX_CCM_SAI2_CLK 0x1101UL
```

相关声明：[IMX_CCM_SAI2_CLK](#aae6ea492162692b3ae2dc6aed60cc08d)。

<a id="r_a28779c577a92d4806239fe6e254d1a84"></a>

```c
#define IMX_CCM_SAI3_CLK 0x1102UL
```

相关声明：[IMX_CCM_SAI3_CLK](#a28779c577a92d4806239fe6e254d1a84)。

<a id="r_a598ae9134610f955e78e46a37c063098"></a>

```c
#define IMX_CCM_SAI4_CLK 0x1103UL
```

相关声明：[IMX_CCM_SAI4_CLK](#a598ae9134610f955e78e46a37c063098)。

<a id="r_aaeff78179dff600c88c1d1986b3976cd"></a>

```c
#define IMX_CCM_ENET_CLK 0x1200UL
```

相关声明：[IMX_CCM_ENET_CLK](#aaeff78179dff600c88c1d1986b3976cd)。

<a id="r_a2a4beef16589b00f9aca825e7419e9ff"></a>

```c
#define IMX_CCM_ENET_PLL 0x1201UL
```

相关声明：[IMX_CCM_ENET_PLL](#a2a4beef16589b00f9aca825e7419e9ff)。

<a id="r_a257c215169947f52e4246a6df2291775"></a>

```c
#define IMX_CCM_ENET1G_CLK 0x1202UL
```

相关声明：[IMX_CCM_ENET1G_CLK](#a257c215169947f52e4246a6df2291775)。

<a id="r_ab9673428588f2540a697febefae2a319"></a>

```c
#define IMX_CCM_ENET1G_PLL 0x1203UL
```

相关声明：[IMX_CCM_ENET1G_PLL](#ab9673428588f2540a697febefae2a319)。

<a id="r_a5f86bba59cc685682df75e66a5d64cea"></a>

```c
#define IMX_CCM_FLEXSPI_CLK 0x1300UL
```

相关声明：[IMX_CCM_FLEXSPI_CLK](#a5f86bba59cc685682df75e66a5d64cea)。

<a id="r_aa471a61b4b453551839b29322ec21422"></a>

```c
#define IMX_CCM_FLEXSPI2_CLK 0x1301UL
```

相关声明：[IMX_CCM_FLEXSPI2_CLK](#aa471a61b4b453551839b29322ec21422)。

<a id="r_a0089a79d220e999a846afc32a827aeb7"></a>

```c
#define IMX_CCM_PIT_CLK 0x1400UL
```

相关声明：[IMX_CCM_PIT_CLK](#a0089a79d220e999a846afc32a827aeb7)。

<a id="r_a9b032bd27d83a8a84781301acc00d258"></a>

```c
#define IMX_CCM_PIT1_CLK 0x1401UL
```

相关声明：[IMX_CCM_PIT1_CLK](#a9b032bd27d83a8a84781301acc00d258)。

<a id="r_a468a092e9e42b4f14ad01a40b6d1dbf3"></a>

```c
#define IMX_CCM_LPADC1_CLK 0x1500UL
```

相关声明：[IMX_CCM_LPADC1_CLK](#a468a092e9e42b4f14ad01a40b6d1dbf3)。

<a id="r_a9e3ce71bfe0612062683dc5f63dac969"></a>

```c
#define IMX_CCM_LPADC2_CLK 0x1501UL
```

相关声明：[IMX_CCM_LPADC2_CLK](#a9e3ce71bfe0612062683dc5f63dac969)。

<a id="r_afcf3940b6ebf99cb3d47faabeb451508"></a>

```c
#define IMX_CCM_SAR_ADC1_CLK 0x1500UL
```

相关声明：[IMX_CCM_SAR_ADC1_CLK](#afcf3940b6ebf99cb3d47faabeb451508)。

<a id="r_a7ae96c7e510274652980837980fa9ac1"></a>

```c
#define IMX_CCM_TPM_CLK 0x1600UL
```

相关声明：[IMX_CCM_TPM_CLK](#a7ae96c7e510274652980837980fa9ac1)。

<a id="r_a637c8e9b2aeed7728321d088dd54bcac"></a>

```c
#define IMX_CCM_TPM1_CLK 0x1600UL
```

相关声明：[IMX_CCM_TPM1_CLK](#a637c8e9b2aeed7728321d088dd54bcac)。

<a id="r_afb0aa61bbd95e292b049b9c2939fc876"></a>

```c
#define IMX_CCM_TPM2_CLK 0x1601UL
```

相关声明：[IMX_CCM_TPM2_CLK](#afb0aa61bbd95e292b049b9c2939fc876)。

<a id="r_aacb38462fec372af3e8f0006ca32043e"></a>

```c
#define IMX_CCM_TPM3_CLK 0x1602UL
```

相关声明：[IMX_CCM_TPM3_CLK](#aacb38462fec372af3e8f0006ca32043e)。

<a id="r_abfd242434f7f9e78e1ad3bd7a4ae25db"></a>

```c
#define IMX_CCM_TPM4_CLK 0x1603UL
```

相关声明：[IMX_CCM_TPM4_CLK](#abfd242434f7f9e78e1ad3bd7a4ae25db)。

<a id="r_acc7dc668e7569249ff7626225890a2a5"></a>

```c
#define IMX_CCM_TPM5_CLK 0x1604UL
```

相关声明：[IMX_CCM_TPM5_CLK](#acc7dc668e7569249ff7626225890a2a5)。

<a id="r_a8872b4f8a671c35c78ff7c08cd7e6942"></a>

```c
#define IMX_CCM_TPM6_CLK 0x1605UL
```

相关声明：[IMX_CCM_TPM6_CLK](#a8872b4f8a671c35c78ff7c08cd7e6942)。

<a id="r_a9ad863eb4ce997479d920655671a09fd"></a>

```c
#define IMX_CCM_FLEXIO_CLK 0x1700UL
```

相关声明：[IMX_CCM_FLEXIO_CLK](#a9ad863eb4ce997479d920655671a09fd)。

<a id="r_a56168563c208301c93c6d54cb06c3a34"></a>

```c
#define IMX_CCM_FLEXIO1_CLK 0x1700UL
```

相关声明：[IMX_CCM_FLEXIO1_CLK](#a56168563c208301c93c6d54cb06c3a34)。

<a id="r_a7854576ab6fab4ef52a210ca26059393"></a>

```c
#define IMX_CCM_FLEXIO2_CLK 0x1701UL
```

相关声明：[IMX_CCM_FLEXIO2_CLK](#a7854576ab6fab4ef52a210ca26059393)。

<a id="r_aa4caa99fcf9e986b3e2c3b2a3f95e291"></a>

```c
#define IMX_CCM_NETC_CLK 0x1800UL
```

相关声明：[IMX_CCM_NETC_CLK](#aa4caa99fcf9e986b3e2c3b2a3f95e291)。

<a id="r_a43b3fdcb2384b7689780beba72fe7d37"></a>

```c
#define IMX_CCM_MIPI_CSI2RX_ROOT_CLK 0x1900UL
```

相关声明：[IMX_CCM_MIPI_CSI2RX_ROOT_CLK](#a43b3fdcb2384b7689780beba72fe7d37)。

<a id="r_ae94af9f0e8ebc5c40316bb59b89e9f05"></a>

```c
#define IMX_CCM_MIPI_CSI2RX_UI_CLK 0x2000UL
```

相关声明：[IMX_CCM_MIPI_CSI2RX_UI_CLK](#ae94af9f0e8ebc5c40316bb59b89e9f05)。

<a id="r_a0ef128918b36cbef23107ab6c33c017b"></a>

```c
#define IMX_CCM_MIPI_CSI2RX_ESC_CLK 0x2100UL
```

相关声明：[IMX_CCM_MIPI_CSI2RX_ESC_CLK](#a0ef128918b36cbef23107ab6c33c017b)。

<a id="r_abf5c4810b6a015240a05b1147283abe2"></a>

```c
#define IMX_CCM_I3C_CLK 0x2200UL
```

相关声明：[IMX_CCM_I3C_CLK](#abf5c4810b6a015240a05b1147283abe2)。

<a id="r_a644f18c38276ab00774d701c3244b277"></a>

```c
#define IMX_CCM_I3C1_CLK 0x2200UL
```

相关声明：[IMX_CCM_I3C1_CLK](#a644f18c38276ab00774d701c3244b277)。

<a id="r_a2dc53c128b4adffbcde9d3292ff76128"></a>

```c
#define IMX_CCM_I3C2_CLK 0x2201UL
```

相关声明：[IMX_CCM_I3C2_CLK](#a2dc53c128b4adffbcde9d3292ff76128)。

<a id="r_acedd3a1794ca0739600490d6a4f836bd"></a>

```c
#define IMX_CCM_LPIT_CLK 0x2300UL
```

相关声明：[IMX_CCM_LPIT_CLK](#acedd3a1794ca0739600490d6a4f836bd)。

<a id="r_afd5eab6d715da414a3f07621dc281555"></a>

```c
#define IMX_CCM_LPIT1_CLK 0x2300UL
```

相关声明：[IMX_CCM_LPIT1_CLK](#afd5eab6d715da414a3f07621dc281555)。

<a id="r_aa796a242725551a64149b2cea7842bfd"></a>

```c
#define IMX_CCM_LPIT2_CLK 0x2301UL
```

相关声明：[IMX_CCM_LPIT2_CLK](#aa796a242725551a64149b2cea7842bfd)。

<a id="r_a7abc69a92d8542fe2c7084083070057e"></a>

```c
#define IMX_CCM_LPIT3_CLK 0x2302UL
```

相关声明：[IMX_CCM_LPIT3_CLK](#a7abc69a92d8542fe2c7084083070057e)。

<a id="r_a478aeb7b31d614943310a8793cee0b85"></a>

```c
#define IMX_CCM_KPP_CLK 0x2400UL
```

相关声明：[IMX_CCM_KPP_CLK](#a478aeb7b31d614943310a8793cee0b85)。

<a id="r_ad5206cd1ff1f809c50489f9c7c1d814f"></a>

```c
#define IMX_CCM_USB_CLK 0x2500UL
```

相关声明：[IMX_CCM_USB_CLK](#ad5206cd1ff1f809c50489f9c7c1d814f)。

<a id="r_a50507c60894da64010102639d333d1fc"></a>

```c
#define IMX_CCM_USB_PHY_CLK 0x2600UL
```

相关声明：[IMX_CCM_USB_PHY_CLK](#a50507c60894da64010102639d333d1fc)。

<a id="r_a1276e0f0877704daf1ddb157560e7042"></a>

```c
#define IMX_CCM_SYSCTR_BASE_CLK 0x2700UL
```

相关声明：[IMX_CCM_SYSCTR_BASE_CLK](#a1276e0f0877704daf1ddb157560e7042)。

SYS_CTR 的 24 MHz 晶体振荡器（XTAL）基准时钟。

<a id="r_af4c04304d83773edb20b2b577c7392d8"></a>

```c
#define IMX_CCM_SYSCTR_SLOW_CLK 0x2701UL
```

相关声明：[IMX_CCM_SYSCTR_SLOW_CLK](#af4c04304d83773edb20b2b577c7392d8)。

SYS_CTR 的 32 kHz 低功耗振荡器（LPO）慢时钟。

<a id="r_a8d6e19325f01f337dab1cf3aeda28cf7"></a>

```c
#define IMX_CCM_PDM_CLK 0x2800UL
```

相关声明：[IMX_CCM_PDM_CLK](#a8d6e19325f01f337dab1cf3aeda28cf7)。

脉冲密度调制／麦克风滤波器（PDM/MICFIL）时钟标识符。

<a id="r_abb42c73d79bfbf06c59e5df1ccd5f53f"></a>

```c
#define IMX_CCM_XBAR1_CLK 0x2900UL
```

相关声明：[IMX_CCM_XBAR1_CLK](#abb42c73d79bfbf06c59e5df1ccd5f53f)。

XBAR1 外设时钟标识符（peripheral clock identifier）。

<a id="r_a1eb87918bce0819b21ec087a5b6e1a56"></a>

```c
#define IMX_CCM_XBAR2_CLK 0x2901UL
```

相关声明：[IMX_CCM_XBAR2_CLK](#a1eb87918bce0819b21ec087a5b6e1a56)。

XBAR2 外设时钟标识符。

<a id="r_a826e76fa1b70598f1650a573c9d060ca"></a>

```c
#define IMX_CCM_XBAR3_CLK 0x2902UL
```

相关声明：[IMX_CCM_XBAR3_CLK](#a826e76fa1b70598f1650a573c9d060ca)。

XBAR3 外设时钟标识符。

<a id="r_a9f790b4b7a783f47f590d5a8f641032a"></a>

```c
#define IMX_CCM_ENC1_CLK 0x2A00UL
```

相关声明：[IMX_CCM_ENC1_CLK](#a9f790b4b7a783f47f590d5a8f641032a)。

ENC1/EQDC1 外设时钟标识符（Clock Identifier）。

<a id="r_afcd84484dc2a9af4232619d2a7d475a9"></a>

```c
#define IMX_CCM_ENC2_CLK 0x2A01UL
```

相关声明：[IMX_CCM_ENC2_CLK](#afcd84484dc2a9af4232619d2a7d475a9)。

ENC2/EQDC2 外设时钟标识符（Clock Identifier）。

<a id="r_a710f29a2c9834c0dc6a943c45b9e67c8"></a>

```c
#define IMX_CCM_ENC3_CLK 0x2A02UL
```

相关声明：[IMX_CCM_ENC3_CLK](#a710f29a2c9834c0dc6a943c45b9e67c8)。

ENC3/EQDC3 外设时钟标识符（Clock Identifier）。

<a id="r_a103e43b4b237869e3246a4e7253be8a5"></a>

```c
#define IMX_CCM_ENC4_CLK 0x2A03UL
```

相关声明：[IMX_CCM_ENC4_CLK](#a103e43b4b237869e3246a4e7253be8a5)。

ENC4/EQDC4 外设时钟标识符（Clock Identifier）。

<a id="r_a0cc7a30460bef2b0e6772a91539203a8"></a>

```c
#define IMX_CCM_QTMR_CLK 0x6000UL
```

相关声明：[IMX_CCM_QTMR_CLK](#a0cc7a30460bef2b0e6772a91539203a8)。

<a id="r_a45f43085103b5710760bb8e563a162b2"></a>

```c
#define IMX_CCM_QTMR1_CLK 0x6000UL
```

相关声明：[IMX_CCM_QTMR1_CLK](#a45f43085103b5710760bb8e563a162b2)。

<a id="r_a7072a686fb2371f7e5d2f5b8be643a49"></a>

```c
#define IMX_CCM_QTMR2_CLK 0x6001UL
```

相关声明：[IMX_CCM_QTMR2_CLK](#a7072a686fb2371f7e5d2f5b8be643a49)。

<a id="r_acf2ef975d1db2edd6b731b6aeb22e3ba"></a>

```c
#define IMX_CCM_QTMR3_CLK 0x6002UL
```

相关声明：[IMX_CCM_QTMR3_CLK](#acf2ef975d1db2edd6b731b6aeb22e3ba)。

<a id="r_a0fe48daeeac26140123438ccfd0aaed7"></a>

```c
#define IMX_CCM_QTMR4_CLK 0x6003UL
```

相关声明：[IMX_CCM_QTMR4_CLK](#a0fe48daeeac26140123438ccfd0aaed7)。

<a id="r_a44de513dd471b32e01822cd8db1ff007"></a>

```c
#define IMX_CCM_MEDIA_AXI_CLK 0x3000UL
```

相关声明：[IMX_CCM_MEDIA_AXI_CLK](#a44de513dd471b32e01822cd8db1ff007)。

<a id="r_abb25717604db5e0decbcf6e39e6db29f"></a>

```c
#define IMX_CCM_MEDIA_APB_CLK 0x3100UL
```

相关声明：[IMX_CCM_MEDIA_APB_CLK](#abb25717604db5e0decbcf6e39e6db29f)。

<a id="r_a0d49520e05ba5e7417878c7dad8bdb9f"></a>

```c
#define IMX_CCM_MEDIA_DISP_PIX_CLK 0x3200UL
```

相关声明：[IMX_CCM_MEDIA_DISP_PIX_CLK](#a0d49520e05ba5e7417878c7dad8bdb9f)。

<a id="r_a8aebddf75fdbedcd2bfc699c76f0a2f9"></a>

```c
#define IMX_CCM_MEDIA_LDB_CLK 0x3300UL
```

相关声明：[IMX_CCM_MEDIA_LDB_CLK](#a8aebddf75fdbedcd2bfc699c76f0a2f9)。

<a id="r_a136623e8f54d2767ad6bee4e745bb2f4"></a>

```c
#define IMX_CCM_MIPI_PHY_CFG_CLK 0x3400UL
```

相关声明：[IMX_CCM_MIPI_PHY_CFG_CLK](#a136623e8f54d2767ad6bee4e745bb2f4)。

<a id="r_ac3bf5ef15b59707a0c1c867de0bb1d92"></a>

```c
#define IMX_CCM_CAM_PIX_CLK 0x3500UL
```

相关声明：[IMX_CCM_CAM_PIX_CLK](#ac3bf5ef15b59707a0c1c867de0bb1d92)。

## 27.2\_详细说明（Detailed Documentation）

<a id="adf198290939696f7902803f5597e12c3"></a>

### `IMX_CCM_ARM_PLL_CLK`

```c
#define IMX_CCM_ARM_PLL_CLK 0x10UL
```

<a id="a0f9e44ec176274d3792bb2dd3e21a28b"></a>

### `IMX_CCM_BUS_CLK`

```c
#define IMX_CCM_BUS_CLK 0x2UL
```

<a id="ac3bf5ef15b59707a0c1c867de0bb1d92"></a>

### `IMX_CCM_CAM_PIX_CLK`

```c
#define IMX_CCM_CAM_PIX_CLK 0x3500UL
```

<a id="a8b4a233a49bf6b078b2b0b51883a49c7"></a>

### `IMX_CCM_CAN1_CLK`

```c
#define IMX_CCM_CAN1_CLK 0x900UL
```

<a id="ae82e9c205254fb85adaedc423cfc7e27"></a>

### `IMX_CCM_CAN2_CLK`

```c
#define IMX_CCM_CAN2_CLK 0x901UL
```

<a id="a16a7e40f69be4d33dd9a9e6aeff03d5e"></a>

### `IMX_CCM_CAN3_CLK`

```c
#define IMX_CCM_CAN3_CLK 0x902UL
```

<a id="aded96aef4768dd5f01d14a163cd7487d"></a>

### `IMX_CCM_CAN_CLK`

```c
#define IMX_CCM_CAN_CLK 0x900UL
```

<a id="ab1e95e431d7486c814c969d0d9c57559"></a>

### `IMX_CCM_CORESYS_CLK`

```c
#define IMX_CCM_CORESYS_CLK 0
```

<a id="a88214a06aada868a5395adc0f198ac02"></a>

### `IMX_CCM_EDMA3_CLK`

```c
#define IMX_CCM_EDMA3_CLK 0x700UL
```

<a id="a975cdcdd652a63b64b2471ad332c557f"></a>

### `IMX_CCM_EDMA4_CLK`

```c
#define IMX_CCM_EDMA4_CLK 0x701UL
```

<a id="aa82ff051d04371deee96c754d93abb57"></a>

### `IMX_CCM_EDMA_CLK`

```c
#define IMX_CCM_EDMA_CLK 0x700UL
```

<a id="a6bd4f0c4c8fa888f986dedce8e0fc950"></a>

### `IMX_CCM_EDMA_LPSR_CLK`

```c
#define IMX_CCM_EDMA_LPSR_CLK 0x701UL
```

<a id="a9f790b4b7a783f47f590d5a8f641032a"></a>

### `IMX_CCM_ENC1_CLK`

```c
#define IMX_CCM_ENC1_CLK 0x2A00UL
```

ENC1/EQDC1 外设时钟标识符（Clock Identifier）。

<a id="afcd84484dc2a9af4232619d2a7d475a9"></a>

### `IMX_CCM_ENC2_CLK`

```c
#define IMX_CCM_ENC2_CLK 0x2A01UL
```

ENC2/EQDC2 外设时钟标识符（Clock Identifier）。

<a id="a710f29a2c9834c0dc6a943c45b9e67c8"></a>

### `IMX_CCM_ENC3_CLK`

```c
#define IMX_CCM_ENC3_CLK 0x2A02UL
```

ENC3/EQDC3 外设时钟标识符（Clock Identifier）。

<a id="a103e43b4b237869e3246a4e7253be8a5"></a>

### `IMX_CCM_ENC4_CLK`

```c
#define IMX_CCM_ENC4_CLK 0x2A03UL
```

ENC4/EQDC4 外设时钟标识符（Clock Identifier）。

<a id="a257c215169947f52e4246a6df2291775"></a>

### `IMX_CCM_ENET1G_CLK`

```c
#define IMX_CCM_ENET1G_CLK 0x1202UL
```

<a id="ab9673428588f2540a697febefae2a319"></a>

### `IMX_CCM_ENET1G_PLL`

```c
#define IMX_CCM_ENET1G_PLL 0x1203UL
```

<a id="aaeff78179dff600c88c1d1986b3976cd"></a>

### `IMX_CCM_ENET_CLK`

```c
#define IMX_CCM_ENET_CLK 0x1200UL
```

<a id="a2a4beef16589b00f9aca825e7419e9ff"></a>

### `IMX_CCM_ENET_PLL`

```c
#define IMX_CCM_ENET_PLL 0x1201UL
```

<a id="a56168563c208301c93c6d54cb06c3a34"></a>

### `IMX_CCM_FLEXIO1_CLK`

```c
#define IMX_CCM_FLEXIO1_CLK 0x1700UL
```

<a id="a7854576ab6fab4ef52a210ca26059393"></a>

### `IMX_CCM_FLEXIO2_CLK`

```c
#define IMX_CCM_FLEXIO2_CLK 0x1701UL
```

<a id="a9ad863eb4ce997479d920655671a09fd"></a>

### `IMX_CCM_FLEXIO_CLK`

```c
#define IMX_CCM_FLEXIO_CLK 0x1700UL
```

<a id="aa471a61b4b453551839b29322ec21422"></a>

### `IMX_CCM_FLEXSPI2_CLK`

```c
#define IMX_CCM_FLEXSPI2_CLK 0x1301UL
```

<a id="a5f86bba59cc685682df75e66a5d64cea"></a>

### `IMX_CCM_FLEXSPI_CLK`

```c
#define IMX_CCM_FLEXSPI_CLK 0x1300UL
```

<a id="a63ddd8dcc8dca4c5a206348d67c0b57d"></a>

### `IMX_CCM_GPT1_CLK`

```c
#define IMX_CCM_GPT1_CLK 0x1000UL
```

<a id="a8fafcbbe14088a3372e681d0f4071ac3"></a>

### `IMX_CCM_GPT2_CLK`

```c
#define IMX_CCM_GPT2_CLK 0x1001UL
```

<a id="a08cba39dbed192509df1e404d49625d0"></a>

### `IMX_CCM_GPT3_CLK`

```c
#define IMX_CCM_GPT3_CLK 0x1002UL
```

<a id="a454f61392489e49a6534b1c115e6e868"></a>

### `IMX_CCM_GPT4_CLK`

```c
#define IMX_CCM_GPT4_CLK 0x1003UL
```

<a id="a491b53b9f223744586578ea0c1db987f"></a>

### `IMX_CCM_GPT5_CLK`

```c
#define IMX_CCM_GPT5_CLK 0x1004UL
```

<a id="a5892393e285e3cb1b9fcb5a65e29b66e"></a>

### `IMX_CCM_GPT6_CLK`

```c
#define IMX_CCM_GPT6_CLK 0x1005UL
```

<a id="aadc28bb4c97c89e86a8a437262a3afad"></a>

### `IMX_CCM_GPT_CLK`

```c
#define IMX_CCM_GPT_CLK 0x1000UL
```

<a id="a644f18c38276ab00774d701c3244b277"></a>

### `IMX_CCM_I3C1_CLK`

```c
#define IMX_CCM_I3C1_CLK 0x2200UL
```

<a id="a2dc53c128b4adffbcde9d3292ff76128"></a>

### `IMX_CCM_I3C2_CLK`

```c
#define IMX_CCM_I3C2_CLK 0x2201UL
```

<a id="abf5c4810b6a015240a05b1147283abe2"></a>

### `IMX_CCM_I3C_CLK`

```c
#define IMX_CCM_I3C_CLK 0x2200UL
```

<a id="a30f30d268fb9aae738f27161e6028f73"></a>

### `IMX_CCM_INSTANCE_MASK`

```c
#define IMX_CCM_INSTANCE_MASK 0xFFUL
```

<a id="a478aeb7b31d614943310a8793cee0b85"></a>

### `IMX_CCM_KPP_CLK`

```c
#define IMX_CCM_KPP_CLK 0x2400UL
```

<a id="a468a092e9e42b4f14ad01a40b6d1dbf3"></a>

### `IMX_CCM_LPADC1_CLK`

```c
#define IMX_CCM_LPADC1_CLK 0x1500UL
```

<a id="a9e3ce71bfe0612062683dc5f63dac969"></a>

### `IMX_CCM_LPADC2_CLK`

```c
#define IMX_CCM_LPADC2_CLK 0x1501UL
```

<a id="aa9e61f731a664a0d34fdd2d861664984"></a>

### `IMX_CCM_LPI2C0102_CLK`

```c
#define IMX_CCM_LPI2C0102_CLK 0x400UL
```

<a id="a47f1911ab7ac9b94d1eec2c1c56cbae2"></a>

### `IMX_CCM_LPI2C0304_CLK`

```c
#define IMX_CCM_LPI2C0304_CLK 0x401UL
```

<a id="ab630bdfa74efd8a0ec614a72ff54baa0"></a>

### `IMX_CCM_LPI2C0506_CLK`

```c
#define IMX_CCM_LPI2C0506_CLK 0x402UL
```

<a id="a500f15ca8d67342db7c14d36344f1331"></a>

### `IMX_CCM_LPI2C0708_CLK`

```c
#define IMX_CCM_LPI2C0708_CLK 0x403UL
```

<a id="a0868c0eeb69b0e67d6e2d022a9e55035"></a>

### `IMX_CCM_LPI2C1_CLK`

```c
#define IMX_CCM_LPI2C1_CLK 0x400UL
```

<a id="a1a684ee49ada9866d61df70c8757bbf6"></a>

### `IMX_CCM_LPI2C2_CLK`

```c
#define IMX_CCM_LPI2C2_CLK 0x401UL
```

<a id="a5d809939798eacedbbf59f38a57fb5ba"></a>

### `IMX_CCM_LPI2C3_CLK`

```c
#define IMX_CCM_LPI2C3_CLK 0x402UL
```

<a id="aac755270370e533fb3f78e471f0efac7"></a>

### `IMX_CCM_LPI2C4_CLK`

```c
#define IMX_CCM_LPI2C4_CLK 0x403UL
```

<a id="a4a73ff0aa1615dfc1171689dbb76636b"></a>

### `IMX_CCM_LPI2C5_CLK`

```c
#define IMX_CCM_LPI2C5_CLK 0x404UL
```

<a id="a61d52e2b71b0eef06d76c8261df4ac1b"></a>

### `IMX_CCM_LPI2C6_CLK`

```c
#define IMX_CCM_LPI2C6_CLK 0x405UL
```

<a id="a002cc9eac38583fca551917c1a1fa299"></a>

### `IMX_CCM_LPI2C7_CLK`

```c
#define IMX_CCM_LPI2C7_CLK 0x406UL
```

<a id="ae7cecaf7c7b40bbc2654c3417ac729cc"></a>

### `IMX_CCM_LPI2C8_CLK`

```c
#define IMX_CCM_LPI2C8_CLK 0x407UL
```

<a id="ac970114caf03b14bf6d3f2ff04f548dc"></a>

### `IMX_CCM_LPI2C_CLK`

```c
#define IMX_CCM_LPI2C_CLK 0x400UL
```

<a id="afd5eab6d715da414a3f07621dc281555"></a>

### `IMX_CCM_LPIT1_CLK`

```c
#define IMX_CCM_LPIT1_CLK 0x2300UL
```

<a id="aa796a242725551a64149b2cea7842bfd"></a>

### `IMX_CCM_LPIT2_CLK`

```c
#define IMX_CCM_LPIT2_CLK 0x2301UL
```

<a id="a7abc69a92d8542fe2c7084083070057e"></a>

### `IMX_CCM_LPIT3_CLK`

```c
#define IMX_CCM_LPIT3_CLK 0x2302UL
```

<a id="acedd3a1794ca0739600490d6a4f836bd"></a>

### `IMX_CCM_LPIT_CLK`

```c
#define IMX_CCM_LPIT_CLK 0x2300UL
```

<a id="a9bf00e2b9b23268f0ae8740fddab2a72"></a>

### `IMX_CCM_LPSPI0102_CLK`

```c
#define IMX_CCM_LPSPI0102_CLK 0x500UL
```

<a id="a2b2b88ad7933da1cb04016da8ccf0a25"></a>

### `IMX_CCM_LPSPI0304_CLK`

```c
#define IMX_CCM_LPSPI0304_CLK 0x501UL
```

<a id="a4f3bc494cbe43f46bc33111a64e6fcb1"></a>

### `IMX_CCM_LPSPI0506_CLK`

```c
#define IMX_CCM_LPSPI0506_CLK 0x502UL
```

<a id="aaa28d51204ece1b636cfb18ae1c40c36"></a>

### `IMX_CCM_LPSPI1_CLK`

```c
#define IMX_CCM_LPSPI1_CLK 0x500UL
```

<a id="af9033f72e88c27d5b423201a23ac8a31"></a>

### `IMX_CCM_LPSPI2_CLK`

```c
#define IMX_CCM_LPSPI2_CLK 0x501UL
```

<a id="a95f654b51e3b94c4f031734761b7db28"></a>

### `IMX_CCM_LPSPI3_CLK`

```c
#define IMX_CCM_LPSPI3_CLK 0x502UL
```

<a id="a7ef7e62f3bc8b4dc6033628bb54d9f48"></a>

### `IMX_CCM_LPSPI4_CLK`

```c
#define IMX_CCM_LPSPI4_CLK 0x503UL
```

<a id="ab77afa02a9375dac8d5241db2f6dcb1e"></a>

### `IMX_CCM_LPSPI5_CLK`

```c
#define IMX_CCM_LPSPI5_CLK 0x504UL
```

<a id="aeaef0fae23329ccf26957f53414bb50e"></a>

### `IMX_CCM_LPSPI6_CLK`

```c
#define IMX_CCM_LPSPI6_CLK 0x505UL
```

<a id="a6d0905600641bf75064eb4c595e8137f"></a>

### `IMX_CCM_LPSPI7_CLK`

```c
#define IMX_CCM_LPSPI7_CLK 0x506UL
```

<a id="a29897a97b6c47d61bc7e05785b54ea50"></a>

### `IMX_CCM_LPSPI8_CLK`

```c
#define IMX_CCM_LPSPI8_CLK 0x507UL
```

<a id="a169487d4c020dee2492e36202fa39158"></a>

### `IMX_CCM_LPSPI_CLK`

```c
#define IMX_CCM_LPSPI_CLK 0x500UL
```

<a id="a4459bcb9e8548ee79d6f870388cee030"></a>

### `IMX_CCM_LPUART0102_CLK`

```c
#define IMX_CCM_LPUART0102_CLK 0x300UL
```

<a id="ae5d1dfb25ea8f51fc5da0c320c4ee372"></a>

### `IMX_CCM_LPUART0304_CLK`

```c
#define IMX_CCM_LPUART0304_CLK 0x301UL
```

<a id="a6bdd125cb6a16fc6f02dfc75a95585d5"></a>

### `IMX_CCM_LPUART0506_CLK`

```c
#define IMX_CCM_LPUART0506_CLK 0x302UL
```

<a id="ac6aa3928911070336e02949cc1461127"></a>

### `IMX_CCM_LPUART0708_CLK`

```c
#define IMX_CCM_LPUART0708_CLK 0x303UL
```

<a id="a669759d71d3b5e52783182a9a5434e4e"></a>

### `IMX_CCM_LPUART0910_CLK`

```c
#define IMX_CCM_LPUART0910_CLK 0x304UL
```

<a id="a24307153d0dbf07b908ab1876ae1a4bc"></a>

### `IMX_CCM_LPUART10_CLK`

```c
#define IMX_CCM_LPUART10_CLK 0x309UL
```

<a id="af6a2a88b71cb02e35fce256aeb2989f2"></a>

### `IMX_CCM_LPUART1112_CLK`

```c
#define IMX_CCM_LPUART1112_CLK 0x305UL
```

<a id="af539f30a7a6cd9ee4aba7f2415b5b3e6"></a>

### `IMX_CCM_LPUART11_CLK`

```c
#define IMX_CCM_LPUART11_CLK 0x30aUL
```

<a id="a68c212e56058fd3f59c8bb7bd7f25984"></a>

### `IMX_CCM_LPUART12_CLK`

```c
#define IMX_CCM_LPUART12_CLK 0x30bUL
```

<a id="a96e62b5b478ee548a1e52b7189a73817"></a>

### `IMX_CCM_LPUART1_CLK`

```c
#define IMX_CCM_LPUART1_CLK 0x300UL
```

<a id="a46255999d02ae6161981374872e065cf"></a>

### `IMX_CCM_LPUART2_CLK`

```c
#define IMX_CCM_LPUART2_CLK 0x301UL
```

<a id="a6676eb59f3d665c2a9bba7aae24228ca"></a>

### `IMX_CCM_LPUART3_CLK`

```c
#define IMX_CCM_LPUART3_CLK 0x302UL
```

<a id="a9647111e5a5af6e8e67e059009490974"></a>

### `IMX_CCM_LPUART4_CLK`

```c
#define IMX_CCM_LPUART4_CLK 0x303UL
```

<a id="acd84397a25a81c7f315c7740049d570a"></a>

### `IMX_CCM_LPUART5_CLK`

```c
#define IMX_CCM_LPUART5_CLK 0x304UL
```

<a id="a3c6916f6ff4fae75dc51177e25d51642"></a>

### `IMX_CCM_LPUART6_CLK`

```c
#define IMX_CCM_LPUART6_CLK 0x305UL
```

<a id="a4f2f07925d50b73cdc218d1f99cedf98"></a>

### `IMX_CCM_LPUART7_CLK`

```c
#define IMX_CCM_LPUART7_CLK 0x306UL
```

<a id="a8db4fa3e674535ba490d89a52979cad0"></a>

### `IMX_CCM_LPUART8_CLK`

```c
#define IMX_CCM_LPUART8_CLK 0x307UL
```

<a id="a0a6f1a1a8141d825058fd5a2c2ca3914"></a>

### `IMX_CCM_LPUART9_CLK`

```c
#define IMX_CCM_LPUART9_CLK 0x308UL
```

<a id="a01fa41a7ad66c54b1c19455b6160bbc2"></a>

### `IMX_CCM_LPUART_CLK`

```c
#define IMX_CCM_LPUART_CLK 0x300UL
```

<a id="abb25717604db5e0decbcf6e39e6db29f"></a>

### `IMX_CCM_MEDIA_APB_CLK`

```c
#define IMX_CCM_MEDIA_APB_CLK 0x3100UL
```

<a id="a44de513dd471b32e01822cd8db1ff007"></a>

### `IMX_CCM_MEDIA_AXI_CLK`

```c
#define IMX_CCM_MEDIA_AXI_CLK 0x3000UL
```

<a id="a0d49520e05ba5e7417878c7dad8bdb9f"></a>

### `IMX_CCM_MEDIA_DISP_PIX_CLK`

```c
#define IMX_CCM_MEDIA_DISP_PIX_CLK 0x3200UL
```

<a id="a8aebddf75fdbedcd2bfc699c76f0a2f9"></a>

### `IMX_CCM_MEDIA_LDB_CLK`

```c
#define IMX_CCM_MEDIA_LDB_CLK 0x3300UL
```

<a id="a0ef128918b36cbef23107ab6c33c017b"></a>

### `IMX_CCM_MIPI_CSI2RX_ESC_CLK`

```c
#define IMX_CCM_MIPI_CSI2RX_ESC_CLK 0x2100UL
```

<a id="a43b3fdcb2384b7689780beba72fe7d37"></a>

### `IMX_CCM_MIPI_CSI2RX_ROOT_CLK`

```c
#define IMX_CCM_MIPI_CSI2RX_ROOT_CLK 0x1900UL
```

<a id="ae94af9f0e8ebc5c40316bb59b89e9f05"></a>

### `IMX_CCM_MIPI_CSI2RX_UI_CLK`

```c
#define IMX_CCM_MIPI_CSI2RX_UI_CLK 0x2000UL
```

<a id="a136623e8f54d2767ad6bee4e745bb2f4"></a>

### `IMX_CCM_MIPI_PHY_CFG_CLK`

```c
#define IMX_CCM_MIPI_PHY_CFG_CLK 0x3400UL
```

<a id="aa4caa99fcf9e986b3e2c3b2a3f95e291"></a>

### `IMX_CCM_NETC_CLK`

```c
#define IMX_CCM_NETC_CLK 0x1800UL
```

<a id="a8d6e19325f01f337dab1cf3aeda28cf7"></a>

### `IMX_CCM_PDM_CLK`

```c
#define IMX_CCM_PDM_CLK 0x2800UL
```

脉冲密度调制／麦克风滤波器（PDM/MICFIL）时钟标识符。

<a id="aa31bf3cf51ff3af717f0d4037eeaa1c9"></a>

### `IMX_CCM_PERIPHERAL_MASK`

```c
#define IMX_CCM_PERIPHERAL_MASK 0xFF00UL
```

<a id="a9b032bd27d83a8a84781301acc00d258"></a>

### `IMX_CCM_PIT1_CLK`

```c
#define IMX_CCM_PIT1_CLK 0x1401UL
```

<a id="a0089a79d220e999a846afc32a827aeb7"></a>

### `IMX_CCM_PIT_CLK`

```c
#define IMX_CCM_PIT_CLK 0x1400UL
```

<a id="afcda3a44b4029872bfa5d219f10dd506"></a>

### `IMX_CCM_PLATFORM_CLK`

```c
#define IMX_CCM_PLATFORM_CLK 0x1UL
```

<a id="acbc9256c26bb1232c5ca0eb8bfe52c22"></a>

### `IMX_CCM_PWM_CLK`

```c
#define IMX_CCM_PWM_CLK 0x800UL
```

<a id="a45f43085103b5710760bb8e563a162b2"></a>

### `IMX_CCM_QTMR1_CLK`

```c
#define IMX_CCM_QTMR1_CLK 0x6000UL
```

<a id="a7072a686fb2371f7e5d2f5b8be643a49"></a>

### `IMX_CCM_QTMR2_CLK`

```c
#define IMX_CCM_QTMR2_CLK 0x6001UL
```

<a id="acf2ef975d1db2edd6b731b6aeb22e3ba"></a>

### `IMX_CCM_QTMR3_CLK`

```c
#define IMX_CCM_QTMR3_CLK 0x6002UL
```

<a id="a0fe48daeeac26140123438ccfd0aaed7"></a>

### `IMX_CCM_QTMR4_CLK`

```c
#define IMX_CCM_QTMR4_CLK 0x6003UL
```

<a id="a0cc7a30460bef2b0e6772a91539203a8"></a>

### `IMX_CCM_QTMR_CLK`

```c
#define IMX_CCM_QTMR_CLK 0x6000UL
```

<a id="a398527cf42962caf290b9ce1e5d7f9ac"></a>

### `IMX_CCM_SAI1_CLK`

```c
#define IMX_CCM_SAI1_CLK 0x1100UL
```

<a id="aae6ea492162692b3ae2dc6aed60cc08d"></a>

### `IMX_CCM_SAI2_CLK`

```c
#define IMX_CCM_SAI2_CLK 0x1101UL
```

<a id="a28779c577a92d4806239fe6e254d1a84"></a>

### `IMX_CCM_SAI3_CLK`

```c
#define IMX_CCM_SAI3_CLK 0x1102UL
```

<a id="a598ae9134610f955e78e46a37c063098"></a>

### `IMX_CCM_SAI4_CLK`

```c
#define IMX_CCM_SAI4_CLK 0x1103UL
```

<a id="afcf3940b6ebf99cb3d47faabeb451508"></a>

### `IMX_CCM_SAR_ADC1_CLK`

```c
#define IMX_CCM_SAR_ADC1_CLK 0x1500UL
```

<a id="a1276e0f0877704daf1ddb157560e7042"></a>

### `IMX_CCM_SYSCTR_BASE_CLK`

```c
#define IMX_CCM_SYSCTR_BASE_CLK 0x2700UL
```

SYS_CTR 的 24 MHz 晶体振荡器（XTAL）基准时钟。

<a id="af4c04304d83773edb20b2b577c7392d8"></a>

### `IMX_CCM_SYSCTR_SLOW_CLK`

```c
#define IMX_CCM_SYSCTR_SLOW_CLK 0x2701UL
```

SYS_CTR 的 32 kHz 低功耗振荡器（LPO）慢时钟。

<a id="a637c8e9b2aeed7728321d088dd54bcac"></a>

### `IMX_CCM_TPM1_CLK`

```c
#define IMX_CCM_TPM1_CLK 0x1600UL
```

<a id="afb0aa61bbd95e292b049b9c2939fc876"></a>

### `IMX_CCM_TPM2_CLK`

```c
#define IMX_CCM_TPM2_CLK 0x1601UL
```

<a id="aacb38462fec372af3e8f0006ca32043e"></a>

### `IMX_CCM_TPM3_CLK`

```c
#define IMX_CCM_TPM3_CLK 0x1602UL
```

<a id="abfd242434f7f9e78e1ad3bd7a4ae25db"></a>

### `IMX_CCM_TPM4_CLK`

```c
#define IMX_CCM_TPM4_CLK 0x1603UL
```

<a id="acc7dc668e7569249ff7626225890a2a5"></a>

### `IMX_CCM_TPM5_CLK`

```c
#define IMX_CCM_TPM5_CLK 0x1604UL
```

<a id="a8872b4f8a671c35c78ff7c08cd7e6942"></a>

### `IMX_CCM_TPM6_CLK`

```c
#define IMX_CCM_TPM6_CLK 0x1605UL
```

<a id="a7ae96c7e510274652980837980fa9ac1"></a>

### `IMX_CCM_TPM_CLK`

```c
#define IMX_CCM_TPM_CLK 0x1600UL
```

<a id="ad5206cd1ff1f809c50489f9c7c1d814f"></a>

### `IMX_CCM_USB_CLK`

```c
#define IMX_CCM_USB_CLK 0x2500UL
```

<a id="a50507c60894da64010102639d333d1fc"></a>

### `IMX_CCM_USB_PHY_CLK`

```c
#define IMX_CCM_USB_PHY_CLK 0x2600UL
```

<a id="a3f07127852de7ae5516c376589f1f780"></a>

### `IMX_CCM_USDHC1_CLK`

```c
#define IMX_CCM_USDHC1_CLK 0x600UL
```

<a id="a4596ce38e656971ec5330dab452bd04c"></a>

### `IMX_CCM_USDHC2_CLK`

```c
#define IMX_CCM_USDHC2_CLK 0x601UL
```

<a id="ae57e6b058c2c473ecf41115506438252"></a>

### `IMX_CCM_USDHC3_CLK`

```c
#define IMX_CCM_USDHC3_CLK 0x602UL
```

uSDHC3 外设的时钟标识符（Clock Identifier）。

<a id="abb42c73d79bfbf06c59e5df1ccd5f53f"></a>

### `IMX_CCM_XBAR1_CLK`

```c
#define IMX_CCM_XBAR1_CLK 0x2900UL
```

XBAR1 外设时钟标识符（peripheral clock identifier）。

<a id="a1eb87918bce0819b21ec087a5b6e1a56"></a>

### `IMX_CCM_XBAR2_CLK`

```c
#define IMX_CCM_XBAR2_CLK 0x2901UL
```

XBAR2 外设时钟标识符。

<a id="a826e76fa1b70598f1650a573c9d060ca"></a>

### `IMX_CCM_XBAR3_CLK`

```c
#define IMX_CCM_XBAR3_CLK 0x2902UL
```

XBAR3 外设时钟标识符。


## 27.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_socket_ethernet_reference/P004_imx_ccm_rev2.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P026_zephyr__dt-bindings__sensor__iis2iclx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__drivers__interrupt_controller__intc_rz_ext_irq.h_文件参考.md)
