---
id: learning.zephyr-docs.api-source-reference.page-469
title: m2-memory-connector.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/m2-memory-connector_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第469章\_m2-memory-connector.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/m2-memory-connector_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/m2-memory-connector_8h.html)。

## 469.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
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
<a id="l00070"></a>
<a id="l00071"></a>

```c
/*
 * Copyright (c) 2026 Filip Stojanovic <filipembedded@gmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_M2_MEMORY_CONNECTOR_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_M2_MEMORY_CONNECTOR_H_


#define M2MEM_CONNECTOR_GPIO_SPI_SCK  16
#define M2MEM_CONNECTOR_GPIO_SPI_MOSI 17
#define M2MEM_CONNECTOR_GPIO_LDO_EN   18
#define M2MEM_CONNECTOR_GPIO_SPI_MISO 19
#define M2MEM_CONNECTOR_XSPI_NCS2     20
#define M2MEM_CONNECTOR_GPIO_SPI_NSS  21
#define M2MEM_CONNECTOR_XSPI_NCS1     22

#define M2MEM_CONNECTOR_XSPI_DQS0 25
#define M2MEM_CONNECTOR_XSPI_D6   26
#define M2MEM_CONNECTOR_XSPI_D7   27
#define M2MEM_CONNECTOR_XSPI_D5   28
#define M2MEM_CONNECTOR_XSPI_D4   31
#define M2MEM_CONNECTOR_XSPI_D3   32
#define M2MEM_CONNECTOR_XSPI_D2   34
#define M2MEM_CONNECTOR_XSPI_D1   35
#define M2MEM_CONNECTOR_XSPI_D0   37

#define M2MEM_CONNECTOR_LED2       38
#define M2MEM_CONNECTOR_INT1       40
#define M2MEM_CONNECTOR_XSPI_CLK1  41
#define M2MEM_CONNECTOR_LED1       42
#define M2MEM_CONNECTOR_XSPI_NCLK1 43

#define M2MEM_CONNECTOR_XSPI_D15  47
#define M2MEM_CONNECTOR_XSPI_D14  49
#define M2MEM_CONNECTOR_XSPI_NCS4 52
#define M2MEM_CONNECTOR_XSPI_D13  53
#define M2MEM_CONNECTOR_XSPI_NCS3 54
#define M2MEM_CONNECTOR_XSPI_D12  55
#define M2MEM_CONNECTOR_XSPI_DQS1 56

#define M2MEM_CONNECTOR_I2C_SDA    58
#define M2MEM_CONNECTOR_XSPI_D11   59
#define M2MEM_CONNECTOR_I2C_SCL    60
#define M2MEM_CONNECTOR_XSPI_D10   61
#define M2MEM_CONNECTOR_INT2       62
#define M2MEM_CONNECTOR_XSPI_D9    65
#define M2MEM_CONNECTOR_NRST       66
#define M2MEM_CONNECTOR_XSPI_D8    67
#define M2MEM_CONNECTOR_XSPI_CLK2  71
#define M2MEM_CONNECTOR_XSPI_NCLK2 73


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_M2_MEMORY_CONNECTOR_H_ */
```

## 469.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Filip Stojanovic <filipembedded@gmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 71 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_M2_MEMORY_CONNECTOR_H_`。

## 469.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/m2-memory-connector_8h.html)

---

[上一章](P468_lwm2m_send_scheduler.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P470_m5pm1.h_源码浏览.md)
