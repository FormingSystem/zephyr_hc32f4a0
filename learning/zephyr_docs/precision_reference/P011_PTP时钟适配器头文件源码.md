---
id: learning.zephyr-docs.precision-reference.page-11
title: PTP时钟适配器头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/precision__clock__ptp_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_PTP时钟适配器头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/precision__clock__ptp_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P010_PTP时钟适配器头文件参考.md)和[公共API](P009_PTP时钟适配器接口.md)。

## 11.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00033"></a>
<a id="foldopen00057"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__precision__clock__ptp_html_ga2ffc6c431dc7c3c0baec0496fdb33db7"></a>
<a id="agroup__precision__clock__ptp_html_ga5633330bf362c3efd3168638cd2f97b4"></a>
<a id="aprecision__clock_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="astructprecision__clock__ptp__adapter_html"></a>
<a id="astructprecision__clock__ptp__adapter_html_a3295217c2eacafb024745e5bfd66cccc"></a>
<a id="astructprecision__clock__ptp__adapter_html_a70581afbe4a7615b12c7116c9f71df19"></a>
<a id="astructprecision__clock_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
<a id="l00003"></a> * SPDX-FileCopyrightText: Copyright (c) 2026 Philipp Steiner
<a id="l00004"></a> *
<a id="l00005"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00006"></a> */
<a id="l00007"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_ZEPHYR_PRECISION_TIMING_PRECISION_CLOCK_PTP_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_ZEPHYR_PRECISION_TIMING_PRECISION_CLOCK_PTP_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/device.h&gt;
<a id="l00017"></a>#include &lt;zephyr/precision_timing/precision_clock.h&gt;
<a id="l00018"></a>
<a id="l00019"></a>#ifdef __cplusplus
<a id="l00020"></a>extern "C" {
<a id="l00021"></a>#endif
<a id="l00022"></a>
<a id="l00031"></a>
<a id="l00033"></a>struct precision_clock_ptp_adapter {
<a id="l00035"></a>        struct precision_clock precision_clk;
<a id="l00037"></a>        const struct device *dev;
<a id="l00038"></a>};
<a id="l00039"></a>
<a id="l00046"></a>void precision_clock_ptp_init(struct precision_clock_ptp_adapter *adapter,
<a id="l00047"></a>                              const struct device *dev);
<a id="l00048"></a>
<a id="l00056"></a>static inline const struct precision_clock *
<a id="l00057"></a>precision_clock_ptp_get(const struct precision_clock_ptp_adapter *adapter)
<a id="l00058"></a>{
<a id="l00059"></a>        return &amp;adapter-&gt;precision_clk;
<a id="l00060"></a>}
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>#ifdef __cplusplus
<a id="l00065"></a>}
<a id="l00066"></a>#endif
<a id="l00067"></a>
<a id="l00068"></a>#endif /* ZEPHYR_INCLUDE_ZEPHYR_PRECISION_TIMING_PRECISION_CLOCK_PTP_H_ */
</code></pre>

## 11.2\_可见注释译文（Comments）

1. 版权与许可证：SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors；SPDX-FileCopyrightText: Copyright (c) 2026 Philipp Steiner；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_ZEPHYR_PRECISION_TIMING_PRECISION_CLOCK_PTP_H_头文件包含保护结束。

## 11.3\_原页符号提示（Symbol Descriptions）

### `device.h`

Zephyr设备模型（Device Model）的API与宏。

符号定位：[device.h](../device_reference/P007_设备模型头文件参考.md)。

### `precision_clock_ptp_init`

```c
void precision_clock_ptp_init(struct precision_clock_ptp_adapter *adapter, const struct device *dev)
```

为一个 PTP 时钟设备初始化适配器。

