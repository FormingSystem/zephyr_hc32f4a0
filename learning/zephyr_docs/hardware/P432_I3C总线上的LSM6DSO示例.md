---
id: learning.zephyr-docs.hardware.i3csamples-2
title: I3C总线上的LSM6DSO示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/lsm6dso_i2c_on_i3c/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="lsmd6dso_i2c_on_i3c"></a>

# 第432章\_I3C总线上的LSM6DSO示例

原文：[LSM6DSO IMU sensor (I2C on I3C bus)](https://docs.zephyrproject.org/latest/samples/sensor/lsm6dso_i2c_on_i3c/README.html)。读取日期：2026-10-13，`latest`。

## 432.1\_概述与要求

本示例将 LSM6DSO 的加速度计（Accelerometer）和陀螺仪（Gyroscope）数据速率设置为 12.5 Hz，并启用数据就绪触发（Data-ready Trigger），在控制台输出加速度和角速度。LSM6DSO 属于**惯性测量单元（Inertial Measurement Unit，IMU）**传感器。

这里使用 I3C 控制器提供的 **I2C（Inter-Integrated Circuit，集成电路互连）**接口控制器件，即在 **I3C（Improved Inter-Integrated Circuit，改进型集成电路互连）**总线上进行 I2C 通信。官方测试使用 STEVAL-MKI196V1 评估板上的 LSM6DSO，连接到 [MIMXRT685-EVK](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt685_evk/doc/index.html#mimxrt685_evk) 的 I3C 接口。

器件资料见 [ST 的 LSM6DSO 产品页](https://www.st.com/en/mems-and-sensors/lsm6dso.html)。

## 432.2\_构建与运行

工程向控制台输出传感器数据，需要 LSM6DSO，例如 STEVAL-MKI196V1 评估板上的器件。在 Zephyr 仓库根目录的开发终端，为 `mimxrt685_evk` 板构建：

```shell
west build -b mimxrt685_evk/mimxrt685s/cm33 samples/sensor/lsm6dso_i2c_on_i3c
```

## 432.3\_开发板与传感器准备

MIMXRT685-EVK 的 J18 连接器提供 I3C 总线引脚。**串行时钟（Serial Clock，SCL）**、**串行数据（Serial Data，SDA）**及其他针脚如下。

| J18 针脚 | 功能 |
| --- | --- |
| 1 | SCL |
| 2 | SDA |
| 3 | 内部上拉（Internal Pull-up），已连接至针脚 2 |
| 4 | 地（Ground） |

将 LSM6DSO 接到这一接口，例如使用 STEVAL-MKI196V1。需把传感器配置为地址 `0x6B`；左移一位后为 `0xD6`。译注：保留原文对地址形式的区分，不能把移位前后值随意用于同一个接口参数。

## 432.4\_示例输出与参考

官方输出如下，持续重复。`accel` 为加速度，`gyro` 为角速度，`trig_cnt` 为触发次数；`dps` 表示度每秒（Degrees per Second）。译注：原日志把加速度单位写成 `ms/2`，此处保留原始输出，不据此改动日志内容。

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

另见[传感器接口（Sensor Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)和[示例源代码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/sensor/lsm6dso_i2c_on_i3c)。

---

[上一章：LPS22HH的I3C示例](P431_LPS22HH的I3C示例.md) · [下一章：IKS4A1标准I3C示例](P433_IKS4A1标准I3C示例.md) · [返回大纲](大纲.md)
