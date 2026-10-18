---
id: learning.zephyr-docs.api-source-reference.page-265
title: flask.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/flask_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第265章\_flask.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/flask_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/flask_8h.html)。

## 265.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00026"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="agroup__xen__xsm__flask_html_gaf7c884e01c7a9bb55c248c53d9b848eb"></a>
<a id="agroup__xen__xsm__flask_html_gafedcdbff09ea3a91952aa011954bcae3"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 EPAM Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */



#ifndef ZEPHYR_XEN_FLASK_H_
#define ZEPHYR_XEN_FLASK_H_

#include <xen/public/xsm/flask_op.h>


int flask_context_to_sid(char *buf, uint32_t size, uint32_t *sid);

int flask_getenforce(void);


#endif /* ZEPHYR_XEN_FLASK_H_ */
```

## 265.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 EPAM Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 60 行

头文件保护宏（Header guard）标记：`ZEPHYR_XEN_FLASK_H_`。

## 265.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/flask_8h.html)
- [flask_context_to_sid](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__xsm__flask.html#gafedcdbff09ea3a91952aa011954bcae3)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flask_getenforce](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__xsm__flask.html#gaf7c884e01c7a9bb55c248c53d9b848eb)

---

[上一章](P264_flash_img.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P266_focaltech_ft9001_clocks.h_源码浏览.md)
