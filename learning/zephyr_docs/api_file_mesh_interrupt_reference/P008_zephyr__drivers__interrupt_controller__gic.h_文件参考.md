---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-8
title: zephyr__drivers__interrupt_controller__gic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_gic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ARM通用中断控制器（Generic Interrupt Controller）的驱动。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
```

查看此文件的源码。

ARM 通用中断控制器（Generic Interrupt Controller，GIC）驱动。GIC 是 ARM A 类和 R 类核心的默认中断控制器。ARM 架构实现使用此驱动处理中断。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="r_adb371115c787d786755ca23eedc6a651"></a>

```c
#define GIC_DIST_BASE DT_REG_ADDR_BY_IDX(DT_INST(0, arm_gic), 0)
```

相关声明：[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)、[DT_REG_ADDR_BY_IDX](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac540b00bb12d0662f6aefe6ac0cff243)、[DT_INST](../dt_identity_reference/P001_设备树节点标识宏.md#gae199b930cb21ff38dab284a696093ead)。

<a id="r_a855f96fbf6e3c5645d7e4d610eb98664"></a>

```c
#define GIC_CPU_BASE DT_REG_ADDR_BY_IDX(DT_INST(0, arm_gic), 1)
```

相关声明：[GIC_CPU_BASE](#a855f96fbf6e3c5645d7e4d610eb98664)、[DT_REG_ADDR_BY_IDX](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac540b00bb12d0662f6aefe6ac0cff243)、[DT_INST](../dt_identity_reference/P001_设备树节点标识宏.md#gae199b930cb21ff38dab284a696093ead)。

<a id="r_a00f17ebce4b31e38e18375340fdf3826"></a>

```c
#define GICD_CTLR (GIC_DIST_BASE + 0x0)
```

相关声明：[GICD_CTLR](#a00f17ebce4b31e38e18375340fdf3826)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a1b97217a477f13f173ff4a22c0aeeef6"></a>

```c
#define GICD_TYPER (GIC_DIST_BASE + 0x4)
```

相关声明：[GICD_TYPER](#a1b97217a477f13f173ff4a22c0aeeef6)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a88abd454e14abb10903e32cc83649e07"></a>

```c
#define GICD_IIDR (GIC_DIST_BASE + 0x8)
```

相关声明：[GICD_IIDR](#a88abd454e14abb10903e32cc83649e07)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a1080fbe96176a41ccf2bd2387ff0db63"></a>

```c
#define GICD_IGROUPRn (GIC_DIST_BASE + 0x80)
```

相关声明：[GICD_IGROUPRn](#a1080fbe96176a41ccf2bd2387ff0db63)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a708bbd9e06c140f7af1fa82da8895862"></a>

```c
#define GICD_IGROUPRnE (GIC_DIST_BASE + 0x1000)
```

相关声明：[GICD_IGROUPRnE](#a708bbd9e06c140f7af1fa82da8895862)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a310ab6442912860cc32c4728323aa77d"></a>

```c
#define GICD_ISENABLERn (GIC_DIST_BASE + 0x100)
```

相关声明：[GICD_ISENABLERn](#a310ab6442912860cc32c4728323aa77d)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_ac025a607c04580cacf0c8acbdd11adbf"></a>

```c
#define GICD_ISENABLERnE (GIC_DIST_BASE + 0x1200)
```

相关声明：[GICD_ISENABLERnE](#ac025a607c04580cacf0c8acbdd11adbf)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a5c3d3ec71773c06de84fae6e9a4e0a09"></a>

```c
#define GICD_ICENABLERn (GIC_DIST_BASE + 0x180)
```

相关声明：[GICD_ICENABLERn](#a5c3d3ec71773c06de84fae6e9a4e0a09)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_ac727aed76e6b88a9ae7f5fcc8eeadc6b"></a>

```c
#define GICD_ICENABLERnE (GIC_DIST_BASE + 0x1400)
```

相关声明：[GICD_ICENABLERnE](#ac727aed76e6b88a9ae7f5fcc8eeadc6b)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a6f6edc1558ef636d46f09b68b7abe025"></a>

```c
#define GICD_ISPENDRn (GIC_DIST_BASE + 0x200)
```

相关声明：[GICD_ISPENDRn](#a6f6edc1558ef636d46f09b68b7abe025)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_abaa3fdc6750ad8a11b6ae13ad23d4455"></a>

```c
#define GICD_ISPENDRnE (GIC_DIST_BASE + 0x1600)
```

相关声明：[GICD_ISPENDRnE](#abaa3fdc6750ad8a11b6ae13ad23d4455)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_aeb43e488b1b2f321aa04973b92f55fde"></a>

```c
#define GICD_ICPENDRn (GIC_DIST_BASE + 0x280)
```

相关声明：[GICD_ICPENDRn](#aeb43e488b1b2f321aa04973b92f55fde)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a9d07d68d06a19deab790f8e9d908b1ed"></a>

```c
#define GICD_ICPENDRnE (GIC_DIST_BASE + 0x1800)
```

相关声明：[GICD_ICPENDRnE](#a9d07d68d06a19deab790f8e9d908b1ed)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a166410e3d61c7b967df532db8b541bf6"></a>

```c
#define GICD_ISACTIVERn (GIC_DIST_BASE + 0x300)
```

相关声明：[GICD_ISACTIVERn](#a166410e3d61c7b967df532db8b541bf6)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a5128486fe91db8fd38cf5d5c07dcf2b1"></a>

```c
#define GICD_ISACTIVERnE (GIC_DIST_BASE + 0x1A00)
```

相关声明：[GICD_ISACTIVERnE](#a5128486fe91db8fd38cf5d5c07dcf2b1)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_ac55442a1b5748b8fcc46a9630ecf1645"></a>

```c
#define GICD_IPRIORITYRn (GIC_DIST_BASE + 0x400)
```

相关声明：[GICD_IPRIORITYRn](#ac55442a1b5748b8fcc46a9630ecf1645)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_ab0596892abd30aeb2cb0f3bcb70b388a"></a>

```c
#define GICD_IPRIORITYRnE (GIC_DIST_BASE + 0x2000)
```

相关声明：[GICD_IPRIORITYRnE](#ab0596892abd30aeb2cb0f3bcb70b388a)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a9b05ed54bb00c209d8774edea5368d5d"></a>

```c
#define GICD_ITARGETSRn (GIC_DIST_BASE + 0x800)
```

相关声明：[GICD_ITARGETSRn](#a9b05ed54bb00c209d8774edea5368d5d)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a4683149b0af23adbf4b1c149be5d9fe5"></a>

```c
#define GICD_ICFGRn (GIC_DIST_BASE + 0xc00)
```

相关声明：[GICD_ICFGRn](#a4683149b0af23adbf4b1c149be5d9fe5)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a255b5836278cef9e538b11118a854944"></a>

```c
#define GICD_ICFGRnE (GIC_DIST_BASE + 0x3000)
```

相关声明：[GICD_ICFGRnE](#a255b5836278cef9e538b11118a854944)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a5125b5f77951f0e882e002aac406beec"></a>

```c
#define GICD_SGIR (GIC_DIST_BASE + 0xf00)
```

相关声明：[GICD_SGIR](#a5125b5f77951f0e882e002aac406beec)、[GIC_DIST_BASE](#adb371115c787d786755ca23eedc6a651)。

<a id="r_a11871e15a62cbfcc1e54f3dd2ce21e74"></a>

```c
#define GICC_CTLR (GIC_CPU_BASE + 0x0)
```

相关声明：[GICC_CTLR](#a11871e15a62cbfcc1e54f3dd2ce21e74)、[GIC_CPU_BASE](#a855f96fbf6e3c5645d7e4d610eb98664)。

<a id="r_a8d72b8216b091c1d148b5812bc46e7d4"></a>

```c
#define GICC_PMR (GIC_CPU_BASE + 0x4)
```

相关声明：[GICC_PMR](#a8d72b8216b091c1d148b5812bc46e7d4)、[GIC_CPU_BASE](#a855f96fbf6e3c5645d7e4d610eb98664)。

<a id="r_acef579bca73eb22cc132808fcfede353"></a>

```c
#define GICC_BPR (GIC_CPU_BASE + 0x8)
```

相关声明：[GICC_BPR](#acef579bca73eb22cc132808fcfede353)、[GIC_CPU_BASE](#a855f96fbf6e3c5645d7e4d610eb98664)。

<a id="r_a61672c3cde5301e076793c2ad904cdb9"></a>

```c
#define GICC_IAR (GIC_CPU_BASE + 0xc)
```

相关声明：[GICC_IAR](#a61672c3cde5301e076793c2ad904cdb9)、[GIC_CPU_BASE](#a855f96fbf6e3c5645d7e4d610eb98664)。

<a id="r_af92519fe60b0cf2183a6100bea15dd43"></a>

```c
#define GICC_EOIR (GIC_CPU_BASE + 0x10)
```

相关声明：[GICC_EOIR](#af92519fe60b0cf2183a6100bea15dd43)、[GIC_CPU_BASE](#a855f96fbf6e3c5645d7e4d610eb98664)。

<a id="r_a518810ec411ebf4fb128a86c3e256333"></a>

```c
#define GICC_CTLR_ENABLEGRP0 BIT(0)
```

相关声明：[GICC_CTLR_ENABLEGRP0](#a518810ec411ebf4fb128a86c3e256333)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a692e86e4ede5319e7480a358fe75172b"></a>

```c
#define GICC_CTLR_ENABLEGRP1 BIT(1)
```

相关声明：[GICC_CTLR_ENABLEGRP1](#a692e86e4ede5319e7480a358fe75172b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ad3403f63efc5ce1dc9f257602f2ff0ae"></a>

```c
#define GICC_CTLR_ENABLE_MASK (GICC_CTLR_ENABLEGRP0 | GICC_CTLR_ENABLEGRP1)
```

相关声明：[GICC_CTLR_ENABLE_MASK](#ad3403f63efc5ce1dc9f257602f2ff0ae)、[GICC_CTLR_ENABLEGRP0](#a518810ec411ebf4fb128a86c3e256333)、[GICC_CTLR_ENABLEGRP1](#a692e86e4ede5319e7480a358fe75172b)。

<a id="r_abb0a8279fd1bafe13b5b79ec7aeb3f90"></a>

```c
#define GICD_SGIR_TGTFILT(x)
```

相关声明：[GICD_SGIR_TGTFILT](#abb0a8279fd1bafe13b5b79ec7aeb3f90)。

<a id="r_a907207ff57799c57a6b84a928738d205"></a>

```c
#define GICD_SGIR_TGTFILT_CPULIST GICD_SGIR_TGTFILT(0b00)
```

相关声明：[GICD_SGIR_TGTFILT_CPULIST](#a907207ff57799c57a6b84a928738d205)、[GICD_SGIR_TGTFILT](#abb0a8279fd1bafe13b5b79ec7aeb3f90)。

<a id="r_a64b98ce10603ac8cb7bb356fa162a344"></a>

```c
#define GICD_SGIR_TGTFILT_ALLBUTREQ GICD_SGIR_TGTFILT(0b01)
```

相关声明：[GICD_SGIR_TGTFILT_ALLBUTREQ](#a64b98ce10603ac8cb7bb356fa162a344)、[GICD_SGIR_TGTFILT](#abb0a8279fd1bafe13b5b79ec7aeb3f90)。

<a id="r_ae759ef6f311a7279db5e7ccd68c80863"></a>

```c
#define GICD_SGIR_TGTFILT_REQONLY GICD_SGIR_TGTFILT(0b10)
```

相关声明：[GICD_SGIR_TGTFILT_REQONLY](#ae759ef6f311a7279db5e7ccd68c80863)、[GICD_SGIR_TGTFILT](#abb0a8279fd1bafe13b5b79ec7aeb3f90)。

<a id="r_a4dff39b6ec90ed14dea04fdd25abc1ce"></a>

```c
#define GICD_SGIR_CPULIST(x)
```

相关声明：[GICD_SGIR_CPULIST](#a4dff39b6ec90ed14dea04fdd25abc1ce)。

<a id="r_a124b8c93f6902e9166447dd735f5dc1a"></a>

```c
#define GICD_SGIR_CPULIST_CPU(n)
```

相关声明：[GICD_SGIR_CPULIST_CPU](#a124b8c93f6902e9166447dd735f5dc1a)。

<a id="r_a011479af47f54dfc94330092191aaac5"></a>

```c
#define GICD_SGIR_CPULIST_MASK 0xff
```

相关声明：[GICD_SGIR_CPULIST_MASK](#a011479af47f54dfc94330092191aaac5)。

<a id="r_a041824e4a8176f8bbbdac5bafe06fae7"></a>

```c
#define GICD_SGIR_NSATT BIT(15)
```

相关声明：[GICD_SGIR_NSATT](#a041824e4a8176f8bbbdac5bafe06fae7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae388207ec492448a22511cee6dcecedc"></a>

```c
#define GICD_SGIR_SGIINTID(x)
```

相关声明：[GICD_SGIR_SGIINTID](#ae388207ec492448a22511cee6dcecedc)。

<a id="r_a3f4886917dc8cf3a2c7d3b590fffbde2"></a>

```c
#define GICD_CTLR_DS BIT(6)
```

相关声明：[GICD_CTLR_DS](#a3f4886917dc8cf3a2c7d3b590fffbde2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

`0x000 GICD_CTLR` 的 DS（Disable Security，禁用安全性）位，即 v3/v3.1 中的第 6 位。参见 ARM GIC 架构规范中的 `GICD_CTLR`。

<a id="r_a44b5b4941c426cd73350eeea005beb8a"></a>

```c
#define GICD_ICFGR_MASK BIT_MASK(2)
```

相关声明：[GICD_ICFGR_MASK](#a44b5b4941c426cd73350eeea005beb8a)、[BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)。

<a id="r_a11ed86dd29db285527ff4474958ade81"></a>

```c
#define GICD_ICFGR_TYPE BIT(1)
```

相关声明：[GICD_ICFGR_TYPE](#a11ed86dd29db285527ff4474958ade81)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a74cbf9f2c19fb1a09f8936958b02503a"></a>

```c
#define GICD_TYPER_ITLINESNUM_MASK 0x1f
```

相关声明：[GICD_TYPER_ITLINESNUM_MASK](#a74cbf9f2c19fb1a09f8936958b02503a)。

<a id="r_a2b22db96d30050d2d33e7a116d778bbd"></a>

```c
#define GICD_TYPER_ESPI_MASK BIT(8)
```

相关声明：[GICD_TYPER_ESPI_MASK](#a2b22db96d30050d2d33e7a116d778bbd)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a62397b69dbb93be1a404d14c195cdb2f"></a>

```c
#define GICD_TYPER_IDBITS(typer)
```

相关声明：[GICD_TYPER_IDBITS](#a62397b69dbb93be1a404d14c195cdb2f)。

<a id="r_a87acbf5e0124561ba231e95cca1bbc7a"></a>

```c
#define GIC_SGI_INT_BASE 0
```

相关声明：[GIC_SGI_INT_BASE](#a87acbf5e0124561ba231e95cca1bbc7a)。

<a id="r_a63bca268593477e8c0b6bc58aa3ee85c"></a>

```c
#define GIC_PPI_INT_BASE 16
```

相关声明：[GIC_PPI_INT_BASE](#a63bca268593477e8c0b6bc58aa3ee85c)。

<a id="r_a9bb04de2bd1f9d4e304ecdbea6a63a85"></a>

```c
#define GIC_IS_SGI(intid)
```

相关声明：[GIC_IS_SGI](#a9bb04de2bd1f9d4e304ecdbea6a63a85)。

<a id="r_ad9e9ba1264c9e57922cc0b8ad2e4dfba"></a>

```c
#define GIC_SPI_INT_BASE 32
```

相关声明：[GIC_SPI_INT_BASE](#ad9e9ba1264c9e57922cc0b8ad2e4dfba)。

<a id="r_a1deeb13c2ac681cb120c06b18dee2b91"></a>

```c
#define GIC_SPI_MAX_INTID 1019
```

相关声明：[GIC_SPI_MAX_INTID](#a1deeb13c2ac681cb120c06b18dee2b91)。

<a id="r_aa2672b14cfaa1a943bf1633e208ba288"></a>

```c
#define GIC_IS_SPI(intid)
```

相关声明：[GIC_IS_SPI](#aa2672b14cfaa1a943bf1633e208ba288)。

<a id="r_aed0af65dd3212045aeb0906d2d937ad5"></a>

```c
#define GIC_NUM_INTR_PER_REG 32
```

相关声明：[GIC_NUM_INTR_PER_REG](#aed0af65dd3212045aeb0906d2d937ad5)。

<a id="r_ad563564c4794a65475474fd8c19f7b41"></a>

```c
#define GIC_NUM_CFG_PER_REG 16
```

相关声明：[GIC_NUM_CFG_PER_REG](#ad563564c4794a65475474fd8c19f7b41)。

<a id="r_abb00f7fda87b16903a1fbcdd85d660bf"></a>

```c
#define GIC_NUM_PRI_PER_REG 4
```

相关声明：[GIC_NUM_PRI_PER_REG](#abb00f7fda87b16903a1fbcdd85d660bf)。

<a id="r_ae29667ceb670f4fabfc442350e8d4152"></a>

```c
#define GIC_IDLE_PRIO 0xff
```

相关声明：[GIC_IDLE_PRIO](#ae29667ceb670f4fabfc442350e8d4152)。

<a id="r_aaa5afc14eff8f002060b52030783cc47"></a>

```c
#define GIC_PRI_MASK 0xff
```

相关声明：[GIC_PRI_MASK](#aaa5afc14eff8f002060b52030783cc47)。

<a id="r_a94e122b157b3e50259581bd1d2f319a1"></a>

```c
#define GIC_INT_DEF_PRI_X4 0xa0a0a0a0
```

相关声明：[GIC_INT_DEF_PRI_X4](#a94e122b157b3e50259581bd1d2f319a1)。

<a id="r_a6ac20d04f13472d5dd915197af39aaf3"></a>

```c
#define GIC_INTID_SPURIOUS 1023
```

相关声明：[GIC_INTID_SPURIOUS](#a6ac20d04f13472d5dd915197af39aaf3)。

<a id="r_a24a62a86eb885f9f47e8bfdc430e8292"></a>

```c
#define GIC_NUM_CPU_IF CONFIG_MP_MAX_NUM_CPUS
```

相关声明：[GIC_NUM_CPU_IF](#a24a62a86eb885f9f47e8bfdc430e8292)。

对称多处理（SMP）环境中支持的最大 CPU 数量。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.2\_函数（Functions）

<a id="r_a585b5b22a16dab6999ab94dae30f4e71"></a>

```c
void arm_gic_irq_enable (unsigned int irq)
```

相关声明：[arm_gic_irq_enable](#a585b5b22a16dab6999ab94dae30f4e71)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

启用中断（interrupt）。

<a id="r_a3f5ec5c6b16fbac66cd02459d6045742"></a>

```c
void arm_gic_irq_disable (unsigned int irq)
```

相关声明：[arm_gic_irq_disable](#a3f5ec5c6b16fbac66cd02459d6045742)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

禁用中断。

<a id="r_acfa77cdcf46cad1181476bc3b974b58e"></a>

```c
bool arm_gic_irq_is_enabled (unsigned int irq)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[arm_gic_irq_is_enabled](#acfa77cdcf46cad1181476bc3b974b58e)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

检查中断是否已启用。

<a id="r_ad0cc0929cc6e0336448d45ebd27a45bd"></a>

```c
bool arm_gic_irq_is_pending (unsigned int irq)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[arm_gic_irq_is_pending](#ad0cc0929cc6e0336448d45ebd27a45bd)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

检查中断是否挂起（Pending）。

<a id="r_aa9e67bf28cee4b9382ebdc641874d2f8"></a>

```c
void arm_gic_irq_set_pending (unsigned int irq)
```

相关声明：[arm_gic_irq_set_pending](#aa9e67bf28cee4b9382ebdc641874d2f8)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

将中断设为待处理状态（Pending）。

<a id="r_a2980cdb020c9d8a886bf9d4fd485121b"></a>

```c
void arm_gic_irq_clear_pending (unsigned int irq)
```

相关声明：[arm_gic_irq_clear_pending](#a2980cdb020c9d8a886bf9d4fd485121b)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

清除挂起的中断请求（Pending IRQ）。

<a id="r_ad5eb3fc988f7077dc9600e62d768b076"></a>

```c
void arm_gic_irq_set_priority (unsigned int irq, unsigned int prio, unsigned int flags)
```

相关声明：[arm_gic_irq_set_priority](#ad5eb3fc988f7077dc9600e62d768b076)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

设置中断优先级（priority）。

<a id="r_a967a15ed8b1eeacde827b5a396867671"></a>

```c
void arm_gic_irq_set_affinity (unsigned int irq, uint64_t mpidr)
```

相关声明：[arm_gic_irq_set_affinity](#a967a15ed8b1eeacde827b5a396867671)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

将共享外设中断（SPI）或扩展 SPI 路由到指定核心。

<a id="r_ae545623722c1b45fda2b58155f3fd0ed"></a>

```c
unsigned int arm_gic_get_active (void)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[arm_gic_get_active](#ae545623722c1b45fda2b58155f3fd0ed)。

获取活动中断 ID（Active Interrupt ID）。

<a id="r_a4bfb597ef68cc7f83d86ba52e099e3b4"></a>

```c
void arm_gic_eoi (unsigned int irq)
```

相关声明：[arm_gic_eoi](#a4bfb597ef68cc7f83d86ba52e099e3b4)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

发出中断结束信号（End-of-interrupt）。

<a id="r_a3c2d3adf07e2d48bdf863d8142a685aa"></a>

```c
void arm_gic_secondary_init (void)
```

相关声明：[arm_gic_secondary_init](#a3c2d3adf07e2d48bdf863d8142a685aa)。

初始化次级核心（Secondary Cores）的 GIC。

<a id="r_a08291705f002f01687cf507abbb410dc"></a>

```c
void gic_raise_sgi (unsigned int sgi_id, uint64_t target_aff, uint16_t target_list)
```

相关声明：[gic_raise_sgi](#a08291705f002f01687cf507abbb410dc)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向目标核心触发软件生成中断（SGI）。

## 8.3\_详细说明（Detailed Documentation）

<a id="a855f96fbf6e3c5645d7e4d610eb98664"></a>

### `GIC_CPU_BASE`

```c
#define GIC_CPU_BASE DT_REG_ADDR_BY_IDX(DT_INST(0, arm_gic), 1)
```

<a id="adb371115c787d786755ca23eedc6a651"></a>

### `GIC_DIST_BASE`

```c
#define GIC_DIST_BASE DT_REG_ADDR_BY_IDX(DT_INST(0, arm_gic), 0)
```

<a id="ae29667ceb670f4fabfc442350e8d4152"></a>

### `GIC_IDLE_PRIO`

```c
#define GIC_IDLE_PRIO 0xff
```

<a id="a94e122b157b3e50259581bd1d2f319a1"></a>

### `GIC_INT_DEF_PRI_X4`

```c
#define GIC_INT_DEF_PRI_X4 0xa0a0a0a0
```

<a id="a6ac20d04f13472d5dd915197af39aaf3"></a>

### `GIC_INTID_SPURIOUS`

```c
#define GIC_INTID_SPURIOUS 1023
```

<a id="a9bb04de2bd1f9d4e304ecdbea6a63a85"></a>

### `GIC_IS_SGI`

```c
#define GIC_IS_SGI ( intid)
```

展开值（Value）：

```c
(((intid) >= GIC_SGI_INT_BASE) && ((intid) < GIC_PPI_INT_BASE))
```

<a id="aa2672b14cfaa1a943bf1633e208ba288"></a>

### `GIC_IS_SPI`

```c
#define GIC_IS_SPI ( intid)
```

展开值（Value）：

```c
(((intid) >= GIC_SPI_INT_BASE) && ((intid) <= GIC_SPI_MAX_INTID))
```

<a id="ad563564c4794a65475474fd8c19f7b41"></a>

### `GIC_NUM_CFG_PER_REG`

```c
#define GIC_NUM_CFG_PER_REG 16
```

<a id="a24a62a86eb885f9f47e8bfdc430e8292"></a>

### `GIC_NUM_CPU_IF`

```c
#define GIC_NUM_CPU_IF CONFIG_MP_MAX_NUM_CPUS
```

对称多处理（SMP）环境中支持的最大 CPU 数量。

待修复（Fixme）：应从平台专用定义或设备树（DT）更新。已弃用（Deprecated），请改用 `CONFIG_MP_MAX_NUM_CPUS`。

<a id="aed0af65dd3212045aeb0906d2d937ad5"></a>

### `GIC_NUM_INTR_PER_REG`

```c
#define GIC_NUM_INTR_PER_REG 32
```

<a id="abb00f7fda87b16903a1fbcdd85d660bf"></a>

### `GIC_NUM_PRI_PER_REG`

```c
#define GIC_NUM_PRI_PER_REG 4
```

<a id="a63bca268593477e8c0b6bc58aa3ee85c"></a>

### `GIC_PPI_INT_BASE`

```c
#define GIC_PPI_INT_BASE 16
```

<a id="aaa5afc14eff8f002060b52030783cc47"></a>

### `GIC_PRI_MASK`

```c
#define GIC_PRI_MASK 0xff
```

<a id="a87acbf5e0124561ba231e95cca1bbc7a"></a>

### `GIC_SGI_INT_BASE`

```c
#define GIC_SGI_INT_BASE 0
```

<a id="ad9e9ba1264c9e57922cc0b8ad2e4dfba"></a>

### `GIC_SPI_INT_BASE`

```c
#define GIC_SPI_INT_BASE 32
```

<a id="a1deeb13c2ac681cb120c06b18dee2b91"></a>

### `GIC_SPI_MAX_INTID`

```c
#define GIC_SPI_MAX_INTID 1019
```

<a id="acef579bca73eb22cc132808fcfede353"></a>

### `GICC_BPR`

```c
#define GICC_BPR (GIC_CPU_BASE + 0x8)
```

<a id="a11871e15a62cbfcc1e54f3dd2ce21e74"></a>

### `GICC_CTLR`

```c
#define GICC_CTLR (GIC_CPU_BASE + 0x0)
```

<a id="ad3403f63efc5ce1dc9f257602f2ff0ae"></a>

### `GICC_CTLR_ENABLE_MASK`

```c
#define GICC_CTLR_ENABLE_MASK (GICC_CTLR_ENABLEGRP0 | GICC_CTLR_ENABLEGRP1)
```

<a id="a518810ec411ebf4fb128a86c3e256333"></a>

### `GICC_CTLR_ENABLEGRP0`

```c
#define GICC_CTLR_ENABLEGRP0 BIT(0)
```

<a id="a692e86e4ede5319e7480a358fe75172b"></a>

### `GICC_CTLR_ENABLEGRP1`

```c
#define GICC_CTLR_ENABLEGRP1 BIT(1)
```

<a id="af92519fe60b0cf2183a6100bea15dd43"></a>

### `GICC_EOIR`

```c
#define GICC_EOIR (GIC_CPU_BASE + 0x10)
```

<a id="a61672c3cde5301e076793c2ad904cdb9"></a>

### `GICC_IAR`

```c
#define GICC_IAR (GIC_CPU_BASE + 0xc)
```

<a id="a8d72b8216b091c1d148b5812bc46e7d4"></a>

### `GICC_PMR`

```c
#define GICC_PMR (GIC_CPU_BASE + 0x4)
```

<a id="a00f17ebce4b31e38e18375340fdf3826"></a>

### `GICD_CTLR`

```c
#define GICD_CTLR (GIC_DIST_BASE + 0x0)
```

<a id="a3f4886917dc8cf3a2c7d3b590fffbde2"></a>

### `GICD_CTLR_DS`

```c
#define GICD_CTLR_DS BIT(6)
```

`0x000 GICD_CTLR` 的 DS（Disable Security，禁用安全性）位，即 v3/v3.1 中的第 6 位。参见 ARM GIC 架构规范中的 `GICD_CTLR`。

<a id="a5c3d3ec71773c06de84fae6e9a4e0a09"></a>

### `GICD_ICENABLERn`

```c
#define GICD_ICENABLERn (GIC_DIST_BASE + 0x180)
```

<a id="ac727aed76e6b88a9ae7f5fcc8eeadc6b"></a>

### `GICD_ICENABLERnE`

```c
#define GICD_ICENABLERnE (GIC_DIST_BASE + 0x1400)
```

<a id="a44b5b4941c426cd73350eeea005beb8a"></a>

### `GICD_ICFGR_MASK`

```c
#define GICD_ICFGR_MASK BIT_MASK(2)
```

<a id="a11ed86dd29db285527ff4474958ade81"></a>

### `GICD_ICFGR_TYPE`

```c
#define GICD_ICFGR_TYPE BIT(1)
```

<a id="a4683149b0af23adbf4b1c149be5d9fe5"></a>

### `GICD_ICFGRn`

```c
#define GICD_ICFGRn (GIC_DIST_BASE + 0xc00)
```

<a id="a255b5836278cef9e538b11118a854944"></a>

### `GICD_ICFGRnE`

```c
#define GICD_ICFGRnE (GIC_DIST_BASE + 0x3000)
```

<a id="aeb43e488b1b2f321aa04973b92f55fde"></a>

### `GICD_ICPENDRn`

```c
#define GICD_ICPENDRn (GIC_DIST_BASE + 0x280)
```

<a id="a9d07d68d06a19deab790f8e9d908b1ed"></a>

### `GICD_ICPENDRnE`

```c
#define GICD_ICPENDRnE (GIC_DIST_BASE + 0x1800)
```

<a id="a1080fbe96176a41ccf2bd2387ff0db63"></a>

### `GICD_IGROUPRn`

```c
#define GICD_IGROUPRn (GIC_DIST_BASE + 0x80)
```

<a id="a708bbd9e06c140f7af1fa82da8895862"></a>

### `GICD_IGROUPRnE`

```c
#define GICD_IGROUPRnE (GIC_DIST_BASE + 0x1000)
```

<a id="a88abd454e14abb10903e32cc83649e07"></a>

### `GICD_IIDR`

```c
#define GICD_IIDR (GIC_DIST_BASE + 0x8)
```

<a id="ac55442a1b5748b8fcc46a9630ecf1645"></a>

### `GICD_IPRIORITYRn`

```c
#define GICD_IPRIORITYRn (GIC_DIST_BASE + 0x400)
```

<a id="ab0596892abd30aeb2cb0f3bcb70b388a"></a>

### `GICD_IPRIORITYRnE`

```c
#define GICD_IPRIORITYRnE (GIC_DIST_BASE + 0x2000)
```

<a id="a166410e3d61c7b967df532db8b541bf6"></a>

### `GICD_ISACTIVERn`

```c
#define GICD_ISACTIVERn (GIC_DIST_BASE + 0x300)
```

<a id="a5128486fe91db8fd38cf5d5c07dcf2b1"></a>

### `GICD_ISACTIVERnE`

```c
#define GICD_ISACTIVERnE (GIC_DIST_BASE + 0x1A00)
```

<a id="a310ab6442912860cc32c4728323aa77d"></a>

### `GICD_ISENABLERn`

```c
#define GICD_ISENABLERn (GIC_DIST_BASE + 0x100)
```

<a id="ac025a607c04580cacf0c8acbdd11adbf"></a>

### `GICD_ISENABLERnE`

```c
#define GICD_ISENABLERnE (GIC_DIST_BASE + 0x1200)
```

<a id="a6f6edc1558ef636d46f09b68b7abe025"></a>

### `GICD_ISPENDRn`

```c
#define GICD_ISPENDRn (GIC_DIST_BASE + 0x200)
```

<a id="abaa3fdc6750ad8a11b6ae13ad23d4455"></a>

### `GICD_ISPENDRnE`

```c
#define GICD_ISPENDRnE (GIC_DIST_BASE + 0x1600)
```

<a id="a9b05ed54bb00c209d8774edea5368d5d"></a>

### `GICD_ITARGETSRn`

```c
#define GICD_ITARGETSRn (GIC_DIST_BASE + 0x800)
```

<a id="a5125b5f77951f0e882e002aac406beec"></a>

### `GICD_SGIR`

```c
#define GICD_SGIR (GIC_DIST_BASE + 0xf00)
```

<a id="a4dff39b6ec90ed14dea04fdd25abc1ce"></a>

### `GICD_SGIR_CPULIST`

```c
#define GICD_SGIR_CPULIST ( x)
```

展开值（Value）：

```c
((x) << 16)
```

<a id="a124b8c93f6902e9166447dd735f5dc1a"></a>

### `GICD_SGIR_CPULIST_CPU`

```c
#define GICD_SGIR_CPULIST_CPU ( n)
```

展开值（Value）：

```c
GICD_SGIR_CPULIST(BIT(n))
```

<a id="a011479af47f54dfc94330092191aaac5"></a>

### `GICD_SGIR_CPULIST_MASK`

```c
#define GICD_SGIR_CPULIST_MASK 0xff
```

<a id="a041824e4a8176f8bbbdac5bafe06fae7"></a>

### `GICD_SGIR_NSATT`

```c
#define GICD_SGIR_NSATT BIT(15)
```

<a id="ae388207ec492448a22511cee6dcecedc"></a>

### `GICD_SGIR_SGIINTID`

```c
#define GICD_SGIR_SGIINTID ( x)
```

展开值（Value）：

```c
(x)
```

<a id="abb0a8279fd1bafe13b5b79ec7aeb3f90"></a>

### `GICD_SGIR_TGTFILT`

```c
#define GICD_SGIR_TGTFILT ( x)
```

展开值（Value）：

```c
((x) << 24)
```

<a id="a64b98ce10603ac8cb7bb356fa162a344"></a>

### `GICD_SGIR_TGTFILT_ALLBUTREQ`

```c
#define GICD_SGIR_TGTFILT_ALLBUTREQ GICD_SGIR_TGTFILT(0b01)
```

<a id="a907207ff57799c57a6b84a928738d205"></a>

### `GICD_SGIR_TGTFILT_CPULIST`

```c
#define GICD_SGIR_TGTFILT_CPULIST GICD_SGIR_TGTFILT(0b00)
```

<a id="ae759ef6f311a7279db5e7ccd68c80863"></a>

### `GICD_SGIR_TGTFILT_REQONLY`

```c
#define GICD_SGIR_TGTFILT_REQONLY GICD_SGIR_TGTFILT(0b10)
```

<a id="a1b97217a477f13f173ff4a22c0aeeef6"></a>

### `GICD_TYPER`

```c
#define GICD_TYPER (GIC_DIST_BASE + 0x4)
```

<a id="a2b22db96d30050d2d33e7a116d778bbd"></a>

### `GICD_TYPER_ESPI_MASK`

```c
#define GICD_TYPER_ESPI_MASK BIT(8)
```

<a id="a62397b69dbb93be1a404d14c195cdb2f"></a>

### `GICD_TYPER_IDBITS`

```c
#define GICD_TYPER_IDBITS ( typer)
```

展开值（Value）：

```c
((((typer) >> 19) & 0x1f) + 1)
```

<a id="a74cbf9f2c19fb1a09f8936958b02503a"></a>

### `GICD_TYPER_ITLINESNUM_MASK`

```c
#define GICD_TYPER_ITLINESNUM_MASK 0x1f
```

<a id="a4bfb597ef68cc7f83d86ba52e099e3b4"></a>

### `arm_gic_eoi()`

```c
void arm_gic_eoi ( unsigned int irq)
```

发出中断结束信号（End-of-interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |

<a id="ae545623722c1b45fda2b58155f3fd0ed"></a>

### `arm_gic_get_active()`

```c
unsigned int arm_gic_get_active ( void )
```

获取活动中断 ID（Active Interrupt ID）。

**返回（Returns）**：**返回值（Returns）：**活动中断（Active Interrupt）的 ID。

<a id="a2980cdb020c9d8a886bf9d4fd485121b"></a>

### `arm_gic_irq_clear_pending()`

```c
void arm_gic_irq_clear_pending ( unsigned int irq)
```

清除挂起的中断请求（Pending IRQ）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |

<a id="a3f5ec5c6b16fbac66cd02459d6045742"></a>

### `arm_gic_irq_disable()`

```c
void arm_gic_irq_disable ( unsigned int irq)
```

禁用中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |

<a id="a585b5b22a16dab6999ab94dae30f4e71"></a>

### `arm_gic_irq_enable()`

```c
void arm_gic_irq_enable ( unsigned int irq)
```

启用中断（interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |

<a id="acfa77cdcf46cad1181476bc3b974b58e"></a>

### `arm_gic_irq_is_enabled()`

```c
bool arm_gic_irq_is_enabled ( unsigned int irq)
```

检查中断是否已启用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |

**返回（Returns）**：返回值：中断已启用时返回 true，否则返回 false。

<a id="ad0cc0929cc6e0336448d45ebd27a45bd"></a>

### `arm_gic_irq_is_pending()`

```c
bool arm_gic_irq_is_pending ( unsigned int irq)
```

检查中断是否挂起（Pending）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |

**返回（Returns）**：返回值：中断挂起（Pending）时返回 `true`，否则返回 `false`。

<a id="a967a15ed8b1eeacde827b5a396867671"></a>

### `arm_gic_irq_set_affinity()`

```c
void arm_gic_irq_set_affinity ( unsigned int irq, uint64_t mpidr )
```

将共享外设中断（SPI）或扩展 SPI 路由到指定核心。

为 `irq` 配置 `GICD_IROUTER`，采用指定亲和性路由（Specific-affinity Routing，`IRM=0`），将目标设置为 `mpidr` 标识的核心，类似于用 `k_thread_cpu_pin()` 将线程固定到某个 CPU。仅适用于 SPI／扩展 SPI，而且仅在 GICv3 亲和性路由本身已启用，即 `GICD_CTLR.ARE_S/ARE_NS` 已启用时生效。启用 `CONFIG_ARMV8_A_NS` 或 `CONFIG_GIC_SINGLE_SECURITY_STATE` 的构建默认满足此条件；自身 EL3／安全预初始化（Secure Pre-init）已开启该功能的 SoC 也满足此条件。

中断连接后，任何核心都可随时调用。`arm_gic_irq_enable()` 的隐式自身亲和性（Self-affinity）始终以调用它的核心为目标，而此接口可指定任意核心。若在 `arm_gic_irq_enable()` 之后调用，则以本次调用的目标为准。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断 ID，必须是共享外设中断（SPI）或扩展 SPI。 |
| `mpidr` | 目标核心的 MPIDR 亲和性值（Affinity Value）。在 arm64 上，可从特定 CPU 的设备树节点获取，即 `DT_REG_ADDR(DT_NODELABEL(cpuX))`；若目标是调用方当前固定到的核心，则可使用 `MPIDR_TO_CORE(GET_MPIDR())`。 |

<a id="aa9e67bf28cee4b9382ebdc641874d2f8"></a>

### `arm_gic_irq_set_pending()`

```c
void arm_gic_irq_set_pending ( unsigned int irq)
```

将中断设为待处理状态（Pending）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |

<a id="ad5eb3fc988f7077dc9600e62d768b076"></a>

### `arm_gic_irq_set_priority()`

```c
void arm_gic_irq_set_priority ( unsigned int irq, unsigned int prio, unsigned int flags )
```

设置中断优先级（priority）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `irq` | 中断标识符（interrupt ID）。 |
| `prio` | 中断优先级。 |
| `flags` | 中断标志（interrupt flags）。 |

<a id="a3c2d3adf07e2d48bdf863d8142a685aa"></a>

### `arm_gic_secondary_init()`

```c
void arm_gic_secondary_init ( void )
```

初始化次级核心（Secondary Cores）的 GIC。

<a id="a08291705f002f01687cf507abbb410dc"></a>

### `gic_raise_sgi()`

```c
void gic_raise_sgi ( unsigned int sgi_id, uint64_t target_aff, uint16_t target_list )
```

向目标核心触发软件生成中断（SGI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sgi_id` | 软件生成中断（SGI）ID，范围为 0 至 15。 |
| `target_aff` | 以 MPIDR 形式表示的目标亲和性（Target Affinity）。API 会提取亲和性层级 1、2、3。 |
| `target_list` | 目标核心位掩码（Target Core Bitmask）。 |


## 8.4\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_scheduler_interrupt_reference/P003_gic.h_源码浏览.md)
- [DT_REG_ADDR_BY_IDX](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac540b00bb12d0662f6aefe6ac0cff243)
- [DT_INST](../dt_identity_reference/P001_设备树节点标识宏.md#gae199b930cb21ff38dab284a696093ead)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BIT_MASK](../util_reference/P001_通用工具公共接口.md#ga3c12c6d36ad0aa481a3436923d21f4f8)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [k_thread_cpu_pin()](../thread_core_reference/P001_线程公共接口.md#gae9ebd9845e14ed02944ab9282a185c03)
- [DT_REG_ADDR(DT_NODELABEL(cpuX))](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agic_8h_html_a63bca268593477e8c0b6bc58aa3ee85c"></a>
<a id="agic_8h_html_a87acbf5e0124561ba231e95cca1bbc7a"></a>
<a id="agic_8h_html_a1deeb13c2ac681cb120c06b18dee2b91"></a>
<a id="agic_8h_html_ad9e9ba1264c9e57922cc0b8ad2e4dfba"></a>
<a id="agic_8h_html_a4dff39b6ec90ed14dea04fdd25abc1ce"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_zephyr__drivers__ethernet__eth_adin2111.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__drivers__haptics.h_文件参考.md)
