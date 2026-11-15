---
id: learning.zephyr-docs.api-source-reference.page-553
title: mpipe_object.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第553章\_mpipe\_object.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h.html)。

## 553.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00087"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="adlist_8h_html"></a>
<a id="agroup__doubly-linked-list__apis_html_ga57fdb936802a617d16c00ab08cd2ad98"></a>
<a id="agroup__mpipe__object_html_ga7ae53fbbd40a3886b0baf767d1e5c4c5"></a>
<a id="agroup__mpipe__object_html_gaa248dc28bf93b5426a9614e8611f60fe"></a>
<a id="agroup__mpipe__object_html_gae63735281ccac01779ba1e037e438641"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__object_html"></a>
<a id="astructmpipe__object_html_a1852f7e5ca10d9bcbe89814ac726d45a"></a>
<a id="astructmpipe__object_html_a2fa018119018fc26ee08bcb07106359d"></a>
<a id="astructmpipe__object_html_a4e0e90f289099c66d3d8949d7dc071c5"></a>
<a id="astructmpipe__object_html_a66b6578b9add34458937f79161ea142b"></a>
<a id="astructmpipe__object_html_ab1851fbf2942804413fa2c79ee7eeac1"></a>
<a id="astructmpipe__object_html_ab4408c02e4b4ecc7112c0b2eaec7dd57"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_OBJECT_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_OBJECT_H_


#include <stdint.h>

#include <zephyr/sys/dlist.h>
#include <zephyr/sys/util_macro.h>

#define MPIPE_OBJECT_FLAG_BASE BIT(0)
#define MPIPE_OBJECT_FLAG_BIN  BIT(1)

#define MPIPE_PROP_LIST_END UINT32_MAX

struct mpipe_object {
        struct mpipe_object *container;
        uint8_t id;
        uint32_t flags;
        sys_dnode_t node;
        int (*set_property)(struct mpipe_object *self, uint32_t key, const void *val);
        int (*get_property)(struct mpipe_object *self, uint32_t key, void *val);
};

void mpipe_object_init(struct mpipe_object *obj);

int mpipe_object_set_properties(struct mpipe_object *obj, ...);

int mpipe_object_get_properties(struct mpipe_object *obj, ...);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_OBJECT_H_ */
```

## 553.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 166 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_OBJECT_H_`。

## 553.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__object_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [mpipe_object](../audio_video_model_reference/P024_mpipe_object_结构体.md)
- [container](../audio_video_model_reference/P024_mpipe_object_结构体.md#a1852f7e5ca10d9bcbe89814ac726d45a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [id](../audio_video_model_reference/P024_mpipe_object_结构体.md#a2fa018119018fc26ee08bcb07106359d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](../audio_video_model_reference/P024_mpipe_object_结构体.md#ab1851fbf2942804413fa2c79ee7eeac1)
- [sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)
- [node](../audio_video_model_reference/P024_mpipe_object_结构体.md#ab4408c02e4b4ecc7112c0b2eaec7dd57)
- [set_property](../audio_video_model_reference/P024_mpipe_object_结构体.md#a66b6578b9add34458937f79161ea142b)
- [get_property](../audio_video_model_reference/P024_mpipe_object_结构体.md#a4e0e90f289099c66d3d8949d7dc071c5)
- [mpipe_object_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#gaa248dc28bf93b5426a9614e8611f60fe)
- [mpipe_object_set_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#gae63735281ccac01779ba1e037e438641)
- [mpipe_object_get_properties](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__object.html#ga7ae53fbbd40a3886b0baf767d1e5c4c5)
- [dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [mpipe_object::container](../audio_video_model_reference/P024_mpipe_object_结构体.md#a1852f7e5ca10d9bcbe89814ac726d45a)
- [mpipe_object::id](../audio_video_model_reference/P024_mpipe_object_结构体.md#a2fa018119018fc26ee08bcb07106359d)
- [mpipe_object::get_property](../audio_video_model_reference/P024_mpipe_object_结构体.md#a4e0e90f289099c66d3d8949d7dc071c5)
- [mpipe_object::set_property](../audio_video_model_reference/P024_mpipe_object_结构体.md#a66b6578b9add34458937f79161ea142b)
- [mpipe_object::flags](../audio_video_model_reference/P024_mpipe_object_结构体.md#ab1851fbf2942804413fa2c79ee7eeac1)
- [mpipe_object::node](../audio_video_model_reference/P024_mpipe_object_结构体.md#ab4408c02e4b4ecc7112c0b2eaec7dd57)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P552_mpipe_message.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P554_mpipe_pad.h_源码浏览.md)
