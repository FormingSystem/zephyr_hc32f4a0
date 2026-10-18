---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-7
title: dma_mcux_lpc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__lpc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_dma\_mcux\_lpc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__lpc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P053_zephyr__drivers__dma__dma_mcux_lpc.h_文件参考.md)。

## 7.1\_原始可见代码（Source Code）

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
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>

```c
/*
 * Copyright 2023 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_MCUX_LPC_H_
#define ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_MCUX_LPC_H_

/*
 * LPC DMA engine channel hardware trigger attributes.
 * These attributes can be set to the "dma_slot" field
 * in a dma_config structure to configure a channel for
 * hardware triggering.
 */

/* Peripheral request enable. When set, the peripheral
 * request line associated with this channel is used to pace DMA transfers.
 */
#define LPC_DMA_PERIPH_REQ_EN BIT(0)

/* Hardware trigger enable. When set, the hardware trigger connected to this
 * channel via INPUTMUX can be used to trigger a transfer
 */
#define LPC_DMA_HWTRIG_EN BIT(1)

/* HW trigger polarity. When this bit is set, the trigger will be active
 * high or rising edge triggered, based on TRIG_TYPE selection
 */
#define LPC_DMA_TRIGPOL_HIGH_RISING BIT(2)

/* HW trigger type. When this bit is set, the trigger will be level triggered.
 * When it is cleared, the hardware trigger will be edge triggered.
 */
#define LPC_DMA_TRIGTYPE_LEVEL BIT(3)

/* HW trigger burst mode. When set, the hardware trigger will cause a burst
 * transfer to occur, the length of which is determined by BURST_POWER.
 * When cleared, a single transfer (of the width selected by XFERCFG register)
 * will occur.
 */
#define LPC_DMA_TRIGBURST BIT(4)

/* HW trigger burst power. Note that due to the size limit of the dma_slot
 * field, the maximum transfer burst possible is 128. The hardware supports
 * up to 1024 transfers in BURSTPOWER. The value set here will result in
 * 2^BURSTPOWER transfers occurring. So for BURSTPOWER=3, 8 transfers would
 * occur.
 */
#define LPC_DMA_BURSTPOWER(pwr) (((pwr) & 0x7) << 5)


/* Used by driver to extract burstpower setting */
#define LPC_DMA_GET_BURSTPOWER(slot) (((slot) & 0xE0) >> 5)

/*
 * Special channel_direction for SPI_MCUX_FLEXCOMM_TX so
 * that DMA driver can configure the last descriptor
 * to deassert CS.
 */
#define LPC_DMA_SPI_MCUX_FLEXCOMM_TX (DMA_CHANNEL_DIRECTION_PRIV_START)

#endif /* ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_MCUX_LPC_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

LPC DMA 引擎通道的硬件触发属性（hardware trigger attributes）。可将这些属性设置到 `dma_config` 结构体的 `dma_slot` 字段中，以将通道配置为硬件触发。

### 注释 3：原第 17 行

外设请求使能（peripheral request enable）。置位时，使用与此通道关联的外设请求线来控制 DMA 传输节奏。

### 注释 4：原第 22 行

硬件触发使能（hardware trigger enable）。置位时，可使用通过 INPUTMUX 连接到此通道的硬件触发源触发传输。

### 注释 5：原第 27 行

硬件触发极性（hardware trigger polarity）。此位置位时，根据 `TRIG_TYPE` 的选择，触发采用高电平有效或上升沿触发。

### 注释 6：原第 32 行

硬件触发类型（hardware trigger type）。此位置位时使用电平触发；清零时使用边沿触发。

### 注释 7：原第 37 行

硬件触发突发模式（hardware trigger burst mode）。置位时，硬件触发会启动一次突发传输，其长度由 `BURST_POWER` 决定。清零时，执行一次传输，宽度由 `XFERCFG` 寄存器选择。

### 注释 8：原第 44 行

硬件触发突发指数（hardware trigger burst power）。注意，由于 `dma_slot` 字段大小有限，最大突发传输次数为 128。硬件的 `BURSTPOWER` 最多支持 1024 次传输。此处设置的值会产生 `2^BURSTPOWER` 次传输，例如 `BURSTPOWER=3` 时执行 8 次传输。

### 注释 9：原第 53 行

驱动程序用它提取 `burstpower` 设置。

### 注释 10：原第 56 行

供 `SPI_MCUX_FLEXCOMM_TX` 使用的特殊 `channel_direction`，使 DMA 驱动能够将最后一个描述符配置为取消片选（deassert CS）。

### 注释 11：原第 63 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_MCUX_LPC_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P053_zephyr__drivers__dma__dma_mcux_lpc.h_文件参考.md)

---

[上一章](P006_coap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_dns_resolve.h_源码浏览.md)
