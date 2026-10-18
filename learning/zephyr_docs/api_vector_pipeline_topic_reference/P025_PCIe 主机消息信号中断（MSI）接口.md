---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-25
title: PCIe 主机消息信号中断（MSI）接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_PCIe 主机消息信号中断（MSI）接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCIe 主机消息信号中断（MSI）接口

<a id="details"></a>

PCIe 主机消息信号中断（MSI）接口

<a id="header-files"></a>
<a id="files"></a>

## 25.1\_文件（Files）

<a id="r_msi_2Eh"></a>

```c
file msi.h
```

相关声明：[msi.h](../api_file_service_reference/P027_zephyr__drivers__pcie__msi.h_文件参考.md)。

PCIe消息信号中断（MSI）和MSI-X支持API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 25.2\_数据结构（Data Structures）

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

## 25.3\_宏定义（Macros）

<a id="r_ga6363ff201cdaf89434be7f7976218132"></a>

```c
#define PCIE_MSI_MCR 0U
```

相关声明：[PCIE_MSI_MCR](#ga6363ff201cdaf89434be7f7976218132)。

<a id="r_ga6d4aa888ca0930998d49abfc21dfc4a0"></a>

```c
#define PCIE_MSI_MCR_EN 0x00010000U /* enable MSI */
```

相关声明：[PCIE_MSI_MCR_EN](#ga6d4aa888ca0930998d49abfc21dfc4a0)。

<a id="r_ga273df548ce103502c69a2aaf32940270"></a>

```c
#define PCIE_MSI_MCR_MMC 0x000E0000U /* Multi Messages Capable mask */
```

相关声明：[PCIE_MSI_MCR_MMC](#ga273df548ce103502c69a2aaf32940270)。

<a id="r_gab0b4bed4d96cc135c38e1762922a6dfc"></a>

```c
#define PCIE_MSI_MCR_MMC_SHIFT 17
```

相关声明：[PCIE_MSI_MCR_MMC_SHIFT](#gab0b4bed4d96cc135c38e1762922a6dfc)。

<a id="r_gae34c85b4346402d14ab7ade656f7874f"></a>

```c
#define PCIE_MSI_MCR_MME 0x00700000U /* mask of # of enabled IRQs */
```

相关声明：[PCIE_MSI_MCR_MME](#gae34c85b4346402d14ab7ade656f7874f)。

<a id="r_ga933abb134aec549761f835f84c0caf53"></a>

```c
#define PCIE_MSI_MCR_MME_SHIFT 20
```

相关声明：[PCIE_MSI_MCR_MME_SHIFT](#ga933abb134aec549761f835f84c0caf53)。

<a id="r_ga8496d1040f5f0388130f3550f27dbf67"></a>

```c
#define PCIE_MSI_MCR_64 0x00800000U /* 64-bit MSI */
```

相关声明：[PCIE_MSI_MCR_64](#ga8496d1040f5f0388130f3550f27dbf67)。

<a id="r_gaf5b03bc395082366b0f4d8a6860753a3"></a>

```c
#define PCIE_MSI_MAP0 1U
```

相关声明：[PCIE_MSI_MAP0](#gaf5b03bc395082366b0f4d8a6860753a3)。

<a id="r_ga7dc1045e58e9e99029d2876adf373f61"></a>

```c
#define PCIE_MSI_MAP1_64 2U
```

相关声明：[PCIE_MSI_MAP1_64](#ga7dc1045e58e9e99029d2876adf373f61)。

<a id="r_ga72a3907f5cfba38103db25a8065efe5d"></a>

```c
#define PCIE_MSI_MDR_32 2U
```

相关声明：[PCIE_MSI_MDR_32](#ga72a3907f5cfba38103db25a8065efe5d)。

<a id="r_ga599d70864c7a8a8d12c56c302f963c75"></a>

```c
#define PCIE_MSI_MDR_64 3U
```

相关声明：[PCIE_MSI_MDR_64](#ga599d70864c7a8a8d12c56c302f963c75)。

<a id="r_ga3f684fa1e9eaf5aad844b7f5c5232adb"></a>

```c
#define PCIE_MSIX_MCR 0U
```

相关声明：[PCIE_MSIX_MCR](#ga3f684fa1e9eaf5aad844b7f5c5232adb)。

<a id="r_gaf309bab15a0118cbc39b3a52354a8067"></a>

```c
#define PCIE_MSIX_MCR_EN 0x80000000U /* Enable MSI-X */
```

相关声明：[PCIE_MSIX_MCR_EN](#gaf309bab15a0118cbc39b3a52354a8067)。

<a id="r_ga7186a5d811ab5f486c7eddbb0b2ecffe"></a>

```c
#define PCIE_MSIX_MCR_FMASK 0x40000000U /* Function Mask */
```

相关声明：[PCIE_MSIX_MCR_FMASK](#ga7186a5d811ab5f486c7eddbb0b2ecffe)。

<a id="r_ga20e8351fd64d8308ff0c94ba02e7c688"></a>

```c
#define PCIE_MSIX_MCR_TSIZE 0x07FF0000U /* Table size mask */
```

相关声明：[PCIE_MSIX_MCR_TSIZE](#ga20e8351fd64d8308ff0c94ba02e7c688)。

<a id="r_gabb2e51e10229fe1b5953548a96892005"></a>

```c
#define PCIE_MSIX_MCR_TSIZE_SHIFT 16
```

相关声明：[PCIE_MSIX_MCR_TSIZE_SHIFT](#gabb2e51e10229fe1b5953548a96892005)。

<a id="r_ga0a403e859ea16d24267fed463c214e22"></a>

```c
#define PCIE_MSIR_TABLE_ENTRY_SIZE 16
```

相关声明：[PCIE_MSIR_TABLE_ENTRY_SIZE](#ga0a403e859ea16d24267fed463c214e22)。

<a id="r_ga701825e23994bdf4da4a86b8776c3248"></a>

```c
#define PCIE_MSIX_TR 1U
```

相关声明：[PCIE_MSIX_TR](#ga701825e23994bdf4da4a86b8776c3248)。

<a id="r_ga13e9132823fa2361ab25e53c75aa8896"></a>

```c
#define PCIE_MSIX_TR_BIR 0x00000007U /* Table BIR mask */
```

相关声明：[PCIE_MSIX_TR_BIR](#ga13e9132823fa2361ab25e53c75aa8896)。

<a id="r_ga44875f9af4865a82438a6a4ec714c6a9"></a>

```c
#define PCIE_MSIX_TR_OFFSET 0xFFFFFFF8U /* Offset mask */
```

相关声明：[PCIE_MSIX_TR_OFFSET](#ga44875f9af4865a82438a6a4ec714c6a9)。

<a id="r_ga6e74db681568d7103100036233e3467d"></a>

```c
#define PCIE_MSIX_PBA 2U
```

相关声明：[PCIE_MSIX_PBA](#ga6e74db681568d7103100036233e3467d)。

<a id="r_gae259720d8a4af8b2aba0625b41d21d40"></a>

```c
#define PCIE_MSIX_PBA_BIR 0x00000007U /* PBA BIR mask */
```

相关声明：[PCIE_MSIX_PBA_BIR](#gae259720d8a4af8b2aba0625b41d21d40)。

<a id="r_ga388b54bd3c60cb46940e1b1defc42dad"></a>

```c
#define PCIE_MSIX_PBA_OFFSET 0xFFFFFFF8U /* Offset mask */
```

相关声明：[PCIE_MSIX_PBA_OFFSET](#ga388b54bd3c60cb46940e1b1defc42dad)。

<a id="r_ga33adc70c295b3ba887529fc8f73f6cb4"></a>

```c
#define PCIE_VTBL_MA 0U /* Msg Address offset */
```

相关声明：[PCIE_VTBL_MA](#ga33adc70c295b3ba887529fc8f73f6cb4)。

<a id="r_ga5711b93de9c485b321a9dcd01ac53b05"></a>

```c
#define PCIE_VTBL_MUA 4U /* Msg Upper Address offset */
```

相关声明：[PCIE_VTBL_MUA](#ga5711b93de9c485b321a9dcd01ac53b05)。

<a id="r_gaf35ee6cb30ff29ae0f6804f3328a1d1d"></a>

```c
#define PCIE_VTBL_MD 8U /* Msg Data offset */
```

相关声明：[PCIE_VTBL_MD](#gaf35ee6cb30ff29ae0f6804f3328a1d1d)。

<a id="r_gae354a23e4f62342cfd4e2572068b51a3"></a>

```c
#define PCIE_VTBL_VCTRL 12U /* Vector control offset */
```

相关声明：[PCIE_VTBL_VCTRL](#gae354a23e4f62342cfd4e2572068b51a3)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 25.4\_类型定义（Typedefs）

<a id="r_ga9ede6a7a472ee62f0975256a1b5f1231"></a>

```c
typedef struct msi_vector msi_vector_t
```

相关声明：[msi_vector](../platform_security_model_reference/P018_msi_vector_结构体.md)、[msi_vector_t](#ga9ede6a7a472ee62f0975256a1b5f1231)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.5\_函数（Functions）

<a id="r_ga2cdf2a32cb4c6e4d68290a1e9020f4ee"></a>

```c
uint32_t pcie_msi_map (unsigned int irq, msi_vector_t *vector, uint8_t n_vector)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_msi_map](#ga2cdf2a32cb4c6e4d68290a1e9020f4ee)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[msi_vector_t](#ga9ede6a7a472ee62f0975256a1b5f1231)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

计算消息信号中断投递写入（MSI Posted Write）的目标地址（Target Address）。

<a id="r_gae89ee2177016ab1df94c7f453eb5c25d"></a>

```c
uint16_t pcie_msi_mdr (unsigned int irq, msi_vector_t *vector)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[pcie_msi_mdr](#gae89ee2177016ab1df94c7f453eb5c25d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[msi_vector_t](#ga9ede6a7a472ee62f0975256a1b5f1231)。

计算消息信号中断投递写入（MSI Posted Write）的数据（Data）。

<a id="r_ga57226ef41cee2008a2c92098dd52af6b"></a>

```c
bool pcie_msi_enable (pcie_bdf_t bdf, msi_vector_t *vectors, uint8_t n_vector, unsigned int irq)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_msi_enable](#ga57226ef41cee2008a2c92098dd52af6b)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[msi_vector_t](#ga9ede6a7a472ee62f0975256a1b5f1231)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

配置给定 PCI 端点（Endpoint），使其生成消息信号中断（Message Signaled Interrupts，MSIs）。

<a id="r_gac16ef7e19d7584aa2fc3a839b1b8fb01"></a>

```c
bool pcie_is_msi (pcie_bdf_t bdf)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_is_msi](#gac16ef7e19d7584aa2fc3a839b1b8fb01)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

检查给定 PCI 端点（Endpoint）是否支持消息信号中断（MSI／MSI-X）。

## 25.6\_详细说明（Detailed Documentation）

<a id="gaf5b03bc395082366b0f4d8a6860753a3"></a>

### `PCIE_MSI_MAP0`

```c
#define PCIE_MSI_MAP0 1U
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga7dc1045e58e9e99029d2876adf373f61"></a>

### `PCIE_MSI_MAP1_64`

```c
#define PCIE_MSI_MAP1_64 2U
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga6363ff201cdaf89434be7f7976218132"></a>

### `PCIE_MSI_MCR`

```c
#define PCIE_MSI_MCR 0U
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga8496d1040f5f0388130f3550f27dbf67"></a>

### `PCIE_MSI_MCR_64`

```c
#define PCIE_MSI_MCR_64 0x00800000U /* 64-bit MSI */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga6d4aa888ca0930998d49abfc21dfc4a0"></a>

### `PCIE_MSI_MCR_EN`

```c
#define PCIE_MSI_MCR_EN 0x00010000U /* enable MSI */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga273df548ce103502c69a2aaf32940270"></a>

### `PCIE_MSI_MCR_MMC`

```c
#define PCIE_MSI_MCR_MMC 0x000E0000U /* Multi Messages Capable mask */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="gab0b4bed4d96cc135c38e1762922a6dfc"></a>

### `PCIE_MSI_MCR_MMC_SHIFT`

```c
#define PCIE_MSI_MCR_MMC_SHIFT 17
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="gae34c85b4346402d14ab7ade656f7874f"></a>

### `PCIE_MSI_MCR_MME`

```c
#define PCIE_MSI_MCR_MME 0x00700000U /* mask of # of enabled IRQs */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga933abb134aec549761f835f84c0caf53"></a>

### `PCIE_MSI_MCR_MME_SHIFT`

```c
#define PCIE_MSI_MCR_MME_SHIFT 20
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga72a3907f5cfba38103db25a8065efe5d"></a>

### `PCIE_MSI_MDR_32`

```c
#define PCIE_MSI_MDR_32 2U
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga599d70864c7a8a8d12c56c302f963c75"></a>

### `PCIE_MSI_MDR_64`

```c
#define PCIE_MSI_MDR_64 3U
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga0a403e859ea16d24267fed463c214e22"></a>

### `PCIE_MSIR_TABLE_ENTRY_SIZE`

```c
#define PCIE_MSIR_TABLE_ENTRY_SIZE 16
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga3f684fa1e9eaf5aad844b7f5c5232adb"></a>

### `PCIE_MSIX_MCR`

```c
#define PCIE_MSIX_MCR 0U
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="gaf309bab15a0118cbc39b3a52354a8067"></a>

### `PCIE_MSIX_MCR_EN`

```c
#define PCIE_MSIX_MCR_EN 0x80000000U /* Enable MSI-X */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga7186a5d811ab5f486c7eddbb0b2ecffe"></a>

### `PCIE_MSIX_MCR_FMASK`

```c
#define PCIE_MSIX_MCR_FMASK 0x40000000U /* Function Mask */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga20e8351fd64d8308ff0c94ba02e7c688"></a>

### `PCIE_MSIX_MCR_TSIZE`

```c
#define PCIE_MSIX_MCR_TSIZE 0x07FF0000U /* Table size mask */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="gabb2e51e10229fe1b5953548a96892005"></a>

### `PCIE_MSIX_MCR_TSIZE_SHIFT`

```c
#define PCIE_MSIX_MCR_TSIZE_SHIFT 16
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga6e74db681568d7103100036233e3467d"></a>

### `PCIE_MSIX_PBA`

```c
#define PCIE_MSIX_PBA 2U
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="gae259720d8a4af8b2aba0625b41d21d40"></a>

### `PCIE_MSIX_PBA_BIR`

```c
#define PCIE_MSIX_PBA_BIR 0x00000007U /* PBA BIR mask */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga388b54bd3c60cb46940e1b1defc42dad"></a>

### `PCIE_MSIX_PBA_OFFSET`

```c
#define PCIE_MSIX_PBA_OFFSET 0xFFFFFFF8U /* Offset mask */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga701825e23994bdf4da4a86b8776c3248"></a>

### `PCIE_MSIX_TR`

```c
#define PCIE_MSIX_TR 1U
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga13e9132823fa2361ab25e53c75aa8896"></a>

### `PCIE_MSIX_TR_BIR`

```c
#define PCIE_MSIX_TR_BIR 0x00000007U /* Table BIR mask */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga44875f9af4865a82438a6a4ec714c6a9"></a>

### `PCIE_MSIX_TR_OFFSET`

```c
#define PCIE_MSIX_TR_OFFSET 0xFFFFFFF8U /* Offset mask */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga33adc70c295b3ba887529fc8f73f6cb4"></a>

### `PCIE_VTBL_MA`

```c
#define PCIE_VTBL_MA 0U /* Msg Address offset */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="gaf35ee6cb30ff29ae0f6804f3328a1d1d"></a>

### `PCIE_VTBL_MD`

```c
#define PCIE_VTBL_MD 8U /* Msg Data offset */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga5711b93de9c485b321a9dcd01ac53b05"></a>

### `PCIE_VTBL_MUA`

```c
#define PCIE_VTBL_MUA 4U /* Msg Upper Address offset */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="gae354a23e4f62342cfd4e2572068b51a3"></a>

### `PCIE_VTBL_VCTRL`

```c
#define PCIE_VTBL_VCTRL 12U /* Vector control offset */
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="ga9ede6a7a472ee62f0975256a1b5f1231"></a>

### `msi_vector_t`

```c
typedef struct msi_vector msi_vector_t
```

```c
#include <zephyr/drivers/pcie/msi.h>
```

<a id="gac16ef7e19d7584aa2fc3a839b1b8fb01"></a>

### `pcie_is_msi()`

```c
bool pcie_is_msi ( pcie_bdf_t bdf)
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/msi.h>
```

检查给定 PCI 端点（Endpoint）是否支持消息信号中断（MSI／MSI-X）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | 目标 PCI 端点（Endpoint）。 |

**返回（Returns）**：**返回值（Returns）：**端点支持消息信号中断（MSI/MSI-X）时返回 `true`。

<a id="ga57226ef41cee2008a2c92098dd52af6b"></a>

### `pcie_msi_enable()`

```c
bool pcie_msi_enable ( pcie_bdf_t bdf, msi_vector_t * vectors, uint8_t n_vector, unsigned int irq )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/msi.h>
```

配置给定 PCI 端点（Endpoint），使其生成消息信号中断（Message Signaled Interrupts，MSIs）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | 目标 PCI 端点（Endpoint）。 |
| `vectors` | 已分配向量（Vector）的数组。 |
| `n_vector` | 向量数组（Vector Array）的大小。 |
| `irq` | 希望通过 MSI 触发的中断请求（IRQ）。 |

**返回（Returns）**：**返回值（Returns）：**端点支持 MSI 时返回 `true`，否则返回 `false`。

<a id="ga2cdf2a32cb4c6e4d68290a1e9020f4ee"></a>

### `pcie_msi_map()`

```c
uint32_t pcie_msi_map ( unsigned int irq, msi_vector_t * vector, uint8_t n_vector )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/msi.h>
```

计算消息信号中断投递写入（MSI Posted Write）的目标地址（Target Address）。

本函数由体系结构（Architecture）、开发板（Board）或片上系统（SoC）代码导出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 希望通过 MSI 触发的中断请求（IRQ）。 |
| `vector` | 要获取其地址的向量（Vector），也可为 `NULL`。 |
| `n_vector` | 向量数组（Vector Array）的大小。 |

**返回（Returns）**：**返回值（Returns）：**MSI MAP 寄存器的 32 位值。

<a id="gae89ee2177016ab1df94c7f453eb5c25d"></a>

### `pcie_msi_mdr()`

```c
uint16_t pcie_msi_mdr ( unsigned int irq, msi_vector_t * vector )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/msi.h>
```

计算消息信号中断投递写入（MSI Posted Write）的数据（Data）。

本函数由体系结构（Architecture）、开发板（Board）或片上系统（SoC）代码导出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 希望通过 MSI 触发的中断请求（IRQ）。 |
| `vector` | 要获取其数据的向量（Vector），也可为 `NULL`。 |

**返回（Returns）**：**返回值（Returns）：**MSI MDR 寄存器的 16 位值。


## 25.7\_原页交叉引用（Cross References）

- [msi.h](../api_file_service_reference/P027_zephyr__drivers__pcie__msi.h_文件参考.md)
- [msix_vector](../platform_security_model_reference/P019_msix_vector_结构体.md)
- [msi_vector](../platform_security_model_reference/P018_msi_vector_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P024_网络核心库（Network Core Library）.md) · [返回大纲](大纲.md) · [下一章](P026_传感器类型——感知子系统（Sensor Types，Sensing）.md)
