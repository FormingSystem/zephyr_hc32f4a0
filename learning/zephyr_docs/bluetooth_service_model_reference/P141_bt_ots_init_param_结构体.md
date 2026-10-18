---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-141
title: bt_ots_init_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__init__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第141章\_bt\_ots\_init\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__init__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象传输服务（OTS）初始化的描述符。

```c
#include <zephyr/bluetooth/services/ots.h>
```

<a id="details"></a>

对象传输服务（OTS）初始化的描述符。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 141.1\_数据成员（Data Fields）

<a id="r_a563c25963aa84726630252eb5aca7cc6"></a>

```c
struct bt_ots_feat features
```

相关声明：[bt_ots_feat](P140_bt_ots_feat_结构体.md)、[features](#a563c25963aa84726630252eb5aca7cc6)。

<a id="r_a22887673f03decf840470cb555f2b7f0"></a>

```c
struct bt_ots_cb * cb
```

相关声明：[bt_ots_cb](P136_bt_ots_cb_结构体.md)、[cb](#a22887673f03decf840470cb555f2b7f0)。

## 141.2\_详细说明（Detailed Documentation）

<a id="a22887673f03decf840470cb555f2b7f0"></a>

### `cb`

```c
struct bt_ots_cb* bt_ots_init_param::cb
```

<a id="a563c25963aa84726630252eb5aca7cc6"></a>

### `features`

```c
struct bt_ots_feat bt_ots_init_param::features
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ots.h`

## 141.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ots.h](https://docs.zephyrproject.org/latest/doxygen/html/ots_8h_source.html)
- [bt_ots_feat](P140_bt_ots_feat_结构体.md)
- [bt_ots_cb](P136_bt_ots_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P140_bt_ots_feat_结构体.md) · [返回大纲](大纲.md) · [下一章](P142_bt_ots_obj_add_param_结构体.md)
