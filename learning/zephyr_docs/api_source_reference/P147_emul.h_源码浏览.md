---
id: learning.zephyr-docs.api-source-reference.page-147
title: emul.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2biometrics_2emul_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第147章\_emul.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2biometrics_2emul_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2biometrics_2emul_8h.html)。

## 147.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00032"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="abiometrics_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__biometrics__emulator_html_ga1d019c8b87edc683164eb4fe50dbcecd"></a>
<a id="agroup__biometrics__emulator_html_ga5263531d01ea35ffbc8c7f012f508ab0"></a>
<a id="agroup__biometrics__emulator_html_ga93a3ca46b71f86b6a61078fb0377f684"></a>
<a id="agroup__biometrics__emulator_html_gac3678eaa27b193eb1a50458a657bb79c"></a>
<a id="agroup__biometrics__emulator_html_gac4373b9736267d218e54373fe5a170e7"></a>
<a id="agroup__biometrics__emulator_html_gac7f189217091ebabf3c797edc8510f79"></a>
<a id="agroup__biometrics__interface_html_ga83c3fbd41de6c4f3739880fceadea96f"></a>
<a id="astdbool_8h_html"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2026 Siratul Islam <email@sirat.me>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_BIOMETRICS_EMUL_H_
#define ZEPHYR_INCLUDE_DRIVERS_BIOMETRICS_EMUL_H_

#include <stdbool.h>
#include <zephyr/drivers/biometrics.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


void biometrics_emul_set_match_score(const struct device *dev, int score);

void biometrics_emul_set_match_id(const struct device *dev, int id);

void biometrics_emul_set_match_fail(const struct device *dev, bool fail);

void biometrics_emul_set_capture_timeout(const struct device *dev, bool timeout);

void biometrics_emul_set_image_quality(const struct device *dev, int quality);

enum biometric_led_state biometrics_emul_get_led_state(const struct device *dev);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_BIOMETRICS_EMUL_H_ */
```

## 147.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Siratul Islam <email@sirat.me>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 107 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_BIOMETRICS_EMUL_H_`。

## 147.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2biometrics_2emul_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/drivers/biometrics.h](https://docs.zephyrproject.org/latest/doxygen/html/biometrics_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [biometrics_emul_set_match_score](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#gac3678eaa27b193eb1a50458a657bb79c)
- [device](../device_reference/P002_设备对象结构.md)
- [biometrics_emul_set_match_id](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#gac7f189217091ebabf3c797edc8510f79)
- [biometrics_emul_set_match_fail](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#ga1d019c8b87edc683164eb4fe50dbcecd)
- [biometrics_emul_set_capture_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#ga5263531d01ea35ffbc8c7f012f508ab0)
- [biometrics_emul_set_image_quality](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#gac4373b9736267d218e54373fe5a170e7)
- [biometric_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__interface.html#ga83c3fbd41de6c4f3739880fceadea96f)
- [biometrics_emul_get_led_state](https://docs.zephyrproject.org/latest/doxygen/html/group__biometrics__emulator.html#ga93a3ca46b71f86b6a61078fb0377f684)
- [biometrics.h](https://docs.zephyrproject.org/latest/doxygen/html/biometrics_8h.html)
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P146_dplpmtud.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P148_npm10xx.h_源码浏览.md)
