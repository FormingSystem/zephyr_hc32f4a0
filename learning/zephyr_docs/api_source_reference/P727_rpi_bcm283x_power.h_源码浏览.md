---
id: learning.zephyr-docs.api-source-reference.page-727
title: rpi_bcm283x_power.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpi__bcm283x__power_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第727章\_rpi\_bcm283x\_power.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rpi__bcm283x__power_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rpi__bcm283x__power_8h.html)。

## 727.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>

```c
/*
 * Copyright (c) 2026 Muhammad Waleed Badar
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_POWER_RPI_BCM283X_POWER__H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_POWER_RPI_BCM283X_POWER__H_

#define RPI_POWER_DOMAIN_SD_CARD  0x00000000U
#define RPI_POWER_DOMAIN_UART0    0x00000001U
#define RPI_POWER_DOMAIN_UART1    0x00000002U
#define RPI_POWER_DOMAIN_USB_HCD  0x00000003U
#define RPI_POWER_DOMAIN_I2C0     0x00000004U
#define RPI_POWER_DOMAIN_I2C1     0x00000005U
#define RPI_POWER_DOMAIN_I2C2     0x00000006U
#define RPI_POWER_DOMAIN_SPI      0x00000007U
#define RPI_POWER_DOMAIN_CCP2TX   0x00000008U
#define RPI_POWER_DOMAIN_UNKNOWN0 0x00000009U
#define RPI_POWER_DOMAIN_UNKNOWN1 0x0000000AU

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_POWER_RPI_BCM283X_POWER__H_ */
```

## 727.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Muhammad Waleed Badar。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 46 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_POWER_RPI_BCM283X_POWER__H_`。

## 727.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rpi__bcm283x__power_8h.html)

---

[上一章](P726_rpi-pico-rp2350-pinctrl-common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P728_rpi_pico.h_源码浏览.md)
