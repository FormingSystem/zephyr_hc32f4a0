---
id: learning.zephyr-docs.api-file-service-reference.page-26
title: zephyr__mpipe__base__mpipe_queue.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__queue_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_zephyr\_\_mpipe\_\_base\_\_mpipe\_queue.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__queue_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于流水线级线程化（Pipeline-Level Threading）的队列元素。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_thread.h>
#include <zephyr/mpipe/mpipe_transform.h>
```

查看此文件的源码。

用于流水线级线程划分（Pipeline-Level Threading）的队列元素（Queue Element）。它将流水线分成在两个线程上运行的两段：上游（Upstream）把缓冲区放入队列，专用线程（Dedicated Thread）从队列取出缓冲区，再将其推送到流水线其余部分。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 26.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fqueue"></a>

```c
struct mpipe_queue
```

相关声明：[mpipe_queue](../audio_video_model_reference/P028_mpipe_queue_结构体.md)。

队列元素（Queue Element）的结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 26.2\_枚举（Enumerations）

<a id="r_gae0389e724fcbb0a41198c2902aa5ead7"></a>

```c
enum { MPIPE_PROP_BASE_QUEUE_SIZE = MPIPE_PROP_TRANSFORM_LAST , MPIPE_PROP_BASE_QUEUE_THREAD_PRIORITY , MPIPE_PROP_BASE_QUEUE_LEAK }
```

相关声明：[MPIPE_PROP_BASE_QUEUE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ggae0389e724fcbb0a41198c2902aa5ead7a72375bea91fdf95aeb286bae43415f1c)、[MPIPE_PROP_BASE_QUEUE_THREAD_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ggae0389e724fcbb0a41198c2902aa5ead7ad9b653b67bd3bda3b56276d918943db6)、[MPIPE_PROP_BASE_QUEUE_LEAK](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ggae0389e724fcbb0a41198c2902aa5ead7a17fb9e12018fca8d667b5771dda465f7)。

队列属性标识（Queue Property Identifiers）。

<a id="r_ga627fd88220a8b0b06c46aa18fe7d8a84"></a>

```c
enum mpipe_base_queue_leak { MPIPE_BASE_QUEUE_LEAK_NONE = 0 , MPIPE_BASE_QUEUE_LEAK_OLDEST , MPIPE_BASE_QUEUE_LEAK_NEWEST }
```

相关声明：[mpipe_base_queue_leak](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ga627fd88220a8b0b06c46aa18fe7d8a84)、[MPIPE_BASE_QUEUE_LEAK_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#gga627fd88220a8b0b06c46aa18fe7d8a84a473301fa176adda9141acdcedc7b70de)、[MPIPE_BASE_QUEUE_LEAK_OLDEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#gga627fd88220a8b0b06c46aa18fe7d8a84a50ac5619e65c3ec7d29ec0abd9bf5cb6)、[MPIPE_BASE_QUEUE_LEAK_NEWEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#gga627fd88220a8b0b06c46aa18fe7d8a84aff5e4f0a9919568a53d442b45d274ecf)。

队列已满（Full Queue）时对新缓冲区（New Buffer）的处理方式。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 26.3\_函数（Functions）

<a id="r_ga6cade533253c3f6d31aaede6bfe5e152"></a>

```c
int mpipe_queue_init (struct mpipe_queue *queue, uint8_t id)
```

相关声明：[mpipe_queue_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ga6cade533253c3f6d31aaede6bfe5e152)、[mpipe_queue](../audio_video_model_reference/P028_mpipe_queue_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

初始化队列元素（Queue Element）。


## 26.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/mpipe/mpipe_element.h](../api_source_reference/P550_mpipe_element.h_源码浏览.md)
- [zephyr/mpipe/mpipe_thread.h](../api_source_runtime_reference/P044_mpipe_thread.h_源码浏览.md)
- [zephyr/mpipe/mpipe_transform.h](../api_source_reference/P562_mpipe_transform.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P557_mpipe_queue.h_源码浏览.md)
- [mpipe_queue](../audio_video_model_reference/P028_mpipe_queue_结构体.md)
- [MPIPE_PROP_BASE_QUEUE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ggae0389e724fcbb0a41198c2902aa5ead7a72375bea91fdf95aeb286bae43415f1c)
- [MPIPE_PROP_BASE_QUEUE_THREAD_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ggae0389e724fcbb0a41198c2902aa5ead7ad9b653b67bd3bda3b56276d918943db6)
- [MPIPE_PROP_BASE_QUEUE_LEAK](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ggae0389e724fcbb0a41198c2902aa5ead7a17fb9e12018fca8d667b5771dda465f7)
- [mpipe_base_queue_leak](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ga627fd88220a8b0b06c46aa18fe7d8a84)
- [MPIPE_BASE_QUEUE_LEAK_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#gga627fd88220a8b0b06c46aa18fe7d8a84a473301fa176adda9141acdcedc7b70de)
- [MPIPE_BASE_QUEUE_LEAK_OLDEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#gga627fd88220a8b0b06c46aa18fe7d8a84a50ac5619e65c3ec7d29ec0abd9bf5cb6)
- [MPIPE_BASE_QUEUE_LEAK_NEWEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#gga627fd88220a8b0b06c46aa18fe7d8a84aff5e4f0a9919568a53d442b45d274ecf)
- [mpipe_queue_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ga6cade533253c3f6d31aaede6bfe5e152)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>

---

[上一章](P025_zephyr__mpipe__mpipe_message.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P027_zephyr__drivers__pcie__msi.h_文件参考.md)
