---
id: learning.zephyr-docs.driver_samples.page-48
title: Grove液晶显示示例
kind: reference
status: maintained
domains: [zephyr, driver_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/drivers/misc/grove_display/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="grove-lcd"></a>

# 第48章\_Grove液晶显示示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/drivers/misc/grove_display/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 48.1\_概览（Overview）

本例通过Grove液晶显示器（Liquid Crystal Display，LCD）显示递增计数器，同时改变背光（Backlight）颜色。

<a id="requirements"></a>

## 48.2\_要求（Requirements）

原文列出以下硬件：

- 一块支持模数转换器（Analog-to-Digital Converter，ADC）的开发板。
- [Grove LCD模块](http://wiki.seeed.cc/Grove-LCD_RGB_Backlight/)。
- 可选的[Grove Base Shield基础扩展板](https://wiki.seeedstudio.com/Base_Shield_V2/)。

> 译注——原要求中的接口差异：本页后文要求I2C，而所读[main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/misc/grove_display/src/main.c)也通过Grove LCD／I2C接口工作，使用glcd设备树节点，并没有ADC采样流程。上面的ADC文字按原文保留，但不能把它当作本例已核实的显示通信条件；应确认I2C、显示模块及驱动配置。

<a id="wiring"></a>

## 48.3\_接线（Wiring）

需要通过Grove扩展板，把Grove LCD连接到支持Arduino扩展板接口的开发板。

部分开发板需要在SCL、SDA两根线与3.3V之间各接一个10 kΩ上拉电阻（Pull-up Resistor）。

请注意：虽然SDA和SCL连接的是3.3V电源，Grove LCD的VDD仍需要连接5V电源，否则LCD不会显示字符；3.3V仅足以给背光供电。

<a id="building-and-running"></a>

## 48.4\_构建与运行（Building and Running）

本例应能用于启用I2C并具有Arduino扩展板接口的开发板。例如，可按以下方式在FRDM K64F上运行：

> 译注——执行环境：从已配置Zephyr环境的终端、Zephyr源码根目录执行。先按上述要求确认总线、上拉和显示供电，并检查glcd节点；构建成功后再烧录，构建或显示异常应返回对应条件检查。本批未接线或给显示模块供电。

```bash
west build -b frdm_k64f samples/drivers/misc/grove_display
west flash
```

<a id="see-also"></a>

## 48.5\_相关接口（See also）

[Grove显示接口参考](https://docs.zephyrproject.org/latest/doxygen/html/group__grove__display.html)。


对应官方文档源码：[samples/drivers/misc/grove_display/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/drivers/misc/grove_display/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/drivers/misc/grove_display/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/drivers/misc/grove_display/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P047_FT800图形控制器示例.md) · [返回大纲](大纲.md) · [下一章](P049_TMC6460电压模式示例.md)
