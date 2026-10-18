---
id: learning.zephyr-docs.api-source-reference.page-557
title: mpipe_queue.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__queue_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第557章\_mpipe\_queue.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__queue_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__queue_8h.html)。

## 557.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00075"></a>
<a id="l00080"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="aatomic_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__mpipe__queue_html_ga627fd88220a8b0b06c46aa18fe7d8a84"></a>
<a id="agroup__mpipe__queue_html_ga6cade533253c3f6d31aaede6bfe5e152"></a>
<a id="agroup__mpipe__queue_html_gga627fd88220a8b0b06c46aa18fe7d8a84a473301fa176adda9141acdcedc7b70de"></a>
<a id="agroup__mpipe__queue_html_gga627fd88220a8b0b06c46aa18fe7d8a84a50ac5619e65c3ec7d29ec0abd9bf5cb6"></a>
<a id="agroup__mpipe__queue_html_gga627fd88220a8b0b06c46aa18fe7d8a84aff5e4f0a9919568a53d442b45d274ecf"></a>
<a id="agroup__mpipe__queue_html_ggae0389e724fcbb0a41198c2902aa5ead7a17fb9e12018fca8d667b5771dda465f7"></a>
<a id="agroup__mpipe__queue_html_ggae0389e724fcbb0a41198c2902aa5ead7a72375bea91fdf95aeb286bae43415f1c"></a>
<a id="agroup__mpipe__queue_html_ggae0389e724fcbb0a41198c2902aa5ead7ad9b653b67bd3bda3b56276d918943db6"></a>
<a id="agroup__mpipe__transform_html_gga1710f61119b47e057d957b56ab690dfeacfa117280b8cda0493183451f21570c7"></a>
<a id="akernel_8h_html"></a>
<a id="ampipe__element_8h_html"></a>
<a id="ampipe__thread_8h_html"></a>
<a id="ampipe__transform_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__msgq_html"></a>
<a id="astructmpipe__queue_html"></a>
<a id="astructmpipe__queue_html_a3123f736e185d05da78d53c67bec52b7"></a>
<a id="astructmpipe__queue_html_a36ee4b88ec2fc501f98e72985ea651a8"></a>
<a id="astructmpipe__queue_html_a4f0676f92ac9a2057af2eca5fd577640"></a>
<a id="astructmpipe__queue_html_a64f81e4ac2cb75cdb4d1a45920211daa"></a>
<a id="astructmpipe__queue_html_a7372d2798449c6d49aae12781ae0ac2a"></a>
<a id="astructmpipe__queue_html_a9950b600a3803eae60e93b28b4ca3986"></a>
<a id="astructmpipe__queue_html_aa392264ebe9576abecce5ec3c91daaa7"></a>
<a id="astructmpipe__thread_html"></a>
<a id="astructmpipe__transform_html"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_QUEUE_H_
#define ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_QUEUE_H_


#include <zephyr/kernel.h>
#include <zephyr/sys/atomic.h>

#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_thread.h>
#include <zephyr/mpipe/mpipe_transform.h>

enum {
        MPIPE_PROP_BASE_QUEUE_SIZE = MPIPE_PROP_TRANSFORM_LAST,
        MPIPE_PROP_BASE_QUEUE_THREAD_PRIORITY,
        MPIPE_PROP_BASE_QUEUE_LEAK,
};

enum mpipe_base_queue_leak {
        MPIPE_BASE_QUEUE_LEAK_NONE = 0,
        MPIPE_BASE_QUEUE_LEAK_OLDEST,
        MPIPE_BASE_QUEUE_LEAK_NEWEST,
};

struct mpipe_queue {
        struct mpipe_transform transform;
        struct mpipe_thread thread;
        struct k_msgq msgq;
        char msgq_buffer[(CONFIG_MPIPE_BASE_QUEUE_MAX_SIZE + 2) * sizeof(void *)];
        uint8_t size;
        uint8_t leak;
        atomic_t flushing;
};

int mpipe_queue_init(struct mpipe_queue *queue, uint8_t id);


#endif /* ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_QUEUE_H_ */
```

## 557.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 107 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_BASE_MPIPE_QUEUE_H_`。

