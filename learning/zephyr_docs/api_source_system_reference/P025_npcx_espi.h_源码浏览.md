---
id: learning.zephyr-docs.api-source-system-reference.page-25
title: npcx_espi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npcx__espi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_npcx\_espi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/npcx__espi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P252_zephyr__dt-bindings__espi__npcx_espi.h_文件参考.md)。

## 25.1\_原始可见代码（Source Code）

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
<a id="foldopen00015"></a>
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

```c
/*
 * Copyright (c) 2020 Nuvoton Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ESPI_NPCX_ESPI_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ESPI_NPCX_ESPI_H_

/*
 * Encode virtual wire information into a 16-bit unsigned.
 * index  = bits[7:0], Replacement index number
 * group = bits[11:8], Group number for VWEVMS or VWEVSM
 * dir = bits[13:12], Direction for controller to target or target to controller
 */
#define ESPI_NPCX_VW_EX_VAL(dir, group, index)                                                     \
        (((dir & 0x1) << 12) + ((group & 0xf) << 8) + (index & 0xff))

/* extract specific information from encoded ESPI_NPCX_VW_EX_VAL */
#define ESPI_NPCX_VW_EX_INDEX(e)     ((e) & 0xff)
#define ESPI_NPCX_VW_EX_GROUP_NUM(e) (((e) >> 8) & 0xf)
#define ESPI_NPCX_VW_EX_DIR(e)       (((e) >> 12) & 0x1)

/* eSPI VW Master to Slave Register Index */
#define NPCX_VWEVMS0 0
#define NPCX_VWEVMS1 1
#define NPCX_VWEVMS2 2
#define NPCX_VWEVMS3 3
#define NPCX_VWEVMS4 4
#define NPCX_VWEVMS5 5
#define NPCX_VWEVMS6 6
#define NPCX_VWEVMS7 7
#define NPCX_VWEVMS8 8
#define NPCX_VWEVMS9 9
#define NPCX_VWEVMS10 10
#define NPCX_VWEVMS11 11
#define NPCX_VWEVMS_MAX 12

/* eSPI VW Slave to Master Register Index */
#define NPCX_VWEVSM0 0
#define NPCX_VWEVSM1 1
#define NPCX_VWEVSM2 2
#define NPCX_VWEVSM3 3
#define NPCX_VWEVSM4 4
#define NPCX_VWEVSM5 5
#define NPCX_VWEVSM6 6
#define NPCX_VWEVSM7 7
#define NPCX_VWEVSM8 8
#define NPCX_VWEVSM9 9
#define NPCX_VWEVSM_MAX 10

/* eSPI VW GPIO Slave to Master Register Index */
#define NPCX_VWGPSM0 0
#define NPCX_VWGPSM1 1
#define NPCX_VWGPSM2 2
#define NPCX_VWGPSM3 3
#define NPCX_VWGPSM4 4
#define NPCX_VWGPSM5 5
#define NPCX_VWGPSM6 6
#define NPCX_VWGPSM7 7
#define NPCX_VWGPSM8 8
#define NPCX_VWGPSM9 9
#define NPCX_VWGPSM10 10
#define NPCX_VWGPSM11 11
#define NPCX_VWGPSM12 12
#define NPCX_VWGPSM13 13
#define NPCX_VWGPSM14 14
#define NPCX_VWGPSM15 15

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ESPI_NPCX_ESPI_H_ */
```

## 25.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nuvoton Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 9 行

将虚拟线信息（Virtual Wire Information）编码为 16 位无符号值（Unsigned Value）：

- `index`：位 `[7:0]`，替代索引编号（Replacement Index Number）。
- `group`：位 `[11:8]`，VWEVMS 或 VWEVSM 的组编号（Group Number）。
- `dir`：位 `[13:12]`，控制器到目标或目标到控制器的方向（Direction）。

### 注释 3：原第 18 行

从已编码的 `ESPI_NPCX_VW_EX_VAL` 中提取特定信息。

### 注释 4：原第 23 行

eSPI 虚拟线主设备到从设备寄存器索引（VW Master-to-Slave Register Index）。

### 注释 5：原第 38 行

eSPI 虚拟线从设备到主设备寄存器索引（VW Slave-to-Master Register Index）。

### 注释 6：原第 51 行

eSPI 虚拟线 GPIO 从设备到主设备寄存器索引（VW GPIO Slave-to-Master Register Index）。

### 注释 7：原第 69 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_ESPI_NPCX_ESPI_H_`。

## 25.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P252_zephyr__dt-bindings__espi__npcx_espi.h_文件参考.md)

---

[上一章](P024_net_event.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P026_numaker_m031x_reset.h_源码浏览.md)
