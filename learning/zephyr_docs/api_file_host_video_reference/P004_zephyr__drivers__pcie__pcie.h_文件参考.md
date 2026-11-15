---
id: learning.zephyr-docs.api-file-host-video-reference.page-4
title: zephyr__drivers__pcie__pcie.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_drivers\_\_pcie\_\_pcie.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCIe驱动API的头文件。

<a id="details"></a>

```c
#include <stddef.h>
#include <zephyr/devicetree.h>
#include <zephyr/dt-bindings/pcie/pcie.h>
#include <zephyr/types.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

PCIe驱动API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_pcie_5Fdev"></a>

```c
struct pcie_dev
```

相关声明：[pcie_dev](../platform_security_model_reference/P028_pcie_dev_结构体.md)。

<a id="r_pcie_5Fbar"></a>

```c
struct pcie_bar
```

相关声明：[pcie_bar](../platform_security_model_reference/P025_pcie_bar_结构体.md)。

<a id="r_pcie_5Fscan_5Fopt"></a>

```c
struct pcie_scan_opt
```

相关声明：[pcie_scan_opt](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md)。

扫描PCI设备（PCI Devices）的选项。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_gac7d5c41ea3c8999126d89d95961b430b"></a>

```c
#define PCIE_ID_IS_VALID(id)
```

相关声明：[PCIE_ID_IS_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gac7d5c41ea3c8999126d89d95961b430b)。

<a id="r_ga304228150cd8ec56aa24be468e9d79bf"></a>

```c
#define PCIE_DT_ID(node_id)
```

相关声明：[PCIE_DT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga304228150cd8ec56aa24be468e9d79bf)。

获取节点的 PCI Express（PCIe）厂商 ID 和设备 ID（Vendor and Device ID）。

<a id="r_ga3e89194346fa9b945f1873380c527cee"></a>

```c
#define PCIE_DT_INST_ID(inst)
```

相关声明：[PCIE_DT_INST_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga3e89194346fa9b945f1873380c527cee)。

获取节点的 PCI Express（PCIe）厂商 ID 和设备 ID（Vendor and Device ID）。

<a id="r_gad0b870d891458c4ebd7ab2ac1c372eec"></a>

```c
#define DEVICE_PCIE_DECLARE(node_id)
```

相关声明：[DEVICE_PCIE_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gad0b870d891458c4ebd7ab2ac1c372eec)。

为设备树源码（DTS）节点声明 PCIe 上下文变量（Context Variable）。

<a id="r_gade2f1f53701b1d80b5593045e977e4d6"></a>

```c
#define DEVICE_PCIE_INST_DECLARE(inst)
```

相关声明：[DEVICE_PCIE_INST_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gade2f1f53701b1d80b5593045e977e4d6)。

为设备树源码（DTS）节点声明 PCIe 上下文变量（Context Variable）。

<a id="r_gab6c472838e13293980cd53c65aaa3c47"></a>

```c
#define DEVICE_PCIE_INIT(node_id, name)
```

相关声明：[DEVICE_PCIE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gab6c472838e13293980cd53c65aaa3c47)。

初始化具名结构体成员，使其指向 PCIe 上下文（Context）。

<a id="r_gac175df702e85f599b28b7a567c64d146"></a>

```c
#define DEVICE_PCIE_INST_INIT(inst, name)
```

相关声明：[DEVICE_PCIE_INST_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gac175df702e85f599b28b7a567c64d146)。

初始化具名结构体成员，使其指向 PCIe 上下文（Context）。

<a id="r_ga7b500200f090dc95322fe670bf64628d"></a>

```c
#define PCIE_HOST_CONTROLLER(n)
```

相关声明：[PCIE_HOST_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga7b500200f090dc95322fe670bf64628d)。

获取指定 PCI 主机控制器（Host Controller）的总线－设备－功能号（BDF）。

<a id="r_gaad23a180cf411bd8fa10027b9f16eb91"></a>

```c
#define PCIE_CONF_CAPPTR 13U /* capabilities pointer */
```

相关声明：[PCIE_CONF_CAPPTR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaad23a180cf411bd8fa10027b9f16eb91)。

<a id="r_gabe5832ddf2b8399e8f672564ce85ad7e"></a>

```c
#define PCIE_CONF_CAPPTR_FIRST(w)
```

相关声明：[PCIE_CONF_CAPPTR_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gabe5832ddf2b8399e8f672564ce85ad7e)。

<a id="r_gaa888f548db209011f1cf5c87b1f351b8"></a>

```c
#define PCIE_CONF_CAP_ID(w)
```

相关声明：[PCIE_CONF_CAP_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaa888f548db209011f1cf5c87b1f351b8)。

<a id="r_ga98476f56fe7d46b6bee505e0db1c1906"></a>

```c
#define PCIE_CONF_CAP_NEXT(w)
```

相关声明：[PCIE_CONF_CAP_NEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga98476f56fe7d46b6bee505e0db1c1906)。

<a id="r_gabeb1434679b73c98f2ada475c8502e32"></a>

```c
#define PCIE_CONF_EXT_CAPPTR 64U
```

相关声明：[PCIE_CONF_EXT_CAPPTR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gabeb1434679b73c98f2ada475c8502e32)。

<a id="r_ga491d796e2477816c8f8aac4c7b753e3d"></a>

```c
#define PCIE_CONF_EXT_CAP_ID(w)
```

相关声明：[PCIE_CONF_EXT_CAP_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga491d796e2477816c8f8aac4c7b753e3d)。

<a id="r_gaf22a73f116325d3509cde1f83b3d7900"></a>

```c
#define PCIE_CONF_EXT_CAP_VER(w)
```

相关声明：[PCIE_CONF_EXT_CAP_VER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf22a73f116325d3509cde1f83b3d7900)。

<a id="r_gad0fa4f22781b85d06321192338088073"></a>

```c
#define PCIE_CONF_EXT_CAP_NEXT(w)
```

相关声明：[PCIE_CONF_EXT_CAP_NEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gad0fa4f22781b85d06321192338088073)。

<a id="r_ga2b694e339f9be5982605ed53e022ae06"></a>

```c
#define PCIE_CONF_ID 0U
```

相关声明：[PCIE_CONF_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga2b694e339f9be5982605ed53e022ae06)。

<a id="r_ga2fc046f15e216337194e41480518c982"></a>

```c
#define PCIE_CONF_CMDSTAT 1U /* command/status register */
```

相关声明：[PCIE_CONF_CMDSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga2fc046f15e216337194e41480518c982)。

<a id="r_ga6a9008421671f66ea9a6f11f87edd514"></a>

```c
#define PCIE_CONF_CMDSTAT_IO 0x00000001U /* I/O access enable */
```

相关声明：[PCIE_CONF_CMDSTAT_IO](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6a9008421671f66ea9a6f11f87edd514)。

<a id="r_ga24661608e9f66f79bbdcde9304b24820"></a>

```c
#define PCIE_CONF_CMDSTAT_MEM 0x00000002U /* mem access enable */
```

相关声明：[PCIE_CONF_CMDSTAT_MEM](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga24661608e9f66f79bbdcde9304b24820)。

<a id="r_ga8a770450f03bfb020f223e0fea96189d"></a>

```c
#define PCIE_CONF_CMDSTAT_MASTER 0x00000004U /* bus master enable */
```

相关声明：[PCIE_CONF_CMDSTAT_MASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga8a770450f03bfb020f223e0fea96189d)。

<a id="r_gaa7054a8eccbd5338fee3bcb16d2c9218"></a>

```c
#define PCIE_CONF_CMDSTAT_SERR 0x00000100U /* SERR# enable */
```

相关声明：[PCIE_CONF_CMDSTAT_SERR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaa7054a8eccbd5338fee3bcb16d2c9218)。

<a id="r_ga4712b7b75d9bf0098e6c80c69587ef86"></a>

```c
#define PCIE_CONF_CMDSTAT_INTERRUPT 0x00080000U /* interrupt status */
```

相关声明：[PCIE_CONF_CMDSTAT_INTERRUPT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga4712b7b75d9bf0098e6c80c69587ef86)。

<a id="r_ga7127f82d9c9b093b1056125ca1bb9d65"></a>

```c
#define PCIE_CONF_CMDSTAT_CAPS 0x00100000U /* capabilities list */
```

相关声明：[PCIE_CONF_CMDSTAT_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga7127f82d9c9b093b1056125ca1bb9d65)。

<a id="r_ga6946589a87e364c4710fba1dded553dc"></a>

```c
#define PCIE_CONF_CLASSREV 2U /* class/revision register */
```

相关声明：[PCIE_CONF_CLASSREV](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6946589a87e364c4710fba1dded553dc)。

<a id="r_gace40af940c01af2876e6fe8d599677bc"></a>

```c
#define PCIE_CONF_CLASSREV_CLASS(w)
```

相关声明：[PCIE_CONF_CLASSREV_CLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gace40af940c01af2876e6fe8d599677bc)。

<a id="r_ga769e486c00a8ceda4ddb3f3eebc09c59"></a>

```c
#define PCIE_CONF_CLASSREV_SUBCLASS(w)
```

相关声明：[PCIE_CONF_CLASSREV_SUBCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga769e486c00a8ceda4ddb3f3eebc09c59)。

<a id="r_ga36f77d220a11a9a30c4656e7f616ec05"></a>

```c
#define PCIE_CONF_CLASSREV_PROGIF(w)
```

相关声明：[PCIE_CONF_CLASSREV_PROGIF](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga36f77d220a11a9a30c4656e7f616ec05)。

<a id="r_gae102d89e2fb359c3c9dda6b35d9ecd4f"></a>

```c
#define PCIE_CONF_CLASSREV_REV(w)
```

相关声明：[PCIE_CONF_CLASSREV_REV](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gae102d89e2fb359c3c9dda6b35d9ecd4f)。

<a id="r_ga43ad620ae5a3041f0d7553de03c6da84"></a>

```c
#define PCIE_CONF_TYPE 3U
```

相关声明：[PCIE_CONF_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga43ad620ae5a3041f0d7553de03c6da84)。

<a id="r_ga9462e002a9d4b49ef7e7c97942765215"></a>

```c
#define PCIE_CONF_MULTIFUNCTION(w)
```

相关声明：[PCIE_CONF_MULTIFUNCTION](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga9462e002a9d4b49ef7e7c97942765215)。

<a id="r_gab7c494d71f6490e483b642a02ef90930"></a>

```c
#define PCIE_CONF_TYPE_BRIDGE(w)
```

相关声明：[PCIE_CONF_TYPE_BRIDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gab7c494d71f6490e483b642a02ef90930)。

<a id="r_ga0580b798e6498097573c1eb0f2c6d2b1"></a>

```c
#define PCIE_CONF_TYPE_GET(w)
```

相关声明：[PCIE_CONF_TYPE_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga0580b798e6498097573c1eb0f2c6d2b1)。

<a id="r_ga8b76fee3c256914a5044313ff9805969"></a>

```c
#define PCIE_CONF_TYPE_STANDARD 0x0U
```

相关声明：[PCIE_CONF_TYPE_STANDARD](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga8b76fee3c256914a5044313ff9805969)。

<a id="r_ga90e8a996bf491fda870ff29b119a5242"></a>

```c
#define PCIE_CONF_TYPE_PCI_BRIDGE 0x1U
```

相关声明：[PCIE_CONF_TYPE_PCI_BRIDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga90e8a996bf491fda870ff29b119a5242)。

<a id="r_gae9587843cac6247fcfb72f985ff4b030"></a>

```c
#define PCIE_CONF_TYPE_CARDBUS_BRIDGE 0x2U
```

相关声明：[PCIE_CONF_TYPE_CARDBUS_BRIDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gae9587843cac6247fcfb72f985ff4b030)。

<a id="r_gadfd21197ccd78d7bfb549fbb6f7070ff"></a>

```c
#define PCIE_CONF_BAR0 4U
```

相关声明：[PCIE_CONF_BAR0](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gadfd21197ccd78d7bfb549fbb6f7070ff)。

<a id="r_ga77e43c6060febf8a5b8439c7fc940a1f"></a>

```c
#define PCIE_CONF_BAR1 5U
```

相关声明：[PCIE_CONF_BAR1](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga77e43c6060febf8a5b8439c7fc940a1f)。

<a id="r_ga90040a3b78c5f5563f2f123e9fb05dd8"></a>

```c
#define PCIE_CONF_BAR2 6U
```

相关声明：[PCIE_CONF_BAR2](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga90040a3b78c5f5563f2f123e9fb05dd8)。

<a id="r_ga05b9be5537cf1a4f3994c1a2c82282a1"></a>

```c
#define PCIE_CONF_BAR3 7U
```

相关声明：[PCIE_CONF_BAR3](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga05b9be5537cf1a4f3994c1a2c82282a1)。

<a id="r_ga51dbf953128b6a464bf50cfa459626e7"></a>

```c
#define PCIE_CONF_BAR4 8U
```

相关声明：[PCIE_CONF_BAR4](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga51dbf953128b6a464bf50cfa459626e7)。

<a id="r_ga84fb2d49dd14438a9ff12a8eeb5bca60"></a>

```c
#define PCIE_CONF_BAR5 9U
```

相关声明：[PCIE_CONF_BAR5](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga84fb2d49dd14438a9ff12a8eeb5bca60)。

<a id="r_ga2f4020ce7fec0e3b5c9b121951468b70"></a>

```c
#define PCIE_CONF_BAR_IO(w)
```

相关声明：[PCIE_CONF_BAR_IO](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga2f4020ce7fec0e3b5c9b121951468b70)。

<a id="r_ga6018ef2d851fd6a64a1ad4dde956f4c9"></a>

```c
#define PCIE_CONF_BAR_MEM(w)
```

相关声明：[PCIE_CONF_BAR_MEM](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6018ef2d851fd6a64a1ad4dde956f4c9)。

<a id="r_ga6d2644d85b7bfbf9a526e6d54096982d"></a>

```c
#define PCIE_CONF_BAR_64(w)
```

相关声明：[PCIE_CONF_BAR_64](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6d2644d85b7bfbf9a526e6d54096982d)。

<a id="r_gaf163a00f52cc96bc7694e4e7e7a8d1fe"></a>

```c
#define PCIE_CONF_BAR_ADDR(w)
```

相关声明：[PCIE_CONF_BAR_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf163a00f52cc96bc7694e4e7e7a8d1fe)。

<a id="r_gabe49cc62101a531ca9e26b0290218797"></a>

```c
#define PCIE_CONF_BAR_IO_ADDR(w)
```

相关声明：[PCIE_CONF_BAR_IO_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gabe49cc62101a531ca9e26b0290218797)。

<a id="r_ga23c45457ec77c6fd2e1977710f6edf28"></a>

```c
#define PCIE_CONF_BAR_FLAGS(w)
```

相关声明：[PCIE_CONF_BAR_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga23c45457ec77c6fd2e1977710f6edf28)。

<a id="r_ga296141fc89700213899b6463e1166477"></a>

```c
#define PCIE_CONF_BAR_NONE 0U
```

相关声明：[PCIE_CONF_BAR_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga296141fc89700213899b6463e1166477)。

<a id="r_ga65e8ddebc6d25b51940ae647f81deca1"></a>

```c
#define PCIE_CONF_BAR_INVAL 0xFFFFFFF0U
```

相关声明：[PCIE_CONF_BAR_INVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga65e8ddebc6d25b51940ae647f81deca1)。

<a id="r_ga8e1968a28791ed0529d622f32e6fad6c"></a>

```c
#define PCIE_CONF_BAR_INVAL64 0xFFFFFFFFFFFFFFF0UL
```

相关声明：[PCIE_CONF_BAR_INVAL64](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga8e1968a28791ed0529d622f32e6fad6c)。

<a id="r_gafd74fe08ef11c685775433236d0fd734"></a>

```c
#define PCIE_CONF_BAR_INVAL_FLAGS(w)
```

相关声明：[PCIE_CONF_BAR_INVAL_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gafd74fe08ef11c685775433236d0fd734)。

<a id="r_gaac6d5d5eb2ff10b6d85b3bb3efb0ce6e"></a>

```c
#define PCIE_BUS_NUMBER 6U
```

相关声明：[PCIE_BUS_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaac6d5d5eb2ff10b6d85b3bb3efb0ce6e)。

<a id="r_ga4c0dbee39acf51c94b5ececba150f8d0"></a>

```c
#define PCIE_BUS_PRIMARY_NUMBER(w)
```

相关声明：[PCIE_BUS_PRIMARY_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga4c0dbee39acf51c94b5ececba150f8d0)。

<a id="r_ga61cd874c47de3545ca2ffa1eecd7eb42"></a>

```c
#define PCIE_BUS_SECONDARY_NUMBER(w)
```

相关声明：[PCIE_BUS_SECONDARY_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga61cd874c47de3545ca2ffa1eecd7eb42)。

<a id="r_ga0be93727f18869b7a486e42eac47fa2d"></a>

```c
#define PCIE_BUS_SUBORDINATE_NUMBER(w)
```

相关声明：[PCIE_BUS_SUBORDINATE_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga0be93727f18869b7a486e42eac47fa2d)。

<a id="r_gaa05e49d0cafbe51b7742354470d07bd0"></a>

```c
#define PCIE_SECONDARY_LATENCY_TIMER(w)
```

相关声明：[PCIE_SECONDARY_LATENCY_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaa05e49d0cafbe51b7742354470d07bd0)。

<a id="r_ga784bc42d77fec195d794c29067bd988c"></a>

```c
#define PCIE_BUS_NUMBER_VAL(prim, sec, sub, lat)
```

相关声明：[PCIE_BUS_NUMBER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga784bc42d77fec195d794c29067bd988c)。

<a id="r_ga111eab92400e240ec5b7f08caf1b8a87"></a>

```c
#define PCIE_IO_SEC_STATUS 7U
```

相关声明：[PCIE_IO_SEC_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga111eab92400e240ec5b7f08caf1b8a87)。

<a id="r_ga34f56e87ececf58b285e91341cd27d23"></a>

```c
#define PCIE_IO_BASE(w)
```

相关声明：[PCIE_IO_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga34f56e87ececf58b285e91341cd27d23)。

<a id="r_ga4629a222d00917b2e3cad6aadbfd2ec1"></a>

```c
#define PCIE_IO_LIMIT(w)
```

相关声明：[PCIE_IO_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga4629a222d00917b2e3cad6aadbfd2ec1)。

<a id="r_ga804b34fd47ba065287e0257fac84ac35"></a>

```c
#define PCIE_SEC_STATUS(w)
```

相关声明：[PCIE_SEC_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga804b34fd47ba065287e0257fac84ac35)。

<a id="r_ga61f05b2c4cd5c672af43960b320e33bc"></a>

```c
#define PCIE_IO_SEC_STATUS_VAL(iob, iol, sec_status)
```

相关声明：[PCIE_IO_SEC_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga61f05b2c4cd5c672af43960b320e33bc)。

<a id="r_ga6fbcd3f523deb069aa31bcd31973d00b"></a>

```c
#define PCIE_MEM_BASE_LIMIT 8U
```

相关声明：[PCIE_MEM_BASE_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6fbcd3f523deb069aa31bcd31973d00b)。

<a id="r_gacd6be1e38666a6a137b1654007cf293a"></a>

```c
#define PCIE_MEM_BASE(w)
```

相关声明：[PCIE_MEM_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gacd6be1e38666a6a137b1654007cf293a)。

<a id="r_ga9f5d23ad0674aed0bf5c1869621de303"></a>

```c
#define PCIE_MEM_LIMIT(w)
```

相关声明：[PCIE_MEM_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga9f5d23ad0674aed0bf5c1869621de303)。

<a id="r_ga93a6dbe27d3d11be29397ae80c58a589"></a>

```c
#define PCIE_MEM_BASE_LIMIT_VAL(memb, meml)
```

相关声明：[PCIE_MEM_BASE_LIMIT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga93a6dbe27d3d11be29397ae80c58a589)。

<a id="r_ga8dd5906e8d735210d9f8ca25d39684b4"></a>

```c
#define PCIE_PREFETCH_BASE_LIMIT 9U
```

相关声明：[PCIE_PREFETCH_BASE_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga8dd5906e8d735210d9f8ca25d39684b4)。

<a id="r_ga5f7aa0fc063ec072bf7e89fca603c825"></a>

```c
#define PCIE_PREFETCH_BASE(w)
```

相关声明：[PCIE_PREFETCH_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga5f7aa0fc063ec072bf7e89fca603c825)。

<a id="r_gaf0a18504a4eb2061d1afc90fc7b8ee21"></a>

```c
#define PCIE_PREFETCH_LIMIT(w)
```

相关声明：[PCIE_PREFETCH_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf0a18504a4eb2061d1afc90fc7b8ee21)。

<a id="r_ga02b269663488e7c7469415622390ce55"></a>

```c
#define PCIE_PREFETCH_BASE_LIMIT_VAL(pmemb, pmeml)
```

相关声明：[PCIE_PREFETCH_BASE_LIMIT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga02b269663488e7c7469415622390ce55)。

<a id="r_ga6ebdd02e0599f33becb6cf413be0a8cd"></a>

```c
#define PCIE_PREFETCH_BASE_UPPER 10U
```

相关声明：[PCIE_PREFETCH_BASE_UPPER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6ebdd02e0599f33becb6cf413be0a8cd)。

<a id="r_gab0eda55fd8c2c4025dc4350ef946a61b"></a>

```c
#define PCIE_PREFETCH_LIMIT_UPPER 11U
```

相关声明：[PCIE_PREFETCH_LIMIT_UPPER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gab0eda55fd8c2c4025dc4350ef946a61b)。

<a id="r_gafc1acf0ac9b46629497c7a552f5650ce"></a>

```c
#define PCIE_IO_BASE_LIMIT_UPPER 12U
```

相关声明：[PCIE_IO_BASE_LIMIT_UPPER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gafc1acf0ac9b46629497c7a552f5650ce)。

<a id="r_ga8bf9a619d6d83cbb009a7f18b501db92"></a>

```c
#define PCIE_IO_BASE_UPPER(w)
```

相关声明：[PCIE_IO_BASE_UPPER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga8bf9a619d6d83cbb009a7f18b501db92)。

<a id="r_ga76a59c926f2760a04c4d8439cb227fe2"></a>

```c
#define PCIE_IO_LIMIT_UPPER(w)
```

相关声明：[PCIE_IO_LIMIT_UPPER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga76a59c926f2760a04c4d8439cb227fe2)。

<a id="r_ga88669a9ca40294cee41bb163a908737f"></a>

```c
#define PCIE_IO_BASE_LIMIT_UPPER_VAL(iobu, iolu)
```

相关声明：[PCIE_IO_BASE_LIMIT_UPPER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga88669a9ca40294cee41bb163a908737f)。

<a id="r_gaa5a2c8849e4cac05ee584827aedbfb93"></a>

```c
#define PCIE_CONF_INTR 15U
```

相关声明：[PCIE_CONF_INTR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaa5a2c8849e4cac05ee584827aedbfb93)。

<a id="r_ga5c2f2d310dc6a73530b6909ce2c2536e"></a>

```c
#define PCIE_CONF_INTR_IRQ(w)
```

相关声明：[PCIE_CONF_INTR_IRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga5c2f2d310dc6a73530b6909ce2c2536e)。

<a id="r_ga995ca5b5146669c9234d3cdd596b715c"></a>

```c
#define PCIE_CONF_INTR_IRQ_NONE 0xFFU /* no interrupt routed */
```

相关声明：[PCIE_CONF_INTR_IRQ_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga995ca5b5146669c9234d3cdd596b715c)。

<a id="r_ga1ce9e061b5a773f3ee74f78893174f9e"></a>

```c
#define PCIE_MAX_BUS (0xFFFFFFFFU & PCIE_BDF_BUS_MASK)
```

相关声明：[PCIE_MAX_BUS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga1ce9e061b5a773f3ee74f78893174f9e)、[PCIE_BDF_BUS_MASK](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#a193dd359d7a96bdd904662717c7fbf6d)。

<a id="r_ga8809359a58c787a939d01f25e12ac51a"></a>

```c
#define PCIE_MAX_DEV (0xFFFFFFFFU & PCIE_BDF_DEV_MASK)
```

相关声明：[PCIE_MAX_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga8809359a58c787a939d01f25e12ac51a)、[PCIE_BDF_DEV_MASK](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#a85cc69963a93046bda0f1594803af9eb)。

<a id="r_gaee8ddb7b7b1354fd5c835b67321f286b"></a>

```c
#define PCIE_MAX_FUNC (0xFFFFFFFFU & PCIE_BDF_FUNC_MASK)
```

相关声明：[PCIE_MAX_FUNC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaee8ddb7b7b1354fd5c835b67321f286b)、[PCIE_BDF_FUNC_MASK](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#ab481360fa29cf086cc5369e6f1860a5f)。

<a id="r_ga6616499a7be31d40af31bb8134aa4a51"></a>

```c
#define PCIE_IRQ_CONNECT(bdf_p, irq_p, priority_p, isr_p, isr_param_p, flags_p)
```

相关声明：[PCIE_IRQ_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6616499a7be31d40af31bb8134aa4a51)。

为 PCIe 端点中断请求（Endpoint IRQ）初始化中断处理函数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.3\_类型定义（Typedefs）

<a id="r_gaf9748042a4f3c8d912d19df1ccf737fb"></a>

```c
typedef uint32_t pcie_bdf_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

