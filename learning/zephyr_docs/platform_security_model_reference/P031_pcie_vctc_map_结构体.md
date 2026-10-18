---
id: learning.zephyr-docs.platform-security-model-reference.page-31
title: pcie_vctc_map_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpcie__vctc__map.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_pcie\_vctc\_map\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpcie__vctc__map.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

流量类别（TC）到虚拟信道（VC）的映射。

```c
#include <zephyr/drivers/pcie/vc.h>
```

<a id="details"></a>

流量类别（TC）到虚拟信道（VC）的映射。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_a93955e5b5e4ef26a81d363e8f10806fc"></a>

```c
uint8_t vc_tc [8U]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[vc_tc](#a93955e5b5e4ef26a81d363e8f10806fc)。

通过设置相应位，将流量类别（TC）映射到各虚拟通道（VC）。注意：同一个位不能在多个 VC 中重复置位。

<a id="r_aa70f7e0a4f2eadcf652e8858b2fc0304"></a>

```c
int vc_count
```

相关声明：[vc_count](#aa70f7e0a4f2eadcf652e8858b2fc0304)。

所处理的 VC 数量。

## 31.2\_详细说明（Detailed Documentation）

<a id="aa70f7e0a4f2eadcf652e8858b2fc0304"></a>

### `vc_count`

```c
int pcie_vctc_map::vc_count
```

所处理的 VC 数量。

<a id="a93955e5b5e4ef26a81d363e8f10806fc"></a>

### `vc_tc`

```c
uint8_t pcie_vctc_map::vc_tc[8U]
```

通过设置相应位，将流量类别（TC）映射到各虚拟通道（VC）。注意：同一个位不能在多个 VC 中重复置位。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pcie/vc.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pcie/vc.h](https://docs.zephyrproject.org/latest/doxygen/html/vc_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_pcie_scan_opt_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_scmi_agent_info_结构体.md)
