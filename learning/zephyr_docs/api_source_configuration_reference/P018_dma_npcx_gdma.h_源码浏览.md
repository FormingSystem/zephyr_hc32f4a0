---
id: learning.zephyr-docs.api-source-configuration-reference.page-18
title: dma_npcx_gdma.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__npcx__gdma_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_dma\_npcx\_gdma.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dma__npcx__gdma_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dma__npcx__gdma_8h.html)。

## 18.1\_原始可见代码（Source Code）

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
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>

```c
/*
 * Copyright (c) 2025 Nuvoton Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_NPCX_GDMA_H_
#define ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_NPCX_GDMA_H_

#define NPCX_DMA_ADDR_16B_ALIGN 16U

/* Macros for DMA channel-config */
/* config: A 32bit mask specifying the GDMA channel configuration
 *           - bit 0-5:  Reserved. (default: 0x0)
 *           - bit 6-7:  Direction  (see dma.h)
 *                       - 0x0: MEM to MEM
 *                       - 0x1: MEM to PERIPH
 *                       - 0x2: PERIPH to MEM
 *                       - 0x3: reserved for PERIPH to PERIPH
 *           - bit 8-9:  Transfer Width Select. The address width must be aligned
 *                       with the selected data width.
 *                       - 0x0: Byte (8 bits)
 *                       - 0x1: Word (16 bits)
 *                       - 0x2: Double-Word (32 bits)
 *                              This value is required if bit 10 is set to 1.
 *                       - 0x3: Reserved
 *           - bit 10:   16-byte transfer (address must be 16-byte aligned)
 *                       - 0x0: Disable 16-byte transfer
 *                      - 0x1: Enable 16-byte transfer
 *           - bit 11:   Destination address direction.
 *                       - 0x0: Destination address incremented successively. (default)
 *                       - 0x1: Destination address decremented successively.
 *           - bit 12:   Source address direction.
 *                       - 0x0: Source address incremented successively. (default)
 *                       - 0x1: Source address decremented successively.
 *           - bit 13:   Destination address fixed.
 *                       - 0x0: Change the Destination address during the GDMA
 *                              operation. (default)
 *                       - 0x1: Fixed address is used for each data transfer from
 *                              the destination.
 *           - bit 14:   Source address fixed.
 *                       - 0x0: Change the source address during the GDMA operation. (default)
 *                       - 0x1: Fixed address is used for each data transfer from
 *                              the source.
 */
#define DMA_NPCX_CONFIG_DIR   FIELD(6, 2)
#define DMA_NPCX_CONFIG_TWS   FIELD(8, 2)
#define DMA_NPCX_CONFIG_BME   10
#define DMA_NPCX_CONFIG_DADIR FIELD(11, 1)
#define DMA_NPCX_CONFIG_SADIR FIELD(12, 1)
#define DMA_NPCX_CONFIG_DAFIX 13
#define DMA_NPCX_CONFIG_SAFIX 14

#define NPCX_GDMA_CHANNEL_CONFIG(inst, name) DT_INST_DMAS_CELL_BY_NAME(inst, name, config)
#define NPCX_GDMA_CONFIG_DIRECTION(config)   GET_FIELD(config, DMA_NPCX_CONFIG_DIR)
#define NPCX_GDMA_CONFIG_BURST_LENGTH(config)                                                      \
        ((1 << GET_FIELD(config, DMA_NPCX_CONFIG_TWS))                                             \
         << (IS_BIT_SET(config, DMA_NPCX_CONFIG_BME) ? 0x2 : 0x0))
#define NPCX_GDMA_CONFIG_DSTADDR_ADJ(config)                                                       \
        (IS_BIT_SET(config, DMA_NPCX_CONFIG_DAFIX)) ? DMA_ADDR_ADJ_NO_CHANGE                       \
                                                    : GET_FIELD(config, DMA_NPCX_CONFIG_DADIR)
#define NPCX_GDMA_CONFIG_SRCADDR_ADJ(config)                                                       \
        (IS_BIT_SET(config, DMA_NPCX_CONFIG_SAFIX)) ? DMA_ADDR_ADJ_NO_CHANGE                       \
                                                    : GET_FIELD(config, DMA_NPCX_CONFIG_SADIR)
#endif /* ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_NPCX_GDMA_H_ */
```

## 18.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Nuvoton Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 13 行

DMA `channel-config` 使用的宏。

### 注释 3：原第 14 行

`config` 是指定 GDMA 通道配置的 32 位掩码：

- 位 `0–5`：保留，默认值为 `0x0`。
- 位 `6–7`：方向（Direction），参见 `dma.h`。`0x0` 为内存到内存（MEM to MEM），`0x1` 为内存到外设（MEM to PERIPH），`0x2` 为外设到内存（PERIPH to MEM），`0x3` 保留用于外设到外设（PERIPH to PERIPH）。
- 位 `8–9`：传输宽度选择（Transfer Width Select），地址宽度必须与所选数据宽度对齐。`0x0` 为字节（Byte，8 位），`0x1` 为字（Word，16 位），`0x2` 为双字（Double-Word，32 位），`0x3` 保留。当位 10 设为 1 时，此值是必需的。
- 位 `10`：16 字节传输，地址必须按 16 字节对齐。`0x0` 禁用，`0x1` 启用。
- 位 `11`：目标地址方向。`0x0` 为目标地址连续递增，默认如此；`0x1` 为目标地址连续递减。
- 位 `12`：源地址方向。`0x0` 为源地址连续递增，默认如此；`0x1` 为源地址连续递减。
- 位 `13`：固定目标地址。`0x0` 为在 GDMA 操作期间改变目标地址，默认如此；`0x1` 为每次从目标进行数据传输时使用固定地址。
- 位 `14`：固定源地址。`0x0` 为在 GDMA 操作期间改变源地址，默认如此；`0x1` 为每次从源进行数据传输时使用固定地址。

译注：位 13 的“从目标”措辞沿用原注释（from the destination）；本注释中的 Word、Double-Word 分别定义为 16 位、32 位。

### 注释 4：原第 66 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_NPCX_GDMA_H_`。

## 18.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dma__npcx__gdma_8h.html)

---

[上一章](P017_dma_mcux_pxp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P019_reset.h_源码浏览.md)
