---
id: learning.zephyr-docs.api-source-device-reference.page-28
title: npcx_fiu_qspi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npcx__fiu__qspi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_npcx\_fiu\_qspi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/npcx__fiu__qspi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P253_zephyr__dt-bindings__flash_controller__npcx_fiu_qspi.h_文件参考.md)。

## 28.1\_原始可见代码（Source Code）

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
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Nuvoton Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_FLASH_CONTROLLER_NPCX_FIU_QSPI_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_FLASH_CONTROLLER_NPCX_FIU_QSPI_H_

#include <zephyr/dt-bindings/dt-util.h>

/* Software controlled Chip-Select number for UMA transactions */
#define NPCX_QSPI_SW_CS0        BIT(0)
#define NPCX_QSPI_SW_CS1        BIT(1)
#define NPCX_QSPI_SW_CS2        BIT(2)
#define NPCX_QSPI_SW_CS_MASK    (NPCX_QSPI_SW_CS0 | NPCX_QSPI_SW_CS1 | NPCX_QSPI_SW_CS2)

/* Supported flash interfaces for UMA transactions */
#define NPCX_QSPI_SEC_FLASH_SL  BIT(4)
#define NPCX_QSPI_PVT_FLASH_SL  BIT(5)
#define NPCX_QSPI_SHD_FLASH_SL  BIT(6)
#define NPCX_QSPI_BKP_FLASH_SL  BIT(7)

/* Supported read mode for Direct Read Access */
#define NPCX_RD_MODE_NORMAL     0
#define NPCX_RD_MODE_FAST       1
#define NPCX_RD_MODE_FAST_DUAL  3

#if defined(CONFIG_NPCX_SOC_VARIANT_NPCKN)
/* Maximum length of a valid read burst */
#define NPCX_BURST_MODE_1_BYTE  0
#define NPCX_BURST_MODE_16_BYTE 3
#endif

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_FLASH_CONTROLLER_NPCX_FIU_QSPI_H_ */
```

## 28.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nuvoton Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

UMA 事务（Transactions）中由软件控制的片选编号（Chip-Select Number）。

### 注释 3：原第 17 行

UMA 事务（Transactions）支持的闪存接口（Flash Interfaces）。

### 注释 4：原第 23 行

直接读取访问（Direct Read Access）支持的读取模式（Read Mode）。

### 注释 5：原第 29 行

有效读取突发（Valid Read Burst）的最大长度（Maximum Length）。

### 注释 6：原第 34 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_FLASH_CONTROLLER_NPCX_FIU_QSPI_H_`。

## 28.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P253_zephyr__dt-bindings__flash_controller__npcx_fiu_qspi.h_文件参考.md)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P027_net_pkt_filter.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P029_nrf_clock_control.h_源码浏览.md)
