---
id: learning.zephyr-docs.api-extension-topic-reference.page-25
title: PCIe 主机精确时间测量（PTM）接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__ptm__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_PCIe 主机精确时间测量（PTM）接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__ptm__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCIe 主机精确时间测量（PTM）接口

<a id="details"></a>

PCIe 主机精确时间测量（PTM）接口

<a id="header-files"></a>
<a id="files"></a>

## 25.1\_文件（Files）

<a id="r_ptm_2Eh"></a>

```c
file ptm.h
```

相关声明：[ptm.h](../api_file_supplement_reference/P093_zephyr__drivers__pcie__ptm.h_文件参考.md)。

PCIe精确时间测量（Precision Time Measurement，PTM）主机API的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.2\_函数（Functions）

<a id="r_gae868e8140938c293ad5685cd77131924"></a>

```c
bool pcie_ptm_enable (pcie_bdf_t bdf)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ptm_enable](#gae868e8140938c293ad5685cd77131924)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

在端点（Endpoint）上启用精确时间测量（Precision Time Measurement，PTM）。

## 25.3\_详细说明（Detailed Documentation）

<a id="gae868e8140938c293ad5685cd77131924"></a>

### `pcie_ptm_enable()`

```c
bool pcie_ptm_enable ( pcie_bdf_t bdf)
```

```c
#include <zephyr/drivers/pcie/ptm.h>
```

在端点（Endpoint）上启用精确时间测量（Precision Time Measurement，PTM）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bdf` | PCI／PCIe 端点（Endpoint）。 |

返回（Returns）：成功时为 `true`，否则为 `false`。


## 25.4\_原页交叉引用（Cross References）

- [ptm.h](../api_file_supplement_reference/P093_zephyr__drivers__pcie__ptm.h_文件参考.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P024_PAW32xx API主题.md) · [返回大纲](大纲.md) · [下一章](P026_平台环境控制接口（PECI）.md)
