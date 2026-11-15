---
id: learning.zephyr-docs.api-source-reference.page-716
title: riscv_aplic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第716章\_riscv\_aplic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html)。

## 716.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="foldopen00229"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="foldopen00240"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="foldopen00252"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="foldopen00334"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="foldopen00346"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="foldopen00360"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="foldopen00373"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="foldopen00384"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="foldopen00395"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="foldopen00406"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="foldopen00417"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__device__model_html_gaadf3ffb63df544eb3de356ab2c5e9e3c"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="ariscv__aplic_8h_html_a122c9068e3bbedf9c145493278b8bd05"></a>
<a id="ariscv__aplic_8h_html_a13ecae2ec0109593570e5f270e230daa"></a>
<a id="ariscv__aplic_8h_html_a189d3723a935cb5b44e1dceaac9e75df"></a>
<a id="ariscv__aplic_8h_html_a25e2d4768a61e0b8b135840d45777c5f"></a>
<a id="ariscv__aplic_8h_html_a2f4b2488b715ab29e6d12fb07947f281"></a>
<a id="ariscv__aplic_8h_html_a310930e6500b8a30d156d621785ec8ca"></a>
<a id="ariscv__aplic_8h_html_a317604c4a77581599e3b568c0af0f8c5"></a>
<a id="ariscv__aplic_8h_html_a32492c238d531bf4474fa391aa634429"></a>
<a id="ariscv__aplic_8h_html_a37b9d14cf6a40d93085e3b2a8bd9d57d"></a>
<a id="ariscv__aplic_8h_html_a3a7d90ad87464060903ac13422150964"></a>
<a id="ariscv__aplic_8h_html_a443e3d8683aec28992398a8ab672af63"></a>
<a id="ariscv__aplic_8h_html_a48bfa691091e24dba2ab8b466e869c9e"></a>
<a id="ariscv__aplic_8h_html_a6599e6e97695abefabbc8a6fc3fd56ff"></a>
<a id="ariscv__aplic_8h_html_a66c8ea9cb1891e48b537a663579e56aa"></a>
<a id="ariscv__aplic_8h_html_a771d4b9c52895945bc94b7ce6bc24c1a"></a>
<a id="ariscv__aplic_8h_html_a83d33a6a410d4fd85da300a8f308dee8"></a>
<a id="ariscv__aplic_8h_html_a871822d8d01a9428795df3bc7a183499"></a>
<a id="ariscv__aplic_8h_html_a959870fc662d2251e280f88766dfb183"></a>
<a id="ariscv__aplic_8h_html_a9842d5ae9cf44ef0396d2a01968c9ce9"></a>
<a id="ariscv__aplic_8h_html_a99ee07d894d3a09370d5ab0077359ac4"></a>
<a id="ariscv__aplic_8h_html_a9bb9d97a3e51d547f314bbb3ff73776a"></a>
<a id="ariscv__aplic_8h_html_ab446350754c3f125e78ae3bf89e71636"></a>
<a id="ariscv__aplic_8h_html_ac78b1ec01b7de7c6bd556cbd0a5efcab"></a>
<a id="ariscv__aplic_8h_html_aca4663969a234c72ca6dcf8ca3834771"></a>
<a id="ariscv__aplic_8h_html_afa4ce7bd64fb5c05ecef44088905f603"></a>
<a id="ariscv__aplic_8h_html_afd9a4f6b16ad61355fd159f87e4ccf9c"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_APLIC_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_APLIC_H_

#include <zephyr/device.h>
#include <zephyr/types.h>

#define APLIC_DOMAINCFG      0x0000
#define APLIC_SOURCECFG_BASE 0x0004
#define APLIC_SETIP_BASE     0x1C00
#define APLIC_SETIPNUM       0x1CDC
#define APLIC_CLRIP_BASE     0x1D00
#define APLIC_CLRIPNUM       0x1DDC
#define APLIC_SETIE_BASE     0x1E00
#define APLIC_SETIENUM       0x1EDC
#define APLIC_CLRIE_BASE     0x1F00
#define APLIC_CLRIENUM       0x1FDC
#define APLIC_MSIADDRCFG     0x1BC0
#define APLIC_MSIADDRCFGH    0x1BC4
#define APLIC_SMSIADDRCFG    0x1BC8
#define APLIC_SMSIADDRCFGH   0x1BCC
#define APLIC_GENMSI         0x3000
#define APLIC_TARGET_BASE    0x3004
#define APLIC_IDC_BASE       0x4000

#define APLIC_DOMAINCFG_IE BIT(8)
#define APLIC_DOMAINCFG_DM BIT(2)
#define APLIC_DOMAINCFG_BE BIT(0)

