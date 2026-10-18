---
id: learning.zephyr-docs.api-source-reference.page-151
title: console.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2console_2console_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第151章\_console.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2console_2console_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2console_2console_8h.html)。

## 151.1\_原始可见代码（Source Code）

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
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="foldopen00021"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="adrivers_2console_2console_8h_html_a0dab6d89950bb4c2bbb17571b9b1461f"></a>
<a id="adrivers_2console_2console_8h_html_ae5aa23edbc2609d1b766340c14fd5a68"></a>
<a id="astdint_8h_html_a0bd5dec00e345e69027427f8621d6a6c"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructconsole__input_html"></a>
<a id="astructconsole__input_html_a2c13a1e2a4895cf1d51c8ce7879af927"></a>
<a id="astructconsole__input_html_a33bf8ba6d114ec99219c134c0f6c3474"></a>
<a id="astructk__fifo_html"></a>

```c
/*
 * Copyright (c) 2017 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_CONSOLE_CONSOLE_H_
#define ZEPHYR_INCLUDE_DRIVERS_CONSOLE_CONSOLE_H_

#ifdef __cplusplus
extern "C" {
#endif

#define CONSOLE_MAX_LINE_LEN CONFIG_CONSOLE_INPUT_MAX_LINE_LEN

struct console_input {
        intptr_t _unused;
        uint8_t is_mcumgr : 1;
        char line[CONSOLE_MAX_LINE_LEN];
};

typedef void (*console_input_fn)(struct k_fifo *avail, struct k_fifo *lines,
                                 uint8_t (*completion)(char *str, uint8_t len));

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_CONSOLE_CONSOLE_H_ */
```

## 151.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 49 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CONSOLE_CONSOLE_H_`。

## 151.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2console_2console_8h.html)
- [console_input](../system_service_model_reference/P005_console_input_结构体.md)
- [intptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0bd5dec00e345e69027427f8621d6a6c)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [is_mcumgr](../system_service_model_reference/P005_console_input_结构体.md#a2c13a1e2a4895cf1d51c8ce7879af927)
- [line](../system_service_model_reference/P005_console_input_结构体.md#a33bf8ba6d114ec99219c134c0f6c3474)
- [CONSOLE_MAX_LINE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2console_2console_8h.html#ae5aa23edbc2609d1b766340c14fd5a68)
- [console_input_fn](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2console_2console_8h.html#a0dab6d89950bb4c2bbb17571b9b1461f)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [console_input::is_mcumgr](../system_service_model_reference/P005_console_input_结构体.md#a2c13a1e2a4895cf1d51c8ce7879af927)
- [console_input::line](../system_service_model_reference/P005_console_input_结构体.md#a33bf8ba6d114ec99219c134c0f6c3474)

---

[上一章](P150_renesas_cpg_mssr.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P152_crc.h_源码浏览.md)
