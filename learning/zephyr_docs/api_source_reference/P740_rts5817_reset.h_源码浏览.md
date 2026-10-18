---
id: learning.zephyr-docs.api-source-reference.page-740
title: rts5817_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rts5817__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第740章\_rts5817\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__reset_8h.html)。

## 740.1\_原始可见代码（Source Code）

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
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>

```c
/*
 * Copyright (c) 2025 Realtek Semiconductor, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_RTS5817_RESET_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_RTS5817_RESET_H_

#define SYS_FORCE_RST_BUS       0
#define SYS_FORCE_RST_AES       1
#define SYS_FORCE_RST_GE        2
#define SYS_FORCE_RST_SHA       3
#define SYS_FORCE_RST_SPI_CACHE 4
#define SYS_FORCE_RST_SPI_SSOR  5
#define SYS_FORCE_RST_SPI_SSI_M 6
#define SYS_FORCE_RST_SPI_SSI_S 7
#define SYS_FORCE_RST_PKE       8
#define SYS_FORCE_RST_I2C       9
#define SYS_FORCE_RST_I2C0      10
#define SYS_FORCE_RST_I2C1      11
#define SYS_FORCE_RST_TRNG      12
#define SYS_FORCE_RST_I2C_S     13
#define SYS_FORCE_RST_UART0     14
#define SYS_FORCE_RST_UART1     15
#define SYS_FORCE_RST_PUF       16
#define SYS_FORCE_RST_USB2      17
#define SYS_FORCE_RST_CK30M     18
#define SYS_FORCE_RST_CK60M     19
#define SYS_FORCE_RST_CK120M    20
#define SYS_FORCE_RST_USB2_PHY  21
#define SYS_FORCE_RST_SYS       22
#define SYS_FORCE_RST_DPHY      23
#define SYS_FORCE_RST_SSI_S_BUS 24

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESET_RTS5817_RESET_H_ */
```

## 740.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Realtek Semiconductor, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 36 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESET_RTS5817_RESET_H_`。

## 740.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__reset_8h.html)

---

[上一章](P739_rts5817_pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P741_rts5912_flash_api_ex.h_源码浏览.md)