符号定位：[precision_clock_ptp_init](P009_PTP时钟适配器接口.md#ga2ffc6c431dc7c3c0baec0496fdb33db7)。

### `precision_clock_ptp_get`

```c
static const struct precision_clock * precision_clock_ptp_get(const struct precision_clock_ptp_adapter *adapter)
```

取得 PTP 适配器提供的精确时钟。

定义位置（Definition）：precision_clock_ptp.h:57。

符号定位：[precision_clock_ptp_get](P009_PTP时钟适配器接口.md#ga5633330bf362c3efd3168638cd2f97b4)。

### `precision_clock.h`

与协议无关的精确时钟操作（Protocol-neutral Precision Clock Operations）。

符号定位：[precision_clock.h](P005_精确时钟头文件参考.md)。

### `device`

每个驱动实例对应的运行时设备结构（位于ROM中）。

定义位置（Definition）：device.h:543。

符号定位：[device](../device_reference/P002_设备对象结构.md)。

### `precision_clock_ptp_adapter`

将精确时间协议（Precision Time Protocol，PTP）时钟设备呈现为精确时钟的适配器。

定义位置（Definition）：precision_clock_ptp.h:33。

符号定位：[precision_clock_ptp_adapter](P012_PTP时钟适配器结构.md)。

### `precision_clock_ptp_adapter::dev`

```c
const struct device * dev
```

被包装的 PTP 时钟设备。

定义位置（Definition）：precision_clock_ptp.h:37。

符号定位：[precision_clock_ptp_adapter::dev](P012_PTP时钟适配器结构.md#a3295217c2eacafb024745e5bfd66cccc)。

### `precision_clock_ptp_adapter::precision_clk`

```c
struct precision_clock precision_clk
```

与协议无关的精确时钟（Protocol-neutral Precision Clock）。

定义位置（Definition）：precision_clock_ptp.h:35。

符号定位：[precision_clock_ptp_adapter::precision_clk](P012_PTP时钟适配器结构.md#a70581afbe4a7615b12c7116c9f71df19)。

### `precision_clock`

与协议无关的精确时钟实例（Protocol-neutral Precision Clock Instance）。

定义位置（Definition）：precision_clock.h:59。

符号定位：[precision_clock](P007_精确时钟结构.md)。

## 11.4\_源码跟踪译注

> 译注——precision_clock_ptp_init只保存设备指针、安装操作表并把precision_clk.data指回适配器自身；函数返回void，不执行设备就绪检查或能力发现。PTP设备和适配器存储必须有效，全部必需驱动回调须可用；这一步不会启动PTP同步协议。

> 译注——precision_clock_ptp_get返回适配器内部precision_clk的地址，不分配新对象。由于data含自指针，初始化后按值复制或移动适配器会留下指向原实例的上下文指针；需要在最终存储位置初始化并维持其生命周期。

> 译注——读取时将net_ptp_time的秒与纳秒合成有符号64位纳秒，先检查纳秒小于10^9及总值不超过PRECISION_TIME_MAX；驱动读取失败直接返回其错误。设置时拒绝负值，拆成秒与纳秒再交给PTP驱动。通用时间类型允许负数，不代表这个PTP适配器允许负的绝对时钟值。

> 译注——相位调整要求phase_ns处于int可表示范围，再转换给驱动adjust回调；这比precision_time_t的64位范围窄。速率调整把scaled_ppm转为1.0 + scaled_ppm / (10^6 × 65536)的比率（Rate Ratio），不在公共层代替具体驱动限制其可调范围。

> 译注——构建入口仅在CONFIG_PTP_CLOCK下加入PTP适配器实现。普通时间运算、时钟抽象和PI控制器可以作为精确计时基础部件存在，不应把可见头文件声明等同于当前目标必然链接了PTP适配器。

官方源码定位：[头文件 include/zephyr/precision_timing/precision_clock_ptp.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/precision_timing/precision_clock_ptp.h)与[关联实现 subsys/precision_timing/precision_clock_ptp.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/precision_timing/precision_clock_ptp.c)，摘要见[来源记录](../SOURCES.md)。该官方模块尚未出现在当前仓库源码中，因此不创建指向不存在文件的本地链接。去掉注释和展示空白后，本页代码与本次读取的官方原始头文件一致；这个结论不自动适用于以后更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 11.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P010_PTP时钟适配器头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/precision_timing/precision_clock.h](P005_精确时钟头文件参考.md)
- [precision_clock_ptp_adapter](P012_PTP时钟适配器结构.md)
- [precision_clock](P007_精确时钟结构.md)
- [precision_clk](P012_PTP时钟适配器结构.md#a70581afbe4a7615b12c7116c9f71df19)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](P012_PTP时钟适配器结构.md#a3295217c2eacafb024745e5bfd66cccc)
- [precision_clock_ptp_init](P009_PTP时钟适配器接口.md#ga2ffc6c431dc7c3c0baec0496fdb33db7)
- [precision_clock_ptp_get](P009_PTP时钟适配器接口.md#ga5633330bf362c3efd3168638cd2f97b4)

---

[上一章](P010_PTP时钟适配器头文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_PTP时钟适配器结构.md)
