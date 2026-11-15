---
id: learning.zephyr-docs.api-file-service-reference.page-27
title: zephyr__drivers__pcie__msi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/msi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_drivers\_\_pcie\_\_msi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/msi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCIe消息信号中断（MSI）和MSI-X支持API的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/drivers/pcie/pcie.h>
```

查看此文件的源码。

PCIe消息信号中断（MSI）和MSI-X支持API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 27.1\_数据结构（Data Structures）

<a id="r_msix_5Fvector"></a>

```c
struct msix_vector
```

相关声明：[msix_vector](../platform_security_model_reference/P019_msix_vector_结构体.md)。

<a id="r_msi_5Fvector"></a>

```c
struct msi_vector
```

相关声明：[msi_vector](../platform_security_model_reference/P018_msi_vector_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 27.2\_宏定义（Macros）

<a id="r_ga6363ff201cdaf89434be7f7976218132"></a>

```c
#define PCIE_MSI_MCR 0U
```

相关声明：[PCIE_MSI_MCR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga6363ff201cdaf89434be7f7976218132)。

<a id="r_ga6d4aa888ca0930998d49abfc21dfc4a0"></a>

```c
#define PCIE_MSI_MCR_EN 0x00010000U /* enable MSI */
```

相关声明：[PCIE_MSI_MCR_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga6d4aa888ca0930998d49abfc21dfc4a0)。

<a id="r_ga273df548ce103502c69a2aaf32940270"></a>

```c
#define PCIE_MSI_MCR_MMC 0x000E0000U /* Multi Messages Capable mask */
```

相关声明：[PCIE_MSI_MCR_MMC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga273df548ce103502c69a2aaf32940270)。

<a id="r_gab0b4bed4d96cc135c38e1762922a6dfc"></a>

```c
#define PCIE_MSI_MCR_MMC_SHIFT 17
```

相关声明：[PCIE_MSI_MCR_MMC_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gab0b4bed4d96cc135c38e1762922a6dfc)。

<a id="r_gae34c85b4346402d14ab7ade656f7874f"></a>

```c
#define PCIE_MSI_MCR_MME 0x00700000U /* mask of # of enabled IRQs */
```

相关声明：[PCIE_MSI_MCR_MME](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gae34c85b4346402d14ab7ade656f7874f)。

<a id="r_ga933abb134aec549761f835f84c0caf53"></a>

```c
#define PCIE_MSI_MCR_MME_SHIFT 20
```

相关声明：[PCIE_MSI_MCR_MME_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga933abb134aec549761f835f84c0caf53)。

<a id="r_ga8496d1040f5f0388130f3550f27dbf67"></a>

```c
#define PCIE_MSI_MCR_64 0x00800000U /* 64-bit MSI */
```

相关声明：[PCIE_MSI_MCR_64](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga8496d1040f5f0388130f3550f27dbf67)。

<a id="r_gaf5b03bc395082366b0f4d8a6860753a3"></a>

```c
#define PCIE_MSI_MAP0 1U
```

相关声明：[PCIE_MSI_MAP0](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gaf5b03bc395082366b0f4d8a6860753a3)。

<a id="r_ga7dc1045e58e9e99029d2876adf373f61"></a>

```c
#define PCIE_MSI_MAP1_64 2U
```

相关声明：[PCIE_MSI_MAP1_64](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga7dc1045e58e9e99029d2876adf373f61)。

<a id="r_ga72a3907f5cfba38103db25a8065efe5d"></a>

```c
#define PCIE_MSI_MDR_32 2U
```

相关声明：[PCIE_MSI_MDR_32](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga72a3907f5cfba38103db25a8065efe5d)。

<a id="r_ga599d70864c7a8a8d12c56c302f963c75"></a>

```c
#define PCIE_MSI_MDR_64 3U
```

相关声明：[PCIE_MSI_MDR_64](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga599d70864c7a8a8d12c56c302f963c75)。

<a id="r_ga3f684fa1e9eaf5aad844b7f5c5232adb"></a>

```c
#define PCIE_MSIX_MCR 0U
```

相关声明：[PCIE_MSIX_MCR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga3f684fa1e9eaf5aad844b7f5c5232adb)。

<a id="r_gaf309bab15a0118cbc39b3a52354a8067"></a>

```c
#define PCIE_MSIX_MCR_EN 0x80000000U /* Enable MSI-X */
```

相关声明：[PCIE_MSIX_MCR_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gaf309bab15a0118cbc39b3a52354a8067)。

<a id="r_ga7186a5d811ab5f486c7eddbb0b2ecffe"></a>

```c
#define PCIE_MSIX_MCR_FMASK 0x40000000U /* Function Mask */
```

相关声明：[PCIE_MSIX_MCR_FMASK](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga7186a5d811ab5f486c7eddbb0b2ecffe)。

<a id="r_ga20e8351fd64d8308ff0c94ba02e7c688"></a>

```c
#define PCIE_MSIX_MCR_TSIZE 0x07FF0000U /* Table size mask */
```

相关声明：[PCIE_MSIX_MCR_TSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga20e8351fd64d8308ff0c94ba02e7c688)。

<a id="r_gabb2e51e10229fe1b5953548a96892005"></a>

```c
#define PCIE_MSIX_MCR_TSIZE_SHIFT 16
```

相关声明：[PCIE_MSIX_MCR_TSIZE_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gabb2e51e10229fe1b5953548a96892005)。

<a id="r_ga0a403e859ea16d24267fed463c214e22"></a>

```c
#define PCIE_MSIR_TABLE_ENTRY_SIZE 16
```

相关声明：[PCIE_MSIR_TABLE_ENTRY_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga0a403e859ea16d24267fed463c214e22)。

<a id="r_ga701825e23994bdf4da4a86b8776c3248"></a>

```c
#define PCIE_MSIX_TR 1U
```

相关声明：[PCIE_MSIX_TR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga701825e23994bdf4da4a86b8776c3248)。

<a id="r_ga13e9132823fa2361ab25e53c75aa8896"></a>

```c
#define PCIE_MSIX_TR_BIR 0x00000007U /* Table BIR mask */
```

相关声明：[PCIE_MSIX_TR_BIR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga13e9132823fa2361ab25e53c75aa8896)。

<a id="r_ga44875f9af4865a82438a6a4ec714c6a9"></a>

```c
#define PCIE_MSIX_TR_OFFSET 0xFFFFFFF8U /* Offset mask */
```

相关声明：[PCIE_MSIX_TR_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga44875f9af4865a82438a6a4ec714c6a9)。

<a id="r_ga6e74db681568d7103100036233e3467d"></a>

```c
#define PCIE_MSIX_PBA 2U
```

相关声明：[PCIE_MSIX_PBA](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga6e74db681568d7103100036233e3467d)。

<a id="r_gae259720d8a4af8b2aba0625b41d21d40"></a>

```c
#define PCIE_MSIX_PBA_BIR 0x00000007U /* PBA BIR mask */
```

相关声明：[PCIE_MSIX_PBA_BIR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gae259720d8a4af8b2aba0625b41d21d40)。

<a id="r_ga388b54bd3c60cb46940e1b1defc42dad"></a>

```c
#define PCIE_MSIX_PBA_OFFSET 0xFFFFFFF8U /* Offset mask */
```

相关声明：[PCIE_MSIX_PBA_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga388b54bd3c60cb46940e1b1defc42dad)。

<a id="r_ga33adc70c295b3ba887529fc8f73f6cb4"></a>

```c
#define PCIE_VTBL_MA 0U /* Msg Address offset */
```

相关声明：[PCIE_VTBL_MA](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga33adc70c295b3ba887529fc8f73f6cb4)。

<a id="r_ga5711b93de9c485b321a9dcd01ac53b05"></a>

```c
#define PCIE_VTBL_MUA 4U /* Msg Upper Address offset */
```

相关声明：[PCIE_VTBL_MUA](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga5711b93de9c485b321a9dcd01ac53b05)。

<a id="r_gaf35ee6cb30ff29ae0f6804f3328a1d1d"></a>

```c
#define PCIE_VTBL_MD 8U /* Msg Data offset */
```

相关声明：[PCIE_VTBL_MD](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gaf35ee6cb30ff29ae0f6804f3328a1d1d)。

<a id="r_gae354a23e4f62342cfd4e2572068b51a3"></a>

```c
#define PCIE_VTBL_VCTRL 12U /* Vector control offset */
```

相关声明：[PCIE_VTBL_VCTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gae354a23e4f62342cfd4e2572068b51a3)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 27.3\_类型定义（Typedefs）

<a id="r_ga9ede6a7a472ee62f0975256a1b5f1231"></a>

```c
typedef struct msi_vector msi_vector_t
```

相关声明：[msi_vector](../platform_security_model_reference/P018_msi_vector_结构体.md)、[msi_vector_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga9ede6a7a472ee62f0975256a1b5f1231)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 27.4\_函数（Functions）

<a id="r_ga2cdf2a32cb4c6e4d68290a1e9020f4ee"></a>

```c
uint32_t pcie_msi_map (unsigned int irq, msi_vector_t *vector, uint8_t n_vector)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_msi_map](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga2cdf2a32cb4c6e4d68290a1e9020f4ee)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[msi_vector_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga9ede6a7a472ee62f0975256a1b5f1231)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

