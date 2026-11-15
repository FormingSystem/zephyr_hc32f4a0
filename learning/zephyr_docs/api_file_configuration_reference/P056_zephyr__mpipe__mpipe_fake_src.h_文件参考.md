---
id: learning.zephyr-docs.api-file-configuration-reference.page-56
title: zephyr__mpipe__mpipe_fake_src.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__fake__src_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_zephyr\_\_mpipe\_\_mpipe\_fake\_src.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__fake__src_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

模拟源元素（Fake Source Element）。

<a id="details"></a>

```c
#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_src.h>
```

查看此文件的源码。

伪源元素（Fake Source Element）。这是一个简单的仿真源元素（Emulated Source Element），生成用于测试的伪数据缓冲区（Fake Data Buffers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 56.1\_数据结构（Data Structures）

<a id="r_mpipe_5Ffake_5Fsrc"></a>

```c
struct mpipe_fake_src
```

相关声明：[mpipe_fake_src](../audio_video_model_reference/P022_mpipe_fake_src_结构体.md)。

模拟源元素（Fake Source Element）的结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 56.2\_函数（Functions）

<a id="r_ga1eed36753b4c3d29b2e8c94e74ee832c"></a>

```c
int mpipe_fake_src_init (struct mpipe_fake_src *fsrc, uint8_t id)
```

相关声明：[mpipe_fake_src_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ga1eed36753b4c3d29b2e8c94e74ee832c)、[mpipe_fake_src](../audio_video_model_reference/P022_mpipe_fake_src_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化伪源元素（Fake Source Element）。


## 56.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_buffer.h](../api_source_reference/P546_mpipe_buffer.h_源码浏览.md)
- [zephyr/mpipe/mpipe_src.h](../api_source_reference/P559_mpipe_src.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P551_mpipe_fake_src.h_源码浏览.md)
- [mpipe_fake_src](../audio_video_model_reference/P022_mpipe_fake_src_结构体.md)
- [mpipe_fake_src_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__src.html#ga1eed36753b4c3d29b2e8c94e74ee832c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>

---

[上一章](P055_zephyr__drivers__sensor__mmc56x3.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P057_zephyr__mpipe__mpipe_workqueue.h_文件参考.md)
