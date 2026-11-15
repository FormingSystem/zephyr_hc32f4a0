---
id: learning.zephyr-docs.audio-video-model-reference.page-40
title: mpl_search_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpl__search.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_mpl\_search\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpl__search.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

搜索（Search）。

```c
#include <zephyr/bluetooth/audio/media_proxy.h>
```

<a id="details"></a>

搜索（Search）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_a9b9c64d3d9a25951da58ebf47bb63617"></a>

```c
uint8_t len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[len](#a9b9c64d3d9a25951da58ebf47bb63617)。

`mpl_search::search` 值的长度。

<a id="r_a836bebfaadb56672a7e76c0ac2e450a9"></a>

```c
char search [64U]
```

相关声明：[search](#a836bebfaadb56672a7e76c0ac2e450a9)。

串接的搜索控制项（search control items），格式为 `(type, length, param)`。

## 40.2\_详细说明（Detailed Documentation）

<a id="a9b9c64d3d9a25951da58ebf47bb63617"></a>

### `len`

```c
uint8_t mpl_search::len
```

`mpl_search::search` 值的长度。

<a id="a836bebfaadb56672a7e76c0ac2e450a9"></a>

### `search`

```c
char mpl_search::search[64U]
```

串接的搜索控制项（search control items），格式为 `(type, length, param)`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/media_proxy.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/media_proxy.h](https://docs.zephyrproject.org/latest/doxygen/html/media__proxy_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_mpl_sci_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_pcm_config_结构体.md)
