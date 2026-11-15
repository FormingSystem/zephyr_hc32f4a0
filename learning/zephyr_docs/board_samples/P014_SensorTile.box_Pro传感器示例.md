---
id: learning.zephyr-docs.board-samples.page-14
title: SensorTile.box_Pro传感器示例
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/st/board_specific/sensortile_box_pro/sensors-on-board/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="sensortile_box_pro_sensors"></a>

# 第14章\_SensorTile.box Pro 传感器（SensorTile.box Pro sensors）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/st/board_specific/sensortile_box_pro/sensors-on-board/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/board_specific/sensortile_box_pro/sensors-on-board/README.rst/..)

<a id="overview"></a>

## 14.1 概述（Overview）

本示例展示如何从 SensorTile.box Pro 开发板读取传感器数据。

示例启用 SensorTile.box Pro 板上的全部传感器，并周期性读取以下传感器的数据，将其显示到控制台：

> 译注——清单并非全部输出：原始日志含 `lis2mdl trig`，而本次源码与配置确有 LIS2MDL 的触发处理，正文简短器件清单未列出它。保留这一差异，并按实际板定义和配置解释输出；不能把缺少某个默认触发计数直接等同于整个传感器应用失败。

- LPS22DF：环境温度与大气压力。

- LSM6DSV16X：六轴加速度与角速度（6-Axis acceleration and angular velocity）。

- LIS2DU12：三轴加速度（3-Axis acceleration）。

<a id="requirements"></a>

## 14.2 前提条件（Requirements）

应用需要一块通过 USB 连接 PC 的 SensorTile.box Pro 开发板，开发板以标准 USB CDC 类设备出现。

<a id="references"></a>

## 14.3 参考资料（References）

- [SensorTile.box PRO](https://docs.zephyrproject.org/latest/boards/st/sensortile_box_pro/doc/index.html#sensortile_box_pro)

<a id="building-and-running"></a>

## 14.4 构建与运行（Building and Running）

> 译注——执行环境：构建与烧录命令从读者自己的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具链、west 工作区及对应开发板。应用目录与配置为官方提供，构建目录由工具生成。板型替换前先核对其硬件条件，构建成功后再按板文档准备启动／烧录模式并烧录。失败时先回查构建配置或板的烧录步骤；本次只核对文档与源码，没有运行固件或操作设备。

按以下方式构建并烧录示例：

```text
# From the root of the zephyr repository
west build -b sensortile_box_pro samples/boards/st/board_specific/sensortile_box_pro/sensors-on-board
west flash
```

注意，烧录前需要完成 [SensorTile.box PRO](https://docs.zephyrproject.org/latest/boards/st/sensortile_box_pro/doc/index.html#sensortile_box_pro) 板文档描述的准备步骤。

随后拔下并重新插入 USB 线，使开发板重新上电。运行常用终端程序查看输出。

> 译注——终端与设备路径：下方 minicom 命令面向安装了 minicom 的 Linux 终端，开头 `$` 是提示符，不属于命令。`<tty_device>` 按本机实际枚举的串口替换；原文 `/dev/ttyUSB*` 和 `/dev/ttyACM*` 是操作系统设备节点示例，不是仓库安装路径。Windows 应使用实际 COM 端口及合适终端程序，不照抄 Linux 设备名。这里 minicom 的 `-b` 表示波特率，和 west build 的 `-b` 选择开发板不同。

```text
$ minicom -D <tty_device> -b 115200
```

将 `<tty_device>` 替换为 SensorTile.box Pro 连接后由主机自动创建的实际设备路径，通常为 `/dev/ttyUSBx` 或 `/dev/ttyACMx`，其中 x 为 0、1、2 等。`-b` 选项设置波特率，并忽略配置中的相应值。

<a id="sample-output"></a>

### 14.4.1 输出示例（Sample Output）

> 译注——日志与单位：Dashboard 为数据面板，Temperature 为温度，Relative Humidity 为相对湿度，Pressure 为压力，Accel 为加速度，Gyro 为角速度，Magn 为磁场，trig 为触发计数。原始日志保留 C、%、kPa、m/s^2、rad/s 和 G 等单位及全部数值；六轴表示三轴加速度与三轴角速度。`<repeats endlessly every 2s>` 是“每两秒持续重复”的说明，不是传感器实际发送的数据。观察读数变化及设备就绪状态，不要求实测值等于原始示例数值。

示例代码将传感器数据输出到 SensorTile.box Pro 控制台。

> ```text
> SensorTile.box Pro dashboard
>
> LPS22DF: Temperature: 28.4 C
> LPS22DF: Pressure:99.694 kPa
> LSM6DSV16X: Accel (m/s^2): x: -0.158, y: 0.158, z: 9.811
> LSM6DSV16X: Gyro (rad/s): x: 0.003, y: 0.000, z: -0.005
> LIS2DU12: Accel (m/s^2): x: -0.756, y: -0.249, z: -9.629
> 1:: lps22df trig 199
> 1:: lsm6dsv16x acc trig 836
> 1:: lsm6dsv16x gyr trig 836
> 1:: lis2mdl trig 402
> 1:: lis2du12 trig 1589
>
> <repeats endlessly every 2s>
> ```

> 译注——源码入口：本仓库[samples/boards/st/sensortile_box_pro/sensors-on-board/src/main.c](../../../samples/boards/st/sensortile_box_pro/sensors-on-board/src/main.c)与[samples/boards/st/sensortile_box_pro/sensors-on-board/prj.conf](../../../samples/boards/st/sensortile_box_pro/sensors-on-board/prj.conf)使用相对路径，可随仓库移动。此处是本仓库旧布局中的参照实现；本次官方新布局为 `samples/boards/st/board_specific/sensortile_box_pro/sensors-on-board`，见[上游 main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/board_specific/sensortile_box_pro/sensors-on-board/src/main.c)和[上游 prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/board_specific/sensortile_box_pro/sensors-on-board/prj.conf)。两者版本可能不同，不把目录迁移当作本次翻译操作。

对应官方文档源码：[samples/boards/st/board_specific/sensortile_box_pro/sensors-on-board/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/st/board_specific/sensortile_box_pro/sensors-on-board/README.rst)。

[上一章](P013_SensorTile.box传感器示例.md) · [返回大纲](大纲.md) · [下一章](P015_STWIN.box传感器示例.md)
