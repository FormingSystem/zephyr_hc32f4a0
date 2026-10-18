---
id: learning.zephyr-docs.api-file-supplement-reference.page-74
title: zephyr__mpipe__mpipe_transform_client.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform__client_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_zephyr\_\_mpipe\_\_mpipe\_transform\_client.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform__client_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

变换客户端（Transform Client）：工作在另一内核上运行的变换。

<a id="details"></a>

```c
#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_transform.h>
```

查看此文件的源码。

变换客户端（Transform Client）：工作在另一内核上运行的变换。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 74.1\_数据结构（Data Structures）

<a id="r_mpipe_5Ftransform_5Fclient"></a>

```c
struct mpipe_transform_client
```

相关声明：[mpipe_transform_client](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md)。

变换客户端元素（Transform Client Element）的结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 74.2\_函数（Functions）

<a id="r_ga2b1ea237f62a4cf9731a90e3b5d0eea4"></a>

```c
int mpipe_transform_client_init (struct mpipe_transform_client *transform_client, uint8_t id)
```

相关声明：[mpipe_transform_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga2b1ea237f62a4cf9731a90e3b5d0eea4)、[mpipe_transform_client](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化变换客户端元素（Transform Client Element）。


## 74.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_buffer.h](../api_source_reference/P546_mpipe_buffer.h_源码浏览.md)
- [zephyr/mpipe/mpipe_transform.h](../api_source_reference/P562_mpipe_transform.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P563_mpipe_transform_client.h_源码浏览.md)
- [mpipe_transform_client](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md)
- [mpipe_transform_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga2b1ea237f62a4cf9731a90e3b5d0eea4)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>

---

[上一章](P073_zephyr__mpipe__mpipe_dispatch.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P075_zephyr__dt-bindings__clock__mspm0_clock.h_文件参考.md)
