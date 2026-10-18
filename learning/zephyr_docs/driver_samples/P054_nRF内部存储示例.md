---
id: learning.zephyr-docs.driver_samples.page-54
title: nRF内部存储示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/soc_flash_nrf/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="soc-flash-nrf"></a>

# 第54章\_nRF内部存储示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/soc_flash_nrf/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 54.1\_概览（Overview）

本例演示在片上系统（System on Chip，SoC）内部存储器上使用[Flash API](../hardware/P012_Flash闪存.md#flash-api)。它借助[闪存映射（Flash Map）API](../storage/P001_Flash分区映射.md#flash-map-api)取得包含标签`storage_partition`分区的设备，然后通过Flash API直接访问和修改该分区区域内的内容。

读者可以从本例观察设备读取（Read）、写入（Write）和擦除（Erase）操作，以及如何先检查设备是否已准备好。

<a id="building-and-running"></a>

## 54.2\_构建与运行（Building and Running）

只要SoC具有内部存储器，并在其中定义名为`storage_partition`的固定分区（Fixed Partition），就可以为其构建本例。

> 译注——执行前提与区域：以下原命令从已配置Zephyr环境的终端、Zephyr源码根目录执行。该例会真正写入测试数据，并对需要显式擦除的设备执行擦除；应先确认storage_partition确为可用于此测试的区域，并核对大小、对齐与驱动约束。构建成功后再烧录；存在分区或设备配置错误时先返回配置检查，不能把它作为只读容量查询程序运行。

```bash
west build -b nrf52840dk/nrf52840 samples/drivers/soc_flash_nrf
west flash
```

<a id="sample-output"></a>

### 54.2.1\_示例输出（Sample Output）

```text
*** Booting Zephyr OS build v2.7.99-17621-g54832687bcbb ***

Nordic nRF5 Internal Storage Sample
===================================

Test 1: Flash erase page at 0x82000
   Flash erase succeeded!

Test 2: Flash write (word array 1)
   Attempted to write 1122 at 0x82000
   Attempted to read 0x82000
   Data read: 1122
   Data read matches data written. Good!
   Attempted to write aabb at 0x82004
   Attempted to read 0x82004
   Data read: aabb
   Data read matches data written. Good!
   Attempted to write abcd at 0x82008
   Attempted to read 0x82008
   Data read: abcd
   Data read matches data written. Good!
   Attempted to write 1234 at 0x8200c
   Attempted to read 0x8200c
   Data read: 1234
   Data read matches data written. Good!

Test 3: Flash erase (2 pages at 0x80000)
   Flash erase succeeded!

Test 4: Flash write (word array 2)
   Attempted to write 1234 at 0x82000
   Attempted to read 0x82000
   Data read: 1234
   Data read matches data written. Good!
   Attempted to write aabb at 0x82004
   Attempted to read 0x82004
   Data read: aabb
   Data read matches data written. Good!
   Attempted to write abcd at 0x82008
   Attempted to read 0x82008
   Data read: abcd
   Data read matches data written. Good!
   Attempted to write 1122 at 0x8200c
   Attempted to read 0x8200c
   Data read: 1122
   Data read matches data written. Good!

Test 5: Flash erase page at 0x82000
   Flash erase succeeded!

Test 6: Non-word aligned write (word array 3)
   Attempted to write 1122 at 0x82001
   Attempted to read 0x82001
   Data read: 1122
   Data read matches data written. Good!
   Attempted to write aabb at 0x82005
   Attempted to read 0x82005
   Data read: aabb
   Data read matches data written. Good!
   Attempted to write abcd at 0x82009
   Attempted to read 0x82009
   Data read: abcd
   Data read matches data written. Good!
   Attempted to write 1234 at 0x8200d
   Attempted to read 0x8200d
   Data read: 1234
   Data read matches data written. Good!
   Attempted to write 1122 at 0x82011
   Attempted to read 0x82011
   Data read: 1122
   Data read matches data written. Good!
   Attempted to write aabb at 0x82015
   Attempted to read 0x82015
   Data read: aabb
   Data read matches data written. Good!
   Attempted to write abcd at 0x82019
   Attempted to read 0x82019
   Data read: abcd
   Data read matches data written. Good!
   Attempted to write 1234 at 0x8201d
   Attempted to read 0x8201d
   Data read: 1234
   Data read matches data written. Good!

Test 7: Page layout API
   Offset  0x00041234:
     belongs to the page 65 of start offset 0x00041000
     and the size of 0x00001000 B.
   Page of number 37 has start offset 0x00025000
     and size of 0x00001000 B.
     Page index resolved properly
   SoC flash consists of 256 pages.

Test 8: Write block size API
   write-block-size = 1

Finished!
```

> 译注——原日志与当前实现：以上完整保留原页八项测试及其地址、数据和页布局输出。所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/soc_flash_nrf/src/main.c)已改为准备128字节递增数据，按设备write_block_size写入和读回；依据擦除能力决定是否显式擦除，且仅在写入块大小为1时测试偏移1字节的非字对齐写入。当前测试编号和输出会与这份旧日志不同，不能强求逐行一致。

> 译注——地址与页大小边界：实际写入地址由分区偏移计算，原日志的0x82000等值不是应照抄到其他板上的文件路径或固定写入地址。当前实现的擦除测试页大小在nRF54H20分支取2048字节，其他分支取4096字节，并含双页擦除；移到其他SoC时仍须核对实际布局和分区容量。页布局查询还使用独立的示例偏移与页索引，不表示这些位置也被写入。本批没有执行内部存储器擦写。

<a id="see-also"></a>

## 54.3\_相关接口（See also）

[Flash接口参考](../flash_reference/P001_Flash公共接口.md)、[闪存区域（Flash Area）接口](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html)。


对应官方文档源码：[samples/drivers/soc_flash_nrf/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/soc_flash_nrf/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/soc_flash_nrf/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/soc_flash_nrf/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P053_eSPI接口示例.md) · [返回大纲](大纲.md) · [下一章](P055_ADC示例目录.md)