#define APLIC_MSIADDRCFGH_L_BIT      31
#define APLIC_MSIADDRCFGH_HHXS_SHIFT 24
#define APLIC_MSIADDRCFGH_HHXS_MASK  0x1F
#define APLIC_MSIADDRCFGH_LHXS_SHIFT 20
#define APLIC_MSIADDRCFGH_LHXS_MASK  0x7
#define APLIC_MSIADDRCFGH_HHXW_SHIFT 16
#define APLIC_MSIADDRCFGH_HHXW_MASK  0x7
#define APLIC_MSIADDRCFGH_LHXW_SHIFT 12
#define APLIC_MSIADDRCFGH_LHXW_MASK  0xF
#define APLIC_MSIADDRCFGH_BAPPN_MASK 0xFFF

#define APLIC_SOURCECFG_D_BIT   10
#define APLIC_SOURCECFG_SM_MASK 0x7
#define APLIC_SM_INACTIVE       0x0
#define APLIC_SM_DETACHED       0x1
#define APLIC_SM_EDGE_RISE      0x4
#define APLIC_SM_EDGE_FALL      0x5
#define APLIC_SM_LEVEL_HIGH     0x6
#define APLIC_SM_LEVEL_LOW      0x7

#define APLIC_TARGET_HART_SHIFT 18
#define APLIC_TARGET_HART_MASK  0x3FFF
#define APLIC_TARGET_MSI_DEL    BIT(11)
#define APLIC_TARGET_EIID_MASK  0x7FF

#define APLIC_GENMSI_HART_SHIFT    18
#define APLIC_GENMSI_HART_MASK     0x3FFF
#define APLIC_GENMSI_CONTEXT_SHIFT 13
#define APLIC_GENMSI_CONTEXT_MASK  0x1F
#define APLIC_GENMSI_BUSY          BIT(12)
#define APLIC_GENMSI_MMSI_MODE     BIT(11)
#define APLIC_GENMSI_EIID_MASK     0x7FF

#define APLIC_IDC_IDELIVERY_OFFSET  0x0
#define APLIC_IDC_IFORCE_OFFSET     0x4
#define APLIC_IDC_ITHRESHOLD_OFFSET 0x8
#define APLIC_IDC_TOPI_OFFSET       0x18
#define APLIC_IDC_CLAIMI_OFFSET     0x1C
#define APLIC_IDC_STRUCT_SIZE       0x20

#define APLIC_IDC_IDELIVERY_ENABLE BIT(0)

#define APLIC_IDC_IFORCE_SET 1

#define APLIC_IDC_ITHRESHOLD 0

#define APLIC_IPRIO_MASK               BIT_MASK(8)
#define APLIC_INTERRUPT_IDENTITY_SHIFT 16
#define APLIC_INTERRUPT_IDENTITY_MASK  (BIT_MASK(10) << APLIC_INTERRUPT_IDENTITY_SHIFT)

static inline uint32_t aplic_sourcecfg_off(unsigned int src)
{
        return APLIC_SOURCECFG_BASE + (src - 1U) * 4U;
}

static inline uint32_t aplic_target_off(unsigned int src)
{
        return APLIC_TARGET_BASE + (src - 1U) * 4U;
}

static inline const struct device *riscv_aplic_get_dev(void)
{
        return DEVICE_DT_GET_ANY(riscv_aplic);
}

void riscv_aplic_domain_enable(const struct device *dev, bool enable);

void riscv_aplic_config_src(const struct device *dev, unsigned int src, unsigned int sm);

void riscv_aplic_enable_src(const struct device *dev, unsigned int src, bool enable);

#if defined(CONFIG_RISCV_APLIC_MSI) || defined(__DOXYGEN__)
void riscv_aplic_msi_route(const struct device *dev, unsigned int src, uint32_t hart,
                           uint32_t eiid);

void riscv_aplic_msi_inject_software_interrupt(const struct device *dev, uint32_t eiid,
                                               uint32_t hart_id, uint32_t context);
#endif /* CONFIG_RISCV_APLIC_MSI */

uint32_t riscv_aplic_get_num_sources(const struct device *dev);

static inline void riscv_aplic_enable_source(unsigned int src)
{
        riscv_aplic_enable_src(riscv_aplic_get_dev(), src, true);
}

static inline void riscv_aplic_disable_source(unsigned int src)
{
        riscv_aplic_enable_src(riscv_aplic_get_dev(), src, false);
}

#if defined(CONFIG_RISCV_APLIC_MSI) || defined(__DOXYGEN__)
static inline void riscv_aplic_msi_inject_genmsi(uint32_t hart, uint32_t eiid)
{
        riscv_aplic_msi_inject_software_interrupt(riscv_aplic_get_dev(), eiid, hart, 0);
}
#endif /* CONFIG_RISCV_APLIC_MSI */

