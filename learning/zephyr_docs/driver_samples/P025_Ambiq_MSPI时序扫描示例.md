---
id: learning.zephyr-docs.driver_samples.page-25
title: Ambiq_MSPI时序扫描示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/mspi/mspi_timing_scan/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mspi-timing-scan"></a>

# 第25章\_Ambiq\_MSPI时序扫描示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/mspi/mspi_timing_scan/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 25.1\_概览（Overview）

本例演示Ambiq时序扫描工具（Timing Scan Utility）的使用，为指定开发板上的指定设备寻找合适时序。

<a id="building-and-running"></a>

## 25.2\_构建与运行（Building and Running）

应用只能为具有相应[设备树（Devicetree）](../devicetree/P013_设备树文档入口.md#dt-guide)别名的目标构建：按使用的接口选择`flash0`或`psram0`，并使别名指向compatible符合[ambiq,mspi-device绑定](../mspi_binding_reference/P002_ambiq_mspi-device.md#std-dtcompatible-ambiq-mspi-device)的条目。

> 译注——配置与前提：以下命令在Zephyr开发环境的终端、源码根目录执行，使用apollo510_evb目标。所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/mspi_timing_scan/src/main.c)在CONFIG_FLASH_MSPI分支选择flash0，在CONFIG_MEMC_MSPI分支选择psram0；后者还要求存储器映射配置enable为真，否则打印需要启用XIP的提示并退出。先确认器件、总线和时序配置，构建成功后再烧录；不能只增加别名就认为所有扫描条件均已满足。

```bash
west build -b apollo510_evb samples/drivers/mspi/mspi_timing_scan
west flash
```

<a id="sample-output"></a>

### 25.2.1\_示例输出（Sample Output）

```text
*** Booting Zephyr OS build zephyr-v3.4.0-27775-g750ed00d564b ***
Starting MSPI Timing Scan.
<inf> mspi_ambiq_timing_scan: TxNeg=0, RxNeg=0, RxCap=0, Turnaround=5
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 0, RxDQSDelay Scan = 0x0007FFFE, Window size = 18
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 1, RxDQSDelay Scan = 0x0007FFFF, Window size = 19
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 1, RxDQSDelay Scan = 0x0007FFFF, Window size = 19
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 2, RxDQSDelay Scan = 0x0007FFFE, Window size = 18
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 3, RxDQSDelay Scan = 0x0007FFFF, Window size = 19
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 4, RxDQSDelay Scan = 0x0007FFFE, Window size = 18
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 5, RxDQSDelay Scan = 0x0005FD54, Window size = 7
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 6, RxDQSDelay Scan = 0x00000000, Window size = 0
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 7, RxDQSDelay Scan = 0x00000000, Window size = 0
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 8, RxDQSDelay Scan = 0x00000000, Window size = 0
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 9, RxDQSDelay Scan = 0x00000000, Window size = 0
<inf> mspi_ambiq_timing_scan:     TxDQSDelay: 10, RxDQSDelay Scan = 0x00000000, Window size = 0
<inf> mspi_ambiq_timing_scan: Selected setting: TxNeg=0, RxNeg=0, RxCap=0, Turnaround=5,TxDQSDelay=2, RxDQSDelay=9
MSPI Timing Scan is successful.
```

> 译注——结果阅读：TxDQSDelay／RxDQSDelay分别为发送／接收数据选通信号（Data Strobe，DQS）的延迟设置，Window size表示可用窗口大小。原日志包含两条相同的TxDQSDelay=1结果，此处保留；最终选中的TxDQSDelay=2、RxDQSDelay=9属于原示例组合，不是其他板卡和器件通用的推荐值。本批没有执行时序扫描。

<a id="see-also"></a>

## 25.3\_相关接口（See also）

[Flash接口参考](../flash_reference/P001_Flash公共接口.md)。


对应官方文档源码：[samples/drivers/mspi/mspi_timing_scan/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/mspi_timing_scan/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/mspi/mspi_timing_scan/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/mspi/mspi_timing_scan/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P024_MSPI吞吐量示例.md) · [返回大纲](大纲.md) · [下一章](P026_音频示例目录.md)
