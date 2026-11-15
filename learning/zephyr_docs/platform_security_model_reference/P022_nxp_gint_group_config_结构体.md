---
id: learning.zephyr-docs.platform-security-model-reference.page-22
title: nxp_gint_group_config_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnxp__gint__group__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_nxp\_gint\_group\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnxp__gint__group__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分组中断（GINT）的组配置。

```c
#include <zephyr/drivers/interrupt_controller/intc_nxp_gint.h>
```

<a id="details"></a>

分组中断（GINT）的组配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_a4a3d57e34c8386775bb0b6302fc2b7c3"></a>

```c
nxp_gint_trigger_type trigger
```

相关声明：[nxp_gint_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#a07f2264ca2366594a571858cc5ee6b9a)、[trigger](#a4a3d57e34c8386775bb0b6302fc2b7c3)。

触发类型：边沿或电平（edge/level）。

<a id="r_aac30f37bb02cc8d10cf308b666efd767"></a>

```c
nxp_gint_combination_type combination
```

相关声明：[nxp_gint_combination_type](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#abc9f321deac34cacd128dc16c2db3df6)、[combination](#aac30f37bb02cc8d10cf308b666efd767)。

组合逻辑：或或与（OR/AND）。

## 22.2\_详细说明（Detailed Documentation）

<a id="aac30f37bb02cc8d10cf308b666efd767"></a>

### `combination`

```c
nxp_gint_combination_type nxp_gint_group_config::combination
```

组合逻辑：或或与（OR/AND）。

<a id="a4a3d57e34c8386775bb0b6302fc2b7c3"></a>

### `trigger`

```c
nxp_gint_trigger_type nxp_gint_group_config::trigger
```

触发类型：边沿或电平（edge/level）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/interrupt_controller/intc_nxp_gint.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/drivers/interrupt_controller/intc_nxp_gint.h](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h_source.html)
- [nxp_gint_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#a07f2264ca2366594a571858cc5ee6b9a)
- [nxp_gint_combination_type](https://docs.zephyrproject.org/latest/doxygen/html/intc__nxp__gint_8h.html#abc9f321deac34cacd128dc16c2db3df6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_nxp_flexio_child_res_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_nxp_rtxxx_dsp_ctrl_api_结构体.md)
