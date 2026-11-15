---
id: learning.zephyr-docs.api-file-kernel-network-reference.page-11
title: zephyr__drivers__interrupt_controller__riscv_aplic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_riscv\_aplic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RISC-V高级平台级中断控制器（Advanced Platform-Level Interrupt Controller，APLIC）的驱动API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/types.h>
```

查看此文件的源码。

RISC-V 高级平台级中断控制器（Advanced Platform-Level Interrupt Controller，APLIC）驱动 API。本头文件提供 RISC-V APLIC 的 API 和寄存器定义。APLIC 是 RISC-V 高级中断架构（Advanced Interrupt Architecture，AIA）的一部分，同时支持消息信号中断（MSI）和直接投递（Direct Delivery）模式。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="define-members-0"></a>

### APLIC 寄存器偏移量（APLIC Register Offsets）

高级中断架构（AIA）规范定义的 APLIC 寄存器偏移量（Register Offsets）。

<a id="r_a3f7c50560007001d1b22e5ac86a4dd3b"></a>

```c
#define APLIC_DOMAINCFG 0x0000
```

相关声明：[APLIC_DOMAINCFG](#a3f7c50560007001d1b22e5ac86a4dd3b)。

域配置寄存器（Domain Configuration Register）的偏移量。

<a id="r_a66c8ea9cb1891e48b537a663579e56aa"></a>

```c
#define APLIC_SOURCECFG_BASE 0x0004
```

相关声明：[APLIC_SOURCECFG_BASE](#a66c8ea9cb1891e48b537a663579e56aa)。

源配置寄存器（Source Configuration Registers）的基偏移量。

<a id="r_a8fe43db0a39481cfbc7fc26d5b201527"></a>

```c
#define APLIC_SETIP_BASE 0x1C00
```

相关声明：[APLIC_SETIP_BASE](#a8fe43db0a39481cfbc7fc26d5b201527)。

设置中断待处理位图（Set Interrupt Pending Bitmap）的基偏移量。

<a id="r_a900aa5210c8feee01c478ca70226af66"></a>

```c
#define APLIC_SETIPNUM 0x1CDC
```

相关声明：[APLIC_SETIPNUM](#a900aa5210c8feee01c478ca70226af66)。

按编号设置中断待处理状态寄存器（Set Interrupt Pending by Number Register）的偏移量。

<a id="r_aaded0cb41afa0352eaab7b0e77675a17"></a>

```c
#define APLIC_CLRIP_BASE 0x1D00
```

相关声明：[APLIC_CLRIP_BASE](#aaded0cb41afa0352eaab7b0e77675a17)。

清除中断待处理位图（Clear Interrupt Pending Bitmap）的基偏移量。

<a id="r_a8b030a6341030491354ed6f600631953"></a>

```c
#define APLIC_CLRIPNUM 0x1DDC
```

相关声明：[APLIC_CLRIPNUM](#a8b030a6341030491354ed6f600631953)。

按编号清除中断待处理状态寄存器（Clear Interrupt Pending by Number Register）的偏移量。

<a id="r_ae024fd41ba913c13e535d10c4adc5d96"></a>

```c
#define APLIC_SETIE_BASE 0x1E00
```

相关声明：[APLIC_SETIE_BASE](#ae024fd41ba913c13e535d10c4adc5d96)。

设置中断使能位图（Set Interrupt Enable Bitmap）的基偏移量。

<a id="r_af5b29f5437042e0dc896403739786931"></a>

```c
#define APLIC_SETIENUM 0x1EDC
```

相关声明：[APLIC_SETIENUM](#af5b29f5437042e0dc896403739786931)。

按编号设置中断使能寄存器（Set Interrupt Enable by Number Register）的偏移量。

<a id="r_ac3600d3c0c4267d9d5b5cc939993da99"></a>

```c
#define APLIC_CLRIE_BASE 0x1F00
```

相关声明：[APLIC_CLRIE_BASE](#ac3600d3c0c4267d9d5b5cc939993da99)。

清除中断使能位图（Clear Interrupt Enable Bitmap）的基偏移量。

<a id="r_adea790690199ee6ce6af4dd01bd7cbd5"></a>

```c
#define APLIC_CLRIENUM 0x1FDC
```

相关声明：[APLIC_CLRIENUM](#adea790690199ee6ce6af4dd01bd7cbd5)。

按编号清除中断使能寄存器（Clear Interrupt Enable by Number Register）的偏移量。

<a id="r_aa8df108c758baf3b9c4ff7023752175f"></a>

```c
#define APLIC_MSIADDRCFG 0x1BC0
```

相关声明：[APLIC_MSIADDRCFG](#aa8df108c758baf3b9c4ff7023752175f)。

MSI 地址配置寄存器（MSI Address Configuration Register）的偏移量。

<a id="r_a7d670eee0662ef13518954bf660fab9d"></a>

```c
#define APLIC_MSIADDRCFGH 0x1BC4
```

相关声明：[APLIC_MSIADDRCFGH](#a7d670eee0662ef13518954bf660fab9d)。

MSI 地址高位配置寄存器（MSI Address Configuration High Register）的偏移量。

<a id="r_a388b44c203dce79637bab32214a3292e"></a>

```c
#define APLIC_SMSIADDRCFG 0x1BC8
```

相关声明：[APLIC_SMSIADDRCFG](#a388b44c203dce79637bab32214a3292e)。

监管者模式 MSI 地址配置寄存器（Supervisor MSI Address Configuration Register）的偏移量。

<a id="r_a67ab6722a8f4042630cf88878d132b47"></a>

```c
#define APLIC_SMSIADDRCFGH 0x1BCC
```

相关声明：[APLIC_SMSIADDRCFGH](#a67ab6722a8f4042630cf88878d132b47)。

监管者模式 MSI 地址高位配置寄存器（Supervisor MSI Address Configuration High Register）的偏移量。

<a id="r_a59237a3a02117b7f7659f10daae1652f"></a>

```c
#define APLIC_GENMSI 0x3000
```

相关声明：[APLIC_GENMSI](#a59237a3a02117b7f7659f10daae1652f)。

生成 MSI 寄存器（Generate MSI Register）的偏移量。

<a id="r_aca4663969a234c72ca6dcf8ca3834771"></a>

```c
#define APLIC_TARGET_BASE 0x3004
```

相关声明：[APLIC_TARGET_BASE](#aca4663969a234c72ca6dcf8ca3834771)。

目标寄存器（Target Registers）的基偏移量。

<a id="r_a9bb9d97a3e51d547f314bbb3ff73776a"></a>

```c
#define APLIC_IDC_BASE 0x4000
```

相关声明：[APLIC_IDC_BASE](#a9bb9d97a3e51d547f314bbb3ff73776a)。

中断域控制（Interrupt Domain Control，IDC）区域的基偏移量。

<a id="define-members-1"></a>

### APLIC 域配置位（APLIC Domain Configuration Bits）

APLIC 域配置寄存器（Domain Configuration Register）的位定义。

<a id="r_a9364d09e7eb53f1086fedfd85886be61"></a>

```c
#define APLIC_DOMAINCFG_IE BIT(8)
```

相关声明：[APLIC_DOMAINCFG_IE](#a9364d09e7eb53f1086fedfd85886be61)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

`domaincfg` 中的中断使能位（Interrupt Enable Bit）。

<a id="r_a9c9338ee1a29221465552696e4be9f78"></a>

```c
#define APLIC_DOMAINCFG_DM BIT(2)
```

相关声明：[APLIC_DOMAINCFG_DM](#a9c9338ee1a29221465552696e4be9f78)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

`domaincfg` 中的投递模式位（Delivery Mode Bit），`1` 表示 MSI 模式。

<a id="r_a9dd5b4b6a5db3791e99da5a929c58a67"></a>

```c
#define APLIC_DOMAINCFG_BE BIT(0)
```

相关声明：[APLIC_DOMAINCFG_BE](#a9dd5b4b6a5db3791e99da5a929c58a67)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

`domaincfg` 中的大端字节序位（Big Endian Bit）。

<a id="define-members-2"></a>

### APLIC MSI 地址配置字段（APLIC MSI Address Configuration Fields）

`MSIADDRCFGH` 寄存器的位字段定义；APLIC 使用该寄存器计算各硬件线程（Hart）的 MSI 目标地址（Target Address）。

<a id="r_a7b453561fe52df0ecafb8a4d6649f54a"></a>

```c
#define APLIC_MSIADDRCFGH_L_BIT 31
```

相关声明：[APLIC_MSIADDRCFGH_L_BIT](#a7b453561fe52df0ecafb8a4d6649f54a)。

`MSIADDRCFGH` 中锁定位（Lock Bit）的位置。

<a id="r_a37d77867e271cbaad199b18c28d36be9"></a>

```c
#define APLIC_MSIADDRCFGH_HHXS_SHIFT 24
```

相关声明：[APLIC_MSIADDRCFGH_HHXS_SHIFT](#a37d77867e271cbaad199b18c28d36be9)。

高位硬件线程索引移位（Higher Hart Index Shift）字段的位置。

<a id="r_a92319174e34d94fecea325fdd1fff8e5"></a>

```c
#define APLIC_MSIADDRCFGH_HHXS_MASK 0x1F
```

相关声明：[APLIC_MSIADDRCFGH_HHXS_MASK](#a92319174e34d94fecea325fdd1fff8e5)。

高位硬件线程索引移位（Higher Hart Index Shift）字段的掩码。

<a id="r_a295ddcf9bb735d33999ed5867a17e9fd"></a>

```c
#define APLIC_MSIADDRCFGH_LHXS_SHIFT 20
```

相关声明：[APLIC_MSIADDRCFGH_LHXS_SHIFT](#a295ddcf9bb735d33999ed5867a17e9fd)。

低位硬件线程索引移位（Lower Hart Index Shift）字段的位置。

<a id="r_a7f5c70c9781ac22923cc254ed4455ce9"></a>

```c
#define APLIC_MSIADDRCFGH_LHXS_MASK 0x7
```

相关声明：[APLIC_MSIADDRCFGH_LHXS_MASK](#a7f5c70c9781ac22923cc254ed4455ce9)。

低位硬件线程索引移位（Lower Hart Index Shift）字段的掩码。

<a id="r_a509bf355ee7255d6ebac41f9afd5d267"></a>

```c
#define APLIC_MSIADDRCFGH_HHXW_SHIFT 16
```

相关声明：[APLIC_MSIADDRCFGH_HHXW_SHIFT](#a509bf355ee7255d6ebac41f9afd5d267)。

高位硬件线程索引宽度（Higher Hart Index Width）字段的位置。

<a id="r_a2ef5898b8817f278efa472b64e93375a"></a>

```c
#define APLIC_MSIADDRCFGH_HHXW_MASK 0x7
```

相关声明：[APLIC_MSIADDRCFGH_HHXW_MASK](#a2ef5898b8817f278efa472b64e93375a)。

高位硬件线程索引宽度（Higher Hart Index Width）字段的掩码。

<a id="r_aba6f0c1feeac8b6d3d61f7dcac57fe86"></a>

```c
#define APLIC_MSIADDRCFGH_LHXW_SHIFT 12
```

相关声明：[APLIC_MSIADDRCFGH_LHXW_SHIFT](#aba6f0c1feeac8b6d3d61f7dcac57fe86)。

低位硬件线程索引宽度（Lower Hart Index Width）字段的位置。

<a id="r_a4bb3daec4301c0d96d97950ac2f5eb6d"></a>

```c
#define APLIC_MSIADDRCFGH_LHXW_MASK 0xF
```

相关声明：[APLIC_MSIADDRCFGH_LHXW_MASK](#a4bb3daec4301c0d96d97950ac2f5eb6d)。

低位硬件线程索引宽度（Lower Hart Index Width）字段的掩码。

<a id="r_a7005e907bc1ba2fffecc756790cbf072"></a>

```c
#define APLIC_MSIADDRCFGH_BAPPN_MASK 0xFFF
```

相关声明：[APLIC_MSIADDRCFGH_BAPPN_MASK](#a7005e907bc1ba2fffecc756790cbf072)。

基地址物理页号（PPN）字段的掩码，对应地址高位。

<a id="define-members-3"></a>

### APLIC 源配置字段（APLIC Source Configuration Fields）

源配置寄存器（Source Configuration Registers）的位字段定义。

<a id="r_aff5c490e0f9b4354fcb17c93755392b1"></a>

```c
#define APLIC_SOURCECFG_D_BIT 10
```

相关声明：[APLIC_SOURCECFG_D_BIT](#aff5c490e0f9b4354fcb17c93755392b1)。

`sourcecfg` 中委派位（Delegate Bit）的位置。

<a id="r_a6124b2a953cb9845e0f929d8bacf5429"></a>

```c
#define APLIC_SOURCECFG_SM_MASK 0x7
```

相关声明：[APLIC_SOURCECFG_SM_MASK](#a6124b2a953cb9845e0f929d8bacf5429)。

源模式（Source Mode）字段的掩码，位范围为 2:0。

<a id="r_ac7b1a0006205f40dcfee41af4d6503d8"></a>

```c
#define APLIC_SM_INACTIVE 0x0
```

相关声明：[APLIC_SM_INACTIVE](#ac7b1a0006205f40dcfee41af4d6503d8)。

源模式（Source Mode）：不活动（Inactive）。

<a id="r_a2ac42dea40ef34002726179333a9044f"></a>

```c
#define APLIC_SM_DETACHED 0x1
```

相关声明：[APLIC_SM_DETACHED](#a2ac42dea40ef34002726179333a9044f)。

源模式（Source Mode）：分离（Detached，原文括注为委派给子域（Delegated to Child Domain））。

<a id="r_a7076de6d67bdb56b7d06954d7f265351"></a>

```c
#define APLIC_SM_EDGE_RISE 0x4
```

相关声明：[APLIC_SM_EDGE_RISE](#a7076de6d67bdb56b7d06954d7f265351)。

源模式（Source Mode）：上升沿触发（Rising Edge Triggered）。

<a id="r_a532a4cc492fe082e4037101269323662"></a>

```c
#define APLIC_SM_EDGE_FALL 0x5
```

相关声明：[APLIC_SM_EDGE_FALL](#a532a4cc492fe082e4037101269323662)。

源模式（Source Mode）：下降沿触发（Falling Edge Triggered）。

<a id="r_af6a5fa88a66572044c57f5ac3d4f85da"></a>

```c
#define APLIC_SM_LEVEL_HIGH 0x6
```

相关声明：[APLIC_SM_LEVEL_HIGH](#af6a5fa88a66572044c57f5ac3d4f85da)。

源模式（Source Mode）：高电平有效触发（Active High Level Triggered）。

<a id="r_af4cadff061bbca644c85a3aee989b959"></a>

```c
#define APLIC_SM_LEVEL_LOW 0x7
```

相关声明：[APLIC_SM_LEVEL_LOW](#af4cadff061bbca644c85a3aee989b959)。

源模式（Source Mode）：低电平有效触发（Active Low Level Triggered）。

<a id="define-members-4"></a>

### APLIC 目标寄存器字段（APLIC Target Register Fields）

`TARGET` 寄存器的位字段定义，用于 MSI 路由（Routing）。

<a id="r_a4de43fa06e2090410f760ca24a101365"></a>

```c
#define APLIC_TARGET_HART_SHIFT 18
```

相关声明：[APLIC_TARGET_HART_SHIFT](#a4de43fa06e2090410f760ca24a101365)。

`TARGET` 寄存器中硬件线程索引（Hart Index）字段的移位量。

<a id="r_ac60ba267acb1f78ef651c2df5bed2577"></a>

```c
#define APLIC_TARGET_HART_MASK 0x3FFF
```

相关声明：[APLIC_TARGET_HART_MASK](#ac60ba267acb1f78ef651c2df5bed2577)。

硬件线程索引（Hart Index）字段的掩码，共 14 位，位范围为 31:18。

<a id="r_af1640546f98bdfcd75c9166b7de7fa28"></a>

```c
#define APLIC_TARGET_MSI_DEL BIT(11)
```

相关声明：[APLIC_TARGET_MSI_DEL](#af1640546f98bdfcd75c9166b7de7fa28)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

MSI 投递模式位（Delivery Mode Bit），`0` 表示 DMSI，`1` 表示 MMSI。

<a id="r_ab833f9c2581491b0ea6043f6e5a3d8c8"></a>

```c
#define APLIC_TARGET_EIID_MASK 0x7FF
```

相关声明：[APLIC_TARGET_EIID_MASK](#ab833f9c2581491b0ea6043f6e5a3d8c8)。

外部中断标识（External Interrupt Identity）字段的掩码，共 11 位，位范围为 10:0。

<a id="define-members-5"></a>

### APLIC GENMSI 寄存器字段（APLIC GENMSI Register Fields）

软件触发 MSI 生成（Software-triggered MSI Generation）的位字段定义。

<a id="r_ac740484ecf8821fa9b076d67f9f5ef4e"></a>

```c
#define APLIC_GENMSI_HART_SHIFT 18
```

相关声明：[APLIC_GENMSI_HART_SHIFT](#ac740484ecf8821fa9b076d67f9f5ef4e)。

`GENMSI` 寄存器中硬件线程索引（Hart Index）字段的移位量。

<a id="r_a869725895a77cd29e1f04281e5e63037"></a>

```c
#define APLIC_GENMSI_HART_MASK 0x3FFF
```

相关声明：[APLIC_GENMSI_HART_MASK](#a869725895a77cd29e1f04281e5e63037)。

硬件线程索引（Hart Index）字段的掩码，共 14 位，位范围为 31:18。

<a id="r_a164a28d72ddd5484cc0ac5d7d2ab0c5e"></a>

```c
#define APLIC_GENMSI_CONTEXT_SHIFT 13
```

相关声明：[APLIC_GENMSI_CONTEXT_SHIFT](#a164a28d72ddd5484cc0ac5d7d2ab0c5e)。

上下文／客户机（Context/Guest）字段的移位量，位范围为 17:13。

<a id="r_a2b9e8e50dd7abb3b72ae4ec9a5891775"></a>

```c
#define APLIC_GENMSI_CONTEXT_MASK 0x1F
```

相关声明：[APLIC_GENMSI_CONTEXT_MASK](#a2b9e8e50dd7abb3b72ae4ec9a5891775)。

上下文（Context）字段的掩码，共 5 位，用于 DMSI。

<a id="r_aed588f169aa14f75646e349a4a79b779"></a>

```c
#define APLIC_GENMSI_BUSY BIT(12)
```

相关声明：[APLIC_GENMSI_BUSY](#aed588f169aa14f75646e349a4a79b779)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

忙标志位（Busy Bit），只读状态。

<a id="r_aa0f5ee9c351ab9b5a7d6d39f11ac3fb0"></a>

```c
#define APLIC_GENMSI_MMSI_MODE BIT(11)
```

相关声明：[APLIC_GENMSI_MMSI_MODE](#aa0f5ee9c351ab9b5a7d6d39f11ac3fb0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

MSI 投递模式（Delivery Mode），`0` 表示 DMSI，`1` 表示 MMSI。

<a id="r_aa489b5e52d8b8bfb90c4420511dc4d47"></a>

```c
#define APLIC_GENMSI_EIID_MASK 0x7FF
```

相关声明：[APLIC_GENMSI_EIID_MASK](#aa489b5e52d8b8bfb90c4420511dc4d47)。

外部中断标识（External Interrupt Identity）字段的掩码，共 11 位，位范围为 10:0。

<a id="define-members-6"></a>

### APLIC IDC 寄存器偏移量（APLIC IDC Register Offsets）

启用直接投递模式（DM）时，IDC 结构体内各寄存器的偏移量。

每个硬件线程（Hart）对应一个 IDC。

<a id="r_afd9a4f6b16ad61355fd159f87e4ccf9c"></a>

```c
#define APLIC_IDC_IDELIVERY_OFFSET 0x0
```

相关声明：[APLIC_IDC_IDELIVERY_OFFSET](#afd9a4f6b16ad61355fd159f87e4ccf9c)。

用于指定中断投递（Interrupt Delivery）的可写任意值、读出合法值（WARL）寄存器，`0` 表示禁用，`1` 表示启用。

<a id="r_a2f4b2488b715ab29e6d12fb07947f281"></a>

```c
#define APLIC_IDC_IFORCE_OFFSET 0x4
```

相关声明：[APLIC_IDC_IFORCE_OFFSET](#a2f4b2488b715ab29e6d12fb07947f281)。

用于测试的可写任意值、读出合法值（WARL）寄存器，`1` 表示强制置位中断。

<a id="r_a13ecae2ec0109593570e5f270e230daa"></a>

```c
#define APLIC_IDC_ITHRESHOLD_OFFSET 0x8
```

相关声明：[APLIC_IDC_ITHRESHOLD_OFFSET](#a13ecae2ec0109593570e5f270e230daa)。

指示中断可被发出信号的最低优先级（Minimum Priority）的仅写合法值、读出合法值（WLRL）寄存器。

<a id="r_a443e3d8683aec28992398a8ab672af63"></a>

```c
#define APLIC_IDC_TOPI_OFFSET 0x18
```

相关声明：[APLIC_IDC_TOPI_OFFSET](#a443e3d8683aec28992398a8ab672af63)。

指示当前优先级最高的待处理中断（Highest-priority Interrupt Pending）的只读寄存器。

<a id="r_a3a7d90ad87464060903ac13422150964"></a>

```c
#define APLIC_IDC_CLAIMI_OFFSET 0x1C
```

相关声明：[APLIC_IDC_CLAIMI_OFFSET](#a3a7d90ad87464060903ac13422150964)。

与 `TOPI` 相同的只读寄存器，但读取时会清除待处理位（Pending Bit）。

<a id="r_a310930e6500b8a30d156d621785ec8ca"></a>

```c
#define APLIC_IDC_STRUCT_SIZE 0x20
```

相关声明：[APLIC_IDC_STRUCT_SIZE](#a310930e6500b8a30d156d621785ec8ca)。

根据高级中断架构（AIA）规范，每个 IDC 结构体占 32 字节。

<a id="define-members-7"></a>

### APLIC idelivery 寄存器字段（APLIC idelivery Register Fields）

APLIC `ithreshold` 配置寄存器（Configuration Register）的位定义。

<a id="r_ad58e8ac2fb12c748f098092240456800"></a>

```c
#define APLIC_IDC_IDELIVERY_ENABLE BIT(0)
```

相关声明：[APLIC_IDC_IDELIVERY_ENABLE](#ad58e8ac2fb12c748f098092240456800)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

IDC 内 `idelivery` 寄存器中的 `idelivery` 使能位（Enable Bit）。

<a id="define-members-8"></a>

### APLIC iforce 寄存器字段（APLIC iforce Register Fields）

APLIC `idelivery` 配置寄存器（Configuration Register）的位定义。

<a id="r_a276af2aebcf2350dfa7e6dc03f27bdd4"></a>

```c
#define APLIC_IDC_IFORCE_SET 1
```

相关声明：[APLIC_IDC_IFORCE_SET](#a276af2aebcf2350dfa7e6dc03f27bdd4)。

`iforce` 默认值（Default Value），`1` 表示设置中断待处理状态（Interrupt Pending）。

<a id="define-members-9"></a>

### APLIC ithreshold 寄存器字段（APLIC ithreshold Register Fields）

APLIC `idelivery` 配置寄存器（Configuration Register）的位定义。

<a id="r_a3840d8b54674b7af194080ce7212323c"></a>

```c
#define APLIC_IDC_ITHRESHOLD 0
```

相关声明：[APLIC_IDC_ITHRESHOLD](#a3840d8b54674b7af194080ce7212323c)。

`ithreshold` 默认值（Default Value），`0` 表示所有已启用的源都可以发出中断信号。

<a id="define-members-10"></a>

### APLIC TOPI／CLAIMI 寄存器字段（APLIC TOPI / CLAIMI Register Fields）

APLIC `idelivery` 配置寄存器（Configuration Register）的位定义。

<a id="r_ad6917cf6f22b8634c20f6825b54f8dcd"></a>

```c
#define APLIC_IPRIO_MASK BIT_MASK(8)
```

相关声明：[APLIC_IPRIO_MASK](#ad6917cf6f22b8634c20f6825b54f8dcd)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

`TOPI`/`CLAIMI` 的低 8 位表示中断优先级（Interrupt Priority）。

<a id="r_a91f356bb1bfe30378ecda2304c9361ea"></a>

```c
#define APLIC_INTERRUPT_IDENTITY_SHIFT 16
```

相关声明：[APLIC_INTERRUPT_IDENTITY_SHIFT](#a91f356bb1bfe30378ecda2304c9361ea)。

寄存器中中断标识（Interrupt Identity）字段的基偏移量。

<a id="r_a0fe97ce538c22fd4dfcf0a80e2e07e9b"></a>

```c
#define APLIC_INTERRUPT_IDENTITY_MASK (BIT_MASK(10) << APLIC_INTERRUPT_IDENTITY_SHIFT)
```

相关声明：[APLIC_INTERRUPT_IDENTITY_MASK](#a0fe97ce538c22fd4dfcf0a80e2e07e9b)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)、[APLIC_INTERRUPT_IDENTITY_SHIFT](#a91f356bb1bfe30378ecda2304c9361ea)。

`TOPI`/`CLAIMI` 的位 25:16 表示中断源编号（Interrupt Source Number）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.2\_函数（Functions）

<a id="r_a317604c4a77581599e3b568c0af0f8c5"></a>

```c
static uint32_t aplic_sourcecfg_off (unsigned int src)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[aplic_sourcecfg_off](#a317604c4a77581599e3b568c0af0f8c5)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

计算某个中断源（Source）的 `sourcecfg` 寄存器偏移量。

<a id="r_a122c9068e3bbedf9c145493278b8bd05"></a>

```c
static uint32_t aplic_target_off (unsigned int src)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[aplic_target_off](#a122c9068e3bbedf9c145493278b8bd05)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

计算某个中断源（Source）的 `target` 寄存器偏移量。

<a id="r_a32492c238d531bf4474fa391aa634429"></a>

```c
static const struct device * riscv_aplic_get_dev (void)
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[riscv_aplic_get_dev](#a32492c238d531bf4474fa391aa634429)。

获取 APLIC 设备实例（Device Instance）。

<a id="r_a771d4b9c52895945bc94b7ce6bc24c1a"></a>

```c
void riscv_aplic_domain_enable (const struct device *dev, bool enable)
```

相关声明：[riscv_aplic_domain_enable](#a771d4b9c52895945bc94b7ce6bc24c1a)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用 APLIC 域（Domain）。

<a id="r_a25e2d4768a61e0b8b135840d45777c5f"></a>

```c
void riscv_aplic_config_src (const struct device *dev, unsigned int src, unsigned int sm)
```

相关声明：[riscv_aplic_config_src](#a25e2d4768a61e0b8b135840d45777c5f)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

配置中断源模式（Interrupt Source Mode）。

<a id="r_a48bfa691091e24dba2ab8b466e869c9e"></a>

```c
void riscv_aplic_enable_src (const struct device *dev, unsigned int src, bool enable)
```

相关声明：[riscv_aplic_enable_src](#a48bfa691091e24dba2ab8b466e869c9e)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用或禁用中断源（Interrupt Source）。

<a id="r_a99ee07d894d3a09370d5ab0077359ac4"></a>

```c
void riscv_aplic_msi_route (const struct device *dev, unsigned int src, uint32_t hart, uint32_t eiid)
```

相关声明：[riscv_aplic_msi_route](#a99ee07d894d3a09370d5ab0077359ac4)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置中断源（Interrupt Source）的 MSI 路由（Routing）。

<a id="r_afa4ce7bd64fb5c05ecef44088905f603"></a>

```c
void riscv_aplic_msi_inject_software_interrupt (const struct device *dev, uint32_t eiid, uint32_t hart_id, uint32_t context)
```

相关声明：[riscv_aplic_msi_inject_software_interrupt](#afa4ce7bd64fb5c05ecef44088905f603)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

注入软件触发的 MSI（Software-triggered MSI）。

<a id="r_ab446350754c3f125e78ae3bf89e71636"></a>

```c
uint32_t riscv_aplic_get_num_sources (const struct device *dev)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[riscv_aplic_get_num_sources](#ab446350754c3f125e78ae3bf89e71636)、[device](../device_reference/P002_设备对象结构.md)。

获取中断源（Interrupt Source）的数量。

<a id="r_a6599e6e97695abefabbc8a6fc3fd56ff"></a>

```c
static void riscv_aplic_enable_source (unsigned int src)
```

相关声明：[riscv_aplic_enable_source](#a6599e6e97695abefabbc8a6fc3fd56ff)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

启用中断源（Interrupt Source）的便捷封装（Convenience Wrapper）。

<a id="r_a959870fc662d2251e280f88766dfb183"></a>

```c
static void riscv_aplic_disable_source (unsigned int src)
```

相关声明：[riscv_aplic_disable_source](#a959870fc662d2251e280f88766dfb183)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

禁用中断源（Interrupt Source）的便捷封装（Convenience Wrapper）。

<a id="r_a871822d8d01a9428795df3bc7a183499"></a>

```c
static void riscv_aplic_msi_inject_genmsi (uint32_t hart, uint32_t eiid)
```

相关声明：[riscv_aplic_msi_inject_genmsi](#a871822d8d01a9428795df3bc7a183499)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使用 `GENMSI` 注入 MSI 的便捷封装（Convenience Wrapper）。

<a id="r_a83d33a6a410d4fd85da300a8f308dee8"></a>

```c
static uint32_t aplic_idelivery_off (unsigned int cpu)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[aplic_idelivery_off](#a83d33a6a410d4fd85da300a8f308dee8)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

计算给定 CPU 的 `idelivery` 寄存器偏移量（Register Offset）。

<a id="r_a189d3723a935cb5b44e1dceaac9e75df"></a>

```c
static uint32_t aplic_ithreshold_off (unsigned int cpu)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[aplic_ithreshold_off](#a189d3723a935cb5b44e1dceaac9e75df)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

计算给定 CPU 的 `ithreshold` 寄存器偏移量（Register Offset）。

<a id="r_a9842d5ae9cf44ef0396d2a01968c9ce9"></a>

```c
static uint32_t aplic_iforce_off (unsigned int cpu)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[aplic_iforce_off](#a9842d5ae9cf44ef0396d2a01968c9ce9)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

计算给定 CPU 的 `iforce` 寄存器偏移量（Register Offset）。

<a id="r_a37b9d14cf6a40d93085e3b2a8bd9d57d"></a>

```c
static uint32_t aplic_topi_off (unsigned int cpu)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[aplic_topi_off](#a37b9d14cf6a40d93085e3b2a8bd9d57d)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

计算给定 CPU 的 `topi` 寄存器偏移量（Register Offset）。

<a id="r_ac78b1ec01b7de7c6bd556cbd0a5efcab"></a>

```c
static uint32_t aplic_claimi_off (unsigned int cpu)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[aplic_claimi_off](#ac78b1ec01b7de7c6bd556cbd0a5efcab)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

计算给定 CPU 的 `claimi` 寄存器偏移量（Register Offset）。

## 11.3\_详细说明（Detailed Documentation）

<a id="ac3600d3c0c4267d9d5b5cc939993da99"></a>

### `APLIC_CLRIE_BASE`

```c
#define APLIC_CLRIE_BASE 0x1F00
```

清除中断使能位图（Clear Interrupt Enable Bitmap）的基偏移量。

<a id="adea790690199ee6ce6af4dd01bd7cbd5"></a>

### `APLIC_CLRIENUM`

```c
#define APLIC_CLRIENUM 0x1FDC
```

按编号清除中断使能寄存器（Clear Interrupt Enable by Number Register）的偏移量。

<a id="aaded0cb41afa0352eaab7b0e77675a17"></a>

### `APLIC_CLRIP_BASE`

```c
#define APLIC_CLRIP_BASE 0x1D00
```

清除中断待处理位图（Clear Interrupt Pending Bitmap）的基偏移量。

<a id="a8b030a6341030491354ed6f600631953"></a>

### `APLIC_CLRIPNUM`

```c
#define APLIC_CLRIPNUM 0x1DDC
```

按编号清除中断待处理状态寄存器（Clear Interrupt Pending by Number Register）的偏移量。

<a id="a3f7c50560007001d1b22e5ac86a4dd3b"></a>

### `APLIC_DOMAINCFG`

```c
#define APLIC_DOMAINCFG 0x0000
```

域配置寄存器（Domain Configuration Register）的偏移量。

<a id="a9dd5b4b6a5db3791e99da5a929c58a67"></a>

### `APLIC_DOMAINCFG_BE`

```c
#define APLIC_DOMAINCFG_BE BIT(0)
```

`domaincfg` 中的大端字节序位（Big Endian Bit）。

<a id="a9c9338ee1a29221465552696e4be9f78"></a>

### `APLIC_DOMAINCFG_DM`

```c
#define APLIC_DOMAINCFG_DM BIT(2)
```

`domaincfg` 中的投递模式位（Delivery Mode Bit），`1` 表示 MSI 模式。

<a id="a9364d09e7eb53f1086fedfd85886be61"></a>

### `APLIC_DOMAINCFG_IE`

```c
#define APLIC_DOMAINCFG_IE BIT(8)
```

`domaincfg` 中的中断使能位（Interrupt Enable Bit）。

<a id="a59237a3a02117b7f7659f10daae1652f"></a>

### `APLIC_GENMSI`

```c
#define APLIC_GENMSI 0x3000
```

生成 MSI 寄存器（Generate MSI Register）的偏移量。

<a id="aed588f169aa14f75646e349a4a79b779"></a>

### `APLIC_GENMSI_BUSY`

```c
#define APLIC_GENMSI_BUSY BIT(12)
```

忙标志位（Busy Bit），只读状态。

<a id="a2b9e8e50dd7abb3b72ae4ec9a5891775"></a>

### `APLIC_GENMSI_CONTEXT_MASK`

```c
#define APLIC_GENMSI_CONTEXT_MASK 0x1F
```

上下文（Context）字段的掩码，共 5 位，用于 DMSI。

<a id="a164a28d72ddd5484cc0ac5d7d2ab0c5e"></a>

### `APLIC_GENMSI_CONTEXT_SHIFT`

```c
#define APLIC_GENMSI_CONTEXT_SHIFT 13
```

上下文／客户机（Context/Guest）字段的移位量，位范围为 17:13。

<a id="aa489b5e52d8b8bfb90c4420511dc4d47"></a>

### `APLIC_GENMSI_EIID_MASK`

```c
#define APLIC_GENMSI_EIID_MASK 0x7FF
```

外部中断标识（External Interrupt Identity）字段的掩码，共 11 位，位范围为 10:0。

<a id="a869725895a77cd29e1f04281e5e63037"></a>

### `APLIC_GENMSI_HART_MASK`

```c
#define APLIC_GENMSI_HART_MASK 0x3FFF
```

硬件线程索引（Hart Index）字段的掩码，共 14 位，位范围为 31:18。

<a id="ac740484ecf8821fa9b076d67f9f5ef4e"></a>

### `APLIC_GENMSI_HART_SHIFT`

```c
#define APLIC_GENMSI_HART_SHIFT 18
```

`GENMSI` 寄存器中硬件线程索引（Hart Index）字段的移位量。

<a id="aa0f5ee9c351ab9b5a7d6d39f11ac3fb0"></a>

### `APLIC_GENMSI_MMSI_MODE`

```c
#define APLIC_GENMSI_MMSI_MODE BIT(11)
```

MSI 投递模式（Delivery Mode），`0` 表示 DMSI，`1` 表示 MMSI。

<a id="a9bb9d97a3e51d547f314bbb3ff73776a"></a>

### `APLIC_IDC_BASE`

```c
#define APLIC_IDC_BASE 0x4000
```

中断域控制（Interrupt Domain Control，IDC）区域的基偏移量。

<a id="a3a7d90ad87464060903ac13422150964"></a>

### `APLIC_IDC_CLAIMI_OFFSET`

```c
#define APLIC_IDC_CLAIMI_OFFSET 0x1C
```

与 `TOPI` 相同的只读寄存器，但读取时会清除待处理位（Pending Bit）。

<a id="ad58e8ac2fb12c748f098092240456800"></a>

### `APLIC_IDC_IDELIVERY_ENABLE`

```c
#define APLIC_IDC_IDELIVERY_ENABLE BIT(0)
```

IDC 内 `idelivery` 寄存器中的 `idelivery` 使能位（Enable Bit）。

<a id="afd9a4f6b16ad61355fd159f87e4ccf9c"></a>

### `APLIC_IDC_IDELIVERY_OFFSET`

```c
#define APLIC_IDC_IDELIVERY_OFFSET 0x0
```

用于指定中断投递（Interrupt Delivery）的可写任意值、读出合法值（WARL）寄存器，`0` 表示禁用，`1` 表示启用。

<a id="a2f4b2488b715ab29e6d12fb07947f281"></a>

### `APLIC_IDC_IFORCE_OFFSET`

```c
#define APLIC_IDC_IFORCE_OFFSET 0x4
```

用于测试的可写任意值、读出合法值（WARL）寄存器，`1` 表示强制置位中断。

<a id="a276af2aebcf2350dfa7e6dc03f27bdd4"></a>

### `APLIC_IDC_IFORCE_SET`

```c
#define APLIC_IDC_IFORCE_SET 1
```

`iforce` 默认值（Default Value），`1` 表示设置中断待处理状态（Interrupt Pending）。

`TOPI` 为 `0` 时属于伪中断（Spurious）。

<a id="a3840d8b54674b7af194080ce7212323c"></a>

### `APLIC_IDC_ITHRESHOLD`

```c
#define APLIC_IDC_ITHRESHOLD 0
```

`ithreshold` 默认值（Default Value），`0` 表示所有已启用的源都可以发出中断信号。

<a id="a13ecae2ec0109593570e5f270e230daa"></a>

### `APLIC_IDC_ITHRESHOLD_OFFSET`

```c
#define APLIC_IDC_ITHRESHOLD_OFFSET 0x8
```

指示中断可被发出信号的最低优先级（Minimum Priority）的仅写合法值、读出合法值（WLRL）寄存器。

<a id="a310930e6500b8a30d156d621785ec8ca"></a>

### `APLIC_IDC_STRUCT_SIZE`

```c
#define APLIC_IDC_STRUCT_SIZE 0x20
```

根据高级中断架构（AIA）规范，每个 IDC 结构体占 32 字节。

<a id="a443e3d8683aec28992398a8ab672af63"></a>

### `APLIC_IDC_TOPI_OFFSET`

```c
#define APLIC_IDC_TOPI_OFFSET 0x18
```

指示当前优先级最高的待处理中断（Highest-priority Interrupt Pending）的只读寄存器。

<a id="a0fe97ce538c22fd4dfcf0a80e2e07e9b"></a>

### `APLIC_INTERRUPT_IDENTITY_MASK`

```c
#define APLIC_INTERRUPT_IDENTITY_MASK (BIT_MASK(10) << APLIC_INTERRUPT_IDENTITY_SHIFT)
```

`TOPI`/`CLAIMI` 的位 25:16 表示中断源编号（Interrupt Source Number）。

<a id="a91f356bb1bfe30378ecda2304c9361ea"></a>

### `APLIC_INTERRUPT_IDENTITY_SHIFT`

```c
#define APLIC_INTERRUPT_IDENTITY_SHIFT 16
```

寄存器中中断标识（Interrupt Identity）字段的基偏移量。

<a id="ad6917cf6f22b8634c20f6825b54f8dcd"></a>

### `APLIC_IPRIO_MASK`

```c
#define APLIC_IPRIO_MASK BIT_MASK(8)
```

`TOPI`/`CLAIMI` 的低 8 位表示中断优先级（Interrupt Priority）。

<a id="aa8df108c758baf3b9c4ff7023752175f"></a>

### `APLIC_MSIADDRCFG`

```c
#define APLIC_MSIADDRCFG 0x1BC0
```

MSI 地址配置寄存器（MSI Address Configuration Register）的偏移量。

<a id="a7d670eee0662ef13518954bf660fab9d"></a>

### `APLIC_MSIADDRCFGH`

```c
#define APLIC_MSIADDRCFGH 0x1BC4
```

MSI 地址高位配置寄存器（MSI Address Configuration High Register）的偏移量。

<a id="a7005e907bc1ba2fffecc756790cbf072"></a>

### `APLIC_MSIADDRCFGH_BAPPN_MASK`

```c
#define APLIC_MSIADDRCFGH_BAPPN_MASK 0xFFF
```

基地址物理页号（PPN）字段的掩码，对应地址高位。

<a id="a92319174e34d94fecea325fdd1fff8e5"></a>

### `APLIC_MSIADDRCFGH_HHXS_MASK`

```c
#define APLIC_MSIADDRCFGH_HHXS_MASK 0x1F
```

高位硬件线程索引移位（Higher Hart Index Shift）字段的掩码。

<a id="a37d77867e271cbaad199b18c28d36be9"></a>

### `APLIC_MSIADDRCFGH_HHXS_SHIFT`

```c
#define APLIC_MSIADDRCFGH_HHXS_SHIFT 24
```

高位硬件线程索引移位（Higher Hart Index Shift）字段的位置。

<a id="a2ef5898b8817f278efa472b64e93375a"></a>

### `APLIC_MSIADDRCFGH_HHXW_MASK`

```c
#define APLIC_MSIADDRCFGH_HHXW_MASK 0x7
```

高位硬件线程索引宽度（Higher Hart Index Width）字段的掩码。

<a id="a509bf355ee7255d6ebac41f9afd5d267"></a>

### `APLIC_MSIADDRCFGH_HHXW_SHIFT`

```c
#define APLIC_MSIADDRCFGH_HHXW_SHIFT 16
```

高位硬件线程索引宽度（Higher Hart Index Width）字段的位置。

<a id="a7b453561fe52df0ecafb8a4d6649f54a"></a>

### `APLIC_MSIADDRCFGH_L_BIT`

```c
#define APLIC_MSIADDRCFGH_L_BIT 31
```

`MSIADDRCFGH` 中锁定位（Lock Bit）的位置。

<a id="a7f5c70c9781ac22923cc254ed4455ce9"></a>

### `APLIC_MSIADDRCFGH_LHXS_MASK`

```c
#define APLIC_MSIADDRCFGH_LHXS_MASK 0x7
```

低位硬件线程索引移位（Lower Hart Index Shift）字段的掩码。

<a id="a295ddcf9bb735d33999ed5867a17e9fd"></a>

### `APLIC_MSIADDRCFGH_LHXS_SHIFT`

```c
#define APLIC_MSIADDRCFGH_LHXS_SHIFT 20
```

低位硬件线程索引移位（Lower Hart Index Shift）字段的位置。

<a id="a4bb3daec4301c0d96d97950ac2f5eb6d"></a>

### `APLIC_MSIADDRCFGH_LHXW_MASK`

```c
#define APLIC_MSIADDRCFGH_LHXW_MASK 0xF
```

低位硬件线程索引宽度（Lower Hart Index Width）字段的掩码。

<a id="aba6f0c1feeac8b6d3d61f7dcac57fe86"></a>

### `APLIC_MSIADDRCFGH_LHXW_SHIFT`

```c
#define APLIC_MSIADDRCFGH_LHXW_SHIFT 12
```

低位硬件线程索引宽度（Lower Hart Index Width）字段的位置。

<a id="ae024fd41ba913c13e535d10c4adc5d96"></a>

### `APLIC_SETIE_BASE`

```c
#define APLIC_SETIE_BASE 0x1E00
```

设置中断使能位图（Set Interrupt Enable Bitmap）的基偏移量。

<a id="af5b29f5437042e0dc896403739786931"></a>

### `APLIC_SETIENUM`

```c
#define APLIC_SETIENUM 0x1EDC
```

按编号设置中断使能寄存器（Set Interrupt Enable by Number Register）的偏移量。

<a id="a8fe43db0a39481cfbc7fc26d5b201527"></a>

### `APLIC_SETIP_BASE`

```c
#define APLIC_SETIP_BASE 0x1C00
```

设置中断待处理位图（Set Interrupt Pending Bitmap）的基偏移量。

<a id="a900aa5210c8feee01c478ca70226af66"></a>

### `APLIC_SETIPNUM`

```c
#define APLIC_SETIPNUM 0x1CDC
```

按编号设置中断待处理状态寄存器（Set Interrupt Pending by Number Register）的偏移量。

<a id="a2ac42dea40ef34002726179333a9044f"></a>

### `APLIC_SM_DETACHED`

```c
#define APLIC_SM_DETACHED 0x1
```

源模式（Source Mode）：分离（Detached，原文括注为委派给子域（Delegated to Child Domain））。

<a id="a532a4cc492fe082e4037101269323662"></a>

### `APLIC_SM_EDGE_FALL`

```c
#define APLIC_SM_EDGE_FALL 0x5
```

源模式（Source Mode）：下降沿触发（Falling Edge Triggered）。

<a id="a7076de6d67bdb56b7d06954d7f265351"></a>

### `APLIC_SM_EDGE_RISE`

```c
#define APLIC_SM_EDGE_RISE 0x4
```

源模式（Source Mode）：上升沿触发（Rising Edge Triggered）。

<a id="ac7b1a0006205f40dcfee41af4d6503d8"></a>

### `APLIC_SM_INACTIVE`

```c
#define APLIC_SM_INACTIVE 0x0
```

源模式（Source Mode）：不活动（Inactive）。

<a id="af6a5fa88a66572044c57f5ac3d4f85da"></a>

### `APLIC_SM_LEVEL_HIGH`

```c
#define APLIC_SM_LEVEL_HIGH 0x6
```

源模式（Source Mode）：高电平有效触发（Active High Level Triggered）。

<a id="af4cadff061bbca644c85a3aee989b959"></a>

### `APLIC_SM_LEVEL_LOW`

```c
#define APLIC_SM_LEVEL_LOW 0x7
```

源模式（Source Mode）：低电平有效触发（Active Low Level Triggered）。

<a id="a388b44c203dce79637bab32214a3292e"></a>

### `APLIC_SMSIADDRCFG`

```c
#define APLIC_SMSIADDRCFG 0x1BC8
```

监管者模式 MSI 地址配置寄存器（Supervisor MSI Address Configuration Register）的偏移量。

<a id="a67ab6722a8f4042630cf88878d132b47"></a>

### `APLIC_SMSIADDRCFGH`

```c
#define APLIC_SMSIADDRCFGH 0x1BCC
```

监管者模式 MSI 地址高位配置寄存器（Supervisor MSI Address Configuration High Register）的偏移量。

<a id="a66c8ea9cb1891e48b537a663579e56aa"></a>

### `APLIC_SOURCECFG_BASE`

```c
#define APLIC_SOURCECFG_BASE 0x0004
```

源配置寄存器（Source Configuration Registers）的基偏移量。

<a id="aff5c490e0f9b4354fcb17c93755392b1"></a>

### `APLIC_SOURCECFG_D_BIT`

```c
#define APLIC_SOURCECFG_D_BIT 10
```

`sourcecfg` 中委派位（Delegate Bit）的位置。

<a id="a6124b2a953cb9845e0f929d8bacf5429"></a>

### `APLIC_SOURCECFG_SM_MASK`

```c
#define APLIC_SOURCECFG_SM_MASK 0x7
```

源模式（Source Mode）字段的掩码，位范围为 2:0。

<a id="aca4663969a234c72ca6dcf8ca3834771"></a>

### `APLIC_TARGET_BASE`

```c
#define APLIC_TARGET_BASE 0x3004
```

目标寄存器（Target Registers）的基偏移量。

<a id="ab833f9c2581491b0ea6043f6e5a3d8c8"></a>

### `APLIC_TARGET_EIID_MASK`

```c
#define APLIC_TARGET_EIID_MASK 0x7FF
```

外部中断标识（External Interrupt Identity）字段的掩码，共 11 位，位范围为 10:0。

<a id="ac60ba267acb1f78ef651c2df5bed2577"></a>

### `APLIC_TARGET_HART_MASK`

```c
#define APLIC_TARGET_HART_MASK 0x3FFF
```

硬件线程索引（Hart Index）字段的掩码，共 14 位，位范围为 31:18。

<a id="a4de43fa06e2090410f760ca24a101365"></a>

### `APLIC_TARGET_HART_SHIFT`

```c
#define APLIC_TARGET_HART_SHIFT 18
```

`TARGET` 寄存器中硬件线程索引（Hart Index）字段的移位量。

<a id="af1640546f98bdfcd75c9166b7de7fa28"></a>

### `APLIC_TARGET_MSI_DEL`

```c
#define APLIC_TARGET_MSI_DEL BIT(11)
```

MSI 投递模式位（Delivery Mode Bit），`0` 表示 DMSI，`1` 表示 MMSI。

<a id="ac78b1ec01b7de7c6bd556cbd0a5efcab"></a>

### `aplic_claimi_off()`

```c
uint32_t aplic_claimi_off ( unsigned int cpu)
```

声明属性：`inline`、`static`。

计算给定 CPU 的 `claimi` 寄存器偏移量（Register Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cpu` | CPU 索引。 |

**返回（Returns）**：返回值（Returns）：IDC 结构体中该 CPU 的 `claimi` 寄存器的基偏移量。

<a id="a83d33a6a410d4fd85da300a8f308dee8"></a>

### `aplic_idelivery_off()`

```c
uint32_t aplic_idelivery_off ( unsigned int cpu)
```

声明属性：`inline`、`static`。

计算给定 CPU 的 `idelivery` 寄存器偏移量（Register Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cpu` | CPU 索引。 |

**返回（Returns）**：返回值（Returns）：IDC 结构体中该 CPU 的 `idelivery` 寄存器的基偏移量。

<a id="a9842d5ae9cf44ef0396d2a01968c9ce9"></a>

### `aplic_iforce_off()`

```c
uint32_t aplic_iforce_off ( unsigned int cpu)
```

声明属性：`inline`、`static`。

计算给定 CPU 的 `iforce` 寄存器偏移量（Register Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cpu` | CPU 索引。 |

**返回（Returns）**：返回值（Returns）：IDC 结构体中该 CPU 的 `iforce` 寄存器的基偏移量。

<a id="a189d3723a935cb5b44e1dceaac9e75df"></a>

### `aplic_ithreshold_off()`

```c
uint32_t aplic_ithreshold_off ( unsigned int cpu)
```

声明属性：`inline`、`static`。

计算给定 CPU 的 `ithreshold` 寄存器偏移量（Register Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cpu` | CPU 索引。 |

**返回（Returns）**：返回值（Returns）：IDC 结构体中该 CPU 的 `ithreshold` 寄存器的基偏移量。

<a id="a317604c4a77581599e3b568c0af0f8c5"></a>

### `aplic_sourcecfg_off()`

```c
uint32_t aplic_sourcecfg_off ( unsigned int src)
```

声明属性：`inline`、`static`。

计算某个中断源（Source）的 `sourcecfg` 寄存器偏移量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 中断源编号（Interrupt Source Number），从 1 开始。 |

**返回（Returns）**：返回值（Returns）：该中断源的配置寄存器（Configuration Register）的偏移量。

<a id="a122c9068e3bbedf9c145493278b8bd05"></a>

### `aplic_target_off()`

```c
uint32_t aplic_target_off ( unsigned int src)
```

声明属性：`inline`、`static`。

计算某个中断源（Source）的 `target` 寄存器偏移量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 中断源编号（Interrupt Source Number），从 1 开始。 |

**返回（Returns）**：返回值（Returns）：该中断源的目标寄存器（Target Register）的偏移量。

<a id="a37b9d14cf6a40d93085e3b2a8bd9d57d"></a>

### `aplic_topi_off()`

```c
uint32_t aplic_topi_off ( unsigned int cpu)
```

声明属性：`inline`、`static`。

计算给定 CPU 的 `topi` 寄存器偏移量（Register Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cpu` | CPU 索引。 |

**返回（Returns）**：返回值（Returns）：IDC 结构体中该 CPU 的 `topi` 寄存器的基偏移量。

<a id="a25e2d4768a61e0b8b135840d45777c5f"></a>

### `riscv_aplic_config_src()`

```c
void riscv_aplic_config_src ( const struct device * dev, unsigned int src, unsigned int sm )
```

配置中断源模式（Interrupt Source Mode）。

设置中断源（Interrupt Source）的触发模式（Trigger Mode），包括边沿／电平和极性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 高级平台级中断控制器（APLIC）设备。 |
| `src` | 中断源编号。 |
| `sm` | 源模式（Source Mode），取值为 `APLIC_SM_*`。 |

<a id="a959870fc662d2251e280f88766dfb183"></a>

### `riscv_aplic_disable_source()`

```c
void riscv_aplic_disable_source ( unsigned int src)
```

声明属性：`inline`、`static`。

禁用中断源（Interrupt Source）的便捷封装（Convenience Wrapper）。

使用默认 APLIC 设备（Device）禁用指定的中断源（Interrupt Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 中断源编号。 |

<a id="a771d4b9c52895945bc94b7ce6bc24c1a"></a>

### `riscv_aplic_domain_enable()`

```c
void riscv_aplic_domain_enable ( const struct device * dev, bool enable )
```

启用或禁用 APLIC 域（Domain）。

控制域配置寄存器（Domain Configuration Register）中的中断使能位（Interrupt Enable Bit）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 高级平台级中断控制器（APLIC）设备。 |
| `enable` | `true` 表示启用域（Domain），`false` 表示禁用。 |

<a id="a6599e6e97695abefabbc8a6fc3fd56ff"></a>

### `riscv_aplic_enable_source()`

```c
void riscv_aplic_enable_source ( unsigned int src)
```

声明属性：`inline`、`static`。

启用中断源（Interrupt Source）的便捷封装（Convenience Wrapper）。

使用默认 APLIC 设备（Device）启用指定的中断源（Interrupt Source）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 中断源编号。 |

<a id="a48bfa691091e24dba2ab8b466e869c9e"></a>

### `riscv_aplic_enable_src()`

```c
void riscv_aplic_enable_src ( const struct device * dev, unsigned int src, bool enable )
```

启用或禁用中断源（Interrupt Source）。

控制指定中断源（Interrupt Source）是否可以产生中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 高级平台级中断控制器（APLIC）设备。 |
| `src` | 中断源编号。 |
| `enable` | `true` 表示启用，`false` 表示禁用。 |

<a id="a32492c238d531bf4474fa391aa634429"></a>

### `riscv_aplic_get_dev()`

```c
const struct device * riscv_aplic_get_dev ( void )
```

声明属性：`inline`、`static`。

获取 APLIC 设备实例（Device Instance）。

返回 APLIC 驱动的设备结构体（Device Structure）。

**返回（Returns）**：返回值（Returns）：指向 APLIC 设备的指针。

<a id="ab446350754c3f125e78ae3bf89e71636"></a>

### `riscv_aplic_get_num_sources()`

```c
uint32_t riscv_aplic_get_num_sources ( const struct device * dev)
```

获取中断源（Interrupt Source）的数量。

返回 APLIC 支持的中断源（Interrupt Source）数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 高级平台级中断控制器（APLIC）设备。 |

**返回（Returns）**：返回值（Returns）：中断源（Interrupt Source）的数量。

<a id="a871822d8d01a9428795df3bc7a183499"></a>

### `riscv_aplic_msi_inject_genmsi()`

```c
void riscv_aplic_msi_inject_genmsi ( uint32_t hart, uint32_t eiid )
```

声明属性：`inline`、`static`。

使用 `GENMSI` 注入 MSI 的便捷封装（Convenience Wrapper）。

使用默认 APLIC 设备（Device），向指定硬件线程（Hart）注入软件 MSI。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hart` | 目标硬件线程（Hart）的索引。 |
| `eiid` | 外部中断标识（External Interrupt Identity）。 |

<a id="afa4ce7bd64fb5c05ecef44088905f603"></a>

### `riscv_aplic_msi_inject_software_interrupt()`

```c
void riscv_aplic_msi_inject_software_interrupt ( const struct device * dev, uint32_t eiid, uint32_t hart_id, uint32_t context )
```

注入软件触发的 MSI（Software-triggered MSI）。

使用 `GENMSI` 寄存器，向指定硬件线程（Hart）触发 MSI。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 高级平台级中断控制器（APLIC）设备。 |
| `eiid` | 外部中断标识（External Interrupt Identity）。 |
| `hart_id` | 目标硬件线程（Hart）的索引。 |
| `context` | 上下文（Context）字段，用于 DMSI 模式。 |

<a id="a99ee07d894d3a09370d5ab0077359ac4"></a>

### `riscv_aplic_msi_route()`

```c
void riscv_aplic_msi_route ( const struct device * dev, unsigned int src, uint32_t hart, uint32_t eiid )
```

配置中断源（Interrupt Source）的 MSI 路由（Routing）。

设置指定源进行 MSI 投递（Delivery）时的目标硬件线程（Hart）和外部中断标识（EIID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 高级平台级中断控制器（APLIC）设备。 |
| `src` | 中断源编号。 |
| `hart` | 目标硬件线程（Hart）的索引。 |
| `eiid` | 目标 IMSIC 的外部中断标识（External Interrupt Identity）。 |


## 11.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P716_riscv_aplic.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_zephyr__net__net_ip.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__dt-bindings__gpio__st-zio-header.h_文件参考.md)
