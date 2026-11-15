---
id: learning.zephyr-docs.sensors.page-47
title: LSM6DSO惯性测量单元示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/lsm6dso/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lsmd6dso"></a>

# 第47章\_LSM6DSO惯性测量单元示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/lsm6dso/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 47.1 概述（Overview）

本示例将LSM6DSO惯性测量单元（Inertial Measurement Unit，IMU）中的加速度计（Accelerometer）和陀螺仪（Gyroscope）数据率配置为12.5 Hz，并启用数据就绪触发（Data-ready trigger）。控制台显示加速度计和陀螺仪读数。

<a id="requirements"></a>

## 47.2 要求（Requirements）

示例使用通过I2C接口控制的LSM6DSO。原文说明已在[STM32L562E-DK Discovery](https://docs.zephyrproject.org/latest/boards/st/stm32l562e_dk/doc/index.html#stm32l562e_dk)上测试。

<a id="references"></a>

## 47.3 参考资料（References）

LSM6DSO：[ST官方产品资料](https://www.st.com/en/mems-and-sensors/lsm6dso.html)。

<a id="building-and-running"></a>

## 47.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，终端及工具链按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

项目将传感器数据输出到控制台，需要LSM6DSO；[STM32L562E-DK Discovery](https://docs.zephyrproject.org/latest/boards/st/stm32l562e_dk/doc/index.html#stm32l562e_dk)开发板具有该器件。

<a id="building-on-stm32l562e-dk-board"></a>

### 47.4.1 在stm32l562e\_dk开发板上构建（Building on stm32l562e\_dk board）

```sh
west build -b stm32l562e_dk samples/sensor/lsm6dso
```

> 译注——触发与轮询：当前`prj.conf`选择全局线程（Global thread）触发模式，回调读取并打印数据。源码也保留未启用触发时的轮询分支，每次输出后休眠1秒。因此改变触发配置也会改变控制台输出节拍。

<a id="sample-output"></a>

### 47.4.2 示例输出（Sample Output）

```text
Testing LSM6DSO sensor in trigger mode.

accel x:-0.650847 ms/2 y:-5.300102 ms/2 z:-8.163114 ms/2
gyro x:-0.167835 dps y:-0.063377 dps z:0.002367 dps
trig_cnt:1

accel x:0.341575 ms/2 y:5.209773 ms/2 z:-7.938787 ms/2
gyro x:-0.034284 dps y:-0.004428 dps z:-0.003512 dps
trig_cnt:2

<repeats endlessly>
```

以上输出不断重复（`<repeats endlessly>`）。

> 译注——原始单位标签：原日志的加速度标签`ms/2`应按通道定义理解为m/s²；陀螺仪标签`dps`与当前实现不同，当前`main.c`已输出`rad/s`，驱动也将角速度转换为rad/s。保留旧日志是为了对应原页，不代表这些旧标签适用于当前版本。

> 译注——频率参数表示：源码将`12.5`赋给整数成员`odr_attr.val1`，`val2`设为0；实际传入整数部分为12。当前驱动用整数数据率映射表中的12选择相应档位。这里需结合驱动理解，不能将写入整数成员的小数写法推广为通用`struct sensor_value`用法；该类型的通用数值表示是`val1 + val2 / 1000000`。

<a id="see-also"></a>

## 47.5 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/lsm6dso/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lsm6dso/src/main.c)、[samples/sensor/lsm6dso/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lsm6dso/prj.conf)、[samples/sensor/lsm6dso/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lsm6dso/tests.yaml)、[include/zephyr/drivers/sensor.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/sensor.h)、[drivers/sensor/st/lsm6dso/lsm6dso.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/sensor/st/lsm6dso/lsm6dso.c)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/lsm6dso/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lsm6dso/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/lsm6dso/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/lsm6dso/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P046_LSM6DSL惯性测量单元示例.md) · [返回大纲](大纲.md) · [下一章](P048_AMG88XX红外阵列传感器示例.md)
