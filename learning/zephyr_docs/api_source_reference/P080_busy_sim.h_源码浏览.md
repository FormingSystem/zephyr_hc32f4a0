---
id: learning.zephyr-docs.api-source-reference.page-80
title: busy_sim.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/busy__sim_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第80章\_busy\_sim.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/busy__sim_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/busy__sim_8h.html)。

## 80.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="abusy__sim_8h_html_a2bb7c55b7e21ee9e5f927fcecd758705"></a>
<a id="abusy__sim_8h_html_a6b09e8372800e740a653f45f10a3501f"></a>
<a id="abusy__sim_8h_html_ae7f199942b18363936dcb11fca8d0c96"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef BUSY_SIM_H__
#define BUSY_SIM_H__

typedef void (*busy_sim_cb_t)(void);

void busy_sim_start(uint32_t active_avg, uint32_t active_delta,
                    uint32_t idle_avg, uint32_t idle_delta, busy_sim_cb_t cb);

void busy_sim_stop(void);

#endif /* BUSY_SIM_H__ */
```

## 80.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 38 行

头文件保护宏（Header guard）标记：`BUSY_SIM_H__`。

## 80.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/busy__sim_8h.html)
- [busy_sim_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/busy__sim_8h.html#a6b09e8372800e740a653f45f10a3501f)
- [busy_sim_start](https://docs.zephyrproject.org/latest/doxygen/html/busy__sim_8h.html#a2bb7c55b7e21ee9e5f927fcecd758705)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [busy_sim_stop](https://docs.zephyrproject.org/latest/doxygen/html/busy__sim_8h.html#ae7f199942b18363936dcb11fca8d0c96)

---

[上一章](P079_buf_loader.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P081_buzzer.h_源码浏览.md)
