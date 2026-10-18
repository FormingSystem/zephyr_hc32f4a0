---
id: learning.zephyr-docs.api-fota-storage-topic-reference.page-6
title: PCIe能力（Capabilities）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_PCIe能力（Capabilities）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-member-group"></a>
<a id="member-group"></a>

## 6.1\_PCI 与 PCI Express 能力（PCI & PCI Express Capabilities）

取自《PCI 代码与标识符分配规范》（PCI Code and ID Assignment Specification）修订版 1.11。

<a id="r_ga890142bda671b3558cd881f4b91a43ab"></a>

```c
#define PCI_CAP_ID_NULL 0x00U
```

相关声明：[PCI_CAP_ID_NULL](#ga890142bda671b3558cd881f4b91a43ab)。

空能力（Null Capability）。

<a id="r_ga9379bf318dd400e1076fbd5f0e331adb"></a>

```c
#define PCI_CAP_ID_PM 0x01U
```

相关声明：[PCI_CAP_ID_PM](#ga9379bf318dd400e1076fbd5f0e331adb)。

电源管理（Power Management）。

<a id="r_gac68c228e23e701fd4040b89c42537eac"></a>

```c
#define PCI_CAP_ID_AGP 0x02U
```

相关声明：[PCI_CAP_ID_AGP](#gac68c228e23e701fd4040b89c42537eac)。

加速图形端口（Accelerated Graphics Port，AGP）。

<a id="r_gaf419a56a517635f4d9f8a5c6f5fd9d08"></a>

```c
#define PCI_CAP_ID_VPD 0x03U
```

相关声明：[PCI_CAP_ID_VPD](#gaf419a56a517635f4d9f8a5c6f5fd9d08)。

关键产品数据（Vital Product Data，VPD）。

<a id="r_ga6d286311dd9f54468f125fd367683f74"></a>

```c
#define PCI_CAP_ID_SLOTID 0x04U
```

相关声明：[PCI_CAP_ID_SLOTID](#ga6d286311dd9f54468f125fd367683f74)。

插槽标识（Slot Identification）。

<a id="r_gad19597699011d0e047083968d2e835bd"></a>

```c
#define PCI_CAP_ID_MSI 0x05U
```

相关声明：[PCI_CAP_ID_MSI](#gad19597699011d0e047083968d2e835bd)。

消息信号中断（Message Signalled Interrupts，MSI）。

<a id="r_ga74356319083570ca7e5cf9a3eaaadd9b"></a>

```c
#define PCI_CAP_ID_CHSWP 0x06U
```

相关声明：[PCI_CAP_ID_CHSWP](#ga74356319083570ca7e5cf9a3eaaadd9b)。

CompactPCI 热插拔（HotSwap）。

<a id="r_ga24709fe61430ca25fabe665d8b1efca0"></a>

```c
#define PCI_CAP_ID_PCIX 0x07U
```

相关声明：[PCI_CAP_ID_PCIX](#ga24709fe61430ca25fabe665d8b1efca0)。

PCI-X。

<a id="r_gad50ed1a81153a04fa19534823d0109c9"></a>

```c
#define PCI_CAP_ID_HT 0x08U
```

相关声明：[PCI_CAP_ID_HT](#gad50ed1a81153a04fa19534823d0109c9)。

HyperTransport。

<a id="r_ga11b65631db23369276e062560f53b433"></a>

```c
#define PCI_CAP_ID_VNDR 0x09U
```

相关声明：[PCI_CAP_ID_VNDR](#ga11b65631db23369276e062560f53b433)。

厂商特定能力（Vendor-Specific）。

<a id="r_ga5a37d779c6259232cd4ec7bc3d80bc83"></a>

```c
#define PCI_CAP_ID_DBG 0x0AU
```

相关声明：[PCI_CAP_ID_DBG](#ga5a37d779c6259232cd4ec7bc3d80bc83)。

调试端口（Debug Port）。

<a id="r_gad45dfbc6ea8d963703e243dacdee084f"></a>

```c
#define PCI_CAP_ID_CCRC 0x0BU
```

相关声明：[PCI_CAP_ID_CCRC](#gad45dfbc6ea8d963703e243dacdee084f)。

CompactPCI 中央资源控制（Central Resource Control）。

<a id="r_gae538cdbc7eba80aac860f3340823f559"></a>

```c
#define PCI_CAP_ID_SHPC 0x0CU
```

相关声明：[PCI_CAP_ID_SHPC](#gae538cdbc7eba80aac860f3340823f559)。

PCI 标准热插拔控制器（PCI Standard Hot-Plug Controller）。

<a id="r_ga8814c4f32748170e8b5f15dc2ade5dc5"></a>

```c
#define PCI_CAP_ID_SSVID 0x0DU
```

相关声明：[PCI_CAP_ID_SSVID](#ga8814c4f32748170e8b5f15dc2ade5dc5)。

桥接器子系统厂商／设备标识符（Bridge Subsystem Vendor/Device ID）。

<a id="r_gae351b2497f7231bfa2c08e97ba589cb7"></a>

```c
#define PCI_CAP_ID_AGP3 0x0EU
```

相关声明：[PCI_CAP_ID_AGP3](#gae351b2497f7231bfa2c08e97ba589cb7)。

AGP 8x。

<a id="r_ga20c7aadce06547a3ea37ce705ff0d289"></a>

```c
#define PCI_CAP_ID_SECDEV 0x0FU
```

相关声明：[PCI_CAP_ID_SECDEV](#ga20c7aadce06547a3ea37ce705ff0d289)。

安全设备（Secure Device）。

<a id="r_ga9b0efbb129a8600203135a64377beed0"></a>

```c
#define PCI_CAP_ID_EXP 0x10U
```

相关声明：[PCI_CAP_ID_EXP](#ga9b0efbb129a8600203135a64377beed0)。

PCI Express。

<a id="r_ga419307c3f83f3dca9aaa329de41dae63"></a>

```c
#define PCI_CAP_ID_MSIX 0x11U
```

相关声明：[PCI_CAP_ID_MSIX](#ga419307c3f83f3dca9aaa329de41dae63)。

MSI-X。

<a id="r_ga437d2f840145a2aae97880ad3579ca7d"></a>

```c
#define PCI_CAP_ID_SATA 0x12U
```

相关声明：[PCI_CAP_ID_SATA](#ga437d2f840145a2aae97880ad3579ca7d)。

串行 ATA 数据／索引配置（Serial ATA Data/Index Configuration）。

<a id="r_ga7bf330224972c1a16cbafa907387b9ed"></a>

```c
#define PCI_CAP_ID_AF 0x13U
```

相关声明：[PCI_CAP_ID_AF](#ga7bf330224972c1a16cbafa907387b9ed)。

PCI 高级功能（PCI Advanced Features）。

<a id="r_ga591d30c052c32a4f3cbb510e8b052b62"></a>

```c
#define PCI_CAP_ID_EA 0x14U
```

相关声明：[PCI_CAP_ID_EA](#ga591d30c052c32a4f3cbb510e8b052b62)。

PCI 增强分配（PCI Enhanced Allocation）。

<a id="r_gad00f421c7bc8613ad7770ea2e0a5d8da"></a>

```c
#define PCI_CAP_ID_FPB 0x14U
```

相关声明：[PCI_CAP_ID_FPB](#gad00f421c7bc8613ad7770ea2e0a5d8da)。

展平门户桥（Flattening Portal Bridge）。

## 6.2\_PCI Express 扩展能力（PCI Express Extended Capabilities）

<a id="r_ga2f6c4feb384e41711aa53545952e3cac"></a>

```c
#define PCIE_EXT_CAP_ID_NULL 0x0000U
```

相关声明：[PCIE_EXT_CAP_ID_NULL](#ga2f6c4feb384e41711aa53545952e3cac)。

空能力（Null Capability）。

<a id="r_ga224acf772427857ca1f5a0b155c30d63"></a>

```c
#define PCIE_EXT_CAP_ID_ERR 0x0001U
```

相关声明：[PCIE_EXT_CAP_ID_ERR](#ga224acf772427857ca1f5a0b155c30d63)。

高级错误报告（Advanced Error Reporting，AER）。

<a id="r_gaaa8d5de1c1925dea16e40b72fafa5b8f"></a>

```c
#define PCIE_EXT_CAP_ID_VC 0x0002U
```

相关声明：[PCIE_EXT_CAP_ID_VC](#gaaa8d5de1c1925dea16e40b72fafa5b8f)。

不使用多功能虚拟通道（MFVC）时的虚拟通道（Virtual Channel）。

<a id="r_ga29a18f51cad5281e3f6a283d3c7acb49"></a>

```c
#define PCIE_EXT_CAP_ID_DSN 0x0003U
```

相关声明：[PCIE_EXT_CAP_ID_DSN](#ga29a18f51cad5281e3f6a283d3c7acb49)。

设备序列号（Device Serial Number）。

<a id="r_gadc91da3b61af0b0a047ec74860dc3201"></a>

```c
#define PCIE_EXT_CAP_ID_PWR 0x0004U
```

相关声明：[PCIE_EXT_CAP_ID_PWR](#gadc91da3b61af0b0a047ec74860dc3201)。

功率预算（Power Budgeting）。

<a id="r_ga46f3607fa47b26ef099f9bfdcdb0763f"></a>

```c
#define PCIE_EXT_CAP_ID_RCLD 0x0005U
```

相关声明：[PCIE_EXT_CAP_ID_RCLD](#ga46f3607fa47b26ef099f9bfdcdb0763f)。

根复合体链路声明（Root Complex Link Declaration）。

<a id="r_ga973a2816ae68ab75d5b4118890fd4383"></a>

```c
#define PCIE_EXT_CAP_ID_RCILC 0x0006U
```

相关声明：[PCIE_EXT_CAP_ID_RCILC](#ga973a2816ae68ab75d5b4118890fd4383)。

根复合体内部链路控制（Root Complex Internal Link Control）。

<a id="r_ga78b98a43b8e6661d6745df19c8591f47"></a>

```c
#define PCIE_EXT_CAP_ID_RCEC 0x0007U
```

相关声明：[PCIE_EXT_CAP_ID_RCEC](#ga78b98a43b8e6661d6745df19c8591f47)。

根复合体事件收集器端点关联（Root Complex Event Collector Endpoint Association）。

<a id="r_ga2cfa2f9212fb923c3811c0cdc769a877"></a>

```c
#define PCIE_EXT_CAP_ID_MFVC 0x0008U
```

相关声明：[PCIE_EXT_CAP_ID_MFVC](#ga2cfa2f9212fb923c3811c0cdc769a877)。

多功能虚拟通道能力（Multi-Function VC Capability，MFVC）。

<a id="r_ga7c2b491e1c994730afe08880dfb1b036"></a>

```c
#define PCIE_EXT_CAP_ID_MFVC_VC 0x0009U
```

相关声明：[PCIE_EXT_CAP_ID_MFVC_VC](#ga7c2b491e1c994730afe08880dfb1b036)。

与多功能虚拟通道（MFVC）配合使用的虚拟通道（Virtual Channel）。

<a id="r_ga356973ae03fb0d33df4092a311818e9b"></a>

```c
#define PCIE_EXT_CAP_ID_RCRB 0x000AU
```

相关声明：[PCIE_EXT_CAP_ID_RCRB](#ga356973ae03fb0d33df4092a311818e9b)。

根复合体寄存器块（Root Complex Register Block）。

<a id="r_gac864550f144038d5bbdf5e556faa640e"></a>

```c
#define PCIE_EXT_CAP_ID_VNDR 0x000BU
```

相关声明：[PCIE_EXT_CAP_ID_VNDR](#gac864550f144038d5bbdf5e556faa640e)。

厂商特定扩展能力（Vendor-Specific Extended Capability）。

<a id="r_gaff6494cd92013933dedbab2e2ae5c6b3"></a>

```c
#define PCIE_EXT_CAP_ID_CAC 0x000CU
```

相关声明：[PCIE_EXT_CAP_ID_CAC](#gaff6494cd92013933dedbab2e2ae5c6b3)。

配置访问关联（Config Access Correlation），已废弃（Obsolete）。

<a id="r_ga6b63b04d182b916db526525b064ed285"></a>

```c
#define PCIE_EXT_CAP_ID_ACS 0x000DU
```

相关声明：[PCIE_EXT_CAP_ID_ACS](#ga6b63b04d182b916db526525b064ed285)。

访问控制服务（Access Control Services，ACS）。

<a id="r_gaf890e2f4f3873b60ac83df345ab0cd8f"></a>

```c
#define PCIE_EXT_CAP_ID_ARI 0x000EU
```

相关声明：[PCIE_EXT_CAP_ID_ARI](#gaf890e2f4f3873b60ac83df345ab0cd8f)。

替代路由标识符解释（Alternate Routing-ID Interpretation，ARI）。

<a id="r_ga79a9cb071afc5cff9e699c232841623c"></a>

```c
#define PCIE_EXT_CAP_ID_ATS 0x000FU
```

相关声明：[PCIE_EXT_CAP_ID_ATS](#ga79a9cb071afc5cff9e699c232841623c)。

地址转换服务（Address Translation Services，ATS）。

<a id="r_gae8767a1dd6e203aa2ccd75d1fd05eb7d"></a>

```c
#define PCIE_EXT_CAP_ID_SRIOV 0x0010U
```

相关声明：[PCIE_EXT_CAP_ID_SRIOV](#gae8767a1dd6e203aa2ccd75d1fd05eb7d)。

单根输入／输出虚拟化（Single Root I/O Virtualization，SR-IOV）。

<a id="r_gaa117a86f2691d8711fa6b70e196ead01"></a>

```c
#define PCIE_EXT_CAP_ID_MRIOV 0x0011U
```

相关声明：[PCIE_EXT_CAP_ID_MRIOV](#gaa117a86f2691d8711fa6b70e196ead01)。

多根输入／输出虚拟化（Multi Root I/O Virtualization，MR-IOV）。

<a id="r_ga2810671833871608043e6e910d79dffd"></a>

```c
#define PCIE_EXT_CAP_ID_MCAST 0x0012U
```

相关声明：[PCIE_EXT_CAP_ID_MCAST](#ga2810671833871608043e6e910d79dffd)。

组播（Multicast）。

<a id="r_ga37e0ac002e9742bb9177588d2dfa850b"></a>

```c
#define PCIE_EXT_CAP_ID_PRI 0x0013U
```

相关声明：[PCIE_EXT_CAP_ID_PRI](#ga37e0ac002e9742bb9177588d2dfa850b)。

页面请求接口（Page Request Interface）。

<a id="r_gab8be630bf1dc810f2964e979ac46f77c"></a>

```c
#define PCIE_EXT_CAP_ID_AMD_XXX 0x0014U
```

相关声明：[PCIE_EXT_CAP_ID_AMD_XXX](#gab8be630bf1dc810f2964e979ac46f77c)。

保留供 AMD 使用（Reserved for AMD）。

<a id="r_gabae7e5d40435723e6d808c377753332a"></a>

```c
#define PCIE_EXT_CAP_ID_REBAR 0x0015U
```

相关声明：[PCIE_EXT_CAP_ID_REBAR](#gabae7e5d40435723e6d808c377753332a)。

可调整大小的基地址寄存器（Resizable BAR）。

<a id="r_ga812c156b93d070a06d3a56b5785788fd"></a>

```c
#define PCIE_EXT_CAP_ID_DPA 0x0016U
```

相关声明：[PCIE_EXT_CAP_ID_DPA](#ga812c156b93d070a06d3a56b5785788fd)。

动态功率分配（Dynamic Power Allocation）。

<a id="r_ga558289987600691fce5574feb253b4cb"></a>

```c
#define PCIE_EXT_CAP_ID_TPH 0x0017U
```

相关声明：[PCIE_EXT_CAP_ID_TPH](#ga558289987600691fce5574feb253b4cb)。

TPH 请求方（TPH Requester）。

<a id="r_ga9545f09c97f2dd4f751767e6e54326ec"></a>

```c
#define PCIE_EXT_CAP_ID_LTR 0x0018U
```

相关声明：[PCIE_EXT_CAP_ID_LTR](#ga9545f09c97f2dd4f751767e6e54326ec)。

延迟容忍度报告（Latency Tolerance Reporting）。

<a id="r_gacd1a90cce3892bacc40939a04b707d20"></a>

```c
#define PCIE_EXT_CAP_ID_SECPCI 0x0019U
```

相关声明：[PCIE_EXT_CAP_ID_SECPCI](#gacd1a90cce3892bacc40939a04b707d20)。

次级 PCIe 能力（Secondary PCIe Capability）。

<a id="r_gaf6c41b4ad9e32c4420cb89cc5a0d51c2"></a>

```c
#define PCIE_EXT_CAP_ID_PMUX 0x001AU
```

相关声明：[PCIE_EXT_CAP_ID_PMUX](#gaf6c41b4ad9e32c4420cb89cc5a0d51c2)。

协议复用（Protocol Multiplexing）。

<a id="r_ga0c3b5efb8d9fb69a8fdbb9ca147a3069"></a>

```c
#define PCIE_EXT_CAP_ID_PASID 0x001BU
```

相关声明：[PCIE_EXT_CAP_ID_PASID](#ga0c3b5efb8d9fb69a8fdbb9ca147a3069)。

进程地址空间标识符（Process Address Space ID，PASID）。

<a id="r_ga40f83a1c280acb8f3f3908d860874015"></a>

```c
#define PCIE_EXT_CAP_ID_DPC 0x001DU
```

相关声明：[PCIE_EXT_CAP_ID_DPC](#ga40f83a1c280acb8f3f3908d860874015)。

下游端口故障遏制（Downstream Port Containment，DPC）。

<a id="r_ga3006998c35d9c8f8e3d69716cda6def7"></a>

```c
#define PCIE_EXT_CAP_ID_L1SS 0x001EU
```

相关声明：[PCIE_EXT_CAP_ID_L1SS](#ga3006998c35d9c8f8e3d69716cda6def7)。

L1 电源管理子状态（L1 PM Substates）。

<a id="r_ga134d53764458500ea4ca58fe016f46fa"></a>

```c
#define PCIE_EXT_CAP_ID_PTM 0x001FU
```

相关声明：[PCIE_EXT_CAP_ID_PTM](#ga134d53764458500ea4ca58fe016f46fa)。

精确时间测量（Precision Time Measurement）。

<a id="r_gab1d94b05177a5064a78e4048eff473b1"></a>

```c
#define PCIE_EXT_CAP_ID_DVSEC 0x0023U
```

相关声明：[PCIE_EXT_CAP_ID_DVSEC](#gab1d94b05177a5064a78e4048eff473b1)。

指定厂商特定扩展能力（Designated Vendor-Specific Extended Capability）。

<a id="r_ga2e8324ea3b27a63e213252bed6c78ca6"></a>

```c
#define PCIE_EXT_CAP_ID_DLF 0x0025U
```

相关声明：[PCIE_EXT_CAP_ID_DLF](#ga2e8324ea3b27a63e213252bed6c78ca6)。

数据链路功能（Data Link Feature）。

<a id="r_ga60203711f9fe698f3e7e138e0468645a"></a>

```c
#define PCIE_EXT_CAP_ID_PL_16GT 0x0026U
```

相关声明：[PCIE_EXT_CAP_ID_PL_16GT](#ga60203711f9fe698f3e7e138e0468645a)。

16.0 GT/s 物理层（Physical Layer）。

<a id="r_ga56b3b2bd686b6b99c2ae34ae57228160"></a>

```c
#define PCIE_EXT_CAP_ID_LMR 0x0027U
```

相关声明：[PCIE_EXT_CAP_ID_LMR](#ga56b3b2bd686b6b99c2ae34ae57228160)。

接收端通道裕量测量（Lane Margining at the Receiver）。

<a id="r_ga0087a39c01053f83b3ac3bb3b057ac2a"></a>

```c
#define PCIE_EXT_CAP_ID_HID 0x0028U
```

相关声明：[PCIE_EXT_CAP_ID_HID](#ga0087a39c01053f83b3ac3bb3b057ac2a)。

层次结构标识符（Hierarchy ID）。

<a id="r_ga03dafb2eb5449f17dc18898ea319d729"></a>

```c
#define PCIE_EXT_CAP_ID_NPEM 0x0029U
```

相关声明：[PCIE_EXT_CAP_ID_NPEM](#ga03dafb2eb5449f17dc18898ea319d729)。

原生 PCIe 机箱管理（Native PCIe Enclosure Management）。

<a id="r_ga8a8768d04866a479114bcf276466501f"></a>

```c
#define PCIE_EXT_CAP_ID_PL_32GT 0x002AU
```

相关声明：[PCIE_EXT_CAP_ID_PL_32GT](#ga8a8768d04866a479114bcf276466501f)。

32.0 GT/s 物理层（Physical Layer）。

<a id="r_ga53e188f6e71f04012e7739e75a015398"></a>

```c
#define PCIE_EXT_CAP_ID_AP 0x002BU
```

相关声明：[PCIE_EXT_CAP_ID_AP](#ga53e188f6e71f04012e7739e75a015398)。

替代协议（Alternate Protocol）。

<a id="r_ga0e173611874d25c0cd5bd62372542380"></a>

```c
#define PCIE_EXT_CAP_ID_SFI 0x002CU
```

相关声明：[PCIE_EXT_CAP_ID_SFI](#ga0e173611874d25c0cd5bd62372542380)。

系统固件中介（System Firmware Intermediary）。

## 6.3\_详细说明（Detailed Documentation）

<a id="ga7bf330224972c1a16cbafa907387b9ed"></a>

### `PCI_CAP_ID_AF`

```c
#define PCI_CAP_ID_AF 0x13U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

PCI 高级功能（PCI Advanced Features）。

<a id="gac68c228e23e701fd4040b89c42537eac"></a>

### `PCI_CAP_ID_AGP`

```c
#define PCI_CAP_ID_AGP 0x02U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

加速图形端口（Accelerated Graphics Port，AGP）。

<a id="gae351b2497f7231bfa2c08e97ba589cb7"></a>

### `PCI_CAP_ID_AGP3`

```c
#define PCI_CAP_ID_AGP3 0x0EU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

AGP 8x。

<a id="gad45dfbc6ea8d963703e243dacdee084f"></a>

### `PCI_CAP_ID_CCRC`

```c
#define PCI_CAP_ID_CCRC 0x0BU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

CompactPCI 中央资源控制（Central Resource Control）。

<a id="ga74356319083570ca7e5cf9a3eaaadd9b"></a>

### `PCI_CAP_ID_CHSWP`

```c
#define PCI_CAP_ID_CHSWP 0x06U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

CompactPCI 热插拔（HotSwap）。

<a id="ga5a37d779c6259232cd4ec7bc3d80bc83"></a>

### `PCI_CAP_ID_DBG`

```c
#define PCI_CAP_ID_DBG 0x0AU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

调试端口（Debug Port）。

<a id="ga591d30c052c32a4f3cbb510e8b052b62"></a>

### `PCI_CAP_ID_EA`

```c
#define PCI_CAP_ID_EA 0x14U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

PCI 增强分配（PCI Enhanced Allocation）。

<a id="ga9b0efbb129a8600203135a64377beed0"></a>

### `PCI_CAP_ID_EXP`

```c
#define PCI_CAP_ID_EXP 0x10U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

PCI Express。

<a id="gad00f421c7bc8613ad7770ea2e0a5d8da"></a>

### `PCI_CAP_ID_FPB`

```c
#define PCI_CAP_ID_FPB 0x14U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

展平门户桥（Flattening Portal Bridge）。

<a id="gad50ed1a81153a04fa19534823d0109c9"></a>

### `PCI_CAP_ID_HT`

```c
#define PCI_CAP_ID_HT 0x08U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

HyperTransport。

<a id="gad19597699011d0e047083968d2e835bd"></a>

### `PCI_CAP_ID_MSI`

```c
#define PCI_CAP_ID_MSI 0x05U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

消息信号中断（Message Signalled Interrupts，MSI）。

<a id="ga419307c3f83f3dca9aaa329de41dae63"></a>

### `PCI_CAP_ID_MSIX`

```c
#define PCI_CAP_ID_MSIX 0x11U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

MSI-X。

<a id="ga890142bda671b3558cd881f4b91a43ab"></a>

### `PCI_CAP_ID_NULL`

```c
#define PCI_CAP_ID_NULL 0x00U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

空能力（Null Capability）。

<a id="ga24709fe61430ca25fabe665d8b1efca0"></a>

### `PCI_CAP_ID_PCIX`

```c
#define PCI_CAP_ID_PCIX 0x07U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

PCI-X。

<a id="ga9379bf318dd400e1076fbd5f0e331adb"></a>

### `PCI_CAP_ID_PM`

```c
#define PCI_CAP_ID_PM 0x01U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

电源管理（Power Management）。

<a id="ga437d2f840145a2aae97880ad3579ca7d"></a>

### `PCI_CAP_ID_SATA`

```c
#define PCI_CAP_ID_SATA 0x12U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

串行 ATA 数据／索引配置（Serial ATA Data/Index Configuration）。

<a id="ga20c7aadce06547a3ea37ce705ff0d289"></a>

### `PCI_CAP_ID_SECDEV`

```c
#define PCI_CAP_ID_SECDEV 0x0FU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

安全设备（Secure Device）。

<a id="gae538cdbc7eba80aac860f3340823f559"></a>

### `PCI_CAP_ID_SHPC`

```c
#define PCI_CAP_ID_SHPC 0x0CU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

PCI 标准热插拔控制器（PCI Standard Hot-Plug Controller）。

<a id="ga6d286311dd9f54468f125fd367683f74"></a>

### `PCI_CAP_ID_SLOTID`

```c
#define PCI_CAP_ID_SLOTID 0x04U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

插槽标识（Slot Identification）。

<a id="ga8814c4f32748170e8b5f15dc2ade5dc5"></a>

### `PCI_CAP_ID_SSVID`

```c
#define PCI_CAP_ID_SSVID 0x0DU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

桥接器子系统厂商／设备标识符（Bridge Subsystem Vendor/Device ID）。

<a id="ga11b65631db23369276e062560f53b433"></a>

### `PCI_CAP_ID_VNDR`

```c
#define PCI_CAP_ID_VNDR 0x09U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

厂商特定能力（Vendor-Specific）。

<a id="gaf419a56a517635f4d9f8a5c6f5fd9d08"></a>

### `PCI_CAP_ID_VPD`

```c
#define PCI_CAP_ID_VPD 0x03U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

关键产品数据（Vital Product Data，VPD）。

<a id="ga6b63b04d182b916db526525b064ed285"></a>

### `PCIE_EXT_CAP_ID_ACS`

```c
#define PCIE_EXT_CAP_ID_ACS 0x000DU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

访问控制服务（Access Control Services，ACS）。

<a id="gab8be630bf1dc810f2964e979ac46f77c"></a>

### `PCIE_EXT_CAP_ID_AMD_XXX`

```c
#define PCIE_EXT_CAP_ID_AMD_XXX 0x0014U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

保留供 AMD 使用（Reserved for AMD）。

<a id="ga53e188f6e71f04012e7739e75a015398"></a>

### `PCIE_EXT_CAP_ID_AP`

```c
#define PCIE_EXT_CAP_ID_AP 0x002BU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

替代协议（Alternate Protocol）。

<a id="gaf890e2f4f3873b60ac83df345ab0cd8f"></a>

### `PCIE_EXT_CAP_ID_ARI`

```c
#define PCIE_EXT_CAP_ID_ARI 0x000EU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

替代路由标识符解释（Alternate Routing-ID Interpretation，ARI）。

<a id="ga79a9cb071afc5cff9e699c232841623c"></a>

### `PCIE_EXT_CAP_ID_ATS`

```c
#define PCIE_EXT_CAP_ID_ATS 0x000FU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

地址转换服务（Address Translation Services，ATS）。

<a id="gaff6494cd92013933dedbab2e2ae5c6b3"></a>

### `PCIE_EXT_CAP_ID_CAC`

```c
#define PCIE_EXT_CAP_ID_CAC 0x000CU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

配置访问关联（Config Access Correlation），已废弃（Obsolete）。

<a id="ga2e8324ea3b27a63e213252bed6c78ca6"></a>

### `PCIE_EXT_CAP_ID_DLF`

```c
#define PCIE_EXT_CAP_ID_DLF 0x0025U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

数据链路功能（Data Link Feature）。

<a id="ga812c156b93d070a06d3a56b5785788fd"></a>

### `PCIE_EXT_CAP_ID_DPA`

```c
#define PCIE_EXT_CAP_ID_DPA 0x0016U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

动态功率分配（Dynamic Power Allocation）。

<a id="ga40f83a1c280acb8f3f3908d860874015"></a>

### `PCIE_EXT_CAP_ID_DPC`

```c
#define PCIE_EXT_CAP_ID_DPC 0x001DU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

下游端口故障遏制（Downstream Port Containment，DPC）。

<a id="ga29a18f51cad5281e3f6a283d3c7acb49"></a>

### `PCIE_EXT_CAP_ID_DSN`

```c
#define PCIE_EXT_CAP_ID_DSN 0x0003U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

设备序列号（Device Serial Number）。

<a id="gab1d94b05177a5064a78e4048eff473b1"></a>

### `PCIE_EXT_CAP_ID_DVSEC`

```c
#define PCIE_EXT_CAP_ID_DVSEC 0x0023U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

指定厂商特定扩展能力（Designated Vendor-Specific Extended Capability）。

<a id="ga224acf772427857ca1f5a0b155c30d63"></a>

### `PCIE_EXT_CAP_ID_ERR`

```c
#define PCIE_EXT_CAP_ID_ERR 0x0001U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

高级错误报告（Advanced Error Reporting，AER）。

<a id="ga0087a39c01053f83b3ac3bb3b057ac2a"></a>

### `PCIE_EXT_CAP_ID_HID`

```c
#define PCIE_EXT_CAP_ID_HID 0x0028U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

层次结构标识符（Hierarchy ID）。

<a id="ga3006998c35d9c8f8e3d69716cda6def7"></a>

### `PCIE_EXT_CAP_ID_L1SS`

```c
#define PCIE_EXT_CAP_ID_L1SS 0x001EU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

L1 电源管理子状态（L1 PM Substates）。

<a id="ga56b3b2bd686b6b99c2ae34ae57228160"></a>

### `PCIE_EXT_CAP_ID_LMR`

```c
#define PCIE_EXT_CAP_ID_LMR 0x0027U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

接收端通道裕量测量（Lane Margining at the Receiver）。

<a id="ga9545f09c97f2dd4f751767e6e54326ec"></a>

### `PCIE_EXT_CAP_ID_LTR`

```c
#define PCIE_EXT_CAP_ID_LTR 0x0018U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

延迟容忍度报告（Latency Tolerance Reporting）。

<a id="ga2810671833871608043e6e910d79dffd"></a>

### `PCIE_EXT_CAP_ID_MCAST`

```c
#define PCIE_EXT_CAP_ID_MCAST 0x0012U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

组播（Multicast）。

<a id="ga2cfa2f9212fb923c3811c0cdc769a877"></a>

### `PCIE_EXT_CAP_ID_MFVC`

```c
#define PCIE_EXT_CAP_ID_MFVC 0x0008U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

多功能虚拟通道能力（Multi-Function VC Capability，MFVC）。

<a id="ga7c2b491e1c994730afe08880dfb1b036"></a>

### `PCIE_EXT_CAP_ID_MFVC_VC`

```c
#define PCIE_EXT_CAP_ID_MFVC_VC 0x0009U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

与多功能虚拟通道（MFVC）配合使用的虚拟通道（Virtual Channel）。

<a id="gaa117a86f2691d8711fa6b70e196ead01"></a>

### `PCIE_EXT_CAP_ID_MRIOV`

```c
#define PCIE_EXT_CAP_ID_MRIOV 0x0011U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

多根输入／输出虚拟化（Multi Root I/O Virtualization，MR-IOV）。

<a id="ga03dafb2eb5449f17dc18898ea319d729"></a>

### `PCIE_EXT_CAP_ID_NPEM`

```c
#define PCIE_EXT_CAP_ID_NPEM 0x0029U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

原生 PCIe 机箱管理（Native PCIe Enclosure Management）。

<a id="ga2f6c4feb384e41711aa53545952e3cac"></a>

### `PCIE_EXT_CAP_ID_NULL`

```c
#define PCIE_EXT_CAP_ID_NULL 0x0000U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

空能力（Null Capability）。

<a id="ga0c3b5efb8d9fb69a8fdbb9ca147a3069"></a>

### `PCIE_EXT_CAP_ID_PASID`

```c
#define PCIE_EXT_CAP_ID_PASID 0x001BU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

进程地址空间标识符（Process Address Space ID，PASID）。

<a id="ga60203711f9fe698f3e7e138e0468645a"></a>

### `PCIE_EXT_CAP_ID_PL_16GT`

```c
#define PCIE_EXT_CAP_ID_PL_16GT 0x0026U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

16.0 GT/s 物理层（Physical Layer）。

<a id="ga8a8768d04866a479114bcf276466501f"></a>

### `PCIE_EXT_CAP_ID_PL_32GT`

```c
#define PCIE_EXT_CAP_ID_PL_32GT 0x002AU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

32.0 GT/s 物理层（Physical Layer）。

<a id="gaf6c41b4ad9e32c4420cb89cc5a0d51c2"></a>

### `PCIE_EXT_CAP_ID_PMUX`

```c
#define PCIE_EXT_CAP_ID_PMUX 0x001AU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

协议复用（Protocol Multiplexing）。

<a id="ga37e0ac002e9742bb9177588d2dfa850b"></a>

### `PCIE_EXT_CAP_ID_PRI`

```c
#define PCIE_EXT_CAP_ID_PRI 0x0013U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

页面请求接口（Page Request Interface）。

<a id="ga134d53764458500ea4ca58fe016f46fa"></a>

### `PCIE_EXT_CAP_ID_PTM`

```c
#define PCIE_EXT_CAP_ID_PTM 0x001FU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

精确时间测量（Precision Time Measurement）。

<a id="gadc91da3b61af0b0a047ec74860dc3201"></a>

### `PCIE_EXT_CAP_ID_PWR`

```c
#define PCIE_EXT_CAP_ID_PWR 0x0004U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

功率预算（Power Budgeting）。

<a id="ga78b98a43b8e6661d6745df19c8591f47"></a>

### `PCIE_EXT_CAP_ID_RCEC`

```c
#define PCIE_EXT_CAP_ID_RCEC 0x0007U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

根复合体事件收集器端点关联（Root Complex Event Collector Endpoint Association）。

<a id="ga973a2816ae68ab75d5b4118890fd4383"></a>

### `PCIE_EXT_CAP_ID_RCILC`

```c
#define PCIE_EXT_CAP_ID_RCILC 0x0006U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

根复合体内部链路控制（Root Complex Internal Link Control）。

<a id="ga46f3607fa47b26ef099f9bfdcdb0763f"></a>

### `PCIE_EXT_CAP_ID_RCLD`

```c
#define PCIE_EXT_CAP_ID_RCLD 0x0005U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

根复合体链路声明（Root Complex Link Declaration）。

<a id="ga356973ae03fb0d33df4092a311818e9b"></a>

### `PCIE_EXT_CAP_ID_RCRB`

```c
#define PCIE_EXT_CAP_ID_RCRB 0x000AU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

根复合体寄存器块（Root Complex Register Block）。

<a id="gabae7e5d40435723e6d808c377753332a"></a>

### `PCIE_EXT_CAP_ID_REBAR`

```c
#define PCIE_EXT_CAP_ID_REBAR 0x0015U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

可调整大小的基地址寄存器（Resizable BAR）。

<a id="gacd1a90cce3892bacc40939a04b707d20"></a>

### `PCIE_EXT_CAP_ID_SECPCI`

```c
#define PCIE_EXT_CAP_ID_SECPCI 0x0019U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

次级 PCIe 能力（Secondary PCIe Capability）。

<a id="ga0e173611874d25c0cd5bd62372542380"></a>

### `PCIE_EXT_CAP_ID_SFI`

```c
#define PCIE_EXT_CAP_ID_SFI 0x002CU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

系统固件中介（System Firmware Intermediary）。

<a id="gae8767a1dd6e203aa2ccd75d1fd05eb7d"></a>

### `PCIE_EXT_CAP_ID_SRIOV`

```c
#define PCIE_EXT_CAP_ID_SRIOV 0x0010U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

单根输入／输出虚拟化（Single Root I/O Virtualization，SR-IOV）。

<a id="ga558289987600691fce5574feb253b4cb"></a>

### `PCIE_EXT_CAP_ID_TPH`

```c
#define PCIE_EXT_CAP_ID_TPH 0x0017U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

TPH 请求方（TPH Requester）。

<a id="gaaa8d5de1c1925dea16e40b72fafa5b8f"></a>

### `PCIE_EXT_CAP_ID_VC`

```c
#define PCIE_EXT_CAP_ID_VC 0x0002U
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

不使用多功能虚拟通道（MFVC）时的虚拟通道（Virtual Channel）。

<a id="gac864550f144038d5bbdf5e556faa640e"></a>

### `PCIE_EXT_CAP_ID_VNDR`

```c
#define PCIE_EXT_CAP_ID_VNDR 0x000BU
```

```c
#include <zephyr/drivers/pcie/cap.h>
```

厂商特定扩展能力（Vendor-Specific Extended Capability）。


## 6.4\_原页交叉引用（Cross References）

- [zephyr/drivers/pcie/cap.h](../api_file_network_pcie_reference/P001_zephyr__drivers__pcie__cap.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_LSM6DSVXXX API主题.md) · [返回大纲](大纲.md) · [下一章](P007_安全数字主机控制器（SDHC）.md)
