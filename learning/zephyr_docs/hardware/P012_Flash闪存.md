---
id: learning.zephyr-docs.hardware.flash
title: Flash闪存
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/flash.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="flash-api"></a>

# 第12章\_Flash闪存

原文：[Flash](https://docs.zephyrproject.org/latest/hardware/peripherals/flash.html)。读取日期：2026-10-12，`latest`。

Flash 用户接口中的偏移量，以**闪存（Flash Memory）**起始地址为基准。该规则适用于能通过页布局接口查询布局的所有常规闪存区域，相关配置为 `CONFIG_FLASH_PAGE_LAYOUT`。

厂商专用、特殊用途的 Flash 区域可以例外；这类区域不能由普通页布局接口覆盖。

> 译注：设备内偏移不是 **中央处理器（Central Processing Unit，CPU）** 绝对地址，也不自动等于某分区内偏移。调用时要区分控制器接口和分区包装接口的寻址基准，不能把映射地址直接当作 `flash_*` 的偏移参数。

## 12.1\_用户接口与示例

接口见 [Flash 用户参考](../flash_reference/P001_Flash公共接口.md)。原页关联全部示例如下：

- [Ambiq MSPI 时序扫描](../driver_samples/P025_Ambiq_MSPI时序扫描示例.md)：为特定开发板上的设备查找合适时序。
- [AT45 DataFlash 驱动](../driver_samples/P006_AT45_DataFlash示例.md)：通过 **串行外设接口（Serial Peripheral Interface，SPI）** 操作 AT45 系列 DataFlash。
- [B-M2MEM-PACK1 扩展板](https://docs.zephyrproject.org/latest/samples/shields/b_m2mem_pack1/README.html)：根据识别 EEPROM 中的信息检查存储模块。
- [Flash shell](https://docs.zephyrproject.org/latest/samples/drivers/flash_shell/README.html)：通过 shell 命令探索 Flash 设备。
- [JEDEC MSPI-NOR](../driver_samples/P023_MSPI_NOR闪存示例.md)：用 Flash 接口操作 MSPI NOR 串行闪存。
- [JEDEC SPI-NOR](../driver_samples/P005_JEDEC_SPI_NOR闪存示例.md)：用 Flash 接口操作 SPI NOR 串行闪存。
- [JESD216 Flash](../driver_samples/P007_JESD216闪存参数示例.md)：从兼容串行存储设备提取信息。
- [内存映射 Flash](https://docs.zephyrproject.org/latest/samples/boards/espressif/flash_memory_mapped/README.html)：写入存储分区，再分别用 Flash 接口和内存映射指针读取。
- [Nordic 蓝牙活动期间写 Flash](https://docs.zephyrproject.org/latest/samples/boards/nordic/flash/README.html)：蓝牙低功耗无线活动期间进行写入。
- [nRF SoC 内部存储](../driver_samples/P054_nRF内部存储示例.md)：通过 Flash 接口操作 **片上系统（System on Chip，SoC）** 内部闪存。
- [RW612 低功耗Flash检查](https://docs.zephyrproject.org/latest/samples/boards/nxp/frdm_rw612/pm_flash_check/README.html)：跨不同低功耗模式检查外部 NOR 状态。
- [X-NUCLEO-PGEEZ1 M95P32扩展操作](https://docs.zephyrproject.org/latest/samples/shields/x_nucleo_pgeez1/README.html)：访问标识页和缓冲页编程。

## 12.2\_驱动实现接口

驱动实现侧接口另见 [Flash 内部参考](../flash_reference/P003_Flash内部接口.md)。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：DMA直接内存访问](P011_DMA直接内存访问.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：I2C总线](P013_I2C总线.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：DMA直接内存访问](P011_DMA直接内存访问.md) · [下一章：I2C总线](P013_I2C总线.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
