---
id: learning.zephyr-docs.sensors.page-39
title: BMI270六轴IMU示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/bmi270/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bmi270"></a>

# 第39章\_BMI270六轴IMU示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/bmi270/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="description"></a>

## 39.1 说明（Description）

本示例将加速度计（Accelerometer）和陀螺仪（Gyroscope）的数据采样频率配置为100 Hz，并将结果写到控制台。BMI270是六轴惯性测量单元（6-axis Inertial Measurement Unit，IMU）。

示例可用于任何具有已启用设备树（Devicetree）节点的开发板，或开发板与扩展板（Shield）的组合；该节点的兼容字符串（Compatible string）为[`bosch,bmi270`](https://docs.zephyrproject.org/latest/build/dts/api/compatibles/bosch,bmi270.html#std-dtcompatible-bosch-bmi270)。

<a id="references"></a>

## 39.2 参考资料（References）

BMI270：[Bosch官方产品资料](https://www.bosch-sensortec.com/products/motion-sensors/imus/bmi270/)。

<a id="building-and-running"></a>

## 39.3 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，终端及工具链按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

项目向控制台输出传感器数据，需要实际BMI270传感器。原文说明它应可用于具有I2C外设接口的平台，不能在QEMU中运行。以下示例使用[nRF52840 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#nrf52840dk)开发板：

```sh
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 samples/sensor/bmi270
west flash
```

> 译注——采样与输出：当前实现将加速度量程配置为2 g、陀螺仪量程配置为500 °/s，再分别设置100 Hz采样频率；应用循环先休眠10毫秒，再获取并打印数据。因此控制台每行之间的间隔还包括读取和打印耗时，不能据此认定日志严格以100 Hz输出。量程中的g和°/s也不等于通道读数单位：传感器API定义加速度为m/s²、角速度为rad/s。

<a id="sample-output"></a>

### 39.3.1 示例输出（Sample Output）

```text
Device 0x200014cc name is BMI270
AX: 0.268150; AY: 0.076614; AZ: 9.730035; GX: 0.001065; GY: -0.005326; GZ: -0.004261;
AX: 0.229843; AY: 0.076614; AZ: 9.806650; GX: 0.000532; GY: -0.005592; GZ: -0.002929;
AX: 0.229843; AY: 0.076614; AZ: 9.806650; GX: 0.000266; GY: -0.006125; GZ: -0.002663;
AX: 0.306457; AY: 0.038307; AZ: 9.768342; GX: 0.001331; GY: -0.005326; GZ: -0.004793;

<repeats endlessly>
```

以上输出不断重复（`<repeats endlessly>`）。`AX`、`AY`、`AZ`对应三轴加速度，`GX`、`GY`、`GZ`对应三轴角速度。

<a id="see-also"></a>

## 39.4 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/bmi270/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/bmi270/src/main.c)、[samples/sensor/bmi270/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/bmi270/prj.conf)、[samples/sensor/bmi270/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/bmi270/tests.yaml)、[include/zephyr/drivers/sensor.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/sensor.h)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/bmi270/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/bmi270/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/bmi270/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/bmi270/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P038_BMG160三轴陀螺仪示例.md) · [返回大纲](大纲.md) · [下一章](P040_FXAS21002陀螺仪示例.md)
