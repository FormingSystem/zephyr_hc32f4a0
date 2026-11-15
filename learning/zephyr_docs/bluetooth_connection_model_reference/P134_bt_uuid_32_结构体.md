---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-134
title: bt_uuid_32_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__uuid__32.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第134章\_bt\_uuid\_32\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__uuid__32.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/uuid.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 134.1\_数据成员（Data Fields）

<a id="r_ae37fff06890b200895d559ef42d454e2"></a>

```c
struct bt_uuid uuid
```

相关声明：[bt_uuid](P131_bt_uuid_结构体.md)、[uuid](#ae37fff06890b200895d559ef42d454e2)。

通用唯一标识符的通用类型（UUID generic type）。

<a id="r_a56e991966643c9a1ca689986e57e6bfc"></a>

```c
uint32_t val
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[val](#a56e991966643c9a1ca689986e57e6bfc)。

32 位通用唯一标识符值（UUID value），采用主机字节序（Host endianness）。

## 134.2\_详细说明（Detailed Documentation）

<a id="ae37fff06890b200895d559ef42d454e2"></a>

### `uuid`

```c
struct bt_uuid bt_uuid_32::uuid
```

通用唯一标识符的通用类型（UUID generic type）。

<a id="a56e991966643c9a1ca689986e57e6bfc"></a>

### `val`

```c
uint32_t bt_uuid_32::val
```

32 位通用唯一标识符值（UUID value），采用主机字节序（Host endianness）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/uuid.h`

## 134.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h_source.html)
- [bt_uuid](P131_bt_uuid_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P133_bt_uuid_16_结构体.md) · [返回大纲](大纲.md) · [下一章](P135_bt_uuid_any_结构体.md)