唯一的 PCI(e) 端点（Endpoint），由总线、设备、功能号标识。

<a id="r_ga30840d0e312e35f00790660193fd4c04"></a>

```c
typedef uint32_t pcie_id_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga30840d0e312e35f00790660193fd4c04)。

唯一的 PCI(e) 标识符（Identifier），由厂商 ID 和设备 ID 组成。

<a id="r_ga922580e4fb6200ef75425bb54801ceda"></a>

```c
typedef bool(* pcie_scan_cb_t) (pcie_bdf_t bdf, pcie_id_t id, void *cb_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_scan_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga922580e4fb6200ef75425bb54801ceda)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[pcie_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga30840d0e312e35f00790660193fd4c04)。

扫描 PCI 端点（Endpoints）所用的回调类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.4\_枚举（Enumerations）

<a id="r_gabe00c00fc0af29786c3b42f22f82aecf"></a>

```c
enum { PCIE_SCAN_RECURSIVE = BIT(0) , PCIE_SCAN_CB_ALL = BIT(1) }
```

相关声明：[PCIE_SCAN_RECURSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ggabe00c00fc0af29786c3b42f22f82aecfa228932ef6533931a9ae55e37dc38f3c4)、[PCIE_SCAN_CB_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ggabe00c00fc0af29786c3b42f22f82aecfa3579c18ade658f55affd41bfd38f9072)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.5\_函数（Functions）

