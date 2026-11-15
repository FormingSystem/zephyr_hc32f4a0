---
id: learning.zephyr-docs.api-source-reference.page-278
title: ft8xx_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第278章\_ft8xx\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__common_8h.html)。

## 278.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00021"></a>
<a id="l00028"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__ft8xx__common_html_ga2c8c5d06b09549ab041bbff4612b4620"></a>
<a id="agroup__ft8xx__common_html_ga743c2d25f728451e98417b2ebcc9c722"></a>
<a id="agroup__ft8xx__common_html_gaa6d306b1e2701e0de415c64d33e575a4"></a>
<a id="agroup__ft8xx__common_html_gab8235ed0c0f7373628457fcf64e15fbd"></a>
<a id="agroup__ft8xx__common_html_gada8d996d58f0f46f3f56534ee0da4c68"></a>
<a id="agroup__ft8xx__common_html_gaed670a8410224f8f3970fad86705f513"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2020 Hubert Miś
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_COMMON_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_COMMON_H_

#include <stdint.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


void ft8xx_wr8(const struct device *dev, uint32_t address, uint8_t data);

void ft8xx_wr16(const struct device *dev, uint32_t address, uint16_t data);

void ft8xx_wr32(const struct device *dev, uint32_t address, uint32_t data);

uint8_t ft8xx_rd8(const struct device *dev, uint32_t address);

uint16_t ft8xx_rd16(const struct device *dev, uint32_t address);

uint32_t ft8xx_rd32(const struct device *dev, uint32_t address);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_COMMON_H_ */
```

## 278.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Hubert Miś。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 94 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_COMMON_H_`。

## 278.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__common_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [ft8xx_wr8](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html#ga2c8c5d06b09549ab041bbff4612b4620)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ft8xx_wr16](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html#gaa6d306b1e2701e0de415c64d33e575a4)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [ft8xx_wr32](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html#gada8d996d58f0f46f3f56534ee0da4c68)
- [ft8xx_rd8](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html#gab8235ed0c0f7373628457fcf64e15fbd)
- [ft8xx_rd16](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html#ga743c2d25f728451e98417b2ebcc9c722)
- [ft8xx_rd32](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__common.html#gaed670a8410224f8f3970fad86705f513)
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P277_fs_sys.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P279_ft8xx_copro.h_源码浏览.md)
