---
id: learning.zephyr-docs.boards-shields.page-205
title: X-NUCLEO-GFX01M2 Display expansion board
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_gfx01m2/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="x-nucleo-gfx01m2-display-expansion-board"></a>

<a id="x-nucleo-gfx01m2-shield"></a>

# 第205章\_X-NUCLEO-GFX01M2显示扩展板

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_gfx01m2/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

X-NUCLEO-GFX01M1及X-NUCLEO-GFX01M2，统称X-NUCLEO-GFX01Mx，为STM32 Nucleo-64增加图形用户界面（GUI）能力。板上有2.2英寸SPI QVGA TFT显示屏，以及用于存储图像、文字及纹理的64 Mbit SPI NOR Flash，并提供用于GUI导航的摇杆。

X-NUCLEO-GFX01M2使用ST Morpho连接器，最多支持2路SPI。

SPI显示屏兼容ilitek,ili9341驱动，SPI Flash兼容jedec,spi-nor驱动。

![官方原图：X-NUCLEO-GFX01M2](images/x_nucleo_gfx01m2.webp)

更多信息见X-NUCLEO-GFX01M2网站。（[X-NUCLEO-GFX01M2 网站](https://www.st.com/en/evaluation-tools/x-nucleo-gfx01m2.html#overview)）

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板只能用于配置了ST Morpho连接器的STM32 Nucleo-64开发板，最多支持2路SPI。设备树覆盖文件定义了LCD SPI及Flash SPI两个节点别名，必须指向Nucleo上相应SPI控制器。开发板所用SPI引脚详情见X-NUCLEO-GFX01M2用户手册：


- [X-NUCLEO-GFX01M2 SPI显示扩展板用户手册](https://www.st.com/resource/en/user_manual/um2750-spi-display-expansion-boards-for-stm32-nucleo64-stmicroelectronics.pdf)

SPI Flash设备不支持写保护（Write Protection）及暂停（Pause）功能。

MX25L6433F Flash及ILI9341显示控制器接口详情见：


- [ILI9341串行SPI总线TFT LCD显示屏数据手册](https://cdn-shop.adafruit.com/datasheets/ILI9341.pdf)
- [MX25L6433F串行SPI总线NOR Flash数据手册](https://www1.futureelectronics.com/doc/Macronix/MX25L6433FZNI-08G.pdf)

<a id="hardware-configuration"></a>

## 硬件配置（Hardware Configuration）

开发板默认SPI引脚控制配置可能与X-NUCLEO-GFX01M2不兼容。另外，建议将SPI引脚设为高速并配置DMA通道，以获得最佳图形性能；示例见boards/nucleo_g071rb.overlay。

<a id="samples"></a>

## 示例（Samples）

可用[Display](../hardware/P171_显示驱动示例.md#display)及[JEDEC SPI-NOR flash](../driver_samples/P005_JEDEC_SPI_NOR闪存示例.md#spi-nor)示例测试扩展板功能。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield x_nucleo_gfx01m2，例如：

```text
# From the root of the zephyr repository
west build -b nucleo_g071rb --shield x_nucleo_gfx01m2 samples/drivers/display/
```

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [x-nucleo-gfx01m2.html](https://www.st.com/en/evaluation-tools/x-nucleo-gfx01m2.html#overview)：HTTP Error 567: Unknown Status。
- [um2750-spi-display-expansion-boards-for-stm32-nucleo64-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um2750-spi-display-expansion-boards-for-stm32-nucleo64-stmicroelectronics.pdf)：HTTP Error 567: Unknown Status。

---

[上一章](P204_X-NUCLEO-EEPRMA2_EEPROM_memory_expansion_board.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P206_X-NUCLEO-GFX02Z1_Display_expansion_board.md)