<a id="r_ga10ecc667c564548e4ddf3ca4374242b5"></a>

```c
uint32_t pcie_conf_read (pcie_bdf_t bdf, unsigned int reg)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga10ecc667c564548e4ddf3ca4374242b5)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

从端点配置空间（Endpoint Configuration Space）读取 32 位字（Word）。

<a id="r_ga47a2e88935e04330d449db5463d9f21a"></a>

```c
void pcie_conf_write (pcie_bdf_t bdf, unsigned int reg, uint32_t data)
```

相关声明：[pcie_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga47a2e88935e04330d449db5463d9f21a)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向端点配置空间（Endpoint Configuration Space）写入 32 位字（Word）。

<a id="r_ga9a7b3c202f91d37fe8445d5016f4c6ab"></a>

```c
int pcie_scan (const struct pcie_scan_opt *opt)
```

相关声明：[pcie_scan](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga9a7b3c202f91d37fe8445d5016f4c6ab)、[pcie_scan_opt](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md)。

扫描 PCIe 设备（Devices）。

<a id="r_gadeb891fbb5b900eb60de22d40afe355e"></a>

```c
bool pcie_get_mbar (pcie_bdf_t bdf, unsigned int bar_index, struct pcie_bar *mbar)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_get_mbar](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gadeb891fbb5b900eb60de22d40afe355e)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pcie_bar](../platform_security_model_reference/P025_pcie_bar_结构体.md)。

