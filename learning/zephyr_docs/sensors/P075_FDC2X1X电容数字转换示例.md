---
id: learning.zephyr-docs.sensors.page-75
title: FDC2X1X电容数字转换示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/fdc2x1x/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="fdc2x1x"></a>

# 第75章\_FDC2X1X电容数字转换示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/fdc2x1x/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 75.1 概述（Overview）

本示例采用轮询模式（Polling mode），也可选择数据就绪触发（Data-ready trigger），周期性读取FDC2X1X的频率和电容。它支持12位与28位、2通道与4通道版本，包括FDC2112、FDC2114、FDC2212和FDC2214。通过设备树属性选择4通道版本；本示例默认采用2通道版本。

电容检测（Capacitive sensing）是一种低功耗、低成本、高分辨率的非接触检测技术，可用于接近检测、手势识别及远程液位检测等。检测系统的感测元件可以是任何金属或导体，使系统设计具有较低成本和较高灵活性。

限制电容检测灵敏度的主要问题是传感器容易受到噪声影响。原文说明，FDC2x1x的抗电磁干扰（Electromagnetic Interference，EMI）架构可在高噪声环境中维持性能。

<a id="wiring"></a>

## 75.2 接线（Wiring）

本示例通过I2C接口控制FDC2X1X。

- 连接供电引脚`VDD`与`GND`；供电范围为2.7 V至3.6 V。
- 将`SD`连接到GPIO，以控制关断模式（Shutdown Mode）。
- 连接`SDA`和`SCL`；如需中断，可将`INTB`连接到支持中断的GPIO。

详细说明见[FDC2X1X数据手册](https://www.ti.com/lit/gpn/fdc2114)第4～5页。

<a id="building-and-running"></a>

## 75.3 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行；Windows使用UCRT64 Bash，Linux使用原生Bash，主机工具、模块与目标工具链先按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

示例向控制台输出传感器数据，可使用任意串口控制台程序读取。它应可用于具有I2C接口的平台，但所用平台必须提供定制的设备树覆盖文件（Devicetree overlay）。

原文以[nRF9160 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf9160dk/doc/index.html#nrf9160dk)为例；随附覆盖文件提供评估设置，可作为其他平台的配置参考。

```sh
west build -b nrf9160dk/nrf9160 samples/sensor/fdc2x1x
west flash
```

> 译注——通道数与节拍：当前覆盖文件定义两个通道子节点，主程序按这些节点建立通道数组；换用4通道器件还须配置匹配的设备树内容。普通轮询分支每次休眠100 ms，触发分支等待数据就绪信号量；如另外启用设备电源管理测试，程序会增加2秒关闭（Turn off）过程，不能把所有配置都视为固定10 Hz输出。

<a id="sample-output-2-channel-28-bit-fdc2212"></a>

### 75.3.1 2通道、28位示例输出（Sample Output: 2-Channel, 28-Bit (FDC2212)）

```text
ch0: 5.318888 MHz ch1: 5.150293 MHz
ch0: 49.742308 pF ch1: 53.052260 pF

ch0: 5.318819 MHz ch1: 5.150307 MHz
ch0: 49.743612 pF ch1: 53.051964 pF

ch0: 5.318822 MHz ch1: 5.150200 MHz
ch0: 49.743548 pF ch1: 53.054176 pF

ch0: 5.318752 MHz ch1: 5.150265 MHz
ch0: 49.744860 pF ch1: 53.052828 pF

<repeats endlessly>
```

`<repeats endlessly>`表示上述输出持续重复。

<a id="sample-output-4-channel-12-bit-fdc2114"></a>

### 75.3.2 4通道、12位示例输出（Sample Output: 4-Channel, 12-Bit (FDC2114)）

```text
ch0: 4.966171 MHz ch1: 4.946465 MHz ch2: 4.985879 MHz ch3: 4.907051 MHz
ch0: 57.059016 pF ch1: 57.514568 pF ch2: 56.608844 pF ch3: 58.442204 pF

ch0: 4.966171 MHz ch1: 4.946465 MHz ch2: 4.985879 MHz ch3: 4.907051 MHz
ch0: 57.059016 pF ch1: 57.514568 pF ch2: 56.608844 pF ch3: 58.442204 pF

ch0: 4.966171 MHz ch1: 4.946465 MHz ch2: 4.985879 MHz ch3: 4.907051 MHz
ch0: 57.059016 pF ch1: 57.514568 pF ch2: 56.608844 pF ch3: 58.442204 pF

ch0: 4.966171 MHz ch1: 4.946465 MHz ch2: 4.985879 MHz ch3: 4.907051 MHz
ch0: 57.059016 pF ch1: 57.514568 pF ch2: 56.608844 pF ch3: 58.442204 pF

<repeats endlessly>
```

上述输出同样持续重复。

> 译注——专用通道单位：FDC2X1X扩展接口明确规定频率通道使用MHz，电容通道使用皮法（Picofarad，pF）。日志中的`ch0`至`ch3`是通道编号，不同于通用传感器接口中其他频率量的单位约定。

<a id="references"></a>

## 75.4 参考资料（References）

FDC2X1X数据手册及产品信息：[TI FDC2114官方资料](https://www.ti.com/product/FDC2114)。

<a id="see-also"></a>

## 75.5 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/fdc2x1x/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/fdc2x1x/src/main.c)、[samples/sensor/fdc2x1x/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/fdc2x1x/prj.conf)、[samples/sensor/fdc2x1x/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/fdc2x1x/tests.yaml)、[samples/sensor/fdc2x1x/boards/nrf9160dk_nrf9160.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/fdc2x1x/boards/nrf9160dk_nrf9160.overlay)、[include/zephyr/drivers/sensor/fdc2x1x.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/sensor/fdc2x1x.h)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/fdc2x1x/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/fdc2x1x/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/fdc2x1x/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/fdc2x1x/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P074_MAX17262电量计示例.md) · [返回大纲](大纲.md) · [下一章](P076_MTCH9010液体泄漏检测示例.md)
