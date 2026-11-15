---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-3
title: bt_a2dp_codec_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__codec__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_bt\_a2dp\_codec\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__a2dp__codec__cfg.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

端点配置（Endpoint Configuration）。

```c
#include <zephyr/bluetooth/classic/a2dp.h>
```

<a id="details"></a>

端点配置（Endpoint Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_ab630148c92c8f7127694e2066cdf4ac8"></a>

```c
bool delay_report
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[delay_report](#ab630148c92c8f7127694e2066cdf4ac8)。

延迟报告（Delay Reporting）的配置状态。

<a id="r_a178eb806a01729d940e6e8c34b0fb513"></a>

```c
struct bt_a2dp_codec_ie * codec_config
```

相关声明：[bt_a2dp_codec_ie](P004_bt_a2dp_codec_ie_结构体.md)、[codec_config](#a178eb806a01729d940e6e8c34b0fb513)。

媒体编解码器配置内容。

## 3.2\_详细说明（Detailed Documentation）

<a id="a178eb806a01729d940e6e8c34b0fb513"></a>

### `codec_config`

```c
struct bt_a2dp_codec_ie* bt_a2dp_codec_cfg::codec_config
```

媒体编解码器配置内容。

<a id="ab630148c92c8f7127694e2066cdf4ac8"></a>

### `delay_report`

```c
bool bt_a2dp_codec_cfg::delay_report
```

延迟报告（Delay Reporting）的配置状态。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/a2dp.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/a2dp.h](https://docs.zephyrproject.org/latest/doxygen/html/a2dp_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_a2dp_codec_ie](P004_bt_a2dp_codec_ie_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_bt_a2dp_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_bt_a2dp_codec_ie_结构体.md)