获取指定基址寄存器（BAR）索引处的内存 BAR（MBAR）。

<a id="r_gad8463013e51c4ddcca7b5f805f918685"></a>

```c
bool pcie_probe_mbar (pcie_bdf_t bdf, unsigned int index, struct pcie_bar *mbar)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_probe_mbar](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gad8463013e51c4ddcca7b5f805f918685)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pcie_bar](../platform_security_model_reference/P025_pcie_bar_结构体.md)。

探测分配给端点的第 n 个内存映射输入输出地址（MMIO Address）。

<a id="r_ga3523bbdfd67d4b56cf6cd86c98c830bf"></a>

```c
bool pcie_get_iobar (pcie_bdf_t bdf, unsigned int bar_index, struct pcie_bar *iobar)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_get_iobar](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga3523bbdfd67d4b56cf6cd86c98c830bf)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pcie_bar](../platform_security_model_reference/P025_pcie_bar_结构体.md)。

获取指定 BAR 索引处的输入／输出基址寄存器（I/O BAR）。

<a id="r_gaa81d98a9ee58062c02be576fb0dfefd9"></a>

```c
bool pcie_probe_iobar (pcie_bdf_t bdf, unsigned int index, struct pcie_bar *iobar)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_probe_iobar](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaa81d98a9ee58062c02be576fb0dfefd9)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pcie_bar](../platform_security_model_reference/P025_pcie_bar_结构体.md)。

探测分配给端点的第 n 个 I/O BAR 地址。

<a id="r_ga3516fec89df75eb3d77f54193059fc5c"></a>

```c
void pcie_set_cmd (pcie_bdf_t bdf, uint32_t bits, bool on)
```

相关声明：[pcie_set_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga3516fec89df75eb3d77f54193059fc5c)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置或清除端点命令／状态寄存器（Command/Status Register）中的位。

<a id="r_gad69ae431e5f91992f071dee9d7fa9110"></a>

```c
unsigned int pcie_alloc_irq (pcie_bdf_t bdf)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pcie_alloc_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gad69ae431e5f91992f071dee9d7fa9110)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

