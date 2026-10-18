---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-1
title: zephyr__drivers__pcie__cap.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2cap_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_drivers\_\_pcie\_\_cap.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2cap_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCIe能力（Capabilities）。

查看此文件的源码。

<a id="details"></a>

PCIe能力（Capabilities）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="define-members-0"></a>

### PCI 与 PCI Express 能力（PCI & PCI Express Capabilities）

取自《PCI 代码与标识符分配规范》（PCI Code and ID Assignment Specification）修订版 1.11。

<a id="r_ga890142bda671b3558cd881f4b91a43ab"></a>

```c
#define PCI_CAP_ID_NULL 0x00U
```

相关声明：[PCI_CAP_ID_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga890142bda671b3558cd881f4b91a43ab)。

空能力（Null Capability）。

<a id="r_ga9379bf318dd400e1076fbd5f0e331adb"></a>

```c
#define PCI_CAP_ID_PM 0x01U
```

相关声明：[PCI_CAP_ID_PM](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga9379bf318dd400e1076fbd5f0e331adb)。

电源管理（Power Management）。

<a id="r_gac68c228e23e701fd4040b89c42537eac"></a>

```c
#define PCI_CAP_ID_AGP 0x02U
```

相关声明：[PCI_CAP_ID_AGP](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gac68c228e23e701fd4040b89c42537eac)。

加速图形端口（Accelerated Graphics Port，AGP）。

<a id="r_gaf419a56a517635f4d9f8a5c6f5fd9d08"></a>

```c
#define PCI_CAP_ID_VPD 0x03U
```

相关声明：[PCI_CAP_ID_VPD](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gaf419a56a517635f4d9f8a5c6f5fd9d08)。

关键产品数据（Vital Product Data，VPD）。

<a id="r_ga6d286311dd9f54468f125fd367683f74"></a>

```c
#define PCI_CAP_ID_SLOTID 0x04U
```

相关声明：[PCI_CAP_ID_SLOTID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga6d286311dd9f54468f125fd367683f74)。

插槽标识（Slot Identification）。

<a id="r_gad19597699011d0e047083968d2e835bd"></a>

```c
#define PCI_CAP_ID_MSI 0x05U
```

相关声明：[PCI_CAP_ID_MSI](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gad19597699011d0e047083968d2e835bd)。

消息信号中断（Message Signalled Interrupts，MSI）。

<a id="r_ga74356319083570ca7e5cf9a3eaaadd9b"></a>

```c
#define PCI_CAP_ID_CHSWP 0x06U
```

相关声明：[PCI_CAP_ID_CHSWP](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga74356319083570ca7e5cf9a3eaaadd9b)。

CompactPCI 热插拔（HotSwap）。

<a id="r_ga24709fe61430ca25fabe665d8b1efca0"></a>

```c
#define PCI_CAP_ID_PCIX 0x07U
```

相关声明：[PCI_CAP_ID_PCIX](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga24709fe61430ca25fabe665d8b1efca0)。

PCI-X。

<a id="r_gad50ed1a81153a04fa19534823d0109c9"></a>

```c
#define PCI_CAP_ID_HT 0x08U
```

相关声明：[PCI_CAP_ID_HT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gad50ed1a81153a04fa19534823d0109c9)。

HyperTransport。

<a id="r_ga11b65631db23369276e062560f53b433"></a>

```c
#define PCI_CAP_ID_VNDR 0x09U
```

相关声明：[PCI_CAP_ID_VNDR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga11b65631db23369276e062560f53b433)。

厂商特定能力（Vendor-Specific）。

<a id="r_ga5a37d779c6259232cd4ec7bc3d80bc83"></a>

```c
#define PCI_CAP_ID_DBG 0x0AU
```

相关声明：[PCI_CAP_ID_DBG](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga5a37d779c6259232cd4ec7bc3d80bc83)。

调试端口（Debug Port）。

<a id="r_gad45dfbc6ea8d963703e243dacdee084f"></a>

```c
#define PCI_CAP_ID_CCRC 0x0BU
```

相关声明：[PCI_CAP_ID_CCRC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gad45dfbc6ea8d963703e243dacdee084f)。

