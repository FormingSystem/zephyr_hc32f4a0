---
id: learning.zephyr-docs.network-application-model-reference.page-49
title: lwm2m_objlnk_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__objlnk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_lwm2m\_objlnk\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__objlnk.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

轻量级M2M（LwM2M）的对象链接（Objlnk）资源类型结构。

```c
#include <zephyr/net/lwm2m.h>
```

<a id="details"></a>

轻量级M2M（LwM2M）的对象链接（Objlnk）资源类型结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

<a id="r_a67193c8612b3a3d2a6a9685f7d1a0053"></a>

```c
uint16_t obj_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[obj_id](#a67193c8612b3a3d2a6a9685f7d1a0053)。

对象标识（Object ID）。

<a id="r_aa51649798b00bc0bb9887c9739b83d27"></a>

```c
uint16_t obj_inst
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[obj_inst](#aa51649798b00bc0bb9887c9739b83d27)。

对象实例标识（Object Instance ID）。

## 49.2\_详细说明（Detailed Documentation）

<a id="a67193c8612b3a3d2a6a9685f7d1a0053"></a>

### `obj_id`

```c
uint16_t lwm2m_objlnk::obj_id
```

对象标识（Object ID）。

<a id="aa51649798b00bc0bb9887c9739b83d27"></a>

### `obj_inst`

```c
uint16_t lwm2m_objlnk::obj_inst
```

对象实例标识（Object Instance ID）。

本数据类型文档由以下文件生成：

- `zephyr/net/lwm2m.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/net/lwm2m.h](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_lwm2m_obj_path_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_lwm2m_res_item_结构体.md)
