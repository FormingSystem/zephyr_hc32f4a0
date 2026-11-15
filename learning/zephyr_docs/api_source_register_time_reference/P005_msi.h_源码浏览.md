---
id: learning.zephyr-docs.api-source-register-time-reference.page-5
title: msi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/msi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_msi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/msi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_service_reference/P027_zephyr__drivers__pcie__msi.h_文件参考.md)。

## 5.1\_原始可见代码（Source Code）

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
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
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
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="adrivers_2pcie_2pcie_8h_html"></a>
<a id="agroup__pcie__host__interface_html_gaf9748042a4f3c8d912d19df1ccf737fb"></a>
<a id="agroup__pcie__host__msi__interface_html_ga2cdf2a32cb4c6e4d68290a1e9020f4ee"></a>
<a id="agroup__pcie__host__msi__interface_html_ga57226ef41cee2008a2c92098dd52af6b"></a>
<a id="agroup__pcie__host__msi__interface_html_ga9ede6a7a472ee62f0975256a1b5f1231"></a>
<a id="agroup__pcie__host__msi__interface_html_gac16ef7e19d7584aa2fc3a839b1b8fb01"></a>
<a id="agroup__pcie__host__msi__interface_html_gae89ee2177016ab1df94c7f453eb5c25d"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructmsi__vector_html"></a>
<a id="astructmsi__vector_html_a643d712565f3464874efaab81b25b68a"></a>
<a id="astructmsi__vector_html_aec3f368bdbe75d9e53d6bc9b0f6a18a7"></a>
<a id="astructmsix__vector_html"></a>
<a id="astructmsix__vector_html_a2c09a989a9ed99536d85c0e800283743"></a>
<a id="astructmsix__vector_html_a908e2d095b43713f0b9682716cd4ae85"></a>
<a id="astructmsix__vector_html_ac4d0f7192cc8bcaffd4fac75589ca298"></a>
<a id="astructmsix__vector_html_acd899f1dc388ef49f38d593083e0042d"></a>

