---
id: learning.zephyr-docs.sensors.page-37
title: TI_TMP11X温度传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/tmp11x/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ti-tmp11x-sample"></a>
<a id="id1"></a>

# 第37章\_TI\_TMP11X温度传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/tmp11x/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="description"></a>

## 37.1 说明（Description）

本示例周期性使用`ti_tmp11x`传感器驱动获取温度，将结果写到控制台。示例还包含使用TMP117及TMP119特性的代码；这两种传感器与TMP116相近。

<a id="requirements"></a>

## 37.2 要求（Requirements）

需要TI TMP116、TI TMP117或TI TMP119传感器，连接到目标开发板的I2C接口。

<a id="wiring"></a>

## 37.3 接线（Wiring）

原文报告本示例使用Nucleo STM32F401RE开发板测试。传感器使用3.3 V供电，通过I2C与开发板通信。外部连线为：

| 传感器转接板（Breakout）引脚 | Nucleo引脚 |
| --- | --- |
| GND | GND |
| VCC | 3V3 |
| SDA | CN5-D14 |
| SCL | CN5-D15 |

<a id="building-and-running"></a>

## 37.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，使用已完成官方入门配置的UCRT64 Bash或Linux Bash终端。构建成功只表示固件生成；烧录和读取真实温湿度还需要正确的目标板、传感器节点及接线。若设备未就绪或读取失败，先检查节点状态、驱动配置和总线连接。

将开发板通过USB连接电脑，然后执行以下命令构建并烧录：

```sh
west build -b nucleo_f401re samples/sensor/tmp11x
west flash
```

> 译注——当前设备树与功能：随附的`nucleo_f401re.overlay`将`ti,tmp11x`设备放在I2C地址`0x4b`，并提供只读EEPROM子节点。当前应用同时取得温度与EEPROM设备，先读取EEPROM内容，再尝试设置温度偏移（Offset）；偏移属性仅由TMP117和TMP119支持，TMP116的属性不支持消息不等于温度读取本身失败。实际地址应与硬件地址选择一致，不能只按器件系列名称套用。

<a id="sample-output"></a>

## 37.5 示例输出（Sample Output）

通过终端模拟器（Terminal emulator，例如minicom）查看输出。USB连接后，在Linux上打开`/dev/ttyACM0`，串口参数如下：

- 波特率（Baud rate）：115200。
- 校验（Parity）：无。
- 数据位（Data bits）：8。
- 停止位（Stop bits）：1。

输出应类似：

```text
Device TMP11X - 0x200010a8 is ready
temp is 26.7031250 oC
temp is 26.7109375 oC
...
```

> 译注——输出版本：上方保留原页的温度日志。当前实现还打印EEPROM读取结果和偏移设置结果，并用`%d.%d`直接拼接`val1`、`val2`；其中`val2`仍按百万分之一表示，不能将没有补零的数字串始终理解为正确的小数格式。`/dev/ttyACM0`是原文Linux串口设备节点，不是作者仓库绝对路径；其他系统应选择实际出现的串口。


> 译注——实现依据：[samples/sensor/tmp11x/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/tmp11x/src/main.c)、[samples/sensor/tmp11x/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/tmp11x/prj.conf)、[samples/sensor/tmp11x/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/tmp11x/tests.yaml)、[samples/sensor/tmp11x/boards/nucleo_f401re.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/tmp11x/boards/nucleo_f401re.overlay)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/tmp11x/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/tmp11x/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/tmp11x/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/tmp11x/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P036_TMP112温度传感器示例.md) · [返回大纲](大纲.md) · [下一章](P038_BMG160三轴陀螺仪示例.md)
