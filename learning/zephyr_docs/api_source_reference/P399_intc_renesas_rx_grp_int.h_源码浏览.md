---
id: learning.zephyr-docs.api-source-reference.page-399
title: intc_renesas_rx_grp_int.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intc__renesas__rx__grp__int_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第399章\_intc\_renesas\_rx\_grp\_int.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intc__renesas__rx__grp__int_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intc__renesas__rx__grp__int_8h.html)。

## 399.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="aintc__renesas__rx__grp__int_8h_html_a349020f5fe0ecc410821be66f87367b7"></a>
<a id="aintc__renesas__rx__grp__int_8h_html_a8a63db97f47dd788a268a9651d43347f"></a>
<a id="aintc__renesas__rx__grp__int_8h_html_ae526fa393cc27cfe87467667dff111d6"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RENESAS_RX_GRP_INT_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RENESAS_RX_GRP_INT_H_

#include "platform.h"

int rx_grp_intc_set_grp_int(const struct device *dev, bsp_int_src_t vector, bool set);

int rx_grp_intc_set_gen(const struct device *dev, uint8_t vector_num, bool set);

int rx_grp_intc_set_callback(const struct device *dev, bsp_int_src_t vector, bsp_int_cb_t callback,
                             void *context);

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RENESAS_RX_GRP_INT_H_ */
```

## 399.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 56 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTC_RENESAS_RX_GRP_INT_H_`。

## 399.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intc__renesas__rx__grp__int_8h.html)
- [rx_grp_intc_set_grp_int](https://docs.zephyrproject.org/latest/doxygen/html/intc__renesas__rx__grp__int_8h.html#ae526fa393cc27cfe87467667dff111d6)
- [device](../device_reference/P002_设备对象结构.md)
- [rx_grp_intc_set_gen](https://docs.zephyrproject.org/latest/doxygen/html/intc__renesas__rx__grp__int_8h.html#a8a63db97f47dd788a268a9651d43347f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [rx_grp_intc_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/intc__renesas__rx__grp__int_8h.html#a349020f5fe0ecc410821be66f87367b7)

---

[上一章](P398_intc_nxp_siul2_eirq.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P400_intc_rz_ext_irq.h_源码浏览.md)
