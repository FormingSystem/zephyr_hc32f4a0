---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-39
title: bt_bap_unicast_group_stream_pair_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__stream__pair__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_bt\_bap\_unicast\_group\_stream\_pair\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bap__unicast__group__stream__pair__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

单播组函数使用的参数结构体。

```c
#include <zephyr/bluetooth/audio/bap.h>
```

<a id="details"></a>

单播组函数使用的参数结构体，供 `bt_bap_unicast_group_create()` 和 `bt_bap_unicast_group_add_streams()` 使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d"></a>

```c
struct bt_bap_unicast_group_stream_param * rx_param
```

相关声明：[bt_bap_unicast_group_stream_param](P040_bt_bap_unicast_group_stream_param_结构体.md)、[rx_param](#ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d)。

指向接收流参数的指针。

<a id="r_ae73a11aab16a60806d1a941306c1822a"></a>

```c
struct bt_bap_unicast_group_stream_param * tx_param
```

相关声明：[bt_bap_unicast_group_stream_param](P040_bt_bap_unicast_group_stream_param_结构体.md)、[tx_param](#ae73a11aab16a60806d1a941306c1822a)。

指向发送流参数的指针。

## 39.2\_详细说明（Detailed Documentation）

<a id="ad2f1f8fb4ab3fd2cb4dca8ed08de5b8d"></a>

### `rx_param`

```c
struct bt_bap_unicast_group_stream_param* bt_bap_unicast_group_stream_pair_param::rx_param
```

指向接收流参数的指针。

<a id="ae73a11aab16a60806d1a941306c1822a"></a>

### `tx_param`

```c
struct bt_bap_unicast_group_stream_param* bt_bap_unicast_group_stream_pair_param::tx_param
```

指向发送流参数的指针。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/bap.h`

## 39.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/bap.h](https://docs.zephyrproject.org/latest/doxygen/html/bap_8h_source.html)
- [bt_bap_unicast_group_stream_param](P040_bt_bap_unicast_group_stream_param_结构体.md)
- [bt_bap_unicast_group_create()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#gaafd53b5f45d998b44e94a1b58e93ba21)
- [bt_bap_unicast_group_add_streams()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__unicast__client.html#ga9cc792cd1eaaa79d56f3df0e2341cbf6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_bt_bap_unicast_group_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_bt_bap_unicast_group_stream_param_结构体.md)
