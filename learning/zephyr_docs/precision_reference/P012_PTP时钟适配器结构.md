---
id: learning.zephyr-docs.precision-reference.page-12
title: PTP时钟适配器结构
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structprecision__clock__ptp__adapter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_PTP时钟适配器结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structprecision__clock__ptp__adapter.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入精确时间、时钟抽象、PTP适配器及比例积分控制器参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

将精确时间协议（Precision Time Protocol，PTP）时钟设备呈现为精确时钟的适配器。

```c
#include <zephyr/precision_timing/precision_clock_ptp.h>
```

<a id="details"></a>

将精确时间协议（Precision Time Protocol，PTP）时钟设备呈现为精确时钟的适配器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_a70581afbe4a7615b12c7116c9f71df19"></a>

```c
struct precision_clock precision_clk
```

相关声明：[precision_clock](P007_精确时钟结构.md)、[precision_clk](#a70581afbe4a7615b12c7116c9f71df19)。

与协议无关的精确时钟（Protocol-neutral Precision Clock）。

<a id="r_a3295217c2eacafb024745e5bfd66cccc"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#a3295217c2eacafb024745e5bfd66cccc)。

被包装的 PTP 时钟设备。

## 12.2\_详细说明（Detailed Documentation）

<a id="a3295217c2eacafb024745e5bfd66cccc"></a>

### `dev`

```c
const struct device* precision_clock_ptp_adapter::dev
```

被包装的 PTP 时钟设备。

<a id="a70581afbe4a7615b12c7116c9f71df19"></a>

### `precision_clk`

```c
struct precision_clock precision_clock_ptp_adapter::precision_clk
```

与协议无关的精确时钟（Protocol-neutral Precision Clock）。

## 12.3\_源码定位与版本边界

官方源码定位：[precision_clock_ptp.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/precision_timing/precision_clock_ptp.h)、[precision_clock_ptp.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/precision_timing/precision_clock_ptp.c)。摘要见[来源记录](../SOURCES.md)。本批对应的官方模块未出现在当前仓库源码中，故使用官方来源链接；译文内部导航均为相对链接。

> 译注——源码核对：以下源码跟踪译注依据来源记录中保存摘要的官方main文件，与官方正文分开。精确计时（Precision Timing，也译作精密计时）为协议提供通用部件，本身不负责选择主时钟、拒绝样本、锁定检测或失步恢复；本批核对不表示本仓库已集成该模块。

> 译注——源码核对：precision_clock_ptp_init只保存设备指针、安装操作表并把precision_clk.data指回适配器自身；函数返回void，不执行设备就绪检查或能力发现。PTP设备和适配器存储必须有效，全部必需驱动回调须可用；这一步不会启动PTP同步协议。

> 译注——源码核对：precision_clock_ptp_get返回适配器内部precision_clk的地址，不分配新对象。由于data含自指针，初始化后按值复制或移动适配器会留下指向原实例的上下文指针；需要在最终存储位置初始化并维持其生命周期。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 12.4\_原页交叉引用（Cross References）

- [zephyr/precision_timing/precision_clock_ptp.h](P011_PTP时钟适配器头文件源码.md)
- [precision_clock](P007_精确时钟结构.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_PTP时钟适配器头文件源码.md) · [返回大纲](大纲.md) · [下一章](P013_比例积分控制器接口.md)
