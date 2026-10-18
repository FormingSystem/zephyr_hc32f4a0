---
id: learning.zephyr-docs.device-power-control-model-reference.page-74
title: renesas_ra_ctsu_touch_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrenesas__ra__ctsu__touch__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_renesas\_ra\_ctsu\_touch\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrenesas__ra__ctsu__touch__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RA电容触摸感应单元（CTSU）设备的配置数据。

```c
#include <zephyr/input/input_renesas_ra_ctsu.h>
```

<a id="details"></a>

Renesas RA电容触摸感应单元（CTSU）设备的配置数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 74.1\_数据成员（Data Fields）

<a id="r_ac1af746e7b95089bf351a2c74f2334e2"></a>

```c
struct st_touch_instance touch_instance
```

相关声明：[touch_instance](#ac1af746e7b95089bf351a2c74f2334e2)。

FSP 触摸（Touch）实例。

## 74.2\_详细说明（Detailed Documentation）

<a id="ac1af746e7b95089bf351a2c74f2334e2"></a>

### `touch_instance`

```c
struct st_touch_instance renesas_ra_ctsu_touch_cfg::touch_instance
```

FSP 触摸（Touch）实例。

本数据类型文档由以下文件生成：

- `zephyr/input/input_renesas_ra_ctsu.h`

## 74.3\_原页交叉引用（Cross References）

- [zephyr/input/input_renesas_ra_ctsu.h](https://docs.zephyrproject.org/latest/doxygen/html/input__renesas__ra__ctsu_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P073_renesas_elc_dt_spec_结构体.md) · [返回大纲](大纲.md) · [下一章](P075_renesas_rx_ctsu_touch_cfg_结构体.md)