CompactPCI 中央资源控制（Central Resource Control）。

<a id="r_gae538cdbc7eba80aac860f3340823f559"></a>

```c
#define PCI_CAP_ID_SHPC 0x0CU
```

相关声明：[PCI_CAP_ID_SHPC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gae538cdbc7eba80aac860f3340823f559)。

PCI 标准热插拔控制器（PCI Standard Hot-Plug Controller）。

<a id="r_ga8814c4f32748170e8b5f15dc2ade5dc5"></a>

```c
#define PCI_CAP_ID_SSVID 0x0DU
```

相关声明：[PCI_CAP_ID_SSVID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga8814c4f32748170e8b5f15dc2ade5dc5)。

桥接器子系统厂商／设备标识符（Bridge Subsystem Vendor/Device ID）。

<a id="r_gae351b2497f7231bfa2c08e97ba589cb7"></a>

```c
#define PCI_CAP_ID_AGP3 0x0EU
```

相关声明：[PCI_CAP_ID_AGP3](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gae351b2497f7231bfa2c08e97ba589cb7)。

AGP 8x。

<a id="r_ga20c7aadce06547a3ea37ce705ff0d289"></a>

```c
#define PCI_CAP_ID_SECDEV 0x0FU
```

相关声明：[PCI_CAP_ID_SECDEV](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga20c7aadce06547a3ea37ce705ff0d289)。

安全设备（Secure Device）。

<a id="r_ga9b0efbb129a8600203135a64377beed0"></a>

```c
#define PCI_CAP_ID_EXP 0x10U
```

相关声明：[PCI_CAP_ID_EXP](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga9b0efbb129a8600203135a64377beed0)。

PCI Express。

<a id="r_ga419307c3f83f3dca9aaa329de41dae63"></a>

```c
#define PCI_CAP_ID_MSIX 0x11U
```

相关声明：[PCI_CAP_ID_MSIX](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga419307c3f83f3dca9aaa329de41dae63)。

MSI-X。

<a id="r_ga437d2f840145a2aae97880ad3579ca7d"></a>

```c
#define PCI_CAP_ID_SATA 0x12U
```

相关声明：[PCI_CAP_ID_SATA](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga437d2f840145a2aae97880ad3579ca7d)。

串行 ATA 数据／索引配置（Serial ATA Data/Index Configuration）。

<a id="r_ga7bf330224972c1a16cbafa907387b9ed"></a>

```c
#define PCI_CAP_ID_AF 0x13U
```

相关声明：[PCI_CAP_ID_AF](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga7bf330224972c1a16cbafa907387b9ed)。

PCI 高级功能（PCI Advanced Features）。

<a id="r_ga591d30c052c32a4f3cbb510e8b052b62"></a>

```c
#define PCI_CAP_ID_EA 0x14U
```

相关声明：[PCI_CAP_ID_EA](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga591d30c052c32a4f3cbb510e8b052b62)。

PCI 增强分配（PCI Enhanced Allocation）。

<a id="r_gad00f421c7bc8613ad7770ea2e0a5d8da"></a>

```c
#define PCI_CAP_ID_FPB 0x14U
```

相关声明：[PCI_CAP_ID_FPB](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gad00f421c7bc8613ad7770ea2e0a5d8da)。

展平门户桥（Flattening Portal Bridge）。

<a id="define-members-1"></a>

### PCI Express 扩展能力（PCI Express Extended Capabilities）

<a id="r_ga2f6c4feb384e41711aa53545952e3cac"></a>

```c
#define PCIE_EXT_CAP_ID_NULL 0x0000U
```

相关声明：[PCIE_EXT_CAP_ID_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga2f6c4feb384e41711aa53545952e3cac)。

空能力（Null Capability）。

<a id="r_ga224acf772427857ca1f5a0b155c30d63"></a>

```c
#define PCIE_EXT_CAP_ID_ERR 0x0001U
```

相关声明：[PCIE_EXT_CAP_ID_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga224acf772427857ca1f5a0b155c30d63)。

高级错误报告（Advanced Error Reporting，AER）。

<a id="r_gaaa8d5de1c1925dea16e40b72fafa5b8f"></a>

