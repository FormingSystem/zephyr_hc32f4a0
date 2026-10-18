---
id: learning.zephyr-docs.api-source-reference.page-254
title: fake_comp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fake__comp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第254章\_fake\_comp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fake__comp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fake__comp_8h.html)。

## 254.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="acomparator_8h_html"></a>
<a id="agroup__comparator__fake_html_ga013745edeee1a931088f6f9e336e92a6"></a>
<a id="agroup__comparator__fake_html_ga0e6a3ea88289165a28f9b3abd051f281"></a>
<a id="agroup__comparator__fake_html_ga3cdbc9e3140c8e3b92fa328bd0917787"></a>
<a id="agroup__comparator__fake_html_ga59ca6b865fe755dfdfc632ede9710f2e"></a>
<a id="agroup__comparator__interface_html_ga409308b8ba2efdca4a6ec4bdc4d3bc31"></a>
<a id="agroup__comparator__interface_html_gab02743771baf02ee0105aa1303931674"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_COMPARATOR_FAKE_H_
#define ZEPHYR_INCLUDE_DRIVERS_COMPARATOR_FAKE_H_

#include <zephyr/drivers/comparator.h>
#include <zephyr/fff.h>

#ifdef __cplusplus
extern "C" {
#endif


DECLARE_FAKE_VALUE_FUNC(int,
                        comp_fake_comp_get_output,
                        const struct device *);

DECLARE_FAKE_VALUE_FUNC(int,
                        comp_fake_comp_set_trigger,
                        const struct device *,
                        enum comparator_trigger);

DECLARE_FAKE_VALUE_FUNC(int,
                        comp_fake_comp_set_trigger_callback,
                        const struct device *,
                        comparator_callback_t,
                        void *);

DECLARE_FAKE_VALUE_FUNC(int,
                        comp_fake_comp_trigger_is_pending,
                        const struct device *);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_COMPARATOR_FAKE_H_ */
```

## 254.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 75 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_COMPARATOR_FAKE_H_`。

## 254.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fake__comp_8h.html)
- [zephyr/drivers/comparator.h](../analog_reference/P001_比较器公共头文件参考.md)
- [comp_fake_comp_get_output](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html#ga013745edeee1a931088f6f9e336e92a6)
- [device](../device_reference/P002_设备对象结构.md)
- [comp_fake_comp_set_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html#ga59ca6b865fe755dfdfc632ede9710f2e)
- [comparator_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__interface.html#gab02743771baf02ee0105aa1303931674)
- [comp_fake_comp_set_trigger_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html#ga0e6a3ea88289165a28f9b3abd051f281)
- [comparator_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__interface.html#ga409308b8ba2efdca4a6ec4bdc4d3bc31)
- [comp_fake_comp_trigger_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/group__comparator__fake.html#ga3cdbc9e3140c8e3b92fa328bd0917787)
- [comparator.h](../analog_reference/P001_比较器公共头文件参考.md)

---

[上一章](P253_fake.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P255_fcntl.h_源码浏览.md)
