---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-14
title: PCIe 虚拟通道（Virtual Channel）主机接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__vc__host__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_PCIe 虚拟通道（Virtual Channel）主机接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__vc__host__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCIe 虚拟通道（Virtual Channel）主机接口

<a id="details"></a>

PCIe 虚拟通道（Virtual Channel）主机接口

<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_vc_2Eh"></a>

```c
file vc.h
```

相关声明：[vc.h](https://docs.zephyrproject.org/latest/doxygen/html/vc_8h.html)。

PCIe虚拟信道（Virtual Channel）支持API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.2\_数据结构（Data Structures）

<a id="r_pcie_5Fvctc_5Fmap"></a>

```c
struct pcie_vctc_map
```

相关声明：[pcie_vctc_map](../platform_security_model_reference/P031_pcie_vctc_map_结构体.md)。

流量类别（TC）到虚拟信道（VC）的映射。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.3\_宏定义（Macros）

<a id="r_ga0567fabc02828372f4e901bb193c9b89"></a>

```c
#define PCIE_VC_MAX_COUNT 8U
```

相关声明：[PCIE_VC_MAX_COUNT](#ga0567fabc02828372f4e901bb193c9b89)。

虚拟通道（Virtual Channel，VC）的最大数量：1 个默认 VC 加 7 个扩展 VC。

<a id="r_gae1ec2ec11736ed97c6e41a2d8c7f4a39"></a>

```c
#define PCIE_VC_SET_TC0 BIT(0)
```

相关声明：[PCIE_VC_SET_TC0](#gae1ec2ec11736ed97c6e41a2d8c7f4a39)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）0 映射到虚拟信道（VC）。

<a id="r_gab4d53cac004ac7b6258fbd387fc90051"></a>

```c
#define PCIE_VC_SET_TC1 BIT(1)
```

相关声明：[PCIE_VC_SET_TC1](#gab4d53cac004ac7b6258fbd387fc90051)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）1 映射到虚拟信道（VC）。

<a id="r_ga3d0311d99240527d86e8f8452f405736"></a>

```c
#define PCIE_VC_SET_TC2 BIT(2)
```

相关声明：[PCIE_VC_SET_TC2](#ga3d0311d99240527d86e8f8452f405736)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）2 映射到虚拟信道（VC）。

<a id="r_ga3122990fd5879e076346efdc706b640e"></a>

```c
#define PCIE_VC_SET_TC3 BIT(3)
```

相关声明：[PCIE_VC_SET_TC3](#ga3122990fd5879e076346efdc706b640e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）3 映射到虚拟信道（VC）。

<a id="r_ga2259546ee27ce43dfb15ea69bdb66a7c"></a>

```c
#define PCIE_VC_SET_TC4 BIT(4)
```

相关声明：[PCIE_VC_SET_TC4](#ga2259546ee27ce43dfb15ea69bdb66a7c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）4 映射到虚拟信道（VC）。

<a id="r_ga9a796b9570585c60c70fb641e0a5a733"></a>

```c
#define PCIE_VC_SET_TC5 BIT(5)
```

相关声明：[PCIE_VC_SET_TC5](#ga9a796b9570585c60c70fb641e0a5a733)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）5 映射到虚拟信道（VC）。

<a id="r_gaf8ff3086a4a5003f303f7b17e2319c09"></a>

```c
#define PCIE_VC_SET_TC6 BIT(6)
```

相关声明：[PCIE_VC_SET_TC6](#gaf8ff3086a4a5003f303f7b17e2319c09)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）6 映射到虚拟信道（VC）。

<a id="r_gacbd9b1877530539d1a14a35d35744634"></a>

```c
#define PCIE_VC_SET_TC7 BIT(7)
```

相关声明：[PCIE_VC_SET_TC7](#gacbd9b1877530539d1a14a35d35744634)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）7 映射到虚拟信道（VC）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.4\_函数（Functions）

<a id="r_ga179628024fc9d651d1027833377ee9d2"></a>

```c
int pcie_vc_enable (pcie_bdf_t bdf)
```

相关声明：[pcie_vc_enable](#ga179628024fc9d651d1027833377ee9d2)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

启用 PCIe 虚拟通道（Virtual Channel）处理。

<a id="r_ga89c684f7ff5e82da86df27d061a8fbd7"></a>

```c
int pcie_vc_disable (pcie_bdf_t bdf)
```

相关声明：[pcie_vc_disable](#ga89c684f7ff5e82da86df27d061a8fbd7)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

禁用 PCIe 虚拟通道（Virtual Channel）处理。

<a id="r_gafd4429e8c14821c685c4103f34b340c8"></a>

```c
int pcie_vc_map_tc (pcie_bdf_t bdf, struct pcie_vctc_map *map)
```

相关声明：[pcie_vc_map_tc](#gafd4429e8c14821c685c4103f34b340c8)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[pcie_vctc_map](../platform_security_model_reference/P031_pcie_vctc_map_结构体.md)。

映射 PCIe 流量类别／虚拟通道（Traffic Class/Virtual Channel，TC/VC）。

## 14.5\_详细说明（Detailed Documentation）

<a id="ga0567fabc02828372f4e901bb193c9b89"></a>

### `PCIE_VC_MAX_COUNT`

```c
#define PCIE_VC_MAX_COUNT 8U
```

```c
#include <zephyr/drivers/pcie/vc.h>
```

虚拟通道（Virtual Channel，VC）的最大数量：1 个默认 VC 加 7 个扩展 VC。

<a id="gae1ec2ec11736ed97c6e41a2d8c7f4a39"></a>

### `PCIE_VC_SET_TC0`

```c
#define PCIE_VC_SET_TC0 BIT(0)
```

```c
#include <zephyr/drivers/pcie/vc.h>
```

将流量类别（Traffic Class）0 映射到虚拟信道（VC）。

<a id="gab4d53cac004ac7b6258fbd387fc90051"></a>

### `PCIE_VC_SET_TC1`

```c
#define PCIE_VC_SET_TC1 BIT(1)
```

```c
#include <zephyr/drivers/pcie/vc.h>
```

将流量类别（Traffic Class）1 映射到虚拟信道（VC）。

<a id="ga3d0311d99240527d86e8f8452f405736"></a>

### `PCIE_VC_SET_TC2`

```c
#define PCIE_VC_SET_TC2 BIT(2)
```

```c
#include <zephyr/drivers/pcie/vc.h>
```

将流量类别（Traffic Class）2 映射到虚拟信道（VC）。

<a id="ga3122990fd5879e076346efdc706b640e"></a>

### `PCIE_VC_SET_TC3`

```c
#define PCIE_VC_SET_TC3 BIT(3)
```

```c
#include <zephyr/drivers/pcie/vc.h>
```

将流量类别（Traffic Class）3 映射到虚拟信道（VC）。

<a id="ga2259546ee27ce43dfb15ea69bdb66a7c"></a>

### `PCIE_VC_SET_TC4`

```c
#define PCIE_VC_SET_TC4 BIT(4)
```

```c
#include <zephyr/drivers/pcie/vc.h>
```

将流量类别（Traffic Class）4 映射到虚拟信道（VC）。

<a id="ga9a796b9570585c60c70fb641e0a5a733"></a>

### `PCIE_VC_SET_TC5`

```c
#define PCIE_VC_SET_TC5 BIT(5)
```

```c
#include <zephyr/drivers/pcie/vc.h>
```

将流量类别（Traffic Class）5 映射到虚拟信道（VC）。

<a id="gaf8ff3086a4a5003f303f7b17e2319c09"></a>

### `PCIE_VC_SET_TC6`

```c
#define PCIE_VC_SET_TC6 BIT(6)
```

```c
#include <zephyr/drivers/pcie/vc.h>
```

将流量类别（Traffic Class）6 映射到虚拟信道（VC）。

<a id="gacbd9b1877530539d1a14a35d35744634"></a>

### `PCIE_VC_SET_TC7`

```c
#define PCIE_VC_SET_TC7 BIT(7)
```

```c
#include <zephyr/drivers/pcie/vc.h>
```

将流量类别（Traffic Class）7 映射到虚拟信道（VC）。

<a id="ga89c684f7ff5e82da86df27d061a8fbd7"></a>

### `pcie_vc_disable()`

```c
int pcie_vc_disable ( pcie_bdf_t bdf)
```

```c
#include <zephyr/drivers/pcie/vc.h>
```

禁用 PCIe 虚拟通道（Virtual Channel）处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | 目标 PCI 端点（Endpoint）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回负错误码。

<a id="ga179628024fc9d651d1027833377ee9d2"></a>

### `pcie_vc_enable()`

```c
int pcie_vc_enable ( pcie_bdf_t bdf)
```

```c
#include <zephyr/drivers/pcie/vc.h>
```

启用 PCIe 虚拟通道（Virtual Channel）处理。

**注意（Note）：**无法启用此功能属于非致命错误（Non-fatal Error）；使用该功能的代码应适当处理，例如输出提示信息后忽略此错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | 目标 PCI 端点（Endpoint）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回负错误码。

<a id="gafd4429e8c14821c685c4103f34b340c8"></a>

### `pcie_vc_map_tc()`

```c
int pcie_vc_map_tc ( pcie_bdf_t bdf, struct pcie_vctc_map * map )
```

```c
#include <zephyr/drivers/pcie/vc.h>
```

映射 PCIe 流量类别／虚拟通道（Traffic Class/Virtual Channel，TC/VC）。

**注意（Note）：**调用此函数之前必须禁用虚拟通道（VC），调用之后再启用，端点（Endpoint）才能使用该映射。

**注意（Note）：**无法启用此功能属于非致命错误（Non-fatal Error）；使用该功能的代码应适当处理，例如输出提示信息后忽略此错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | 目标 PCI 端点（Endpoint）。 |
| `map` | 要应用的流量类别／虚拟通道（TC/VC）映射。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回负错误码。


## 14.6\_原页交叉引用（Cross References）

- [vc.h](https://docs.zephyrproject.org/latest/doxygen/html/vc_8h.html)
- [pcie_vctc_map](../platform_security_model_reference/P031_pcie_vctc_map_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P015_NXP CPU 域协议（NXP CPU Domain Protocol）.md)