```c
#define PCIE_EXT_CAP_ID_VC 0x0002U
```

相关声明：[PCIE_EXT_CAP_ID_VC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gaaa8d5de1c1925dea16e40b72fafa5b8f)。

不使用多功能虚拟通道（MFVC）时的虚拟通道（Virtual Channel）。

<a id="r_ga29a18f51cad5281e3f6a283d3c7acb49"></a>

```c
#define PCIE_EXT_CAP_ID_DSN 0x0003U
```

相关声明：[PCIE_EXT_CAP_ID_DSN](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga29a18f51cad5281e3f6a283d3c7acb49)。

设备序列号（Device Serial Number）。

<a id="r_gadc91da3b61af0b0a047ec74860dc3201"></a>

```c
#define PCIE_EXT_CAP_ID_PWR 0x0004U
```

相关声明：[PCIE_EXT_CAP_ID_PWR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gadc91da3b61af0b0a047ec74860dc3201)。

功率预算（Power Budgeting）。

<a id="r_ga46f3607fa47b26ef099f9bfdcdb0763f"></a>

```c
#define PCIE_EXT_CAP_ID_RCLD 0x0005U
```

相关声明：[PCIE_EXT_CAP_ID_RCLD](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga46f3607fa47b26ef099f9bfdcdb0763f)。

根复合体链路声明（Root Complex Link Declaration）。

<a id="r_ga973a2816ae68ab75d5b4118890fd4383"></a>

```c
#define PCIE_EXT_CAP_ID_RCILC 0x0006U
```

相关声明：[PCIE_EXT_CAP_ID_RCILC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga973a2816ae68ab75d5b4118890fd4383)。

根复合体内部链路控制（Root Complex Internal Link Control）。

<a id="r_ga78b98a43b8e6661d6745df19c8591f47"></a>

```c
#define PCIE_EXT_CAP_ID_RCEC 0x0007U
```

相关声明：[PCIE_EXT_CAP_ID_RCEC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga78b98a43b8e6661d6745df19c8591f47)。

根复合体事件收集器端点关联（Root Complex Event Collector Endpoint Association）。

<a id="r_ga2cfa2f9212fb923c3811c0cdc769a877"></a>

```c
#define PCIE_EXT_CAP_ID_MFVC 0x0008U
```

相关声明：[PCIE_EXT_CAP_ID_MFVC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga2cfa2f9212fb923c3811c0cdc769a877)。

多功能虚拟通道能力（Multi-Function VC Capability，MFVC）。

<a id="r_ga7c2b491e1c994730afe08880dfb1b036"></a>

```c
#define PCIE_EXT_CAP_ID_MFVC_VC 0x0009U
```

相关声明：[PCIE_EXT_CAP_ID_MFVC_VC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga7c2b491e1c994730afe08880dfb1b036)。

与多功能虚拟通道（MFVC）配合使用的虚拟通道（Virtual Channel）。

<a id="r_ga356973ae03fb0d33df4092a311818e9b"></a>

```c
#define PCIE_EXT_CAP_ID_RCRB 0x000AU
```

相关声明：[PCIE_EXT_CAP_ID_RCRB](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga356973ae03fb0d33df4092a311818e9b)。

根复合体寄存器块（Root Complex Register Block）。

<a id="r_gac864550f144038d5bbdf5e556faa640e"></a>

```c
#define PCIE_EXT_CAP_ID_VNDR 0x000BU
```

相关声明：[PCIE_EXT_CAP_ID_VNDR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gac864550f144038d5bbdf5e556faa640e)。

厂商特定扩展能力（Vendor-Specific Extended Capability）。

<a id="r_gaff6494cd92013933dedbab2e2ae5c6b3"></a>

```c
#define PCIE_EXT_CAP_ID_CAC 0x000CU
```

相关声明：[PCIE_EXT_CAP_ID_CAC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gaff6494cd92013933dedbab2e2ae5c6b3)。

配置访问关联（Config Access Correlation），已废弃（Obsolete）。

<a id="r_ga6b63b04d182b916db526525b064ed285"></a>

```c
#define PCIE_EXT_CAP_ID_ACS 0x000DU
```

