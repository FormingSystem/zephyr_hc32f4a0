---
id: learning.zephyr-docs.api-source-reference.page-694
title: ra_flash_api_extensions.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ra__flash__api__extensions_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第694章\_ra\_flash\_api\_extensions.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ra__flash__api__extensions_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ra__flash__api__extensions_8h.html)。

## 694.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="aflash_8h_html"></a>
<a id="agroup__ra__flash__ex__op_html_ga00ad044f5928882300e87ff9a13c1f74"></a>
<a id="agroup__ra__flash__ex__op_html_gga00ad044f5928882300e87ff9a13c1f74ab955683b469ec4f2d77f202896ccad3b"></a>

```c
/*
 * Copyright (c) 2024-2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FLASH_RA_FLASH_API_EXTENSIONS_H_
#define ZEPHYR_INCLUDE_DRIVERS_FLASH_RA_FLASH_API_EXTENSIONS_H_


#include <zephyr/drivers/flash.h>

enum ra_ex_ops {
        QSPI_FLASH_EX_OP_EXIT_QPI = 1,
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_FLASH_RA_FLASH_API_EXTENSIONS_H_ */
```

## 694.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024-2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 39 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FLASH_RA_FLASH_API_EXTENSIONS_H_`。

## 694.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ra__flash__api__extensions_8h.html)
- [zephyr/drivers/flash.h](../flash_reference/P009_Flash公共头文件参考.md)
- [ra_ex_ops](https://docs.zephyrproject.org/latest/doxygen/html/group__ra__flash__ex__op.html#ga00ad044f5928882300e87ff9a13c1f74)
- [QSPI_FLASH_EX_OP_EXIT_QPI](https://docs.zephyrproject.org/latest/doxygen/html/group__ra__flash__ex__op.html#gga00ad044f5928882300e87ff9a13c1f74ab955683b469ec4f2d77f202896ccad3b)
- [flash.h](../flash_reference/P009_Flash公共头文件参考.md)

---

[上一章](P693_ra_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P695_raspberrypi-csi-connector.h_源码浏览.md)
