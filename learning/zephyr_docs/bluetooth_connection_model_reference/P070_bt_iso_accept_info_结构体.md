---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-70
title: bt_iso_accept_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__accept__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_bt\_iso\_accept\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__accept__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时通信（ISO）接入信息结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时通信（ISO）接入信息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 70.1\_数据成员（Data Fields）

<a id="r_a4225ccc90f1e17e26ce61fe398f506d1"></a>

```c
struct bt_conn * acl
```

相关声明：[bt_conn](P002_bt_conn_结构体.md)、[acl](#a4225ccc90f1e17e26ce61fe398f506d1)。

请求授权（Authorization）的异步面向连接链路连接（ACL connection）。

<a id="r_a88002043a67c89c8d518ebdf92cf8847"></a>

```c
uint8_t cig_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cig_id](#a88002043a67c89c8d518ebdf92cf8847)。

中心设备上的连接等时组标识符（Connected Isochronous Group，CIG ID）。

<a id="r_a688809132997c37a6fe2529498a4ee0e"></a>

```c
uint8_t cis_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cis_id](#a688809132997c37a6fe2529498a4ee0e)。

中心设备上的连接等时流标识符（Connected Isochronous Stream，CIS ID）。

## 70.2\_详细说明（Detailed Documentation）

<a id="a4225ccc90f1e17e26ce61fe398f506d1"></a>

### `acl`

```c
struct bt_conn* bt_iso_accept_info::acl
```

请求授权（Authorization）的异步面向连接链路连接（ACL connection）。

<a id="a88002043a67c89c8d518ebdf92cf8847"></a>

### `cig_id`

```c
uint8_t bt_iso_accept_info::cig_id
```

中心设备上的连接等时组标识符（Connected Isochronous Group，CIG ID）。

此标识符（ID）在每条异步面向连接链路（ACL）内唯一。

<a id="a688809132997c37a6fe2529498a4ee0e"></a>

### `cis_id`

```c
uint8_t bt_iso_accept_info::cis_id
```

中心设备上的连接等时流标识符（Connected Isochronous Stream，CIS ID）。

此标识符（ID）在一个连接等时组（CIG）内唯一。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 70.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [bt_conn](P002_bt_conn_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P069_bt_gatt_write_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P071_bt_iso_big_结构体.md)
