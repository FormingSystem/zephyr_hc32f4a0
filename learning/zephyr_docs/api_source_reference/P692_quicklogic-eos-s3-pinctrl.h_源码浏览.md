---
id: learning.zephyr-docs.api-source-reference.page-692
title: quicklogic-eos-s3-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/quicklogic-eos-s3-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第692章\_quicklogic-eos-s3-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/quicklogic-eos-s3-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/quicklogic-eos-s3-pinctrl_8h.html)。

## 692.1\_原始可见代码（Source Code）

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
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Antmicro <www.antmicro.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_QUICKLOGIC_EOS_S3_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_QUICKLOGIC_EOS_S3_PINCTRL_H_

#include <zephyr/dt-bindings/dt-util.h>

#define IO_MUX_REG_MAX_OFFSET   107
#define IO_MUX_MAX_PAD_NR       45

#define FUNC_SEL_UART_RX        (77 << 13)

#define QUICKLOGIC_EOS_S3_PINMUX(pin, fun)      (pin) (fun)

#define UART_TX_PAD44           QUICKLOGIC_EOS_S3_PINMUX(44, 0x3)
#define UART_RX_PAD45           QUICKLOGIC_EOS_S3_PINMUX(45, FUNC_SEL_UART_RX | BIT(2))
#define USB_PU_CTRL_PAD23       QUICKLOGIC_EOS_S3_PINMUX(23, 0x0)
#define USB_DN_PAD28            QUICKLOGIC_EOS_S3_PINMUX(28, 0x0)
#define USB_DP_PAD31            QUICKLOGIC_EOS_S3_PINMUX(31, 0x0)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_QUICKLOGIC_EOS_S3_PINCTRL_H_ */
```

## 692.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Antmicro <www.antmicro.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 25 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_QUICKLOGIC_EOS_S3_PINCTRL_H_`。

## 692.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/quicklogic-eos-s3-pinctrl_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P691_qemu_fwcfg.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P693_ra_clock.h_源码浏览.md)
