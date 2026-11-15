---
id: learning.zephyr-docs.api-source-reference.page-850
title: syna_sr100_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/syna__sr100__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第850章\_syna\_sr100\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/syna__sr100__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/syna__sr100__reset_8h.html)。

## 850.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00061"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Synaptics, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_SYNA_SR100_RESET_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_SYNA_SR100_RESET_H_

#include <zephyr/sys/util_macro.h>

#define IMGPROC_RST   0x20
#define NPU_RST       0x30
#define DMA0_RST      0x40
#define DMA1_RST      0x48
#define AXI_RST       0x50
#define APB_PERIF_RST 0x8C
#define PERIF_RST     0x80

#define TOP_STICKY_RST 0x58
#define PER_STICKY_RST 0x88

#define STI_REG  24
#define STI_MASK 21
#define STI_BIT  16
#define RST_REG  8
#define RST_MASK 5
#define RST_BIT  0

#define SYNA_IMGPRC_RST                                                                            \
        ((TOP_STICKY_RST << STI_REG) | (1 << STI_BIT) | (IMGPROC_RST << RST_REG) | (0 << RST_BIT))

#define SYNA_NPU_RST                                                                               \
        ((TOP_STICKY_RST << STI_REG) | (0 << STI_BIT) | (NPU_RST << RST_REG) | (0 << RST_BIT))

#define SYNA_DMA0_RST                                                                              \
        ((TOP_STICKY_RST << STI_REG) | (2 << STI_BIT) | (DMA0_RST << RST_REG) | (0 << RST_BIT))

#define SYNA_DMA1_RST                                                                              \
        ((TOP_STICKY_RST << STI_REG) | (5 << STI_BIT) | (DMA1_RST << RST_REG) | (0 << RST_BIT))

#define SYNA_AXI_RST   ((AXI_RST << RST_REG) | (0 << RST_BIT))
#define SYNA_OTP_RST   ((TOP_STICKY_RST << STI_REG) | (3 << STI_BIT))
#define SYNA_CALIB_RST ((TOP_STICKY_RST << STI_REG) | (6 << STI_BIT))
#define SYNA_USB_RST                                                                               \
        ((PER_STICKY_RST << STI_REG) | (0 << STI_BIT) | (7 << STI_MASK) | (PERIF_RST << RST_REG) | \
         (4 << RST_BIT))

#define SYNA_UART0_RST ((APB_PERIF_RST << RST_REG) | (0 << RST_BIT))
#define SYNA_UART1_RST ((APB_PERIF_RST << RST_REG) | (1 << RST_BIT))
#define SYNA_I2C0M_RST ((APB_PERIF_RST << RST_REG) | (2 << RST_BIT))
#define SYNA_I2C1M_RST ((APB_PERIF_RST << RST_REG) | (3 << RST_BIT))
#define SYNA_I2CS_RST  ((APB_PERIF_RST << RST_REG) | (4 << RST_BIT))
#define SYNA_I3C0_RST  ((APB_PERIF_RST << RST_REG) | (5 << RST_BIT))
#define SYNA_I3C1_RST  ((APB_PERIF_RST << RST_REG) | (6 << RST_BIT))
#define SYNA_SPIM_RST  ((APB_PERIF_RST << RST_REG) | (7 << RST_BIT))
#define SYNA_SPIS_RST  ((APB_PERIF_RST << RST_REG) | (8 << RST_BIT))
#define SYNA_GPIO_RST  ((APB_PERIF_RST << RST_REG) | (9 << RST_BIT))
#define SYNA_SWIRE_RST ((APB_PERIF_RST << RST_REG) | (19 << RST_BIT))
#define SYNA_SD0_RST   ((PERIF_RST << RST_REG) | (2 << RST_BIT))
#define SYNA_SD1_RST   ((PERIF_RST << RST_REG) | (3 << RST_BIT))
#define SYNA_XSPI_RST  ((PERIF_RST << RST_REG) | (5 << RST_BIT))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESET_SYNA_SR100_RESET_H_ */
```

## 850.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Synaptics, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 105 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESET_SYNA_SR100_RESET_H_`。

## 850.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/syna__sr100__reset_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P849_syna_sr100_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P851_dirent.h_源码浏览.md)
