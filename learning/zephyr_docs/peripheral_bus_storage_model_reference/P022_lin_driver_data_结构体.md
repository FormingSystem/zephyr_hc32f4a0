---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-22
title: lin_driver_data_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlin__driver__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_lin\_driver\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlin__driver__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用LIN驱动数据结构。

```c
#include <zephyr/drivers/lin.h>
```

<a id="details"></a>

通用 LIN 驱动数据结构体（Driver data structure）。此结构体用于保存 LIN 驱动状态，应作为 `device` 结构体的 `data` 字段所指对象的第一个成员。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_aa83a634b8726bf5f2ff8552aedc9ca36"></a>

```c
struct lin_config config
```

相关声明：[lin_config](P019_lin_config_结构体.md)、[config](#aa83a634b8726bf5f2ff8552aedc9ca36)。

当前 LIN 控制器配置。

<a id="r_acfe00a4ae3aeaff0d43d51c9b8aeeec1"></a>

```c
bool started
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[started](#acfe00a4ae3aeaff0d43d51c9b8aeeec1)。

LIN 控制器已启动时为 `true`，否则为 `false`。

<a id="r_a5c8c75a944077f3c84d80826dbcb76a5"></a>

```c
lin_event_callback_t callback
```

相关声明：[lin_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gae69d33055fe07087a19b33dbe7a7252f)、[callback](#a5c8c75a944077f3c84d80826dbcb76a5)。

LIN 事件回调函数指针，或 `NULL`。

<a id="r_a227dd7bb9dd4778a4dcfe13d5cc29751"></a>

```c
void * callback_data
```

相关声明：[callback_data](#a227dd7bb9dd4778a4dcfe13d5cc29751)。

传递给回调函数的用户数据指针。

## 22.2\_详细说明（Detailed Documentation）

<a id="a5c8c75a944077f3c84d80826dbcb76a5"></a>

### `callback`

```c
lin_event_callback_t lin_driver_data::callback
```

LIN 事件回调函数指针，或 `NULL`。

<a id="a227dd7bb9dd4778a4dcfe13d5cc29751"></a>

### `callback_data`

```c
void* lin_driver_data::callback_data
```

传递给回调函数的用户数据指针。

<a id="aa83a634b8726bf5f2ff8552aedc9ca36"></a>

### `config`

```c
struct lin_config lin_driver_data::config
```

当前 LIN 控制器配置。

<a id="acfe00a4ae3aeaff0d43d51c9b8aeeec1"></a>

### `started`

```c
bool lin_driver_data::started
```

LIN 控制器已启动时为 `true`，否则为 `false`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/lin.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/drivers/lin.h](https://docs.zephyrproject.org/latest/doxygen/html/lin_8h_source.html)
- [lin_config](P019_lin_config_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [lin_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gae69d33055fe07087a19b33dbe7a7252f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_lin_driver_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_lin_event_结构体.md)
