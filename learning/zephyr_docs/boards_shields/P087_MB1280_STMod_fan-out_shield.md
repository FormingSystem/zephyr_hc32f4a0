---
id: learning.zephyr-docs.boards-shields.page-87
title: MB1280 STMod fan-out shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/mb1280_stmod_plus/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="mb1280-stmod-fan-out-shield"></a>

<a id="mb1280-stmod-plus"></a>

# 第87章\_MB1280 STMod+扇出扩展板（Fan-out Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/mb1280_stmod_plus/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

MB1280将STMod+连接器转换为Grove UART、Grove I2C、ESP-01及mikroBUS兼容连接器。

扩展板通过开发板的stmod_plus_connector GPIO连接映射节点（Nexus）提供MB1280扇出连接器。

MB1280的mikroBUS兼容连接器上全部可作GPIO的引脚经mikrobus_header提供。

可叠加的扩展板变体提供接口别名：


- mb1280_stmod_plus_adc将mikrobus_adc映射到stmod_adc。
- mb1280_stmod_plus_i2c将grove_i2c及mikrobus_i2c映射到stmod_i2c。
- mb1280_stmod_plus_pwm将mikrobus_pwm映射到stmod_pwm。
- mb1280_stmod_plus_serial将grove_serial、esp_01_serial及mikrobus_serial映射到stmod_serial。
- mb1280_stmod_plus_spi将mikrobus_spi映射到stmod_spi。

<a id="requirements"></a>

## 前置要求（Requirements）

开发板须提供带stmod_plus_connector节点标签的STMod+接口，并为选用的叠加变体提供对应stmod_adc、stmod_i2c、stmod_pwm、stmod_serial或stmod_spi标签。

<a id="programming"></a>

## 编程（Programming）

调用west build时添加--shield mb1280_stmod_plus，并按开发板提供的STMod+接口添加对应叠加变体，例如：

```text
# From the root of the zephyr repository
west build -b stm32n6570_dk/stm32n657xx/sb --shield mb1280_stmod_plus --shield mb1280_stmod_plus_i2c --shield mb1280_stmod_plus_serial samples/basic/blinky
```

---

[上一章](P086_MAX7219_LED_display_driver_shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P088_RNBD451_Add-on_Board.md)
