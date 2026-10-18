---
id: learning.zephyr-docs.api-source-device-reference.page-56
title: winstream.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/winstream_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_winstream.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/winstream_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/winstream_8h.html)。

## 56.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="foldopen00025"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructsys__winstream_html"></a>
<a id="astructsys__winstream_html_a1cc84dfd9f812b3491135d13365c7a98"></a>
<a id="astructsys__winstream_html_a30b03df76a51ecbf0cbe33975d5aaa66"></a>
<a id="astructsys__winstream_html_a341203116bfee52d4b801466097fc3eb"></a>
<a id="astructsys__winstream_html_a6b80cf715e4a3ca7b7b74b9efd150a23"></a>
<a id="astructsys__winstream_html_a7d946d6a54652a8ac035dd8cd0ba861a"></a>
<a id="awinstream_8h_html_a55dc3b77ec21e6d799aa951e327dc392"></a>
<a id="awinstream_8h_html_acc72f0f65bd88e8f2b630a3832006f9c"></a>
<a id="awinstream_8h_html_ae8686be598c081858322378c8e4368cb"></a>

```c
/*
 * Copyright (c) 2021 Intel Corporation
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_SYS_WINSTREAM_H_
#define ZEPHYR_INCLUDE_SYS_WINSTREAM_H_

#include <stdint.h>

struct sys_winstream {
        uint32_t len;   /* Length of data[] in bytes */
        uint32_t start; /* Index of first valid byte in data[] */
        uint32_t end;   /* Index of next byte in data[] to write */
        uint32_t seq;   /* Mod-2^32 index of 'end' since stream init */
        uint8_t data[];
};

static inline struct sys_winstream *sys_winstream_init(void *buf, int buflen)
{
        struct sys_winstream *ws = buf, tmp = { .len = buflen - sizeof(*ws) };

        *ws = tmp;
        return ws;
}

void sys_winstream_write(struct sys_winstream *ws,
                         const char *data, uint32_t len);

uint32_t sys_winstream_read(struct sys_winstream *ws,
                            uint32_t *seq, char *buf, uint32_t buflen);

#endif /* ZEPHYR_INCLUDE_SYS_WINSTREAM_H_ */
```

## 56.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 26 行

`data[]` 的长度（Length），单位为字节（Bytes）。

### 注释 3：原第 27 行

`data[]` 中第一个有效字节的索引（Index）。

### 注释 4：原第 28 行

`data[]` 中下一个待写入字节的索引（Index）。

### 注释 5：原第 29 行

从流初始化（Stream Init）起计算的 `end` 索引，对 `2^32` 取模（Mod-2^32）。

### 注释 6：原第 95 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SYS_WINSTREAM_H_`。

## 56.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/winstream_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [sys_winstream](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [len](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md#a30b03df76a51ecbf0cbe33975d5aaa66)
- [start](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md#a1cc84dfd9f812b3491135d13365c7a98)
- [end](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md#a6b80cf715e4a3ca7b7b74b9efd150a23)
- [seq](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md#a7d946d6a54652a8ac035dd8cd0ba861a)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md#a341203116bfee52d4b801466097fc3eb)
- [sys_winstream_init](https://docs.zephyrproject.org/latest/doxygen/html/winstream_8h.html#acc72f0f65bd88e8f2b630a3832006f9c)
- [sys_winstream_write](https://docs.zephyrproject.org/latest/doxygen/html/winstream_8h.html#ae8686be598c081858322378c8e4368cb)
- [sys_winstream_read](https://docs.zephyrproject.org/latest/doxygen/html/winstream_8h.html#a55dc3b77ec21e6d799aa951e327dc392)
- [sys_winstream::start](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md#a1cc84dfd9f812b3491135d13365c7a98)
- [sys_winstream::len](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md#a30b03df76a51ecbf0cbe33975d5aaa66)
- [sys_winstream::data](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md#a341203116bfee52d4b801466097fc3eb)
- [sys_winstream::end](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md#a6b80cf715e4a3ca7b7b74b9efd150a23)
- [sys_winstream::seq](../kernel_runtime_model_reference/P019_sys_winstream_结构体.md#a7d946d6a54652a8ac035dd8cd0ba861a)

---

[上一章](P055_virtual.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P057_ztest_assert.h_源码浏览.md)
