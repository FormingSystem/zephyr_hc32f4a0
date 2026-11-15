---
id: learning.zephyr-docs.api-source-interrupt-modem-reference.page-3
title: dma_stm32.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__stm32_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_dma\_stm32.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dma__stm32_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P056_zephyr__drivers__dma__dma_stm32.h_文件参考.md)。

## 3.1\_原始可见代码（Source Code）

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
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="adevicetree_2dma_8h_html"></a>
<a id="adevicetree_8h_html"></a>
<a id="adrivers_2dma_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdma__config_html"></a>

```c
/*
 * Copyright (c) 2021 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_STM32_H_
#define ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_STM32_H_

#include <zephyr/devicetree.h>
#include <zephyr/devicetree/dma.h>
#include <zephyr/drivers/dma.h>

/* @brief linked_channel value to inform zephyr dma driver that
 * DMA channel will be handled by HAL
 */
#define STM32_DMA_HAL_OVERRIDE      0x7F

/* @brief gives the first DMA channel : 0 or 1 in the register map
 * when counting channels from 1 to N or from 0 to N-1
 */
#if defined(CONFIG_DMA_STM32U5)
/* from DTS the dma stream id is in range 0..N-1 */
#define STM32_DMA_STREAM_OFFSET 0
#elif !defined(CONFIG_DMA_STM32_V1)
/* from DTS the dma stream id is in range 1..N */
/* so decrease to set range from 0 from now on */
#define STM32_DMA_STREAM_OFFSET 1
#elif defined(CONFIG_DMA_STM32_V1) && defined(CONFIG_DMAMUX_STM32)
/* typically on the stm32H7 series, DMA V1 with mux */
#define STM32_DMA_STREAM_OFFSET 1
#else
/* from DTS the dma stream id is in range 0..N-1 */
#define STM32_DMA_STREAM_OFFSET 0
#endif /* ! CONFIG_DMA_STM32_V1 */

/* macro for dma slot (only for dma-v1 or dma-v2 types) */
#if DT_HAS_COMPAT_STATUS_OKAY(st_stm32_dma_v2bis)
#define STM32_DT_DMA_SLOT(node_id, dir) 0
#define STM32_DT_INST_DMA_SLOT(inst, dir) 0

#define STM32_DT_DMA_SLOT_BY_IDX(node_id, idx) 0
#define STM32_DT_INST_DMA_SLOT_BY_IDX(inst, idx) 0
#else
#define STM32_DT_DMA_SLOT(node_id, dir) DT_DMAS_CELL_BY_NAME(node_id, dir, slot)
#define STM32_DT_INST_DMA_SLOT(inst, dir) STM32_DT_DMA_SLOT(DT_DRV_INST(inst), dir)

#define STM32_DT_DMA_SLOT_BY_IDX(node_id, idx) DT_DMAS_CELL_BY_IDX(node_id, idx, slot)
#define STM32_DT_INST_DMA_SLOT_BY_IDX(inst, idx) STM32_DT_DMA_SLOT_BY_IDX(DT_DRV_INST(inst), idx)
#endif

#if DT_HAS_COMPAT_STATUS_OKAY(st_stm32_dma_v2) || \
        DT_HAS_COMPAT_STATUS_OKAY(st_stm32_dma_v2bis) || \
        DT_HAS_COMPAT_STATUS_OKAY(st_stm32_dmamux)
#define STM32_DT_DMA_FEATURES(node_id, dir) 0
#define STM32_DT_INST_DMA_FEATURES(inst, dir) 0
#else
#define STM32_DT_DMA_FEATURES(node_id, dir) DT_DMAS_CELL_BY_NAME(node_id, dir, features)
#define STM32_DT_INST_DMA_FEATURES(inst, dir) STM32_DT_DMA_FEATURES(DT_DRV_INST(inst), dir)
#endif

#define STM32_DT_DMA_CTLR(node_id, dir) DT_DMAS_CTLR_BY_NAME(node_id, dir)
#define STM32_DT_INST_DMA_CTLR(inst, dir) STM32_DT_DMA_CTLR(DT_DRV_INST(inst), dir)

#define STM32_DT_DMA_CHANNEL_CONFIG(node_id, dir)                               \
                DT_DMAS_CELL_BY_NAME(node_id, dir, channel_config)
#define STM32_DT_INST_DMA_CHANNEL_CONFIG(inst, dir)                             \
                STM32_DT_DMA_CHANNEL_CONFIG(DT_DRV_INST(inst), dir)

#define STM32_DT_DMA_CHANNEL_CONFIG_BY_IDX(node_id, idx)                        \
                DT_DMAS_CELL_BY_IDX(node_id, idx, channel_config)
#define STM32_DT_INST_DMA_CHANNEL_CONFIG_BY_IDX(inst, idx)                      \
                STM32_DT_DMA_CHANNEL_CONFIG_BY_IDX(DT_DRV_INST(inst), idx)

/* macros for channel-config */
/* enable circular buffer */
#define STM32_DMA_CONFIG_CYCLIC(config)                 ((config >> 5) & 0x1)
/* direction defined on bits 6-7 */
/* 0 -> MEM_TO_MEM, 1 -> MEM_TO_PERIPH, 2 -> PERIPH_TO_MEM */
#define STM32_DMA_CONFIG_DIRECTION(config)              ((config >> 6) & 0x3)
/* periph increment defined on bit 9 as true/false */
#define STM32_DMA_CONFIG_PERIPHERAL_ADDR_INC(config)    ((config >> 9) & 0x1)
/* mem increment defined on bit 10 as true/false */
#define STM32_DMA_CONFIG_MEMORY_ADDR_INC(config)        ((config >> 10) & 0x1)
/* periph data size defined on bits 11-12 */
/* 0 -> 1 byte, 1 -> 2 bytes, 2 -> 4 bytes */
#define STM32_DMA_CONFIG_PERIPHERAL_DATA_SIZE(config)   \
                                                (1 << ((config >> 11) & 0x3))
/* memory data size defined on bits 13, 14 */
/* 0 -> 1 byte, 1 -> 2 bytes, 2 -> 4 bytes */
#define STM32_DMA_CONFIG_MEMORY_DATA_SIZE(config)       \
                                                (1 << ((config >> 13) & 0x3))
/* priority increment offset defined on bit 15 */
#define STM32_DMA_CONFIG_PERIPHERAL_INC_FIXED(config)   ((config >> 15) & 0x1)
/* priority defined on bits 16-17 as 0, 1, 2, 3 */
#define STM32_DMA_CONFIG_PRIORITY(config)               ((config >> 16) & 0x3)

/* macro for features (only for dma-v1) */
#if DT_HAS_COMPAT_STATUS_OKAY(st_stm32_dma_v1)
#define STM32_DMA_FEATURES_FIFO_THRESHOLD(features)     (features & 0x3)
#else
#define STM32_DMA_FEATURES_FIFO_THRESHOLD(features)     0
#endif

#if defined(CONFIG_SOC_SERIES_STM32H5X) || defined(CONFIG_SOC_SERIES_STM32H7RSX) ||                \
        defined(CONFIG_SOC_SERIES_STM32MP2X) || defined(CONFIG_SOC_SERIES_STM32N6X) ||             \
        defined(CONFIG_SOC_SERIES_STM32U3X) || defined(CONFIG_SOC_SERIES_STM32U5X) ||              \
        defined(CONFIG_SOC_SERIES_STM32WBAX)
#define STM32_DMA_GET_CHANNEL_INSTANCE LL_DMA_GET_CHANNEL_INSTANCE
#else
#define STM32_DMA_GET_CHANNEL_INSTANCE __LL_DMA_GET_CHANNEL_INSTANCE
#endif

#if DT_HAS_COMPAT_STATUS_OKAY(st_stm32_dma_v1)
#define STM32_DMA_GET_INSTANCE(reg, channel)                            \
                __LL_DMA_GET_STREAM_INSTANCE((reg), (channel) - STM32_DMA_STREAM_OFFSET);
#else
#define STM32_DMA_GET_INSTANCE(reg, channel)                            \
                STM32_DMA_GET_CHANNEL_INSTANCE((reg), (channel) - STM32_DMA_STREAM_OFFSET);
#endif

#ifndef CONFIG_STM32_HAL2
int dma_stm32_zcfg_to_halcfg(const struct device *dma, const struct dma_config *zephyr_config,
                             DMA_InitTypeDef *hal_config, uint16_t source_addr_adj,
                             uint16_t dest_addr_adj);
#endif /* CONFIG_STM32_HAL2 */

#endif /* ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_STM32_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 14 行

@brief `linked_channel` 的取值，用于通知 Zephyr DMA 驱动：该 DMA 通道将由硬件抽象层（HAL）处理。

### 注释 3：原第 19 行

@brief 给出寄存器映射（register map）中首个 DMA 通道的编号：通道按 1 至 N 或 0 至 N−1 编号时，该值为 0 或 1。

### 注释 4：原第 23 行

来自 DTS 的 DMA 流标识符（stream ID）范围为 0 至 N−1。

### 注释 5：原第 26 行

来自 DTS 的 DMA 流标识符范围为 1 至 N。

### 注释 6：原第 27 行

因此将其减小，使后续范围从 0 开始。

### 注释 7：原第 30 行

通常见于 STM32H7 系列：带多路复用器（mux）的 DMA V1。

### 注释 8：原第 33 行

来自 DTS 的 DMA 流标识符（stream ID）范围为 0 至 N−1。

### 注释 9：原第 35 行

条件标记：`! CONFIG_DMA_STM32_V1`。

### 注释 10：原第 38 行

用于 DMA 槽位（dma slot）的宏，仅适用于 dma-v1 或 dma-v2 类型。

### 注释 11：原第 76 行

用于 `channel-config` 的宏。

### 注释 12：原第 77 行

启用循环缓冲区（circular buffer）。

### 注释 13：原第 79 行

方向（direction）定义在位 6–7 中。

### 注释 14：原第 80 行

0 表示 `MEM_TO_MEM`（内存到内存），1 表示 `MEM_TO_PERIPH`（内存到外设），2 表示 `PERIPH_TO_MEM`（外设到内存）。

### 注释 15：原第 82 行

外设地址递增（peripheral increment）定义在位 9 中，以 true/false 表示。

### 注释 16：原第 84 行

内存地址递增（memory increment）定义在位 10 中，以 true/false 表示。

### 注释 17：原第 86 行

外设数据大小（peripheral data size）定义在位 11–12 中。

### 注释 18：原第 87 行

0 表示 1 字节，1 表示 2 字节，2 表示 4 字节。

### 注释 19：原第 90 行

内存数据大小（memory data size）定义在位 13、14 中。

### 注释 20：原第 91 行

0 表示 1 字节，1 表示 2 字节，2 表示 4 字节。

### 注释 21：原第 94 行

优先级增量偏移（priority increment offset）定义在位 15 中。

### 注释 22：原第 96 行

优先级（priority）定义在位 16–17 中，取值为 0、1、2、3。

### 注释 23：原第 99 行

用于功能（features）的宏，仅适用于 dma-v1。

### 注释 24：原第 153 行

条件编译配置（Configuration）标记：`CONFIG_STM32_HAL2`。

### 注释 25：原第 155 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DMA_DMA_STM32_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P056_zephyr__drivers__dma__dma_stm32.h_文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/devicetree/dma.h](../dma_reference/P011_DMA设备树头文件参考.md)
- [zephyr/drivers/dma.h](../dma_reference/P009_DMA驱动头文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [dma_config](../dma_reference/P004_DMA通道配置.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [dma.h](../dma_reference/P011_DMA设备树头文件参考.md)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [dma.h](../dma_reference/P009_DMA驱动头文件参考.md)

---

[上一章](P002_chat.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_ieee802154_pkt.h_源码浏览.md)