#if defined(CONFIG_RISCV_APLIC_DIRECT) || defined(__DOXYGEN__)
static inline uint32_t aplic_idelivery_off(unsigned int cpu)
{
        return APLIC_IDC_BASE + (cpu * APLIC_IDC_STRUCT_SIZE) + APLIC_IDC_IDELIVERY_OFFSET;
}

static inline uint32_t aplic_ithreshold_off(unsigned int cpu)
{
        return APLIC_IDC_BASE + (cpu * APLIC_IDC_STRUCT_SIZE) + APLIC_IDC_ITHRESHOLD_OFFSET;
}

static inline uint32_t aplic_iforce_off(unsigned int cpu)
{
        return APLIC_IDC_BASE + (cpu * APLIC_IDC_STRUCT_SIZE) + APLIC_IDC_IFORCE_OFFSET;
}

static inline uint32_t aplic_topi_off(unsigned int cpu)
{
        return APLIC_IDC_BASE + (cpu * APLIC_IDC_STRUCT_SIZE) + APLIC_IDC_TOPI_OFFSET;
}

static inline uint32_t aplic_claimi_off(unsigned int cpu)
{
        return APLIC_IDC_BASE + (cpu * APLIC_IDC_STRUCT_SIZE) + APLIC_IDC_CLAIMI_OFFSET;
}
#endif /* CONFIG_RISCV_APLIC_DIRECT */

#endif
```

## 716.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 315 行

条件编译配置（Configuration）标记：`CONFIG_RISCV_APLIC_MSI`。

### 注释 3：原第 364 行

条件编译配置（Configuration）标记：`CONFIG_RISCV_APLIC_MSI`。

### 注释 4：原第 421 行

条件编译配置（Configuration）标记：`CONFIG_RISCV_APLIC_DIRECT`。

## 716.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [aplic_sourcecfg_off](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a317604c4a77581599e3b568c0af0f8c5)
- [APLIC_SOURCECFG_BASE](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a66c8ea9cb1891e48b537a663579e56aa)
- [aplic_target_off](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a122c9068e3bbedf9c145493278b8bd05)
- [APLIC_TARGET_BASE](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#aca4663969a234c72ca6dcf8ca3834771)
- [device](../device_reference/P002_设备对象结构.md)
- [riscv_aplic_get_dev](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a32492c238d531bf4474fa391aa634429)
- [DEVICE_DT_GET_ANY](../device_reference/P001_设备模型公共接口.md#gaadf3ffb63df544eb3de356ab2c5e9e3c)
- [riscv_aplic_domain_enable](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a771d4b9c52895945bc94b7ce6bc24c1a)
- [riscv_aplic_config_src](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a25e2d4768a61e0b8b135840d45777c5f)
- [riscv_aplic_enable_src](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a48bfa691091e24dba2ab8b466e869c9e)
- [riscv_aplic_msi_route](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a99ee07d894d3a09370d5ab0077359ac4)
- [riscv_aplic_msi_inject_software_interrupt](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#afa4ce7bd64fb5c05ecef44088905f603)
- [riscv_aplic_get_num_sources](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#ab446350754c3f125e78ae3bf89e71636)
- [riscv_aplic_enable_source](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a6599e6e97695abefabbc8a6fc3fd56ff)
- [riscv_aplic_disable_source](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a959870fc662d2251e280f88766dfb183)
- [riscv_aplic_msi_inject_genmsi](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a871822d8d01a9428795df3bc7a183499)
- [aplic_idelivery_off](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a83d33a6a410d4fd85da300a8f308dee8)
- [APLIC_IDC_BASE](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a9bb9d97a3e51d547f314bbb3ff73776a)
- [APLIC_IDC_STRUCT_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a310930e6500b8a30d156d621785ec8ca)
- [APLIC_IDC_IDELIVERY_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#afd9a4f6b16ad61355fd159f87e4ccf9c)
- [aplic_ithreshold_off](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a189d3723a935cb5b44e1dceaac9e75df)
- [APLIC_IDC_ITHRESHOLD_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a13ecae2ec0109593570e5f270e230daa)
- [aplic_iforce_off](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a9842d5ae9cf44ef0396d2a01968c9ce9)
- [APLIC_IDC_IFORCE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a2f4b2488b715ab29e6d12fb07947f281)
- [aplic_topi_off](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a37b9d14cf6a40d93085e3b2a8bd9d57d)
- [APLIC_IDC_TOPI_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a443e3d8683aec28992398a8ab672af63)
- [aplic_claimi_off](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#ac78b1ec01b7de7c6bd556cbd0a5efcab)
- [APLIC_IDC_CLAIMI_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html#a3a7d90ad87464060903ac13422150964)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P715_riscv_aia.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P717_riscv_aplic_direct.h_源码浏览.md)
