---
id: learning.zephyr-docs.api-source-configuration-reference.page-58
title: mpipe_bin.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_mpipe\_bin.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h.html)。

## 58.1\_原始可见代码（Source Code）

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
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="adlist_8h_html"></a>
<a id="agroup__doubly-linked-list__apis_html_gaa03f9557215b486fee1039dd4c07e683"></a>
<a id="agroup__mpipe__bin_html_ga0029c3da6a9bfca02c22673e4622a957"></a>
<a id="agroup__mpipe__bin_html_ga564685f39d56de259d9df1257a57b1b7"></a>
<a id="agroup__mpipe__bin_html_ga57d13bc1cb4c8f3095e3acbe08f7b6d4"></a>
<a id="agroup__mpipe__bin_html_gab9a27c7642bd57189aa1f62da3c080e3"></a>
<a id="agroup__mpipe__element_html_ga219cea77697cda52503e88096029c287"></a>
<a id="agroup__zbus__apis_html_ga44ca2e52a4f1bcf298888a7ebf9b5cf7"></a>
<a id="ampipe__element_8h_html"></a>
<a id="ampipe__message_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__bin_html"></a>
<a id="astructmpipe__bin_html_a165735c1d573616e990b8bf707a2567f"></a>
<a id="astructmpipe__bin_html_a40ceee13946c8b9e408cc53e9ecfed09"></a>
<a id="astructmpipe__bin_html_a60d49bd3793ea05e14f7c6d959a182d7"></a>
<a id="astructmpipe__bin_html_aecf25e2b5010acc8754dc7ae9bd4c222"></a>
<a id="astructmpipe__element_html"></a>
<a id="astructmpipe__message_html"></a>
<a id="astructzbus__channel__data_html"></a>
<a id="astructzbus__runtime__channel_html"></a>
<a id="azbus_8h_html"></a>

```c
/*
 * Copyright 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_BIN_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_BIN_H_


#include <stdint.h>

#include <zephyr/sys/dlist.h>
#include <zephyr/zbus/zbus.h>

#include <zephyr/mpipe/mpipe_element.h>
#include <zephyr/mpipe/mpipe_message.h>

struct mpipe_bin {
        struct mpipe_element element;
        int children_num;
        sys_dlist_t children;
        struct zbus_runtime_channel bus;

        /* Bus channel mutable runtime state: observer bookkeeping, lock, counters. */
        struct zbus_channel_data chan_data;
        /* Bus channel message buffer: holds the last published mpipe_message. */
        struct mpipe_message chan_msg;
};

int mpipe_bin_init(struct mpipe_bin *bin, uint8_t id);

int mpipe_bin_set_bus_validator(struct mpipe_bin *bin, zbus_validator bus_validator,
                                void *user_data);

int mpipe_bin_add(struct mpipe_bin *bin, struct mpipe_element *element, ...);

int mpipe_bin_change_state_func(struct mpipe_element *element, enum mpipe_state_change transition);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_BIN_H_ */
```

## 58.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 69 行

总线通道的可变运行时状态（Mutable runtime state）：观察者记录、锁和计数器。

### 注释 3：原第 71 行

总线通道消息缓冲区：保存最后一次发布的 `mpipe_message`。

### 注释 4：原第 152 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_BIN_H_`。

## 58.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [zephyr/zbus/zbus.h](../intercore_reference/P211_zbus核心头文件参考.md)
- [zephyr/mpipe/mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [zephyr/mpipe/mpipe_message.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h.html)
- [mpipe_bin](../audio_video_model_reference/P015_mpipe_bin_结构体.md)
- [mpipe_element](../audio_video_model_reference/P021_mpipe_element_结构体.md)
- [element](../audio_video_model_reference/P015_mpipe_bin_结构体.md#aecf25e2b5010acc8754dc7ae9bd4c222)
- [children_num](../audio_video_model_reference/P015_mpipe_bin_结构体.md#a40ceee13946c8b9e408cc53e9ecfed09)
- [sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)
- [children](../audio_video_model_reference/P015_mpipe_bin_结构体.md#a165735c1d573616e990b8bf707a2567f)
- [zbus_runtime_channel](../intercore_reference/P210_zbus运行时通道结构.md)
- [bus](../audio_video_model_reference/P015_mpipe_bin_结构体.md#a60d49bd3793ea05e14f7c6d959a182d7)
- [zbus_channel_data](../intercore_reference/P207_zbus通道运行时结构.md)
- [mpipe_message](../audio_video_model_reference/P023_mpipe_message_结构体.md)
- [mpipe_bin_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#gab9a27c7642bd57189aa1f62da3c080e3)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_bin_set_bus_validator](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#ga57d13bc1cb4c8f3095e3acbe08f7b6d4)
- [zbus_validator](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__apis.html#ga44ca2e52a4f1bcf298888a7ebf9b5cf7)
- [mpipe_bin_add](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#ga0029c3da6a9bfca02c22673e4622a957)
- [mpipe_bin_change_state_func](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__bin.html#ga564685f39d56de259d9df1257a57b1b7)
- [mpipe_state_change](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#ga219cea77697cda52503e88096029c287)
- [dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [mpipe_element.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__element_8h.html)
- [mpipe_message.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__message_8h.html)
- [mpipe_bin::children](../audio_video_model_reference/P015_mpipe_bin_结构体.md#a165735c1d573616e990b8bf707a2567f)
- [mpipe_bin::children_num](../audio_video_model_reference/P015_mpipe_bin_结构体.md#a40ceee13946c8b9e408cc53e9ecfed09)
- [mpipe_bin::bus](../audio_video_model_reference/P015_mpipe_bin_结构体.md#a60d49bd3793ea05e14f7c6d959a182d7)
- [mpipe_bin::element](../audio_video_model_reference/P015_mpipe_bin_结构体.md#aecf25e2b5010acc8754dc7ae9bd4c222)
- [zbus.h](../intercore_reference/P211_zbus核心头文件参考.md)

---

[上一章](P057_mm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P059_mspm0_clock.h_源码浏览.md)
