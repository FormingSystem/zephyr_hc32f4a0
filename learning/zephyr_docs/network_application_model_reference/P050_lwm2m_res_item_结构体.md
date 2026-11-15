---
id: learning.zephyr-docs.network-application-model-reference.page-50
title: lwm2m_res_item_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__res__item.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_lwm2m\_res\_item\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__res__item.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

轻量级M2M（LwM2M）的资源项结构。

```c
#include <zephyr/net/lwm2m.h>
```

<a id="details"></a>

LwM2M资源项（Resource Item）结构。值类型必须与目标资源匹配，因为不执行类型转换，只进行内存复制。资源类型使用以下C类型：BOOL和U8使用uint8_t；S8使用int8_t；U16使用uint16_t；S16使用int16_t；U32使用uint32_t；S32使用int32_t；S64使用int64_t；TIME使用time_t；FLOAT使用double；OBJLNK使用struct lwm2m_objlnk；STRING使用char *，且大小必须包含空终止符（Null Terminator）；OPAQUE为任意二进制数据。向OPAQUE资源写入以空字符终止的字符串时，大小不应包含终止符。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 50.1\_数据成员（Data Fields）

<a id="r_ab1aecc059a1f88d84b37131884afbf2f"></a>

```c
struct lwm2m_obj_path * path
```

相关声明：[lwm2m_obj_path](P048_lwm2m_obj_path_结构体.md)、[path](#ab1aecc059a1f88d84b37131884afbf2f)。

指向结构体形式LwM2M路径（Path）的指针。

<a id="r_a7edf4cf404d4fae3ba0193fde76a66ff"></a>

```c
void * value
```

相关声明：[value](#a7edf4cf404d4fae3ba0193fde76a66ff)。

指向资源值（Resource Value）的指针。

<a id="r_a7693d039248f61eaed193b131a7f6d5a"></a>

```c
uint16_t size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[size](#a7693d039248f61eaed193b131a7f6d5a)。

值的大小（Value Size）。

## 50.2\_详细说明（Detailed Documentation）

<a id="ab1aecc059a1f88d84b37131884afbf2f"></a>

### `path`

```c
struct lwm2m_obj_path* lwm2m_res_item::path
```

指向结构体形式LwM2M路径（Path）的指针。

<a id="a7693d039248f61eaed193b131a7f6d5a"></a>

### `size`

```c
uint16_t lwm2m_res_item::size
```

值的大小（Value Size）。

对于字符串资源（String Resources），应包含空终止符（Null Terminator）。

<a id="a7edf4cf404d4fae3ba0193fde76a66ff"></a>

### `value`

```c
void* lwm2m_res_item::value
```

指向资源值（Resource Value）的指针。

本数据类型文档由以下文件生成：

- `zephyr/net/lwm2m.h`

## 50.3\_原页交叉引用（Cross References）

- [zephyr/net/lwm2m.h](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h_source.html)
- [lwm2m_obj_path](P048_lwm2m_obj_path_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [lwm2m_objlnk](P049_lwm2m_objlnk_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P049_lwm2m_objlnk_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_lwm2m_time_series_elem_结构体.md)
