---
id: learning.zephyr-docs.api-source-reference.page-263
title: fido2_up.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fido2__up_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第263章\_fido2\_up.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fido2__up_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fido2__up_8h.html)。

## 263.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="agroup__fido2_html_gab782d78847a38dd7aeac52a806879dfb"></a>
<a id="agroup__fido2_html_gae7fb0da6d327ef0be220d32558ea6be2"></a>
<a id="agroup__fido2_html_gaf6d50aa0022f56350a927149086d7838"></a>
<a id="akernel_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Siratul Islam <email@sirat.me>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_UP_H_
#define ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_UP_H_

#include <zephyr/kernel.h>


#ifdef __cplusplus
extern "C" {
#endif

int fido2_up_wait(void);

void fido2_up_reset(void);

void fido2_up_cancel(void);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_UP_H_ */
```

## 263.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Siratul Islam <email@sirat.me>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 64 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_AUTHENTICATION_FIDO2_FIDO2_UP_H_`。

## 263.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fido2__up_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [fido2_up_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gab782d78847a38dd7aeac52a806879dfb)
- [fido2_up_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gae7fb0da6d327ef0be220d32558ea6be2)
- [fido2_up_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaf6d50aa0022f56350a927149086d7838)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P262_fido2_types.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P264_flash_img.h_源码浏览.md)
