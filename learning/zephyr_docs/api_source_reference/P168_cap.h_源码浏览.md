---
id: learning.zephyr-docs.api-source-reference.page-168
title: cap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2cap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第168章\_cap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2cap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2cap_8h.html)。

## 168.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00016"></a>
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
<a id="l00048"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
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
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00097"></a>
<a id="l00101"></a>
<a id="l00102"></a>

```c
/*
 * Copyright (c) 2021 BayLibre, SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DRIVERS_PCIE_CAP_H_
#define ZEPHYR_INCLUDE_DRIVERS_PCIE_CAP_H_


#define PCI_CAP_ID_NULL         0x00U
#define PCI_CAP_ID_PM           0x01U
#define PCI_CAP_ID_AGP          0x02U
#define PCI_CAP_ID_VPD          0x03U
#define PCI_CAP_ID_SLOTID       0x04U
#define PCI_CAP_ID_MSI          0x05U
#define PCI_CAP_ID_CHSWP        0x06U
#define PCI_CAP_ID_PCIX         0x07U
#define PCI_CAP_ID_HT           0x08U
#define PCI_CAP_ID_VNDR         0x09U
#define PCI_CAP_ID_DBG          0x0AU
#define PCI_CAP_ID_CCRC         0x0BU
#define PCI_CAP_ID_SHPC         0x0CU
#define PCI_CAP_ID_SSVID        0x0DU
#define PCI_CAP_ID_AGP3         0x0EU
#define PCI_CAP_ID_SECDEV       0x0FU
#define PCI_CAP_ID_EXP          0x10U
#define PCI_CAP_ID_MSIX         0x11U
#define PCI_CAP_ID_SATA         0x12U
#define PCI_CAP_ID_AF           0x13U
#define PCI_CAP_ID_EA           0x14U
#define PCI_CAP_ID_FPB          0x14U


#define PCIE_EXT_CAP_ID_NULL    0x0000U
#define PCIE_EXT_CAP_ID_ERR     0x0001U
#define PCIE_EXT_CAP_ID_VC      0x0002U
#define PCIE_EXT_CAP_ID_DSN     0x0003U
#define PCIE_EXT_CAP_ID_PWR     0x0004U
#define PCIE_EXT_CAP_ID_RCLD    0x0005U
#define PCIE_EXT_CAP_ID_RCILC   0x0006U
#define PCIE_EXT_CAP_ID_RCEC    0x0007U
#define PCIE_EXT_CAP_ID_MFVC    0x0008U
#define PCIE_EXT_CAP_ID_MFVC_VC 0x0009U
#define PCIE_EXT_CAP_ID_RCRB    0x000AU
#define PCIE_EXT_CAP_ID_VNDR    0x000BU
#define PCIE_EXT_CAP_ID_CAC     0x000CU
#define PCIE_EXT_CAP_ID_ACS     0x000DU
#define PCIE_EXT_CAP_ID_ARI     0x000EU
#define PCIE_EXT_CAP_ID_ATS     0x000FU
#define PCIE_EXT_CAP_ID_SRIOV   0x0010U
#define PCIE_EXT_CAP_ID_MRIOV   0x0011U
#define PCIE_EXT_CAP_ID_MCAST   0x0012U
#define PCIE_EXT_CAP_ID_PRI     0x0013U
#define PCIE_EXT_CAP_ID_AMD_XXX 0x0014U
#define PCIE_EXT_CAP_ID_REBAR   0x0015U
#define PCIE_EXT_CAP_ID_DPA     0x0016U
#define PCIE_EXT_CAP_ID_TPH     0x0017U
#define PCIE_EXT_CAP_ID_LTR     0x0018U
#define PCIE_EXT_CAP_ID_SECPCI  0x0019U
#define PCIE_EXT_CAP_ID_PMUX    0x001AU
#define PCIE_EXT_CAP_ID_PASID   0x001BU
#define PCIE_EXT_CAP_ID_DPC     0x001DU
#define PCIE_EXT_CAP_ID_L1SS    0x001EU
#define PCIE_EXT_CAP_ID_PTM     0x001FU
#define PCIE_EXT_CAP_ID_DVSEC   0x0023U
#define PCIE_EXT_CAP_ID_DLF     0x0025U
#define PCIE_EXT_CAP_ID_PL_16GT 0x0026U
#define PCIE_EXT_CAP_ID_LMR     0x0027U
#define PCIE_EXT_CAP_ID_HID     0x0028U
#define PCIE_EXT_CAP_ID_NPEM    0x0029U
#define PCIE_EXT_CAP_ID_PL_32GT 0x002AU
#define PCIE_EXT_CAP_ID_AP      0x002BU
#define PCIE_EXT_CAP_ID_SFI     0x002CU


#endif /* ZEPHYR_INCLUDE_DRIVERS_PCIE_CAP_H_ */
```

## 168.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 BayLibre, SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 102 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PCIE_CAP_H_`。

## 168.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2cap_8h.html)

---

[上一章](P167_npm10xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P169_controller.h_源码浏览.md)
