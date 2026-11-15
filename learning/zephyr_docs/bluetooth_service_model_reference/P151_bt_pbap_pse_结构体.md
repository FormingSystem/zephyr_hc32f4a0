---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-151
title: bt_pbap_pse_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__pbap__pse.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第151章\_bt\_pbap\_pse\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__pbap__pse.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电话簿访问配置文件（PBAP）的电话簿服务器设备（PSE）结构。

```c
#include <zephyr/bluetooth/classic/pbap.h>
```

<a id="details"></a>

电话簿访问配置文件（PBAP）的电话簿服务器设备（PSE）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 151.1\_数据成员（Data Fields）

<a id="r_a05196786dfb6f2d4e2a3e6add38bc3d1"></a>

```c
struct bt_pbap_pse_cb * cb
```

相关声明：[bt_pbap_pse_cb](P152_bt_pbap_pse_cb_结构体.md)、[cb](#a05196786dfb6f2d4e2a3e6add38bc3d1)。

回调操作（Callback operations）结构体。

## 151.2\_详细说明（Detailed Documentation）

<a id="a05196786dfb6f2d4e2a3e6add38bc3d1"></a>

### `cb`

```c
struct bt_pbap_pse_cb* bt_pbap_pse::cb
```

回调操作（Callback operations）结构体。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/pbap.h`

## 151.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/pbap.h](https://docs.zephyrproject.org/latest/doxygen/html/pbap_8h_source.html)
- [bt_pbap_pse_cb](P152_bt_pbap_pse_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P150_bt_pbap_pce_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P152_bt_pbap_pse_cb_结构体.md)
