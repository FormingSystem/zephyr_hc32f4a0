---
id: learning.zephyr-docs.api-source-supplement-reference.page-226
title: tiva-c-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tiva-c-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第226章\_tiva-c-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tiva-c-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tiva-c-pinctrl_8h.html)。

## 226.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00089"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="foldopen00100"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>

```c


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_TIVA_C_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_TIVA_C_PINCTRL_H_

/*
 * Tiva C pinmux encoding (32-bit):
 *   Bits [15:0]  : port details
 *   Bits [31:16] : pin details
 */

#define TIVA_C_PORT_SHIFT  0
#define TIVA_C_PORT_MASK   0x7
#define TIVA_C_PIN_SHIFT   16
#define TIVA_C_PIN_MASK    0x7
#define TIVA_C_MUX_SHIFT   19
#define TIVA_C_MUX_MASK    0xF
#define TIVA_C_TYPE_SHIFT  23
#define TIVA_C_TYPE_MASK   0x7

#define TIVA_C_PORT_A 0
#define TIVA_C_PORT_B 1
#define TIVA_C_PORT_C 2
#define TIVA_C_PORT_D 3
#define TIVA_C_PORT_E 4
#define TIVA_C_PORT_F 5

#define TIVA_C_TYPE_GPIO 0
#define TIVA_C_TYPE_UART 1
#define TIVA_C_TYPE_I2C 2
#define TIVA_C_TYPE_I2C_SCL 3
#define TIVA_C_TYPE_SSI 4
#define TIVA_C_TYPE_CAN 5
#define TIVA_C_TYPE_PWM 6

#define TIVA_C_PINMUX(port, pin, mux, type) \
        ((((port) & TIVA_C_PORT_MASK) << TIVA_C_PORT_SHIFT) | \
         (((pin) & TIVA_C_PIN_MASK) << TIVA_C_PIN_SHIFT) | \
         (((mux) & TIVA_C_MUX_MASK) << TIVA_C_MUX_SHIFT) | \
         (((type) & TIVA_C_TYPE_MASK) << TIVA_C_TYPE_SHIFT))

#define TIVA_C_PINMUX_PORT(pm) \
        (((pm) >> TIVA_C_PORT_SHIFT) & TIVA_C_PORT_MASK)

#define TIVA_C_PINMUX_PIN(pm) \
        (((pm) >> TIVA_C_PIN_SHIFT) & TIVA_C_PIN_MASK)

#define TIVA_C_PINMUX_MUX(pm) \
        (((pm) >> TIVA_C_MUX_SHIFT) & TIVA_C_MUX_MASK)

#define TIVA_C_PINMUX_TYPE(pm) \
        (((pm) >> TIVA_C_TYPE_SHIFT) & TIVA_C_TYPE_MASK)

#define TIVA_C_PULL_UP_SHIFT 26
#define TIVA_C_PULL_DOWN_SHIFT 27
#define TIVA_C_OPEN_DRAIN_SHIFT 28

#define TIVA_C_PINMUX_PULL_UP(pm) \
        (((pm) >> TIVA_C_PULL_UP_SHIFT) & 0x1U)

#define TIVA_C_PINMUX_PULL_DOWN(pm) \
        (((pm) >> TIVA_C_PULL_DOWN_SHIFT) & 0x1U)

#define TIVA_C_PINMUX_OPEN_DRAIN(pm) \
        (((pm) >> TIVA_C_OPEN_DRAIN_SHIFT) & 0x1U)

#define TIVA_C_PINCFG_PORT_SHIFT 16
#define TIVA_C_PINCFG_PIN_SHIFT 10

#endif
```

## 226.2\_可见注释译文（Comments）

### 注释 1：原第 12 行

Tiva C 引脚复用编码（Pinmux encoding），共 32 位：

- 位 `[15:0]`：端口详细信息。
- 位 `[31:16]`：引脚详细信息。

## 226.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tiva-c-pinctrl_8h.html)

---

[上一章](P225_times.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P227_tm6605.h_源码浏览.md)
