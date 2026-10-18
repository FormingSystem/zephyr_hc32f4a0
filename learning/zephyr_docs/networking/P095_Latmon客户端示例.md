---
id: learning.zephyr-docs.networking.page-95
title: Latmon客户端示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/latmon/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第95章\_Latmon客户端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/latmon/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 95.1\_概述

[在GitHub浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/latmon)。

本项目提供工具，用于测量被测系统（System Under Test，SUT）对GPIO事件的最坏响应时间（Worst-case Response Time）：

- Latmon运行在基于Zephyr的开发板上，产生并监测GPIO事件，同时采集指标。
- Latmus运行在SUT上，对输入GPIO事件的下降沿（Falling Edge）作出响应，显示延迟指标并生成直方图数据（Histogram Data）。

项目属于开源计划[EVL项目：Latmus GPIO响应时间](https://v4.xenomai.org/core/benchmarks/#latmus-gpio-response-time)。主程序在Zephyr系统上通过GPIO引脚监测延迟：先产生一个脉冲，再测量运行Latmus的SUT对该脉冲作出响应所需的时间。

SUT必须运行Latmus，才能接收通过网络上报的延迟指标和直方图信息。程序使用LED指示状态：DHCP绑定为红色，等待Latmus连接为蓝色，采样为绿色。

## 95.2\_为什么不只使用定时器

定时器测试（Timer Test）无法覆盖GPIO信号、硬件和中断处理等外部因素。Latmon与Latmus模拟实际使用场景，采集端到端延迟指标（End-to-End Latency Metrics），从而评估整个系统的实时响应能力。

- 实时线程测试（Real-Time Thread Testing）：评估用户空间线程如何处理外部中断。
- 端到端延迟测量（End-to-End Latency Measurement）：覆盖硬件、驱动和用户空间线程带来的延迟。
- 多平台支持（Versatile Platform Support）：可用于EVL、PREEMPT_RT及其他平台。

## 95.3\_代码结构

示例分为两个主要部分：

| 部分 | 官方文件与职责 |
| --- | --- |
| 应用逻辑（Application Logic） | [samples/net/latmon/src/main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/latmon/src/main.c)：初始化网络，提供测量机制，并处理不同状态的LED指示。 |
| 库（Library） | [subsys/net/lib/latmon/latmon.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/latmon.c)：提供通过Latmus监测延迟的可复用函数和抽象，包含延迟指标与直方图数据上报的核心逻辑。 |

## 95.4\_要求

- Zephyr兼容开发板（Zephyr-Compatible Board）：支持外部GPIO并具有IPv4网络接口，例如FRDM-K64F。
- 被测系统（System under Test）：具有外部GPIO引脚、运行Latmus服务并具有IPv4网络接口。
- 网络连接（Network Connection）：使用DHCP服务器分配IP地址。
- 物理连接（Physical Connection）：通过GPIO连线连接Zephyr开发板与SUT，并将两者接入网络。

## 95.5\_设置与使用

1. 将Latmon烧录到Zephyr开发板。应用会连接网络，通过DHCP获取IPv4地址，然后等待SUT发起连接。
2. 连接发送GPIO（Zephyr到SUT）和接收GPIO（SUT到Zephyr）。FRDM-K64F示例使用Arduino排针J2的20号引脚（`pin 20`）向SUT发送脉冲，使用18号引脚（`pin 18`）接收SUT的应答（Acknowledgment）。
3. 在SUT上运行[Latmus](https://v4.xenomai.org/core/testing/#latmus-program)并选择合适选项。例如用`-p`修改采样周期（Sampling Period），用`-g`生成供后处理使用的直方图数据。
4. 在SUT端监测结果。Latmus会报告延迟数据，并在请求时生成直方图数据文件。

校准（Calibration）由[`CONFIG_LATMON_LOOPBACK_CALIBRATION`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/latmon/Kconfig)控制。可将发送GPIO与应答GPIO相连，形成回环（Loopback），并在启用该配置后构建示例。Latmus连接到这种配置下的Latmon时，会提供一个可用于调整最终延迟结果的校准值。

> 译注：上述排针位置是官方FRDM-K64F示例的接线，不能套用到其他板卡。当前[官方叠加文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/latmon/boards/frdm_k64f.overlay)用`pulse_gpios`指定`gpioe`的24号引脚，用`ack_gpios`指定25号引脚；换板时应核对设备树和实际连接。校准选项是[此示例的私有Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/latmon/Kconfig)。

## 95.6\_示例

在主机上构建并烧录FRDM-K64F开发板。以下为原文命令；`user@host:~$`是提示符，执行时不输入提示符。相对路径`samples/net/latmon`要求当前目录为Zephyr源码根。

```console
user@host:~$ west build -b frdm_k64f samples/net/latmon
user@host:~$ west flash
```

在运行Linux的SUT上，Latmus**必须跟踪信号下降沿**：

```console
root@target:~$ latmus -I gpiochip2,23,falling-edge -O gpiochip2,21 -z -g"histogram" "broadcast"
```

同时观察两个控制台，应能看到类似以下输出。首先是Zephyr端日志：

```text
[00:00:03.311,000] <inf> phy_mc_ksz8081: PHY 0 is up
[00:00:03.311,000] <inf> phy_mc_ksz8081: PHY (0) Link speed 100 Mb, full duplex
[00:00:03.312,000] <inf> eth_nxp_enet_mac: Link is up
*** Booting Zephyr OS build v4.1.0-3337-g886443a190b1 ***
[00:00:03.313,000] <inf> sample_latmon: DHCPv4: binding...
[00:00:03.313,000] <inf> latmon: Latmon server thread priority: 14
[00:00:10.964,000] <inf> net_dhcpv4: Received: 192.168.1.58
[00:00:10.964,000] <inf> sample_latmon: Listening on 192.168.1.58
[00:00:30.966,000] <inf> latmon: Waiting for Latmus ...
[00:00:31.356,000] <inf> latmon: Monitor thread priority: -16
[00:00:31.356,000] <inf> latmon:        monitoring started:
[00:00:31.356,000] <inf> latmon:         - samples per period: 1000
[00:00:31.356,000] <inf> latmon:         - period: 1000 usecs
[00:00:31.356,000] <inf> latmon:         - histogram cells: 200
[00:00:31.393,000] <inf> latmon: Transfer thread priority: 14
```

然后是SUT端的Latmus输出：

```text
root@target:~$ latmus -I gpiochip2,23,falling-edge -O gpiochip2,21 -Z -g"histogram" broadcast
Received broadcast message: 192.168.1.58
warming up on CPU0 (not isolated)...
connecting to latmon at 192.168.1.58:2306...
RTT|  00:00:16  (oob-gpio, 1000 us period, priority 98, CPU0-noisol)
RTH|----lat min|----lat avg|----lat max|-overrun|---msw|---lat best|--lat worst
RTD|     26.375|     30.839|     33.508|       0|     0|     26.375|     33.508
RTD|     26.333|     30.801|     37.633|       0|     0|     26.333|     37.633
RTD|     26.375|     30.801|     31.966|       0|     0|     26.333|     37.633
RTD|     26.375|     30.911|     49.675|       0|     0|     26.333|     49.675
RTD|     26.333|     30.830|     41.658|       0|     0|     26.333|     49.675
RTD|     26.375|     31.107|     59.216|       0|     0|     26.333|     59.216
RTD|     26.333|     30.767|     30.925|       0|     0|     26.333|     59.216
RTD|     26.333|     30.781|     41.616|       0|     0|     26.333|     59.216
RTD|     26.375|     30.768|     32.925|       0|     0|     26.333|     59.216
RTD|     26.375|     30.768|     37.633|       0|     0|     26.333|     59.216
```

> 译注：原文前一条命令使用小写`-z`，日志示例中的命令使用大写`-Z`，这里分别保留。按[Latmus官方选项说明](https://v4.xenomai.org/core/testing/#latmus-program)，`-z`选择带内GPIO测试（In-band GPIO），`-Z`选择依赖EVL实时能力的带外GPIO测试（Out-of-band GPIO）；两者不是大小写别名。`gpiochip2,23`、`gpiochip2,21`是示例SUT的GPIO定位，`192.168.1.58`是示例DHCP地址，日志中的Zephyr版本和测量值也都是原文记录，不是当前仓库或当前硬件的实测结果。

结束后，在主机上从SUT取回直方图文件，并用gnuplot生成PNG图。先将数据文件`histogram`和脚本`plot_data.gp`放到主机当前工作目录，再执行原文命令：

```console
user@host:~$ gnuplot plot_data.gp
```

对于名为`histogram`的数据文件，`plot_data.gp`应包含以下内容：

```gnuplot
set terminal pngcairo size 800,600
set output 'plot.png'
set title "Data Plot"
set xlabel "Latency (usec)"
set ylabel "Sample Count"
set grid
set style data linespoints
plot 'histogram' using 1:2 with linespoints title "Data Points"
```

脚本设置800×600的PNG输出，文件名为`plot.png`；横轴为微秒延迟（Latency，usec），纵轴为样本数（Sample Count），读取数据文件的第1、2列并以点线绘制。

译注：原网页提供的是生成图片的脚本，没有附带生成后的PNG原图；此处保留脚本，不把虚构测量图当作官方原图。

## 95.7\_另见

[延迟监测器API](P099_Latmon完整API参考.md)。


<a id="latmon-client"></a>
<a id="overview"></a>
<a id="why-not-just-use-a-timer"></a>
<a id="code-structure"></a>
<a id="requirements"></a>
<a id="setup-and-usage"></a>
<a id="example"></a>
<a id="see-also"></a>

[上一章](P094_Latmon网络延迟监测服务.md) · [返回大纲](大纲.md) · [下一章](P096_zperf网络流量生成器.md)
