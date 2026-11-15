---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-2
title: bt_hci_cis_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_bt\_hci\_cis\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cis.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_a84165d526c10a91fa42d306276d97c74"></a>

```c
uint16_t cis_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cis_handle](#a84165d526c10a91fa42d306276d97c74)。

<a id="r_a754c3c75c0ad13a11d89fa3347112e2c"></a>

```c
uint16_t acl_handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[acl_handle](#a754c3c75c0ad13a11d89fa3347112e2c)。

## 2.2\_详细说明（Detailed Documentation）

<a id="a754c3c75c0ad13a11d89fa3347112e2c"></a>

### `acl_handle`

```c
uint16_t bt_hci_cis::acl_handle
```

<a id="a84165d526c10a91fa42d306276d97c74"></a>

### `cis_handle`

```c
uint16_t bt_hci_cis::cis_handle
```

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_bt_hci_acl_hdr_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_bt_hci_cis_params_结构体.md)
