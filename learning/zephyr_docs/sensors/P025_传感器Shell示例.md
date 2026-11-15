---
id: learning.zephyr-docs.sensors.page-25
title: 传感器Shell示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/sensor_shell/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="sensor_shell"></a>

# 第25章\_传感器Shell示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/sensor_shell/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 25.1 概述（Overview）

这是一个简单的Shell模块，用于获取系统中已有传感器的数据。

<a id="building-and-running"></a>

## 25.2 构建与运行（Building and Running）

> 译注——命令位置：以下主机构建命令从读者自己的Zephyr源码根目录执行，使用已完成官方入门配置的UCRT64 Bash或Linux Bash终端。设备树片段属于覆盖文件内容，不是Shell命令。构建成功只说明固件生成，烧录和传感器输出需要实际目标硬件及接线。出现设备未就绪或读取错误时，先核对别名、节点启用状态、驱动配置及总线连接。

选择已经启用传感器驱动的目标开发板来构建示例，例如：

```sh
# From the root of the zephyr repository
west build -b reel_board samples/sensor/sensor_shell
west flash
```

对于没有传感器的开发板，示例提供简单的模拟传感器驱动（Fake sensor driver），可通过加入以下覆盖文件启用：

```sh
# From the root of the zephyr repository
west build -b qemu_riscv64 samples/sensor/sensor_shell -- -DEXTRA_DTC_OVERLAY_FILE=fake_sensor.overlay
west build -t run
```

> 译注——模拟路径：`fake_sensor.overlay`是官方示例已有文件，不是读者另行寻找的真实传感器驱动。第二组命令在QEMU中运行模拟设备，不能证明真实I2C／SPI通信、接线或实板传感器正常。

<a id="shell-module-command-help"></a>

## 25.3 Shell模块命令帮助（Shell Module Command Help）

```text
sensor - Sensor commands
Subcommands:
  get   :Get sensor data. Channel names are optional. All channels are read when
         no channels are provided. Syntax:
         <device_name> <channel name 0> .. <channel name N>
  info  :Get sensor info, such as vendor and model name, for all sensors.
```

`get`：根据给定传感器设备名打印其所有通道（Channel）的数据。也可以选择传入一个通道名称或索引，只打印该通道；设备名与通道名支持自动补全（Autocompletion）。

在`reel_board`上的输出示例：

```text
uart:~$ sensor get mma8652fc@1d
channel idx=0 accel_x =   0.000000
channel idx=1 accel_y =   0.268150
channel idx=2 accel_z =   9.959878
channel idx=3 accel_xyz x =   0.000000 y =   0.268150 z =   9.959878

uart:~$ sensor get mma8652fc@1d accel_z
channel idx=2 accel_z =   9.959878

uart:~$ sensor get mma8652fc@1d 2
channel idx=2 accel_z =   9.959878
```

原文注意事项：应传入有效的传感器设备名，否则可能出现硬件异常等未定义行为（Undefined behavior）。原文解释，Shell子系统运行于监督者模式（Supervisor mode），调用API回调前不会检查回调。

> 译注——版本差异：当前`sensor_shell.c`的获取命令已检查设备绑定结果和`DEVICE_API_IS(sensor, dev)`，并在未知设备或类型不匹配时返回`-ENODEV`；启用传感器信息时还有额外的传感器身份检查。因此不能把原文旧提示概括为“当前所有无效设备名都会导致硬件异常”。仍应按自动补全或实际设备信息选择有效传感器。

`info`：打印所有传感器的厂商（Vendor）、型号（Model）及友好名称（Friendly name）。该命令依赖启用[`CONFIG_SENSOR_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR_INFO)。

```text
uart:~$ sensor info
device name: apds9960@39, vendor: Avago Technologies, model: apds9960, friendly name: (null)
device name: mma8652fc@1d, vendor: NXP Semiconductors, model: fxos8700, friendly name: (null)
device name: ti_hdc@43, vendor: Texas Instruments, model: hdc, friendly name: (null)
device name: temp@4000c000, vendor: Nordic Semiconductor, model: nrf-temp, friendly name: (null)
```

> 译注——命令版本：原帮助块只列出`get`与`info`，本文保持原样。当前Shell源码还包含属性和触发器相关命令，实际可用项目以所构建固件的帮助及配置为准。

<a id="see-also"></a>

## 25.4 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/sensor_shell/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sensor_shell/src/main.c)、[samples/sensor/sensor_shell/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sensor_shell/prj.conf)、[samples/sensor/sensor_shell/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sensor_shell/tests.yaml)、[samples/sensor/sensor_shell/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sensor_shell/Kconfig)、[drivers/sensor/sensor_shell.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/sensor/sensor_shell.c)、[samples/sensor/sensor_shell/fake_sensor.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sensor_shell/fake_sensor.overlay)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/sensor_shell/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/sensor_shell/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/sensor_shell/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/sensor_shell/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P024_接近传感器轮询示例.md) · [返回大纲](大纲.md) · [下一章](P026_ADT7420高精度温度传感器示例.md)
