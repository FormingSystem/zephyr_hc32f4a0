---
id: learning.zephyr-docs.api-source-reference.page-289
title: generic_emul.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/generic__emul_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第289章\_generic\_emul.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/generic__emul_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/generic__emul_8h.html)。

## 289.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2emul_8h_html"></a>
<a id="agroup__generic__emul_html_gaa46e3a3f212fabb397347cacece3325c"></a>
<a id="agroup__generic__emul_html_gadaae3d98d7e56858b882319b26990803"></a>
<a id="astructemul_html"></a>

```c
/*
 * Copyright (c) 2026 Embeint Inc
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_GENERIC_EMUL_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_GENERIC_EMUL_H_

#include <zephyr/device.h>
#include <zephyr/drivers/emul.h>


#ifdef __cplusplus
extern "C" {
#endif

void generic_emul_reset(const struct emul *target, bool reset_rc);

void generic_emul_func_rc(const struct emul *target, int resume_rc, int suspend_rc, int fetch_rc);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_GENERIC_EMUL_H_ */
```

## 289.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Embeint Inc。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 56 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_GENERIC_EMUL_H_`。

## 289.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/generic__emul_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [generic_emul_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__generic__emul.html#gaa46e3a3f212fabb397347cacece3325c)
- [emul](../hardware/P477_仿真器实例结构.md)
- [generic_emul_func_rc](https://docs.zephyrproject.org/latest/doxygen/html/group__generic__emul.html#gadaae3d98d7e56858b882319b26990803)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)

---

[上一章](P288_gd32_exti.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P290_gicv3_its.h_源码浏览.md)
