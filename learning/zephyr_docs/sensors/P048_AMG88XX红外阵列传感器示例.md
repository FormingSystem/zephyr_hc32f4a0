---
id: learning.zephyr-docs.sensors.page-48
title: AMG88XX红外阵列传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/amg88xx/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="amg88xx"></a>

# 第48章\_AMG88XX红外阵列传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/amg88xx/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 48.1 概述（Overview）

本示例周期性读取AMG88XX红外阵列传感器（Infrared array sensor）的8×8温度阵列（Temperature array），并将各点数值显示到串口控制台（Serial console）。

示例还可以配置为在达到27 °C上限阈值（Upper threshold）时触发。

<a id="building-and-running"></a>

## 48.2 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，终端及工具链按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

本示例需要受支持的AMG88xx扩展板（Shield）。支持的型号及构建说明见[Panasonic Grid-EYE扩展板](https://docs.zephyrproject.org/latest/boards/shields/amg88xx/doc/index.html#amg88xx-shields)。

> 译注——轮询与阈值：当前实现使用64个`struct sensor_value`存储阵列，轮询分支读取后休眠1秒。若启用`CONFIG_AMG88XX_TRIGGER`，先设置27 °C阈值，再等待阈值事件释放信号量（Semaphore）后读取；这种情况下不能把下方“每秒输出”理解为无条件周期输出。原`prj.conf`中两个触发线程选项处于注释状态，最终模式仍应按实际构建配置核对。

<a id="sample-output"></a>

### 48.2.1 示例输出（Sample Output）

输出数值是摄氏温度乘以100后的整数。例如`02075`表示20.75 °C。

```text
new sample:
---|  00    01    02    03    04    05    06    07
000|02075 01900 02000 01925 02050 01975 01950 01900
001|02000 02000 02000 01900 02125 02000 02050 02050
002|02075 01950 01950 01925 02050 01975 02075 02000
003|02175 02000 01975 01800 02000 02125 01925 02050
004|01975 02050 02050 02000 02000 01975 01925 02000
005|02100 02100 02075 02000 02025 02050 02100 02100
006|01975 02150 02075 02025 02025 02225 02025 02375
007|02025 02075 02150 02075 02025 02050 02125 02400
```

原文说明传感器阵列数据每秒输出一次。

<a id="see-also"></a>

## 48.3 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/amg88xx/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/amg88xx/src/main.c)、[samples/sensor/amg88xx/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/amg88xx/prj.conf)、[samples/sensor/amg88xx/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/amg88xx/tests.yaml)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/amg88xx/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/amg88xx/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/amg88xx/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/amg88xx/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P047_LSM6DSO惯性测量单元示例.md) · [返回大纲](大纲.md) · [下一章](P049_iAQcore室内空气质量传感器示例.md)