计算消息信号中断投递写入（MSI Posted Write）的目标地址（Target Address）。

<a id="r_gae89ee2177016ab1df94c7f453eb5c25d"></a>

```c
uint16_t pcie_msi_mdr (unsigned int irq, msi_vector_t *vector)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[pcie_msi_mdr](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gae89ee2177016ab1df94c7f453eb5c25d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[msi_vector_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga9ede6a7a472ee62f0975256a1b5f1231)。

计算消息信号中断投递写入（MSI Posted Write）的数据（Data）。

<a id="r_ga57226ef41cee2008a2c92098dd52af6b"></a>

```c
bool pcie_msi_enable (pcie_bdf_t bdf, msi_vector_t *vectors, uint8_t n_vector, unsigned int irq)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_msi_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga57226ef41cee2008a2c92098dd52af6b)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[msi_vector_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga9ede6a7a472ee62f0975256a1b5f1231)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

配置给定 PCI 端点（Endpoint），使其生成消息信号中断（Message Signaled Interrupts，MSIs）。

<a id="r_gac16ef7e19d7584aa2fc3a839b1b8fb01"></a>

```c
bool pcie_is_msi (pcie_bdf_t bdf)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_is_msi](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gac16ef7e19d7584aa2fc3a839b1b8fb01)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

检查给定 PCI 端点（Endpoint）是否支持消息信号中断（MSI／MSI-X）。


## 27.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/drivers/pcie/pcie.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/msi_8h_source.html)
- [msix_vector](../platform_security_model_reference/P019_msix_vector_结构体.md)
- [msi_vector](../platform_security_model_reference/P018_msi_vector_结构体.md)
- [PCIE_MSI_MCR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga6363ff201cdaf89434be7f7976218132)
- [PCIE_MSI_MCR_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga6d4aa888ca0930998d49abfc21dfc4a0)
- [PCIE_MSI_MCR_MMC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga273df548ce103502c69a2aaf32940270)
- [PCIE_MSI_MCR_MMC_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gab0b4bed4d96cc135c38e1762922a6dfc)
- [PCIE_MSI_MCR_MME](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gae34c85b4346402d14ab7ade656f7874f)
- [PCIE_MSI_MCR_MME_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga933abb134aec549761f835f84c0caf53)
- [PCIE_MSI_MCR_64](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga8496d1040f5f0388130f3550f27dbf67)
- [PCIE_MSI_MAP0](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gaf5b03bc395082366b0f4d8a6860753a3)
- [PCIE_MSI_MAP1_64](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga7dc1045e58e9e99029d2876adf373f61)
- [PCIE_MSI_MDR_32](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga72a3907f5cfba38103db25a8065efe5d)
- [PCIE_MSI_MDR_64](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga599d70864c7a8a8d12c56c302f963c75)
- [PCIE_MSIX_MCR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga3f684fa1e9eaf5aad844b7f5c5232adb)
- [PCIE_MSIX_MCR_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gaf309bab15a0118cbc39b3a52354a8067)
- [PCIE_MSIX_MCR_FMASK](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga7186a5d811ab5f486c7eddbb0b2ecffe)
- [PCIE_MSIX_MCR_TSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga20e8351fd64d8308ff0c94ba02e7c688)
- [PCIE_MSIX_MCR_TSIZE_SHIFT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gabb2e51e10229fe1b5953548a96892005)
- [PCIE_MSIR_TABLE_ENTRY_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga0a403e859ea16d24267fed463c214e22)
- [PCIE_MSIX_TR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga701825e23994bdf4da4a86b8776c3248)
- [PCIE_MSIX_TR_BIR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga13e9132823fa2361ab25e53c75aa8896)
- [PCIE_MSIX_TR_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga44875f9af4865a82438a6a4ec714c6a9)
- [PCIE_MSIX_PBA](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga6e74db681568d7103100036233e3467d)
- [PCIE_MSIX_PBA_BIR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gae259720d8a4af8b2aba0625b41d21d40)
- [PCIE_MSIX_PBA_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga388b54bd3c60cb46940e1b1defc42dad)
- [PCIE_VTBL_MA](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga33adc70c295b3ba887529fc8f73f6cb4)
- [PCIE_VTBL_MUA](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga5711b93de9c485b321a9dcd01ac53b05)
- [PCIE_VTBL_MD](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gaf35ee6cb30ff29ae0f6804f3328a1d1d)
- [PCIE_VTBL_VCTRL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gae354a23e4f62342cfd4e2572068b51a3)
- [msi_vector_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga9ede6a7a472ee62f0975256a1b5f1231)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pcie_msi_map](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga2cdf2a32cb4c6e4d68290a1e9020f4ee)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [pcie_msi_mdr](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gae89ee2177016ab1df94c7f453eb5c25d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [pcie_msi_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga57226ef41cee2008a2c92098dd52af6b)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)
- [pcie_is_msi](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gac16ef7e19d7584aa2fc3a839b1b8fb01)

<a id="header-details"></a>

---

[上一章](P026_zephyr__mpipe__base__mpipe_queue.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__net__prometheus__counter.h_文件参考.md)
