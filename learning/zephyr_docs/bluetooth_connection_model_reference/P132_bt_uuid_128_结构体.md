---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-132
title: bt_uuid_128_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__uuid__128.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第132章\_bt\_uuid\_128\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__uuid__128.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/uuid.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 132.1\_数据成员（Data Fields）

<a id="r_a3b8fd8a362ed8fd9eabcfa5bffa9eeee"></a>

```c
struct bt_uuid uuid
```

相关声明：[bt_uuid](P131_bt_uuid_结构体.md)、[uuid](#a3b8fd8a362ed8fd9eabcfa5bffa9eeee)。

通用唯一标识符的通用类型（UUID generic type）。

<a id="r_a0918addaa7afaf1eeb864d5ec40bd59a"></a>

```c
uint8_t val [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[val](#a0918addaa7afaf1eeb864d5ec40bd59a)。

128 位通用唯一标识符值（UUID value），采用小端格式（Little-endian）。

## 132.2\_详细说明（Detailed Documentation）

<a id="a3b8fd8a362ed8fd9eabcfa5bffa9eeee"></a>

### `uuid`

```c
struct bt_uuid bt_uuid_128::uuid
```

通用唯一标识符的通用类型（UUID generic type）。

<a id="a0918addaa7afaf1eeb864d5ec40bd59a"></a>

### `val`

```c
uint8_t bt_uuid_128::val[16]
```

128 位通用唯一标识符值（UUID value），采用小端格式（Little-endian）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/uuid.h`

## 132.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/uuid.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2uuid_8h_source.html)
- [bt_uuid](P131_bt_uuid_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P131_bt_uuid_结构体.md) · [返回大纲](大纲.md) · [下一章](P133_bt_uuid_16_结构体.md)
