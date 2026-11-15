---
id: learning.zephyr-docs.observability.obapi-1
title: CoreSight解格式接口
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__cs__trace__defmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第26章\_CoreSight解格式接口

原文：[group__cs__trace__defmt](https://docs.zephyrproject.org/latest/doxygen/html/group__cs__trace__defmt.html)。读取日期：2026-10-13，`latest`。

## 26.1\_头文件与帧大小

本页为 CoreSight **跟踪解格式器（Trace Deformatter）**接口参考。

```c
#include <zephyr/debug/coresight/cs_trace_defmt.h>
```

| 宏 | 定义值 | 含义 |
| --- | --- | --- |
| [`CORESIGHT_TRACE_FRAME_SIZE32`](https://docs.zephyrproject.org/latest/doxygen/html/group__cs__trace__defmt.html#gabecbf043f9f0888a0b60d2784aff55e3) | `4` | 以32位字为单位的帧大小 |
| [`CORESIGHT_TRACE_FRAME_SIZE`](https://docs.zephyrproject.org/latest/doxygen/html/group__cs__trace__defmt.html#ga7a31378ad5570f930cab4227a018d80d) | `(CORESIGHT_TRACE_FRAME_SIZE32 * sizeof(uint32_t))` | 以字节为单位的帧大小，即16字节 |

## 26.2\_回调类型

回调（Callback）类型 [`cs_trace_defmt_cb`](https://docs.zephyrproject.org/latest/doxygen/html/group__cs__trace__defmt.html#gaccc05f92bfbc04b787f6f959e954115d) 的签名为：

<a id="gaccc05f92bfbc04b787f6f959e954115d"></a>

```c
typedef void (*cs_trace_defmt_cb)(uint32_t id, const uint8_t *data, size_t len);
```

`id` 为流标识符（Stream ID），`data` 为数据，`len` 为数据长度。

## 26.3\_初始化

<a id="gaaeaaefe2221161691144d82c932196ca"></a>

```c
int cs_trace_defmt_init(cs_trace_defmt_cb cb);
```

初始化 CoreSight 跟踪解格式器。参数 `cb` 为回调。原文未列出该函数的返回值约定。

## 26.4\_处理数据帧

<a id="ga109bab752da74692779aa3eb96b771ba"></a>

```c
int cs_trace_defmt_process(const uint8_t *data, size_t len);
```

从流中解码数据，并通过回调提供解码结果。跟踪格式器以16字节块封装数据：`data` 指向数据，`len` 为长度，**必须等于16**。

返回 `0` 表示成功解格式；长度错误返回 `-EINVAL`。

---

[上一章：插桩接口参考](P025_插桩接口参考.md) · [下一章：MIPI_STP解码接口](P027_MIPI_STP解码接口.md) · [返回大纲](大纲.md)
