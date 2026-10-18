---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-13
title: bt_mesh_blob_target_pull_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__target__pull.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_bt\_mesh\_blob\_target\_pull\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__target__pull.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

向目标节点发送分片时使用的目标节点拉取模式（Pull BLOB Transfer Mode）上下文。

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

<a id="details"></a>

向目标节点发送分片时使用的目标节点拉取模式（Pull BLOB Transfer Mode）上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_a9234ee3246890285b5cd30c32866b718"></a>

```c
int64_t block_report_timestamp
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[block_report_timestamp](#a9234ee3246890285b5cd30c32866b718)。

此目标节点的块报告超时定时器（Block Report Timeout Timer）到期的时间戳。

<a id="r_a4c43698926ba22eb43e4f92bb874ca46"></a>

```c
uint8_t missing [(((CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX)+(8) - 1)/(8))]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[missing](#a4c43698926ba22eb43e4f92bb874ca46)、[CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga4e1ea17e8a8ffd42f62d64286ddc576e)。

此目标节点报告的缺失分片（Missing chunks）。

## 13.2\_详细说明（Detailed Documentation）

<a id="a9234ee3246890285b5cd30c32866b718"></a>

### `block_report_timestamp`

```c
int64_t bt_mesh_blob_target_pull::block_report_timestamp
```

此目标节点的块报告超时定时器（Block Report Timeout Timer）到期的时间戳。

<a id="a4c43698926ba22eb43e4f92bb874ca46"></a>

### `missing`

```c
uint8_t bt_mesh_blob_target_pull::missing[(((CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX)+(8) - 1)/(8))]
```

此目标节点报告的缺失分片（Missing chunks）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob_cli.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h_source.html)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga4e1ea17e8a8ffd42f62d64286ddc576e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_bt_mesh_blob_target_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_bt_mesh_blob_xfer_结构体.md)
