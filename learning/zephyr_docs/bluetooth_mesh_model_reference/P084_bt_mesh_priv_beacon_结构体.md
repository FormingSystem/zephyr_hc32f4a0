---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-84
title: bt_mesh_priv_beacon_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__priv__beacon.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第84章\_bt\_mesh\_priv\_beacon\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__priv__beacon.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

私有信标（Private Beacon）。

```c
#include <zephyr/bluetooth/mesh/priv_beacon_cli.h>
```

<a id="details"></a>

私有信标（Private Beacon）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 84.1\_数据成员（Data Fields）

<a id="r_ac38424ed4ebcd69307568763ff2d6ffb"></a>

```c
uint8_t enabled
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[enabled](#ac38424ed4ebcd69307568763ff2d6ffb)。

私有信标（Private beacon）已启用。

<a id="r_a1a4972527afde6f9aa5c7726d85ddd45"></a>

```c
uint8_t rand_interval
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rand_interval](#a1a4972527afde6f9aa5c7726d85ddd45)。

随机值刷新间隔（Random refresh interval），以 10 秒为步长；设为 `0` 时保留当前值。

## 84.2\_详细说明（Detailed Documentation）

<a id="ac38424ed4ebcd69307568763ff2d6ffb"></a>

### `enabled`

```c
uint8_t bt_mesh_priv_beacon::enabled
```

私有信标（Private beacon）已启用。

<a id="a1a4972527afde6f9aa5c7726d85ddd45"></a>

### `rand_interval`

```c
uint8_t bt_mesh_priv_beacon::rand_interval
```

随机值刷新间隔（Random refresh interval），以 10 秒为步长；设为 `0` 时保留当前值。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/priv_beacon_cli.h`

## 84.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/priv_beacon_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/priv__beacon__cli_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P083_bt_mesh_od_priv_proxy_cli_结构体.md) · [返回大纲](大纲.md) · [下一章](P085_bt_mesh_priv_beacon_cli_结构体.md)
