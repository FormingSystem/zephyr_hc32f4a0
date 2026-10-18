---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-2
title: dali_frame_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdali__frame.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_dali\_frame\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdali__frame.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

数字可寻址照明接口（DALI）的帧结构。

```c
#include <zephyr/drivers/dali.h>
```

<a id="details"></a>

数字可寻址照明接口（DALI）的帧结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_a1fe86b3e83933bb32f6025414ed2405d"></a>

```c
uint32_t data
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[data](#a1fe86b3e83933bb32f6025414ed2405d)。

最低有效位对齐（LSB aligned）的载荷。

<a id="r_a401d83846d0ef76cee430ab1085f3ed6"></a>

```c
enum dali_event_type event_type
```

相关声明：[dali_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga0e295a9e86bc694d1516cb50cb579f91)、[event_type](#a401d83846d0ef76cee430ab1085f3ed6)。

帧的事件类型。

## 2.2\_详细说明（Detailed Documentation）

<a id="a1fe86b3e83933bb32f6025414ed2405d"></a>

### `data`

```c
uint32_t dali_frame::data
```

最低有效位对齐（LSB aligned）的载荷。

<a id="a401d83846d0ef76cee430ab1085f3ed6"></a>

### `event_type`

```c
enum dali_event_type dali_frame::event_type
```

帧的事件类型。

本数据类型文档由以下文件生成：

- `zephyr/drivers/dali.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/drivers/dali.h](https://docs.zephyrproject.org/latest/doxygen/html/dali_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [dali_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__dali__interface.html#ga0e295a9e86bc694d1516cb50cb579f91)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_dali_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_devmux_driver_api_结构体.md)
