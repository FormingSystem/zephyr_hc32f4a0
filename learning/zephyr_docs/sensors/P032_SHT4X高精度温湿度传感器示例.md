---
id: learning.zephyr-docs.sensors.page-32
title: SHT4X高精度温湿度传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/sht4x/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="sht4x-high-accuracy-digital-i2c-humidity-sensor"></a>
<a id="sht4x"></a>

# 第32章\_SHT4X高精度温湿度传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/sht4x/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="description"></a>

## 32.1 说明（Description）

本示例周期性读取SHT4X设备的环境温度及湿度，将结果写到控制台。

SHT4X带有可选加热器（Heater），可用于特定环境或应用，详情参阅数据手册。要使用加热器，检查本应用的Kconfig选项。

> 译注——加热器配置：应用通过`CONFIG_APP_USE_HEATER`启用该分支。相关选项包括湿度阈值`CONFIG_APP_HEATER_HUMIDITY_THRESH`、功率档位`CONFIG_APP_HEATER_PULSE_POWER`和长脉冲选择`CONFIG_APP_HEATER_PULSE_DURATION_LONG`。当前示例只在湿度整数部分超过阈值、温度整数部分低于驱动定义的上限时调用带加热的获取接口；随后只更新湿度，保留加热前的温度读数。Kconfig帮助要求加热占空比（Duty cycle）不超过5%，不能把加热器当作可持续开启的普通输出。

<a id="references"></a>

## 32.2 参考资料（References）

[SHT4X传感器官方资料](https://sensirion.com/products/catalog/SHT45)。

<a id="wiring"></a>

## 32.3 接线（Wiring）

通过I2C接口控制SHT4X。连接电源引脚`VDD`、`GND`及接口引脚`SDA`、`SCL`。供电范围为1.7—3.6 V。根据底板，SDA和SCL可能需要上拉电阻（Pull-up resistor）。

<a id="building-and-running"></a>

## 32.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，使用已完成官方入门配置的UCRT64 Bash或Linux Bash终端。构建成功只表示固件生成；烧录和读取真实温湿度还需要正确的目标板、传感器节点及接线。若设备未就绪或读取失败，先检查节点状态、驱动配置和总线连接。

项目需要实际SHT4X传感器并向控制台输出数据；原文说明它应可用于具有I2C外设接口的平台。示例提供[Black Pill V2.0](https://docs.zephyrproject.org/latest/boards/weact/blackpill_f411ce/doc/index.html#blackpill_f411ce)开发板的设备树覆盖文件。

```sh
# From the root of the zephyr repository
west build -b blackpill_f411ce samples/sensor/sht4x
west flash
```

> 译注——间隔选项名称：当前Kconfig定义的是`APP_HEATER_PULSE_DURATION_LONG`，而主循环休眠分支检查`CONFIG_APP_HEATER_PULSE_DURATION`。两处名称不一致，不能依据该分支认定长／短脉冲会自动获得预期的不同等待间隔。复现加热功能前应核对所用版本的实际配置与驱动约束；本文未更改源码或开启硬件加热。

<a id="sample-output"></a>

### 32.4.1 示例输出（Sample Output）

```text
*** Booting Zephyr OS build v2.6.0-rc1-315-g50d8d1187138  ***
SHT4X: 23.64 Temp. [C] ; 30.74 RH [%]
SHT4X: 23.66 Temp. [C] ; 32.16 RH [%]
SHT4X: 23.63 Temp. [C] ; 30.83 RH [%]
```

数据手册说明，温度和湿度分别以摄氏度及相对湿度百分比表示。


> 译注——实现依据：[samples/sensor/sht4x/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sht4x/src/main.c)、[samples/sensor/sht4x/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sht4x/prj.conf)、[samples/sensor/sht4x/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sht4x/tests.yaml)、[samples/sensor/sht4x/boards/blackpill_f411ce.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sht4x/boards/blackpill_f411ce.overlay)、[samples/sensor/sht4x/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sht4x/Kconfig)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/sht4x/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sht4x/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/sht4x/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/sht4x/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P031_SHT3XD温湿度传感器示例.md) · [返回大纲](大纲.md) · [下一章](P033_TH02温湿度传感器示例.md)
