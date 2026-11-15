---
id: learning.zephyr-docs.api-source-register-time-reference.page-9
title: stm32-fmc-nor-psram.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32-fmc-nor-psram_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_stm32-fmc-nor-psram.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32-fmc-nor-psram_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P411_zephyr__dt-bindings__memory-controller__stm32-fmc-nor-psram.h_文件参考.md)。

## 9.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2022 Georgij Cernysiov
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_CONTROLLER_STM32_FMC_NOR_PSRAM_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_CONTROLLER_STM32_FMC_NOR_PSRAM_H_

/* NOR/SRAM Bank */
#define STM32_FMC_NORSRAM_BANK1                    0x00000000UL
#define STM32_FMC_NORSRAM_BANK2                    0x00000002UL
#define STM32_FMC_NORSRAM_BANK3                    0x00000004UL
#define STM32_FMC_NORSRAM_BANK4                    0x00000006UL

/* Data Address Bus Multiplexing */
#define STM32_FMC_DATA_ADDRESS_MUX_DISABLE         0x00000000UL
#define STM32_FMC_DATA_ADDRESS_MUX_ENABLE          0x00000002UL

/* Memory Type */
#define STM32_FMC_MEMORY_TYPE_SRAM                 0x00000000UL
#define STM32_FMC_MEMORY_TYPE_PSRAM                0x00000004UL
#define STM32_FMC_MEMORY_TYPE_NOR                  0x00000008UL

/* NORSRAM Data Width */
#define STM32_FMC_NORSRAM_MEM_BUS_WIDTH_8          0x00000000UL
#define STM32_FMC_NORSRAM_MEM_BUS_WIDTH_16         0x00000010UL
#define STM32_FMC_NORSRAM_MEM_BUS_WIDTH_32         0x00000020UL

/* Burst Access Mode */
#define STM32_FMC_BURST_ACCESS_MODE_DISABLE        0x00000000UL
#define STM32_FMC_BURST_ACCESS_MODE_ENABLE         0x00000100UL

/* Wait Signal Polarity */
#define STM32_FMC_WAIT_SIGNAL_POLARITY_LOW         0x00000000UL
#define STM32_FMC_WAIT_SIGNAL_POLARITY_HIGH        0x00000200UL

/* Wait Timing */
#define STM32_FMC_WAIT_TIMING_BEFORE_WS            0x00000000UL
#define STM32_FMC_WAIT_TIMING_DURING_WS            0x00000800UL

/* Write Operation */
#define STM32_FMC_WRITE_OPERATION_DISABLE          0x00000000UL
#define STM32_FMC_WRITE_OPERATION_ENABLE           0x00001000UL

/* Wait Signal */
#define STM32_FMC_WAIT_SIGNAL_DISABLE              0x00000000UL
#define STM32_FMC_WAIT_SIGNAL_ENABLE               0x00002000UL

/* Extended Mode */
#define STM32_FMC_EXTENDED_MODE_DISABLE            0x00000000UL
#define STM32_FMC_EXTENDED_MODE_ENABLE             0x00004000UL

/* Asynchronous Wait */
#define STM32_FMC_ASYNCHRONOUS_WAIT_DISABLE        0x00000000UL
#define STM32_FMC_ASYNCHRONOUS_WAIT_ENABLE         0x00008000UL

/* Write Burst */
#define STM32_FMC_WRITE_BURST_DISABLE              0x00000000UL
#define STM32_FMC_WRITE_BURST_ENABLE               0x00080000UL

/* Continuous Clock */
#define STM32_FMC_CONTINUOUS_CLOCK_SYNC_ONLY       0x00000000UL
#define STM32_FMC_CONTINUOUS_CLOCK_SYNC_ASYNC      0x00100000UL

/* Write FIFO */
/* Not every SoC can disable FIFO, refer to reference manual */
#define STM32_FMC_WRITE_FIFO_DISABLE               0x00200000UL
#define STM32_FMC_WRITE_FIFO_ENABLE                0x00000000UL

/* Page Size */
#define STM32_FMC_PAGE_SIZE_NONE                   0x00000000UL
#define STM32_FMC_PAGE_SIZE_128                    0x00010000UL
#define STM32_FMC_PAGE_SIZE_256                    0x00020000UL
#define STM32_FMC_PAGE_SIZE_512                    0x00030000UL
#define STM32_FMC_PAGE_SIZE_1024                   0x00040000UL

/* Access Mode */
#define STM32_FMC_ACCESS_MODE_A                    0x00000000UL
#define STM32_FMC_ACCESS_MODE_B                    0x10000000UL
#define STM32_FMC_ACCESS_MODE_C                    0x20000000UL
#define STM32_FMC_ACCESS_MODE_D                    0x30000000UL

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_CONTROLLER_STM32_FMC_NOR_PSRAM_H_ */
```

## 9.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Georgij Cernysiov。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

NOR／SRAM 存储体（Bank）。

### 注释 3：原第 16 行

数据／地址总线复用（Data Address Bus Multiplexing）。

### 注释 4：原第 20 行

存储器类型（Memory Type）。

### 注释 5：原第 25 行

NOR／SRAM 数据宽度（Data Width）。

### 注释 6：原第 30 行

突发访问模式（Burst Access Mode）。

### 注释 7：原第 34 行

等待信号极性（Wait Signal Polarity）。

### 注释 8：原第 38 行

等待时序（Wait Timing）。

### 注释 9：原第 42 行

写操作（Write Operation）。

### 注释 10：原第 46 行

等待信号（Wait Signal）。

### 注释 11：原第 50 行

扩展模式（Extended Mode）。

### 注释 12：原第 54 行

异步等待（Asynchronous Wait）。

### 注释 13：原第 58 行

写突发（Write Burst）。

### 注释 14：原第 62 行

连续时钟（Continuous Clock）。

### 注释 15：原第 66 行

写先进先出缓冲区（Write FIFO）。

### 注释 16：原第 67 行

并非每个 SoC 都能禁用 FIFO，请参阅参考手册（reference manual）。

### 注释 17：原第 71 行

页大小（Page Size）。

### 注释 18：原第 78 行

访问模式（Access Mode）。

### 注释 19：原第 84 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_CONTROLLER_STM32_FMC_NOR_PSRAM_H_`。

## 9.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P411_zephyr__dt-bindings__memory-controller__stm32-fmc-nor-psram.h_文件参考.md)

---

[上一章](P008_posix_time.h_源码浏览.md) · [返回大纲](大纲.md)