## 557.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__queue_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [zephyr/mpipe/mpipe_thread.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__thread_8h.html)
- [zephyr/mpipe/mpipe_transform.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h.html)
- [MPIPE_PROP_BASE_QUEUE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ggae0389e724fcbb0a41198c2902aa5ead7a72375bea91fdf95aeb286bae43415f1c)
- [MPIPE_PROP_TRANSFORM_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#gga1710f61119b47e057d957b56ab690dfeacfa117280b8cda0493183451f21570c7)
- [MPIPE_PROP_BASE_QUEUE_THREAD_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ggae0389e724fcbb0a41198c2902aa5ead7ad9b653b67bd3bda3b56276d918943db6)
- [MPIPE_PROP_BASE_QUEUE_LEAK](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ggae0389e724fcbb0a41198c2902aa5ead7a17fb9e12018fca8d667b5771dda465f7)
- [mpipe_base_queue_leak](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ga627fd88220a8b0b06c46aa18fe7d8a84)
- [MPIPE_BASE_QUEUE_LEAK_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#gga627fd88220a8b0b06c46aa18fe7d8a84a473301fa176adda9141acdcedc7b70de)
- [MPIPE_BASE_QUEUE_LEAK_OLDEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#gga627fd88220a8b0b06c46aa18fe7d8a84a50ac5619e65c3ec7d29ec0abd9bf5cb6)
- [MPIPE_BASE_QUEUE_LEAK_NEWEST](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#gga627fd88220a8b0b06c46aa18fe7d8a84aff5e4f0a9919568a53d442b45d274ecf)
- [mpipe_queue](../audio_video_model_reference/P028_mpipe_queue_结构体.md)
- [mpipe_transform](../audio_video_model_reference/P034_mpipe_transform_结构体.md)
- [transform](../audio_video_model_reference/P028_mpipe_queue_结构体.md#a7372d2798449c6d49aae12781ae0ac2a)
- [mpipe_thread](../audio_video_model_reference/P033_mpipe_thread_结构体.md)
- [thread](../audio_video_model_reference/P028_mpipe_queue_结构体.md#a64f81e4ac2cb75cdb4d1a45920211daa)
- [k_msgq](../msgstack_reference/P002_内核消息队列结构.md)
- [msgq](../audio_video_model_reference/P028_mpipe_queue_结构体.md#a36ee4b88ec2fc501f98e72985ea651a8)
- [msgq_buffer](../audio_video_model_reference/P028_mpipe_queue_结构体.md#aa392264ebe9576abecce5ec3c91daaa7)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [size](../audio_video_model_reference/P028_mpipe_queue_结构体.md#a4f0676f92ac9a2057af2eca5fd577640)
- [leak](../audio_video_model_reference/P028_mpipe_queue_结构体.md#a9950b600a3803eae60e93b28b4ca3986)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [flushing](../audio_video_model_reference/P028_mpipe_queue_结构体.md#a3123f736e185d05da78d53c67bec52b7)
- [mpipe_queue_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__queue.html#ga6cade533253c3f6d31aaede6bfe5e152)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_thread.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__thread_8h.html)
- [mpipe_transform.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h.html)
- [mpipe_queue::flushing](../audio_video_model_reference/P028_mpipe_queue_结构体.md#a3123f736e185d05da78d53c67bec52b7)
- [mpipe_queue::msgq](../audio_video_model_reference/P028_mpipe_queue_结构体.md#a36ee4b88ec2fc501f98e72985ea651a8)
- [mpipe_queue::size](../audio_video_model_reference/P028_mpipe_queue_结构体.md#a4f0676f92ac9a2057af2eca5fd577640)
- [mpipe_queue::thread](../audio_video_model_reference/P028_mpipe_queue_结构体.md#a64f81e4ac2cb75cdb4d1a45920211daa)
- [mpipe_queue::transform](../audio_video_model_reference/P028_mpipe_queue_结构体.md#a7372d2798449c6d49aae12781ae0ac2a)
- [mpipe_queue::leak](../audio_video_model_reference/P028_mpipe_queue_结构体.md#a9950b600a3803eae60e93b28b4ca3986)
- [mpipe_queue::msgq_buffer](../audio_video_model_reference/P028_mpipe_queue_结构体.md#aa392264ebe9576abecce5ec3c91daaa7)

---

[上一章](P556_mpipe_pipeline.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P558_mpipe_sink.h_源码浏览.md)
