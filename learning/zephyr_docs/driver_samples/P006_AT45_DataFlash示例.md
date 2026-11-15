---
id: learning.zephyr-docs.driver_samples.page-6
title: AT45_DataFlash示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/spi_flash_at45/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="spi-flash-at45"></a>

# 第6章\_AT45\_DataFlash示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/spi_flash_at45/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 6.1\_概览（Overview）

本例演示AT45系列DataFlash驱动及设备树节点配置。随附覆盖文件有两个示例节点，用于让驱动管理闪存芯片实例。

程序向指定测试区域写入递增字节，数值超出8位范围后回绕，再读回检查写入是否成功。连续运行示例时，起始值也递增。

本例提供两个配置覆盖文件：[samples/drivers/spi_flash_at45/overlay-pm.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/spi_flash_at45/overlay-pm.conf)启用设备电源管理（Device Power Management，Device PM）API，使设备可进入低功耗状态；[samples/drivers/spi_flash_at45/overlay-page_layout.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/spi_flash_at45/overlay-page_layout.conf)启用闪存页布局（Flash Page Layout）API以显示闪存信息。

默认配置使用DataFlash的读—改—写（Read-Modify-Write）功能，因此不需要执行页擦除。禁用 [`CONFIG_SPI_FLASH_AT45_USE_READ_MODIFY_WRITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_FLASH_AT45_USE_READ_MODIFY_WRITE) 可改变此行为。

<a id="requirements"></a>

## 6.2\_要求（Requirements）

原文说明，本例曾在连接AT45DB321E的Nordic nRF9160 DK（`nrf9160dk/nrf9160`）上测试。为其他板和AT45系列器件提供相应覆盖文件，即可按各自硬件调整。

> 译注——数据修改范围：所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/spi_flash_at45/src/main.c)的测试偏移为0xFE00、大小为0x400字节，整片擦除开关默认关闭；擦除逻辑还受读—改—写选项影响。默认不显式擦页不代表不改变原内容，测试仍会写入该区域。应核对所用版本与器件容量，不将这些值视为所有应用可用的空闲区。

<a id="building-and-running"></a>

## 6.3\_构建与运行（Building and Running）

代码位于 [samples/drivers/spi_flash_at45](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/drivers/spi_flash_at45)。以下命令从Zephyr源码根执行，依赖已准备好的工具链、模块、匹配接线与板配置；各配置分支按目的选择。

基本构建与烧录：

```bash
west build -b nrf9160dk/nrf9160 samples/drivers/spi_flash_at45
west flash
```

启用设备电源管理：

```bash
west build -b nrf9160dk/nrf9160 samples/drivers/spi_flash_at45 -- -DEXTRA_CONF_FILE=overlay-pm.conf
west flash
```

启用闪存页布局：

```bash
west build -b nrf9160dk/nrf9160 samples/drivers/spi_flash_at45 -- -DEXTRA_CONF_FILE=overlay-page_layout.conf
west flash
```

同时启用设备电源管理与页布局：

```bash
west build -b nrf9160dk/nrf9160 samples/drivers/spi_flash_at45 -- -DEXTRA_CONF_FILE="overlay-pm.conf overlay-page_layout.conf"
west flash
```

<a id="sample-output"></a>

## 6.4\_示例输出（Sample Output）

同时启用两项功能时，典型输出为：

```text
DataFlash sample app on nrf9160dk_nrf9160
Using DATAFLASH_1, chip size: 4194304 bytes (page: 512)
Reading the first byte of the test region ... OK
Preparing test content starting with 0x01.
Writing the first half of the test region... OK
Writing the second half of the test region... OK
Reading the whole test region... OK
Checking the read content... OK
Putting the flash device into low power state... OK
```

> 译注——日志顺序：输出先显示芯片容量与页大小，再读取测试区首字节、准备数据、分两半写入、读回整区、校验，并进入低功耗状态。各步OK对应原文操作成功，不能仅凭最后一行代替前面全部检查。本次没有运行该示例。

随附覆盖文件定义两个AT45芯片实例，但示例运行只要求标为“DATAFLASH_1”的芯片。若另一个芯片未连接，会出现以下日志，而示例其余行为不受影响：

```text
[00:00:00.000,000] <err> spi_flash_at45: Wrong JEDEC ID: ff ff ff, expected: 1f 24 00
```

> 译注——错误边界：这条Wrong JEDEC ID表示读出的标识为ff ff ff，与期望1f 24 00不符。“其余行为不受影响”仅针对原文所说的另一个可选芯片未接；若必需芯片本身报错，仍需检查连接、供电和设备树配置。

<a id="see-also"></a>

## 6.5\_相关接口（See also）

[闪存接口参考](../flash_reference/P001_Flash公共接口.md)。


对应官方文档源码：[samples/drivers/spi_flash_at45/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/spi_flash_at45/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/spi_flash_at45/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/spi_flash_at45/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P005_JEDEC_SPI_NOR闪存示例.md) · [返回大纲](大纲.md) · [下一章](P007_JESD216闪存参数示例.md)
