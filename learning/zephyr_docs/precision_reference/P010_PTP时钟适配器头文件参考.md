---
id: learning.zephyr-docs.precision-reference.page-10
title: PTP时钟适配器头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/precision__clock__ptp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_PTP时钟适配器头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/precision__clock__ptp_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入精确时间、时钟抽象、PTP适配器及比例积分控制器参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

用于精确时钟的 PTP 时钟设备适配器。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/precision_timing/precision_clock.h>
```

查看此文件的源码。

用于精确时钟的 PTP 时钟设备适配器。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_precision_5Fclock_5Fptp_5Fadapter"></a>

```c
struct precision_clock_ptp_adapter
```

相关声明：[precision_clock_ptp_adapter](P012_PTP时钟适配器结构.md)。

将精确时间协议（Precision Time Protocol，PTP）时钟设备呈现为精确时钟的适配器。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.2\_函数（Functions）

<a id="r_ga2ffc6c431dc7c3c0baec0496fdb33db7"></a>

```c
void precision_clock_ptp_init (struct precision_clock_ptp_adapter *adapter, const struct device *dev)
```

相关声明：[precision_clock_ptp_init](P009_PTP时钟适配器接口.md#ga2ffc6c431dc7c3c0baec0496fdb33db7)、[precision_clock_ptp_adapter](P012_PTP时钟适配器结构.md)、[device](../device_reference/P002_设备对象结构.md)。

为一个 PTP 时钟设备初始化适配器。

<a id="r_ga5633330bf362c3efd3168638cd2f97b4"></a>

```c
static const struct precision_clock * precision_clock_ptp_get (const struct precision_clock_ptp_adapter *adapter)
```

相关声明：[precision_clock](P007_精确时钟结构.md)、[precision_clock_ptp_get](P009_PTP时钟适配器接口.md#ga5633330bf362c3efd3168638cd2f97b4)、[precision_clock_ptp_adapter](P012_PTP时钟适配器结构.md)。

取得 PTP 适配器提供的精确时钟。

## 10.3\_源码定位与版本边界

官方源码定位：[precision_clock_ptp.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/precision_timing/precision_clock_ptp.h)、[precision_clock_ptp.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/precision_timing/precision_clock_ptp.c)。摘要见[来源记录](../SOURCES.md)。本批对应的官方模块未出现在当前仓库源码中，故使用官方来源链接；译文内部导航均为相对链接。

> 译注——源码核对：以下源码跟踪译注依据来源记录中保存摘要的官方main文件，与官方正文分开。精确计时（Precision Timing，也译作精密计时）为协议提供通用部件，本身不负责选择主时钟、拒绝样本、锁定检测或失步恢复；本批核对不表示本仓库已集成该模块。

> 译注——源码核对：precision_clock_ptp_init只保存设备指针、安装操作表并把precision_clk.data指回适配器自身；函数返回void，不执行设备就绪检查或能力发现。PTP设备和适配器存储必须有效，全部必需驱动回调须可用；这一步不会启动PTP同步协议。

> 译注——源码核对：precision_clock_ptp_get返回适配器内部precision_clk的地址，不分配新对象。由于data含自指针，初始化后按值复制或移动适配器会留下指向原实例的上下文指针；需要在最终存储位置初始化并维持其生命周期。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 10.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/precision_timing/precision_clock.h](P006_精确时钟头文件源码.md)
- [查看此文件的源码](P011_PTP时钟适配器头文件源码.md)
- [precision_clock_ptp_adapter](P012_PTP时钟适配器结构.md)
- [precision_clock_ptp_init](P009_PTP时钟适配器接口.md#ga2ffc6c431dc7c3c0baec0496fdb33db7)
- [device](../device_reference/P002_设备对象结构.md)
- [precision_clock](P007_精确时钟结构.md)
- [precision_clock_ptp_get](P009_PTP时钟适配器接口.md#ga5633330bf362c3efd3168638cd2f97b4)

<a id="header-details"></a>

---

[上一章](P009_PTP时钟适配器接口.md) · [返回大纲](大纲.md) · [下一章](P011_PTP时钟适配器头文件源码.md)
