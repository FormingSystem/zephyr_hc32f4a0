---
id: learning.zephyr-docs.api-source-reference.page-849
title: syna_sr100_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/syna__sr100__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第849章\_syna\_sr100\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/syna__sr100__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/syna__sr100__clock_8h.html)。

## 849.1\_原始可见代码（Source Code）

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
<a id="l00017"></a>
<a id="l00019"></a>
<a id="l00021"></a>
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
<a id="l00042"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>

```c
/*
 * Copyright (c) 2025 Synaptics, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SYNA_SR100_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SYNA_SR100_CLOCK_H_

#define XSPI_CORE_CLK_CTRL      0x30
#define SD0_CORE_CLK_CTRL       0x38
#define SD1_CORE_CLK_CTRL       0x3c
#define SPI_MSTR_SSI_CLK_CTRL   0x40
#define SPI_SLV_SSI_CLK_CTRL    0x44
#define I3C0_CORE_CLK_CTRL      0x48
#define I3C1_CORE_CLK_CTRL      0x4c
#define UART0_CORE_CLK_CTRL     0x50
#define UART1_CORE_CLK_CTRL     0x54
#define I2C0_MSTR_CORE_CLK_CTRL 0x58
#define I2C1_MSTR_CORE_CLK_CTRL 0x5c
#define I2C_SLV_CORE_CLK_CTRL   0x60
#define USB2_CORE_CLK_CTRL      0x64

#define CGL_REG 16
#define AXI_ID  8

#define SYNA_IMG_CAM_CLK 0
#define SYNA_GPIO_DB_CLK 1
#define SYNA_AXI_CLK     2
#define SYNA_NPU_CLK     3
#define SYNA_DMA0_CLK    4
#define SYNA_IMG_SYS_CLK 9
#define SYNA_IMG_CFG_CLK 10
#define SYNA_IMG_APB_CLK 11
#define SYNA_DMA1_CLK    12
#define SYNA_PVT_APB_CLK 13

#define SYNA_XSPI_CLK      ((XSPI_CORE_CLK_CTRL << CGL_REG) | (7 << AXI_ID) | 32)
#define SYNA_USB_CLK       ((USB2_CORE_CLK_CTRL << CGL_REG) | (8 << AXI_ID) | 35)
#define SYNA_SD0_CLK       ((SD0_CORE_CLK_CTRL << CGL_REG) | (5 << AXI_ID) | 33)
#define SYNA_SD1_CLK       ((SD1_CORE_CLK_CTRL << CGL_REG) | (6 << AXI_ID) | 34)
#define SYNA_SPI_MSTR_CLK  ((SPI_MSTR_SSI_CLK_CTRL << CGL_REG) | 36)
#define SYNA_SPI_SLV_CLK   ((SPI_SLV_SSI_CLK_CTRL << CGL_REG) | 37)
#define SYNA_I3C0_CLK      ((I3C0_CORE_CLK_CTRL << CGL_REG) | 38)
#define SYNA_I3C1_CLK      ((I3C1_CORE_CLK_CTRL << CGL_REG) | 39)
#define SYNA_UART0_CLK     ((UART0_CORE_CLK_CTRL << CGL_REG) | 40)
#define SYNA_UART1_CLK     ((UART1_CORE_CLK_CTRL << CGL_REG) | 41)
#define SYNA_I2C0_MSTR_CLK ((I2C0_MSTR_CORE_CLK_CTRL << CGL_REG) | 42)
#define SYNA_I2C1_MSTR_CLK ((I2C1_MSTR_CORE_CLK_CTRL << CGL_REG) | 43)
#define SYNA_I2C_SLV_CLK   ((I2C_SLV_CORE_CLK_CTRL << CGL_REG) | 44)

#define SYNA_GPIO_CFG_CLK      45
#define SYNA_I2S_CFG_CLK       46
#define SYNA_I2S_TX0_PCLK      47
#define SYNA_I2S_TX1_PCLK      48
#define SYNA_I2S_TX2_PCLK      49
#define SYNA_I2S_TX3_PCLK      50
#define SYNA_I2S_RX0_PCLK      51
#define SYNA_I2S_RX1_PCLK      52
#define SYNA_I2S_RX2_PCLK      53
#define SYNA_I2S_RX3_PCLK      54
#define SYNA_I2S_SWIRE_CFG_CLK 55

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SYNA_SR100_CLOCK_H_ */
```

## 849.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Synaptics, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 121 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SYNA_SR100_CLOCK_H_`。

## 849.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/syna__sr100__clock_8h.html)

---

[上一章](P848_syna-sr100-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P850_syna_sr100_reset.h_源码浏览.md)
