---
id: learning.zephyr-docs.api-source-supplement-reference.page-163
title: rk3588-cru-reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rk3588-cru-reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第163章\_rk3588-cru-reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rk3588-cru-reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rk3588-cru-reset_8h.html)。

## 163.1\_原始可见代码（Source Code）

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

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2026 KylinSoft Corporation
 * SPDX-License-Identifier: Apache-2.0
 *
 * RK3588 CRU reset identifiers used by the GMAC controllers.
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_RK3588_CRU_RESET_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_RK3588_CRU_RESET_H_

#define SRST_A_GMAC0 522
#define SRST_A_GMAC1 523

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESET_RK3588_CRU_RESET_H_ */
```

## 163.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2026 KylinSoft Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

GMAC 控制器使用的 RK3588 CRU 复位标识符（Reset identifiers）。

### 注释 2：原第 14 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESET_RK3588_CRU_RESET_H_`。

## 163.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rk3588-cru-reset_8h.html)

---

[上一章](P162_renesas_rza2m_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P164_rk3588-cru.h_源码浏览.md)