为端点（Endpoint）分配中断请求（IRQ）。

<a id="r_gaed7fef462ba02a22b5875b1a2c0d965a"></a>

```c
unsigned int pcie_get_irq (pcie_bdf_t bdf)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pcie_get_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaed7fef462ba02a22b5875b1a2c0d965a)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

返回固件／开发板为端点分配的中断请求（IRQ）。

<a id="r_gafb69216f9224a9040b1f0b58eb286196"></a>

```c
void pcie_irq_enable (pcie_bdf_t bdf, unsigned int irq)
```

相关声明：[pcie_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gafb69216f9224a9040b1f0b58eb286196)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使能 PCI(e) 端点，使其可产生指定中断请求（IRQ）。

<a id="r_ga56e724c9bfd7f44c550ccff1b46978a8"></a>

```c
uint32_t pcie_get_cap (pcie_bdf_t bdf, uint32_t cap_id)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_get_cap](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga56e724c9bfd7f44c550ccff1b46978a8)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在端点配置空间（Configuration Space）中查找 PCI(e) 能力（Capability）。

<a id="r_ga5db0d2a5946d20406070b47a1a7acf21"></a>

```c
uint32_t pcie_get_ext_cap (pcie_bdf_t bdf, uint32_t cap_id)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_get_ext_cap](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga5db0d2a5946d20406070b47a1a7acf21)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在端点配置空间（Configuration Space）中查找 PCI(e) 扩展能力（Extended Capability）。

<a id="r_ga14970194de1024a1a4669b69f932a4f5"></a>

```c
bool pcie_connect_dynamic_irq (pcie_bdf_t bdf, unsigned int irq, unsigned int priority, void(*routine)(const void *parameter), const void *parameter, uint32_t flags)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_connect_dynamic_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga14970194de1024a1a4669b69f932a4f5)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将 PCIe 端点中断请求（IRQ）动态连接到中断服务例程（ISR）处理函数。


