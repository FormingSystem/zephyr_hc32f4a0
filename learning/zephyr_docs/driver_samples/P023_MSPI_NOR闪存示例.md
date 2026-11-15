---
id: learning.zephyr-docs.driver_samples.page-23
title: MSPI_NOR闪存示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/mspi/mspi_flash/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mspi-flash"></a>

# 第23章\_MSPI\_NOR闪存示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/mspi/mspi_flash/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 23.1\_概览（Overview）

本例演示通过[闪存（Flash）API](../hardware/P012_Flash闪存.md#flash-api)访问MSPI NOR串行闪存器件。虽然例子简单，但它展示直接访问方式，可用于确认闪存工作情况，以及自动节能（Automatic Power Savings）是否正确实现。

<a id="building-and-running"></a>

## 23.2\_构建与运行（Building and Running）

只有在[设备树（Devicetree）](../devicetree/P013_设备树文档入口.md#dt-guide)中提供`flash0`别名，并指向采用以下compatible绑定的条目时，本应用才能为相应目标构建：

- [ambiq,mspi-device绑定](../mspi_binding_reference/P002_ambiq_mspi-device.md#std-dtcompatible-ambiq-mspi-device)、[atxp032绑定](../mtd_atmel_bouffalo_binding_reference/P010_atxp032-mspi.md#std-dtcompatible-atxp032)。

> 译注——操作前提与实际写入：以下原命令从已配置Zephyr环境的源码根目录执行。所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/mspi_flash/src/main.c)优先选择ext_nor0别名，没有它时才选择flash0；测试从偏移0xff000开始，先擦除4096字节扇区，再进行启用的连续双扇区测试，并写入、读回比较数据。运行前应确认目标器件与测试区域，不能把此程序当作无修改的读状态操作；构建失败时先核对目标板和设备树配置。

```bash
west build -b apollo3p_evb samples/drivers/mspi/mspi_flash
west flash
```

<a id="sample-output"></a>

### 23.2.1\_示例输出（Sample Output）

```text
*** Booting Zephyr OS build zephyr-v2.3.0-2142-gca01d2e1d748  ***

JEDEC MSPI-NOR flash testing
==========================

Test 1: Flash erase
Flash erase succeeded!

Test 2: Flash write
Attempting to write 4 bytes
Data read matches data written. Good!
```

> 译注——输出范围：原日志只显示一次擦除与4字节写入。当前实现还含双扇区路径，日志和操作范围可能不同。数据比较成功不能单独证明所有自动节能行为已经验证，本批未执行上述测试。

<a id="see-also"></a>

## 23.3\_相关接口（See also）

[Flash接口参考](../flash_reference/P001_Flash公共接口.md)。


对应官方文档源码：[samples/drivers/mspi/mspi_flash/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/mspi/mspi_flash/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/mspi/mspi_flash/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/mspi/mspi_flash/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P022_MSPI异步传输示例.md) · [返回大纲](大纲.md) · [下一章](P024_MSPI吞吐量示例.md)
