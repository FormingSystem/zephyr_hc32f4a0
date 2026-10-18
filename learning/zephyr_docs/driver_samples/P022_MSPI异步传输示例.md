---
id: learning.zephyr-docs.driver_samples.page-22
title: MSPI异步传输示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/mspi/mspi_async/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mspi-async"></a>

# 第22章\_MSPI异步传输示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/mspi/mspi_async/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 22.1\_概览（Overview）

本例演示通过[MSPI驱动API](../hardware/P065_多位SPI总线.md#mspi-api)访问MSPI存储器件。异步收发（Asynchronous Transceive）调用需要控制器支持软件队列（Software Queue）或硬件队列（Hardware Queue）；对本例而言，底层采用哪种队列实现不应造成使用方式上的差异。

<a id="building-and-running"></a>

## 22.2\_构建与运行（Building and Running）

只有在[设备树（Devicetree）](../devicetree/P013_设备树文档入口.md#dt-guide)中提供`dev0`别名，并使其指向具有以下compatible描述的条目时，本应用才能为相应目标构建：

- [ambiq,mspi-device绑定](../mspi_binding_reference/P002_ambiq_mspi-device.md#std-dtcompatible-ambiq-mspi-device)、[aps6404l绑定](../mtd_atmel_bouffalo_binding_reference/P003_aps6404l-mspi.md#std-dtcompatible-aps6404l)。

> 译注——操作前提：以下原命令在已配置Zephyr开发环境的终端、Zephyr源码根目录执行，目标为apollo3p_evb。确认该版本的板配置和外部存储器配置满足上述条件，构建成功后再烧录；出现设备树或驱动错误时先返回检查这些配置，不把更改板名等同于完成硬件适配。

```bash
west build -b apollo3p_evb samples/drivers/mspi/mspi_async
west flash
```

<a id="sample-output"></a>

### 22.2.1\_示例输出（Sample Output）

```text
*** Booting Zephyr OS build zephyr-v3.5.0-8581-gc80b243c7598 ***
w:3,r:3
Read data matches written data
```

> 译注——传输与版本：所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/mspi_async/src/main.c)把1024字节写缓冲区分成四个256字节分组，再异步读回并逐字节比较；最后一个分组请求完成回调（Completion Callback）。程序会写入目标器件地址0开始的测试区域，不能当作只读探测。原输出中的w:3,r:3按旧示例保留，当前代码等待消息的文字不同；该数字不表示只传了3字节。

<a id="see-also"></a>

## 22.3\_相关接口（See also）

[MSPI接口参考](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html)。


对应官方文档源码：[samples/drivers/mspi/mspi_async/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/mspi_async/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/mspi/mspi_async/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/mspi/mspi_async/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P021_MSPI示例目录.md) · [返回大纲](大纲.md) · [下一章](P023_MSPI_NOR闪存示例.md)
