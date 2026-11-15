---
id: learning.zephyr-docs.system-service-model-reference.page-52
title: input_callback_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structinput__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_input\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structinput__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

输入（Input）的回调结构。

```c
#include <zephyr/input/input.h>
```

<a id="details"></a>

输入（Input）的回调结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_afe8fa2362e5c2ad35a00e05f33498a20"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#afe8fa2362e5c2ad35a00e05f33498a20)。

设备指针或 `NULL`。

<a id="r_a1f50a902f5f1ce10ee9131fcd1e7865d"></a>

```c
void(* callback )(struct input_event *evt, void *user_data)
```

相关声明：[callback](#a1f50a902f5f1ce10ee9131fcd1e7865d)、[input_event](P053_input_event_结构体.md)、[user_data](#a353255145aabf43c92faab719b8f524c)。

回调函数。

<a id="r_a353255145aabf43c92faab719b8f524c"></a>

```c
void * user_data
```

相关声明：[user_data](#a353255145aabf43c92faab719b8f524c)。

用户数据指针。

## 52.2\_详细说明（Detailed Documentation）

<a id="a1f50a902f5f1ce10ee9131fcd1e7865d"></a>

### `callback`

```c
void(* input_callback::callback) (struct input_event *evt, void *user_data)
```

回调函数。

<a id="afe8fa2362e5c2ad35a00e05f33498a20"></a>

### `dev`

```c
const struct device* input_callback::dev
```

设备指针或 `NULL`。

<a id="a353255145aabf43c92faab719b8f524c"></a>

### `user_data`

```c
void* input_callback::user_data
```

用户数据指针。

本数据类型文档由以下文件生成：

- `zephyr/input/input.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/input/input.h](https://docs.zephyrproject.org/latest/doxygen/html/input_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [input_event](P053_input_event_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_img_mgmt_upload_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_input_event_结构体.md)
