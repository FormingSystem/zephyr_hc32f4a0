---
id: learning.zephyr-docs.api-source-reference.page-519
title: mfd_maxq10xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mfd__maxq10xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第519章\_mfd\_maxq10xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mfd__maxq10xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mfd__maxq10xx_8h.html)。

## 519.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="adevice_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amfd__maxq10xx_8h_html_afab2fb34feb7d84e42caea6021dd1ed9"></a>
<a id="astructdevice_html"></a>
<a id="astructk__sem_html"></a>

```c
/*
 * Copyright (c) 2025 Vogl Electronic GmbH
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_MFD_MAXQ10XX_H_
#define ZEPHYR_INCLUDE_DRIVERS_MFD_MAXQ10XX_H_

#include <zephyr/device.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif

struct k_sem *mfd_maxq10xx_get_lock(const struct device *dev);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MFD_MAXQ10XX_H_ */
```

## 519.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Vogl Electronic GmbH。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 31 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MFD_MAXQ10XX_H_`。

## 519.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mfd__maxq10xx_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [mfd_maxq10xx_get_lock](https://docs.zephyrproject.org/latest/doxygen/html/mfd__maxq10xx_8h.html#afab2fb34feb7d84e42caea6021dd1ed9)
- [device](../device_reference/P002_设备对象结构.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P518_mfd_it8801_altctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P520_mfd_mchp_sam_flexcom.h_源码浏览.md)
