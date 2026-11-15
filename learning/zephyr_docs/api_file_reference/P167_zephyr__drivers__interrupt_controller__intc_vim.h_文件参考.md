---
id: learning.zephyr-docs.api-file-reference.page-167
title: zephyr__drivers__interrupt_controller__intc_vim.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__vim_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第167章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_intc\_vim.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intc__vim_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/devicetree.h>
#include <zephyr/dt-bindings/interrupt-controller/ti-vim.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 167.1\_宏定义（Macros）

<a id="r_a6b442dccdb4e254cac43abd28c0a724d"></a>

```c
#define VIM_BASE_ADDR DT_REG_ADDR(DT_INST(0, ti_vim))
```

相关声明：[VIM_BASE_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)、[DT_REG_ADDR](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)、[DT_INST](../dt_identity_reference/P001_设备树节点标识宏.md#gae199b930cb21ff38dab284a696093ead)。

<a id="r_af3def9f38617688929e29eec9651c64b"></a>

```c
#define VIM_MAX_IRQ_PER_GROUP (32)
```

相关声明：[VIM_MAX_IRQ_PER_GROUP](#af3def9f38617688929e29eec9651c64b)。

<a id="r_a2520b3f68146858942723fe295c0dae4"></a>

```c
#define VIM_MAX_GROUP_NUM ((uint32_t)(CONFIG_NUM_IRQS / VIM_MAX_IRQ_PER_GROUP))
```

相关声明：[VIM_MAX_GROUP_NUM](#a2520b3f68146858942723fe295c0dae4)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[VIM_MAX_IRQ_PER_GROUP](#af3def9f38617688929e29eec9651c64b)。

<a id="r_a2bbbdbfa2a3dd00d1bd54d5c804220c1"></a>

```c
#define VIM_GET_IRQ_GROUP_NUM(n)
```

相关声明：[VIM_GET_IRQ_GROUP_NUM](#a2bbbdbfa2a3dd00d1bd54d5c804220c1)。

<a id="r_a765f1dd48172c22f4fb9cb5eb2c0ecfc"></a>

```c
#define VIM_GET_IRQ_BIT_NUM(n)
```

相关声明：[VIM_GET_IRQ_BIT_NUM](#a765f1dd48172c22f4fb9cb5eb2c0ecfc)。

<a id="r_aba7671d7f7dee14d87f7feff8a3451f7"></a>

```c
#define VIM_PRI_INT_MAX (15)
```

相关声明：[VIM_PRI_INT_MAX](#aba7671d7f7dee14d87f7feff8a3451f7)。

<a id="r_a378ef153f705928fff529e02838d50af"></a>

```c
#define VIM_PID (VIM_BASE_ADDR + 0x0000)
```

相关声明：[VIM_PID](#a378ef153f705928fff529e02838d50af)、[VIM_BASE_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)。

<a id="r_adf312872ea552e35a0e9fed4ef69ae11"></a>

```c
#define VIM_INFO (VIM_BASE_ADDR + 0x0004)
```

相关声明：[VIM_INFO](#adf312872ea552e35a0e9fed4ef69ae11)、[VIM_BASE_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)。

<a id="r_ab4ee6967e7149c07a2690978e7a2f97b"></a>

```c
#define VIM_PRIIRQ (VIM_BASE_ADDR + 0x0008)
```

相关声明：[VIM_PRIIRQ](#ab4ee6967e7149c07a2690978e7a2f97b)、[VIM_BASE_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)。

<a id="r_a17ea1cd9d06d003bbc094bffbefb47c4"></a>

```c
#define VIM_PRIFIQ (VIM_BASE_ADDR + 0x000C)
```

相关声明：[VIM_PRIFIQ](#a17ea1cd9d06d003bbc094bffbefb47c4)、[VIM_BASE_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)。

<a id="r_a7bcbdd8241d466014361b13baf43d81b"></a>

```c
#define VIM_IRQGSTS (VIM_BASE_ADDR + 0x0010)
```

相关声明：[VIM_IRQGSTS](#a7bcbdd8241d466014361b13baf43d81b)、[VIM_BASE_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)。

<a id="r_a6c2b44a4cabf058542f9663f48d1bc07"></a>

```c
#define VIM_FIQGSTS (VIM_BASE_ADDR + 0x0014)
```

相关声明：[VIM_FIQGSTS](#a6c2b44a4cabf058542f9663f48d1bc07)、[VIM_BASE_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)。

<a id="r_a893a5e8467a3e5417272dedc098e42b5"></a>

```c
#define VIM_IRQVEC (VIM_BASE_ADDR + 0x0018)
```

相关声明：[VIM_IRQVEC](#a893a5e8467a3e5417272dedc098e42b5)、[VIM_BASE_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)。

<a id="r_aba9caef8adb052c353f54679b95f4001"></a>

```c
#define VIM_FIQVEC (VIM_BASE_ADDR + 0x001C)
```

相关声明：[VIM_FIQVEC](#aba9caef8adb052c353f54679b95f4001)、[VIM_BASE_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)。

<a id="r_a814d881a2f50b7b47ab25084f59587f5"></a>

```c
#define VIM_ACTIRQ (VIM_BASE_ADDR + 0x0020)
```

相关声明：[VIM_ACTIRQ](#a814d881a2f50b7b47ab25084f59587f5)、[VIM_BASE_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)。

<a id="r_a48bda38b33fc5dfc695dfdbe627f4984"></a>

```c
#define VIM_ACTFIQ (VIM_BASE_ADDR + 0x0024)
```

相关声明：[VIM_ACTFIQ](#a48bda38b33fc5dfc695dfdbe627f4984)、[VIM_BASE_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)。

<a id="r_ac77876e0bfdd3a9382e28728d9e2ebd3"></a>

```c
#define VIM_DEDVEC (VIM_BASE_ADDR + 0x0030)
```

相关声明：[VIM_DEDVEC](#ac77876e0bfdd3a9382e28728d9e2ebd3)、[VIM_BASE_ADDR](#a6b442dccdb4e254cac43abd28c0a724d)。

<a id="r_a0b86c01e8e3844c71a74380c2392a847"></a>

```c
#define VIM_RAW(n)
```

相关声明：[VIM_RAW](#a0b86c01e8e3844c71a74380c2392a847)。

<a id="r_ae714f8162f5840ab2eb655d48c92ac99"></a>

```c
#define VIM_STS(n)
```

相关声明：[VIM_STS](#ae714f8162f5840ab2eb655d48c92ac99)。

<a id="r_a0d2b404f0483d09a32b6a4914cd660ef"></a>

```c
#define VIM_INTR_EN_SET(n)
```

相关声明：[VIM_INTR_EN_SET](#a0d2b404f0483d09a32b6a4914cd660ef)。

<a id="r_a313eefa1e7b90c3988c8d15c1dfb2aae"></a>

```c
#define VIM_INTR_EN_CLR(n)
```

相关声明：[VIM_INTR_EN_CLR](#a313eefa1e7b90c3988c8d15c1dfb2aae)。

<a id="r_a6a07b16389503e1131e9b46e84545c4e"></a>

```c
#define VIM_IRQSTS(n)
```

相关声明：[VIM_IRQSTS](#a6a07b16389503e1131e9b46e84545c4e)。

<a id="r_ac20f6ab045eb4c7193c94252d4ee26a5"></a>

```c
#define VIM_FIQSTS(n)
```

相关声明：[VIM_FIQSTS](#ac20f6ab045eb4c7193c94252d4ee26a5)。

<a id="r_adbf1801e1f7dfa45f19f20e91ccbf1e2"></a>

```c
#define VIM_INTMAP(n)
```

相关声明：[VIM_INTMAP](#adbf1801e1f7dfa45f19f20e91ccbf1e2)。

<a id="r_a28965b8d5ed95f9bd0322e95d41aa65c"></a>

```c
#define VIM_INTTYPE(n)
```

相关声明：[VIM_INTTYPE](#a28965b8d5ed95f9bd0322e95d41aa65c)。

<a id="r_ad7c36f8650ff847544a550a31235193b"></a>

```c
#define VIM_PRI_INT(n)
```

相关声明：[VIM_PRI_INT](#ad7c36f8650ff847544a550a31235193b)。

<a id="r_abb38d6437a3f25c193c2506fe97cf89c"></a>

```c
#define VIM_VEC_INT(n)
```

相关声明：[VIM_VEC_INT](#abb38d6437a3f25c193c2506fe97cf89c)。

<a id="r_acd62766b3379b5baf178a33b6ff3d905"></a>

```c
#define VIM_GRP_RAW_STS_MASK (BIT64_MASK(32))
```

相关声明：[VIM_GRP_RAW_STS_MASK](#acd62766b3379b5baf178a33b6ff3d905)、[BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)。

<a id="r_a7f4d55def9ac847ff1c2f6739f09a636"></a>

```c
#define VIM_GRP_STS_MSK_MASK (BIT64_MASK(32))
```

相关声明：[VIM_GRP_STS_MSK_MASK](#a7f4d55def9ac847ff1c2f6739f09a636)、[BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)。

<a id="r_a339c2737a2eb9180b78305a058b6aa90"></a>

```c
#define VIM_GRP_INTR_EN_SET_MSK_MASK (BIT64_MASK(32))
```

相关声明：[VIM_GRP_INTR_EN_SET_MSK_MASK](#a339c2737a2eb9180b78305a058b6aa90)、[BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)。

<a id="r_a5b0397e530cdcc0ae4f88796a9ef86ef"></a>

```c
#define VIM_GRP_INTR_EN_CLR_MSK_MASK (BIT64_MASK(32))
```

相关声明：[VIM_GRP_INTR_EN_CLR_MSK_MASK](#a5b0397e530cdcc0ae4f88796a9ef86ef)、[BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)。

<a id="r_a13abe76418c094499d537b7fad5a171c"></a>

```c
#define VIM_GRP_IRQSTS_MSK_MASK (BIT64_MASK(32))
```

相关声明：[VIM_GRP_IRQSTS_MSK_MASK](#a13abe76418c094499d537b7fad5a171c)、[BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)。

<a id="r_a374962357620f5b6ea7f3938158f52c9"></a>

```c
#define VIM_GRP_FIQSTS_MSK_MASK (BIT64_MASK(32))
```

相关声明：[VIM_GRP_FIQSTS_MSK_MASK](#a374962357620f5b6ea7f3938158f52c9)、[BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)。

<a id="r_a0259713478ab1f5930d1b303450d9b72"></a>

```c
#define VIM_GRP_INTMAP_MSK_MASK (BIT64_MASK(32))
```

相关声明：[VIM_GRP_INTMAP_MSK_MASK](#a0259713478ab1f5930d1b303450d9b72)、[BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)。

<a id="r_a29cdb963486249ff8d87c1bf4ceeeb74"></a>

```c
#define VIM_GRP_INTTYPE_MSK_MASK (BIT64_MASK(32))
```

相关声明：[VIM_GRP_INTTYPE_MSK_MASK](#a29cdb963486249ff8d87c1bf4ceeeb74)、[BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)。

<a id="r_a996fc01313c3b05b298f32b7691a0ba1"></a>

```c
#define VIM_PRI_INT_VAL_MASK (BIT_MASK(4))
```

相关声明：[VIM_PRI_INT_VAL_MASK](#a996fc01313c3b05b298f32b7691a0ba1)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_a8076a54316cec3fc0de52079bd4cd598"></a>

```c
#define VIM_VEC_INT_VAL_MASK (0xFFFFFFFCU)
```

相关声明：[VIM_VEC_INT_VAL_MASK](#a8076a54316cec3fc0de52079bd4cd598)。

<a id="r_adeba4e94c9d68665820fd13483d24b85"></a>

```c
#define VIM_INFO_INTERRUPTS_MASK (BIT_MASK(11))
```

相关声明：[VIM_INFO_INTERRUPTS_MASK](#adeba4e94c9d68665820fd13483d24b85)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_a4d4d0d285eabeccb6418c442a7b3453b"></a>

```c
#define VIM_PRIIRQ_VALID_MASK (0x80000000U)
```

相关声明：[VIM_PRIIRQ_VALID_MASK](#a4d4d0d285eabeccb6418c442a7b3453b)。

<a id="r_adc2729dd6329da29bac1ac4942003f7d"></a>

```c
#define VIM_PRIIRQ_VALID_VAL_TRUE (0x1U)
```

相关声明：[VIM_PRIIRQ_VALID_VAL_TRUE](#adc2729dd6329da29bac1ac4942003f7d)。

<a id="r_a0966b95628413d1efdf9e572783865bd"></a>

```c
#define VIM_PRIIRQ_VALID_VAL_FALSE (0x0U)
```

相关声明：[VIM_PRIIRQ_VALID_VAL_FALSE](#a0966b95628413d1efdf9e572783865bd)。

<a id="r_ad952cdc46228507194a3b19baf6d71e7"></a>

```c
#define VIM_PRIIRQ_PRI_MASK (0x000F0000U)
```

相关声明：[VIM_PRIIRQ_PRI_MASK](#ad952cdc46228507194a3b19baf6d71e7)。

<a id="r_a236930837a36a72e4b29f81175537543"></a>

```c
#define VIM_PRIIRQ_NUM_MASK (BIT_MASK(10))
```

相关声明：[VIM_PRIIRQ_NUM_MASK](#a236930837a36a72e4b29f81175537543)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_aba90d57af70816d9b58dc8851f6da004"></a>

```c
#define VIM_PRIFIQ_VALID_MASK (0x80000000U)
```

相关声明：[VIM_PRIFIQ_VALID_MASK](#aba90d57af70816d9b58dc8851f6da004)。

<a id="r_ac5ced3000f18ecfc7fc5ea07e3473f78"></a>

```c
#define VIM_PRIFIQ_VALID_VAL_TRUE (0x1U)
```

相关声明：[VIM_PRIFIQ_VALID_VAL_TRUE](#ac5ced3000f18ecfc7fc5ea07e3473f78)。

<a id="r_a6bdf3d9847f3ccad759874bb5b09cfb4"></a>

```c
#define VIM_PRIFIQ_VALID_VAL_FALSE (0x0U)
```

相关声明：[VIM_PRIFIQ_VALID_VAL_FALSE](#a6bdf3d9847f3ccad759874bb5b09cfb4)。

<a id="r_a6de77b9058d6b58314097adebe045a86"></a>

```c
#define VIM_PRIFIQ_PRI_MASK (0x000F0000U)
```

相关声明：[VIM_PRIFIQ_PRI_MASK](#a6de77b9058d6b58314097adebe045a86)。

<a id="r_aad509ed553a5e15f893390481ac739fa"></a>

```c
#define VIM_PRIFIQ_NUM_MASK (BIT_MASK(10))
```

相关声明：[VIM_PRIFIQ_NUM_MASK](#aad509ed553a5e15f893390481ac739fa)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_a4497e08f4d565ace708e50c84f0f51b6"></a>

```c
#define VIM_IRQGSTS_STS_MASK (BIT64_MASK(32))
```

相关声明：[VIM_IRQGSTS_STS_MASK](#a4497e08f4d565ace708e50c84f0f51b6)、[BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)。

<a id="r_a4047a2f3c251c623a7bb4f03e2c80aa9"></a>

```c
#define VIM_FIQGSTS_STS_MASK (BIT64_MASK(32))
```

相关声明：[VIM_FIQGSTS_STS_MASK](#a4047a2f3c251c623a7bb4f03e2c80aa9)、[BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)。

<a id="r_a854706bcbaeb0764d2dac7a325734b20"></a>

```c
#define VIM_IRQVEC_ADDR_MASK (0xFFFFFFFCU)
```

相关声明：[VIM_IRQVEC_ADDR_MASK](#a854706bcbaeb0764d2dac7a325734b20)。

<a id="r_a88ff3e766b092657a21fdf7ae2e93564"></a>

```c
#define VIM_FIQVEC_ADDR_MASK (0xFFFFFFFCU)
```

相关声明：[VIM_FIQVEC_ADDR_MASK](#a88ff3e766b092657a21fdf7ae2e93564)。

<a id="r_a9740e75023b8bf6ddc87f2aabc234a5c"></a>

```c
#define VIM_ACTIRQ_VALID_MASK (0x80000000U)
```

相关声明：[VIM_ACTIRQ_VALID_MASK](#a9740e75023b8bf6ddc87f2aabc234a5c)。

<a id="r_a67149d8156c8c49e50ffd974ff541be8"></a>

```c
#define VIM_ACTIRQ_VALID_VAL_TRUE (0x1U)
```

相关声明：[VIM_ACTIRQ_VALID_VAL_TRUE](#a67149d8156c8c49e50ffd974ff541be8)。

<a id="r_a4755bb481e7b635fb78a1ed1645fd65f"></a>

```c
#define VIM_ACTIRQ_VALID_VAL_FALSE (0x0U)
```

相关声明：[VIM_ACTIRQ_VALID_VAL_FALSE](#a4755bb481e7b635fb78a1ed1645fd65f)。

<a id="r_aa67330dfd1a07514b6aefb175688f6a2"></a>

```c
#define VIM_ACTIRQ_PRI_MASK (0x000F0000U)
```

相关声明：[VIM_ACTIRQ_PRI_MASK](#aa67330dfd1a07514b6aefb175688f6a2)。

<a id="r_af37fe4204363b131433c08e144b706c0"></a>

```c
#define VIM_ACTIRQ_NUM_MASK (BIT_MASK(10))
```

相关声明：[VIM_ACTIRQ_NUM_MASK](#af37fe4204363b131433c08e144b706c0)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_a5f654648e1fceddc473017f5c69ebfde"></a>

```c
#define VIM_ACTFIQ_VALID_MASK (0x80000000U)
```

相关声明：[VIM_ACTFIQ_VALID_MASK](#a5f654648e1fceddc473017f5c69ebfde)。

<a id="r_a89a2a0626470f6d4efe41ea9790d6dfb"></a>

```c
#define VIM_ACTFIQ_VALID_VAL_TRUE (0x1U)
```

相关声明：[VIM_ACTFIQ_VALID_VAL_TRUE](#a89a2a0626470f6d4efe41ea9790d6dfb)。

<a id="r_ad931b8267aa9895fb907f83b9bcab0a8"></a>

```c
#define VIM_ACTFIQ_VALID_VAL_FALSE (0x0U)
```

相关声明：[VIM_ACTFIQ_VALID_VAL_FALSE](#ad931b8267aa9895fb907f83b9bcab0a8)。

<a id="r_a53c9c40d87a7f364b61a6e2f626ec289"></a>

```c
#define VIM_ACTFIQ_PRI_MASK (0x000F0000U)
```

相关声明：[VIM_ACTFIQ_PRI_MASK](#a53c9c40d87a7f364b61a6e2f626ec289)。

<a id="r_a6245859896c6fcaf000ce56a04d30d5f"></a>

```c
#define VIM_ACTFIQ_NUM_MASK (BIT_MASK(10))
```

相关声明：[VIM_ACTFIQ_NUM_MASK](#a6245859896c6fcaf000ce56a04d30d5f)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_a29b50c725ad2f701fb0c324f178579fb"></a>

```c
#define VIM_DEDVEC_ADDR_MASK (0xFFFFFFFCU)
```

相关声明：[VIM_DEDVEC_ADDR_MASK](#a29b50c725ad2f701fb0c324f178579fb)。

## 167.2\_详细说明（Detailed Documentation）

<a id="a48bda38b33fc5dfc695dfdbe627f4984"></a>

### `VIM_ACTFIQ`

```c
#define VIM_ACTFIQ (VIM_BASE_ADDR + 0x0024)
```

<a id="a6245859896c6fcaf000ce56a04d30d5f"></a>

### `VIM_ACTFIQ_NUM_MASK`

```c
#define VIM_ACTFIQ_NUM_MASK (BIT_MASK(10))
```

<a id="a53c9c40d87a7f364b61a6e2f626ec289"></a>

### `VIM_ACTFIQ_PRI_MASK`

```c
#define VIM_ACTFIQ_PRI_MASK (0x000F0000U)
```

<a id="a5f654648e1fceddc473017f5c69ebfde"></a>

### `VIM_ACTFIQ_VALID_MASK`

```c
#define VIM_ACTFIQ_VALID_MASK (0x80000000U)
```

<a id="ad931b8267aa9895fb907f83b9bcab0a8"></a>

### `VIM_ACTFIQ_VALID_VAL_FALSE`

```c
#define VIM_ACTFIQ_VALID_VAL_FALSE (0x0U)
```

<a id="a89a2a0626470f6d4efe41ea9790d6dfb"></a>

### `VIM_ACTFIQ_VALID_VAL_TRUE`

```c
#define VIM_ACTFIQ_VALID_VAL_TRUE (0x1U)
```

<a id="a814d881a2f50b7b47ab25084f59587f5"></a>

### `VIM_ACTIRQ`

```c
#define VIM_ACTIRQ (VIM_BASE_ADDR + 0x0020)
```

<a id="af37fe4204363b131433c08e144b706c0"></a>

### `VIM_ACTIRQ_NUM_MASK`

```c
#define VIM_ACTIRQ_NUM_MASK (BIT_MASK(10))
```

<a id="aa67330dfd1a07514b6aefb175688f6a2"></a>

### `VIM_ACTIRQ_PRI_MASK`

```c
#define VIM_ACTIRQ_PRI_MASK (0x000F0000U)
```

<a id="a9740e75023b8bf6ddc87f2aabc234a5c"></a>

### `VIM_ACTIRQ_VALID_MASK`

```c
#define VIM_ACTIRQ_VALID_MASK (0x80000000U)
```

<a id="a4755bb481e7b635fb78a1ed1645fd65f"></a>

### `VIM_ACTIRQ_VALID_VAL_FALSE`

```c
#define VIM_ACTIRQ_VALID_VAL_FALSE (0x0U)
```

<a id="a67149d8156c8c49e50ffd974ff541be8"></a>

### `VIM_ACTIRQ_VALID_VAL_TRUE`

```c
#define VIM_ACTIRQ_VALID_VAL_TRUE (0x1U)
```

<a id="a6b442dccdb4e254cac43abd28c0a724d"></a>

### `VIM_BASE_ADDR`

```c
#define VIM_BASE_ADDR DT_REG_ADDR(DT_INST(0, ti_vim))
```

<a id="ac77876e0bfdd3a9382e28728d9e2ebd3"></a>

### `VIM_DEDVEC`

```c
#define VIM_DEDVEC (VIM_BASE_ADDR + 0x0030)
```

<a id="a29b50c725ad2f701fb0c324f178579fb"></a>

### `VIM_DEDVEC_ADDR_MASK`

```c
#define VIM_DEDVEC_ADDR_MASK (0xFFFFFFFCU)
```

<a id="a6c2b44a4cabf058542f9663f48d1bc07"></a>

### `VIM_FIQGSTS`

```c
#define VIM_FIQGSTS (VIM_BASE_ADDR + 0x0014)
```

<a id="a4047a2f3c251c623a7bb4f03e2c80aa9"></a>

### `VIM_FIQGSTS_STS_MASK`

```c
#define VIM_FIQGSTS_STS_MASK (BIT64_MASK(32))
```

<a id="ac20f6ab045eb4c7193c94252d4ee26a5"></a>

### `VIM_FIQSTS`

```c
#define VIM_FIQSTS ( n)
```

展开值（Value）：

```c
(VIM_BASE_ADDR + (0x414) + ((n) * 0x20))
```

<a id="aba9caef8adb052c353f54679b95f4001"></a>

### `VIM_FIQVEC`

```c
#define VIM_FIQVEC (VIM_BASE_ADDR + 0x001C)
```

<a id="a88ff3e766b092657a21fdf7ae2e93564"></a>

### `VIM_FIQVEC_ADDR_MASK`

```c
#define VIM_FIQVEC_ADDR_MASK (0xFFFFFFFCU)
```

<a id="a765f1dd48172c22f4fb9cb5eb2c0ecfc"></a>

### `VIM_GET_IRQ_BIT_NUM`

```c
#define VIM_GET_IRQ_BIT_NUM ( n)
```

展开值（Value）：

```c
((uint32_t)((n) % VIM_MAX_IRQ_PER_GROUP))
```

<a id="a2bbbdbfa2a3dd00d1bd54d5c804220c1"></a>

### `VIM_GET_IRQ_GROUP_NUM`

```c
#define VIM_GET_IRQ_GROUP_NUM ( n)
```

展开值（Value）：

```c
((uint32_t)((n) / VIM_MAX_IRQ_PER_GROUP))
```

<a id="a374962357620f5b6ea7f3938158f52c9"></a>

### `VIM_GRP_FIQSTS_MSK_MASK`

```c
#define VIM_GRP_FIQSTS_MSK_MASK (BIT64_MASK(32))
```

<a id="a0259713478ab1f5930d1b303450d9b72"></a>

### `VIM_GRP_INTMAP_MSK_MASK`

```c
#define VIM_GRP_INTMAP_MSK_MASK (BIT64_MASK(32))
```

<a id="a5b0397e530cdcc0ae4f88796a9ef86ef"></a>

### `VIM_GRP_INTR_EN_CLR_MSK_MASK`

```c
#define VIM_GRP_INTR_EN_CLR_MSK_MASK (BIT64_MASK(32))
```

<a id="a339c2737a2eb9180b78305a058b6aa90"></a>

### `VIM_GRP_INTR_EN_SET_MSK_MASK`

```c
#define VIM_GRP_INTR_EN_SET_MSK_MASK (BIT64_MASK(32))
```

<a id="a29cdb963486249ff8d87c1bf4ceeeb74"></a>

### `VIM_GRP_INTTYPE_MSK_MASK`

```c
#define VIM_GRP_INTTYPE_MSK_MASK (BIT64_MASK(32))
```

<a id="a13abe76418c094499d537b7fad5a171c"></a>

### `VIM_GRP_IRQSTS_MSK_MASK`

```c
#define VIM_GRP_IRQSTS_MSK_MASK (BIT64_MASK(32))
```

<a id="acd62766b3379b5baf178a33b6ff3d905"></a>

### `VIM_GRP_RAW_STS_MASK`

```c
#define VIM_GRP_RAW_STS_MASK (BIT64_MASK(32))
```

<a id="a7f4d55def9ac847ff1c2f6739f09a636"></a>

### `VIM_GRP_STS_MSK_MASK`

```c
#define VIM_GRP_STS_MSK_MASK (BIT64_MASK(32))
```

<a id="adf312872ea552e35a0e9fed4ef69ae11"></a>

### `VIM_INFO`

```c
#define VIM_INFO (VIM_BASE_ADDR + 0x0004)
```

<a id="adeba4e94c9d68665820fd13483d24b85"></a>

### `VIM_INFO_INTERRUPTS_MASK`

```c
#define VIM_INFO_INTERRUPTS_MASK (BIT_MASK(11))
```

<a id="adbf1801e1f7dfa45f19f20e91ccbf1e2"></a>

### `VIM_INTMAP`

```c
#define VIM_INTMAP ( n)
```

展开值（Value）：

```c
(VIM_BASE_ADDR + (0x418) + ((n) * 0x20))
```

<a id="a313eefa1e7b90c3988c8d15c1dfb2aae"></a>

### `VIM_INTR_EN_CLR`

```c
#define VIM_INTR_EN_CLR ( n)
```

展开值（Value）：

```c
(VIM_BASE_ADDR + (0x40c) + ((n) * 0x20))
```

<a id="a0d2b404f0483d09a32b6a4914cd660ef"></a>

### `VIM_INTR_EN_SET`

```c
#define VIM_INTR_EN_SET ( n)
```

展开值（Value）：

```c
(VIM_BASE_ADDR + (0x408) + ((n) * 0x20))
```

<a id="a28965b8d5ed95f9bd0322e95d41aa65c"></a>

### `VIM_INTTYPE`

```c
#define VIM_INTTYPE ( n)
```

展开值（Value）：

```c
(VIM_BASE_ADDR + (0x41c) + ((n) * 0x20))
```

<a id="a7bcbdd8241d466014361b13baf43d81b"></a>

### `VIM_IRQGSTS`

```c
#define VIM_IRQGSTS (VIM_BASE_ADDR + 0x0010)
```

<a id="a4497e08f4d565ace708e50c84f0f51b6"></a>

### `VIM_IRQGSTS_STS_MASK`

```c
#define VIM_IRQGSTS_STS_MASK (BIT64_MASK(32))
```

<a id="a6a07b16389503e1131e9b46e84545c4e"></a>

### `VIM_IRQSTS`

```c
#define VIM_IRQSTS ( n)
```

展开值（Value）：

```c
(VIM_BASE_ADDR + (0x410) + ((n) * 0x20))
```

<a id="a893a5e8467a3e5417272dedc098e42b5"></a>

### `VIM_IRQVEC`

```c
#define VIM_IRQVEC (VIM_BASE_ADDR + 0x0018)
```

<a id="a854706bcbaeb0764d2dac7a325734b20"></a>

### `VIM_IRQVEC_ADDR_MASK`

```c
#define VIM_IRQVEC_ADDR_MASK (0xFFFFFFFCU)
```

<a id="a2520b3f68146858942723fe295c0dae4"></a>

### `VIM_MAX_GROUP_NUM`

```c
#define VIM_MAX_GROUP_NUM ((uint32_t)(CONFIG_NUM_IRQS / VIM_MAX_IRQ_PER_GROUP))
```

<a id="af3def9f38617688929e29eec9651c64b"></a>

### `VIM_MAX_IRQ_PER_GROUP`

```c
#define VIM_MAX_IRQ_PER_GROUP (32)
```

<a id="a378ef153f705928fff529e02838d50af"></a>

### `VIM_PID`

```c
#define VIM_PID (VIM_BASE_ADDR + 0x0000)
```

<a id="ad7c36f8650ff847544a550a31235193b"></a>

### `VIM_PRI_INT`

```c
#define VIM_PRI_INT ( n)
```

展开值（Value）：

```c
(VIM_BASE_ADDR + (0x1000) + ((n) * 0x4))
```

<a id="aba7671d7f7dee14d87f7feff8a3451f7"></a>

### `VIM_PRI_INT_MAX`

```c
#define VIM_PRI_INT_MAX (15)
```

<a id="a996fc01313c3b05b298f32b7691a0ba1"></a>

### `VIM_PRI_INT_VAL_MASK`

```c
#define VIM_PRI_INT_VAL_MASK (BIT_MASK(4))
```

<a id="a17ea1cd9d06d003bbc094bffbefb47c4"></a>

### `VIM_PRIFIQ`

```c
#define VIM_PRIFIQ (VIM_BASE_ADDR + 0x000C)
```

<a id="aad509ed553a5e15f893390481ac739fa"></a>

### `VIM_PRIFIQ_NUM_MASK`

```c
#define VIM_PRIFIQ_NUM_MASK (BIT_MASK(10))
```

<a id="a6de77b9058d6b58314097adebe045a86"></a>

### `VIM_PRIFIQ_PRI_MASK`

```c
#define VIM_PRIFIQ_PRI_MASK (0x000F0000U)
```

<a id="aba90d57af70816d9b58dc8851f6da004"></a>

### `VIM_PRIFIQ_VALID_MASK`

```c
#define VIM_PRIFIQ_VALID_MASK (0x80000000U)
```

<a id="a6bdf3d9847f3ccad759874bb5b09cfb4"></a>

### `VIM_PRIFIQ_VALID_VAL_FALSE`

```c
#define VIM_PRIFIQ_VALID_VAL_FALSE (0x0U)
```

<a id="ac5ced3000f18ecfc7fc5ea07e3473f78"></a>

### `VIM_PRIFIQ_VALID_VAL_TRUE`

```c
#define VIM_PRIFIQ_VALID_VAL_TRUE (0x1U)
```

<a id="ab4ee6967e7149c07a2690978e7a2f97b"></a>

### `VIM_PRIIRQ`

```c
#define VIM_PRIIRQ (VIM_BASE_ADDR + 0x0008)
```

<a id="a236930837a36a72e4b29f81175537543"></a>

### `VIM_PRIIRQ_NUM_MASK`

```c
#define VIM_PRIIRQ_NUM_MASK (BIT_MASK(10))
```

<a id="ad952cdc46228507194a3b19baf6d71e7"></a>

### `VIM_PRIIRQ_PRI_MASK`

```c
#define VIM_PRIIRQ_PRI_MASK (0x000F0000U)
```

<a id="a4d4d0d285eabeccb6418c442a7b3453b"></a>

### `VIM_PRIIRQ_VALID_MASK`

```c
#define VIM_PRIIRQ_VALID_MASK (0x80000000U)
```

<a id="a0966b95628413d1efdf9e572783865bd"></a>

### `VIM_PRIIRQ_VALID_VAL_FALSE`

```c
#define VIM_PRIIRQ_VALID_VAL_FALSE (0x0U)
```

<a id="adc2729dd6329da29bac1ac4942003f7d"></a>

### `VIM_PRIIRQ_VALID_VAL_TRUE`

```c
#define VIM_PRIIRQ_VALID_VAL_TRUE (0x1U)
```

<a id="a0b86c01e8e3844c71a74380c2392a847"></a>

### `VIM_RAW`

```c
#define VIM_RAW ( n)
```

展开值（Value）：

```c
(VIM_BASE_ADDR + (0x400) + ((n) * 0x20))
```

<a id="ae714f8162f5840ab2eb655d48c92ac99"></a>

### `VIM_STS`

```c
#define VIM_STS ( n)
```

展开值（Value）：

```c
(VIM_BASE_ADDR + (0x404) + ((n) * 0x20))
```

<a id="abb38d6437a3f25c193c2506fe97cf89c"></a>

### `VIM_VEC_INT`

```c
#define VIM_VEC_INT ( n)
```

展开值（Value）：

```c
(VIM_BASE_ADDR + (0x2000) + ((n) * 0x4))
```

<a id="a8076a54316cec3fc0de52079bd4cd598"></a>

### `VIM_VEC_INT_VAL_MASK`

```c
#define VIM_VEC_INT_VAL_MASK (0xFFFFFFFCU)
```


## 167.3\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/dt-bindings/interrupt-controller/ti-vim.h](../api_source_reference/P865_ti-vim.h_源码浏览.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/intc__vim_8h_source.html)
- [DT_REG_ADDR](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)
- [DT_INST](../dt_identity_reference/P001_设备树节点标识宏.md#gae199b930cb21ff38dab284a696093ead)
- [uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [BIT64_MASK](../util_reference/P001_通用工具公共接口.md#ga1a138896caafcb2429a6483ea7412d12)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aintc__vim_8h_html_a6b442dccdb4e254cac43abd28c0a724d"></a>
<a id="aintc__vim_8h_html_af3def9f38617688929e29eec9651c64b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

---

[上一章](P166_zephyr__drivers__interrupt_controller__intc_rx_icu.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P168_zephyr__dt-bindings__clock__intel_socfpga_clock.h_文件参考.md)
