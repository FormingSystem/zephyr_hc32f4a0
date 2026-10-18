---
id: learning.zephyr-docs.hardware.i3csamples-1
title: LPS22HH的I3C示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/lps22hh_i3c/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="lps22hh_i3c"></a>

# 第431章\_LPS22HH的I3C示例

原文：[LPS22HH Temperature and Pressure Sensor (I3C)](https://docs.zephyrproject.org/latest/samples/sensor/lps22hh_i3c/README.html)。读取日期：2026-10-13，`latest`。

## 431.1\_概述与要求

本示例周期性读取 LPS22HH **微机电系统（Micro-Electro-Mechanical Systems，MEMS）**压力传感器的数据，并在控制台显示压力和温度。

示例通过**改进型集成电路互连（Improved Inter-Integrated Circuit，I3C）**接口控制 LPS22HH。官方已使用 STEVALMKI192-V1 评估板上的 LPS22HH，将其接到 [MIMXRT685-EVK](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt685_evk/doc/index.html#mimxrt685_evk) 的 I3C 接口进行测试。器件资料见 [ST 的 LPS22HH 产品页](https://www.st.com/en/mems-and-sensors/lps22hh.html)。

## 431.2\_构建与运行

工程向控制台输出传感器数据，需要连接 LPS22HH，例如 STEVALMKI192-V1 上的器件。

如果启用配置项 `CONFIG_LPS22HH_TRIGGER`，触发器（Trigger）通过 I3C **带内中断（In-Band Interrupt，IBI）**通知新数据就绪。IBI 由传感器发起，它会取得 I3C 总线的控制。因此，**烧录新镜像时需要重新断电上电，让传感器复位并停止继续产生 IBI**。否则，I3C 控制器将无法初始化，示例也就无法与传感器通信。

在 Zephyr 仓库根目录的开发终端，为 `mimxrt685_evk` 板构建：

```shell
west build -b mimxrt685_evk/mimxrt685s/cm33 samples/sensor/lps22hh_i3c
```

## 431.3\_开发板与传感器准备

MIMXRT685-EVK 的 I3C 引脚从 J18 连接器引出。**串行时钟（Serial Clock，SCL）**、**串行数据（Serial Data，SDA）**及其他针脚如下。

| J18 针脚 | 功能 |
| --- | --- |
| 1 | SCL |
| 2 | SDA |
| 3 | 内部上拉（Internal Pull-up），已连接至针脚 2 |
| 4 | 地（Ground） |

将 LPS22HH 接到该接口，例如使用 STEVAL-MKI192V1 评估板。需要把传感器配置为地址 `0x5D`，左移一位后的值为 `0xBA`。译注：两个写法表示原文明确区分的地址形式，不应在接口参数中不加区分地替换。

## 431.4\_示例输出与参考

以下为官方控制台输出，配置为以 1 Hz 触发采集（Triggered Collection）。`Observation` 为观测序号，`Pressure` 为压力，`Temperature` 为温度；kPa 表示千帕，C 表示摄氏温度。输出每秒持续重复。

```text
Configured for triggered collection at 1 Hz
Observation: 1
Pressure: 97.474 kPa
Temperature: 22.19 C
Observation: 2
Pressure: 97.466 kPa
Temperature: 22.21 C
Observation: 3
Pressure: 97.473 kPa
Temperature: 22.21 C
Observation: 4
Pressure: 97.455 kPa
Temperature: 22.21 C

<repeats endlessly every second>
```

另见[传感器接口（Sensor Interface）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)和[示例源代码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/sensor/lps22hh_i3c)。

---

[上一章：P3T1755DP扩展板](P430_P3T1755DP扩展板.md) · [下一章：I3C总线上的LSM6DSO示例](P432_I3C总线上的LSM6DSO示例.md) · [返回大纲](大纲.md)
