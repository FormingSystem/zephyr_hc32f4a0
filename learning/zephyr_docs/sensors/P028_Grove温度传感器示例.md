---
id: learning.zephyr-docs.sensors.page-28
title: Grove温度传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/grove_temperature/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="grove_temperature"></a>

# 第28章\_Grove温度传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/grove_temperature/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 28.1 概述（Overview）

本示例读取Grove温度传感器输出，每秒向控制台打印一次摄氏温度。设置[`CONFIG_GROVE_LCD_RGB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GROVE_LCD_RGB)和[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)选项后，温度还会显示在Grove液晶显示屏（Liquid Crystal Display，LCD）上。

<a id="requirements"></a>

## 28.2 要求（Requirements）

需要以下硬件：

- 支持模数转换器（Analog-to-Digital Converter，ADC）的开发板。
- [Grove温度传感器（Grove Temperature Sensor）](https://wiki.seeedstudio.com/Grove-Temperature_Sensor_V1.2/)。
- [Grove基础扩展板（Grove Base Shield）](https://wiki.seeedstudio.com/Base_Shield_V2/)。
- 可选的[Grove液晶显示屏（Grove LCD）](https://wiki.seeedstudio.com/Grove-LCD_RGB_Backlight/)。

<a id="wiring"></a>

## 28.3 接线（Wiring）

较简单的连接方式是在支持Arduino扩展板的开发板上安装Grove Shield，再连接传感器。提供设备树覆盖文件，描述传感器位置。采用本示例随附的覆盖文件时，传感器应连接Grove Shield的`A0`接口。

如果使用Grove LCD，应将它接到Shield的I2C接口，并在覆盖文件中添加对应节点。

<a id="building-and-running"></a>

## 28.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，使用已完成官方入门配置的UCRT64 Bash或Linux Bash终端。构建成功只表示固件生成；烧录和读取真实温湿度还需要正确的目标板、传感器节点及接线。若设备未就绪或读取失败，先检查节点状态、驱动配置和总线连接。

按以下命令构建并烧录，将`nrf52dk_nrf52832`替换为实际开发板：

```sh
west build -b nrf52dk_nrf52832 samples/sensor/grove_temperature
west flash
```

> 译注——当前板名：原文保留旧的`nrf52dk_nrf52832`目标写法；当前官方`tests.yaml`使用`nrf52dk/nrf52832`。对该板，构建部分应写为`west build -b nrf52dk/nrf52832 samples/sensor/grove_temperature`。板级覆盖文件仍名为`boards/nrf52dk_nrf52832.overlay`，文件名中的下划线不表示命令行板目标也应沿用旧格式。

<a id="sample-output"></a>

### 28.4.1 示例输出（Sample Output）

```text
*** Booting Zephyr OS build v3.6.0-rc1-32-gba639ed6a893 ***
Temperature: 22.90 C
Temperature: 22.96 C
Temperature: 22.82 C
```

<a id="see-also"></a>

## 28.5 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/grove_temperature/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/grove_temperature/src/main.c)、[samples/sensor/grove_temperature/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/grove_temperature/prj.conf)、[samples/sensor/grove_temperature/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/grove_temperature/tests.yaml)、[samples/sensor/grove_temperature/boards/nrf52dk_nrf52832.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/grove_temperature/boards/nrf52dk_nrf52832.overlay)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/grove_temperature/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/grove_temperature/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/grove_temperature/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/grove_temperature/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P027_DS18B20单总线温度传感器示例.md) · [返回大纲](大纲.md) · [下一章](P029_HTS221温湿度传感器示例.md)
