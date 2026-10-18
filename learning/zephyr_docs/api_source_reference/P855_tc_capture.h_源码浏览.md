---
id: learning.zephyr-docs.api-source-reference.page-855
title: tc_capture.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tc__capture_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第855章\_tc\_capture.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tc__capture_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tc__capture_8h.html)。

## 855.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="astdbool_8h_html"></a>
<a id="atc__capture_8h_html_ac2625e49dd53df7deec771032bcce292"></a>
<a id="atc__capture_8h_html_acf7be87c335c18979f438fd944d31f17"></a>
<a id="atc__capture_8h_html_ad98361ae538dba0ba74614de75d951bb"></a>
<a id="atc__capture_8h_html_ae4d70b8a2ff709bed3a955b1b9ed612d"></a>
<a id="atc__capture_8h_html_afd40b7a2fc58f3e27c03fe3eae59a582"></a>

```c
/*
 * Copyright (c) 2020 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_TESTSUITE_TC_CAPTURE_H_
#define ZEPHYR_TESTSUITE_TC_CAPTURE_H_

#include <stdbool.h>
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

void tc_capture_start(void);

void tc_capture_stop(void);

bool tc_capture_contains(const char *substr);

size_t tc_capture_get(char *dst, size_t size);

void tc_capture_clear(void);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_TESTSUITE_TC_CAPTURE_H_ */
```

## 855.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 97 行

头文件保护宏（Header guard）标记：`ZEPHYR_TESTSUITE_TC_CAPTURE_H_`。

## 855.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tc__capture_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [tc_capture_start](https://docs.zephyrproject.org/latest/doxygen/html/tc__capture_8h.html#ad98361ae538dba0ba74614de75d951bb)
- [tc_capture_stop](https://docs.zephyrproject.org/latest/doxygen/html/tc__capture_8h.html#ac2625e49dd53df7deec771032bcce292)
- [tc_capture_contains](https://docs.zephyrproject.org/latest/doxygen/html/tc__capture_8h.html#ae4d70b8a2ff709bed3a955b1b9ed612d)
- [tc_capture_get](https://docs.zephyrproject.org/latest/doxygen/html/tc__capture_8h.html#acf7be87c335c18979f438fd944d31f17)
- [tc_capture_clear](https://docs.zephyrproject.org/latest/doxygen/html/tc__capture_8h.html#afd40b7a2fc58f3e27c03fe3eae59a582)

---

[上一章](P854_target_device.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P856_tcp.h_源码浏览.md)
