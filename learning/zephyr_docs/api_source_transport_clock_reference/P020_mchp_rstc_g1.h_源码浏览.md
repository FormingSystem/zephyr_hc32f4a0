---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-20
title: mchp_rstc_g1.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__rstc__g1_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_mchp\_rstc\_g1.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp__rstc__g1_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_runtime_reference/P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md)。

## 20.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="foldopen00024"></a>
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
<a id="amchp__rstc__g1_8h_html_a6af694fadfdfbe42200c31988c69ad43"></a>
<a id="amchp__rstc__g1_8h_html_a6af694fadfdfbe42200c31988c69ad43a1a7e6a2780ee3126cde8a34cd1169fef"></a>
<a id="amchp__rstc__g1_8h_html_a6af694fadfdfbe42200c31988c69ad43a2a59fe99e59d04641461db953476ac31"></a>
<a id="amchp__rstc__g1_8h_html_a6af694fadfdfbe42200c31988c69ad43a405a015f25eb5b6ff23fd98cf155ccfa"></a>
<a id="amchp__rstc__g1_8h_html_a6af694fadfdfbe42200c31988c69ad43a5bf10ab2c8d2c18b238638ebe45e66a6"></a>
<a id="amchp__rstc__g1_8h_html_a6af694fadfdfbe42200c31988c69ad43a7ab5a6787ea160f36c80e8b13f9dbb3a"></a>
<a id="amchp__rstc__g1_8h_html_a6af694fadfdfbe42200c31988c69ad43a9168e6a7b1e10b08fd456a0444de0310"></a>
<a id="amchp__rstc__g1_8h_html_a6af694fadfdfbe42200c31988c69ad43ae2dd00e91b977026125424a6a3cbe739"></a>
<a id="amchp__rstc__g1_8h_html_a6af694fadfdfbe42200c31988c69ad43aeaee4fd0c513e69f21cbb4ba7cde26d7"></a>

```c
/*
 * Copyright (c) 2025-2026 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef INCLUDE_ZEPHYR_DRIVERS_RESET_MCHP_RSTC_G1_H_
#define INCLUDE_ZEPHYR_DRIVERS_RESET_MCHP_RSTC_G1_H_

enum rstc_g1_rcause {
        RSTC_G1_RCAUSE_POR = 0,   /* Power-on Reset */
        RSTC_G1_RCAUSE_BOD12 = 1, /* Brown-Out 1.2V Detector Reset */
        RSTC_G1_RCAUSE_BOD33 = 2, /* Brown-Out 3.3V Detector Reset */
        RSTC_G1_RCAUSE_NVM = 3,   /* NVM Reset */
        RSTC_G1_RCAUSE_EXT = 4,   /* External Reset */
        RSTC_G1_RCAUSE_WDT = 5,   /* Watchdog Reset */
        RSTC_G1_RCAUSE_SYST = 6,  /* System Reset Request */
        RSTC_G1_RCAUSE_BACKUP = 7 /* Backup Reset */
};

#ifdef CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH
/* Reserved reset-cause bits on PIC32CM JH */
#define RSTC_RESERVED_BIT_3     BIT(3)
#define RSTC_RESERVED_BIT_7     BIT(7)
#define RSTC_UNSUPPORTED_RCAUSE ((RSTC_RESERVED_BIT_3) | (RSTC_RESERVED_BIT_7))
#else
#define RSTC_UNSUPPORTED_RCAUSE 0U
#endif /* CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH */

#endif /* INCLUDE_ZEPHYR_DRIVERS_RESET_MCHP_RSTC_G1_H_ */
```

## 20.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025-2026 Microchip Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 25 行

上电复位（Power-on Reset）。

### 注释 3：原第 26 行

1.2 V 欠压检测器复位（Brown-Out 1.2V Detector Reset）。

### 注释 4：原第 27 行

3.3 V 欠压检测器复位（Brown-Out 3.3V Detector Reset）。

### 注释 5：原第 28 行

非易失性存储器复位（NVM Reset）。

### 注释 6：原第 29 行

外部复位（External Reset）。

### 注释 7：原第 30 行

看门狗复位（Watchdog Reset）。

### 注释 8：原第 31 行

系统复位请求（System Reset Request）。

### 注释 9：原第 32 行

备份复位（Backup Reset）。

### 注释 10：原第 36 行

PIC32CM JH 上保留的复位原因位（reset-cause bits）。

### 注释 11：原第 42 行

条件编译配置（Configuration）标记：`CONFIG_SOC_FAMILY_MICROCHIP_PIC32CM_JH`。

### 注释 12：原第 44 行

头文件保护宏（Header guard）标记：`INCLUDE_ZEPHYR_DRIVERS_RESET_MCHP_RSTC_G1_H_`。

## 20.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_runtime_reference/P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md)
- [rstc_g1_rcause](../api_file_runtime_reference/P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md#a6af694fadfdfbe42200c31988c69ad43)
- [RSTC_G1_RCAUSE_POR](../api_file_runtime_reference/P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md#a6af694fadfdfbe42200c31988c69ad43a1a7e6a2780ee3126cde8a34cd1169fef)
- [RSTC_G1_RCAUSE_BOD12](../api_file_runtime_reference/P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md#a6af694fadfdfbe42200c31988c69ad43a7ab5a6787ea160f36c80e8b13f9dbb3a)
- [RSTC_G1_RCAUSE_BOD33](../api_file_runtime_reference/P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md#a6af694fadfdfbe42200c31988c69ad43a405a015f25eb5b6ff23fd98cf155ccfa)
- [RSTC_G1_RCAUSE_NVM](../api_file_runtime_reference/P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md#a6af694fadfdfbe42200c31988c69ad43a9168e6a7b1e10b08fd456a0444de0310)
- [RSTC_G1_RCAUSE_EXT](../api_file_runtime_reference/P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md#a6af694fadfdfbe42200c31988c69ad43a2a59fe99e59d04641461db953476ac31)
- [RSTC_G1_RCAUSE_WDT](../api_file_runtime_reference/P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md#a6af694fadfdfbe42200c31988c69ad43aeaee4fd0c513e69f21cbb4ba7cde26d7)
- [RSTC_G1_RCAUSE_SYST](../api_file_runtime_reference/P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md#a6af694fadfdfbe42200c31988c69ad43a5bf10ab2c8d2c18b238638ebe45e66a6)
- [RSTC_G1_RCAUSE_BACKUP](../api_file_runtime_reference/P036_zephyr__drivers__reset__mchp_rstc_g1.h_文件参考.md#a6af694fadfdfbe42200c31988c69ad43ae2dd00e91b977026125424a6a3cbe739)

---

[上一章](P019_mchp_pic32cm_jh_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P021_ots.h_源码浏览.md)
