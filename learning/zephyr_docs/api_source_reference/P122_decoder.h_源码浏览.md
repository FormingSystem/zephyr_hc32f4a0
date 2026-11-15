---
id: learning.zephyr-docs.api-source-reference.page-122
title: decoder.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/decoder_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第122章\_decoder.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/decoder_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/decoder_8h.html)。

## 122.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="adecoder_8h_html_a036ac8162086665053e5ea7deaa48a93"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

```c
/*
 * Copyright (c) 2025 Croxel Inc.
 * Copyright (c) 2025 CogniPilot Foundation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_GNSS_RTK_DECODER_H_
#define ZEPHYR_INCLUDE_GNSS_RTK_DECODER_H_

#include <stdint.h>
#include <stddef.h>

int gnss_rtk_decoder_frame_get(uint8_t *buf, size_t buf_len,
                               uint8_t **data, size_t *data_len);

#endif /* ZEPHYR_INCLUDE_GNSS_RTK_DECODER_H_ */
```

## 122.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Croxel Inc.。

版权（Copyright）：© 2025 CogniPilot Foundation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 31 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_GNSS_RTK_DECODER_H_`。

## 122.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/decoder_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [gnss_rtk_decoder_frame_get](https://docs.zephyrproject.org/latest/doxygen/html/decoder_8h.html#a036ac8162086665053e5ea7deaa48a93)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

---

[上一章](P121_data.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P123_device_runtime.h_源码浏览.md)