## 4.6\_原页交叉引用（Cross References）

- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/dt-bindings/pcie/pcie.h](../api_source_runtime_reference/P016_pcie.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_pcie_hid_reference/P001_pcie.h_源码浏览.md)
- [pcie_dev](../platform_security_model_reference/P028_pcie_dev_结构体.md)
- [pcie_bar](../platform_security_model_reference/P025_pcie_bar_结构体.md)
- [pcie_scan_opt](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md)
- [PCIE_ID_IS_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gac7d5c41ea3c8999126d89d95961b430b)
- [PCIE_DT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga304228150cd8ec56aa24be468e9d79bf)
- [PCIE_DT_INST_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga3e89194346fa9b945f1873380c527cee)
- [DEVICE_PCIE_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gad0b870d891458c4ebd7ab2ac1c372eec)
- [DEVICE_PCIE_INST_DECLARE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gade2f1f53701b1d80b5593045e977e4d6)
- [DEVICE_PCIE_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gab6c472838e13293980cd53c65aaa3c47)
- [DEVICE_PCIE_INST_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gac175df702e85f599b28b7a567c64d146)
- [PCIE_HOST_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga7b500200f090dc95322fe670bf64628d)
- [PCIE_CONF_CAPPTR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaad23a180cf411bd8fa10027b9f16eb91)
- [PCIE_CONF_CAPPTR_FIRST](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gabe5832ddf2b8399e8f672564ce85ad7e)
- [PCIE_CONF_CAP_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaa888f548db209011f1cf5c87b1f351b8)
- [PCIE_CONF_CAP_NEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga98476f56fe7d46b6bee505e0db1c1906)
- [PCIE_CONF_EXT_CAPPTR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gabeb1434679b73c98f2ada475c8502e32)
- [PCIE_CONF_EXT_CAP_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga491d796e2477816c8f8aac4c7b753e3d)
- [PCIE_CONF_EXT_CAP_VER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf22a73f116325d3509cde1f83b3d7900)
- [PCIE_CONF_EXT_CAP_NEXT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gad0fa4f22781b85d06321192338088073)
- [PCIE_CONF_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga2b694e339f9be5982605ed53e022ae06)
- [PCIE_CONF_CMDSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga2fc046f15e216337194e41480518c982)
- [PCIE_CONF_CMDSTAT_IO](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6a9008421671f66ea9a6f11f87edd514)
- [PCIE_CONF_CMDSTAT_MEM](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga24661608e9f66f79bbdcde9304b24820)
- [PCIE_CONF_CMDSTAT_MASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga8a770450f03bfb020f223e0fea96189d)
- [PCIE_CONF_CMDSTAT_SERR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaa7054a8eccbd5338fee3bcb16d2c9218)
- [PCIE_CONF_CMDSTAT_INTERRUPT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga4712b7b75d9bf0098e6c80c69587ef86)
- [PCIE_CONF_CMDSTAT_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga7127f82d9c9b093b1056125ca1bb9d65)
- [PCIE_CONF_CLASSREV](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6946589a87e364c4710fba1dded553dc)
- [PCIE_CONF_CLASSREV_CLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gace40af940c01af2876e6fe8d599677bc)
- [PCIE_CONF_CLASSREV_SUBCLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga769e486c00a8ceda4ddb3f3eebc09c59)
- [PCIE_CONF_CLASSREV_PROGIF](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga36f77d220a11a9a30c4656e7f616ec05)
- [PCIE_CONF_CLASSREV_REV](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gae102d89e2fb359c3c9dda6b35d9ecd4f)
- [PCIE_CONF_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga43ad620ae5a3041f0d7553de03c6da84)
- [PCIE_CONF_MULTIFUNCTION](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga9462e002a9d4b49ef7e7c97942765215)
- [PCIE_CONF_TYPE_BRIDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gab7c494d71f6490e483b642a02ef90930)
- [PCIE_CONF_TYPE_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga0580b798e6498097573c1eb0f2c6d2b1)
- [PCIE_CONF_TYPE_STANDARD](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga8b76fee3c256914a5044313ff9805969)
- [PCIE_CONF_TYPE_PCI_BRIDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga90e8a996bf491fda870ff29b119a5242)
- [PCIE_CONF_TYPE_CARDBUS_BRIDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gae9587843cac6247fcfb72f985ff4b030)
- [PCIE_CONF_BAR0](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gadfd21197ccd78d7bfb549fbb6f7070ff)
- [PCIE_CONF_BAR1](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga77e43c6060febf8a5b8439c7fc940a1f)
- [PCIE_CONF_BAR2](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga90040a3b78c5f5563f2f123e9fb05dd8)
- [PCIE_CONF_BAR3](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga05b9be5537cf1a4f3994c1a2c82282a1)
- [PCIE_CONF_BAR4](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga51dbf953128b6a464bf50cfa459626e7)
- [PCIE_CONF_BAR5](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga84fb2d49dd14438a9ff12a8eeb5bca60)
- [PCIE_CONF_BAR_IO](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga2f4020ce7fec0e3b5c9b121951468b70)
- [PCIE_CONF_BAR_MEM](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6018ef2d851fd6a64a1ad4dde956f4c9)
- [PCIE_CONF_BAR_64](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6d2644d85b7bfbf9a526e6d54096982d)
- [PCIE_CONF_BAR_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf163a00f52cc96bc7694e4e7e7a8d1fe)
- [PCIE_CONF_BAR_IO_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gabe49cc62101a531ca9e26b0290218797)
- [PCIE_CONF_BAR_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga23c45457ec77c6fd2e1977710f6edf28)
- [PCIE_CONF_BAR_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga296141fc89700213899b6463e1166477)
- [PCIE_CONF_BAR_INVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga65e8ddebc6d25b51940ae647f81deca1)
- [PCIE_CONF_BAR_INVAL64](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga8e1968a28791ed0529d622f32e6fad6c)
- [PCIE_CONF_BAR_INVAL_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gafd74fe08ef11c685775433236d0fd734)
- [PCIE_BUS_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaac6d5d5eb2ff10b6d85b3bb3efb0ce6e)
- [PCIE_BUS_PRIMARY_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga4c0dbee39acf51c94b5ececba150f8d0)
- [PCIE_BUS_SECONDARY_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga61cd874c47de3545ca2ffa1eecd7eb42)
- [PCIE_BUS_SUBORDINATE_NUMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga0be93727f18869b7a486e42eac47fa2d)
- [PCIE_SECONDARY_LATENCY_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaa05e49d0cafbe51b7742354470d07bd0)
- [PCIE_BUS_NUMBER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga784bc42d77fec195d794c29067bd988c)
- [PCIE_IO_SEC_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga111eab92400e240ec5b7f08caf1b8a87)
- [PCIE_IO_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga34f56e87ececf58b285e91341cd27d23)
- [PCIE_IO_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga4629a222d00917b2e3cad6aadbfd2ec1)
- [PCIE_SEC_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga804b34fd47ba065287e0257fac84ac35)
- [PCIE_IO_SEC_STATUS_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga61f05b2c4cd5c672af43960b320e33bc)
- [PCIE_MEM_BASE_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6fbcd3f523deb069aa31bcd31973d00b)
- [PCIE_MEM_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gacd6be1e38666a6a137b1654007cf293a)
- [PCIE_MEM_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga9f5d23ad0674aed0bf5c1869621de303)
- [PCIE_MEM_BASE_LIMIT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga93a6dbe27d3d11be29397ae80c58a589)
- [PCIE_PREFETCH_BASE_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga8dd5906e8d735210d9f8ca25d39684b4)
- [PCIE_PREFETCH_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga5f7aa0fc063ec072bf7e89fca603c825)
- [PCIE_PREFETCH_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf0a18504a4eb2061d1afc90fc7b8ee21)
- [PCIE_PREFETCH_BASE_LIMIT_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga02b269663488e7c7469415622390ce55)
- [PCIE_PREFETCH_BASE_UPPER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6ebdd02e0599f33becb6cf413be0a8cd)
- [PCIE_PREFETCH_LIMIT_UPPER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gab0eda55fd8c2c4025dc4350ef946a61b)
- [PCIE_IO_BASE_LIMIT_UPPER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gafc1acf0ac9b46629497c7a552f5650ce)
- [PCIE_IO_BASE_UPPER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga8bf9a619d6d83cbb009a7f18b501db92)
- [PCIE_IO_LIMIT_UPPER](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga76a59c926f2760a04c4d8439cb227fe2)
- [PCIE_IO_BASE_LIMIT_UPPER_VAL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga88669a9ca40294cee41bb163a908737f)
- [PCIE_CONF_INTR](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaa5a2c8849e4cac05ee584827aedbfb93)
- [PCIE_CONF_INTR_IRQ](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga5c2f2d310dc6a73530b6909ce2c2536e)
- [PCIE_CONF_INTR_IRQ_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga995ca5b5146669c9234d3cdd596b715c)
- [PCIE_MAX_BUS](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga1ce9e061b5a773f3ee74f78893174f9e)
- [PCIE_BDF_BUS_MASK](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#a193dd359d7a96bdd904662717c7fbf6d)
- [PCIE_MAX_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga8809359a58c787a939d01f25e12ac51a)
- [PCIE_BDF_DEV_MASK](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#a85cc69963a93046bda0f1594803af9eb)
- [PCIE_MAX_FUNC](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaee8ddb7b7b1354fd5c835b67321f286b)
- [PCIE_BDF_FUNC_MASK](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#ab481360fa29cf086cc5369e6f1860a5f)
- [PCIE_IRQ_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga6616499a7be31d40af31bb8134aa4a51)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)
- [pcie_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga30840d0e312e35f00790660193fd4c04)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [pcie_scan_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga922580e4fb6200ef75425bb54801ceda)
- [PCIE_SCAN_RECURSIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ggabe00c00fc0af29786c3b42f22f82aecfa228932ef6533931a9ae55e37dc38f3c4)
- [PCIE_SCAN_CB_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ggabe00c00fc0af29786c3b42f22f82aecfa3579c18ade658f55affd41bfd38f9072)
- [pcie_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga10ecc667c564548e4ddf3ca4374242b5)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [pcie_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga47a2e88935e04330d449db5463d9f21a)
- [pcie_scan](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga9a7b3c202f91d37fe8445d5016f4c6ab)
- [pcie_get_mbar](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gadeb891fbb5b900eb60de22d40afe355e)
- [pcie_probe_mbar](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gad8463013e51c4ddcca7b5f805f918685)
- [pcie_get_iobar](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga3523bbdfd67d4b56cf6cd86c98c830bf)
- [pcie_probe_iobar](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaa81d98a9ee58062c02be576fb0dfefd9)
- [pcie_set_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga3516fec89df75eb3d77f54193059fc5c)
- [pcie_alloc_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gad69ae431e5f91992f071dee9d7fa9110)
- [pcie_get_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaed7fef462ba02a22b5875b1a2c0d965a)
- [pcie_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gafb69216f9224a9040b1f0b58eb286196)
- [pcie_get_cap](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga56e724c9bfd7f44c550ccff1b46978a8)
- [pcie_get_ext_cap](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga5db0d2a5946d20406070b47a1a7acf21)
- [pcie_connect_dynamic_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#ga14970194de1024a1a4669b69f932a4f5)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="header-details"></a>

---

[上一章](P003_zephyr__drivers__mipi_dbi.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__sensor__it8xxx2_vcmp.h_文件参考.md)
