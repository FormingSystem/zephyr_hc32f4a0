---
id: learning.zephyr-docs.api-source-configuration-reference.page-47
title: kinetis_sim.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kinetis__sim_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_kinetis\_sim.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/kinetis__sim_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/kinetis__sim_8h.html)。

## 47.1\_原始可见代码（Source Code）

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
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="foldopen00108"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>

```c
/*
 * Copyright (c) 2017, 2025-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_KINETIS_SIM_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_KINETIS_SIM_H_

#define KINETIS_SIM_CORESYS_CLK         0
#define KINETIS_SIM_PLATFORM_CLK        1
#define KINETIS_SIM_BUS_CLK             2
#define KINETIS_SIM_FAST_PERIPHERAL_CLK 5
#define KINETIS_SIM_LPO_CLK             19
#define KINETIS_SIM_DMAMUX_CLK  KINETIS_SIM_BUS_CLK
#define KINETIS_SIM_DMA_CLK     KINETIS_SIM_CORESYS_CLK
#define KINETIS_SIM_SIM_SOPT7   7
#define KINETIS_SIM_OSCERCLK    8
#define KINETIS_SIM_MCGIRCLK    12
#define KINETIS_SIM_MCGPCLK     18

#define KINETIS_SIM_PLLFLLSEL_MCGFLLCLK 0
#define KINETIS_SIM_PLLFLLSEL_MCGPLLCLK 1
#define KINETIS_SIM_PLLFLLSEL_IRC48MHZ  3

#define KINETIS_SIM_ER32KSEL_OSC32KCLK  0
#define KINETIS_SIM_ER32KSEL_RTC        2
#define KINETIS_SIM_ER32KSEL_LPO1KHZ    3

#define KINETIS_SIM_ENET_CLK            4321
#define KINETIS_SIM_ENET_1588_CLK       4322

#define KINETIS_SIM_CMP_CLK             4323
#define KINETIS_SIM_VREF_CLK            4324

/*
 * SIM clock specifier encoding.
 *
 * Each SIM clock reference is a 3-cell specifier <id offset bits>:
 *
 *   id     - 32-bit encoded value containing gate and rate information
 *   offset - gate register offset (explicit, for readability and
 *             consumers such as ADC16 that read it directly)
 *   bits   - gate bit index or mask (explicit, same reason)
 *
 * Layout of the `id` cell (32-bit):
 *   [31:19] gate_offset (13 bits) - SCGC register offset; 0 = no gate
 *   [18:14] gate_bit    (5 bits)  - bit position within SCGC register
 *   [13:9]  clock_name  (5 bits)  - KINETIS_SIM_*_CLK for get_rate
 *   [8:6]   mux_val     (3 bits)  - mux source value for configure
 *   [5:1]   mux_shift   (5 bits)  - mux bit shift in mux register
 *   [0]     has_mux     (1 bit)   - 1 = configure mux on .configure call
 *
 * All known clock name values (0-19) and gate offsets (up to 0x1040)
 * fit within their respective fields.
 */

#define KINETIS_SIM_CLOCK_ID(name, gate_offset, gate_bit) \
        ((((gate_offset) & 0x1FFFU) << 19) | \
         (((gate_bit)    & 0x1FU)   << 14) | \
         (((name)        & 0x1FU)   <<  9))

#define KINETIS_SIM_CLOCK_ID_MUX(name, gate_offset, gate_bit, mux_shift, mux_val) \
        (KINETIS_SIM_CLOCK_ID(name, gate_offset, gate_bit) | \
         (((mux_val)   & 0x7U) << 6) | \
         (((mux_shift) & 0x1FU) << 1) | 0x1U)

/* Decoders used by the driver and soc.c */
#define KINETIS_SIM_CLOCK_DECODE_GATE_OFFSET(val)  (((val) >> 19) & 0x1FFFU)
#define KINETIS_SIM_CLOCK_DECODE_GATE_BIT(val)     (((val) >> 14) & 0x1FU)
#define KINETIS_SIM_CLOCK_DECODE_NAME(val)         (((val) >>  9) & 0x1FU)
#define KINETIS_SIM_CLOCK_DECODE_MUX_VAL(val)      (((val) >>  6) & 0x7U)
#define KINETIS_SIM_CLOCK_DECODE_MUX_SHIFT(val)    (((val) >>  1) & 0x1FU)
#define KINETIS_SIM_CLOCK_HAS_MUX(val)             ((val) & 0x1U)

#define KINETIS_SIM_CLOCK(name, offset, bits) \
        KINETIS_SIM_CLOCK_ID(name, offset, bits) offset bits

#define KINETIS_SIM_CLOCK_MUX(name, offset, bits, mux_shift, mux_val) \
        KINETIS_SIM_CLOCK_ID_MUX(name, offset, bits, mux_shift, mux_val) offset bits

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_KINETIS_SIM_H_ */
```

## 47.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017, 2025-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 36 行

SIM 时钟说明符编码（Clock specifier encoding）。

每个 SIM 时钟引用都是由三个单元组成的说明符 `<id offset bits>`：

- `id`：包含门控与频率信息的 32 位编码值。
- `offset`：门控寄存器偏移量。显式给出以提高可读性，也供 ADC16 等直接读取该值的使用方使用。
- `bits`：门控位索引或掩码；出于同样原因显式给出。

`id` 单元的 32 位布局：

- `[31:19] gate_offset`，13 位：SCGC 寄存器偏移量；0 表示没有门控。
- `[18:14] gate_bit`，5 位：SCGC 寄存器内的位位置。
- `[13:9] clock_name`，5 位：供 `get_rate` 使用的 `KINETIS_SIM_*_CLK`。
- `[8:6] mux_val`，3 位：供 `configure` 使用的多路复用源值。
- `[5:1] mux_shift`，5 位：多路复用寄存器中的位移量。
- `[0] has_mux`，1 位：1 表示在调用 `.configure` 时配置多路复用器。

所有已知时钟名称值（0–19）和门控偏移量（最大 `0x1040`）都能容纳在各自字段中。

### 注释 3：原第 71 行

驱动和 `soc.c` 使用的解码器（Decoders）。

### 注释 4：原第 111 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_KINETIS_SIM_H_`。

## 47.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/kinetis__sim_8h.html)

---

[上一章](P046_kinetis_scg.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P048_time.h_源码浏览.md)
