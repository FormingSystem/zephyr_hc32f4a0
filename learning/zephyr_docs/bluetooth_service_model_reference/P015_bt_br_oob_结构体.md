---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-15
title: bt_br_oob_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__oob.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_bt\_br\_oob\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__br__oob.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/classic/classic.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_a9b9f4c830a4e48736ac6b793d628ee98"></a>

```c
bt_addr_t addr
```

相关声明：[bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)、[addr](#a9b9f4c830a4e48736ac6b793d628ee98)。

基本速率／增强数据率地址（BR/EDR address）。

## 15.2\_详细说明（Detailed Documentation）

<a id="a9b9f4c830a4e48736ac6b793d628ee98"></a>

### `addr`

```c
bt_addr_t bt_br_oob::addr
```

基本速率／增强数据率地址（BR/EDR address）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/classic.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/classic.h](https://docs.zephyrproject.org/latest/doxygen/html/classic_8h_source.html)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_bt_br_inquiry_scan_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_bt_br_page_scan_param_结构体.md)
