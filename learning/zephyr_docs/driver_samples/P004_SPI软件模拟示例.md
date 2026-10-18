---
id: learning.zephyr-docs.driver_samples.page-4
title: SPI软件模拟示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/spi_bitbang/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="spi-bitbang"></a>

# 第4章\_SPI软件模拟示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/spi_bitbang/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 4.1\_概览（Overview）

本例演示使用软件模拟SPI（Bitbang SPI）驱动。这类驱动适合传输字长（Word Size）不是8的整数倍的设备，例如某些液晶显示器（Liquid Crystal Display，LCD）需要额外的命令／数据位（Command/Data Bit）。

示例循环使用若干不同的SPI传输配置。

<a id="building-and-running"></a>

## 4.2\_构建与运行（Building and Running）

只有目标[设备树](../devicetree/P013_设备树文档入口.md#dt-guide)中存在兼容字符串为 [zephyr,spi-bitbang](../spi_stm32_ti_xilinx_binding_reference/P022_zephyr_spi-bitbang.md#std-dtcompatible-zephyr-spi-bitbang) 的节点，应用才能构建。可用导线连接串行数据输入（Serial Data Input，SDI）与串行数据输出（Serial Data Output，SDO）引脚，形成基本的接收数据回环测试（Loopback Test）。

```bash
west build -b nrf52840dk/nrf52840 samples/drivers/spi_bitbang
west flash
```

> 译注——操作位置：从Zephyr源码根执行，先确认目标板覆盖配置和物理接线。原命令以nrf52840dk/nrf52840构建并烧录；换板时需先具备对应设备树节点和有效引脚，不能只替换板名。

<a id="sample-output"></a>

### 4.2.1\_示例输出（Sample Output）

```text
*** Booting Zephyr OS build zephyr-v2.6.0-2939-g1882b95b42e2  ***
basic_write_9bit_words; ret: 0
  wrote 0101 00ff 00a5 0000 0102
9bit_loopback_partial; ret: 0
 tx (i)  : 0101 0102
 tx (ii) : 0003 0004 0105
 rx (ii) : 0003 0004 0105
basic_write_9bit_words; ret: 0
 wrote 0101 00ff 00a5 0000 0102
9bit_loopback_partial; ret: 0
 tx (i)  : 0101 0102
 tx (ii) : 0003 0004 0105
 rx (ii) : 0003 0004 0105
basic_write_9bit_words; ret: 0
 wrote 0101 00ff 00a5 0000 0102
9bit_loopback_partial; ret: 0
 tx (i)  : 0101 0102
 tx (ii) : 0003 0004 0105
 rx (ii) : 0003 0004 0105
```

> 译注——日志阅读：basic_write_9bit_words是9位字写入，ret: 0表示该调用返回成功；tx、rx分别表示发送和接收。9bit_loopback_partial展示部分传输缓冲区的回环结果，接收值与对应发送值一致。启动版本号和多轮重复输出属于原文日志，不是本次执行结果。

<a id="see-also"></a>

## 4.3\_相关接口（See also）

[SPI接口参考](../hardware/P318_SPI公共接口.md)。


对应官方文档源码：[samples/drivers/spi_bitbang/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/spi_bitbang/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/spi_bitbang/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/spi_bitbang/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P003_SPI实时IO回环示例.md) · [返回大纲](大纲.md) · [下一章](P005_JEDEC_SPI_NOR闪存示例.md)
