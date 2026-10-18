---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-133
title: bt_uuid_16_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__uuid__16.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第133章\_bt\_uuid\_16\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__uuid__16.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/uuid.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 133.1\_数据成员（Data Fields）

<a id="r_a08f8a5e0eadf1ef2c4c917a5dd3db191"></a>

```c
struct bt_uuid uuid
```

相关声明：[bt_uuid](P131_bt_uuid_结构体.md)、[uuid](#a08f8a5e0eadf1ef2c4c917a5dd3db191)。

通用唯一标识符的通用类型（UUID generic type）。

<a id="r_a13ee02ec58cf5fdede249aa8b20a1a9a"></a>

```c
uint16_t val
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[val](#a13ee02ec58cf5fdede249aa8b20a1a9a)。

16 位通用唯一标识符值（UUID value），采用主机字节序（Host endianness）。

## 133.2\_详细说明（Detailed Documentation）

<a id="a08f8a5e0eadf1ef2c4c917a5dd3db191"></a>

### `uuid`

```c
struct bt_uuid bt_uuid_16::uuid
```

通用唯一标识符的通用类型（UUID generic type）。

<a id="a13ee02ec58cf5fdede249aa8b20a1a9a"></a>

### `val`

```c
uint16_t bt_uuid_16::val
```

16 位通用唯一标识符值（UUID value），采用主机字节序（Host endianness）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/uuid.h`

## 133.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h_source.html)
- [bt_uuid](P131_bt_uuid_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P132_bt_uuid_128_结构体.md) · [返回大纲](大纲.md) · [下一章](P134_bt_uuid_32_结构体.md)
