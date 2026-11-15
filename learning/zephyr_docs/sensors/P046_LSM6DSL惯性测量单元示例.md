---
id: learning.zephyr-docs.sensors.page-46
title: LSM6DSL惯性测量单元示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/lsm6dsl/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lsmd6dsl"></a>

# 第46章\_LSM6DSL惯性测量单元示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/lsm6dsl/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 46.1 概述（Overview）

本示例将LSM6DSL惯性测量单元（Inertial Measurement Unit，IMU）中的加速度计（Accelerometer）和陀螺仪（Gyroscope）设为104 Hz，并启用数据就绪触发（Data-ready trigger）。控制台显示加速度计和陀螺仪读数；还可以通过传感器集线器功能（Sensor hub）显示连接到LSM6DSL的磁力计（Magnetometer）或压力传感器（Pressure sensor）读数。

<a id="requirements"></a>

## 46.2 要求（Requirements）

示例使用通过I2C或SPI接口控制的LSM6DSL。原文说明已在[Argonkey](https://docs.zephyrproject.org/latest/boards/96boards/argonkey/doc/index.html#96b_argonkey)和[Disco L475 IOT01 (B-L475E-IOT01A)](https://docs.zephyrproject.org/latest/boards/st/disco_l475_iot1/doc/index.html#disco_l475_iot1)上测试。

<a id="references"></a>

## 46.3 参考资料（References）

LSM6DSL：[ST官方产品资料](https://www.st.com/en/mems-and-sensors/lsm6dsl.html)。

<a id="building-and-running"></a>

## 46.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，终端及工具链按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

本项目将传感器数据输出到控制台，需要LSM6DSL；[Argonkey](https://docs.zephyrproject.org/latest/boards/96boards/argonkey/doc/index.html#96b_argonkey)和[Disco L475 IOT01 (B-L475E-IOT01A)](https://docs.zephyrproject.org/latest/boards/st/disco_l475_iot1/doc/index.html#disco_l475_iot1)开发板均具有该传感器。

<a id="building-on-argonkey-board"></a>

### 46.4.1 在ArgonKey开发板上构建（Building on ArgonKey board）

```sh
west build -b 96b_argonkey samples/sensor/lsm6dsl
```

<a id="building-on-disco-l475-iot1-board"></a>

### 46.4.2 在disco\_l475\_iot1开发板上构建（Building on disco\_l475\_iot1 board）

```sh
west build -b disco_l475_iot1 samples/sensor/lsm6dsl
```

<a id="building-on-nrf52840dk-nrf52840-board-with-x-nucleo-iks01a2-shield"></a>

### 46.4.3 使用x-nucleo-iks01a2扩展板在nrf52840dk/nrf52840上构建（Building on nrf52840dk/nrf52840 board with x-nucleo-iks01a2 shield）

```sh
west build -b nrf52840dk/nrf52840 --shield x_nucleo_iks01a2 samples/sensor/lsm6dsl
```

<a id="sample-output"></a>

### 46.4.4 示例输出（Sample Output）

```text
LSM6DSL sensor samples:

accel (-3.184000 -0.697000 9.207000) m/s2
gyro (0.065000 -0.029000 0.002000) dps
magn (-0.042000 0.294000 -0.408000) G
- (0) (trig_cnt: 190474)

<repeats endlessly every 2 seconds>
```

以上输出每2秒不断重复（`<repeats endlessly every 2 seconds>`）。

> 原文说明（Note）：`magn`行只在`96b_argonkey`开发板运行此示例时显示，因为该板上有连接到LSM6DSL的磁力计。

> 译注——读取与显示节拍：当前实现仍请求104 Hz采样，并在触发回调中读取数据；主循环每2秒输出一次缓存值。104 Hz不是控制台刷新频率。可选磁场输出由`CONFIG_LSM6DSL_EXT0_LIS2MDL`控制；压力／温度输出由`CONFIG_LSM6DSL_EXT0_LPS22HB`控制，需有对应外接设备和配置。

> 译注——陀螺仪单位：原日志标为`dps`，当前示例打印字符串中也保留此标签，但驱动`lsm6dsl_gyro_convert()`已把角速度转换为rad/s，示例没有再转换成°/s。对当前实现应按rad/s理解；原始日志保持不变。加速度的规范单位是m/s²，磁场的`G`是高斯（Gauss），与加速度量程中的g含义不同。

<a id="see-also"></a>

## 46.5 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/lsm6dsl/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lsm6dsl/src/main.c)、[samples/sensor/lsm6dsl/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lsm6dsl/prj.conf)、[samples/sensor/lsm6dsl/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lsm6dsl/tests.yaml)、[include/zephyr/drivers/sensor.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/sensor.h)、[drivers/sensor/st/lsm6dsl/lsm6dsl.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/sensor/st/lsm6dsl/lsm6dsl.c)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/lsm6dsl/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lsm6dsl/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/lsm6dsl/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/lsm6dsl/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P045_LSM303DLHC磁力计与加速度计示例.md) · [返回大纲](大纲.md) · [下一章](P047_LSM6DSO惯性测量单元示例.md)
