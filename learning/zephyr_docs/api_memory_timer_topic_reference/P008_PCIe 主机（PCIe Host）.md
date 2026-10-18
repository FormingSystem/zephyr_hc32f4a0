---
id: learning.zephyr-docs.api-memory-timer-topic-reference.page-8
title: PCIe 主机（PCIe Host）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_PCIe 主机（PCIe Host）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCIe 主机接口。

<a id="details"></a>

PCIe 主机接口。

<a id="header-groups"></a>
<a id="groups"></a>

## 8.1\_主题（Topics）

<a id="r_pcie_5Fcapabilities"></a>

相关声明：[PCIe能力（Capabilities）。](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html)。

<a id="r_pcie_5Fhost_5Fmsi_5Finterface"></a>

相关声明：[PCIe 主机消息信号中断（MSI）接口](../api_vector_pipeline_topic_reference/P025_PCIe 主机消息信号中断（MSI）接口.md)。

PCIe 主机消息信号中断（MSI）接口

<a id="r_pcie_5Fhost_5Fptm_5Finterface"></a>

相关声明：[PCIe 主机精确时间测量（PTM）接口](../api_extension_topic_reference/P025_PCIe 主机精确时间测量（PTM）接口.md)。

PCIe 主机精确时间测量（PTM）接口

<a id="r_pcie_5Fvc_5Fhost_5Finterface"></a>

相关声明：[PCIe 虚拟通道（Virtual Channel）主机接口](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md)。

PCIe 虚拟通道（Virtual Channel）主机接口

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.2\_数据结构（Data Structures）

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

## 8.3\_宏定义（Macros）

<a id="r_gac7d5c41ea3c8999126d89d95961b430b"></a>

```c
#define PCIE_ID_IS_VALID(id)
```