相关声明：[PCIE_EXT_CAP_ID_ACS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga6b63b04d182b916db526525b064ed285)。

访问控制服务（Access Control Services，ACS）。

<a id="r_gaf890e2f4f3873b60ac83df345ab0cd8f"></a>

```c
#define PCIE_EXT_CAP_ID_ARI 0x000EU
```

相关声明：[PCIE_EXT_CAP_ID_ARI](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gaf890e2f4f3873b60ac83df345ab0cd8f)。

替代路由标识符解释（Alternate Routing-ID Interpretation，ARI）。

<a id="r_ga79a9cb071afc5cff9e699c232841623c"></a>

```c
#define PCIE_EXT_CAP_ID_ATS 0x000FU
```

相关声明：[PCIE_EXT_CAP_ID_ATS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga79a9cb071afc5cff9e699c232841623c)。

地址转换服务（Address Translation Services，ATS）。

<a id="r_gae8767a1dd6e203aa2ccd75d1fd05eb7d"></a>

```c
#define PCIE_EXT_CAP_ID_SRIOV 0x0010U
```

相关声明：[PCIE_EXT_CAP_ID_SRIOV](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gae8767a1dd6e203aa2ccd75d1fd05eb7d)。

单根输入／输出虚拟化（Single Root I/O Virtualization，SR-IOV）。

<a id="r_gaa117a86f2691d8711fa6b70e196ead01"></a>

```c
#define PCIE_EXT_CAP_ID_MRIOV 0x0011U
```

相关声明：[PCIE_EXT_CAP_ID_MRIOV](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gaa117a86f2691d8711fa6b70e196ead01)。

多根输入／输出虚拟化（Multi Root I/O Virtualization，MR-IOV）。

<a id="r_ga2810671833871608043e6e910d79dffd"></a>

```c
#define PCIE_EXT_CAP_ID_MCAST 0x0012U
```

相关声明：[PCIE_EXT_CAP_ID_MCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga2810671833871608043e6e910d79dffd)。

组播（Multicast）。

<a id="r_ga37e0ac002e9742bb9177588d2dfa850b"></a>

```c
#define PCIE_EXT_CAP_ID_PRI 0x0013U
```

相关声明：[PCIE_EXT_CAP_ID_PRI](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga37e0ac002e9742bb9177588d2dfa850b)。

页面请求接口（Page Request Interface）。

<a id="r_gab8be630bf1dc810f2964e979ac46f77c"></a>

```c
#define PCIE_EXT_CAP_ID_AMD_XXX 0x0014U
```

相关声明：[PCIE_EXT_CAP_ID_AMD_XXX](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gab8be630bf1dc810f2964e979ac46f77c)。

保留供 AMD 使用（Reserved for AMD）。

<a id="r_gabae7e5d40435723e6d808c377753332a"></a>

```c
#define PCIE_EXT_CAP_ID_REBAR 0x0015U
```

相关声明：[PCIE_EXT_CAP_ID_REBAR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gabae7e5d40435723e6d808c377753332a)。

可调整大小的基地址寄存器（Resizable BAR）。

<a id="r_ga812c156b93d070a06d3a56b5785788fd"></a>

```c
#define PCIE_EXT_CAP_ID_DPA 0x0016U
```

相关声明：[PCIE_EXT_CAP_ID_DPA](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga812c156b93d070a06d3a56b5785788fd)。

动态功率分配（Dynamic Power Allocation）。

<a id="r_ga558289987600691fce5574feb253b4cb"></a>

```c
#define PCIE_EXT_CAP_ID_TPH 0x0017U
```

相关声明：[PCIE_EXT_CAP_ID_TPH](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga558289987600691fce5574feb253b4cb)。

TPH 请求方（TPH Requester）。

<a id="r_ga9545f09c97f2dd4f751767e6e54326ec"></a>

```c
#define PCIE_EXT_CAP_ID_LTR 0x0018U
```

相关声明：[PCIE_EXT_CAP_ID_LTR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga9545f09c97f2dd4f751767e6e54326ec)。

延迟容忍度报告（Latency Tolerance Reporting）。

<a id="r_gacd1a90cce3892bacc40939a04b707d20"></a>

