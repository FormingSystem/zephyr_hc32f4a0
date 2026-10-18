---
id: learning.zephyr-docs.driver_samples.page-5
title: JEDEC_SPI_NOR闪存示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/spi_flash/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="spi-nor"></a>

# 第5章\_JEDEC\_SPI\_NOR闪存示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/spi_flash/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 5.1\_概览（Overview）

本例在SPI NOR串行闪存（Serial Flash Memory）设备上演示[闪存API](../hardware/P012_Flash闪存.md#flash-api)。虽然流程简单，却展示了直接访问，可用于确认闪存正常工作以及自动节能（Automatic Power Savings）实现是否正确。

<a id="building-and-running"></a>

## 5.2\_构建与运行（Building and Running）

只有目标设备树存在使用以下任一绑定兼容字符串的节点，应用才能构建：

- [jedec,spi-nor](../mtd_microchip_nordic_nxp_binding_reference/P002_jedec_spi-nor.md#std-dtcompatible-jedec-spi-nor)。
- [st,stm32-qspi-nor](../flash_renesas_st_ti_binding_reference/P013_st_stm32-qspi-nor.md#std-dtcompatible-st-stm32-qspi-nor)。
- [st,stm32-ospi-nor](../flash_renesas_st_ti_binding_reference/P012_st_stm32-ospi-nor.md#std-dtcompatible-st-stm32-ospi-nor)。
- [nordic,qspi-nor](../mtd_microchip_nordic_nxp_binding_reference/P012_nordic_qspi-nor.md#std-dtcompatible-nordic-qspi-nor)。

```bash
west build -b nrf52840dk/nrf52840 samples/drivers/spi_flash
west flash
```

> 译注——测试区域：从Zephyr源码根使用已就绪的west环境构建。此例实际执行擦除和写入，不是只读识别；运行前按[对应源码](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/spi_flash/src/main.c)核对SPI_FLASH_TEST_REGION_OFFSET和SPI_FLASH_SECTOR_SIZE，两者有板型分支，部分配置还测试连续扇区。测试区域不得覆盖要保留的内容。本批仅翻译，没有对闪存执行操作。

<a id="sample-output"></a>

### 5.2.1\_示例输出（Sample Output）

```text
*** Booting Zephyr OS build zephyr-v2.3.0-2142-gca01d2e1d748  ***

JEDEC QSPI-NOR SPI flash testing
==========================

Test 1: Flash erase
Flash erase succeeded!

Test 2: Flash write
Attempting to write 4 bytes
Data read matches data written. Good!
```

> 译注——结果解释：日志依次表示擦除成功、尝试写入4字节、读回内容与写入相同。该日志不是功耗测量数据；若要确认真实低功耗行为，还需按实际设备与驱动验证。出现擦除、写入或比对错误时，先检查器件就绪状态、接线、容量与测试区域。

<a id="see-also"></a>

## 5.3\_相关接口（See also）

[闪存接口参考](../flash_reference/P001_Flash公共接口.md)。


对应官方文档源码：[samples/drivers/spi_flash/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/spi_flash/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/spi_flash/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/spi_flash/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P004_SPI软件模拟示例.md) · [返回大纲](大纲.md) · [下一章](P006_AT45_DataFlash示例.md)
