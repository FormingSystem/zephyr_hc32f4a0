---
id: learning.zephyr-docs.observability.obheader-1
title: CoreSight解格式头文件
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cs__trace__defmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第45章\_CoreSight解格式头文件

原文：[cs__trace__defmt_8h](https://docs.zephyrproject.org/latest/doxygen/html/cs__trace__defmt_8h.html)。读取日期：2026-10-13，`latest`。

## 45.1\_用途与包含关系

`zephyr/debug/coresight/cs_trace_defmt.h` 是CoreSight跟踪解格式器（Trace Deformatter）的头文件参考。

官方页面列出的包含项如下：

```c
#include <zephyr/kernel.h>
```

[查看官方头文件源码](../debug_trace_reference/P002_CoreSight跟踪解格式头文件源码.md)。

## 45.2\_帧大小与回调

| 宏 | 定义值 | 说明 |
| --- | --- | --- |
| [`CORESIGHT_TRACE_FRAME_SIZE32`](https://docs.zephyrproject.org/latest/doxygen/html/group__cs__trace__defmt.html#gabecbf043f9f0888a0b60d2784aff55e3) | `4` | 以32位字为单位的帧大小 |
| [`CORESIGHT_TRACE_FRAME_SIZE`](https://docs.zephyrproject.org/latest/doxygen/html/group__cs__trace__defmt.html#ga7a31378ad5570f930cab4227a018d80d) | `(CORESIGHT_TRACE_FRAME_SIZE32 * sizeof(uint32_t))` | 以字节为单位的帧大小 |

回调（Callback）类型签名如下：

```c
typedef void (*cs_trace_defmt_cb)(uint32_t id, const uint8_t *data, size_t len);
```

## 45.3\_函数声明

以下声明与官方头文件参考页对应，完整参数和返回值见[对应接口说明](P026_CoreSight解格式接口.md)。

| 声明 | 说明 |
| --- | --- |
| `int cs_trace_defmt_init(cs_trace_defmt_cb cb);` | 初始化CoreSight跟踪解格式器 |
| `int cs_trace_defmt_process(const uint8_t *data, size_t len);` | 解码流中的数据 |

---

[上一章：插桩头文件](P044_插桩头文件.md) · [下一章：MIPI_STP解码头文件](P046_MIPI_STP解码头文件.md) · [返回大纲](大纲.md)
