---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-97
title: w1_master_data_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structw1__master__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第97章\_w1\_master\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structw1__master__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全部单总线（1-Wire）主机实现共用的数据。

```c
#include <zephyr/drivers/w1.h>
```

<a id="details"></a>

所有 1-Wire 主机实现共用的数据。此结构体为所有 1-Wire 主机实现所共用，应作为 `device` 结构体的 `data` 字段所指对象的第一个成员。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 97.1\_数据成员（Data Fields）

<a id="r_af9cc46f803aff0d5e0d8ca345aaf8b9e"></a>

```c
struct k_mutex bus_lock
```

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[bus_lock](#af9cc46f803aff0d5e0d8ca345aaf8b9e)。

供 `w1_lock_bus()` 和 `w1_unlock_bus()` 方法使用的互斥锁。

## 97.2\_详细说明（Detailed Documentation）

<a id="af9cc46f803aff0d5e0d8ca345aaf8b9e"></a>

### `bus_lock`

```c
struct k_mutex w1_master_data::bus_lock
```

供 `w1_lock_bus()` 和 `w1_unlock_bus()` 方法使用的互斥锁。

本数据类型文档由以下文件生成：

- `zephyr/drivers/w1.h`

## 97.3\_原页交叉引用（Cross References）

- [zephyr/drivers/w1.h](https://docs.zephyrproject.org/latest/doxygen/html/w1_8h_source.html)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [w1_lock_bus()](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gab18b0f60a126d38c982730d3ad9756c1)
- [w1_unlock_bus()](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#ga7230fad2428ab62fa963b50e67388c19)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P096_w1_master_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P098_w1_rom_结构体.md)
