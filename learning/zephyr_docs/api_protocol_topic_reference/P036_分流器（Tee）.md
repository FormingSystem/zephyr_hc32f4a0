---
id: learning.zephyr-docs.api-protocol-topic-reference.page-36
title: 分流器（Tee）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_分流器（Tee）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__tee.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

管线分支元素：具有一个接收端口（Sink pad）和 N 个源端口（Source pad）。

<a id="details"></a>

管线分支元素：具有一个接收端口（Sink pad）和 N 个源端口（Source pad）。

<a id="header-files"></a>
<a id="files"></a>

## 36.1\_文件（Files）

<a id="r_mpipe_5Ftee_2Eh"></a>

```c
file mpipe_tee.h
```

相关声明：[mpipe_tee.h](../api_file_runtime_reference/P043_zephyr__mpipe__base__mpipe_tee.h_文件参考.md)。

用于流水线分支（Pipeline Branching）的分流元素（Tee）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 36.2\_数据结构（Data Structures）

<a id="r_mpipe_5Ftee"></a>

```c
struct mpipe_tee
```

相关声明：[mpipe_tee](../audio_video_model_reference/P032_mpipe_tee_结构体.md)。

分流元素（Tee Element）的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 36.3\_枚举（Enumerations）

<a id="r_ga963f0d9cbcc79afcaea9de8fcd27e671"></a>

```c
enum mpipe_prop_base_tee { MPIPE_PROP_BASE_TEE_SRC_PADS_NUM }
```

相关声明：[mpipe_prop_base_tee](#ga963f0d9cbcc79afcaea9de8fcd27e671)、[MPIPE_PROP_BASE_TEE_SRC_PADS_NUM](#gga963f0d9cbcc79afcaea9de8fcd27e671af381b068c7f00ca42dd9116809eabbd2)。

分流元素属性标识（Tee Property Identifiers）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 36.4\_函数（Functions）

<a id="r_ga3b4228b75ae8c2b6274240979c3a1162"></a>

```c
int mpipe_tee_init (struct mpipe_tee *tee, uint8_t id)
```

相关声明：[mpipe_tee_init](#ga3b4228b75ae8c2b6274240979c3a1162)、[mpipe_tee](../audio_video_model_reference/P032_mpipe_tee_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化分流元素（Tee Element）。

## 36.5\_详细说明（Detailed Documentation）

<a id="ga963f0d9cbcc79afcaea9de8fcd27e671"></a>

### `mpipe_prop_base_tee`

```c
enum mpipe_prop_base_tee
```

```c
#include <zephyr/mpipe/base/mpipe_tee.h>
```

分流元素属性标识（Tee Property Identifiers）。

可为分流元素（tee element）配置的属性枚举。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MPIPE_PROP_BASE_TEE_SRC_PADS_NUM` | 源连接点数量。 |

<a id="ga3b4228b75ae8c2b6274240979c3a1162"></a>

### `mpipe_tee_init()`

```c
int mpipe_tee_init ( struct mpipe_tee * tee, uint8_t id )
```

```c
#include <zephyr/mpipe/base/mpipe_tee.h>
```

初始化分流元素（Tee Element）。

初始化分流元素（tee element），配置一个接收端连接端（sink pad）和两个默认的 `src_pads` 发送端连接端。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tee` | 指向待初始化元素（Element）的指针（Pointer）。 |
| `id` | 唯一元素标识（Unique Element Identifier）。 |

返回（Returns）：成功时为 0，否则为负错误号（Negative `errno`）。


## 36.6\_原页交叉引用（Cross References）

- [mpipe_tee.h](../api_file_runtime_reference/P043_zephyr__mpipe__base__mpipe_tee.h_文件参考.md)
- [mpipe_tee](../audio_video_model_reference/P032_mpipe_tee_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga963f0d9cbcc79afcaea9de8fcd27e671af381b068c7f00ca42dd9116809eabbd2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P035_解析器（Parsers）.md) · [返回大纲](大纲.md) · [下一章](P037_MSPI 回调 API（MSPI callback API）.md)
