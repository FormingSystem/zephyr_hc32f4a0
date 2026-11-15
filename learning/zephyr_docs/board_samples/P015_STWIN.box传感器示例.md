---
id: learning.zephyr-docs.board-samples.page-15
title: STWIN.box传感器示例
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/board_specific/steval_stwinbx1/sensors/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="stwinbx1_sensors"></a>

# 第15章\_STWIN.box 传感器（STWIN.box sensors）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/st/board_specific/steval_stwinbx1/sensors/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/board_specific/steval_stwinbx1/sensors/README.rst/..)

<a id="overview"></a>

## 15.1 概述（Overview）

本示例展示如何从 STWIN.box 开发板读取传感器数据。

示例启用 STWIN.box 板上的全部传感器，并周期性读取以下传感器的数据，将其显示到控制台：

- STTS22H：数字温度传感器（Digital temperature sensor）。

- IIS2MDC：三轴磁力计（3-axis magnetometer）。

- ISM330DHCX：惯性测量单元（Inertial Measurement Unit，IMU），包含三维加速度计与三维陀螺仪，并具有机器学习内核（Machine Learning Core）及有限状态机（Finite State Machine）。

> 译注——器件能力与示例范围：机器学习内核、有限状态机和倾角计是原文描述的器件特性。此示例展示传感器通道读取与触发计数，不能仅凭器件特性介绍认定已经加载机器学习模型、配置状态机任务或完成应用级姿态算法。

- IIS2DLPC：面向工业应用的高性能、超低功耗三轴加速度计。

- IIS2ICLX：具有机器学习内核的高精度、高分辨率、低功耗双轴数字倾角计。

- ILPS22QS：超紧凑压阻式绝对压力传感器。

<a id="requirements"></a>

## 15.2 前提条件（Requirements）

应用需要一块通过 USB 连接 PC 的 STWIN.box 开发板，开发板以标准 USB CDC 类设备出现。

<a id="references"></a>

## 15.3 参考资料（References）

- [STEVAL STWINBX1 开发套件（Development kit）](https://docs.zephyrproject.org/latest/boards/st/steval_stwinbx1/doc/index.html#steval_stwinbx1)

<a id="building-and-running"></a>

## 15.4 构建与运行（Building and Running）

> 译注——执行环境：构建与烧录命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具链、west 工作区及对应开发板。应用目录与配置为官方提供，构建目录由工具生成。板型替换前先核对其硬件条件，构建成功后再按板文档准备启动／烧录模式并烧录。失败时先回查构建配置或板的烧录步骤；本次只核对文档与源码，没有运行固件或操作设备。

按以下方式构建并烧录示例：

```text
# From the root of the zephyr repository
west build -b steval_stwinbx1 samples/boards/st/board_specific/steval_stwinbx1/sensors
west flash
```

注意，烧录前需要完成 STEVAL STWINBX1 开发套件文档描述的准备步骤。 相关链接：[STEVAL STWINBX1 开发套件（Development kit）](https://docs.zephyrproject.org/latest/boards/st/steval_stwinbx1/doc/index.html#steval_stwinbx1)。

随后拔下并重新插入 USB 线，使开发板重新上电。运行常用终端程序查看输出。

> 译注——终端与设备路径：下方 minicom 命令面向安装了 minicom 的 Linux 终端，开头 `$` 是提示符，不属于命令。`<tty_device>` 按本机实际枚举的串口替换；原文 `/dev/ttyUSB*` 和 `/dev/ttyACM*` 是操作系统设备节点示例，不是仓库安装路径。Windows 应使用实际 COM 端口及合适终端程序，不照抄 Linux 设备名。这里 minicom 的 `-b` 表示波特率，和 west build 的 `-b` 选择开发板不同。

```text
$ minicom -D <tty_device> -b 115200
```

将 `<tty_device>` 替换为 STWIN.box 连接后由主机自动创建的实际设备路径，通常为 `/dev/ttyUSBx` 或 `/dev/ttyACMx`，其中 x 为 0、1、2 等。`-b` 选项设置波特率，并忽略配置中的相应值。

<a id="sample-output"></a>

### 15.4.1 输出示例（Sample Output）

> 译注——日志与单位：Dashboard 为数据面板，Temperature 为温度，Relative Humidity 为相对湿度，Pressure 为压力，Accel 为加速度，Gyro 为角速度，Magn 为磁场，trig 为触发计数。原始日志保留 C、%、kPa、m/s^2、rad/s 和 G 等单位及全部数值；六轴表示三轴加速度与三轴角速度。`<repeats endlessly every 2s>` 是“每两秒持续重复”的说明，不是传感器实际发送的数据。观察读数变化及设备就绪状态，不要求实测值等于原始示例数值。

示例代码将传感器数据输出到 STWIN.box 控制台。

> ```text
> STWIN.box dashboard
>
> STTS22H: Temperature: 24.4 C
> IIS2DLPC: Accel (m/s^2): x: -5.590, y: -0.536, z: 8.040
> IIS2MDC: Magn (G): x: 0.420, y: -0.116, z: -0.103
> IIS2MDC: Temperature: 21.0 C
> ISM330DHCX: Accel (m/s^2): x: 0.000, y: 5.704, z: 7.982
> ISM330DHCX: Gyro (rad/s): x: 0.026, y: -0.006, z: -0.008
> IIS2ICLX: Accel (m/s^2): x: -0.157, y: 5.699
> ILPS22QS: Temperature: 26.4 C
> ILPS22QS: Pressure: 100.539 kPa
> 1:: iis2dlpc trig 2021
> 1:: iis2mdc trig 993
> 1:: ism330dhcx acc trig 4447
> 1:: ism330dhcx gyr trig 2223
> 1:: iis2iclx trig 2091
>
> <repeats endlessly every 2s>
> ```

> 译注——源码入口：本仓库[samples/boards/st/steval_stwinbx1/sensors/src/main.c](../../../samples/boards/st/steval_stwinbx1/sensors/src/main.c)与[samples/boards/st/steval_stwinbx1/sensors/prj.conf](../../../samples/boards/st/steval_stwinbx1/sensors/prj.conf)使用相对路径，可随仓库移动。此处是本仓库旧布局中的参照实现；本次官方新布局为 `samples/boards/st/board_specific/steval_stwinbx1/sensors`，见[上游 main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/board_specific/steval_stwinbx1/sensors/src/main.c)和[上游 prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/board_specific/steval_stwinbx1/sensors/prj.conf)。两者版本可能不同，不把目录迁移当作本次翻译操作。

对应官方文档源码：[samples/boards/st/board_specific/steval_stwinbx1/sensors/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/board_specific/steval_stwinbx1/sensors/README.rst)。

[上一章](P014_SensorTile.box_Pro传感器示例.md) · [返回大纲](大纲.md) · [下一章](P016_ST蓝牙示例目录.md)