```c
#define PCIE_EXT_CAP_ID_SECPCI 0x0019U
```

相关声明：[PCIE_EXT_CAP_ID_SECPCI](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gacd1a90cce3892bacc40939a04b707d20)。

次级 PCIe 能力（Secondary PCIe Capability）。

<a id="r_gaf6c41b4ad9e32c4420cb89cc5a0d51c2"></a>

```c
#define PCIE_EXT_CAP_ID_PMUX 0x001AU
```

相关声明：[PCIE_EXT_CAP_ID_PMUX](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gaf6c41b4ad9e32c4420cb89cc5a0d51c2)。

协议复用（Protocol Multiplexing）。

<a id="r_ga0c3b5efb8d9fb69a8fdbb9ca147a3069"></a>

```c
#define PCIE_EXT_CAP_ID_PASID 0x001BU
```

相关声明：[PCIE_EXT_CAP_ID_PASID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga0c3b5efb8d9fb69a8fdbb9ca147a3069)。

进程地址空间标识符（Process Address Space ID，PASID）。

<a id="r_ga40f83a1c280acb8f3f3908d860874015"></a>

```c
#define PCIE_EXT_CAP_ID_DPC 0x001DU
```

相关声明：[PCIE_EXT_CAP_ID_DPC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga40f83a1c280acb8f3f3908d860874015)。

下游端口故障遏制（Downstream Port Containment，DPC）。

<a id="r_ga3006998c35d9c8f8e3d69716cda6def7"></a>

```c
#define PCIE_EXT_CAP_ID_L1SS 0x001EU
```

相关声明：[PCIE_EXT_CAP_ID_L1SS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga3006998c35d9c8f8e3d69716cda6def7)。

L1 电源管理子状态（L1 PM Substates）。

<a id="r_ga134d53764458500ea4ca58fe016f46fa"></a>

```c
#define PCIE_EXT_CAP_ID_PTM 0x001FU
```

相关声明：[PCIE_EXT_CAP_ID_PTM](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga134d53764458500ea4ca58fe016f46fa)。

精确时间测量（Precision Time Measurement）。

<a id="r_gab1d94b05177a5064a78e4048eff473b1"></a>

```c
#define PCIE_EXT_CAP_ID_DVSEC 0x0023U
```

相关声明：[PCIE_EXT_CAP_ID_DVSEC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gab1d94b05177a5064a78e4048eff473b1)。

指定厂商特定扩展能力（Designated Vendor-Specific Extended Capability）。

<a id="r_ga2e8324ea3b27a63e213252bed6c78ca6"></a>

```c
#define PCIE_EXT_CAP_ID_DLF 0x0025U
```

相关声明：[PCIE_EXT_CAP_ID_DLF](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga2e8324ea3b27a63e213252bed6c78ca6)。

数据链路功能（Data Link Feature）。

<a id="r_ga60203711f9fe698f3e7e138e0468645a"></a>

```c
#define PCIE_EXT_CAP_ID_PL_16GT 0x0026U
```

相关声明：[PCIE_EXT_CAP_ID_PL_16GT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga60203711f9fe698f3e7e138e0468645a)。

16.0 GT/s 物理层（Physical Layer）。

<a id="r_ga56b3b2bd686b6b99c2ae34ae57228160"></a>

```c
#define PCIE_EXT_CAP_ID_LMR 0x0027U
```

相关声明：[PCIE_EXT_CAP_ID_LMR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga56b3b2bd686b6b99c2ae34ae57228160)。

接收端通道裕量测量（Lane Margining at the Receiver）。

<a id="r_ga0087a39c01053f83b3ac3bb3b057ac2a"></a>

```c
#define PCIE_EXT_CAP_ID_HID 0x0028U
```

相关声明：[PCIE_EXT_CAP_ID_HID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga0087a39c01053f83b3ac3bb3b057ac2a)。

层次结构标识符（Hierarchy ID）。

<a id="r_ga03dafb2eb5449f17dc18898ea319d729"></a>

```c
#define PCIE_EXT_CAP_ID_NPEM 0x0029U
```

相关声明：[PCIE_EXT_CAP_ID_NPEM](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga03dafb2eb5449f17dc18898ea319d729)。

