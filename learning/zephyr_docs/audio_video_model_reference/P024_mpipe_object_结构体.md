---
id: learning.zephyr-docs.audio-video-model-reference.page-24
title: mpipe_object_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__object.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_mpipe\_object\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__object.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基础对象结构（Base Object Structure）。

```c
#include <zephyr/mpipe/mpipe_object.h>
```

<a id="details"></a>

基础对象结构体。此结构体定义 mpipe 对象系统中所有对象共有的字段和接口：身份标识、列表成员关系以及属性访问。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 24.1\_数据成员（Data Fields）

<a id="r_a1852f7e5ca10d9bcbe89814ac726d45a"></a>

```c
struct mpipe_object * container
```

相关声明：[mpipe_object](P024_mpipe_object_结构体.md)、[container](#a1852f7e5ca10d9bcbe89814ac726d45a)。

包含此对象的父元素。

<a id="r_a2fa018119018fc26ee08bcb07106359d"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a2fa018119018fc26ee08bcb07106359d)。

分配给对象实例的唯一 ID。

<a id="r_ab1851fbf2942804413fa2c79ee7eeac1"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#ab1851fbf2942804413fa2c79ee7eeac1)。

对象标志，为可继承的位域（bitfield）。

<a id="r_ab4408c02e4b4ecc7112c0b2eaec7dd57"></a>

```c
sys_dnode_t node
```

相关声明：[sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)、[node](#ab4408c02e4b4ecc7112c0b2eaec7dd57)。

用于链表的对象节点。

<a id="r_a66b6578b9add34458937f79161ea142b"></a>

```c
int(* set_property )(struct mpipe_object *self, uint32_t key, const void *val)
```

相关声明：[set_property](#a66b6578b9add34458937f79161ea142b)、[mpipe_object](P024_mpipe_object_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

设置一个属性。

<a id="r_a4e0e90f289099c66d3d8949d7dc071c5"></a>

```c
int(* get_property )(struct mpipe_object *self, uint32_t key, void *val)
```

相关声明：[get_property](#a4e0e90f289099c66d3d8949d7dc071c5)、[mpipe_object](P024_mpipe_object_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

读取一个属性。

## 24.2\_详细说明（Detailed Documentation）

<a id="a1852f7e5ca10d9bcbe89814ac726d45a"></a>

### `container`

```c
struct mpipe_object* mpipe_object::container
```

包含此对象的父元素。

<a id="ab1851fbf2942804413fa2c79ee7eeac1"></a>

### `flags`

```c
uint32_t mpipe_object::flags
```

对象标志，为可继承的位域（bitfield）。

<a id="a4e0e90f289099c66d3d8949d7dc071c5"></a>

### `get_property`

```c
int(* mpipe_object::get_property) (struct mpipe_object *self, uint32_t key, void *val)
```

读取一个属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` self` | 指向对象的指针。 |
| ` key` | 属性标识符，取自该元素的属性枚举。 |
| `[out] val` | 用于写入属性值的存储空间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOTSUP` | 对象没有此属性。 |

<a id="a2fa018119018fc26ee08bcb07106359d"></a>

### `id`

```c
uint8_t mpipe_object::id
```

分配给对象实例的唯一 ID。

最大值 `UINT8_MAX` 为保留值，不应使用。

<a id="ab4408c02e4b4ecc7112c0b2eaec7dd57"></a>

### `node`

```c
sys_dnode_t mpipe_object::node
```

用于链表的对象节点。

<a id="a66b6578b9add34458937f79161ea142b"></a>

### `set_property`

```c
int(* mpipe_object::set_property) (struct mpipe_object *self, uint32_t key, const void *val)
```

设置一个属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `self` | 指向对象的指针。 |
| `key` | 属性标识符，取自该元素的属性枚举。 |
| `val` | 要设置的值，仅在调用期间读取。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOTSUP` | 对象没有此属性。 |

**返回（Returns）**：返回值：如果对象拒绝该值，则返回相应的负值 `errno`。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_object.h`

## 24.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_object.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h_source.html)
- [mpipe_object](P024_mpipe_object_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P023_mpipe_message_结构体.md) · [返回大纲](大纲.md) · [下一章](P025_mpipe_pad_结构体.md)
