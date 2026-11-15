---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-18
title: bt_mesh_brg_cfg_filter_netkey_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__filter__netkey.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_bt\_mesh\_brg\_cfg\_filter\_netkey\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__brg__cfg__filter__netkey.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于筛选桥接表（Bridging Table）中的网络密钥索引（NetKey Index）对集合。

```c
#include <zephyr/bluetooth/mesh/brg_cfg.h>
```

<a id="details"></a>

用于筛选桥接表（Bridging Table）中的网络密钥索引（NetKey Index）对集合。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_ab224e4982b355cc99e246b2b7c398fee"></a>

```c
uint16_t filter: 2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[filter](#ab224e4982b355cc99e246b2b7c398fee)。

<a id="r_a41778bb5014eda9ee6e6fc4c83e339cb"></a>

```c
uint16_t prohibited: 2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[prohibited](#a41778bb5014eda9ee6e6fc4c83e339cb)。

<a id="r_abe9462af4258301317fe95757982e46a"></a>

```c
uint16_t net_idx: 12
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx](#abe9462af4258301317fe95757982e46a)。

## 18.2\_详细说明（Detailed Documentation）

<a id="ab224e4982b355cc99e246b2b7c398fee"></a>

### `filter`

```c
uint16_t bt_mesh_brg_cfg_filter_netkey::filter
```

<a id="abe9462af4258301317fe95757982e46a"></a>

### `net_idx`

```c
uint16_t bt_mesh_brg_cfg_filter_netkey::net_idx
```

<a id="a41778bb5014eda9ee6e6fc4c83e339cb"></a>

### `prohibited`

```c
uint16_t bt_mesh_brg_cfg_filter_netkey::prohibited
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/brg_cfg.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/brg_cfg.h](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_bt_mesh_brg_cfg_cli_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_bt_mesh_brg_cfg_subnets_list_结构体.md)
