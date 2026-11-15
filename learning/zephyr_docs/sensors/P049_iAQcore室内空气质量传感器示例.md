---
id: learning.zephyr-docs.sensors.page-49
title: iAQcore室内空气质量传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/ams_iAQcore/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ams_iaqcore"></a>

# 第49章\_iAQcore室内空气质量传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/ams_iAQcore/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 49.1 概述（Overview）

本示例演示如何使用ams iAQcore传感器测量等效二氧化碳（CO₂ equivalent）和挥发性有机化合物（Volatile Organic Compounds，VOC）。这里的CO₂数值是根据VOC推算的预测值。示例每秒获取并打印一次读数。

<a id="building-and-running"></a>

## 49.2 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，终端及工具链按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

本示例使用连接到`app.overlay`中指定I2C总线的传感器。将生成的二进制文件烧录到已连接该传感器的目标板。原文说明示例可用于具有I2C的开发板，以下以`nucleo_f446re`为例：

```sh
west build -b nucleo_f446re samples/sensor/ams_iAQcore
west flash
```

> 译注——覆盖文件的实际前提：当前`app.overlay`引用`arduino_i2c`，在总线上创建地址为`0x5a`、兼容字符串为`ams,iaqcore`的节点。因此，直接使用随示例提供的覆盖文件还要求开发板定义相应总线节点；只有I2C硬件而没有该节点名称时，需要按实际板级设备树调整覆盖文件。

<a id="sample-output"></a>

### 49.2.1 示例输出（Sample Output）

```text
device is 0x20001a08, name is IAQ_CORE
Co2: 882.000000ppm; VOC: 244.000000ppb
Co2: 863.000000ppm; VOC: 239.000000ppb
Co2: 836.000000ppm; VOC: 232.000000ppb
```

读数中的ppm表示百万分之一（Parts per million），ppb表示十亿分之一（Parts per billion）。CO₂一栏仍是上述由VOC推算的等效值。

<a id="see-also"></a>

## 49.3 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/ams_iAQcore/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/ams_iAQcore/src/main.c)、[samples/sensor/ams_iAQcore/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/ams_iAQcore/prj.conf)、[samples/sensor/ams_iAQcore/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/ams_iAQcore/tests.yaml)、[samples/sensor/ams_iAQcore/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/ams_iAQcore/app.overlay)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/ams_iAQcore/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/ams_iAQcore/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/ams_iAQcore/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/ams_iAQcore/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P048_AMG88XX红外阵列传感器示例.md) · [返回大纲](大纲.md) · [下一章](P050_BME280温湿度与气压传感器示例.md)
