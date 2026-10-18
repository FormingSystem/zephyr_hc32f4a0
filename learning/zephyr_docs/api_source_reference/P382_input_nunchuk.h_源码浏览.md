---
id: learning.zephyr-docs.api-source-reference.page-382
title: input_nunchuk.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__nunchuk_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第382章\_input\_nunchuk.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/input__nunchuk_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/input__nunchuk_8h.html)。

## 382.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00027"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__nunchuk__interface_html_ga481650458998947e79ee89fbf1402435"></a>
<a id="astructdevice_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_INPUT_INPUT_NUNCHUK_H_
#define ZEPHYR_INCLUDE_INPUT_INPUT_NUNCHUK_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/device.h>


#define INPUT_NUNCHUK_ACCEL_X 0

#define INPUT_NUNCHUK_ACCEL_Y 1

#define INPUT_NUNCHUK_ACCEL_Z 2

int nunchuk_read(const struct device *dev);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_INPUT_INPUT_NUNCHUK_H_ */
```

## 382.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 71 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_INPUT_INPUT_NUNCHUK_H_`。

## 382.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/input__nunchuk_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [nunchuk_read](https://docs.zephyrproject.org/latest/doxygen/html/group__nunchuk__interface.html#ga481650458998947e79ee89fbf1402435)
- [device](../device_reference/P002_设备对象结构.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P381_input_keymap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P383_input_pat912x.h_源码浏览.md)
