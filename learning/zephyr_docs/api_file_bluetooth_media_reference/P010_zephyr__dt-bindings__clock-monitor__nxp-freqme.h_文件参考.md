---
id: learning.zephyr-docs.api-file-bluetooth-media-reference.page-10
title: zephyr__dt-bindings__clock-monitor__nxp-freqme.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp-freqme_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_dt-bindings\_\_clock-monitor\_\_nxp-freqme.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp-freqme_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NXP FREQME参考/目标路由（Reference / Target Routing）使用的INPUTMUX连接标记。

查看此文件的源码。

<a id="details"></a>

用于 NXP FREQME 参考源／目标源路由（Reference / Target Routing）的 INPUTMUX 连接编码（Connection Cookie）。数值与各设备 MCUX HAL 头文件 fsl_inputmux_connections.h 中的 inputmux_connection_t 枚举一致：`cookie = selector + (destination_register << PMUX_SHIFT)`。所有支持 FREQME 的 SoC 上，PMUX_SHIFT 均为 20。目标寄存器和各源的选择器编号随 SoC 系列而异，因此下面按系列分组，每组列出适用设备。设备树和驱动只负责附加该编码，硬件根据编码将连接路由至相应寄存器。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="r_afce68af2dc4640ce340ae319e67ccd23"></a>

```c
#define NXP_FREQME_PMUX_SHIFT 20
```

