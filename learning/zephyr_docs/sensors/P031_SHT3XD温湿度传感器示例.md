---
id: learning.zephyr-docs.sensors.page-31
title: SHT3XD温湿度传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/sht3xd/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="sht3xd"></a>

# 第31章\_SHT3XD温湿度传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/sht3xd/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="description"></a>

## 31.1 说明（Description）

本示例周期性地以2 Hz测量环境温度及湿度，并将结果写到控制台。也可选择演示上阈值触发器（Upper threshold trigger）的使用。

> 译注——频率差异：原文为2 Hz；当前`main.c`每次读取后执行`k_sleep(K_MSEC(2000))`，即约每2秒一轮，不能将它解释为每秒两次。本文保留原文频率并给出实现依据。

<a id="references"></a>

## 31.2 参考资料（References）

[SHT3X-DIS传感器官方资料](https://sensirion.com/products/catalog/SHT31-DIS-B)。

<a id="wiring"></a>

## 31.3 接线（Wiring）

通过I2C接口控制SHT3X_DIS传感器。连接电源引脚`VDD`、`GND`和接口引脚`SDA`、`SCL`；可选地将`ALERT`接到支持中断的GPIO。供电电压范围为2.15—5.5 V。根据底板，SDA及SCL可能需要上拉电阻（Pull-up resistor）。

<a id="building-and-running"></a>

## 31.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，使用已完成官方入门配置的UCRT64 Bash或Linux Bash终端。构建成功只表示固件生成；烧录和读取真实温湿度还需要正确的目标板、传感器节点及接线。若设备未就绪或读取失败，先检查节点状态、驱动配置和总线连接。

项目需要实际SHT3XD传感器，向控制台输出数据。原文说明它应可用于具有I2C外设接口的平台，不能在QEMU中运行。以下示例使用[BLE400](https://docs.zephyrproject.org/latest/boards/waveshare/nrf51_ble400/doc/index.html#nrf51_ble400)开发板：

```sh
# From the root of the zephyr repository
west build -b nrf51_ble400 samples/sensor/sht3xd
west flash
```

> 译注——告警通道：当前可选触发路径由`CONFIG_SHT3XD_TRIGGER`控制，作用于湿度通道`SENSOR_CHAN_HUMIDITY`，配置50 %RH下阈值及60 %RH上阈值；它不是温度超过某个数值的告警。

<a id="sample-output"></a>

### 31.4.1 示例输出（Sample Output）

```text
SHT3XD: 19.64 Cel ; 41.96 %RH
SHT3XD: 19.74 Cel ; 42.06 %RH
SHT3XD: 19.75 Cel ; 42.08 %RH
```

输出不断重复（`<repeats endlessly>`）。`%RH`表示相对湿度百分比（Relative humidity）。

<a id="see-also"></a>

## 31.5 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/sht3xd/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sht3xd/src/main.c)、[samples/sensor/sht3xd/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sht3xd/prj.conf)、[samples/sensor/sht3xd/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sht3xd/tests.yaml)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/sht3xd/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sht3xd/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/sht3xd/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/sht3xd/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P030_JEDEC温度传感器示例.md) · [返回大纲](大纲.md) · [下一章](P032_SHT4X高精度温湿度传感器示例.md)
