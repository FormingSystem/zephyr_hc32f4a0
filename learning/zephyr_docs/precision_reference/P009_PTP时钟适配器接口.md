---
id: learning.zephyr-docs.precision-reference.page-9
title: PTP时钟适配器接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__precision__clock__ptp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_PTP时钟适配器接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__precision__clock__ptp.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入精确时间、时钟抽象、PTP适配器及比例积分控制器参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

精确时钟的 PTP 适配器（Precision Clock PTP Adapter）。

<a id="details"></a>

精确时钟的 PTP 适配器（Precision Clock PTP Adapter）。

**引入版本（Since）**：4.5。**接口版本（Version）**：0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_precision_5Fclock_5Fptp_5Fadapter"></a>

```c
struct precision_clock_ptp_adapter
```

相关声明：[precision_clock_ptp_adapter](P012_PTP时钟适配器结构.md)。

将精确时间协议（Precision Time Protocol，PTP）时钟设备呈现为精确时钟的适配器。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.2\_函数（Functions）

<a id="r_ga2ffc6c431dc7c3c0baec0496fdb33db7"></a>

```c
void precision_clock_ptp_init (struct precision_clock_ptp_adapter *adapter, const struct device *dev)
```

相关声明：[precision_clock_ptp_init](#ga2ffc6c431dc7c3c0baec0496fdb33db7)、[precision_clock_ptp_adapter](P012_PTP时钟适配器结构.md)、[device](../device_reference/P002_设备对象结构.md)。

为一个 PTP 时钟设备初始化适配器。

<a id="r_ga5633330bf362c3efd3168638cd2f97b4"></a>

```c
static const struct precision_clock * precision_clock_ptp_get (const struct precision_clock_ptp_adapter *adapter)
```

相关声明：[precision_clock](P007_精确时钟结构.md)、[precision_clock_ptp_get](#ga5633330bf362c3efd3168638cd2f97b4)、[precision_clock_ptp_adapter](P012_PTP时钟适配器结构.md)。

取得 PTP 适配器提供的精确时钟。

## 9.3\_详细说明（Detailed Documentation）

<a id="ga5633330bf362c3efd3168638cd2f97b4"></a>

### `precision_clock_ptp_get()`

```c
const struct precision_clock * precision_clock_ptp_get ( const struct precision_clock_ptp_adapter * adapter)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/precision_timing/precision_clock_ptp.h>
```

取得 PTP 适配器提供的精确时钟。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adapter` | 已初始化的 PTP 时钟适配器。 |

返回（Returns）：指向内嵌精确时钟的指针。

<a id="ga2ffc6c431dc7c3c0baec0496fdb33db7"></a>

### `precision_clock_ptp_init()`

```c
void precision_clock_ptp_init ( struct precision_clock_ptp_adapter * adapter, const struct device * dev )
```

```c
#include <zephyr/precision_timing/precision_clock_ptp.h>
```

为一个 PTP 时钟设备初始化适配器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `adapter` | 待初始化的非空适配器存储区域。 |
| `dev` | 待包装的非空 PTP 时钟设备。 |

## 9.4\_源码定位与版本边界

官方源码定位：[precision_clock_ptp.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/precision_timing/precision_clock_ptp.h)、[precision_clock_ptp.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/precision_timing/precision_clock_ptp.c)。摘要见[来源记录](../SOURCES.md)。本批对应的官方模块未出现在当前仓库源码中，故使用官方来源链接；译文内部导航均为相对链接。

> 译注——源码核对：以下源码跟踪译注依据来源记录中保存摘要的官方main文件，与官方正文分开。精确计时（Precision Timing，也译作精密计时）为协议提供通用部件，本身不负责选择主时钟、拒绝样本、锁定检测或失步恢复；本批核对不表示本仓库已集成该模块。

> 译注——源码核对：precision_clock_ptp_init只保存设备指针、安装操作表并把precision_clk.data指回适配器自身；函数返回void，不执行设备就绪检查或能力发现。PTP设备和适配器存储必须有效，全部必需驱动回调须可用；这一步不会启动PTP同步协议。

> 译注——源码核对：precision_clock_ptp_get返回适配器内部precision_clk的地址，不分配新对象。由于data含自指针，初始化后按值复制或移动适配器会留下指向原实例的上下文指针；需要在最终存储位置初始化并维持其生命周期。

> 译注——源码核对：读取时将net_ptp_time的秒与纳秒合成有符号64位纳秒，先检查纳秒小于10^9及总值不超过PRECISION_TIME_MAX；驱动读取失败直接返回其错误。设置时拒绝负值，拆成秒与纳秒再交给PTP驱动。通用时间类型允许负数，不代表这个PTP适配器允许负的绝对时钟值。

> 译注——源码核对：相位调整要求phase_ns处于int可表示范围，再转换给驱动adjust回调；这比precision_time_t的64位范围窄。速率调整把scaled_ppm转为1.0 + scaled_ppm / (10^6 × 65536)的比率（Rate Ratio），不在公共层代替具体驱动限制其可调范围。

> 译注——源码核对：构建入口仅在CONFIG_PTP_CLOCK下加入PTP适配器实现。普通时间运算、时钟抽象和PI控制器可以作为精确计时基础部件存在，不应把可见头文件声明等同于当前目标必然链接了PTP适配器。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 9.5\_原页交叉引用（Cross References）

- [precision_clock_ptp_adapter](P012_PTP时钟适配器结构.md)
- [device](../device_reference/P002_设备对象结构.md)
- [precision_clock](P007_精确时钟结构.md)
- [zephyr/precision_timing/precision_clock_ptp.h](P010_PTP时钟适配器头文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_精确时钟操作结构.md) · [返回大纲](大纲.md) · [下一章](P010_PTP时钟适配器头文件参考.md)
