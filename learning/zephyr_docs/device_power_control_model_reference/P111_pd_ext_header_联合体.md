---
id: learning.zephyr-docs.device-power-control-model-reference.page-111
title: pd_ext_header_联合体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionpd__ext__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第111章\_pd\_ext\_header\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionpd__ext__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

构造扩展消息头部（Extended Message Header），见表6-3。

```c
#include <zephyr/drivers/usb_c/usbc_pd.h>
```

<a id="details"></a>

构造扩展消息头部（Extended Message Header），见表6-3。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 111.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a8bbb609ac3462bff9e01ef61571247fc"></a>

```c
uint16_t data_size: 9
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[data_size](#a4a7a948d3463ddfbebf1d75faeda293e)。

数据块的总字节数。

<a id="r_a4c48b53885bfba82d9cddbdf446f0ffb"></a>

```c
uint16_t reserved0: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[reserved0](#aae09d0399c0a121e3c216047e908b9ec)。

保留（Reserved）。

<a id="r_a9906c58cae279168435b5ed5fb5206d9"></a>

```c
uint16_t request_chunk: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[request_chunk](#a36a65a1e52875721758d1273b0e76279)。

分块消息（Chunked message）为 `1`，否则为 `0`。

<a id="r_ac25dd31055f454045b228dee65159dda"></a>

```c
uint16_t chunk_number: 4
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[chunk_number](#aced0489c4e2462652c0d91187c07b27e)。

`chkd = 1` 时表示分块编号（Chunk number），否则为 `0`。

<a id="r_a90a6cb8d30590d935fa482b89fb1c1a1"></a>

```c
uint16_t chunked: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[chunked](#a180ccc6854c1341e638ca338e6eb1cd8)。

分块消息为 `1`。

<a id="r_a69b9d12c8810ae52b389cef6253f912d"></a>

```c
};
```

扩展消息头（Extended Message Header）字段。

<a id="r_a8a1d0f0d38b3a5c4aa3a80586e7a1e8f"></a>

```c
uint16_t raw_value
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[raw_value](#a8a1d0f0d38b3a5c4aa3a80586e7a1e8f)。

原始 PD 扩展头（Ext Header）值。

## 111.2\_详细说明（Detailed Documentation）

<a id="a69b9d12c8810ae52b389cef6253f912d"></a>

### `[struct]`

```c
struct { ... } pd_ext_header
```

扩展消息头（Extended Message Header）字段。

<a id="aced0489c4e2462652c0d91187c07b27e"></a>

### `chunk_number`

```c
uint16_t pd_ext_header::chunk_number
```

`chkd = 1` 时表示分块编号（Chunk number），否则为 `0`。

<a id="a180ccc6854c1341e638ca338e6eb1cd8"></a>

### `chunked`

```c
uint16_t pd_ext_header::chunked
```

分块消息为 `1`。

<a id="a4a7a948d3463ddfbebf1d75faeda293e"></a>

### `data_size`

```c
uint16_t pd_ext_header::data_size
```

数据块的总字节数。

<a id="a8a1d0f0d38b3a5c4aa3a80586e7a1e8f"></a>

### `raw_value`

```c
uint16_t pd_ext_header::raw_value
```

原始 PD 扩展头（Ext Header）值。

<a id="a36a65a1e52875721758d1273b0e76279"></a>

### `request_chunk`

```c
uint16_t pd_ext_header::request_chunk
```

分块消息（Chunked message）为 `1`，否则为 `0`。

<a id="aae09d0399c0a121e3c216047e908b9ec"></a>

### `reserved0`

```c
uint16_t pd_ext_header::reserved0
```

保留（Reserved）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_pd.h`

## 111.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [pd_ext_header](P111_pd_ext_header_联合体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P110_pd_battery_supply_pdo_source_联合体.md) · [返回大纲](大纲.md) · [下一章](P112_pd_fixed_supply_pdo_sink_联合体.md)
