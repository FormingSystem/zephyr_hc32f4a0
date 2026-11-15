---
id: learning.zephyr-docs.api-source-reference.page-539
title: stats.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modem_2stats_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第539章\_stats.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/modem_2stats_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/modem_2stats_8h.html)。

## 539.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00016"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00028"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amodem_2stats_8h_html_ac97a44071b31768bd2d39bef27bfd746"></a>
<a id="amodem_2stats_8h_html_af4ccdf8a97586021431d858565a8f28f"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2024 Trackunit Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/types.h>
#include <zephyr/kernel.h>

#ifndef ZEPHYR_INCLUDE_MODEM_STATS_H_
#define ZEPHYR_INCLUDE_MODEM_STATS_H_


struct modem_stats_buffer {
        sys_snode_t node;
        char name[CONFIG_MODEM_STATS_BUFFER_NAME_SIZE];
        uint32_t max_used;
        uint32_t size;
};


void modem_stats_buffer_init(struct modem_stats_buffer *buffer,
                             const char *name, uint32_t size);

void modem_stats_buffer_advertise_length(struct modem_stats_buffer *buffer, uint32_t length);

#endif /* ZEPHYR_INCLUDE_MODEM_STATS_H_ */
```

## 539.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Trackunit Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 50 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MODEM_STATS_H_`。

## 539.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/modem_2stats_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [modem_stats_buffer_init](https://docs.zephyrproject.org/latest/doxygen/html/modem_2stats_8h.html#ac97a44071b31768bd2d39bef27bfd746)
- [modem_stats_buffer_advertise_length](https://docs.zephyrproject.org/latest/doxygen/html/modem_2stats_8h.html#af4ccdf8a97586021431d858565a8f28f)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P538_tty.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P540_keys.h_源码浏览.md)