```c
/*
 * Copyright (c) 2019 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_PCIE_MSI_H_
#define ZEPHYR_INCLUDE_DRIVERS_PCIE_MSI_H_


#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <stdbool.h>

#include <zephyr/drivers/pcie/pcie.h>

#ifdef __cplusplus
extern "C" {
#endif

#ifdef CONFIG_PCIE_CONTROLLER
struct msi_vector_generic {
        unsigned int irq;
        uint32_t address;
        uint16_t eventid;
        unsigned int priority;
};

typedef struct msi_vector_generic arch_msi_vector_t;

#define PCI_DEVID(bus, dev, fn) ((((bus) & 0xff) << 8) | (((dev) & 0x1f) << 3) | ((fn) & 0x07))
#define PCI_BDF_TO_DEVID(bdf)   PCI_DEVID(PCIE_BDF_TO_BUS(bdf), \
                                          PCIE_BDF_TO_DEV(bdf), \
                                          PCIE_BDF_TO_FUNC(bdf))

#endif

struct msix_vector {
        uint32_t msg_addr;
        uint32_t msg_up_addr;
        uint32_t msg_data;
        uint32_t vector_ctrl;
} __packed;

struct msi_vector {
        pcie_bdf_t bdf;
        arch_msi_vector_t arch;
#ifdef CONFIG_PCIE_MSI_X
        struct msix_vector *msix_vector;
        bool msix;
#endif /* CONFIG_PCIE_MSI_X */
};

typedef struct msi_vector msi_vector_t;

#ifdef CONFIG_PCIE_MSI_MULTI_VECTOR

extern uint8_t pcie_msi_vectors_allocate(pcie_bdf_t bdf,
                                         unsigned int priority,
                                         msi_vector_t *vectors,
                                         uint8_t n_vector);

extern bool pcie_msi_vector_connect(pcie_bdf_t bdf,
                                    msi_vector_t *vector,
                                    void (*routine)(const void *parameter),
                                    const void *parameter,
                                    uint32_t flags);

#endif /* CONFIG_PCIE_MSI_MULTI_VECTOR */

extern uint32_t pcie_msi_map(unsigned int irq,
                             msi_vector_t *vector,
                             uint8_t n_vector);

extern uint16_t pcie_msi_mdr(unsigned int irq,
                             msi_vector_t *vector);

extern bool pcie_msi_enable(pcie_bdf_t bdf,
                            msi_vector_t *vectors,
                            uint8_t n_vector,
                            unsigned int irq);

extern bool pcie_is_msi(pcie_bdf_t bdf);

/*
 * The first word of the MSI capability is shared with the
 * capability ID and list link.  The high 16 bits are the MCR.
 */

#define PCIE_MSI_MCR            0U

#define PCIE_MSI_MCR_EN         0x00010000U  /* enable MSI */
#define PCIE_MSI_MCR_MMC        0x000E0000U  /* Multi Messages Capable mask */
#define PCIE_MSI_MCR_MMC_SHIFT  17
#define PCIE_MSI_MCR_MME        0x00700000U  /* mask of # of enabled IRQs */
#define PCIE_MSI_MCR_MME_SHIFT  20
#define PCIE_MSI_MCR_64         0x00800000U  /* 64-bit MSI */

/*
 * The MAP follows the MCR. If PCIE_MSI_MCR_64, then the MAP
 * is two words long. The MDR follows immediately after the MAP.
 */

#define PCIE_MSI_MAP0           1U
#define PCIE_MSI_MAP1_64        2U
#define PCIE_MSI_MDR_32         2U
#define PCIE_MSI_MDR_64         3U

/*
 * As for MSI, he first word of the MSI-X capability is shared
 * with the capability ID and list link.  The high 16 bits are the MCR.
 */

#define PCIE_MSIX_MCR                   0U

#define PCIE_MSIX_MCR_EN                0x80000000U /* Enable MSI-X */
#define PCIE_MSIX_MCR_FMASK             0x40000000U /* Function Mask */
#define PCIE_MSIX_MCR_TSIZE             0x07FF0000U /* Table size mask */
#define PCIE_MSIX_MCR_TSIZE_SHIFT       16
#define PCIE_MSIR_TABLE_ENTRY_SIZE      16

#define PCIE_MSIX_TR                    1U
#define PCIE_MSIX_TR_BIR                0x00000007U /* Table BIR mask */
#define PCIE_MSIX_TR_OFFSET             0xFFFFFFF8U /* Offset mask */

#define PCIE_MSIX_PBA                   2U
#define PCIE_MSIX_PBA_BIR               0x00000007U /* PBA BIR mask */
#define PCIE_MSIX_PBA_OFFSET            0xFFFFFFF8U /* Offset mask */

#define PCIE_VTBL_MA                    0U /* Msg Address offset */
#define PCIE_VTBL_MUA                   4U /* Msg Upper Address offset */
#define PCIE_VTBL_MD                    8U /* Msg Data offset */
#define PCIE_VTBL_VCTRL                 12U /* Vector control offset */

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_PCIE_MSI_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 63 行

条件编译配置（Configuration）标记：`CONFIG_PCIE_MSI_X`。

### 注释 3：原第 102 行

条件编译配置（Configuration）标记：`CONFIG_PCIE_MSI_MULTI_VECTOR`。

### 注释 4：原第 152 行

消息信号中断（MSI）能力结构的第一个字与能力标识符（capability ID）和列表链接（list link）共享；高 16 位为消息控制寄存器（MCR）。

### 注释 5：原第 159 行

启用消息信号中断（MSI）。

### 注释 6：原第 160 行

多消息能力（Multi Messages Capable）掩码。

### 注释 7：原第 162 行

已启用 IRQ 数量的掩码。

### 注释 8：原第 164 行

64 位 MSI。

### 注释 9：原第 166 行

消息地址指针（MAP）位于 MCR 之后。如果设置 `PCIE_MSI_MCR_64`，MAP 长度为两个字。消息数据寄存器（MDR）紧接在 MAP 之后。

### 注释 10：原第 176 行

与 MSI 相同，MSI-X 能力结构的第一个字与能力标识符（capability ID）和列表链接（list link）共享；高 16 位为消息控制寄存器（MCR）。

### 注释 11：原第 183 行

启用 MSI-X。

### 注释 12：原第 184 行

功能掩码（Function Mask）。

### 注释 13：原第 185 行

表大小掩码（Table size mask）。

### 注释 14：原第 190 行

表的基地址寄存器指示器（Table BIR）掩码。

### 注释 15：原第 191 行

偏移量掩码（Offset mask）。

### 注释 16：原第 194 行

挂起位数组（PBA）的 BIR 掩码。

### 注释 17：原第 195 行

偏移量掩码（Offset mask）。

### 注释 18：原第 197 行

消息地址（Msg Address）偏移量。

### 注释 19：原第 198 行

消息高位地址（Msg Upper Address）偏移量。

### 注释 20：原第 199 行

消息数据（Msg Data）偏移量。

### 注释 21：原第 200 行

向量控制（Vector control）偏移量。

### 注释 22：原第 210 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PCIE_MSI_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_service_reference/P027_zephyr__drivers__pcie__msi.h_文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [zephyr/drivers/pcie/pcie.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h.html)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [msix_vector](../platform_security_model_reference/P019_msix_vector_结构体.md)
- [msg_addr](../platform_security_model_reference/P019_msix_vector_结构体.md#a2c09a989a9ed99536d85c0e800283743)
- [msg_up_addr](../platform_security_model_reference/P019_msix_vector_结构体.md#a908e2d095b43713f0b9682716cd4ae85)
- [msg_data](../platform_security_model_reference/P019_msix_vector_结构体.md#acd899f1dc388ef49f38d593083e0042d)
- [vector_ctrl](../platform_security_model_reference/P019_msix_vector_结构体.md#ac4d0f7192cc8bcaffd4fac75589ca298)
- [msi_vector](../platform_security_model_reference/P018_msi_vector_结构体.md)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)
- [bdf](../platform_security_model_reference/P018_msi_vector_结构体.md#a643d712565f3464874efaab81b25b68a)
- [arch](../platform_security_model_reference/P018_msi_vector_结构体.md#aec3f368bdbe75d9e53d6bc9b0f6a18a7)
- [msi_vector_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga9ede6a7a472ee62f0975256a1b5f1231)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [pcie_msi_map](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga2cdf2a32cb4c6e4d68290a1e9020f4ee)
- [pcie_msi_mdr](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gae89ee2177016ab1df94c7f453eb5c25d)
- [pcie_msi_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga57226ef41cee2008a2c92098dd52af6b)
- [pcie_is_msi](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#gac16ef7e19d7584aa2fc3a839b1b8fb01)
- [pcie.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h.html)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [msi_vector::bdf](../platform_security_model_reference/P018_msi_vector_结构体.md#a643d712565f3464874efaab81b25b68a)
- [msi_vector::arch](../platform_security_model_reference/P018_msi_vector_结构体.md#aec3f368bdbe75d9e53d6bc9b0f6a18a7)
- [msix_vector::msg_addr](../platform_security_model_reference/P019_msix_vector_结构体.md#a2c09a989a9ed99536d85c0e800283743)
- [msix_vector::msg_up_addr](../platform_security_model_reference/P019_msix_vector_结构体.md#a908e2d095b43713f0b9682716cd4ae85)
- [msix_vector::vector_ctrl](../platform_security_model_reference/P019_msix_vector_结构体.md#ac4d0f7192cc8bcaffd4fac75589ca298)
- [msix_vector::msg_data](../platform_security_model_reference/P019_msix_vector_结构体.md#acd899f1dc388ef49f38d593083e0042d)

---

[上一章](P004_mcc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_mdio.h_源码浏览.md)
