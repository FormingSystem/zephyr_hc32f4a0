---
id: learning.zephyr-docs.sensors.page-44
title: LIS2DH运动传感器示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/lis2dh/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lis2dh"></a>

# 第44章\_LIS2DH运动传感器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/lis2dh/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 44.1 概述（Overview）

本示例周期性读取LIS2DH传感器的加速度计（Accelerometer）数据，并在控制台显示。它也适用于兼容的LIS2DH12、LIS3DH和LSM303DLHC传感器。

> 译注——器件拼写：本段原文把LIS2DH12写成`LS2DH12`，下方构建说明还出现`LIS2DH2`；后续Icarus说明明确使用LIS2DH12。译文据此统一相应器件名称，并保留原文拼写以便检索核对。

<a id="requirements"></a>

## 44.2 要求（Requirements）

本示例使用LIS2DH。这是ST的微机电系统（Micro-Electro-Mechanical Systems，MEMS）系统级封装（System-in-package），具有三维数字输出运动传感器（3D digital output motion sensor）。

<a id="references"></a>

## 44.3 参考资料（References）

> 译注——链接状态：本次直接请求ST LIS2DH产品页返回567，网页工具也未能读取。保留原始参考链接，不将其计为已验证可访问。

关于LIS2DH运动传感器的更多信息，参阅[ST官方产品资料](https://www.st.com/en/mems-and-sensors/lis2dh.html)。

<a id="building-and-running"></a>

## 44.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，终端及工具链按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

Zephyr支持的多种开发板和扩展板（Shield）具有LIS2DH系列或兼容传感器，包括：

- [Icarus](https://docs.zephyrproject.org/latest/boards/actinius/icarus/doc/index.html#actinius_icarus)。
- [Thingy:52](https://docs.zephyrproject.org/latest/boards/nordic/thingy52/doc/index.html#thingy52)。
- [STM32F3 Discovery](https://docs.zephyrproject.org/latest/boards/st/stm32f3_disco/doc/index.html#stm32f3_disco)。
- [X-NUCLEO-IKS01A2 MEMS惯性与环境多传感器扩展板](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_iks01a2/doc/index.html#x-nucleo-iks01a2)。

有关烧录及访问控制台的具体说明，请参阅相应开发板文档；加速度数据会在控制台中显示。

<a id="building-on-actinius-icarus"></a>

### 44.4.1 在actinius\_icarus上构建（Building on actinius\_icarus）

[Icarus](https://docs.zephyrproject.org/latest/boards/actinius/icarus/doc/index.html#actinius_icarus)内置ST LIS2DH12加速度计，它支持LIS2DH接口。

```sh
west build -b actinius_icarus samples/sensor/lis2dh
west flash
```

<a id="building-on-nucleo-l476rg-with-iks01a2-shield"></a>

### 44.4.2 使用IKS01A2扩展板在nucleo\_l476rg上构建（Building on nucleo\_l476rg with IKS01A2 shield）

[X-NUCLEO-IKS01A2扩展板](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_iks01a2/doc/index.html#x-nucleo-iks01a2)具有支持LIS2DH接口的LSM303AGR加速度计。该扩展板也可用于其他具有Arduino排针的开发板。

```sh
west build -b nucleo_l476rg --shield x_nucleo_iks01a2 samples/sensor/lis2dh
west flash
```

<a id="sample-output"></a>

### 44.4.3 示例输出（Sample Output）

```text
 Polling at 0.5 Hz
 #1 @ 12 ms: x -5.387328 , y 5.578368 , z -5.463744
 #2 @ 2017 ms: x -5.310912 , y 5.654784 , z -5.501952
 #3 @ 4022 ms: x -5.349120 , y 5.692992 , z -5.463744

<repeats endlessly every 2 seconds>
```

以上输出每2秒不断重复（`<repeats endlessly every 2 seconds>`）。

> 译注——模式选择：上方是轮询输出。当前源码还支持`CONFIG_LIS2DH_TRIGGER`控制的数据就绪触发模式；启用运行时输出数据率配置（Runtime output data rate）时，请求1 Hz再等待触发。读取返回`-EBADMSG`时，示例继续获取通道值；触发模式会标记`[OVERRUN]`，轮询模式忽略这一溢出提示。若启用`CONFIG_LIS2DH_MEASURE_TEMPERATURE`，输出还包含芯片温度。实际模式取决于最终配置，不能仅凭这份旧日志判断。

<a id="see-also"></a>

## 44.5 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/lis2dh/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lis2dh/src/main.c)、[samples/sensor/lis2dh/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lis2dh/prj.conf)、[samples/sensor/lis2dh/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lis2dh/tests.yaml)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/lis2dh/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lis2dh/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/lis2dh/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/lis2dh/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P043_MPU6050运动跟踪示例.md) · [返回大纲](大纲.md) · [下一章](P045_LSM303DLHC磁力计与加速度计示例.md)
