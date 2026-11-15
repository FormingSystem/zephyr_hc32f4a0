---
id: learning.zephyr-docs.device-power-control-model-reference.page-75
title: renesas_rx_ctsu_touch_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrenesas__rx__ctsu__touch__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第75章\_renesas\_rx\_ctsu\_touch\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrenesas__rx__ctsu__touch__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RX电容触摸感应单元（CTSU）设备的配置数据。

```c
#include <zephyr/input/input_renesas_rx_ctsu.h>
```

<a id="details"></a>

Renesas RX电容触摸感应单元（CTSU）设备的配置数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 75.1\_数据成员（Data Fields）

<a id="r_aab1ae31d5380ba801401aa5f9e4a7ae0"></a>

```c
struct st_touch_instance touch_instance
```

相关声明：[touch_instance](#aab1ae31d5380ba801401aa5f9e4a7ae0)。

FSP 触摸（Touch）实例。

## 75.2\_详细说明（Detailed Documentation）

<a id="aab1ae31d5380ba801401aa5f9e4a7ae0"></a>

### `touch_instance`

```c
struct st_touch_instance renesas_rx_ctsu_touch_cfg::touch_instance
```

FSP 触摸（Touch）实例。

本数据类型文档由以下文件生成：

- `zephyr/input/input_renesas_rx_ctsu.h`

## 75.3\_原页交叉引用（Cross References）

- [zephyr/input/input_renesas_rx_ctsu.h](https://docs.zephyrproject.org/latest/doxygen/html/input__renesas__rx__ctsu_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P074_renesas_ra_ctsu_touch_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P076_rts5912_sccon_subsys_结构体.md)
