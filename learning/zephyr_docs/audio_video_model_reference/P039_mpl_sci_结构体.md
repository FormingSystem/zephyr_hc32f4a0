---
id: learning.zephyr-docs.audio-video-model-reference.page-39
title: mpl_sci_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpl__sci.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_mpl\_sci\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpl__sci.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

搜索控制项（Search Control Item）。

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

<a id="details"></a>

搜索控制项（Search Control Item）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_a348314407c7b46d5ed583b97dfe932bc"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#a348314407c7b46d5ed583b97dfe932bc)。

类型与参数的长度。

<a id="r_a1dfc87f7e8b509ca05cbcd97a245953f"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a1dfc87f7e8b509ca05cbcd97a245953f)。

搜索类型：`MEDIA_PROXY_SEARCH_TYPE_<...>`。

<a id="r_af093a6cd52a74cb2a0989727fc89f3aa"></a>

```c
char param [62U]
```

相关声明：[param](#af093a6cd52a74cb2a0989727fc89f3aa)。

搜索参数（Search parameter）。

## 39.2\_详细说明（Detailed Documentation）

<a id="a348314407c7b46d5ed583b97dfe932bc"></a>

### `len`

```c
uint8_t mpl_sci::len
```

类型与参数的长度。

<a id="af093a6cd52a74cb2a0989727fc89f3aa"></a>

### `param`

```c
char mpl_sci::param[62U]
```

搜索参数（Search parameter）。

<a id="a1dfc87f7e8b509ca05cbcd97a245953f"></a>

### `type`

```c
uint8_t mpl_sci::type
```

搜索类型：`MEDIA_PROXY_SEARCH_TYPE_<...>`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/media_proxy.h`

## 39.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/media_proxy.h](https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_mpl_cmd_ntf_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_mpl_search_结构体.md)
