---
id: learning.zephyr-docs.device-power-control-model-reference.page-80
title: sam_pmc_data_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsam__pmc__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第80章\_sam\_pmc\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsam__pmc__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电源管理控制器（PMC）设备的运行时数据。

```c
#include <zephyr/drivers/clock_control/mchp_sam_pmc.h>
```

<a id="details"></a>

电源管理控制器（PMC）设备的运行时数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 80.1\_数据成员（Data Fields）

<a id="r_abdab335def8be1593fdac72a5092a77d"></a>

```c
struct pmc_data * pmc
```

相关声明：[pmc](#abdab335def8be1593fdac72a5092a77d)。

后端 PMC 实例数据。

## 80.2\_详细说明（Detailed Documentation）

<a id="abdab335def8be1593fdac72a5092a77d"></a>

### `pmc`

```c
struct pmc_data* sam_pmc_data::pmc
```

后端 PMC 实例数据。

本数据类型文档由以下文件生成：

- `zephyr/drivers/clock_control/mchp_sam_pmc.h`

## 80.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control/mchp_sam_pmc.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__sam__pmc_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P079_sam_pmc_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P081_sam_sckc_config_结构体.md)
