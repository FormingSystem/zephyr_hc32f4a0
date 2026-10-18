---
id: learning.zephyr-docs.api-source-reference.page-420
title: it8xxx2-wuc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-wuc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第420章\_it8xxx2-wuc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-wuc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-wuc_8h.html)。

## 420.1\_原始可见代码（Source Code）

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
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2022 ITE Corporation. All Rights Reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_IT8XXX2_WUC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_IT8XXX2_WUC_H_

#include <zephyr/dt-bindings/dt-util.h>


#define IT8XXX2_WUC_UNUSED_REG  0

#define WUC_TYPE_EDGE_RISING    BIT(0)
#define WUC_TYPE_EDGE_FALLING   BIT(1)
#define WUC_TYPE_EDGE_BOTH      (WUC_TYPE_EDGE_RISING | WUC_TYPE_EDGE_FALLING)



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_IT8XXX2_WUC_H_ */
```

## 420.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 ITE Corporation. All Rights Reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 55 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_IT8XXX2_WUC_H_`。

## 420.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/it8xxx2-wuc_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P419_it8xxx2-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P421_it8xxx2_tach.h_源码浏览.md)
