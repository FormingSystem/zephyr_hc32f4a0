---
id: learning.zephyr-docs.api-file-supplement-reference.page-93
title: zephyr__drivers__pcie__ptm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ptm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第93章\_zephyr\_\_drivers\_\_pcie\_\_ptm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ptm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCIe精确时间测量（Precision Time Measurement，PTM）主机API的头文件。

<a id="details"></a>

```c
#include <stddef.h>
#include <zephyr/types.h>
```

查看此文件的源码。

PCIe精确时间测量（Precision Time Measurement，PTM）主机API的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 93.1\_函数（Functions）

<a id="r_gae868e8140938c293ad5685cd77131924"></a>

```c
bool pcie_ptm_enable (pcie_bdf_t bdf)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[pcie_ptm_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__ptm__interface.html#gae868e8140938c293ad5685cd77131924)、[pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)。

在端点（Endpoint）上启用精确时间测量（Precision Time Measurement，PTM）。


## 93.2\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P679_ptm.h_源码浏览.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [pcie_ptm_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__ptm__interface.html#gae868e8140938c293ad5685cd77131924)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)

<a id="header-details"></a>

---

[上一章](P092_zephyr__bluetooth__mesh__priv_beacon_srv.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P094_zephyr__drivers__pwm__pwm_fake.h_文件参考.md)
