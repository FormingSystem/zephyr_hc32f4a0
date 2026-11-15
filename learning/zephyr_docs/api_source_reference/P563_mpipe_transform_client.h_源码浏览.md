---
id: learning.zephyr-docs.api-source-reference.page-563
title: mpipe_transform_client.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform__client_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第563章\_mpipe\_transform\_client.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform__client_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform__client_8h.html)。

## 563.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00039"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="agroup__mpipe__transform_html_ga2b1ea237f62a4cf9731a90e3b5d0eea4"></a>
<a id="ampipe__buffer_8h_html"></a>
<a id="ampipe__transform_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructmpipe__transform__client_html"></a>
<a id="astructmpipe__transform__client_html_a65c1ee88e4255222e7b1ed93f4c56a58"></a>
<a id="astructmpipe__transform__client_html_a8e406cdc0e2c448faf5c6e286779739e"></a>
<a id="astructmpipe__transform__client_html_a9d6edb742acdfe64509d0c3fb6567a36"></a>
<a id="astructmpipe__transform_html"></a>

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MPIPE_MPIPE_TRANSFORM_CLIENT_H_
#define ZEPHYR_INCLUDE_MPIPE_MPIPE_TRANSFORM_CLIENT_H_


#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_transform.h>

struct mpipe_transform_client {
        struct mpipe_transform transform;

        int (*init_rpc)(void);
        int (*process_fn_rpc)(uint32_t in_buf, uint32_t in_sz, uint32_t out_buf, uint32_t *out_sz);
};

int mpipe_transform_client_init(struct mpipe_transform_client *transform_client, uint8_t id);


#endif /* ZEPHYR_INCLUDE_MPIPE_MPIPE_TRANSFORM_CLIENT_H_ */
```

## 563.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MPIPE_MPIPE_TRANSFORM_CLIENT_H_`。

## 563.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform__client_8h.html)
- [zephyr/mpipe/mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [zephyr/mpipe/mpipe_transform.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h.html)
- [mpipe_transform_client](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md)
- [mpipe_transform](../audio_video_model_reference/P034_mpipe_transform_结构体.md)
- [transform](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md#a8e406cdc0e2c448faf5c6e286779739e)
- [init_rpc](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md#a9d6edb742acdfe64509d0c3fb6567a36)
- [process_fn_rpc](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md#a65c1ee88e4255222e7b1ed93f4c56a58)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mpipe_transform_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__transform.html#ga2b1ea237f62a4cf9731a90e3b5d0eea4)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mpipe_buffer.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__buffer_8h.html)
- [mpipe_transform.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__transform_8h.html)
- [mpipe_transform_client::process_fn_rpc](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md#a65c1ee88e4255222e7b1ed93f4c56a58)
- [mpipe_transform_client::transform](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md#a8e406cdc0e2c448faf5c6e286779739e)
- [mpipe_transform_client::init_rpc](../audio_video_model_reference/P035_mpipe_transform_client_结构体.md#a9d6edb742acdfe64509d0c3fb6567a36)

---

[上一章](P562_mpipe_transform.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P564_mpipe_value.h_源码浏览.md)
