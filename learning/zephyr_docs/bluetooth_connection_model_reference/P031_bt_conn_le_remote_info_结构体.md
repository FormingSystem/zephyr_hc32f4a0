---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-31
title: bt_conn_le_remote_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__remote__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_bt\_conn\_le\_remote\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__remote__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LE 连接的远端信息结构体。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

LE 连接的远端信息结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_a4ff434f6c501dc60db5c4b776be46b3b"></a>

```c
const uint8_t * features
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[features](#a4ff434f6c501dc60db5c4b776be46b3b)。

远端低功耗特性集合（Remote LE feature set），以位掩码表示。

## 31.2\_详细说明（Detailed Documentation）

<a id="a4ff434f6c501dc60db5c4b776be46b3b"></a>

### `features`

```c
const uint8_t* bt_conn_le_remote_info::features
```

远端低功耗特性集合（Remote LE feature set），以位掩码表示。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_bt_conn_le_read_all_remote_feat_complete_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_bt_conn_le_subrate_changed_结构体.md)