原生 PCIe 机箱管理（Native PCIe Enclosure Management）。

<a id="r_ga8a8768d04866a479114bcf276466501f"></a>

```c
#define PCIE_EXT_CAP_ID_PL_32GT 0x002AU
```

相关声明：[PCIE_EXT_CAP_ID_PL_32GT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga8a8768d04866a479114bcf276466501f)。

32.0 GT/s 物理层（Physical Layer）。

<a id="r_ga53e188f6e71f04012e7739e75a015398"></a>

```c
#define PCIE_EXT_CAP_ID_AP 0x002BU
```

相关声明：[PCIE_EXT_CAP_ID_AP](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga53e188f6e71f04012e7739e75a015398)。

替代协议（Alternate Protocol）。

<a id="r_ga0e173611874d25c0cd5bd62372542380"></a>

```c
#define PCIE_EXT_CAP_ID_SFI 0x002CU
```

相关声明：[PCIE_EXT_CAP_ID_SFI](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga0e173611874d25c0cd5bd62372542380)。

系统固件中介（System Firmware Intermediary）。


## 1.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P168_cap.h_源码浏览.md)
- [PCI_CAP_ID_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga890142bda671b3558cd881f4b91a43ab)
- [PCI_CAP_ID_PM](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga9379bf318dd400e1076fbd5f0e331adb)
- [PCI_CAP_ID_AGP](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gac68c228e23e701fd4040b89c42537eac)
- [PCI_CAP_ID_VPD](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gaf419a56a517635f4d9f8a5c6f5fd9d08)
- [PCI_CAP_ID_SLOTID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga6d286311dd9f54468f125fd367683f74)
- [PCI_CAP_ID_MSI](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gad19597699011d0e047083968d2e835bd)
- [PCI_CAP_ID_CHSWP](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga74356319083570ca7e5cf9a3eaaadd9b)
- [PCI_CAP_ID_PCIX](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga24709fe61430ca25fabe665d8b1efca0)
- [PCI_CAP_ID_HT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gad50ed1a81153a04fa19534823d0109c9)
- [PCI_CAP_ID_VNDR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga11b65631db23369276e062560f53b433)
- [PCI_CAP_ID_DBG](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga5a37d779c6259232cd4ec7bc3d80bc83)
- [PCI_CAP_ID_CCRC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gad45dfbc6ea8d963703e243dacdee084f)
- [PCI_CAP_ID_SHPC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gae538cdbc7eba80aac860f3340823f559)
- [PCI_CAP_ID_SSVID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga8814c4f32748170e8b5f15dc2ade5dc5)
- [PCI_CAP_ID_AGP3](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gae351b2497f7231bfa2c08e97ba589cb7)
- [PCI_CAP_ID_SECDEV](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga20c7aadce06547a3ea37ce705ff0d289)
- [PCI_CAP_ID_EXP](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga9b0efbb129a8600203135a64377beed0)
- [PCI_CAP_ID_MSIX](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga419307c3f83f3dca9aaa329de41dae63)
- [PCI_CAP_ID_SATA](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga437d2f840145a2aae97880ad3579ca7d)
- [PCI_CAP_ID_AF](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga7bf330224972c1a16cbafa907387b9ed)
- [PCI_CAP_ID_EA](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga591d30c052c32a4f3cbb510e8b052b62)
- [PCI_CAP_ID_FPB](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gad00f421c7bc8613ad7770ea2e0a5d8da)
- [PCIE_EXT_CAP_ID_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga2f6c4feb384e41711aa53545952e3cac)
- [PCIE_EXT_CAP_ID_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga224acf772427857ca1f5a0b155c30d63)
- [PCIE_EXT_CAP_ID_VC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gaaa8d5de1c1925dea16e40b72fafa5b8f)
- [PCIE_EXT_CAP_ID_DSN](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga29a18f51cad5281e3f6a283d3c7acb49)
- [PCIE_EXT_CAP_ID_PWR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gadc91da3b61af0b0a047ec74860dc3201)
- [PCIE_EXT_CAP_ID_RCLD](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga46f3607fa47b26ef099f9bfdcdb0763f)
- [PCIE_EXT_CAP_ID_RCILC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga973a2816ae68ab75d5b4118890fd4383)
- [PCIE_EXT_CAP_ID_RCEC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga78b98a43b8e6661d6745df19c8591f47)
- [PCIE_EXT_CAP_ID_MFVC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga2cfa2f9212fb923c3811c0cdc769a877)
- [PCIE_EXT_CAP_ID_MFVC_VC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga7c2b491e1c994730afe08880dfb1b036)
- [PCIE_EXT_CAP_ID_RCRB](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga356973ae03fb0d33df4092a311818e9b)
- [PCIE_EXT_CAP_ID_VNDR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gac864550f144038d5bbdf5e556faa640e)
- [PCIE_EXT_CAP_ID_CAC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gaff6494cd92013933dedbab2e2ae5c6b3)
- [PCIE_EXT_CAP_ID_ACS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga6b63b04d182b916db526525b064ed285)
- [PCIE_EXT_CAP_ID_ARI](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gaf890e2f4f3873b60ac83df345ab0cd8f)
- [PCIE_EXT_CAP_ID_ATS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga79a9cb071afc5cff9e699c232841623c)
- [PCIE_EXT_CAP_ID_SRIOV](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gae8767a1dd6e203aa2ccd75d1fd05eb7d)
- [PCIE_EXT_CAP_ID_MRIOV](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gaa117a86f2691d8711fa6b70e196ead01)
- [PCIE_EXT_CAP_ID_MCAST](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga2810671833871608043e6e910d79dffd)
- [PCIE_EXT_CAP_ID_PRI](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga37e0ac002e9742bb9177588d2dfa850b)
- [PCIE_EXT_CAP_ID_AMD_XXX](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gab8be630bf1dc810f2964e979ac46f77c)
- [PCIE_EXT_CAP_ID_REBAR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gabae7e5d40435723e6d808c377753332a)
- [PCIE_EXT_CAP_ID_DPA](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga812c156b93d070a06d3a56b5785788fd)
- [PCIE_EXT_CAP_ID_TPH](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga558289987600691fce5574feb253b4cb)
- [PCIE_EXT_CAP_ID_LTR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga9545f09c97f2dd4f751767e6e54326ec)
- [PCIE_EXT_CAP_ID_SECPCI](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gacd1a90cce3892bacc40939a04b707d20)
- [PCIE_EXT_CAP_ID_PMUX](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gaf6c41b4ad9e32c4420cb89cc5a0d51c2)
- [PCIE_EXT_CAP_ID_PASID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga0c3b5efb8d9fb69a8fdbb9ca147a3069)
- [PCIE_EXT_CAP_ID_DPC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga40f83a1c280acb8f3f3908d860874015)
- [PCIE_EXT_CAP_ID_L1SS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga3006998c35d9c8f8e3d69716cda6def7)
- [PCIE_EXT_CAP_ID_PTM](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga134d53764458500ea4ca58fe016f46fa)
- [PCIE_EXT_CAP_ID_DVSEC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#gab1d94b05177a5064a78e4048eff473b1)
- [PCIE_EXT_CAP_ID_DLF](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga2e8324ea3b27a63e213252bed6c78ca6)
- [PCIE_EXT_CAP_ID_PL_16GT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga60203711f9fe698f3e7e138e0468645a)
- [PCIE_EXT_CAP_ID_LMR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga56b3b2bd686b6b99c2ae34ae57228160)
- [PCIE_EXT_CAP_ID_HID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga0087a39c01053f83b3ac3bb3b057ac2a)
- [PCIE_EXT_CAP_ID_NPEM](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga03dafb2eb5449f17dc18898ea319d729)
- [PCIE_EXT_CAP_ID_PL_32GT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga8a8768d04866a479114bcf276466501f)
- [PCIE_EXT_CAP_ID_AP](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga53e188f6e71f04012e7739e75a015398)
- [PCIE_EXT_CAP_ID_SFI](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html#ga0e173611874d25c0cd5bd62372542380)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__sensor__lsm6dsvxxx.h_文件参考.md)
