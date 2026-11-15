---
id: learning.zephyr-docs.network-application-model-reference.page-48
title: lwm2m_obj_path_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__obj__path.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_lwm2m\_obj\_path\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__obj__path.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

轻量级M2M（LwM2M）的对象路径结构。

```c
#include <zephyr/net/lwm2m.h>
```

<a id="details"></a>

轻量级M2M（LwM2M）的对象路径结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_ad1cf2b4f67b059e92853a05e2d070bb7"></a>

```c
uint16_t obj_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[obj_id](#ad1cf2b4f67b059e92853a05e2d070bb7)。

对象标识（Object ID）。

<a id="r_a7ae1a626b6f4b4c9cdc3e1a99d644ff2"></a>

```c
uint16_t obj_inst_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[obj_inst_id](#a7ae1a626b6f4b4c9cdc3e1a99d644ff2)。

对象实例标识（Object Instance ID）。

<a id="r_ac52cc68142a270b4bab8edfc7cb8b106"></a>

```c
uint16_t res_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[res_id](#ac52cc68142a270b4bab8edfc7cb8b106)。

资源标识（Resource ID）。

<a id="r_a924d75187c05b64989b6eed69b563c29"></a>

```c
uint16_t res_inst_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[res_inst_id](#a924d75187c05b64989b6eed69b563c29)。

资源实例标识（Resource Instance ID）。

<a id="r_aaeb8482037aa5d9b389236eb9f3e2984"></a>

```c
uint8_t level
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[level](#aaeb8482037aa5d9b389236eb9f3e2984)。

路径级别（Path Level），范围为0至4。

## 48.2\_详细说明（Detailed Documentation）

<a id="aaeb8482037aa5d9b389236eb9f3e2984"></a>

### `level`

```c
uint8_t lwm2m_obj_path::level
```

路径级别（Path Level），范围为0至4。

例如，4表示资源实例（Resource Instance）。

<a id="ad1cf2b4f67b059e92853a05e2d070bb7"></a>

### `obj_id`

```c
uint16_t lwm2m_obj_path::obj_id
```

对象标识（Object ID）。

<a id="a7ae1a626b6f4b4c9cdc3e1a99d644ff2"></a>

### `obj_inst_id`

```c
uint16_t lwm2m_obj_path::obj_inst_id
```

对象实例标识（Object Instance ID）。

<a id="ac52cc68142a270b4bab8edfc7cb8b106"></a>

### `res_id`

```c
uint16_t lwm2m_obj_path::res_id
```

资源标识（Resource ID）。

<a id="a924d75187c05b64989b6eed69b563c29"></a>

### `res_inst_id`

```c
uint16_t lwm2m_obj_path::res_inst_id
```

资源实例标识（Resource Instance ID）。

本数据类型文档由以下文件生成：

- `zephyr/net/lwm2m.h`

## 48.3\_原页交叉引用（Cross References）

- [zephyr/net/lwm2m.h](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_lwm2m_ctx_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_lwm2m_objlnk_结构体.md)
