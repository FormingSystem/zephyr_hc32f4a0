---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-149
title: bt_pbap_pce_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__pbap__pce.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第149章\_bt\_pbap\_pce\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__pbap__pce.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电话簿访问配置文件（PBAP）的电话簿客户端设备（PCE）结构。

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

<a id="details"></a>

电话簿访问配置文件（PBAP）的电话簿客户端设备（PCE）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 149.1\_数据成员（Data Fields）

<a id="r_aa1b9c9c733cf5e7277697a2e6119204b"></a>

```c
struct bt_pbap_pce_cb * cb
```

相关声明：[bt_pbap_pce_cb](P150_bt_pbap_pce_cb_结构体.md)、[cb](#aa1b9c9c733cf5e7277697a2e6119204b)。

回调操作（Callback operations）结构体。

## 149.2\_详细说明（Detailed Documentation）

<a id="aa1b9c9c733cf5e7277697a2e6119204b"></a>

### `cb`

```c
struct bt_pbap_pce_cb* bt_pbap_pce::cb
```

回调操作（Callback operations）结构体。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/pbap.h`

## 149.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/pbap.h](https://docs.zephyrproject.org/latest/doxygen/html/pbap_8h_source.html)
- [bt_pbap_pce_cb](P150_bt_pbap_pce_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P148_bt_pacs_register_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P150_bt_pbap_pce_cb_结构体.md)
