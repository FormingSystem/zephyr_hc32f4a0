---
id: learning.zephyr-docs.network-service-model-reference.page-20
title: gptp_scaled_ns_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgptp__scaled__ns.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_gptp\_scaled\_ns\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgptp__scaled__ns.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

缩放纳秒（Scaled Nanoseconds）。

```c
#include <zephyr/net/gptp.h>
```

<a id="details"></a>

缩放纳秒（Scaled Nanoseconds）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 20.1\_数据成员（Data Fields）

<a id="r_af35add15383b49b677e604d61b3d9739"></a>

```c
int32_t high
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[high](#af35add15383b49b677e604d61b3d9739)。

高半部分（High half）。

<a id="r_ac1e95f32bdb1a98f945d9d05a28e8f7f"></a>

```c
int64_t low
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[low](#ac1e95f32bdb1a98f945d9d05a28e8f7f)。

低半部分（Low half）。

## 20.2\_详细说明（Detailed Documentation）

<a id="af35add15383b49b677e604d61b3d9739"></a>

### `high`

```c
int32_t gptp_scaled_ns::high
```

高半部分（High half）。

<a id="ac1e95f32bdb1a98f945d9d05a28e8f7f"></a>

### `low`

```c
int64_t gptp_scaled_ns::low
```

低半部分（Low half）。

本数据类型文档由以下文件生成：

- `zephyr/net/gptp.h`

## 20.3\_原页交叉引用（Cross References）

- [zephyr/net/gptp.h](https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h_source.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P019_gptp_port_identity_结构体.md) · [返回大纲](大纲.md) · [下一章](P021_gptp_uscaled_ns_结构体.md)
