---
id: learning.zephyr-docs.board-samples.page-13
title: SensorTile.box传感器示例
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/board_specific/sensortile_box/sensors/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="sensortile_box_sensors"></a>

# 第13章\_SensorTile.box 传感器（SensorTile.box sensors）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/st/board_specific/sensortile_box/sensors/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/board_specific/sensortile_box/sensors/README.rst/..)

<a id="overview"></a>

## 13.1 概述（Overview）

本示例展示如何从 SensorTile.box 开发板读取传感器数据。

示例启用 SensorTile.box 板上的全部传感器，并周期性读取以下传感器的数据，将其显示到控制台：

> 译注——清单与日志范围：正文清单没有列出 IIS3DHHC，但原始日志和本次官方 main.c 均包含其加速度与触发计数，配置也启用了相应触发线程。这里保留正文和日志各自内容，不据简短清单删除已有输出；具体启用器件仍由板定义、驱动与构建配置共同决定。

- HTS221：环境温度与相对湿度。

- LPS22HH：环境温度与大气压力。

- LIS2DW12：三轴加速度（3-Axis acceleration）。

- LSM6DSOX：六轴加速度与角速度（6-Axis acceleration and angular velocity）。

- STTS751：温度传感器（Temperature sensor）。

<a id="requirements"></a>

## 13.2 前提条件（Requirements）

应用需要一块通过 USB 连接 PC 的 SensorTile.box 开发板，开发板将自己声明为 USB 通信设备类（Communications Device Class，CDC）设备。

<a id="references"></a>

## 13.3 参考资料（References）

- [SensorTile.box](https://docs.zephyrproject.org/latest/boards/st/sensortile_box/doc/index.html#sensortile_box)

<a id="building-and-running"></a>

## 13.4 构建与运行（Building and Running）

> 译注——执行环境：构建与烧录命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具链、west 工作区及对应开发板。应用目录与配置为官方提供，构建目录由工具生成。板型替换前先核对其硬件条件，构建成功后再按板文档准备启动／烧录模式并烧录。失败时先回查构建配置或板的烧录步骤；本次只核对文档与源码，没有运行固件或操作设备。

按以下方式构建并烧录示例：

> 译注——官方命令路径差异：下面原命令给出 `samples/boards/st/board_specific/sensortile_box`；本次上游该目录没有 CMakeLists.txt，而实际应用位于其 `sensors` 子目录。针对这一上游布局构建，应将命令中的应用目录替换为 `samples/boards/st/board_specific/sensortile_box/sensors`。本仓库旧版本布局不同，见本页源码入口，先按所用源码确认 CMakeLists.txt 所在位置，不能把新旧目录混用。

```text
# From the root of the zephyr repository
west build -b sensortile_box samples/boards/st/board_specific/sensortile_box
west flash
```

注意，烧录前需要完成 [SensorTile.box](https://docs.zephyrproject.org/latest/boards/st/sensortile_box/doc/index.html#sensortile_box) 板文档描述的准备步骤。

随后拔下并重新插入 USB 线，使开发板重新上电。运行常用终端程序查看输出。

> 译注——终端与设备路径：下方 minicom 命令面向安装了 minicom 的 Linux 终端，开头 `$` 是提示符，不属于命令。`<tty_device>` 按本机实际枚举的串口替换；原文 `/dev/ttyUSB*` 和 `/dev/ttyACM*` 是操作系统设备节点示例，不是仓库安装路径。Windows 应使用实际 COM 端口及合适终端程序，不照抄 Linux 设备名。这里 minicom 的 `-b` 表示波特率，和 west build 的 `-b` 选择开发板不同。

```text
$ minicom -D <tty_device> -b 115200
```

将 `<tty_device>` 替换为 SensorTile.box 开发板所在的端口，例如 Linux 中的 `/dev/ttyUSB0`。`-b` 选项设置波特率，并忽略配置中的相应值。

<a id="sample-output"></a>

### 13.4.1 输出示例（Sample Output）

> 译注——日志与单位：Dashboard 为数据面板，Temperature 为温度，Relative Humidity 为相对湿度，Pressure 为压力，Accel 为加速度，Gyro 为角速度，Magn 为磁场，trig 为触发计数。原始日志保留 C、%、kPa、m/s^2、rad/s 和 G 等单位及全部数值；六轴表示三轴加速度与三轴角速度。`<repeats endlessly every 2s>` 是“每两秒持续重复”的说明，不是传感器实际发送的数据。观察读数变化及设备就绪状态，不要求实测值等于原始示例数值。

示例代码将传感器数据输出到 SensorTile.box 控制台。

> ```text
> SensorTile.box dashboard
>
> HTS221: Temperature: 26.4 C
> HTS221: Relative Humidity: 60.5%
> LPS22HH: Temperature: 28.4 C
> LPS22HH: Pressure:99.694 kPa
> LIS2DW12: Accel (m/s^2): x: 0.306, y: -0.459, z: 10.031
> IIS3DHHC: Accel (m/s^2): x: -0.581, y: 0.880, z: -9.933
> LSM6DSOX: Accel (m/s^2): x: -0.158, y: 0.158, z: 9.811
> LSM6DSOX: Gyro (rad/s): x: 0.003, y: 0.000, z: -0.005
> STTS751: Temperature: 27.0 C
> 1:: lps22hh trig 206
> 1:: lis2dw12 trig 410
> 1:: lsm6dsox acc trig 836
> 1:: lsm6dsox gyr trig 836
> 1:: iis3dhhc trig 2422
>
> <repeats endlessly every 2s>
> ```

移动开发板或将手指放到温度传感器上，可看到加速度计、陀螺仪和温度读数变化。

> 译注——源码入口：本仓库[samples/boards/st/sensortile_box/src/main.c](../../../samples/boards/st/sensortile_box/src/main.c)与[samples/boards/st/sensortile_box/prj.conf](../../../samples/boards/st/sensortile_box/prj.conf)使用相对路径，可随仓库移动。此处是本仓库旧布局中的参照实现；本次官方新布局为 `samples/boards/st/board_specific/sensortile_box/sensors`，见[上游 main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/board_specific/sensortile_box/sensors/src/main.c)和[上游 prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/board_specific/sensortile_box/sensors/prj.conf)。两者版本可能不同，不把目录迁移当作本次翻译操作。

对应官方文档源码：[samples/boards/st/board_specific/sensortile_box/sensors/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/board_specific/sensortile_box/sensors/README.rst)。

[上一章](P012_ST蓝牙低功耗传感器演示.md) · [返回大纲](大纲.md) · [下一章](P014_SensorTile.box_Pro传感器示例.md)
