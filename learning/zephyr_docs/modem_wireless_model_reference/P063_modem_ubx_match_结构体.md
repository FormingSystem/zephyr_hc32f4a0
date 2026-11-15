---
id: learning.zephyr-docs.modem-wireless-model-reference.page-63
title: modem_ubx_match_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__ubx__match.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_modem\_ubx\_match\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__ubx__match.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_aba64a4f7825a1f3b3cbee6f3473d7f74"></a>

```c
struct ubx_frame_match filter
```

相关声明：[ubx_frame_match](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md)、[filter](#aba64a4f7825a1f3b3cbee6f3473d7f74)。

<a id="r_a657d7961121ed1860635df96597b88b8"></a>

```c
modem_ubx_match_callback handler
```

相关声明：[modem_ubx_match_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#gae0bfe22e7e8d7d38ae9f41648f7fcfda)、[handler](#a657d7961121ed1860635df96597b88b8)。

## 63.2\_详细说明（Detailed Documentation）

<a id="aba64a4f7825a1f3b3cbee6f3473d7f74"></a>

### `filter`

```c
struct ubx_frame_match modem_ubx_match::filter
```

<a id="a657d7961121ed1860635df96597b88b8"></a>

### `handler`

```c
modem_ubx_match_callback modem_ubx_match::handler
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx.h](https://docs.zephyrproject.org/latest/doxygen/html/ubx_8h_source.html)
- [ubx_frame_match](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md)
- [modem_ubx_match_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#gae0bfe22e7e8d7d38ae9f41648f7fcfda)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_modem_ubx_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_modem_ubx_script_结构体.md)