相关声明：[NXP_FREQME_PMUX_SHIFT](#afce68af2dc4640ce340ae319e67ccd23)。

连接编码（Connection Cookie）中目标多路复用寄存器（Destination Mux Register）的位位置。

<a id="r_a73311c47e8dce82fb7e534058bcd5f3d"></a>

```c
#define NXP_FREQME_SOURCE_UNCHANGED 0U
```

相关声明：[NXP_FREQME_SOURCE_UNCHANGED](#a73311c47e8dce82fb7e534058bcd5f3d)。

set_source() 的哨兵值（Sentinel）：保持该轴，即参考源或目标源，不变。

<a id="r_a506f2a1287403d8ec791c4ba0dea8a69"></a>

```c
#define NXP_FREQME_REF_REG 0x180
```

相关声明：[NXP_FREQME_REF_REG](#a506f2a1287403d8ec791c4ba0dea8a69)。

FREQMEAS 参考源多路复用寄存器偏移（Reference Mux Register Offset），用于 MCXA／MCXC／MCXN／MCXL／MCXW。

<a id="r_ae6715216ab04ee3b2aba165a3cfbab2c"></a>

```c
#define NXP_FREQME_TAR_REG 0x184
```

相关声明：[NXP_FREQME_TAR_REG](#ae6715216ab04ee3b2aba165a3cfbab2c)。

FREQMEAS 目标源多路复用寄存器偏移（Target Mux Register Offset），用于 MCXA／MCXC／MCXN／MCXL／MCXW。

<a id="r_a036fd1a95200e61ddf132e6739c65144"></a>

```c
#define NXP_FREQME_REF(sel)
```

相关声明：[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

根据选择器 sel 构造 MCX 参考路由连接编码（Reference-route Cookie）。

<a id="r_a512bbc622eb2505deabc25b4c62f749f"></a>

```c
#define NXP_FREQME_TAR(sel)
```

相关声明：[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

根据选择器 sel 构造 MCX 目标路由连接编码（Target-route Cookie）。

<a id="r_ad2d979c3c19f79d23e20ad477d17eed9"></a>

```c
#define NXP_FREQME_REF_CLK_IN NXP_FREQME_REF(1)
```

相关声明：[NXP_FREQME_REF_CLK_IN](#ad2d979c3c19f79d23e20ad477d17eed9)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXA/MCXC 参考源（Reference）：CLK_IN 输入时钟。

<a id="r_a9491056c937aa34d68549c2b6e2c37b1"></a>

```c
#define NXP_FREQME_REF_FRO_12M NXP_FREQME_REF(2)
```

相关声明：[NXP_FREQME_REF_FRO_12M](#a9491056c937aa34d68549c2b6e2c37b1)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXA/MCXC 参考源（Reference）：12 MHz 自由运行振荡器（FRO）。

<a id="r_a4c849f6750d444e68600944fa81ad7ca"></a>

```c
#define NXP_FREQME_REF_FRO_HF_DIV NXP_FREQME_REF(3)
```

相关声明：[NXP_FREQME_REF_FRO_HF_DIV](#a4c849f6750d444e68600944fa81ad7ca)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXA/MCXC 参考源（Reference）：高频自由运行振荡器（FRO_HF）分频输出。

<a id="r_a837a32a82e9e160f05d49a4d5b53d269"></a>

```c
#define NXP_FREQME_REF_CLK_16K1 NXP_FREQME_REF(5)
```

相关声明：[NXP_FREQME_REF_CLK_16K1](#a837a32a82e9e160f05d49a4d5b53d269)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXA/MCXC 参考源（Reference）：16 kHz CLK_16K1 时钟。

<a id="r_a45a8b1d87a1d4bbb2df63f19cb44554d"></a>

```c
#define NXP_FREQME_REF_SLOW_CLK NXP_FREQME_REF(6)
```

相关声明：[NXP_FREQME_REF_SLOW_CLK](#a45a8b1d87a1d4bbb2df63f19cb44554d)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXA/MCXC 参考源（Reference）：慢速时钟（Slow Clock）。

<a id="r_a3e37ce6bb63f4b7019482aa1c88a2843"></a>

```c
#define NXP_FREQME_REF_CLK_IN0 NXP_FREQME_REF(7)
```

相关声明：[NXP_FREQME_REF_CLK_IN0](#a3e37ce6bb63f4b7019482aa1c88a2843)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXA/MCXC 参考源（Reference）：CLK_IN0 输入时钟。

<a id="r_ae8a751821c35b8fbfc9ff30ab247654f"></a>

```c
#define NXP_FREQME_REF_CLK_IN1 NXP_FREQME_REF(8)
```

相关声明：[NXP_FREQME_REF_CLK_IN1](#ae8a751821c35b8fbfc9ff30ab247654f)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXA/MCXC 参考源（Reference）：CLK_IN1 输入时钟。

<a id="r_ad008ec6af0986efda4384382c745c181"></a>

```c
#define NXP_FREQME_TAR_CLK_IN NXP_FREQME_TAR(1)
```

相关声明：[NXP_FREQME_TAR_CLK_IN](#ad008ec6af0986efda4384382c745c181)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXA/MCXC 目标源（Target）：CLK_IN 输入时钟。

<a id="r_ab78b3f57937902dd1877778d4ef8ea28"></a>

```c
#define NXP_FREQME_TAR_FRO_12M NXP_FREQME_TAR(2)
```

相关声明：[NXP_FREQME_TAR_FRO_12M](#ab78b3f57937902dd1877778d4ef8ea28)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXA/MCXC 目标源（Target）：12 MHz 自由运行振荡器（FRO）。

<a id="r_af56bc4f769fa2afd01f72e58bd4ad118"></a>

```c
#define NXP_FREQME_TAR_FRO_HF_DIV NXP_FREQME_TAR(3)
```

相关声明：[NXP_FREQME_TAR_FRO_HF_DIV](#af56bc4f769fa2afd01f72e58bd4ad118)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXA/MCXC 目标源（Target）：高频自由运行振荡器（FRO_HF）分频输出。

<a id="r_a103c44716e4b5fb2b9d7db6ebb867c61"></a>

```c
#define NXP_FREQME_TAR_CLK_16K1 NXP_FREQME_TAR(5)
```

相关声明：[NXP_FREQME_TAR_CLK_16K1](#a103c44716e4b5fb2b9d7db6ebb867c61)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXA/MCXC 目标源（Target）：16 kHz CLK_16K1 时钟。

<a id="r_a5b0558305c315d1de5dc04707ac96118"></a>

```c
#define NXP_FREQME_TAR_SLOW_CLK NXP_FREQME_TAR(6)
```

相关声明：[NXP_FREQME_TAR_SLOW_CLK](#a5b0558305c315d1de5dc04707ac96118)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXA/MCXC 目标源（Target）：慢速时钟（Slow Clock）。

<a id="r_a11c4d36bde30623dd91781e5fb831a6e"></a>

```c
#define NXP_FREQME_TAR_CLK_IN0 NXP_FREQME_TAR(7)
```

相关声明：[NXP_FREQME_TAR_CLK_IN0](#a11c4d36bde30623dd91781e5fb831a6e)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXA/MCXC 目标源（Target）：CLK_IN0 输入时钟。

<a id="r_a06cedc74a9e755a863ae3831393442ae"></a>

```c
#define NXP_FREQME_TAR_CLK_IN1 NXP_FREQME_TAR(8)
```

相关声明：[NXP_FREQME_TAR_CLK_IN1](#a06cedc74a9e755a863ae3831393442ae)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXA/MCXC 目标源（Target）：CLK_IN1 输入时钟。

<a id="r_a75640420cd786d17bc9796d1a60e2159"></a>

```c
#define NXP_FREQME_MCXN_REF_CLK_IN NXP_FREQME_REF(0)
```

相关声明：[NXP_FREQME_MCXN_REF_CLK_IN](#a75640420cd786d17bc9796d1a60e2159)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXN 参考源（Reference）：CLK_IN 输入时钟。

<a id="r_af0a2e211fc5442bbcae60cf85c85d222"></a>

```c
#define NXP_FREQME_MCXN_REF_FRO_12M NXP_FREQME_REF(1)
```

相关声明：[NXP_FREQME_MCXN_REF_FRO_12M](#af0a2e211fc5442bbcae60cf85c85d222)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXN 参考源（Reference）：12 MHz 自由运行振荡器（FRO）。

<a id="r_adaa22c1648aa4c871de6214e44b0be5d"></a>

```c
#define NXP_FREQME_MCXN_REF_FRO_HF NXP_FREQME_REF(2)
```

相关声明：[NXP_FREQME_MCXN_REF_FRO_HF](#adaa22c1648aa4c871de6214e44b0be5d)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXN 参考源（Reference）：高频自由运行振荡器（FRO_HF）。

<a id="r_aafad9c9cce7bf5fa2a225790f5e76814"></a>

```c
#define NXP_FREQME_MCXN_REF_OSC32K NXP_FREQME_REF(4)
```

相关声明：[NXP_FREQME_MCXN_REF_OSC32K](#aafad9c9cce7bf5fa2a225790f5e76814)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXN 参考源（Reference）：32 kHz 振荡器（OSC）。

<a id="r_aa1ab4d527101410e7d62654cfaa46d0f"></a>

```c
#define NXP_FREQME_MCXN_REF_CPU_AHB_CLK NXP_FREQME_REF(5)
```

相关声明：[NXP_FREQME_MCXN_REF_CPU_AHB_CLK](#aa1ab4d527101410e7d62654cfaa46d0f)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXN 参考源（Reference）：CPU／AHB 时钟（Clock）。

<a id="r_a2cd26128d1bdb2c14536d4765d5d3b7b"></a>

```c
#define NXP_FREQME_MCXN_REF_CLK_IN0 NXP_FREQME_REF(6)
```

相关声明：[NXP_FREQME_MCXN_REF_CLK_IN0](#a2cd26128d1bdb2c14536d4765d5d3b7b)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXN 参考源（Reference）：CLK_IN0 输入时钟。

<a id="r_a769e53537cae50931c2c31e4a867466e"></a>

```c
#define NXP_FREQME_MCXN_REF_CLK_IN1 NXP_FREQME_REF(7)
```

相关声明：[NXP_FREQME_MCXN_REF_CLK_IN1](#a769e53537cae50931c2c31e4a867466e)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXN 参考源（Reference）：CLK_IN1 输入时钟。

<a id="r_a35c65822bdf2ebe669dc049070eed6b1"></a>

```c
#define NXP_FREQME_MCXN_TAR_CLK_IN NXP_FREQME_TAR(0)
```

相关声明：[NXP_FREQME_MCXN_TAR_CLK_IN](#a35c65822bdf2ebe669dc049070eed6b1)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXN 目标源（Target）：CLK_IN 输入时钟。

<a id="r_a35512f3a80c5808ecc21f3574de35d5c"></a>

```c
#define NXP_FREQME_MCXN_TAR_FRO_12M NXP_FREQME_TAR(1)
```

相关声明：[NXP_FREQME_MCXN_TAR_FRO_12M](#a35512f3a80c5808ecc21f3574de35d5c)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXN 目标源（Target）：12 MHz 自由运行振荡器（FRO）。

<a id="r_a2f2d649c2081769944ffbf52b45c77a6"></a>

```c
#define NXP_FREQME_MCXN_TAR_FRO_HF NXP_FREQME_TAR(2)
```

相关声明：[NXP_FREQME_MCXN_TAR_FRO_HF](#a2f2d649c2081769944ffbf52b45c77a6)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXN 目标源（Target）：高频自由运行振荡器（FRO_HF）。

<a id="r_a6132cb4f44be3fbf2ce4eca378d166c2"></a>

```c
#define NXP_FREQME_MCXN_TAR_OSC32K NXP_FREQME_TAR(4)
```

相关声明：[NXP_FREQME_MCXN_TAR_OSC32K](#a6132cb4f44be3fbf2ce4eca378d166c2)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXN 目标源（Target）：32 kHz 振荡器（OSC）。

<a id="r_a7f8e8a86cb7e337d978385502a9e1f5c"></a>

```c
#define NXP_FREQME_MCXN_TAR_CPU_AHB_CLK NXP_FREQME_TAR(5)
```

相关声明：[NXP_FREQME_MCXN_TAR_CPU_AHB_CLK](#a7f8e8a86cb7e337d978385502a9e1f5c)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXN 目标源（Target）：CPU／AHB 时钟（Clock）。

<a id="r_a0c620be896a1e3b40f51e83854c0f94a"></a>

```c
#define NXP_FREQME_MCXN_TAR_CLK_IN0 NXP_FREQME_TAR(6)
```

相关声明：[NXP_FREQME_MCXN_TAR_CLK_IN0](#a0c620be896a1e3b40f51e83854c0f94a)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXN 目标源（Target）：CLK_IN0 输入时钟。

<a id="r_a684fce76ef328ac3e160e9c8d33be3f0"></a>

```c
#define NXP_FREQME_MCXN_TAR_CLK_IN1 NXP_FREQME_TAR(7)
```

相关声明：[NXP_FREQME_MCXN_TAR_CLK_IN1](#a684fce76ef328ac3e160e9c8d33be3f0)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXN 目标源（Target）：CLK_IN1 输入时钟。

<a id="r_a84272706c2eb7fe1d0cbb11290eca405"></a>

```c
#define NXP_FREQME_MCXL_REF_FRO_12M NXP_FREQME_REF(2)
```

相关声明：[NXP_FREQME_MCXL_REF_FRO_12M](#a84272706c2eb7fe1d0cbb11290eca405)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXL 参考源（Reference）：12 MHz 自由运行振荡器（FRO）。

<a id="r_aebb2c3bcb6f96a6f80cf8a4e5c9e4368"></a>

```c
#define NXP_FREQME_MCXL_REF_FRO_HF_DIV NXP_FREQME_REF(3)
```

相关声明：[NXP_FREQME_MCXL_REF_FRO_HF_DIV](#aebb2c3bcb6f96a6f80cf8a4e5c9e4368)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXL 参考源（Reference）：高频自由运行振荡器（FRO_HF）分频输出。

<a id="r_abfb9b0d4f23292da0e330c515bda6aaa"></a>

```c
#define NXP_FREQME_MCXL_REF_XTAL32K NXP_FREQME_REF(4)
```

相关声明：[NXP_FREQME_MCXL_REF_XTAL32K](#abfb9b0d4f23292da0e330c515bda6aaa)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXL 参考源（Reference）：32 kHz 晶体（Crystal）。

<a id="r_a54a895dfab544ef1a6b3ae0c837350aa"></a>

```c
#define NXP_FREQME_MCXL_REF_CLK_16K0 NXP_FREQME_REF(5)
```

相关声明：[NXP_FREQME_MCXL_REF_CLK_16K0](#a54a895dfab544ef1a6b3ae0c837350aa)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXL 参考源（Reference）：16 kHz CLK_16K0 时钟。

<a id="r_a268fcecd1463c51a331bba692e4f0f45"></a>

```c
#define NXP_FREQME_MCXL_REF_SLOW_CLK NXP_FREQME_REF(6)
```

相关声明：[NXP_FREQME_MCXL_REF_SLOW_CLK](#a268fcecd1463c51a331bba692e4f0f45)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXL 参考源（Reference）：慢速时钟（Slow Clock）。

<a id="r_ae4723a70d182c244fc7f1d8dd6a7b025"></a>

```c
#define NXP_FREQME_MCXL_REF_CLK_IN0 NXP_FREQME_REF(7)
```

相关声明：[NXP_FREQME_MCXL_REF_CLK_IN0](#ae4723a70d182c244fc7f1d8dd6a7b025)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXL 参考源（Reference）：CLK_IN0 输入时钟。

<a id="r_afccaeb5728060509bef4afc3b0813067"></a>

```c
#define NXP_FREQME_MCXL_REF_CLK_IN1 NXP_FREQME_REF(8)
```

相关声明：[NXP_FREQME_MCXL_REF_CLK_IN1](#afccaeb5728060509bef4afc3b0813067)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXL 参考源（Reference）：CLK_IN1 输入时钟。

<a id="r_a821ea2b47219883aa9661a7a71da0769"></a>

```c
#define NXP_FREQME_MCXL_TAR_FRO_12M NXP_FREQME_TAR(2)
```

相关声明：[NXP_FREQME_MCXL_TAR_FRO_12M](#a821ea2b47219883aa9661a7a71da0769)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXL 目标源（Target）：12 MHz 自由运行振荡器（FRO）。

<a id="r_a277028f91a2386f33a9e8bb9b62c1bdc"></a>

```c
#define NXP_FREQME_MCXL_TAR_FRO_HF_DIV NXP_FREQME_TAR(3)
```

相关声明：[NXP_FREQME_MCXL_TAR_FRO_HF_DIV](#a277028f91a2386f33a9e8bb9b62c1bdc)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXL 目标源（Target）：高频自由运行振荡器（FRO_HF）分频输出。

<a id="r_acb6f427b714256589aadc1d0039bec6c"></a>

```c
#define NXP_FREQME_MCXL_TAR_XTAL32K NXP_FREQME_TAR(4)
```

相关声明：[NXP_FREQME_MCXL_TAR_XTAL32K](#acb6f427b714256589aadc1d0039bec6c)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXL 目标源（Target）：32 kHz 晶体（Crystal）。

<a id="r_a0b22a9b9a09d1d9f9e69bb68fc5d927d"></a>

```c
#define NXP_FREQME_MCXL_TAR_CLK_16K0 NXP_FREQME_TAR(5)
```

相关声明：[NXP_FREQME_MCXL_TAR_CLK_16K0](#a0b22a9b9a09d1d9f9e69bb68fc5d927d)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXL 目标源（Target）：16 kHz CLK_16K0 时钟。

<a id="r_a456d143a1eab50f3b6ae5dd778cd6841"></a>

```c
#define NXP_FREQME_MCXL_TAR_SLOW_CLK NXP_FREQME_TAR(6)
```

相关声明：[NXP_FREQME_MCXL_TAR_SLOW_CLK](#a456d143a1eab50f3b6ae5dd778cd6841)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXL 目标源（Target）：慢速时钟（Slow Clock）。

<a id="r_a78492c27207400aa0df0c52535b4c00a"></a>

```c
#define NXP_FREQME_MCXL_TAR_CLK_IN0 NXP_FREQME_TAR(7)
```

相关声明：[NXP_FREQME_MCXL_TAR_CLK_IN0](#a78492c27207400aa0df0c52535b4c00a)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXL 目标源（Target）：CLK_IN0 输入时钟。

<a id="r_a26405a18dac06f5536da484c14f54b6d"></a>

```c
#define NXP_FREQME_MCXL_TAR_CLK_IN1 NXP_FREQME_TAR(8)
```

相关声明：[NXP_FREQME_MCXL_TAR_CLK_IN1](#a26405a18dac06f5536da484c14f54b6d)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXL 目标源（Target）：CLK_IN1 输入时钟。

<a id="r_a98de19d89863fa12d455b98ddb5b54da"></a>

```c
#define NXP_FREQME_MCXW_REF_EXTERN_OSC NXP_FREQME_REF(0)
```

相关声明：[NXP_FREQME_MCXW_REF_EXTERN_OSC](#a98de19d89863fa12d455b98ddb5b54da)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXW 参考源（Reference）：外部振荡器（External OSC）。

<a id="r_ae9470e6dbfdcf0475e539d765a49249a"></a>

```c
#define NXP_FREQME_MCXW_REF_FRO_12M NXP_FREQME_REF(1)
```

相关声明：[NXP_FREQME_MCXW_REF_FRO_12M](#ae9470e6dbfdcf0475e539d765a49249a)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXW 参考源（Reference）：12 MHz 自由运行振荡器（FRO）。

<a id="r_afe29312ace21aae1ac95188d567c2472"></a>

```c
#define NXP_FREQME_MCXW_REF_FRO_32M NXP_FREQME_REF(2)
```

相关声明：[NXP_FREQME_MCXW_REF_FRO_32M](#afe29312ace21aae1ac95188d567c2472)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXW 参考源（Reference）：32 MHz 自由运行振荡器（FRO）。

<a id="r_a0d038c078009448aa3ac2e35fb4bfb32"></a>

```c
#define NXP_FREQME_MCXW_REF_FRO_1M NXP_FREQME_REF(3)
```

相关声明：[NXP_FREQME_MCXW_REF_FRO_1M](#a0d038c078009448aa3ac2e35fb4bfb32)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXW 参考源（Reference）：1 MHz 自由运行振荡器（FRO）。

<a id="r_a56d89574c476c95fb52a2be307ab54c8"></a>

```c
#define NXP_FREQME_MCXW_REF_OSC32K NXP_FREQME_REF(4)
```

相关声明：[NXP_FREQME_MCXW_REF_OSC32K](#a56d89574c476c95fb52a2be307ab54c8)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXW 参考源（Reference）：32 kHz 振荡器（OSC）。

<a id="r_addb9ad8794a30bdbbfb1d2f716b8f592"></a>

```c
#define NXP_FREQME_MCXW_REF_MAIN_CLK NXP_FREQME_REF(5)
```

相关声明：[NXP_FREQME_MCXW_REF_MAIN_CLK](#addb9ad8794a30bdbbfb1d2f716b8f592)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXW 参考源（Reference）：主时钟（Main Clock）。

<a id="r_aa978118aa05eab021ef889157b1a34d5"></a>

```c
#define NXP_FREQME_MCXW_REF_SPIFI_CLK NXP_FREQME_REF(6)
```

相关声明：[NXP_FREQME_MCXW_REF_SPIFI_CLK](#aa978118aa05eab021ef889157b1a34d5)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXW 参考源（Reference）：SPIFI 时钟（Clock）。

<a id="r_a5b0257bf5de04343784159a4fb5f5eb8"></a>

```c
#define NXP_FREQME_MCXW_REF_PORT0_PIN3 NXP_FREQME_REF(7)
```

相关声明：[NXP_FREQME_MCXW_REF_PORT0_PIN3](#a5b0257bf5de04343784159a4fb5f5eb8)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXW 参考源（Reference）：PORT0 引脚（Pin）3。

<a id="r_aa9931a4eca4812135cfd9143fe4c2b34"></a>

```c
#define NXP_FREQME_MCXW_REF_PORT0_PIN11 NXP_FREQME_REF(8)
```

相关声明：[NXP_FREQME_MCXW_REF_PORT0_PIN11](#aa9931a4eca4812135cfd9143fe4c2b34)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXW 参考源（Reference）：PORT0 引脚（Pin）11。

<a id="r_aa9e6e7be71602d6fb200c8fc5c52fc1a"></a>

```c
#define NXP_FREQME_MCXW_REF_PORT0_PIN12 NXP_FREQME_REF(9)
```

相关声明：[NXP_FREQME_MCXW_REF_PORT0_PIN12](#aa9e6e7be71602d6fb200c8fc5c52fc1a)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXW 参考源（Reference）：PORT0 引脚（Pin）12。

<a id="r_a03a40513511eb6c4dda3c48b0075c692"></a>

```c
#define NXP_FREQME_MCXW_REF_PORT0_PIN14 NXP_FREQME_REF(10)
```

相关声明：[NXP_FREQME_MCXW_REF_PORT0_PIN14](#a03a40513511eb6c4dda3c48b0075c692)、[NXP_FREQME_REF](#a036fd1a95200e61ddf132e6739c65144)。

MCXW 参考源（Reference）：PORT0 引脚（Pin）14。

<a id="r_aa6f9b4e059b1b77f6a48e1c67f96cd93"></a>

```c
#define NXP_FREQME_MCXW_TAR_EXTERN_OSC NXP_FREQME_TAR(0)
```

相关声明：[NXP_FREQME_MCXW_TAR_EXTERN_OSC](#aa6f9b4e059b1b77f6a48e1c67f96cd93)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXW 目标源（Target）：外部振荡器（External OSC）。

<a id="r_a6672aae4fc91466ddafedd604826d365"></a>

```c
#define NXP_FREQME_MCXW_TAR_FRO_12M NXP_FREQME_TAR(1)
```

相关声明：[NXP_FREQME_MCXW_TAR_FRO_12M](#a6672aae4fc91466ddafedd604826d365)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXW 目标源（Target）：12 MHz 自由运行振荡器（FRO）。

<a id="r_ada45ea6013b7d76a16b149be8935967d"></a>

```c
#define NXP_FREQME_MCXW_TAR_FRO_32M NXP_FREQME_TAR(2)
```

相关声明：[NXP_FREQME_MCXW_TAR_FRO_32M](#ada45ea6013b7d76a16b149be8935967d)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXW 目标源（Target）：32 MHz 自由运行振荡器（FRO）。

<a id="r_a0a0f573856bd6fe97dc94586b4548ecf"></a>

```c
#define NXP_FREQME_MCXW_TAR_FRO_1M NXP_FREQME_TAR(3)
```

相关声明：[NXP_FREQME_MCXW_TAR_FRO_1M](#a0a0f573856bd6fe97dc94586b4548ecf)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXW 目标源（Target）：1 MHz 自由运行振荡器（FRO）。

<a id="r_a442efbe3164eb9593cf8c4ff28e95142"></a>

```c
#define NXP_FREQME_MCXW_TAR_OSC32K NXP_FREQME_TAR(4)
```

相关声明：[NXP_FREQME_MCXW_TAR_OSC32K](#a442efbe3164eb9593cf8c4ff28e95142)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXW 目标源（Target）：32 kHz 振荡器（OSC）。

<a id="r_a61c8e0fbefe900bf62287e870d510d33"></a>

```c
#define NXP_FREQME_MCXW_TAR_MAIN_CLK NXP_FREQME_TAR(5)
```

相关声明：[NXP_FREQME_MCXW_TAR_MAIN_CLK](#a61c8e0fbefe900bf62287e870d510d33)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXW 目标源（Target）：主时钟（Main Clock）。

<a id="r_a85ec3a46699d40523d40d6f3af996791"></a>

```c
#define NXP_FREQME_MCXW_TAR_SPIFI_CLK NXP_FREQME_TAR(6)
```

相关声明：[NXP_FREQME_MCXW_TAR_SPIFI_CLK](#a85ec3a46699d40523d40d6f3af996791)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXW 目标源（Target）：SPIFI 时钟（Clock）。

<a id="r_a4ffaacdd343fb51391d6a2bb25505b56"></a>

```c
#define NXP_FREQME_MCXW_TAR_PORT0_PIN3 NXP_FREQME_TAR(7)
```

相关声明：[NXP_FREQME_MCXW_TAR_PORT0_PIN3](#a4ffaacdd343fb51391d6a2bb25505b56)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXW 目标源（Target）：PORT0 引脚（Pin）3。

<a id="r_a77d00b6bfeac34a73f8bfd59de9c866b"></a>

```c
#define NXP_FREQME_MCXW_TAR_PORT0_PIN11 NXP_FREQME_TAR(8)
```

相关声明：[NXP_FREQME_MCXW_TAR_PORT0_PIN11](#a77d00b6bfeac34a73f8bfd59de9c866b)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXW 目标源（Target）：PORT0 引脚（Pin）11。

<a id="r_aa2a09bf6569be434d92ccba44ae42119"></a>

```c
#define NXP_FREQME_MCXW_TAR_PORT0_PIN12 NXP_FREQME_TAR(9)
```

相关声明：[NXP_FREQME_MCXW_TAR_PORT0_PIN12](#aa2a09bf6569be434d92ccba44ae42119)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXW 目标源（Target）：PORT0 引脚（Pin）12。

<a id="r_a8349c007a3e7fed3047d25664b0d0b26"></a>

```c
#define NXP_FREQME_MCXW_TAR_PORT0_PIN14 NXP_FREQME_TAR(10)
```

相关声明：[NXP_FREQME_MCXW_TAR_PORT0_PIN14](#a8349c007a3e7fed3047d25664b0d0b26)、[NXP_FREQME_TAR](#a512bbc622eb2505deabc25b4c62f749f)。

MCXW 目标源（Target）：PORT0 引脚（Pin）14。

<a id="r_aaa75455e6c501daa91160bd3127210ea"></a>

```c
#define NXP_FREQME_RT7XX_REF_REG 0x700
```

相关声明：[NXP_FREQME_RT7XX_REF_REG](#aaa75455e6c501daa91160bd3127210ea)。

FREQMEAS 参考源多路复用寄存器偏移（Reference Mux Register Offset），用于 i.MX RT7xx。

<a id="r_a43310a0f56792a071817dba7cd860929"></a>

```c
#define NXP_FREQME_RT7XX_TAR_REG 0x704
```

相关声明：[NXP_FREQME_RT7XX_TAR_REG](#a43310a0f56792a071817dba7cd860929)。

FREQMEAS 目标源多路复用寄存器偏移（Target Mux Register Offset），用于 i.MX RT7xx。

<a id="r_acbe675d00e95f6f0835c73d6b499a192"></a>

```c
#define NXP_FREQME_RT7XX_REF(sel)
```

相关声明：[NXP_FREQME_RT7XX_REF](#acbe675d00e95f6f0835c73d6b499a192)。

根据选择器 sel 构造 RT7xx 参考路由连接编码（Reference-route Cookie）。

<a id="r_a0d520db079d9a1b2dc3e834f8388d7e6"></a>

```c
#define NXP_FREQME_RT7XX_TAR(sel)
```

相关声明：[NXP_FREQME_RT7XX_TAR](#a0d520db079d9a1b2dc3e834f8388d7e6)。

根据选择器 sel 构造 RT7xx 目标路由连接编码（Target-route Cookie）。

<a id="r_a22ab6d5ffd3dda1c3104825160be22bb"></a>

```c
#define NXP_FREQME_RT7XX_REF_OSC_CLK NXP_FREQME_RT7XX_REF(0)
```

相关声明：[NXP_FREQME_RT7XX_REF_OSC_CLK](#a22ab6d5ffd3dda1c3104825160be22bb)、[NXP_FREQME_RT7XX_REF](#acbe675d00e95f6f0835c73d6b499a192)。

RT7xx 参考源（Reference）：系统振荡器（System OSC）。

<a id="r_a1b3026d4759997aa7d5c1a245e38c3a3"></a>

```c
#define NXP_FREQME_RT7XX_REF_FRO1_DIV8 NXP_FREQME_RT7XX_REF(1)
```

相关声明：[NXP_FREQME_RT7XX_REF_FRO1_DIV8](#a1b3026d4759997aa7d5c1a245e38c3a3)、[NXP_FREQME_RT7XX_REF](#acbe675d00e95f6f0835c73d6b499a192)。

RT7xx 参考源（Reference）：自由运行振荡器 FRO1 的八分频输出（FRO1 / 8）。

<a id="r_a454671e6f8fbd55fb092296eb8fb9927"></a>

```c
#define NXP_FREQME_RT7XX_REF_FRO1 NXP_FREQME_RT7XX_REF(2)
```

相关声明：[NXP_FREQME_RT7XX_REF_FRO1](#a454671e6f8fbd55fb092296eb8fb9927)、[NXP_FREQME_RT7XX_REF](#acbe675d00e95f6f0835c73d6b499a192)。

RT7xx 参考源（Reference）：自由运行振荡器 FRO1。

<a id="r_a6348ca1bfb967b8bd065cd85a5eb9d8b"></a>

```c
#define NXP_FREQME_RT7XX_REF_LPOSC NXP_FREQME_RT7XX_REF(3)
```

相关声明：[NXP_FREQME_RT7XX_REF_LPOSC](#a6348ca1bfb967b8bd065cd85a5eb9d8b)、[NXP_FREQME_RT7XX_REF](#acbe675d00e95f6f0835c73d6b499a192)。

RT7xx 参考源（Reference）：低功耗振荡器（Low-power OSC）。

<a id="r_a02796d3e2f2338133dbab5129f115f7c"></a>

```c
#define NXP_FREQME_RT7XX_REF_OSC32K NXP_FREQME_RT7XX_REF(4)
```

相关声明：[NXP_FREQME_RT7XX_REF_OSC32K](#a02796d3e2f2338133dbab5129f115f7c)、[NXP_FREQME_RT7XX_REF](#acbe675d00e95f6f0835c73d6b499a192)。

RT7xx 参考源（Reference）：32 kHz 振荡器（OSC）。

<a id="r_a549016e092cb1206c4a3561cd22c7af1"></a>

```c
#define NXP_FREQME_RT7XX_REF_FRO0 NXP_FREQME_RT7XX_REF(6)
```

相关声明：[NXP_FREQME_RT7XX_REF_FRO0](#a549016e092cb1206c4a3561cd22c7af1)、[NXP_FREQME_RT7XX_REF](#acbe675d00e95f6f0835c73d6b499a192)。

RT7xx 参考源（Reference）：自由运行振荡器 FRO0。

<a id="r_a923ce22b10a2ec1d88a5bede4ff99326"></a>

```c
#define NXP_FREQME_RT7XX_REF_FRO2 NXP_FREQME_RT7XX_REF(7)
```

相关声明：[NXP_FREQME_RT7XX_REF_FRO2](#a923ce22b10a2ec1d88a5bede4ff99326)、[NXP_FREQME_RT7XX_REF](#acbe675d00e95f6f0835c73d6b499a192)。

RT7xx 参考源（Reference）：自由运行振荡器 FRO2。

<a id="r_a94609d288e673b126cefd6f8e9f51988"></a>

```c
#define NXP_FREQME_RT7XX_REF_GPIO_A_CLK NXP_FREQME_RT7XX_REF(8)
```

相关声明：[NXP_FREQME_RT7XX_REF_GPIO_A_CLK](#a94609d288e673b126cefd6f8e9f51988)、[NXP_FREQME_RT7XX_REF](#acbe675d00e95f6f0835c73d6b499a192)。

RT7xx 参考源（Reference）：GPIO A 时钟（Clock）。

<a id="r_aff1e5efccd8326bab8b0432991888d36"></a>

```c
#define NXP_FREQME_RT7XX_REF_GPIO_B_CLK NXP_FREQME_RT7XX_REF(9)
```

相关声明：[NXP_FREQME_RT7XX_REF_GPIO_B_CLK](#aff1e5efccd8326bab8b0432991888d36)、[NXP_FREQME_RT7XX_REF](#acbe675d00e95f6f0835c73d6b499a192)。

RT7xx 参考源（Reference）：GPIO B 时钟（Clock）。

<a id="r_ac5f0b331c0c49268f3b50b488a0c3291"></a>

```c
#define NXP_FREQME_RT7XX_TAR_OSC_CLK NXP_FREQME_RT7XX_TAR(0)
```

相关声明：[NXP_FREQME_RT7XX_TAR_OSC_CLK](#ac5f0b331c0c49268f3b50b488a0c3291)、[NXP_FREQME_RT7XX_TAR](#a0d520db079d9a1b2dc3e834f8388d7e6)。

RT7xx 目标源（Target）：系统振荡器（System OSC）。

<a id="r_ade0da93dda4f1d6975aee36e67840689"></a>

```c
#define NXP_FREQME_RT7XX_TAR_FRO1_DIV8 NXP_FREQME_RT7XX_TAR(1)
```

相关声明：[NXP_FREQME_RT7XX_TAR_FRO1_DIV8](#ade0da93dda4f1d6975aee36e67840689)、[NXP_FREQME_RT7XX_TAR](#a0d520db079d9a1b2dc3e834f8388d7e6)。

RT7xx 目标源（Target）：自由运行振荡器 FRO1 的八分频输出（FRO1 / 8）。

<a id="r_aa5c095ca84eb85ab1efa6d96304027c3"></a>

```c
#define NXP_FREQME_RT7XX_TAR_FRO1 NXP_FREQME_RT7XX_TAR(2)
```

相关声明：[NXP_FREQME_RT7XX_TAR_FRO1](#aa5c095ca84eb85ab1efa6d96304027c3)、[NXP_FREQME_RT7XX_TAR](#a0d520db079d9a1b2dc3e834f8388d7e6)。

RT7xx 目标源（Target）：自由运行振荡器 FRO1。

<a id="r_aa01abe04d2459a4c9e5d18713225787e"></a>

```c
#define NXP_FREQME_RT7XX_TAR_LPOSC NXP_FREQME_RT7XX_TAR(3)
```

相关声明：[NXP_FREQME_RT7XX_TAR_LPOSC](#aa01abe04d2459a4c9e5d18713225787e)、[NXP_FREQME_RT7XX_TAR](#a0d520db079d9a1b2dc3e834f8388d7e6)。

RT7xx 目标源（Target）：低功耗振荡器（Low-power OSC）。

<a id="r_aa2bcd46eef9e446666d91b942152e6cc"></a>

```c
#define NXP_FREQME_RT7XX_TAR_OSC32K NXP_FREQME_RT7XX_TAR(4)
```

相关声明：[NXP_FREQME_RT7XX_TAR_OSC32K](#aa2bcd46eef9e446666d91b942152e6cc)、[NXP_FREQME_RT7XX_TAR](#a0d520db079d9a1b2dc3e834f8388d7e6)。

RT7xx 目标源（Target）：32 kHz 振荡器（OSC）。

<a id="r_a5c567312e8c547a8963e722ba8eabedd"></a>

```c
#define NXP_FREQME_RT7XX_TAR_FRO0 NXP_FREQME_RT7XX_TAR(6)
```

相关声明：[NXP_FREQME_RT7XX_TAR_FRO0](#a5c567312e8c547a8963e722ba8eabedd)、[NXP_FREQME_RT7XX_TAR](#a0d520db079d9a1b2dc3e834f8388d7e6)。

RT7xx 目标源（Target）：自由运行振荡器 FRO0。

<a id="r_a57b5e5a5bcad8935fae692ba5f13d6b1"></a>

```c
#define NXP_FREQME_RT7XX_TAR_FRO2 NXP_FREQME_RT7XX_TAR(7)
```

相关声明：[NXP_FREQME_RT7XX_TAR_FRO2](#a57b5e5a5bcad8935fae692ba5f13d6b1)、[NXP_FREQME_RT7XX_TAR](#a0d520db079d9a1b2dc3e834f8388d7e6)。

RT7xx 目标源（Target）：自由运行振荡器 FRO2。

<a id="r_aa3c4eb5ab843a4c106bc406a82e69bf8"></a>

```c
#define NXP_FREQME_RT7XX_TAR_GPIO_A_CLK NXP_FREQME_RT7XX_TAR(8)
```

相关声明：[NXP_FREQME_RT7XX_TAR_GPIO_A_CLK](#aa3c4eb5ab843a4c106bc406a82e69bf8)、[NXP_FREQME_RT7XX_TAR](#a0d520db079d9a1b2dc3e834f8388d7e6)。

RT7xx 目标源（Target）：GPIO A 时钟（Clock）。

<a id="r_a5b22b3ec6c3cf86190a975f2137369be"></a>

```c
#define NXP_FREQME_RT7XX_TAR_GPIO_B_CLK NXP_FREQME_RT7XX_TAR(9)
```

相关声明：[NXP_FREQME_RT7XX_TAR_GPIO_B_CLK](#a5b22b3ec6c3cf86190a975f2137369be)、[NXP_FREQME_RT7XX_TAR](#a0d520db079d9a1b2dc3e834f8388d7e6)。

RT7xx 目标源（Target）：GPIO B 时钟（Clock）。

## 10.2\_详细说明（Detailed Documentation）

<a id="a54a895dfab544ef1a6b3ae0c837350aa"></a>

### `NXP_FREQME_MCXL_REF_CLK_16K0`

```c
#define NXP_FREQME_MCXL_REF_CLK_16K0 NXP_FREQME_REF(5)
```

MCXL 参考源（Reference）：16 kHz CLK_16K0 时钟。

<a id="ae4723a70d182c244fc7f1d8dd6a7b025"></a>

### `NXP_FREQME_MCXL_REF_CLK_IN0`

```c
#define NXP_FREQME_MCXL_REF_CLK_IN0 NXP_FREQME_REF(7)
```

MCXL 参考源（Reference）：CLK_IN0 输入时钟。

<a id="afccaeb5728060509bef4afc3b0813067"></a>

### `NXP_FREQME_MCXL_REF_CLK_IN1`

```c
#define NXP_FREQME_MCXL_REF_CLK_IN1 NXP_FREQME_REF(8)
```

MCXL 参考源（Reference）：CLK_IN1 输入时钟。

<a id="a84272706c2eb7fe1d0cbb11290eca405"></a>

### `NXP_FREQME_MCXL_REF_FRO_12M`

```c
#define NXP_FREQME_MCXL_REF_FRO_12M NXP_FREQME_REF(2)
```

MCXL 参考源（Reference）：12 MHz 自由运行振荡器（FRO）。

<a id="aebb2c3bcb6f96a6f80cf8a4e5c9e4368"></a>

### `NXP_FREQME_MCXL_REF_FRO_HF_DIV`

```c
#define NXP_FREQME_MCXL_REF_FRO_HF_DIV NXP_FREQME_REF(3)
```

MCXL 参考源（Reference）：高频自由运行振荡器（FRO_HF）分频输出。

<a id="a268fcecd1463c51a331bba692e4f0f45"></a>

### `NXP_FREQME_MCXL_REF_SLOW_CLK`

```c
#define NXP_FREQME_MCXL_REF_SLOW_CLK NXP_FREQME_REF(6)
```

MCXL 参考源（Reference）：慢速时钟（Slow Clock）。

<a id="abfb9b0d4f23292da0e330c515bda6aaa"></a>

### `NXP_FREQME_MCXL_REF_XTAL32K`

```c
#define NXP_FREQME_MCXL_REF_XTAL32K NXP_FREQME_REF(4)
```

MCXL 参考源（Reference）：32 kHz 晶体（Crystal）。

<a id="a0b22a9b9a09d1d9f9e69bb68fc5d927d"></a>

### `NXP_FREQME_MCXL_TAR_CLK_16K0`

```c
#define NXP_FREQME_MCXL_TAR_CLK_16K0 NXP_FREQME_TAR(5)
```

MCXL 目标源（Target）：16 kHz CLK_16K0 时钟。

<a id="a78492c27207400aa0df0c52535b4c00a"></a>

### `NXP_FREQME_MCXL_TAR_CLK_IN0`

```c
#define NXP_FREQME_MCXL_TAR_CLK_IN0 NXP_FREQME_TAR(7)
```

MCXL 目标源（Target）：CLK_IN0 输入时钟。

<a id="a26405a18dac06f5536da484c14f54b6d"></a>

### `NXP_FREQME_MCXL_TAR_CLK_IN1`

```c
#define NXP_FREQME_MCXL_TAR_CLK_IN1 NXP_FREQME_TAR(8)
```

MCXL 目标源（Target）：CLK_IN1 输入时钟。

<a id="a821ea2b47219883aa9661a7a71da0769"></a>

### `NXP_FREQME_MCXL_TAR_FRO_12M`

```c
#define NXP_FREQME_MCXL_TAR_FRO_12M NXP_FREQME_TAR(2)
```

MCXL 目标源（Target）：12 MHz 自由运行振荡器（FRO）。

<a id="a277028f91a2386f33a9e8bb9b62c1bdc"></a>

### `NXP_FREQME_MCXL_TAR_FRO_HF_DIV`

```c
#define NXP_FREQME_MCXL_TAR_FRO_HF_DIV NXP_FREQME_TAR(3)
```

MCXL 目标源（Target）：高频自由运行振荡器（FRO_HF）分频输出。

<a id="a456d143a1eab50f3b6ae5dd778cd6841"></a>

### `NXP_FREQME_MCXL_TAR_SLOW_CLK`

```c
#define NXP_FREQME_MCXL_TAR_SLOW_CLK NXP_FREQME_TAR(6)
```

MCXL 目标源（Target）：慢速时钟（Slow Clock）。

<a id="acb6f427b714256589aadc1d0039bec6c"></a>

### `NXP_FREQME_MCXL_TAR_XTAL32K`

```c
#define NXP_FREQME_MCXL_TAR_XTAL32K NXP_FREQME_TAR(4)
```

MCXL 目标源（Target）：32 kHz 晶体（Crystal）。

<a id="a75640420cd786d17bc9796d1a60e2159"></a>

### `NXP_FREQME_MCXN_REF_CLK_IN`

```c
#define NXP_FREQME_MCXN_REF_CLK_IN NXP_FREQME_REF(0)
```

MCXN 参考源（Reference）：CLK_IN 输入时钟。

<a id="a2cd26128d1bdb2c14536d4765d5d3b7b"></a>

### `NXP_FREQME_MCXN_REF_CLK_IN0`

```c
#define NXP_FREQME_MCXN_REF_CLK_IN0 NXP_FREQME_REF(6)
```

MCXN 参考源（Reference）：CLK_IN0 输入时钟。

<a id="a769e53537cae50931c2c31e4a867466e"></a>

### `NXP_FREQME_MCXN_REF_CLK_IN1`

```c
#define NXP_FREQME_MCXN_REF_CLK_IN1 NXP_FREQME_REF(7)
```

MCXN 参考源（Reference）：CLK_IN1 输入时钟。

<a id="aa1ab4d527101410e7d62654cfaa46d0f"></a>

### `NXP_FREQME_MCXN_REF_CPU_AHB_CLK`

```c
#define NXP_FREQME_MCXN_REF_CPU_AHB_CLK NXP_FREQME_REF(5)
```

MCXN 参考源（Reference）：CPU／AHB 时钟（Clock）。

<a id="af0a2e211fc5442bbcae60cf85c85d222"></a>

### `NXP_FREQME_MCXN_REF_FRO_12M`

```c
#define NXP_FREQME_MCXN_REF_FRO_12M NXP_FREQME_REF(1)
```

MCXN 参考源（Reference）：12 MHz 自由运行振荡器（FRO）。

<a id="adaa22c1648aa4c871de6214e44b0be5d"></a>

### `NXP_FREQME_MCXN_REF_FRO_HF`

```c
#define NXP_FREQME_MCXN_REF_FRO_HF NXP_FREQME_REF(2)
```

MCXN 参考源（Reference）：高频自由运行振荡器（FRO_HF）。

<a id="aafad9c9cce7bf5fa2a225790f5e76814"></a>

### `NXP_FREQME_MCXN_REF_OSC32K`

```c
#define NXP_FREQME_MCXN_REF_OSC32K NXP_FREQME_REF(4)
```

MCXN 参考源（Reference）：32 kHz 振荡器（OSC）。

<a id="a35c65822bdf2ebe669dc049070eed6b1"></a>

### `NXP_FREQME_MCXN_TAR_CLK_IN`

```c
#define NXP_FREQME_MCXN_TAR_CLK_IN NXP_FREQME_TAR(0)
```

MCXN 目标源（Target）：CLK_IN 输入时钟。

<a id="a0c620be896a1e3b40f51e83854c0f94a"></a>

### `NXP_FREQME_MCXN_TAR_CLK_IN0`

```c
#define NXP_FREQME_MCXN_TAR_CLK_IN0 NXP_FREQME_TAR(6)
```

MCXN 目标源（Target）：CLK_IN0 输入时钟。

<a id="a684fce76ef328ac3e160e9c8d33be3f0"></a>

### `NXP_FREQME_MCXN_TAR_CLK_IN1`

```c
#define NXP_FREQME_MCXN_TAR_CLK_IN1 NXP_FREQME_TAR(7)
```

MCXN 目标源（Target）：CLK_IN1 输入时钟。

<a id="a7f8e8a86cb7e337d978385502a9e1f5c"></a>

### `NXP_FREQME_MCXN_TAR_CPU_AHB_CLK`

```c
#define NXP_FREQME_MCXN_TAR_CPU_AHB_CLK NXP_FREQME_TAR(5)
```

MCXN 目标源（Target）：CPU／AHB 时钟（Clock）。

<a id="a35512f3a80c5808ecc21f3574de35d5c"></a>

### `NXP_FREQME_MCXN_TAR_FRO_12M`

```c
#define NXP_FREQME_MCXN_TAR_FRO_12M NXP_FREQME_TAR(1)
```

MCXN 目标源（Target）：12 MHz 自由运行振荡器（FRO）。

<a id="a2f2d649c2081769944ffbf52b45c77a6"></a>

### `NXP_FREQME_MCXN_TAR_FRO_HF`

```c
#define NXP_FREQME_MCXN_TAR_FRO_HF NXP_FREQME_TAR(2)
```

MCXN 目标源（Target）：高频自由运行振荡器（FRO_HF）。

<a id="a6132cb4f44be3fbf2ce4eca378d166c2"></a>

### `NXP_FREQME_MCXN_TAR_OSC32K`

```c
#define NXP_FREQME_MCXN_TAR_OSC32K NXP_FREQME_TAR(4)
```

MCXN 目标源（Target）：32 kHz 振荡器（OSC）。

<a id="a98de19d89863fa12d455b98ddb5b54da"></a>

### `NXP_FREQME_MCXW_REF_EXTERN_OSC`

```c
#define NXP_FREQME_MCXW_REF_EXTERN_OSC NXP_FREQME_REF(0)
```

MCXW 参考源（Reference）：外部振荡器（External OSC）。

<a id="ae9470e6dbfdcf0475e539d765a49249a"></a>

### `NXP_FREQME_MCXW_REF_FRO_12M`

```c
#define NXP_FREQME_MCXW_REF_FRO_12M NXP_FREQME_REF(1)
```

MCXW 参考源（Reference）：12 MHz 自由运行振荡器（FRO）。

<a id="a0d038c078009448aa3ac2e35fb4bfb32"></a>

### `NXP_FREQME_MCXW_REF_FRO_1M`

```c
#define NXP_FREQME_MCXW_REF_FRO_1M NXP_FREQME_REF(3)
```

MCXW 参考源（Reference）：1 MHz 自由运行振荡器（FRO）。

<a id="afe29312ace21aae1ac95188d567c2472"></a>

### `NXP_FREQME_MCXW_REF_FRO_32M`

```c
#define NXP_FREQME_MCXW_REF_FRO_32M NXP_FREQME_REF(2)
```

MCXW 参考源（Reference）：32 MHz 自由运行振荡器（FRO）。

<a id="addb9ad8794a30bdbbfb1d2f716b8f592"></a>

### `NXP_FREQME_MCXW_REF_MAIN_CLK`

```c
#define NXP_FREQME_MCXW_REF_MAIN_CLK NXP_FREQME_REF(5)
```

MCXW 参考源（Reference）：主时钟（Main Clock）。

<a id="a56d89574c476c95fb52a2be307ab54c8"></a>

### `NXP_FREQME_MCXW_REF_OSC32K`

```c
#define NXP_FREQME_MCXW_REF_OSC32K NXP_FREQME_REF(4)
```

MCXW 参考源（Reference）：32 kHz 振荡器（OSC）。

<a id="aa9931a4eca4812135cfd9143fe4c2b34"></a>

### `NXP_FREQME_MCXW_REF_PORT0_PIN11`

```c
#define NXP_FREQME_MCXW_REF_PORT0_PIN11 NXP_FREQME_REF(8)
```

MCXW 参考源（Reference）：PORT0 引脚（Pin）11。

<a id="aa9e6e7be71602d6fb200c8fc5c52fc1a"></a>

### `NXP_FREQME_MCXW_REF_PORT0_PIN12`

```c
#define NXP_FREQME_MCXW_REF_PORT0_PIN12 NXP_FREQME_REF(9)
```

MCXW 参考源（Reference）：PORT0 引脚（Pin）12。

<a id="a03a40513511eb6c4dda3c48b0075c692"></a>

### `NXP_FREQME_MCXW_REF_PORT0_PIN14`

```c
#define NXP_FREQME_MCXW_REF_PORT0_PIN14 NXP_FREQME_REF(10)
```

MCXW 参考源（Reference）：PORT0 引脚（Pin）14。

<a id="a5b0257bf5de04343784159a4fb5f5eb8"></a>

### `NXP_FREQME_MCXW_REF_PORT0_PIN3`

```c
#define NXP_FREQME_MCXW_REF_PORT0_PIN3 NXP_FREQME_REF(7)
```

MCXW 参考源（Reference）：PORT0 引脚（Pin）3。

<a id="aa978118aa05eab021ef889157b1a34d5"></a>

### `NXP_FREQME_MCXW_REF_SPIFI_CLK`

```c
#define NXP_FREQME_MCXW_REF_SPIFI_CLK NXP_FREQME_REF(6)
```

MCXW 参考源（Reference）：SPIFI 时钟（Clock）。

<a id="aa6f9b4e059b1b77f6a48e1c67f96cd93"></a>

### `NXP_FREQME_MCXW_TAR_EXTERN_OSC`

```c
#define NXP_FREQME_MCXW_TAR_EXTERN_OSC NXP_FREQME_TAR(0)
```

MCXW 目标源（Target）：外部振荡器（External OSC）。

<a id="a6672aae4fc91466ddafedd604826d365"></a>

### `NXP_FREQME_MCXW_TAR_FRO_12M`

```c
#define NXP_FREQME_MCXW_TAR_FRO_12M NXP_FREQME_TAR(1)
```

MCXW 目标源（Target）：12 MHz 自由运行振荡器（FRO）。

<a id="a0a0f573856bd6fe97dc94586b4548ecf"></a>

### `NXP_FREQME_MCXW_TAR_FRO_1M`

```c
#define NXP_FREQME_MCXW_TAR_FRO_1M NXP_FREQME_TAR(3)
```

MCXW 目标源（Target）：1 MHz 自由运行振荡器（FRO）。

<a id="ada45ea6013b7d76a16b149be8935967d"></a>

### `NXP_FREQME_MCXW_TAR_FRO_32M`

```c
#define NXP_FREQME_MCXW_TAR_FRO_32M NXP_FREQME_TAR(2)
```

MCXW 目标源（Target）：32 MHz 自由运行振荡器（FRO）。

<a id="a61c8e0fbefe900bf62287e870d510d33"></a>

### `NXP_FREQME_MCXW_TAR_MAIN_CLK`

```c
#define NXP_FREQME_MCXW_TAR_MAIN_CLK NXP_FREQME_TAR(5)
```

MCXW 目标源（Target）：主时钟（Main Clock）。

<a id="a442efbe3164eb9593cf8c4ff28e95142"></a>

### `NXP_FREQME_MCXW_TAR_OSC32K`

```c
#define NXP_FREQME_MCXW_TAR_OSC32K NXP_FREQME_TAR(4)
```

MCXW 目标源（Target）：32 kHz 振荡器（OSC）。

<a id="a77d00b6bfeac34a73f8bfd59de9c866b"></a>

### `NXP_FREQME_MCXW_TAR_PORT0_PIN11`

```c
#define NXP_FREQME_MCXW_TAR_PORT0_PIN11 NXP_FREQME_TAR(8)
```

MCXW 目标源（Target）：PORT0 引脚（Pin）11。

<a id="aa2a09bf6569be434d92ccba44ae42119"></a>

### `NXP_FREQME_MCXW_TAR_PORT0_PIN12`

```c
#define NXP_FREQME_MCXW_TAR_PORT0_PIN12 NXP_FREQME_TAR(9)
```

MCXW 目标源（Target）：PORT0 引脚（Pin）12。

<a id="a8349c007a3e7fed3047d25664b0d0b26"></a>

### `NXP_FREQME_MCXW_TAR_PORT0_PIN14`

```c
#define NXP_FREQME_MCXW_TAR_PORT0_PIN14 NXP_FREQME_TAR(10)
```

MCXW 目标源（Target）：PORT0 引脚（Pin）14。

<a id="a4ffaacdd343fb51391d6a2bb25505b56"></a>

### `NXP_FREQME_MCXW_TAR_PORT0_PIN3`

```c
#define NXP_FREQME_MCXW_TAR_PORT0_PIN3 NXP_FREQME_TAR(7)
```

MCXW 目标源（Target）：PORT0 引脚（Pin）3。

<a id="a85ec3a46699d40523d40d6f3af996791"></a>

### `NXP_FREQME_MCXW_TAR_SPIFI_CLK`

```c
#define NXP_FREQME_MCXW_TAR_SPIFI_CLK NXP_FREQME_TAR(6)
```

MCXW 目标源（Target）：SPIFI 时钟（Clock）。

<a id="afce68af2dc4640ce340ae319e67ccd23"></a>

### `NXP_FREQME_PMUX_SHIFT`

```c
#define NXP_FREQME_PMUX_SHIFT 20
```

连接编码（Connection Cookie）中目标多路复用寄存器（Destination Mux Register）的位位置。

<a id="a036fd1a95200e61ddf132e6739c65144"></a>

### `NXP_FREQME_REF`

```c
#define NXP_FREQME_REF ( sel)
```

展开值（Value）：

```c
((sel) + (NXP_FREQME_REF_REG << NXP_FREQME_PMUX_SHIFT))
```

根据选择器 sel 构造 MCX 参考路由连接编码（Reference-route Cookie）。

<a id="a837a32a82e9e160f05d49a4d5b53d269"></a>

### `NXP_FREQME_REF_CLK_16K1`

```c
#define NXP_FREQME_REF_CLK_16K1 NXP_FREQME_REF(5)
```

MCXA/MCXC 参考源（Reference）：16 kHz CLK_16K1 时钟。

<a id="ad2d979c3c19f79d23e20ad477d17eed9"></a>

### `NXP_FREQME_REF_CLK_IN`

```c
#define NXP_FREQME_REF_CLK_IN NXP_FREQME_REF(1)
```

MCXA/MCXC 参考源（Reference）：CLK_IN 输入时钟。

<a id="a3e37ce6bb63f4b7019482aa1c88a2843"></a>

### `NXP_FREQME_REF_CLK_IN0`

```c
#define NXP_FREQME_REF_CLK_IN0 NXP_FREQME_REF(7)
```

MCXA/MCXC 参考源（Reference）：CLK_IN0 输入时钟。

<a id="ae8a751821c35b8fbfc9ff30ab247654f"></a>

### `NXP_FREQME_REF_CLK_IN1`

```c
#define NXP_FREQME_REF_CLK_IN1 NXP_FREQME_REF(8)
```

MCXA/MCXC 参考源（Reference）：CLK_IN1 输入时钟。

<a id="a9491056c937aa34d68549c2b6e2c37b1"></a>

### `NXP_FREQME_REF_FRO_12M`

```c
#define NXP_FREQME_REF_FRO_12M NXP_FREQME_REF(2)
```

MCXA/MCXC 参考源（Reference）：12 MHz 自由运行振荡器（FRO）。

<a id="a4c849f6750d444e68600944fa81ad7ca"></a>

### `NXP_FREQME_REF_FRO_HF_DIV`

```c
#define NXP_FREQME_REF_FRO_HF_DIV NXP_FREQME_REF(3)
```

MCXA/MCXC 参考源（Reference）：高频自由运行振荡器（FRO_HF）分频输出。

<a id="a506f2a1287403d8ec791c4ba0dea8a69"></a>

### `NXP_FREQME_REF_REG`

```c
#define NXP_FREQME_REF_REG 0x180
```

FREQMEAS 参考源多路复用寄存器偏移（Reference Mux Register Offset），用于 MCXA／MCXC／MCXN／MCXL／MCXW。

<a id="a45a8b1d87a1d4bbb2df63f19cb44554d"></a>

### `NXP_FREQME_REF_SLOW_CLK`

```c
#define NXP_FREQME_REF_SLOW_CLK NXP_FREQME_REF(6)
```

MCXA/MCXC 参考源（Reference）：慢速时钟（Slow Clock）。

<a id="acbe675d00e95f6f0835c73d6b499a192"></a>

### `NXP_FREQME_RT7XX_REF`

```c
#define NXP_FREQME_RT7XX_REF ( sel)
```

展开值（Value）：

```c
((sel) + (NXP_FREQME_RT7XX_REF_REG << NXP_FREQME_PMUX_SHIFT))
```

根据选择器 sel 构造 RT7xx 参考路由连接编码（Reference-route Cookie）。

<a id="a549016e092cb1206c4a3561cd22c7af1"></a>

### `NXP_FREQME_RT7XX_REF_FRO0`

```c
#define NXP_FREQME_RT7XX_REF_FRO0 NXP_FREQME_RT7XX_REF(6)
```

RT7xx 参考源（Reference）：自由运行振荡器 FRO0。

<a id="a454671e6f8fbd55fb092296eb8fb9927"></a>

### `NXP_FREQME_RT7XX_REF_FRO1`

```c
#define NXP_FREQME_RT7XX_REF_FRO1 NXP_FREQME_RT7XX_REF(2)
```

RT7xx 参考源（Reference）：自由运行振荡器 FRO1。

<a id="a1b3026d4759997aa7d5c1a245e38c3a3"></a>

### `NXP_FREQME_RT7XX_REF_FRO1_DIV8`

```c
#define NXP_FREQME_RT7XX_REF_FRO1_DIV8 NXP_FREQME_RT7XX_REF(1)
```

RT7xx 参考源（Reference）：自由运行振荡器 FRO1 的八分频输出（FRO1 / 8）。

<a id="a923ce22b10a2ec1d88a5bede4ff99326"></a>

### `NXP_FREQME_RT7XX_REF_FRO2`

```c
#define NXP_FREQME_RT7XX_REF_FRO2 NXP_FREQME_RT7XX_REF(7)
```

RT7xx 参考源（Reference）：自由运行振荡器 FRO2。

<a id="a94609d288e673b126cefd6f8e9f51988"></a>

### `NXP_FREQME_RT7XX_REF_GPIO_A_CLK`

```c
#define NXP_FREQME_RT7XX_REF_GPIO_A_CLK NXP_FREQME_RT7XX_REF(8)
```

RT7xx 参考源（Reference）：GPIO A 时钟（Clock）。

<a id="aff1e5efccd8326bab8b0432991888d36"></a>

### `NXP_FREQME_RT7XX_REF_GPIO_B_CLK`

```c
#define NXP_FREQME_RT7XX_REF_GPIO_B_CLK NXP_FREQME_RT7XX_REF(9)
```

RT7xx 参考源（Reference）：GPIO B 时钟（Clock）。

<a id="a6348ca1bfb967b8bd065cd85a5eb9d8b"></a>

### `NXP_FREQME_RT7XX_REF_LPOSC`

```c
#define NXP_FREQME_RT7XX_REF_LPOSC NXP_FREQME_RT7XX_REF(3)
```

RT7xx 参考源（Reference）：低功耗振荡器（Low-power OSC）。

<a id="a02796d3e2f2338133dbab5129f115f7c"></a>

### `NXP_FREQME_RT7XX_REF_OSC32K`

```c
#define NXP_FREQME_RT7XX_REF_OSC32K NXP_FREQME_RT7XX_REF(4)
```

RT7xx 参考源（Reference）：32 kHz 振荡器（OSC）。

<a id="a22ab6d5ffd3dda1c3104825160be22bb"></a>

### `NXP_FREQME_RT7XX_REF_OSC_CLK`

```c
#define NXP_FREQME_RT7XX_REF_OSC_CLK NXP_FREQME_RT7XX_REF(0)
```

RT7xx 参考源（Reference）：系统振荡器（System OSC）。

<a id="aaa75455e6c501daa91160bd3127210ea"></a>

### `NXP_FREQME_RT7XX_REF_REG`

```c
#define NXP_FREQME_RT7XX_REF_REG 0x700
```

FREQMEAS 参考源多路复用寄存器偏移（Reference Mux Register Offset），用于 i.MX RT7xx。

<a id="a0d520db079d9a1b2dc3e834f8388d7e6"></a>

### `NXP_FREQME_RT7XX_TAR`

```c
#define NXP_FREQME_RT7XX_TAR ( sel)
```

展开值（Value）：

```c
((sel) + (NXP_FREQME_RT7XX_TAR_REG << NXP_FREQME_PMUX_SHIFT))
```

根据选择器 sel 构造 RT7xx 目标路由连接编码（Target-route Cookie）。

<a id="a5c567312e8c547a8963e722ba8eabedd"></a>

### `NXP_FREQME_RT7XX_TAR_FRO0`

```c
#define NXP_FREQME_RT7XX_TAR_FRO0 NXP_FREQME_RT7XX_TAR(6)
```

RT7xx 目标源（Target）：自由运行振荡器 FRO0。

<a id="aa5c095ca84eb85ab1efa6d96304027c3"></a>

### `NXP_FREQME_RT7XX_TAR_FRO1`

```c
#define NXP_FREQME_RT7XX_TAR_FRO1 NXP_FREQME_RT7XX_TAR(2)
```

RT7xx 目标源（Target）：自由运行振荡器 FRO1。

<a id="ade0da93dda4f1d6975aee36e67840689"></a>

### `NXP_FREQME_RT7XX_TAR_FRO1_DIV8`

```c
#define NXP_FREQME_RT7XX_TAR_FRO1_DIV8 NXP_FREQME_RT7XX_TAR(1)
```

RT7xx 目标源（Target）：自由运行振荡器 FRO1 的八分频输出（FRO1 / 8）。

<a id="a57b5e5a5bcad8935fae692ba5f13d6b1"></a>

### `NXP_FREQME_RT7XX_TAR_FRO2`

```c
#define NXP_FREQME_RT7XX_TAR_FRO2 NXP_FREQME_RT7XX_TAR(7)
```

RT7xx 目标源（Target）：自由运行振荡器 FRO2。

<a id="aa3c4eb5ab843a4c106bc406a82e69bf8"></a>

### `NXP_FREQME_RT7XX_TAR_GPIO_A_CLK`

```c
#define NXP_FREQME_RT7XX_TAR_GPIO_A_CLK NXP_FREQME_RT7XX_TAR(8)
```

RT7xx 目标源（Target）：GPIO A 时钟（Clock）。

<a id="a5b22b3ec6c3cf86190a975f2137369be"></a>

### `NXP_FREQME_RT7XX_TAR_GPIO_B_CLK`

```c
#define NXP_FREQME_RT7XX_TAR_GPIO_B_CLK NXP_FREQME_RT7XX_TAR(9)
```

RT7xx 目标源（Target）：GPIO B 时钟（Clock）。

<a id="aa01abe04d2459a4c9e5d18713225787e"></a>

### `NXP_FREQME_RT7XX_TAR_LPOSC`

```c
#define NXP_FREQME_RT7XX_TAR_LPOSC NXP_FREQME_RT7XX_TAR(3)
```

RT7xx 目标源（Target）：低功耗振荡器（Low-power OSC）。

<a id="aa2bcd46eef9e446666d91b942152e6cc"></a>

### `NXP_FREQME_RT7XX_TAR_OSC32K`

```c
#define NXP_FREQME_RT7XX_TAR_OSC32K NXP_FREQME_RT7XX_TAR(4)
```

RT7xx 目标源（Target）：32 kHz 振荡器（OSC）。

<a id="ac5f0b331c0c49268f3b50b488a0c3291"></a>

### `NXP_FREQME_RT7XX_TAR_OSC_CLK`

```c
#define NXP_FREQME_RT7XX_TAR_OSC_CLK NXP_FREQME_RT7XX_TAR(0)
```

RT7xx 目标源（Target）：系统振荡器（System OSC）。

<a id="a43310a0f56792a071817dba7cd860929"></a>

### `NXP_FREQME_RT7XX_TAR_REG`

```c
#define NXP_FREQME_RT7XX_TAR_REG 0x704
```

FREQMEAS 目标源多路复用寄存器偏移（Target Mux Register Offset），用于 i.MX RT7xx。

<a id="a73311c47e8dce82fb7e534058bcd5f3d"></a>

### `NXP_FREQME_SOURCE_UNCHANGED`

```c
#define NXP_FREQME_SOURCE_UNCHANGED 0U
```

set_source() 的哨兵值（Sentinel）：保持该轴，即参考源或目标源，不变。

实际 INPUTMUX 连接编码（Connection Cookie）始终非零：其高位始终包含目标寄存器字段，MCX 为 0x180／0x184，RT7xx 为 0x700／0x704。因此，NXP FREQME 的 clock_monitor_set_source() 后端可使用 0 表示“不变”（No Change）。公共 clock_monitor API 没有定义通用哨兵值（Generic Sentinel）；此常量为 FREQME 私有。

<a id="a512bbc622eb2505deabc25b4c62f749f"></a>

### `NXP_FREQME_TAR`

```c
#define NXP_FREQME_TAR ( sel)
```

展开值（Value）：

```c
((sel) + (NXP_FREQME_TAR_REG << NXP_FREQME_PMUX_SHIFT))
```

根据选择器 sel 构造 MCX 目标路由连接编码（Target-route Cookie）。

<a id="a103c44716e4b5fb2b9d7db6ebb867c61"></a>

### `NXP_FREQME_TAR_CLK_16K1`

```c
#define NXP_FREQME_TAR_CLK_16K1 NXP_FREQME_TAR(5)
```

MCXA/MCXC 目标源（Target）：16 kHz CLK_16K1 时钟。

<a id="ad008ec6af0986efda4384382c745c181"></a>

### `NXP_FREQME_TAR_CLK_IN`

```c
#define NXP_FREQME_TAR_CLK_IN NXP_FREQME_TAR(1)
```

MCXA/MCXC 目标源（Target）：CLK_IN 输入时钟。

<a id="a11c4d36bde30623dd91781e5fb831a6e"></a>

### `NXP_FREQME_TAR_CLK_IN0`

```c
#define NXP_FREQME_TAR_CLK_IN0 NXP_FREQME_TAR(7)
```

MCXA/MCXC 目标源（Target）：CLK_IN0 输入时钟。

<a id="a06cedc74a9e755a863ae3831393442ae"></a>

### `NXP_FREQME_TAR_CLK_IN1`

```c
#define NXP_FREQME_TAR_CLK_IN1 NXP_FREQME_TAR(8)
```

MCXA/MCXC 目标源（Target）：CLK_IN1 输入时钟。

<a id="ab78b3f57937902dd1877778d4ef8ea28"></a>

### `NXP_FREQME_TAR_FRO_12M`

```c
#define NXP_FREQME_TAR_FRO_12M NXP_FREQME_TAR(2)
```

MCXA/MCXC 目标源（Target）：12 MHz 自由运行振荡器（FRO）。

<a id="af56bc4f769fa2afd01f72e58bd4ad118"></a>

### `NXP_FREQME_TAR_FRO_HF_DIV`

```c
#define NXP_FREQME_TAR_FRO_HF_DIV NXP_FREQME_TAR(3)
```

MCXA/MCXC 目标源（Target）：高频自由运行振荡器（FRO_HF）分频输出。

<a id="ae6715216ab04ee3b2aba165a3cfbab2c"></a>

### `NXP_FREQME_TAR_REG`

```c
#define NXP_FREQME_TAR_REG 0x184
```

FREQMEAS 目标源多路复用寄存器偏移（Target Mux Register Offset），用于 MCXA／MCXC／MCXN／MCXL／MCXW。

<a id="a5b0558305c315d1de5dc04707ac96118"></a>

### `NXP_FREQME_TAR_SLOW_CLK`

```c
#define NXP_FREQME_TAR_SLOW_CLK NXP_FREQME_TAR(6)
```

MCXA/MCXC 目标源（Target）：慢速时钟（Slow Clock）。


## 10.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_architecture_reference/P015_nxp-freqme.h_源码浏览.md)
- [clock_monitor_set_source()](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__monitor__interface.html#ga60d5aefa9429cafce872c8f3be40c100)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="anxp-freqme_8h_html_a506f2a1287403d8ec791c4ba0dea8a69"></a>
<a id="anxp-freqme_8h_html_afce68af2dc4640ce340ae319e67ccd23"></a>
<a id="anxp-freqme_8h_html_aaa75455e6c501daa91160bd3127210ea"></a>
<a id="anxp-freqme_8h_html_a43310a0f56792a071817dba7cd860929"></a>
<a id="anxp-freqme_8h_html_ae6715216ab04ee3b2aba165a3cfbab2c"></a>

---

[上一章](P009_zephyr__dt-bindings__pinctrl__nrf-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__bluetooth__classic__obex.h_文件参考.md)