相关声明：[PCIE_ID_IS_VALID](#gac7d5c41ea3c8999126d89d95961b430b)。

<a id="r_ga304228150cd8ec56aa24be468e9d79bf"></a>

```c
#define PCIE_DT_ID(node_id)
```

相关声明：[PCIE_DT_ID](#ga304228150cd8ec56aa24be468e9d79bf)。

获取节点的 PCI Express（PCIe）厂商 ID 和设备 ID（Vendor and Device ID）。

<a id="r_ga3e89194346fa9b945f1873380c527cee"></a>

```c
#define PCIE_DT_INST_ID(inst)
```

相关声明：[PCIE_DT_INST_ID](#ga3e89194346fa9b945f1873380c527cee)。

获取节点的 PCI Express（PCIe）厂商 ID 和设备 ID（Vendor and Device ID）。

<a id="r_gad0b870d891458c4ebd7ab2ac1c372eec"></a>

```c
#define DEVICE_PCIE_DECLARE(node_id)
```

相关声明：[DEVICE_PCIE_DECLARE](#gad0b870d891458c4ebd7ab2ac1c372eec)。

为设备树源码（DTS）节点声明 PCIe 上下文变量（Context Variable）。

<a id="r_gade2f1f53701b1d80b5593045e977e4d6"></a>

```c
#define DEVICE_PCIE_INST_DECLARE(inst)
```

相关声明：[DEVICE_PCIE_INST_DECLARE](#gade2f1f53701b1d80b5593045e977e4d6)。

为设备树源码（DTS）节点声明 PCIe 上下文变量（Context Variable）。

<a id="r_gab6c472838e13293980cd53c65aaa3c47"></a>

```c
#define DEVICE_PCIE_INIT(node_id, name)
```

相关声明：[DEVICE_PCIE_INIT](#gab6c472838e13293980cd53c65aaa3c47)。

初始化具名结构体成员，使其指向 PCIe 上下文（Context）。

<a id="r_gac175df702e85f599b28b7a567c64d146"></a>

```c
#define DEVICE_PCIE_INST_INIT(inst, name)
```

相关声明：[DEVICE_PCIE_INST_INIT](#gac175df702e85f599b28b7a567c64d146)。

初始化具名结构体成员，使其指向 PCIe 上下文（Context）。

<a id="r_ga7b500200f090dc95322fe670bf64628d"></a>

```c
#define PCIE_HOST_CONTROLLER(n)
```

相关声明：[PCIE_HOST_CONTROLLER](#ga7b500200f090dc95322fe670bf64628d)。

获取指定 PCI 主机控制器（Host Controller）的总线－设备－功能号（BDF）。

<a id="r_gaad23a180cf411bd8fa10027b9f16eb91"></a>

```c
#define PCIE_CONF_CAPPTR 13U /* capabilities pointer */
```

相关声明：[PCIE_CONF_CAPPTR](#gaad23a180cf411bd8fa10027b9f16eb91)。

<a id="r_gabe5832ddf2b8399e8f672564ce85ad7e"></a>

```c
#define PCIE_CONF_CAPPTR_FIRST(w)
```

相关声明：[PCIE_CONF_CAPPTR_FIRST](#gabe5832ddf2b8399e8f672564ce85ad7e)。

<a id="r_gaa888f548db209011f1cf5c87b1f351b8"></a>

```c
#define PCIE_CONF_CAP_ID(w)
```

相关声明：[PCIE_CONF_CAP_ID](#gaa888f548db209011f1cf5c87b1f351b8)。

<a id="r_ga98476f56fe7d46b6bee505e0db1c1906"></a>

```c
#define PCIE_CONF_CAP_NEXT(w)
```

相关声明：[PCIE_CONF_CAP_NEXT](#ga98476f56fe7d46b6bee505e0db1c1906)。

<a id="r_gabeb1434679b73c98f2ada475c8502e32"></a>

```c
#define PCIE_CONF_EXT_CAPPTR 64U
```

相关声明：[PCIE_CONF_EXT_CAPPTR](#gabeb1434679b73c98f2ada475c8502e32)。

<a id="r_ga491d796e2477816c8f8aac4c7b753e3d"></a>

```c
#define PCIE_CONF_EXT_CAP_ID(w)
```

相关声明：[PCIE_CONF_EXT_CAP_ID](#ga491d796e2477816c8f8aac4c7b753e3d)。

<a id="r_gaf22a73f116325d3509cde1f83b3d7900"></a>

```c
#define PCIE_CONF_EXT_CAP_VER(w)
```

相关声明：[PCIE_CONF_EXT_CAP_VER](#gaf22a73f116325d3509cde1f83b3d7900)。

<a id="r_gad0fa4f22781b85d06321192338088073"></a>

```c
#define PCIE_CONF_EXT_CAP_NEXT(w)
```

相关声明：[PCIE_CONF_EXT_CAP_NEXT](#gad0fa4f22781b85d06321192338088073)。

<a id="r_ga2b694e339f9be5982605ed53e022ae06"></a>

```c
#define PCIE_CONF_ID 0U
```

相关声明：[PCIE_CONF_ID](#ga2b694e339f9be5982605ed53e022ae06)。

<a id="r_ga2fc046f15e216337194e41480518c982"></a>

```c
#define PCIE_CONF_CMDSTAT 1U /* command/status register */
```

相关声明：[PCIE_CONF_CMDSTAT](#ga2fc046f15e216337194e41480518c982)。

<a id="r_ga6a9008421671f66ea9a6f11f87edd514"></a>

```c
#define PCIE_CONF_CMDSTAT_IO 0x00000001U /* I/O access enable */
```

相关声明：[PCIE_CONF_CMDSTAT_IO](#ga6a9008421671f66ea9a6f11f87edd514)。

<a id="r_ga24661608e9f66f79bbdcde9304b24820"></a>

```c
#define PCIE_CONF_CMDSTAT_MEM 0x00000002U /* mem access enable */
```

相关声明：[PCIE_CONF_CMDSTAT_MEM](#ga24661608e9f66f79bbdcde9304b24820)。

<a id="r_ga8a770450f03bfb020f223e0fea96189d"></a>

```c
#define PCIE_CONF_CMDSTAT_MASTER 0x00000004U /* bus master enable */
```

相关声明：[PCIE_CONF_CMDSTAT_MASTER](#ga8a770450f03bfb020f223e0fea96189d)。

<a id="r_gaa7054a8eccbd5338fee3bcb16d2c9218"></a>

```c
#define PCIE_CONF_CMDSTAT_SERR 0x00000100U /* SERR# enable */
```

相关声明：[PCIE_CONF_CMDSTAT_SERR](#gaa7054a8eccbd5338fee3bcb16d2c9218)。

<a id="r_ga4712b7b75d9bf0098e6c80c69587ef86"></a>

```c
#define PCIE_CONF_CMDSTAT_INTERRUPT 0x00080000U /* interrupt status */
```

相关声明：[PCIE_CONF_CMDSTAT_INTERRUPT](#ga4712b7b75d9bf0098e6c80c69587ef86)。

<a id="r_ga7127f82d9c9b093b1056125ca1bb9d65"></a>

```c
#define PCIE_CONF_CMDSTAT_CAPS 0x00100000U /* capabilities list */
```

相关声明：[PCIE_CONF_CMDSTAT_CAPS](#ga7127f82d9c9b093b1056125ca1bb9d65)。

<a id="r_ga6946589a87e364c4710fba1dded553dc"></a>

```c
#define PCIE_CONF_CLASSREV 2U /* class/revision register */
```

相关声明：[PCIE_CONF_CLASSREV](#ga6946589a87e364c4710fba1dded553dc)。

<a id="r_gace40af940c01af2876e6fe8d599677bc"></a>

```c
#define PCIE_CONF_CLASSREV_CLASS(w)
```

相关声明：[PCIE_CONF_CLASSREV_CLASS](#gace40af940c01af2876e6fe8d599677bc)。

<a id="r_ga769e486c00a8ceda4ddb3f3eebc09c59"></a>

```c
#define PCIE_CONF_CLASSREV_SUBCLASS(w)
```

相关声明：[PCIE_CONF_CLASSREV_SUBCLASS](#ga769e486c00a8ceda4ddb3f3eebc09c59)。

<a id="r_ga36f77d220a11a9a30c4656e7f616ec05"></a>

```c
#define PCIE_CONF_CLASSREV_PROGIF(w)
```

相关声明：[PCIE_CONF_CLASSREV_PROGIF](#ga36f77d220a11a9a30c4656e7f616ec05)。

<a id="r_gae102d89e2fb359c3c9dda6b35d9ecd4f"></a>

```c
#define PCIE_CONF_CLASSREV_REV(w)
```

相关声明：[PCIE_CONF_CLASSREV_REV](#gae102d89e2fb359c3c9dda6b35d9ecd4f)。

<a id="r_ga43ad620ae5a3041f0d7553de03c6da84"></a>

```c
#define PCIE_CONF_TYPE 3U
```

相关声明：[PCIE_CONF_TYPE](#ga43ad620ae5a3041f0d7553de03c6da84)。

<a id="r_ga9462e002a9d4b49ef7e7c97942765215"></a>

```c
#define PCIE_CONF_MULTIFUNCTION(w)
```

相关声明：[PCIE_CONF_MULTIFUNCTION](#ga9462e002a9d4b49ef7e7c97942765215)。

<a id="r_gab7c494d71f6490e483b642a02ef90930"></a>

```c
#define PCIE_CONF_TYPE_BRIDGE(w)
```

相关声明：[PCIE_CONF_TYPE_BRIDGE](#gab7c494d71f6490e483b642a02ef90930)。

<a id="r_ga0580b798e6498097573c1eb0f2c6d2b1"></a>

```c
#define PCIE_CONF_TYPE_GET(w)
```

相关声明：[PCIE_CONF_TYPE_GET](#ga0580b798e6498097573c1eb0f2c6d2b1)。

<a id="r_ga8b76fee3c256914a5044313ff9805969"></a>

```c
#define PCIE_CONF_TYPE_STANDARD 0x0U
```

相关声明：[PCIE_CONF_TYPE_STANDARD](#ga8b76fee3c256914a5044313ff9805969)。

<a id="r_ga90e8a996bf491fda870ff29b119a5242"></a>

```c
#define PCIE_CONF_TYPE_PCI_BRIDGE 0x1U
```

相关声明：[PCIE_CONF_TYPE_PCI_BRIDGE](#ga90e8a996bf491fda870ff29b119a5242)。

<a id="r_gae9587843cac6247fcfb72f985ff4b030"></a>

```c
#define PCIE_CONF_TYPE_CARDBUS_BRIDGE 0x2U
```

相关声明：[PCIE_CONF_TYPE_CARDBUS_BRIDGE](#gae9587843cac6247fcfb72f985ff4b030)。

<a id="r_gadfd21197ccd78d7bfb549fbb6f7070ff"></a>

```c
#define PCIE_CONF_BAR0 4U
```

相关声明：[PCIE_CONF_BAR0](#gadfd21197ccd78d7bfb549fbb6f7070ff)。

<a id="r_ga77e43c6060febf8a5b8439c7fc940a1f"></a>

```c
#define PCIE_CONF_BAR1 5U
```

相关声明：[PCIE_CONF_BAR1](#ga77e43c6060febf8a5b8439c7fc940a1f)。

<a id="r_ga90040a3b78c5f5563f2f123e9fb05dd8"></a>

```c
#define PCIE_CONF_BAR2 6U
```

相关声明：[PCIE_CONF_BAR2](#ga90040a3b78c5f5563f2f123e9fb05dd8)。

<a id="r_ga05b9be5537cf1a4f3994c1a2c82282a1"></a>

```c
#define PCIE_CONF_BAR3 7U
```

相关声明：[PCIE_CONF_BAR3](#ga05b9be5537cf1a4f3994c1a2c82282a1)。

<a id="r_ga51dbf953128b6a464bf50cfa459626e7"></a>

```c
#define PCIE_CONF_BAR4 8U
```

相关声明：[PCIE_CONF_BAR4](#ga51dbf953128b6a464bf50cfa459626e7)。

<a id="r_ga84fb2d49dd14438a9ff12a8eeb5bca60"></a>

```c
#define PCIE_CONF_BAR5 9U
```

相关声明：[PCIE_CONF_BAR5](#ga84fb2d49dd14438a9ff12a8eeb5bca60)。

<a id="r_ga2f4020ce7fec0e3b5c9b121951468b70"></a>

```c
#define PCIE_CONF_BAR_IO(w)
```

相关声明：[PCIE_CONF_BAR_IO](#ga2f4020ce7fec0e3b5c9b121951468b70)。

<a id="r_ga6018ef2d851fd6a64a1ad4dde956f4c9"></a>

```c
#define PCIE_CONF_BAR_MEM(w)
```

相关声明：[PCIE_CONF_BAR_MEM](#ga6018ef2d851fd6a64a1ad4dde956f4c9)。

<a id="r_ga6d2644d85b7bfbf9a526e6d54096982d"></a>

```c
#define PCIE_CONF_BAR_64(w)
```

相关声明：[PCIE_CONF_BAR_64](#ga6d2644d85b7bfbf9a526e6d54096982d)。

<a id="r_gaf163a00f52cc96bc7694e4e7e7a8d1fe"></a>

```c
#define PCIE_CONF_BAR_ADDR(w)
```

相关声明：[PCIE_CONF_BAR_ADDR](#gaf163a00f52cc96bc7694e4e7e7a8d1fe)。

<a id="r_gabe49cc62101a531ca9e26b0290218797"></a>

```c
#define PCIE_CONF_BAR_IO_ADDR(w)
```

相关声明：[PCIE_CONF_BAR_IO_ADDR](#gabe49cc62101a531ca9e26b0290218797)。

<a id="r_ga23c45457ec77c6fd2e1977710f6edf28"></a>

```c
#define PCIE_CONF_BAR_FLAGS(w)
```

相关声明：[PCIE_CONF_BAR_FLAGS](#ga23c45457ec77c6fd2e1977710f6edf28)。

<a id="r_ga296141fc89700213899b6463e1166477"></a>

```c
#define PCIE_CONF_BAR_NONE 0U
```

相关声明：[PCIE_CONF_BAR_NONE](#ga296141fc89700213899b6463e1166477)。

<a id="r_ga65e8ddebc6d25b51940ae647f81deca1"></a>

```c
#define PCIE_CONF_BAR_INVAL 0xFFFFFFF0U
```

相关声明：[PCIE_CONF_BAR_INVAL](#ga65e8ddebc6d25b51940ae647f81deca1)。

<a id="r_ga8e1968a28791ed0529d622f32e6fad6c"></a>

```c
#define PCIE_CONF_BAR_INVAL64 0xFFFFFFFFFFFFFFF0UL
```

相关声明：[PCIE_CONF_BAR_INVAL64](#ga8e1968a28791ed0529d622f32e6fad6c)。

<a id="r_gafd74fe08ef11c685775433236d0fd734"></a>

```c
#define PCIE_CONF_BAR_INVAL_FLAGS(w)
```

相关声明：[PCIE_CONF_BAR_INVAL_FLAGS](#gafd74fe08ef11c685775433236d0fd734)。

<a id="r_gaac6d5d5eb2ff10b6d85b3bb3efb0ce6e"></a>

```c
#define PCIE_BUS_NUMBER 6U
```

相关声明：[PCIE_BUS_NUMBER](#gaac6d5d5eb2ff10b6d85b3bb3efb0ce6e)。

<a id="r_ga4c0dbee39acf51c94b5ececba150f8d0"></a>

```c
#define PCIE_BUS_PRIMARY_NUMBER(w)
```

相关声明：[PCIE_BUS_PRIMARY_NUMBER](#ga4c0dbee39acf51c94b5ececba150f8d0)。

<a id="r_ga61cd874c47de3545ca2ffa1eecd7eb42"></a>

```c
#define PCIE_BUS_SECONDARY_NUMBER(w)
```

相关声明：[PCIE_BUS_SECONDARY_NUMBER](#ga61cd874c47de3545ca2ffa1eecd7eb42)。

<a id="r_ga0be93727f18869b7a486e42eac47fa2d"></a>

```c
#define PCIE_BUS_SUBORDINATE_NUMBER(w)
```

相关声明：[PCIE_BUS_SUBORDINATE_NUMBER](#ga0be93727f18869b7a486e42eac47fa2d)。

<a id="r_gaa05e49d0cafbe51b7742354470d07bd0"></a>

```c
#define PCIE_SECONDARY_LATENCY_TIMER(w)
```

相关声明：[PCIE_SECONDARY_LATENCY_TIMER](#gaa05e49d0cafbe51b7742354470d07bd0)。

<a id="r_ga784bc42d77fec195d794c29067bd988c"></a>

```c
#define PCIE_BUS_NUMBER_VAL(prim, sec, sub, lat)
```

相关声明：[PCIE_BUS_NUMBER_VAL](#ga784bc42d77fec195d794c29067bd988c)。

<a id="r_ga111eab92400e240ec5b7f08caf1b8a87"></a>

```c
#define PCIE_IO_SEC_STATUS 7U
```

相关声明：[PCIE_IO_SEC_STATUS](#ga111eab92400e240ec5b7f08caf1b8a87)。

<a id="r_ga34f56e87ececf58b285e91341cd27d23"></a>

```c
#define PCIE_IO_BASE(w)
```

相关声明：[PCIE_IO_BASE](#ga34f56e87ececf58b285e91341cd27d23)。

<a id="r_ga4629a222d00917b2e3cad6aadbfd2ec1"></a>

```c
#define PCIE_IO_LIMIT(w)
```

相关声明：[PCIE_IO_LIMIT](#ga4629a222d00917b2e3cad6aadbfd2ec1)。

<a id="r_ga804b34fd47ba065287e0257fac84ac35"></a>

```c
#define PCIE_SEC_STATUS(w)
```

相关声明：[PCIE_SEC_STATUS](#ga804b34fd47ba065287e0257fac84ac35)。

<a id="r_ga61f05b2c4cd5c672af43960b320e33bc"></a>

```c
#define PCIE_IO_SEC_STATUS_VAL(iob, iol, sec_status)
```

相关声明：[PCIE_IO_SEC_STATUS_VAL](#ga61f05b2c4cd5c672af43960b320e33bc)。

<a id="r_ga6fbcd3f523deb069aa31bcd31973d00b"></a>

```c
#define PCIE_MEM_BASE_LIMIT 8U
```

相关声明：[PCIE_MEM_BASE_LIMIT](#ga6fbcd3f523deb069aa31bcd31973d00b)。

<a id="r_gacd6be1e38666a6a137b1654007cf293a"></a>

```c
#define PCIE_MEM_BASE(w)
```

相关声明：[PCIE_MEM_BASE](#gacd6be1e38666a6a137b1654007cf293a)。

<a id="r_ga9f5d23ad0674aed0bf5c1869621de303"></a>

```c
#define PCIE_MEM_LIMIT(w)
```

相关声明：[PCIE_MEM_LIMIT](#ga9f5d23ad0674aed0bf5c1869621de303)。

<a id="r_ga93a6dbe27d3d11be29397ae80c58a589"></a>

```c
#define PCIE_MEM_BASE_LIMIT_VAL(memb, meml)
```

相关声明：[PCIE_MEM_BASE_LIMIT_VAL](#ga93a6dbe27d3d11be29397ae80c58a589)。

<a id="r_ga8dd5906e8d735210d9f8ca25d39684b4"></a>

```c
#define PCIE_PREFETCH_BASE_LIMIT 9U
```

相关声明：[PCIE_PREFETCH_BASE_LIMIT](#ga8dd5906e8d735210d9f8ca25d39684b4)。

<a id="r_ga5f7aa0fc063ec072bf7e89fca603c825"></a>

```c
#define PCIE_PREFETCH_BASE(w)
```

相关声明：[PCIE_PREFETCH_BASE](#ga5f7aa0fc063ec072bf7e89fca603c825)。

<a id="r_gaf0a18504a4eb2061d1afc90fc7b8ee21"></a>

```c
#define PCIE_PREFETCH_LIMIT(w)
```

相关声明：[PCIE_PREFETCH_LIMIT](#gaf0a18504a4eb2061d1afc90fc7b8ee21)。

<a id="r_ga02b269663488e7c7469415622390ce55"></a>

```c
#define PCIE_PREFETCH_BASE_LIMIT_VAL(pmemb, pmeml)
```

相关声明：[PCIE_PREFETCH_BASE_LIMIT_VAL](#ga02b269663488e7c7469415622390ce55)。

<a id="r_ga6ebdd02e0599f33becb6cf413be0a8cd"></a>

```c
#define PCIE_PREFETCH_BASE_UPPER 10U
```

相关声明：[PCIE_PREFETCH_BASE_UPPER](#ga6ebdd02e0599f33becb6cf413be0a8cd)。

<a id="r_gab0eda55fd8c2c4025dc4350ef946a61b"></a>

```c
#define PCIE_PREFETCH_LIMIT_UPPER 11U
```

相关声明：[PCIE_PREFETCH_LIMIT_UPPER](#gab0eda55fd8c2c4025dc4350ef946a61b)。

<a id="r_gafc1acf0ac9b46629497c7a552f5650ce"></a>

```c
#define PCIE_IO_BASE_LIMIT_UPPER 12U
```

相关声明：[PCIE_IO_BASE_LIMIT_UPPER](#gafc1acf0ac9b46629497c7a552f5650ce)。

<a id="r_ga8bf9a619d6d83cbb009a7f18b501db92"></a>

```c
#define PCIE_IO_BASE_UPPER(w)
```

相关声明：[PCIE_IO_BASE_UPPER](#ga8bf9a619d6d83cbb009a7f18b501db92)。

<a id="r_ga76a59c926f2760a04c4d8439cb227fe2"></a>

```c
#define PCIE_IO_LIMIT_UPPER(w)
```

相关声明：[PCIE_IO_LIMIT_UPPER](#ga76a59c926f2760a04c4d8439cb227fe2)。

<a id="r_ga88669a9ca40294cee41bb163a908737f"></a>

```c
#define PCIE_IO_BASE_LIMIT_UPPER_VAL(iobu, iolu)
```

相关声明：[PCIE_IO_BASE_LIMIT_UPPER_VAL](#ga88669a9ca40294cee41bb163a908737f)。

<a id="r_gaa5a2c8849e4cac05ee584827aedbfb93"></a>

```c
#define PCIE_CONF_INTR 15U
```

相关声明：[PCIE_CONF_INTR](#gaa5a2c8849e4cac05ee584827aedbfb93)。

<a id="r_ga5c2f2d310dc6a73530b6909ce2c2536e"></a>

```c
#define PCIE_CONF_INTR_IRQ(w)
```

相关声明：[PCIE_CONF_INTR_IRQ](#ga5c2f2d310dc6a73530b6909ce2c2536e)。

<a id="r_ga995ca5b5146669c9234d3cdd596b715c"></a>

```c
#define PCIE_CONF_INTR_IRQ_NONE 0xFFU /* no interrupt routed */
```

相关声明：[PCIE_CONF_INTR_IRQ_NONE](#ga995ca5b5146669c9234d3cdd596b715c)。

<a id="r_ga1ce9e061b5a773f3ee74f78893174f9e"></a>

```c
#define PCIE_MAX_BUS (0xFFFFFFFFU & PCIE_BDF_BUS_MASK)
```

相关声明：[PCIE_MAX_BUS](#ga1ce9e061b5a773f3ee74f78893174f9e)、[PCIE_BDF_BUS_MASK](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#a193dd359d7a96bdd904662717c7fbf6d)。

<a id="r_ga8809359a58c787a939d01f25e12ac51a"></a>

```c
#define PCIE_MAX_DEV (0xFFFFFFFFU & PCIE_BDF_DEV_MASK)
```

相关声明：[PCIE_MAX_DEV](#ga8809359a58c787a939d01f25e12ac51a)、[PCIE_BDF_DEV_MASK](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#a85cc69963a93046bda0f1594803af9eb)。

<a id="r_gaee8ddb7b7b1354fd5c835b67321f286b"></a>

```c
#define PCIE_MAX_FUNC (0xFFFFFFFFU & PCIE_BDF_FUNC_MASK)
```

相关声明：[PCIE_MAX_FUNC](#gaee8ddb7b7b1354fd5c835b67321f286b)、[PCIE_BDF_FUNC_MASK](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#ab481360fa29cf086cc5369e6f1860a5f)。

<a id="r_ga6616499a7be31d40af31bb8134aa4a51"></a>

```c
#define PCIE_IRQ_CONNECT(bdf_p, irq_p, priority_p, isr_p, isr_param_p, flags_p)
```

相关声明：[PCIE_IRQ_CONNECT](#ga6616499a7be31d40af31bb8134aa4a51)。

为 PCIe 端点中断请求（Endpoint IRQ）初始化中断处理函数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.4\_类型定义（Typedefs）

<a id="r_gaf9748042a4f3c8d912d19df1ccf737fb"></a>

```c
typedef uint32_t pcie_bdf_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)。

唯一的 PCI(e) 端点（Endpoint），由总线、设备、功能号标识。

<a id="r_ga30840d0e312e35f00790660193fd4c04"></a>

```c
typedef uint32_t pcie_id_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_id_t](#ga30840d0e312e35f00790660193fd4c04)。

唯一的 PCI(e) 标识符（Identifier），由厂商 ID 和设备 ID 组成。

<a id="r_ga922580e4fb6200ef75425bb54801ceda"></a>

```c
typedef bool(* pcie_scan_cb_t) (pcie_bdf_t bdf, pcie_id_t id, void *cb_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_scan_cb_t](#ga922580e4fb6200ef75425bb54801ceda)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)、[pcie_id_t](#ga30840d0e312e35f00790660193fd4c04)。

扫描 PCI 端点（Endpoints）所用的回调类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.5\_枚举（Enumerations）

<a id="r_gabe00c00fc0af29786c3b42f22f82aecf"></a>

```c
enum { PCIE_SCAN_RECURSIVE = BIT(0) , PCIE_SCAN_CB_ALL = BIT(1) }
```

相关声明：[PCIE_SCAN_RECURSIVE](#ggabe00c00fc0af29786c3b42f22f82aecfa228932ef6533931a9ae55e37dc38f3c4)、[PCIE_SCAN_CB_ALL](#ggabe00c00fc0af29786c3b42f22f82aecfa3579c18ade658f55affd41bfd38f9072)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.6\_函数（Functions）

<a id="r_ga10ecc667c564548e4ddf3ca4374242b5"></a>

```c
uint32_t pcie_conf_read (pcie_bdf_t bdf, unsigned int reg)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_conf_read](#ga10ecc667c564548e4ddf3ca4374242b5)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

从端点配置空间（Endpoint Configuration Space）读取 32 位字（Word）。

<a id="r_ga47a2e88935e04330d449db5463d9f21a"></a>

```c
void pcie_conf_write (pcie_bdf_t bdf, unsigned int reg, uint32_t data)
```

相关声明：[pcie_conf_write](#ga47a2e88935e04330d449db5463d9f21a)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向端点配置空间（Endpoint Configuration Space）写入 32 位字（Word）。

<a id="r_ga9a7b3c202f91d37fe8445d5016f4c6ab"></a>

```c
int pcie_scan (const struct pcie_scan_opt *opt)
```

相关声明：[pcie_scan](#ga9a7b3c202f91d37fe8445d5016f4c6ab)、[pcie_scan_opt](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md)。

扫描 PCIe 设备（Devices）。

<a id="r_gadeb891fbb5b900eb60de22d40afe355e"></a>

```c
bool pcie_get_mbar (pcie_bdf_t bdf, unsigned int bar_index, struct pcie_bar *mbar)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_get_mbar](#gadeb891fbb5b900eb60de22d40afe355e)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pcie_bar](../platform_security_model_reference/P025_pcie_bar_结构体.md)。

获取指定基址寄存器（BAR）索引处的内存 BAR（MBAR）。

<a id="r_gad8463013e51c4ddcca7b5f805f918685"></a>

```c
bool pcie_probe_mbar (pcie_bdf_t bdf, unsigned int index, struct pcie_bar *mbar)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_probe_mbar](#gad8463013e51c4ddcca7b5f805f918685)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pcie_bar](../platform_security_model_reference/P025_pcie_bar_结构体.md)。

探测分配给端点的第 n 个内存映射输入输出地址（MMIO Address）。

<a id="r_ga3523bbdfd67d4b56cf6cd86c98c830bf"></a>

```c
bool pcie_get_iobar (pcie_bdf_t bdf, unsigned int bar_index, struct pcie_bar *iobar)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_get_iobar](#ga3523bbdfd67d4b56cf6cd86c98c830bf)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pcie_bar](../platform_security_model_reference/P025_pcie_bar_结构体.md)。

获取指定 BAR 索引处的输入／输出基址寄存器（I/O BAR）。

<a id="r_gaa81d98a9ee58062c02be576fb0dfefd9"></a>

```c
bool pcie_probe_iobar (pcie_bdf_t bdf, unsigned int index, struct pcie_bar *iobar)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_probe_iobar](#gaa81d98a9ee58062c02be576fb0dfefd9)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pcie_bar](../platform_security_model_reference/P025_pcie_bar_结构体.md)。

探测分配给端点的第 n 个 I/O BAR 地址。

<a id="r_ga3516fec89df75eb3d77f54193059fc5c"></a>

```c
void pcie_set_cmd (pcie_bdf_t bdf, uint32_t bits, bool on)
```

相关声明：[pcie_set_cmd](#ga3516fec89df75eb3d77f54193059fc5c)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置或清除端点命令／状态寄存器（Command/Status Register）中的位。

<a id="r_gad69ae431e5f91992f071dee9d7fa9110"></a>

```c
unsigned int pcie_alloc_irq (pcie_bdf_t bdf)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pcie_alloc_irq](#gad69ae431e5f91992f071dee9d7fa9110)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)。

为端点（Endpoint）分配中断请求（IRQ）。

<a id="r_gaed7fef462ba02a22b5875b1a2c0d965a"></a>

```c
unsigned int pcie_get_irq (pcie_bdf_t bdf)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pcie_get_irq](#gaed7fef462ba02a22b5875b1a2c0d965a)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)。

返回固件／开发板为端点分配的中断请求（IRQ）。

<a id="r_gafb69216f9224a9040b1f0b58eb286196"></a>

```c
void pcie_irq_enable (pcie_bdf_t bdf, unsigned int irq)
```

相关声明：[pcie_irq_enable](#gafb69216f9224a9040b1f0b58eb286196)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使能 PCI(e) 端点，使其可产生指定中断请求（IRQ）。

<a id="r_ga56e724c9bfd7f44c550ccff1b46978a8"></a>

```c
uint32_t pcie_get_cap (pcie_bdf_t bdf, uint32_t cap_id)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_get_cap](#ga56e724c9bfd7f44c550ccff1b46978a8)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在端点配置空间（Configuration Space）中查找 PCI(e) 能力（Capability）。

<a id="r_ga5db0d2a5946d20406070b47a1a7acf21"></a>

```c
uint32_t pcie_get_ext_cap (pcie_bdf_t bdf, uint32_t cap_id)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_get_ext_cap](#ga5db0d2a5946d20406070b47a1a7acf21)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在端点配置空间（Configuration Space）中查找 PCI(e) 扩展能力（Extended Capability）。

<a id="r_ga14970194de1024a1a4669b69f932a4f5"></a>

```c
bool pcie_connect_dynamic_irq (pcie_bdf_t bdf, unsigned int irq, unsigned int priority, void(*routine)(const void *parameter), const void *parameter, uint32_t flags)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_connect_dynamic_irq](#ga14970194de1024a1a4669b69f932a4f5)、[pcie_bdf_t](#gaf9748042a4f3c8d912d19df1ccf737fb)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

将 PCIe 端点中断请求（IRQ）动态连接到中断服务例程（ISR）处理函数。

## 8.7\_详细说明（Detailed Documentation）

<a id="gad0b870d891458c4ebd7ab2ac1c372eec"></a>

### `DEVICE_PCIE_DECLARE`

```c
#define DEVICE_PCIE_DECLARE ( node_id)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
STRUCT_SECTION_ITERABLE(pcie_dev, Z_DEVICE_PCIE_NAME(node_id)) = {  \
        .bdf = PCIE_BDF_NONE,                                       \
        .id = PCIE_DT_ID(node_id),                                  \
        .class_rev = DT_PROP_OR(node_id, class_rev, 0),             \
        .class_rev_mask = DT_PROP_OR(node_id, class_rev_mask, 0),   \
}
```

为设备树源码（DTS）节点声明 PCIe 上下文变量（Context Variable）。

为 DTS 节点声明 PCIe 上下文（PCIe Context）。对同一节点使用 DEVICE_PCIE_INIT() 宏之前，必须先完成此声明。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | DTS节点标识符。 |

<a id="gab6c472838e13293980cd53c65aaa3c47"></a>

### `DEVICE_PCIE_INIT`

```c
#define DEVICE_PCIE_INIT ( node_id, name )
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
.name = &Z_DEVICE_PCIE_NAME(node_id)
```

初始化具名结构体成员，使其指向 PCIe 上下文（Context）。

使用 DTS 信息，初始化设备配置结构体某个实例中的 PCIe 相关信息。使用此宏前，必须已通过 DEVICE_PCIE_DECLARE() 宏创建 PCIe 上下文结构体（PCIe Context Struct）。

属于 foo 子系统（Subsystem）的驱动实例示例：

配置结构体示例（Config Structure）：`struct foo_config { struct pcie_dev *pcie; ... };`

声明与初始化示例（Declaration and Initialization）：`DEVICE_PCIE_ID_DECLARE(DT_DRV_INST(...)); struct foo_config my_config = { DEVICE_PCIE_INIT(pcie, DT_DRV_INST(...)), ... };`

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | DTS节点标识符。 |
| `name` | config中该MMIO区域的成员名称。 |

<a id="gade2f1f53701b1d80b5593045e977e4d6"></a>

### `DEVICE_PCIE_INST_DECLARE`

```c
#define DEVICE_PCIE_INST_DECLARE ( inst)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
DEVICE_PCIE_DECLARE(DT_DRV_INST(inst))
```

为设备树源码（DTS）节点声明 PCIe 上下文变量（Context Variable）。

等价于 DEVICE_PCIE_DECLARE(DT_DRV_INST(inst))。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号。 |

<a id="gac175df702e85f599b28b7a567c64d146"></a>

### `DEVICE_PCIE_INST_INIT`

```c
#define DEVICE_PCIE_INST_INIT ( inst, name )
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
DEVICE_PCIE_INIT(DT_DRV_INST(inst), name)
```

初始化具名结构体成员，使其指向 PCIe 上下文（Context）。

等价于 DEVICE_PCIE_INIT(DT_DRV_INST(inst), name)。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号。 |
| `name` | 结构体成员名称（Struct Member Name），类型为 struct pcie_dev *。 |

<a id="gaac6d5d5eb2ff10b6d85b3bb3efb0ce6e"></a>

### `PCIE_BUS_NUMBER`

```c
#define PCIE_BUS_NUMBER 6U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga784bc42d77fec195d794c29067bd988c"></a>

### `PCIE_BUS_NUMBER_VAL`

```c
#define PCIE_BUS_NUMBER_VAL ( prim, sec, sub, lat )
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((prim) & 0xffUL) |                     \
 (((sec) & 0xffUL) << 8) |               \
 (((sub) & 0xffUL) << 16) |              \
 (((lat) & 0xffUL) << 24))
```

<a id="ga4c0dbee39acf51c94b5ececba150f8d0"></a>

### `PCIE_BUS_PRIMARY_NUMBER`

```c
#define PCIE_BUS_PRIMARY_NUMBER ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((w) & 0xffUL)
```

<a id="ga61cd874c47de3545ca2ffa1eecd7eb42"></a>

### `PCIE_BUS_SECONDARY_NUMBER`

```c
#define PCIE_BUS_SECONDARY_NUMBER ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 8) & 0xffUL)
```

<a id="ga0be93727f18869b7a486e42eac47fa2d"></a>

### `PCIE_BUS_SUBORDINATE_NUMBER`

```c
#define PCIE_BUS_SUBORDINATE_NUMBER ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 16) & 0xffUL)
```

<a id="gadfd21197ccd78d7bfb549fbb6f7070ff"></a>

### `PCIE_CONF_BAR0`

```c
#define PCIE_CONF_BAR0 4U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga77e43c6060febf8a5b8439c7fc940a1f"></a>

### `PCIE_CONF_BAR1`

```c
#define PCIE_CONF_BAR1 5U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga90040a3b78c5f5563f2f123e9fb05dd8"></a>

### `PCIE_CONF_BAR2`

```c
#define PCIE_CONF_BAR2 6U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga05b9be5537cf1a4f3994c1a2c82282a1"></a>

### `PCIE_CONF_BAR3`

```c
#define PCIE_CONF_BAR3 7U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga51dbf953128b6a464bf50cfa459626e7"></a>

### `PCIE_CONF_BAR4`

```c
#define PCIE_CONF_BAR4 8U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga84fb2d49dd14438a9ff12a8eeb5bca60"></a>

### `PCIE_CONF_BAR5`

```c
#define PCIE_CONF_BAR5 9U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga6d2644d85b7bfbf9a526e6d54096982d"></a>

### `PCIE_CONF_BAR_64`

```c
#define PCIE_CONF_BAR_64 ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) & 0x00000006U) == 0x00000004U)
```

<a id="gaf163a00f52cc96bc7694e4e7e7a8d1fe"></a>

### `PCIE_CONF_BAR_ADDR`

```c
#define PCIE_CONF_BAR_ADDR ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((w) & ~0xfUL)
```

<a id="ga23c45457ec77c6fd2e1977710f6edf28"></a>

### `PCIE_CONF_BAR_FLAGS`

```c
#define PCIE_CONF_BAR_FLAGS ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((w) & 0xfUL)
```

<a id="ga65e8ddebc6d25b51940ae647f81deca1"></a>

### `PCIE_CONF_BAR_INVAL`

```c
#define PCIE_CONF_BAR_INVAL 0xFFFFFFF0U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga8e1968a28791ed0529d622f32e6fad6c"></a>

### `PCIE_CONF_BAR_INVAL64`

```c
#define PCIE_CONF_BAR_INVAL64 0xFFFFFFFFFFFFFFF0UL
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="gafd74fe08ef11c685775433236d0fd734"></a>

### `PCIE_CONF_BAR_INVAL_FLAGS`

```c
#define PCIE_CONF_BAR_INVAL_FLAGS ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((((w) & 0x00000006U) == 0x00000006U) ||        \
 (((w) & 0x00000006U) == 0x00000002U))
```

<a id="ga2f4020ce7fec0e3b5c9b121951468b70"></a>

### `PCIE_CONF_BAR_IO`

```c
#define PCIE_CONF_BAR_IO ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) & 0x00000001U) == 0x00000001U)
```

<a id="gabe49cc62101a531ca9e26b0290218797"></a>

### `PCIE_CONF_BAR_IO_ADDR`

```c
#define PCIE_CONF_BAR_IO_ADDR ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((w) & ~0x3UL)
```

<a id="ga6018ef2d851fd6a64a1ad4dde956f4c9"></a>

### `PCIE_CONF_BAR_MEM`

```c
#define PCIE_CONF_BAR_MEM ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) & 0x00000001U) != 0x00000001U)
```

<a id="ga296141fc89700213899b6463e1166477"></a>

### `PCIE_CONF_BAR_NONE`

```c
#define PCIE_CONF_BAR_NONE 0U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="gaa888f548db209011f1cf5c87b1f351b8"></a>

### `PCIE_CONF_CAP_ID`

```c
#define PCIE_CONF_CAP_ID ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((w) & 0xFFU)
```

<a id="ga98476f56fe7d46b6bee505e0db1c1906"></a>

### `PCIE_CONF_CAP_NEXT`

```c
#define PCIE_CONF_CAP_NEXT ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 10) & 0x3FU)
```

<a id="gaad23a180cf411bd8fa10027b9f16eb91"></a>

### `PCIE_CONF_CAPPTR`

```c
#define PCIE_CONF_CAPPTR 13U /* capabilities pointer */
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="gabe5832ddf2b8399e8f672564ce85ad7e"></a>

### `PCIE_CONF_CAPPTR_FIRST`

```c
#define PCIE_CONF_CAPPTR_FIRST ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 2) & 0x3FU)
```

<a id="ga6946589a87e364c4710fba1dded553dc"></a>

### `PCIE_CONF_CLASSREV`

```c
#define PCIE_CONF_CLASSREV 2U /* class/revision register */
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="gace40af940c01af2876e6fe8d599677bc"></a>

### `PCIE_CONF_CLASSREV_CLASS`

```c
#define PCIE_CONF_CLASSREV_CLASS ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 24) & 0xFFU)
```

<a id="ga36f77d220a11a9a30c4656e7f616ec05"></a>

### `PCIE_CONF_CLASSREV_PROGIF`

```c
#define PCIE_CONF_CLASSREV_PROGIF ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 8) & 0xFFU)
```

<a id="gae102d89e2fb359c3c9dda6b35d9ecd4f"></a>

### `PCIE_CONF_CLASSREV_REV`

```c
#define PCIE_CONF_CLASSREV_REV ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((w) & 0xFFU)
```

<a id="ga769e486c00a8ceda4ddb3f3eebc09c59"></a>

### `PCIE_CONF_CLASSREV_SUBCLASS`

```c
#define PCIE_CONF_CLASSREV_SUBCLASS ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 16) & 0xFFU)
```

<a id="ga2fc046f15e216337194e41480518c982"></a>

### `PCIE_CONF_CMDSTAT`

```c
#define PCIE_CONF_CMDSTAT 1U /* command/status register */
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga7127f82d9c9b093b1056125ca1bb9d65"></a>

### `PCIE_CONF_CMDSTAT_CAPS`

```c
#define PCIE_CONF_CMDSTAT_CAPS 0x00100000U /* capabilities list */
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga4712b7b75d9bf0098e6c80c69587ef86"></a>

### `PCIE_CONF_CMDSTAT_INTERRUPT`

```c
#define PCIE_CONF_CMDSTAT_INTERRUPT 0x00080000U /* interrupt status */
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga6a9008421671f66ea9a6f11f87edd514"></a>

### `PCIE_CONF_CMDSTAT_IO`

```c
#define PCIE_CONF_CMDSTAT_IO 0x00000001U /* I/O access enable */
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga8a770450f03bfb020f223e0fea96189d"></a>

### `PCIE_CONF_CMDSTAT_MASTER`

```c
#define PCIE_CONF_CMDSTAT_MASTER 0x00000004U /* bus master enable */
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga24661608e9f66f79bbdcde9304b24820"></a>

### `PCIE_CONF_CMDSTAT_MEM`

```c
#define PCIE_CONF_CMDSTAT_MEM 0x00000002U /* mem access enable */
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="gaa7054a8eccbd5338fee3bcb16d2c9218"></a>

### `PCIE_CONF_CMDSTAT_SERR`

```c
#define PCIE_CONF_CMDSTAT_SERR 0x00000100U /* SERR# enable */
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga491d796e2477816c8f8aac4c7b753e3d"></a>

### `PCIE_CONF_EXT_CAP_ID`

```c
#define PCIE_CONF_EXT_CAP_ID ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((w) & 0xFFFFU)
```

<a id="gad0fa4f22781b85d06321192338088073"></a>

### `PCIE_CONF_EXT_CAP_NEXT`

```c
#define PCIE_CONF_EXT_CAP_NEXT ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 20) & 0xFFFU)
```

<a id="gaf22a73f116325d3509cde1f83b3d7900"></a>

### `PCIE_CONF_EXT_CAP_VER`

```c
#define PCIE_CONF_EXT_CAP_VER ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 16) & 0xFU)
```

<a id="gabeb1434679b73c98f2ada475c8502e32"></a>

### `PCIE_CONF_EXT_CAPPTR`

```c
#define PCIE_CONF_EXT_CAPPTR 64U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga2b694e339f9be5982605ed53e022ae06"></a>

### `PCIE_CONF_ID`

```c
#define PCIE_CONF_ID 0U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="gaa5a2c8849e4cac05ee584827aedbfb93"></a>

### `PCIE_CONF_INTR`

```c
#define PCIE_CONF_INTR 15U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga5c2f2d310dc6a73530b6909ce2c2536e"></a>

### `PCIE_CONF_INTR_IRQ`

```c
#define PCIE_CONF_INTR_IRQ ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((w) & 0xFFU)
```

<a id="ga995ca5b5146669c9234d3cdd596b715c"></a>

### `PCIE_CONF_INTR_IRQ_NONE`

```c
#define PCIE_CONF_INTR_IRQ_NONE 0xFFU /* no interrupt routed */
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga9462e002a9d4b49ef7e7c97942765215"></a>

### `PCIE_CONF_MULTIFUNCTION`

```c
#define PCIE_CONF_MULTIFUNCTION ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) & 0x00800000U) != 0U)
```

<a id="ga43ad620ae5a3041f0d7553de03c6da84"></a>

### `PCIE_CONF_TYPE`

```c
#define PCIE_CONF_TYPE 3U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="gab7c494d71f6490e483b642a02ef90930"></a>

### `PCIE_CONF_TYPE_BRIDGE`

```c
#define PCIE_CONF_TYPE_BRIDGE ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) & 0x007F0000U) != 0U)
```

<a id="gae9587843cac6247fcfb72f985ff4b030"></a>

### `PCIE_CONF_TYPE_CARDBUS_BRIDGE`

```c
#define PCIE_CONF_TYPE_CARDBUS_BRIDGE 0x2U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga0580b798e6498097573c1eb0f2c6d2b1"></a>

### `PCIE_CONF_TYPE_GET`

```c
#define PCIE_CONF_TYPE_GET ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 16) & 0x7F)
```

<a id="ga90e8a996bf491fda870ff29b119a5242"></a>

### `PCIE_CONF_TYPE_PCI_BRIDGE`

```c
#define PCIE_CONF_TYPE_PCI_BRIDGE 0x1U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga8b76fee3c256914a5044313ff9805969"></a>

### `PCIE_CONF_TYPE_STANDARD`

```c
#define PCIE_CONF_TYPE_STANDARD 0x0U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga304228150cd8ec56aa24be468e9d79bf"></a>

### `PCIE_DT_ID`

```c
#define PCIE_DT_ID ( node_id)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
PCIE_ID(DT_PROP_OR(node_id, vendor_id, 0xffff), \
DT_PROP_OR(node_id, device_id, 0xffff))
```

获取节点的 PCI Express（PCIe）厂商 ID 和设备 ID（Vendor and Device ID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | DTS节点标识符。 |

返回（Returns）：以 pcie_id_t 表示的厂商标识符／设备标识符组合（VID/DID）。

<a id="ga3e89194346fa9b945f1873380c527cee"></a>

### `PCIE_DT_INST_ID`

```c
#define PCIE_DT_INST_ID ( inst)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
PCIE_DT_ID(DT_DRV_INST(inst))
```

获取节点的 PCI Express（PCIe）厂商 ID 和设备 ID（Vendor and Device ID）。

等价于 PCIE_DT_ID(DT_DRV_INST(inst))。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号。 |

返回（Returns）：以 pcie_id_t 表示的厂商标识符／设备标识符组合（VID/DID）。

<a id="ga7b500200f090dc95322fe670bf64628d"></a>

### `PCIE_HOST_CONTROLLER`

```c
#define PCIE_HOST_CONTROLLER ( n)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
PCIE_BDF(0, 0, n)
```

获取指定 PCI 主机控制器（Host Controller）的总线－设备－功能号（BDF）。

PCIE_BDF(0, 0, 0) 对应的 PCI 主机控制器报告多功能设备（Multifunction Device）时，此宏很有用；此时该端点的每个功能（Function）自身都可能是主机控制器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `n` | 总线编号（Bus Number）。 |

返回（Returns）：给定主机控制器（Host Controller）的 BDF 值。

<a id="gac7d5c41ea3c8999126d89d95961b430b"></a>

### `PCIE_ID_IS_VALID`

```c
#define PCIE_ID_IS_VALID ( id)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((id != PCIE_ID_NONE) && \
(id != PCIE_ID(0x0000, 0x0000)) && \
(id != PCIE_ID(0xFFFF, 0x0000)) && \
(id != PCIE_ID(0x0000, 0xFFFF)))
```

<a id="ga34f56e87ececf58b285e91341cd27d23"></a>

### `PCIE_IO_BASE`

```c
#define PCIE_IO_BASE ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((w) & 0xffUL)
```

<a id="gafc1acf0ac9b46629497c7a552f5650ce"></a>

### `PCIE_IO_BASE_LIMIT_UPPER`

```c
#define PCIE_IO_BASE_LIMIT_UPPER 12U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga88669a9ca40294cee41bb163a908737f"></a>

### `PCIE_IO_BASE_LIMIT_UPPER_VAL`

```c
#define PCIE_IO_BASE_LIMIT_UPPER_VAL ( iobu, iolu )
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((iobu) & 0xffffUL) |                   \
 (((iolu) & 0xffffUL) << 16))
```

<a id="ga8bf9a619d6d83cbb009a7f18b501db92"></a>

### `PCIE_IO_BASE_UPPER`

```c
#define PCIE_IO_BASE_UPPER ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((w) & 0xffffUL)
```

<a id="ga4629a222d00917b2e3cad6aadbfd2ec1"></a>

### `PCIE_IO_LIMIT`

```c
#define PCIE_IO_LIMIT ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 8) & 0xffUL)
```

<a id="ga76a59c926f2760a04c4d8439cb227fe2"></a>

### `PCIE_IO_LIMIT_UPPER`

```c
#define PCIE_IO_LIMIT_UPPER ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 16) & 0xffffUL)
```

<a id="ga111eab92400e240ec5b7f08caf1b8a87"></a>

### `PCIE_IO_SEC_STATUS`

```c
#define PCIE_IO_SEC_STATUS 7U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga61f05b2c4cd5c672af43960b320e33bc"></a>

### `PCIE_IO_SEC_STATUS_VAL`

```c
#define PCIE_IO_SEC_STATUS_VAL ( iob, iol, sec_status )
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((iob) & 0xffUL) |                          \
 (((iol) & 0xffUL) << 8) |                   \
 (((sec_status) & 0xffffUL) << 16))
```

<a id="ga6616499a7be31d40af31bb8134aa4a51"></a>

### `PCIE_IRQ_CONNECT`

```c
#define PCIE_IRQ_CONNECT ( bdf_p, irq_p, priority_p, isr_p, isr_param_p, flags_p )
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
ARCH_PCIE_IRQ_CONNECT(bdf_p, irq_p, priority_p,                 \
                      isr_p, isr_param_p, flags_p)
```

为 PCIe 端点中断请求（Endpoint IRQ）初始化中断处理函数。

此例程仅供使用 PCIe 总线、采用固定 IRQ 或基于消息信号中断（MSI）的 IRQ 的驱动使用，也就是不在运行时检测 IRQ。运行时检测的情况请参见 pcie_connect_dynamic_irq()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf_p` | PCIe 端点的总线／设备／功能地址（BDF）。 |
| `irq_p` | IRQ 线路编号。 |
| `priority_p` | 中断优先级。 |
| `isr_p` | 中断服务例程的地址。 |
| `isr_param_p` | 传给中断服务例程的参数。 |
| `flags_p` | 架构专有的 IRQ 配置标志。 |

<a id="ga1ce9e061b5a773f3ee74f78893174f9e"></a>

### `PCIE_MAX_BUS`

```c
#define PCIE_MAX_BUS (0xFFFFFFFFU & PCIE_BDF_BUS_MASK)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga8809359a58c787a939d01f25e12ac51a"></a>

### `PCIE_MAX_DEV`

```c
#define PCIE_MAX_DEV (0xFFFFFFFFU & PCIE_BDF_DEV_MASK)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="gaee8ddb7b7b1354fd5c835b67321f286b"></a>

### `PCIE_MAX_FUNC`

```c
#define PCIE_MAX_FUNC (0xFFFFFFFFU & PCIE_BDF_FUNC_MASK)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="gacd6be1e38666a6a137b1654007cf293a"></a>

### `PCIE_MEM_BASE`

```c
#define PCIE_MEM_BASE ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((w) & 0xffffUL)
```

<a id="ga6fbcd3f523deb069aa31bcd31973d00b"></a>

### `PCIE_MEM_BASE_LIMIT`

```c
#define PCIE_MEM_BASE_LIMIT 8U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga93a6dbe27d3d11be29397ae80c58a589"></a>

### `PCIE_MEM_BASE_LIMIT_VAL`

```c
#define PCIE_MEM_BASE_LIMIT_VAL ( memb, meml )
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((memb) & 0xffffUL) |              \
 (((meml) & 0xffffUL) << 16))
```

<a id="ga9f5d23ad0674aed0bf5c1869621de303"></a>

### `PCIE_MEM_LIMIT`

```c
#define PCIE_MEM_LIMIT ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 16) & 0xffffUL)
```

<a id="ga5f7aa0fc063ec072bf7e89fca603c825"></a>

### `PCIE_PREFETCH_BASE`

```c
#define PCIE_PREFETCH_BASE ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
((w) & 0xffffUL)
```

<a id="ga8dd5906e8d735210d9f8ca25d39684b4"></a>

### `PCIE_PREFETCH_BASE_LIMIT`

```c
#define PCIE_PREFETCH_BASE_LIMIT 9U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga02b269663488e7c7469415622390ce55"></a>

### `PCIE_PREFETCH_BASE_LIMIT_VAL`

```c
#define PCIE_PREFETCH_BASE_LIMIT_VAL ( pmemb, pmeml )
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((pmemb) & 0xffffUL) |                    \
 (((pmeml) & 0xffffUL) << 16))
```

<a id="ga6ebdd02e0599f33becb6cf413be0a8cd"></a>

### `PCIE_PREFETCH_BASE_UPPER`

```c
#define PCIE_PREFETCH_BASE_UPPER 10U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="gaf0a18504a4eb2061d1afc90fc7b8ee21"></a>

### `PCIE_PREFETCH_LIMIT`

```c
#define PCIE_PREFETCH_LIMIT ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 16) & 0xffffUL)
```

<a id="gab0eda55fd8c2c4025dc4350ef946a61b"></a>

### `PCIE_PREFETCH_LIMIT_UPPER`

```c
#define PCIE_PREFETCH_LIMIT_UPPER 11U
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

<a id="ga804b34fd47ba065287e0257fac84ac35"></a>

### `PCIE_SEC_STATUS`

```c
#define PCIE_SEC_STATUS ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 16) & 0xffffUL)
```

<a id="gaa05e49d0cafbe51b7742354470d07bd0"></a>

### `PCIE_SECONDARY_LATENCY_TIMER`

```c
#define PCIE_SECONDARY_LATENCY_TIMER ( w)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

展开值（Value）：

```c
(((w) >> 24) & 0xffUL)
```

<a id="gaf9748042a4f3c8d912d19df1ccf737fb"></a>

### `pcie_bdf_t`

```c
typedef uint32_t pcie_bdf_t
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

唯一的 PCI(e) 端点（Endpoint），由总线、设备、功能号标识。

PCI(e) 端点在拓扑中由总线、设备、功能三元组（Bus, Device, Function）唯一标识。由于设备树引用这些三元组，其内部结构记录在 include/dt-bindings/pcie/pcie.h 中，参见 PCIE_BDF() 及相关宏。

<a id="ga30840d0e312e35f00790660193fd4c04"></a>

### `pcie_id_t`

```c
typedef uint32_t pcie_id_t
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

唯一的 PCI(e) 标识符（Identifier），由厂商 ID 和设备 ID 组成。

每个端点的 PCIE_CONF_ID 寄存器包含厂商标识符和设备标识符对（Vendor ID, Device ID），用于告知系统该 PCI(e) 端点是什么设备。更多说明同样参见 include/dt-bindings/pcie/pcie.h 中的 `PCIE_ID_*` 宏。

<a id="ga922580e4fb6200ef75425bb54801ceda"></a>

### `pcie_scan_cb_t`

```c
typedef bool(* pcie_scan_cb_t) (pcie_bdf_t bdf, pcie_id_t id, void *cb_data)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

扫描 PCI 端点（Endpoints）所用的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | 找到的端点的 BDF 值。 |
| `id` | 找到的端点的厂商与设备标识符（Vendor & Device ID）。 |
| `cb_data` | 自定义、特定于使用场景的数据（Use Case Specific Data）。 |

返回（Returns）：true 表示继续扫描，false 表示停止扫描。

<a id="gabe00c00fc0af29786c3b42f22f82aecf"></a>

### `anonymous enum`

```c
anonymous enum
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PCIE_SCAN_RECURSIVE` | 扫描所有可用 PCI 主机控制器（Host Controllers）及下级总线（Sub-buses）。 |
| `PCIE_SCAN_CB_ALL` | 对所有端点类型（Endpoint Types）执行回调，包括桥（Bridges）。 |

<a id="gad69ae431e5f91992f071dee9d7fa9110"></a>

### `pcie_alloc_irq()`

```c
unsigned int pcie_alloc_irq ( pcie_bdf_t bdf)
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

为端点（Endpoint）分配中断请求（IRQ）。

此函数先检查 IRQ 寄存器；包含有效值时，直接返回该值，否则尝试分配新的 IRQ。只有未设置 CONFIG_PCIE_CONTROLLER 时才公开此函数，因此它可用于适合按架构进行 PCIe 设备动态 IRQ 分配的场景。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | PCI／PCIe 端点（Endpoint）。 |

返回（Returns）：IRQ 编号；分配失败时为 PCIE_CONF_INTR_IRQ_NONE。

<a id="ga10ecc667c564548e4ddf3ca4374242b5"></a>

### `pcie_conf_read()`

```c
uint32_t pcie_conf_read ( pcie_bdf_t bdf, unsigned int reg )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

从端点配置空间（Endpoint Configuration Space）读取 32 位字（Word）。

此函数由架构／SoC／开发板代码（Arch/SoC/Board Code）导出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | PCI(e) 端点（Endpoint）。 |
| `reg` | 配置字索引（Configuration Word Index），不是地址。 |

**返回（Returns）**：返回值：读出的字（Word）；端点或该字不存在时为 `0xFFFFFFFFU`。

<a id="ga47a2e88935e04330d449db5463d9f21a"></a>

### `pcie_conf_write()`

```c
void pcie_conf_write ( pcie_bdf_t bdf, unsigned int reg, uint32_t data )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

向端点配置空间（Endpoint Configuration Space）写入 32 位字（Word）。

此函数由架构／SoC／开发板代码（Arch/SoC/Board Code）导出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | PCI(e) 端点（Endpoint）。 |
| `reg` | 配置字索引（Configuration Word Index），不是地址。 |
| `data` | 要写入的值（Value）。 |

<a id="ga14970194de1024a1a4669b69f932a4f5"></a>

### `pcie_connect_dynamic_irq()`

```c
bool pcie_connect_dynamic_irq ( pcie_bdf_t bdf, unsigned int irq, unsigned int priority, void(* routine )(const void *parameter), const void * parameter, uint32_t flags )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

将 PCIe 端点中断请求（IRQ）动态连接到中断服务例程（ISR）处理函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | 要检查的 PCI 端点（Endpoint）。 |
| `irq` | 要连接的 IRQ，参见 pcie_alloc_irq()。 |
| `priority` | IRQ 优先级（Priority）。 |
| `routine` | 要连接到 IRQ 的中断服务例程（ISR Handler）。 |
| `parameter` | 提供给处理程序（Handler）的参数。 |
| `flags` | IRQ 连接标志（Connection Flags）。 |

返回（Returns）：连接成功时为 true，否则为 false。

<a id="ga56e724c9bfd7f44c550ccff1b46978a8"></a>

### `pcie_get_cap()`

```c
uint32_t pcie_get_cap ( pcie_bdf_t bdf, uint32_t cap_id )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

在端点配置空间（Configuration Space）中查找 PCI(e) 能力（Capability）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | 要检查的 PCI 端点（Endpoint）。 |
| `cap_id` | 所关注的能力标识符（Capability ID）。 |

返回（Returns）：配置字（Configuration Word）的索引；没有该能力时为 0。

<a id="ga5db0d2a5946d20406070b47a1a7acf21"></a>

### `pcie_get_ext_cap()`

```c
uint32_t pcie_get_ext_cap ( pcie_bdf_t bdf, uint32_t cap_id )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

在端点配置空间（Configuration Space）中查找 PCI(e) 扩展能力（Extended Capability）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | 要检查的 PCI 端点（Endpoint）。 |
| `cap_id` | 所关注的能力标识符（Capability ID）。 |

返回（Returns）：配置字（Configuration Word）的索引；没有该能力时为 0。

<a id="ga3523bbdfd67d4b56cf6cd86c98c830bf"></a>

### `pcie_get_iobar()`

```c
bool pcie_get_iobar ( pcie_bdf_t bdf, unsigned int bar_index, struct pcie_bar * iobar )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

获取指定 BAR 索引处的输入／输出基址寄存器（I/O BAR）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | PCI／PCIe 端点（Endpoint）。 |
| `bar_index` | 从 0 开始的基地址寄存器索引（BAR Index）。 |
| `iobar` | 指向 struct pcie_bar 的指针。 |

返回（Returns）：找到有效的 I/O 基地址寄存器（I/O BAR）时为 true，否则为 false。

<a id="gaed7fef462ba02a22b5875b1a2c0d965a"></a>

### `pcie_get_irq()`

```c
unsigned int pcie_get_irq ( pcie_bdf_t bdf)
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

返回固件／开发板为端点分配的中断请求（IRQ）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | PCI／PCIe 端点（Endpoint）。 |

返回（Returns）：IRQ 编号；未知时为 PCIE_CONF_INTR_IRQ_NONE。

<a id="gadeb891fbb5b900eb60de22d40afe355e"></a>

### `pcie_get_mbar()`

```c
bool pcie_get_mbar ( pcie_bdf_t bdf, unsigned int bar_index, struct pcie_bar * mbar )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

获取指定基址寄存器（BAR）索引处的内存 BAR（MBAR）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | PCI／PCIe 端点（Endpoint）。 |
| `bar_index` | 从 0 开始的基地址寄存器索引（BAR Index）。 |
| `mbar` | 指向 struct pcie_bar 的指针。 |

返回（Returns）：找到有效的内存基地址寄存器（mbar）时为 true，否则为 false。

<a id="gafb69216f9224a9040b1f0b58eb286196"></a>

### `pcie_irq_enable()`

```c
void pcie_irq_enable ( pcie_bdf_t bdf, unsigned int irq )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

使能 PCI(e) 端点，使其可产生指定中断请求（IRQ）。

启用了消息信号中断（MSI）且端点支持它时，将配置端点通过 MSI 产生指定 IRQ。否则，假定启动固件（Boot Firmware）已将中断路由到指定 IRQ，并在 I/O APIC 或其他适当位置启用该 IRQ。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | PCI／PCIe 端点（Endpoint）。 |
| `irq` | 要产生的 IRQ。 |

<a id="gaa81d98a9ee58062c02be576fb0dfefd9"></a>

### `pcie_probe_iobar()`

```c
bool pcie_probe_iobar ( pcie_bdf_t bdf, unsigned int index, struct pcie_bar * iobar )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

探测分配给端点的第 n 个 I/O BAR 地址。

PCI(e) 端点具有零个或多个 I/O 区域（I/O Regions）。调用者可用 index=0..n 逐个调用此函数进行枚举。由于最多有 6 个基地址寄存器（BARs），n 必须小于 6。索引保持端点 BAR 的顺序，例如 index 为 0 时返回端点编号最小的 I/O BAR。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | PCI／PCIe 端点（Endpoint）。 |
| `index` | 从 0 开始的索引（Index）。 |
| `iobar` | 指向 struct pcie_bar 的指针。 |

返回（Returns）：找到有效的 I/O 基地址寄存器（I/O BAR）时为 true，否则为 false。

<a id="gad8463013e51c4ddcca7b5f805f918685"></a>

### `pcie_probe_mbar()`

```c
bool pcie_probe_mbar ( pcie_bdf_t bdf, unsigned int index, struct pcie_bar * mbar )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

探测分配给端点的第 n 个内存映射输入输出地址（MMIO Address）。

PCI(e) 端点具有零个或多个内存映射区域（Memory-mapped Regions）。调用者可用 index=0..n 逐个调用此函数进行枚举。由于最多有 6 个基地址寄存器（BARs），n 必须小于 6。索引保持端点 BAR 的顺序，例如 index 为 0 时返回端点编号最小的内存 BAR。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | PCI／PCIe 端点（Endpoint）。 |
| `index` | 从 0 开始的索引（Index）。 |
| `mbar` | 指向 struct pcie_bar 的指针。 |

返回（Returns）：找到有效的内存基地址寄存器（mbar）时为 true，否则为 false。

<a id="ga9a7b3c202f91d37fe8445d5016f4c6ab"></a>

### `pcie_scan()`

```c
int pcie_scan ( const struct pcie_scan_opt * opt)
```

```c
#include <zephyr/drivers/pcie/pcie.h>
```

扫描 PCIe 设备（Devices）。

扫描一个或多个 PCI 总线（Buses），查找可用端点（Endpoints）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `opt` | 决定扫描执行方式的选项（Scan Options）。 |

返回（Returns）：成功时为 0，失败时为负 POSIX 错误码。

<a id="ga3516fec89df75eb3d77f54193059fc5c"></a>

### `pcie_set_cmd()`

```c
void pcie_set_cmd ( pcie_bdf_t bdf, uint32_t bits, bool on )
```

声明属性：`extern`。

```c
#include <zephyr/drivers/pcie/pcie.h>
```

设置或清除端点命令／状态寄存器（Command/Status Register）中的位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | PCI／PCIe 端点（Endpoint）。 |
| `bits` | 所关注位的集合（Powerset of Bits）。 |
| `on` | 使用 true 设置这些位，使用 false 清除它们。 |


## 8.8\_原页交叉引用（Cross References）

- [PCIe能力（Capabilities）。](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__capabilities.html)
- [PCIe 主机消息信号中断（MSI）接口](../api_vector_pipeline_topic_reference/P025_PCIe 主机消息信号中断（MSI）接口.md)
- [PCIe 主机精确时间测量（PTM）接口](../api_extension_topic_reference/P025_PCIe 主机精确时间测量（PTM）接口.md)
- [PCIe 虚拟通道（Virtual Channel）主机接口](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md)
- [pcie_dev](../platform_security_model_reference/P028_pcie_dev_结构体.md)
- [pcie_bar](../platform_security_model_reference/P025_pcie_bar_结构体.md)
- [pcie_scan_opt](../platform_security_model_reference/P030_pcie_scan_opt_结构体.md)
- [PCIE_BDF_BUS_MASK](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#a193dd359d7a96bdd904662717c7fbf6d)
- [PCIE_BDF_DEV_MASK](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#a85cc69963a93046bda0f1594803af9eb)
- [PCIE_BDF_FUNC_MASK](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#ab481360fa29cf086cc5369e6f1860a5f)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zephyr/drivers/pcie/pcie.h](../api_file_host_video_reference/P004_zephyr__drivers__pcie__pcie.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [PCIE_BDF_NONE](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#a6268e6c107a85fbc6035eca5e6b3cfd6)
- [DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [PCIE_ID](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#af3107df4821c35c5f217a2b8bc49bce6)
- [PCIE_BDF](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#a09a440a45623a282c23eaa2cfeef63d2)
- [PCIE_ID_NONE](../api_file_reference/P069_zephyr__dt-bindings__pcie__pcie.h_文件参考.md#a23ce79d01609cb14f0cd4b2298e13b14)
- [ARCH_PCIE_IRQ_CONNECT](../fatal_irq_reference/P008_架构中断接口.md#gaf6abdfe089e423aa209f7ad4b8934022)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_a6268e6c107a85fbc6035eca5e6b3cfd6"></a>
<a id="agroup__devicetree-generic-prop_html_ga5e5bfc9b1a6627b3f73014329e96340f"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="agroup__pcie__host__interface_html_ga304228150cd8ec56aa24be468e9d79bf"></a>
<a id="astructpcie__dev_html"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__pcie__host__interface_html_gad0b870d891458c4ebd7ab2ac1c372eec"></a>
<a id="agroup__pcie__host__interface_html_gab6c472838e13293980cd53c65aaa3c47"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_af3107df4821c35c5f217a2b8bc49bce6"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_a09a440a45623a282c23eaa2cfeef63d2"></a>
<a id="adt-bindings_2pcie_2pcie_8h_html_a23ce79d01609cb14f0cd4b2298e13b14"></a>
<a id="agroup__arch-irq_html_gaf6abdfe089e423aa209f7ad4b8934022"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggabe00c00fc0af29786c3b42f22f82aecfa228932ef6533931a9ae55e37dc38f3c4"></a>
<a id="ggabe00c00fc0af29786c3b42f22f82aecfa3579c18ade658f55affd41bfd38f9072"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_元素（Elements）.md) · [返回大纲](大纲.md) · [下一章](P009_统计信息（Statistics）。.md)
