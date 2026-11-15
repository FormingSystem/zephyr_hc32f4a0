---
id: learning.zephyr-docs.api-source-supplement-reference.page-188
title: stm32_dcmipp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32__dcmipp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第188章\_stm32\_dcmipp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dcmipp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dcmipp_8h.html)。

## 188.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astm32__dcmipp_8h_html_a37286ed8041fa5de1840151a3d8c5a74"></a>
<a id="astm32__dcmipp_8h_html_a3f46ac0646bb14656fcb89a7720d171a"></a>
<a id="astm32__dcmipp_8h_html_a74db1fc75808b5d306f56a59539a3cab"></a>
<a id="astm32__dcmipp_8h_html_ac395f951a019d41ec3b72156cd6b5ce5"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2025 STMicroelectronics.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_VIDEO_STM32_DCMIPP_H_
#define ZEPHYR_INCLUDE_VIDEO_STM32_DCMIPP_H_

/* Prototypes of ISP external handler weak functions */
void stm32_dcmipp_isp_vsync_update(DCMIPP_HandleTypeDef *hdcmipp, uint32_t Pipe);
int stm32_dcmipp_isp_init(DCMIPP_HandleTypeDef *hdcmipp, const struct device *source);
int stm32_dcmipp_isp_start(void);
int stm32_dcmipp_isp_stop(void);

#endif /* ZEPHYR_INCLUDE_VIDEO_STM32_DCMIPP_H_ */
```

## 188.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 STMicroelectronics.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

图像信号处理器（ISP）外部处理程序弱函数（Weak functions）的原型。

### 注释 3：原第 16 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_VIDEO_STM32_DCMIPP_H_`。

## 188.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dcmipp_8h.html)
- [stm32_dcmipp_isp_vsync_update](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dcmipp_8h.html#a74db1fc75808b5d306f56a59539a3cab)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [stm32_dcmipp_isp_init](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dcmipp_8h.html#a37286ed8041fa5de1840151a3d8c5a74)
- [device](../device_reference/P002_设备对象结构.md)
- [stm32_dcmipp_isp_start](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dcmipp_8h.html#a3f46ac0646bb14656fcb89a7720d171a)
- [stm32_dcmipp_isp_stop](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dcmipp_8h.html#ac395f951a019d41ec3b72156cd6b5ce5)

---

[上一章](P187_stm32-timer.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P189_stm32_dma.h_源码浏览.md)
