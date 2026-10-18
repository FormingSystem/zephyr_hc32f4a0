---
id: learning.zephyr-docs.hardware.i3csamples-3
title: IKS4A1标准I3C示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/shields/x_nucleo_iks4a1/standard_i3c/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="x-nucleo-iks4a1-std-i3c"></a>

# 第433章\_IKS4A1标准I3C示例

原文：[X-NUCLEO-IKS4A1 shield - Standard (Mode 1 + I3C)](https://docs.zephyrproject.org/latest/samples/shields/x_nucleo_iks4a1/standard_i3c/README.html)。读取日期：2026-10-13，`latest`。

## 433.1\_概述

本示例用于测试 X-NUCLEO-IKS4A1 扩展板（Shield）在标准模式（Standard Mode，即 Mode 1）下启用 **I3C（Improved Inter-Integrated Circuit，改进型集成电路互连）**接口的运行情况。

它启用扩展板上的四个传感器，周期性读取并显示数据：

| 传感器 | 测量内容 |
| --- | --- |
| LSM6DSV16X | 六轴加速度与角速度（Acceleration and Angular Velocity） |
| LSM6DSO16IS | 六轴加速度与角速度 |
| LPS22DF | 环境温度与大气压力（Ambient Temperature and Atmospheric Pressure） |
| LIS2MDL | 三轴磁场强度（Magnetic Field Intensity） |

## 433.2\_要求

示例通过 I3C 与扩展板通信，目标开发板需要提供支持 I3C 的 Arduino 连接器。示例配置使用 `x_nucleo_iks4a1_i3c` 扩展板变体（Shield Variant），并为 [Nucleo H503RB](https://docs.zephyrproject.org/latest/boards/st/nucleo_h503rb/doc/index.html#nucleo_h503rb) 提供设备树覆盖文件（Devicetree Overlay）。

## 433.3\_构建与运行

将 X-NUCLEO-IKS4A1 堆叠安装到具有匹配 Arduino 连接器和 I3C 总线的开发板上。官方例子使用 Nucleo H503RB。以下命令在 Zephyr 仓库根目录的开发终端执行：第一行构建，第二行烧录（Flash）。

```shell
west build -b nucleo_h503rb samples/shields/x_nucleo_iks4a1/standard_i3c/
west flash
```

## 433.4\_示例输出

官方传感器仪表板（Sensor Dashboard）输出如下，每 2 秒持续更新。`Magn` 表示磁场，G 为高斯（Gauss）；`Accel` 表示加速度，单位为米每二次方秒；`Gyro` 表示角速度，单位为弧度每秒；`Temperature` 表示温度，`Pressure` 表示压力，`trig` 表示触发计数。

```text
X-NUCLEO-IKS4A1 sensor dashboard

LIS2MDL: Magn (G): x: -0.261, y: -0.339, z: -0.261
LIS2MDL: Temperature: 24.6 C
LSM6DSO16IS: Accel (m/s^2): x: 0.177, y: -0.024, z: 9.882
LSM6DSO16IS: Gyro (rad/s): x: 0.049, y: -0.063, z: -0.033
LSM6DSO16IS: Temperature: 27.9 C
LSM6DSV16X: Accel (m/s^2): x: 0.067, y: 0.167, z: 9.820
LSM6DSV16X: Gyro (rad/s): x: -0.005, y: 0.005, z: 0.004
LSM6DSV16X: Temperature: 27.0 C
LPS22DF: Temperature: 27.1 C
LPS22DF: Pressure:102.202 kPa

2: lis2mdl trig 215
2: lsm6dsv16x acc trig 467

<updated endlessly every 2 seconds>
```

## 433.5\_参考资料

- [X-NUCLEO-IKS4A1：MEMS 惯性与环境多传感器扩展板](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_iks4a1/doc/index.html#x-nucleo-iks4a1)。MEMS 为微机电系统（Micro-Electro-Mechanical Systems）。
- [传感器接口（Sensor Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。
- [示例源代码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/shields/x_nucleo_iks4a1/standard_i3c)。

---

[上一章：I3C总线上的LSM6DSO示例](P432_I3C总线上的LSM6DSO示例.md) · [下一章：RTIO的I3C标志](P434_RTIO的I3C标志.md) · [返回大纲](大纲.md)
