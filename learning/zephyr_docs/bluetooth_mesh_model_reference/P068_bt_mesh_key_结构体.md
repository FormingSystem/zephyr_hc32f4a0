---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-68
title: bt_mesh_key_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__key.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_bt\_mesh\_key\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__key.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存密钥表示（Key Representation）的结构。

```c
#include <zephyr/bluetooth/mesh/keys.h>
```

<a id="details"></a>

保存密钥表示（Key Representation）的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_a50acd9d36423b22aab033795b9d29d78"></a>

```c
psa_key_id_t key
```

相关声明：[psa_key_id_t](https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h.html#a11e986351c65bd3dc3c0fe2cd9926e4b)、[key](#a50acd9d36423b22aab033795b9d29d78)。

PSA 密钥以 PSA 密钥标识符（PSA key identifier）表示。

## 68.2\_详细说明（Detailed Documentation）

<a id="a50acd9d36423b22aab033795b9d29d78"></a>

### `key`

```c
psa_key_id_t bt_mesh_key::key
```

PSA 密钥以 PSA 密钥标识符（PSA key identifier）表示。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/keys.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/keys.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2mesh_2keys_8h_source.html)
- [psa_key_id_t](https://docs.zephyrproject.org/latest/doxygen/html/key__ids_8h.html#a11e986351c65bd3dc3c0fe2cd9926e4b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_bt_mesh_health_srv_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_bt_mesh_large_comp_data_cli_结构体.md)
