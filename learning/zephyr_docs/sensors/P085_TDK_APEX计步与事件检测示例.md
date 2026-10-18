---
id: learning.zephyr-docs.sensors.page-85
title: TDK_APEX计步与事件检测示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/tdk_apex/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="tdk_apex"></a>

# 第85章\_TDK\_APEX计步与事件检测示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/tdk_apex/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 85.1 概述（Overview）

本示例演示TDK Invensense传感器的高级计步与事件检测（Advanced Pedometer and Event Detection，APEX）功能：

- 计步器（Pedometer）：跟踪步数，并提供步频（Cadence）及估计的活动类型，包括行走（Walk）、跑步（Run）和未知（Unknown）。
- 倾斜检测（Tilt Detection）：开发板倾斜30度或以上，并保持该姿态4秒后产生倾斜事件。
- 运动唤醒（Wake on Motion，WoM）：检测各轴超过195 mg阈值的运动。
- 显著运动检测器（Significant Motion Detector，SMD）：检测显著移动。

通过设备树配置APEX功能支持。

> 译注——加速度单位：此处`mg`是千分之一重力加速度g，195 mg即0.195 g，不是质量单位毫克。

<a id="references"></a>

## 85.2 参考资料（References）

[TDK应用笔记AN-000271：ICM-42607x及ICM-42670x的APEX运动功能说明与用法](https://invensense.tdk.com/download-pdf/an-000271-icm-42607x-and-icm-42670x-apex-motion-functions-description-and-usage/)。

<a id="driver-configuration"></a>

> 译注——外链状态：原TDK应用笔记入口本次返回404，网页工具也未能读取。检索到的旧官方PDF地址同样无法读取，因此保留原链接供追溯，未将搜索摘要视为完整手册核验。

## 85.3 驱动配置（Driver configuration）

APEX只依赖加速度计数据。TDK传感器驱动将加速度计配置为低功耗模式（Low-power mode），并设置APEX工作频率为25 Hz或50 Hz。

<a id="wiring"></a>

## 85.4 接线（Wiring）

示例使用外接传感器转接板。必须提供设备树覆盖文件，标明TDK传感器、SPI或I2C总线接口以及传感器中断GPIO。

<a id="building-and-running"></a>

## 85.5 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行；Windows使用UCRT64 Bash，Linux使用原生Bash，先按官方入门说明准备主机工具、模块与目标工具链。原生模拟目标还须满足相应主机环境要求；硬件分支需要目标板、设备树节点和接线。下方命令及日志来自官方文档，本次没有运行模拟器或硬件实验。

本示例支持TDK惯性测量单元（Inertial Measurement Unit，IMU）。原文要求将各设备设置为`tdk-apex-sensorN`别名，其中`N`取`0`到`9`，例如：

```dts
/ {
       aliases {
                       tdk-apex-sensor0 = &icm42670p;
               };
       };
```

需要按以下方式指定设备的APEX功能：

```dts
icm42670p: icm42670p@0 {
        apex = "pedometer";
}
```

确认所用APEX功能已写入设备树，然后构建并运行：

```sh
# From the root of the zephyr repository
west build -b nrf52dk/nrf52832 samples/sensor/tdk_apex
west flash
```

> 译注——当前设备选择与配置片段：当前主程序仅通过`DT_ALIAS(tdk_apex_sensor0)`取得一个设备，并未遍历0～9号全部别名。随附I2C与SPI覆盖文件分别给出完整节点及中断配置；上方小段只是展示别名和`apex`属性的原文片段，节点末尾也未写完整结束分号，不能当作完整覆盖文件单独编译。应选定实际接口对应的覆盖文件，再修改所需功能。

<a id="sample-output"></a>

### 85.5.1 示例输出（Sample Output）

**计步器（Pedometer）配置及输出：**

```dts
icm42670p: icm42670p@0 {
        apex = "pedometer";
}
```

```text
Found device "icm42670p@68", getting sensor data
[0:00:09.287]: STEP_DET     count: 6 steps  cadence: 2.0 steps/s  activity: Unknown
[0:00:09.689]: STEP_DET     count: 7 steps  cadence: 2.1 steps/s  activity: Walk
[0:00:10.051]: STEP_DET     count: 8 steps  cadence: 2.2 steps/s  activity: Walk
[0:00:10.433]: STEP_DET     count: 9 steps  cadence: 2.2 steps/s  activity: Walk
[0:00:10.835]: STEP_DET     count: 10 steps  cadence: 2.3 steps/s  activity: Walk

<repeats endlessly>
```

**倾斜检测（Tilt Detection）配置及输出：**

```dts
icm42670p: icm42670p@0 {
        apex = "tilt";
}
```

```text
Found device "icm42670p@68", getting sensor data
[0:00:15.249]: TILT
[0:00:21.479]: TILT
[0:00:26.765]: TILT

<repeats endlessly>
```

**运动唤醒（Wake on Motion）配置及输出：**

```dts
icm42670p: icm42670p@0 {
        apex = "wom";
}
```

```text
Found device "icm42670p@68", getting sensor data
[0:00:02.555]: WOM x=1 y=0 z=1
[0:00:02.636]: WOM x=0 y=0 z=1
[0:00:02.797]: WOM x=0 y=1 z=0
[0:00:02.877]: WOM x=0 y=0 z=1
[0:00:02.957]: WOM x=1 y=1 z=1

<repeats endlessly>
```

**显著运动检测（Significant Motion Detection）配置及输出：**

```dts
icm42670p: icm42670p@0 {
        apex = "smd";
}
```

```text
Found device "icm42670@68", getting sensor data
[0:00:04.622]: SMD
[0:00:05.084]: SMD
[0:00:05.566]: SMD

<repeats endlessly>
```

每组日志中的`<repeats endlessly>`表示对应事件输出可持续出现。

> 译注——事件与频率：当前程序注册`SENSOR_TRIG_MOTION`，回调读取事件并设置标志，主循环据此输出；25／50 Hz是APEX工作频率，不是承诺每秒打印25／50条事件。当前实现还包含敲击（Tap）分支，但原页没有该分支的配置及输出，本页不补造日志。

<a id="see-also"></a>

## 85.6 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/tdk_apex/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/tdk_apex/src/main.c)、[samples/sensor/tdk_apex/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/tdk_apex/prj.conf)、[samples/sensor/tdk_apex/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/tdk_apex/tests.yaml)、[samples/sensor/tdk_apex/boards/nrf52dk_nrf52832_i2c.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/tdk_apex/boards/nrf52dk_nrf52832_i2c.overlay)、[samples/sensor/tdk_apex/boards/nrf52dk_nrf52832_spi.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/tdk_apex/boards/nrf52dk_nrf52832_spi.overlay)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/tdk_apex/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/tdk_apex/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/tdk_apex/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/tdk_apex/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P084_TDK_TAD2144隧道磁阻角度传感器示例.md) · [返回大纲](大纲.md) · [下一章](P086_VEAA_X_3比例压力控制阀示例.md)
