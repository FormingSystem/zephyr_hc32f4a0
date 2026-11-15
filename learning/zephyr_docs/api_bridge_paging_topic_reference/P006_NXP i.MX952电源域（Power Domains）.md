---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-6
title: NXP i.MX952电源域（Power Domains）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__power__domains.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_NXP i.MX952电源域（Power Domains）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__power__domains.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

i.MX952 系统级芯片（SoC）的电源域分区索引（Power Domain Slice Indices）。

<a id="details"></a>

i.MX952 系统级芯片（SoC）的电源域分区索引（Power Domain Slice Indices）。

<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_imx952_5Fpower_2Eh"></a>

```c
file imx952_power.h
```

相关声明：[imx952_power.h](https://docs.zephyrproject.org/latest/doxygen/html/imx952__power_8h.html)。

NXP i.MX952片上系统（SoC）的电源域定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ga619e535321d78b4673b3d75b6a6eabc9"></a>

```c
#define IMX952_PD_ANA 0
```

相关声明：[IMX952_PD_ANA](#ga619e535321d78b4673b3d75b6a6eabc9)。

模拟电源域（Analog Power Domain）。

<a id="r_ga39eb7b17cd2d75f9dd5389cfe046ee88"></a>

```c
#define IMX952_PD_AON 1
```

相关声明：[IMX952_PD_AON](#ga39eb7b17cd2d75f9dd5389cfe046ee88)。

常开电源域（Always-on Power Domain）。

<a id="r_ga2dc16076c0c135b4b9b47775d36d2d59"></a>

```c
#define IMX952_PD_BBSM 2
```

相关声明：[IMX952_PD_BBSM](#ga2dc16076c0c135b4b9b47775d36d2d59)。

电池备份安全模块（Battery-Backed Security Module，BBSM）电源域（Power Domain）。

<a id="r_gabd36ed3b0a37bdbfaffb3297b81a5376"></a>

```c
#define IMX952_PD_CAMERA 3
```

相关声明：[IMX952_PD_CAMERA](#gabd36ed3b0a37bdbfaffb3297b81a5376)。

摄像头子系统电源域（Camera Subsystem Power Domain）。

<a id="r_ga786258ae435f51f07024a776f29f8d7b"></a>

```c
#define IMX952_PD_CCMSRCGPC 4
```

相关声明：[IMX952_PD_CCMSRCGPC](#ga786258ae435f51f07024a776f29f8d7b)。

CCM/SRC/GPC 电源域（Power Domain）。

<a id="r_ga8ee90b8928e7e64218c3e23e70511196"></a>

```c
#define IMX952_PD_A55C0 5
```

相关声明：[IMX952_PD_A55C0](#ga8ee90b8928e7e64218c3e23e70511196)。

A55 核心 0 电源域（Core 0 Power Domain）。

<a id="r_gad80e363b3b47fa5ace41b822adac9f0f"></a>

```c
#define IMX952_PD_A55C1 6
```

相关声明：[IMX952_PD_A55C1](#gad80e363b3b47fa5ace41b822adac9f0f)。

A55 核心 1 电源域（Core 1 Power Domain）。

<a id="r_ga1d5bddbc3572302bb02f399b587c627f"></a>

```c
#define IMX952_PD_A55C2 7
```

相关声明：[IMX952_PD_A55C2](#ga1d5bddbc3572302bb02f399b587c627f)。

A55 核心 2 电源域（Core 2 Power Domain）。

<a id="r_gae1f7f2e3a82b1303d7a1618c08cccfac"></a>

```c
#define IMX952_PD_A55C3 8
```

相关声明：[IMX952_PD_A55C3](#gae1f7f2e3a82b1303d7a1618c08cccfac)。

A55 核心 3 电源域（Core 3 Power Domain）。

<a id="r_ga93494b335e5e04da23562dd761c527e5"></a>

```c
#define IMX952_PD_A55P 9
```

相关声明：[IMX952_PD_A55P](#ga93494b335e5e04da23562dd761c527e5)。

A55 平台电源域（Platform Power Domain）。

<a id="r_ga7f2f4cdd4c50d5f7a302cc5213917228"></a>

```c
#define IMX952_PD_DDR 10
```

相关声明：[IMX952_PD_DDR](#ga7f2f4cdd4c50d5f7a302cc5213917228)。

DDR 子系统电源域（Subsystem Power Domain）。

<a id="r_ga7f834f86e948737624fd92f389bce6af"></a>

```c
#define IMX952_PD_DISPLAY 11
```

相关声明：[IMX952_PD_DISPLAY](#ga7f834f86e948737624fd92f389bce6af)。

显示子系统电源域（Display Subsystem Power Domain）。

<a id="r_gab6a63f2c0b270591fe47e1ac7fc20dfd"></a>

```c
#define IMX952_PD_GPU 12
```

相关声明：[IMX952_PD_GPU](#gab6a63f2c0b270591fe47e1ac7fc20dfd)。

图形处理器（GPU）电源域（Power Domain）。

<a id="r_ga7ad60973e1deff63776b4aafe1f41c70"></a>

```c
#define IMX952_PD_HSIO_TOP 13
```

相关声明：[IMX952_PD_HSIO_TOP](#ga7ad60973e1deff63776b4aafe1f41c70)。

HSIO 顶层电源域（Top Power Domain）。

<a id="r_ga3ca1417fe6cfd397538d99c1c7487bf8"></a>

```c
#define IMX952_PD_HSIO_WAON 14
```

相关声明：[IMX952_PD_HSIO_WAON](#ga3ca1417fe6cfd397538d99c1c7487bf8)。

HSIO Wakeup-AON 唤醒常开电源域（Power Domain）。

<a id="r_gab3cd24dd2ee9e8c53484b75723d1708e"></a>

```c
#define IMX952_PD_M7 15
```

相关声明：[IMX952_PD_M7](#gab3cd24dd2ee9e8c53484b75723d1708e)。

M7 核心电源域（Core Power Domain）。

<a id="r_gae952e18ba9705dcf1b6236da8d799944"></a>

```c
#define IMX952_PD_NETC 16
```

相关声明：[IMX952_PD_NETC](#gae952e18ba9705dcf1b6236da8d799944)。

网络控制器（Network Controller，NETC）电源域（Power Domain）。

<a id="r_gaeb8e91004d08f68eacd56c688133a1cf"></a>

```c
#define IMX952_PD_NOC 17
```

相关声明：[IMX952_PD_NOC](#gaeb8e91004d08f68eacd56c688133a1cf)。

片上网络（Network-on-Chip，NOC）电源域（Power Domain）。

<a id="r_ga15002babf2edb32c6fd9a59fb15cfcb1"></a>

```c
#define IMX952_PD_NPU 18
```

相关声明：[IMX952_PD_NPU](#ga15002babf2edb32c6fd9a59fb15cfcb1)。

神经网络处理单元（Neural Processing Unit，NPU）电源域（Power Domain）。

<a id="r_ga1d8d9b7357b28a609c5c398f04ab0d17"></a>

```c
#define IMX952_PD_VPU 19
```

相关声明：[IMX952_PD_VPU](#ga1d8d9b7357b28a609c5c398f04ab0d17)。

视频处理单元（Video Processing Unit，VPU）电源域（Power Domain）。

<a id="r_gac4b193eaea6286c428d7f723ab9de916"></a>

```c
#define IMX952_PD_WAKEUP 20
```

相关声明：[IMX952_PD_WAKEUP](#gac4b193eaea6286c428d7f723ab9de916)。

唤醒域电源域（Wakeup Domain Power Domain）。

<a id="r_ga5d9625e864121e82e7d87cc1f8b9c13f"></a>

```c
#define IMX952_NUM_MIX_SLICE 21
```

相关声明：[IMX952_NUM_MIX_SLICE](#ga5d9625e864121e82e7d87cc1f8b9c13f)。

MIX 电源域分片（Power Domain Slices）总数。

## 6.3\_详细说明（Detailed Documentation）

<a id="ga5d9625e864121e82e7d87cc1f8b9c13f"></a>

### `IMX952_NUM_MIX_SLICE`

```c
#define IMX952_NUM_MIX_SLICE 21
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

MIX 电源域分片（Power Domain Slices）总数。

<a id="ga8ee90b8928e7e64218c3e23e70511196"></a>

### `IMX952_PD_A55C0`

```c
#define IMX952_PD_A55C0 5
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

A55 核心 0 电源域（Core 0 Power Domain）。

<a id="gad80e363b3b47fa5ace41b822adac9f0f"></a>

### `IMX952_PD_A55C1`

```c
#define IMX952_PD_A55C1 6
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

A55 核心 1 电源域（Core 1 Power Domain）。

<a id="ga1d5bddbc3572302bb02f399b587c627f"></a>

### `IMX952_PD_A55C2`

```c
#define IMX952_PD_A55C2 7
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

A55 核心 2 电源域（Core 2 Power Domain）。

<a id="gae1f7f2e3a82b1303d7a1618c08cccfac"></a>

### `IMX952_PD_A55C3`

```c
#define IMX952_PD_A55C3 8
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

A55 核心 3 电源域（Core 3 Power Domain）。

<a id="ga93494b335e5e04da23562dd761c527e5"></a>

### `IMX952_PD_A55P`

```c
#define IMX952_PD_A55P 9
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

A55 平台电源域（Platform Power Domain）。

<a id="ga619e535321d78b4673b3d75b6a6eabc9"></a>

### `IMX952_PD_ANA`

```c
#define IMX952_PD_ANA 0
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

模拟电源域（Analog Power Domain）。

<a id="ga39eb7b17cd2d75f9dd5389cfe046ee88"></a>

### `IMX952_PD_AON`

```c
#define IMX952_PD_AON 1
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

常开电源域（Always-on Power Domain）。

<a id="ga2dc16076c0c135b4b9b47775d36d2d59"></a>

### `IMX952_PD_BBSM`

```c
#define IMX952_PD_BBSM 2
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

电池备份安全模块（Battery-Backed Security Module，BBSM）电源域（Power Domain）。

<a id="gabd36ed3b0a37bdbfaffb3297b81a5376"></a>

### `IMX952_PD_CAMERA`

```c
#define IMX952_PD_CAMERA 3
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

摄像头子系统电源域（Camera Subsystem Power Domain）。

<a id="ga786258ae435f51f07024a776f29f8d7b"></a>

### `IMX952_PD_CCMSRCGPC`

```c
#define IMX952_PD_CCMSRCGPC 4
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

CCM/SRC/GPC 电源域（Power Domain）。

<a id="ga7f2f4cdd4c50d5f7a302cc5213917228"></a>

### `IMX952_PD_DDR`

```c
#define IMX952_PD_DDR 10
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

DDR 子系统电源域（Subsystem Power Domain）。

<a id="ga7f834f86e948737624fd92f389bce6af"></a>

### `IMX952_PD_DISPLAY`

```c
#define IMX952_PD_DISPLAY 11
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

显示子系统电源域（Display Subsystem Power Domain）。

<a id="gab6a63f2c0b270591fe47e1ac7fc20dfd"></a>

### `IMX952_PD_GPU`

```c
#define IMX952_PD_GPU 12
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

图形处理器（GPU）电源域（Power Domain）。

<a id="ga7ad60973e1deff63776b4aafe1f41c70"></a>

### `IMX952_PD_HSIO_TOP`

```c
#define IMX952_PD_HSIO_TOP 13
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

HSIO 顶层电源域（Top Power Domain）。

<a id="ga3ca1417fe6cfd397538d99c1c7487bf8"></a>

### `IMX952_PD_HSIO_WAON`

```c
#define IMX952_PD_HSIO_WAON 14
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

HSIO Wakeup-AON 唤醒常开电源域（Power Domain）。

<a id="gab3cd24dd2ee9e8c53484b75723d1708e"></a>

### `IMX952_PD_M7`

```c
#define IMX952_PD_M7 15
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

M7 核心电源域（Core Power Domain）。

<a id="gae952e18ba9705dcf1b6236da8d799944"></a>

### `IMX952_PD_NETC`

```c
#define IMX952_PD_NETC 16
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

网络控制器（Network Controller，NETC）电源域（Power Domain）。

<a id="gaeb8e91004d08f68eacd56c688133a1cf"></a>

### `IMX952_PD_NOC`

```c
#define IMX952_PD_NOC 17
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

片上网络（Network-on-Chip，NOC）电源域（Power Domain）。

<a id="ga15002babf2edb32c6fd9a59fb15cfcb1"></a>

### `IMX952_PD_NPU`

```c
#define IMX952_PD_NPU 18
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

神经网络处理单元（Neural Processing Unit，NPU）电源域（Power Domain）。

<a id="ga1d8d9b7357b28a609c5c398f04ab0d17"></a>

### `IMX952_PD_VPU`

```c
#define IMX952_PD_VPU 19
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

视频处理单元（Video Processing Unit，VPU）电源域（Power Domain）。

<a id="gac4b193eaea6286c428d7f723ab9de916"></a>

### `IMX952_PD_WAKEUP`

```c
#define IMX952_PD_WAKEUP 20
```

```c
#include <zephyr/dt-bindings/power/imx952_power.h>
```

唤醒域电源域（Wakeup Domain Power Domain）。


## 6.4\_原页交叉引用（Cross References）

- [imx952_power.h](https://docs.zephyrproject.org/latest/doxygen/html/imx952__power_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_IIS2DLPC API主题.md) · [返回大纲](大纲.md) · [下一章](P007_INA226 API主题.md)
