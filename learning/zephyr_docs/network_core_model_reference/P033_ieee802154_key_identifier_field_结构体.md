---
id: learning.zephyr-docs.network-core-model-reference.page-33
title: ieee802154_key_identifier_field_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__key__identifier__field.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_ieee802154\_key\_identifier\_field\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__key__identifier__field.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

辅助安全头（Auxiliary Security Header）的密钥标识符字段。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

辅助安全头（Auxiliary Security Header）的密钥标识符字段（Key Identifier Field）。格式取决于密钥标识符模式，见第9.4.4节。说明（Note）：当前仅支持模式0，因此此结构尚不保存信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

```c
union {
```

```c
struct {
```

<a id="r_ac8169a9abdac538db01abd91f35085d4"></a>

```c
uint8_t key_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_index](#a115e0904934594d97835794d557c67c8)。

密钥索引（Key Index）。

<a id="r_ad52e160575cd332466de027602994c7d"></a>

```c
} mode_1
```

相关声明：[mode_1](#a90c06bb718d4c41172d1a3bb593ecdea)。

密钥标识符模式1（Key Identifier Mode 1）：仅包含密钥索引（Key Index）。

```c
struct {
```

<a id="r_a903abd80e2ed2d511d23e262526b1707"></a>

```c
uint8_t key_src [4]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_src](#af3253a67435557031b548e44a6b32710)。

密钥源（Key Source），长度为4个八位组。

<a id="r_a7ad4f0880d3255331fb32461bd3774ab"></a>

```c
uint8_t key_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_index](#a115e0904934594d97835794d557c67c8)。

密钥索引（Key Index）。

<a id="r_ad964086be43bfecdd485fdb05148cc3c"></a>

```c
} mode_2
```

相关声明：[mode_2](#a62bd54d089679ad1fa3507aa51703a11)。

密钥标识符模式2（Key Identifier Mode 2）：包含4个八位组的密钥源（Key Source）及密钥索引（Key Index）。

```c
struct {
```

<a id="r_a0f5376f34ecc0bbe5e7cd5f0aa272f58"></a>

```c
uint8_t key_src [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_src](#af3253a67435557031b548e44a6b32710)。

密钥源（Key Source），长度为8个八位组。

<a id="r_a79a370b05c29334daf72522cfded0b6c"></a>

```c
uint8_t key_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[key_index](#a115e0904934594d97835794d557c67c8)。

密钥索引（Key Index）。

<a id="r_a85abc4296cdb03edd5e3f79a34455e84"></a>

```c
} mode_3
```

相关声明：[mode_3](#a8808e859495b57da67517a43f0220f93)。

密钥标识符模式3（Key Identifier Mode 3）：包含8个八位组的密钥源（Key Source）及密钥索引（Key Index）。

<a id="r_a3ed39ede8ab6b612546d1dca20aca89f"></a>

```c
};
```

模式1至3的密钥标识符字段布局（Key Identifier Field Layout）。

## 33.2\_详细说明（Detailed Documentation）

<a id="a3ed39ede8ab6b612546d1dca20aca89f"></a>

### `[union]`

```c
union { ... } ieee802154_key_identifier_field
```

模式1至3的密钥标识符字段布局（Key Identifier Field Layout）。

见第9.4.4节。

<a id="a115e0904934594d97835794d557c67c8"></a>

### `key_index`

```c
uint8_t ieee802154_key_identifier_field::key_index
```

密钥索引（Key Index）。

<a id="af3253a67435557031b548e44a6b32710"></a>

### `key_src`

```c
uint8_t ieee802154_key_identifier_field::key_src[8]
```

密钥源（Key Source），长度为4个八位组。

密钥源（Key Source），长度为8个八位组。

<a id="a90c06bb718d4c41172d1a3bb593ecdea"></a>

### `[struct]`

```c
struct { ... } ieee802154_key_identifier_field::mode_1
```

密钥标识符模式1（Key Identifier Mode 1）：仅包含密钥索引（Key Index）。

<a id="a62bd54d089679ad1fa3507aa51703a11"></a>

### `[struct]`

```c
struct { ... } ieee802154_key_identifier_field::mode_2
```

密钥标识符模式2（Key Identifier Mode 2）：包含4个八位组的密钥源（Key Source）及密钥索引（Key Index）。

<a id="a8808e859495b57da67517a43f0220f93"></a>

### `[struct]`

```c
struct { ... } ieee802154_key_identifier_field::mode_3
```

密钥标识符模式3（Key Identifier Mode 3）：包含8个八位组的密钥源（Key Source）及密钥索引（Key Index）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ieee802154_key_identifier_field](P033_ieee802154_key_identifier_field_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_ieee802154_key_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_ieee802154_mhr_结构体.md)
