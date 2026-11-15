---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-36
title: zephyr__drivers__pcie__vc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/vc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_zephyr\_\_drivers\_\_pcie\_\_vc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/vc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCIe虚拟信道（Virtual Channel）支持API的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <stdbool.h>
#include <zephyr/drivers/pcie/pcie.h>
```

查看此文件的源码。

PCIe虚拟信道（Virtual Channel）支持API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 36.1\_数据结构（Data Structures）

<a id="r_pcie_5Fvctc_5Fmap"></a>

```c
struct pcie_vctc_map
```

相关声明：[pcie_vctc_map](../platform_security_model_reference/P031_pcie_vctc_map_结构体.md)。

流量类别（TC）到虚拟信道（VC）的映射。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 36.2\_宏定义（Macros）

<a id="r_ga0567fabc02828372f4e901bb193c9b89"></a>

```c
#define PCIE_VC_MAX_COUNT 8U
```

相关声明：[PCIE_VC_MAX_COUNT](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga0567fabc02828372f4e901bb193c9b89)。

虚拟通道（Virtual Channel，VC）的最大数量：1 个默认 VC 加 7 个扩展 VC。

<a id="r_gae1ec2ec11736ed97c6e41a2d8c7f4a39"></a>

```c
#define PCIE_VC_SET_TC0 BIT(0)
```

相关声明：[PCIE_VC_SET_TC0](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#gae1ec2ec11736ed97c6e41a2d8c7f4a39)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）0 映射到虚拟信道（VC）。

<a id="r_gab4d53cac004ac7b6258fbd387fc90051"></a>

```c
#define PCIE_VC_SET_TC1 BIT(1)
```

相关声明：[PCIE_VC_SET_TC1](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#gab4d53cac004ac7b6258fbd387fc90051)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）1 映射到虚拟信道（VC）。

<a id="r_ga3d0311d99240527d86e8f8452f405736"></a>

```c
#define PCIE_VC_SET_TC2 BIT(2)
```

相关声明：[PCIE_VC_SET_TC2](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga3d0311d99240527d86e8f8452f405736)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）2 映射到虚拟信道（VC）。

<a id="r_ga3122990fd5879e076346efdc706b640e"></a>

```c
#define PCIE_VC_SET_TC3 BIT(3)
```

相关声明：[PCIE_VC_SET_TC3](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga3122990fd5879e076346efdc706b640e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）3 映射到虚拟信道（VC）。

<a id="r_ga2259546ee27ce43dfb15ea69bdb66a7c"></a>

```c
#define PCIE_VC_SET_TC4 BIT(4)
```

相关声明：[PCIE_VC_SET_TC4](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga2259546ee27ce43dfb15ea69bdb66a7c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）4 映射到虚拟信道（VC）。

<a id="r_ga9a796b9570585c60c70fb641e0a5a733"></a>

```c
#define PCIE_VC_SET_TC5 BIT(5)
```

相关声明：[PCIE_VC_SET_TC5](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga9a796b9570585c60c70fb641e0a5a733)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）5 映射到虚拟信道（VC）。

<a id="r_gaf8ff3086a4a5003f303f7b17e2319c09"></a>

```c
#define PCIE_VC_SET_TC6 BIT(6)
```

相关声明：[PCIE_VC_SET_TC6](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#gaf8ff3086a4a5003f303f7b17e2319c09)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）6 映射到虚拟信道（VC）。

<a id="r_gacbd9b1877530539d1a14a35d35744634"></a>

```c
#define PCIE_VC_SET_TC7 BIT(7)
```

相关声明：[PCIE_VC_SET_TC7](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#gacbd9b1877530539d1a14a35d35744634)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

将流量类别（Traffic Class）7 映射到虚拟信道（VC）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 36.3\_函数（Functions）

<a id="r_ga179628024fc9d651d1027833377ee9d2"></a>

```c
int pcie_vc_enable (pcie_bdf_t bdf)
```

相关声明：[pcie_vc_enable](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga179628024fc9d651d1027833377ee9d2)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

启用 PCIe 虚拟通道（Virtual Channel）处理。

<a id="r_ga89c684f7ff5e82da86df27d061a8fbd7"></a>

```c
int pcie_vc_disable (pcie_bdf_t bdf)
```

相关声明：[pcie_vc_disable](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga89c684f7ff5e82da86df27d061a8fbd7)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

禁用 PCIe 虚拟通道（Virtual Channel）处理。

<a id="r_gafd4429e8c14821c685c4103f34b340c8"></a>

```c
int pcie_vc_map_tc (pcie_bdf_t bdf, struct pcie_vctc_map *map)
```

相关声明：[pcie_vc_map_tc](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#gafd4429e8c14821c685c4103f34b340c8)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)、[pcie_vctc_map](../platform_security_model_reference/P031_pcie_vctc_map_结构体.md)。

映射 PCIe 流量类别／虚拟通道（Traffic Class/Virtual Channel，TC/VC）。


## 36.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/drivers/pcie/pcie.h](../api_source_pcie_hid_reference/P001_pcie.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P901_vc.h_源码浏览.md)
- [pcie_vctc_map](../platform_security_model_reference/P031_pcie_vctc_map_结构体.md)
- [PCIE_VC_MAX_COUNT](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga0567fabc02828372f4e901bb193c9b89)
- [PCIE_VC_SET_TC0](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#gae1ec2ec11736ed97c6e41a2d8c7f4a39)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [PCIE_VC_SET_TC1](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#gab4d53cac004ac7b6258fbd387fc90051)
- [PCIE_VC_SET_TC2](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga3d0311d99240527d86e8f8452f405736)
- [PCIE_VC_SET_TC3](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga3122990fd5879e076346efdc706b640e)
- [PCIE_VC_SET_TC4](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga2259546ee27ce43dfb15ea69bdb66a7c)
- [PCIE_VC_SET_TC5](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga9a796b9570585c60c70fb641e0a5a733)
- [PCIE_VC_SET_TC6](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#gaf8ff3086a4a5003f303f7b17e2319c09)
- [PCIE_VC_SET_TC7](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#gacbd9b1877530539d1a14a35d35744634)
- [pcie_vc_enable](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga179628024fc9d651d1027833377ee9d2)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)
- [pcie_vc_disable](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#ga89c684f7ff5e82da86df27d061a8fbd7)
- [pcie_vc_map_tc](../api_interaction_transport_topic_reference/P014_PCIe 虚拟通道（Virtual Channel）主机接口.md#gafd4429e8c14821c685c4103f34b340c8)

<a id="header-details"></a>

---

[上一章](P035_zephyr__dt-bindings__pinctrl__stm32f1-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P037_zephyr__dt-bindings__gpio__wisblock-sensor-slot.h_文件参考.md)
