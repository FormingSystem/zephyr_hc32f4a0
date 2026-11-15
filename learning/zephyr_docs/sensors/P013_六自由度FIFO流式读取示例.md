---
id: learning.zephyr-docs.sensors.page-13
title: 六自由度FIFO流式读取示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/6dof_fifo_stream/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="6dof_fifo_stream"></a>

# 第13章\_六自由度FIFO流式读取示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/6dof_fifo_stream/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 13.1 概述（Overview）

本示例通过基于[实时输入输出框架（RTIO）](../io_services/P001_实时输入输出.md#rtio)的[读取与解码方法（Read and Decode）](P006_读取与解码.md#sensor-read-and-decode)，从先进先出缓冲区（First In, First Out，FIFO）流式读取六自由度（Six degrees of freedom，6DOF，包括旋转与平移）设备的数据。

流通过`sensor_stream()`API启动，随后由`SENSOR_TRIG_FIFO_WATERMARK`水位触发器持续驱动。

示例获取并打印以下传感器通道：

- `SENSOR_CHAN_ACCEL_XYZ`：三轴加速度（Acceleration）。
- `SENSOR_CHAN_GYRO_XYZ`：三轴角速度（Angular velocity）。
- `SENSOR_CHAN_DIE_TEMP`：芯片温度（Die temperature）。
- `SENSOR_CHAN_GAME_ROTATION_VECTOR`：游戏旋转向量（Game rotation vector）。
- `SENSOR_CHAN_GRAVITY_VECTOR`：重力向量（Gravity vector）。
- `SENSOR_CHAN_GBIAS_XYZ`：三轴陀螺仪偏置（Gyroscope bias）。

<a id="building-and-running"></a>

## 13.2 构建与运行（Building and Running）

> 译注——命令位置：以下主机构建命令从读者自己的Zephyr源码根目录执行，使用已完成官方入门配置的UCRT64 Bash或Linux Bash终端。设备树片段属于覆盖文件内容，不是Shell命令。构建成功只说明固件生成，烧录和传感器输出需要实际目标硬件及接线。出现设备未就绪或读取错误时，先核对别名、节点启用状态、驱动配置及总线连接。

示例支持最多10个FIFO流式设备。每个设备需要设置`streamN`别名，其中`N`从`0`到`9`。例如：

```devicetree
/ {
    aliases {
                 stream0 = &lsm6dsv16x_6b_x_nucleo_iks4a1;
            };
    };
```

原文注意事项：`main.c`中的`NUM_SENSORS`必须与`N`匹配，应相应设置。

> 译注——数量与编号：这里应按实际设备数量理解`NUM_SENSORS`，不是直接填写最大别名编号。例如仅有`stream0`时数量为1；有连续的`stream0`和`stream1`时数量为2。当前定义为1，它控制IO设备、线程和栈数组的规模。增加设备还应检查共享RTIO完成队列与每个线程所用解码器的对应关系，不能只增加别名就认为多设备数据路由已验证。

`boards`目录已经为`sensortile_box_pro`提供设备树覆盖及配置：

- [samples/sensor/6dof_fifo_stream/boards/sensortile_box_pro.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/6dof_fifo_stream/boards/sensortile_box_pro.overlay)：该板的设备树覆盖文件。
- [samples/sensor/6dof_fifo_stream/boards/sensortile_box_pro.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/sensor/6dof_fifo_stream/boards/sensortile_box_pro.conf)：该板的配置文件。

为`sensortile_box_pro`构建并运行：

```sh
west build -b sensortile_box_pro samples/sensor/6dof_fifo_stream
west flash
```

如果传感器位于扩展板（Shield），构建时还需要指定它。例如，对安装[X-NUCLEO-IKS4A1惯性与环境多传感器扩展板](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_iks4a1/doc/index.html#x-nucleo-iks4a1)的[Nucleo H503RB](https://docs.zephyrproject.org/latest/boards/st/nucleo_h503rb/doc/index.html#nucleo_h503rb)，使用：

```sh
west build -b nucleo_h503rb --shield x_nucleo_iks4a1 samples/sensor/6dof_fifo_stream -- -DEXTRA_DTC_OVERLAY_FILE="x_nucleo_iks4a1.overlay" -DEXTRA_CONF_FILE="x_nucleo_iks4a1.conf"
west flash
```

<a id="sample-output"></a>

### 13.2.1 示例输出（Sample Output）

以下输出来自带加速度计、陀螺仪及温度传感器的`lsm6dsv16x`IMU，也包含低功耗传感器融合（Sensor Fusion Low Power，SFLP）信息。FIFO水位设为64。使用的开发板是配备[X-NUCLEO-IKS4A1扩展板](https://docs.zephyrproject.org/latest/boards/shields/x_nucleo_iks4a1/doc/index.html#x-nucleo-iks4a1)的`nucleo_h503rb`。

```text
FIFO count - 64
XL data for lsm6dsv16x@6b 1680572433340ns (0.373229, -0.009569, 9.909734)
XL data for lsm6dsv16x@6b 1680639100006ns (0.354089, -0.023924, 9.909734)
XL data for lsm6dsv16x@6b 1680705766672ns (0.368444, 0.000000, 9.933659)
XL data for lsm6dsv16x@6b 1680772433338ns (0.373229, 0.000000, 9.924089)
XL data for lsm6dsv16x@6b 1680839100004ns (0.368444, -0.004784, 9.924089)
XL data for lsm6dsv16x@6b 1680905766670ns (0.363659, -0.009569, 9.924089)
XL data for lsm6dsv16x@6b 1680972433336ns (0.358874, -0.004784, 9.928874)
XL data for lsm6dsv16x@6b 1681039100002ns (0.363659, 0.004784, 9.928874)
GY data for lsm6dsv16x@6b 1680572433340ns (0.001524, -0.000609, 0.004269)
GY data for lsm6dsv16x@6b 1680639100006ns (-0.001219, 0.002134, 0.004879)
GY data for lsm6dsv16x@6b 1680705766672ns (0.001219, -0.001219, 0.004879)
GY data for lsm6dsv16x@6b 1680772433338ns (-0.000914, 0.001219, 0.003964)
GY data for lsm6dsv16x@6b 1680839100004ns (0.000914, -0.001219, 0.004574)
GY data for lsm6dsv16x@6b 1680905766670ns (0.001829, 0.000914, 0.005489)
GY data for lsm6dsv16x@6b 1680972433336ns (-0.000609, 0.000304, 0.004574)
GY data for lsm6dsv16x@6b 1681039100002ns (0.001829, 0.000304, 0.004879)
TP data for lsm6dsv16x@6b 1680572433340ns 24.347656 °C
TP data for lsm6dsv16x@6b 1680639100006ns 24.324218 °C
TP data for lsm6dsv16x@6b 1680705766672ns 24.316406 °C
TP data for lsm6dsv16x@6b 1680772433338ns 24.296875 °C
ROT data for lsm6dsv16x@6b 1680639100006ns (-0.000008, -0.018661, 0.021575, 0.999593)
ROT data for lsm6dsv16x@6b 1680705766672ns (-0.000139, -0.018524, 0.021606, 0.999594)
ROT data for lsm6dsv16x@6b 1680772433338ns (-0.000055, -0.018569, 0.021621, 0.999593)
ROT data for lsm6dsv16x@6b 1680839100004ns (-0.000050, -0.018539, 0.021606, 0.999594)
ROT data for lsm6dsv16x@6b 1680905766670ns (-0.000003, -0.018569, 0.021621, 0.999593)
ROT data for lsm6dsv16x@6b 1680972433336ns (0.000044, -0.018493, 0.021667, 0.999594)
ROT data for lsm6dsv16x@6b 1681039100002ns (0.000013, -0.018432, 0.021667, 0.999595)
ROT data for lsm6dsv16x@6b 1681105766668ns (0.000113, -0.018402, 0.021682, 0.999595)
GV data for lsm6dsv16x@6b 1680639100006ns (37.270999, -0.792999, 998.447998)
GV data for lsm6dsv16x@6b 1680705766672ns (36.965999, -1.037000, 998.447998)
GV data for lsm6dsv16x@6b 1680772433338ns (37.088001, -0.854000, 998.447998)
GV data for lsm6dsv16x@6b 1680839100004ns (37.027000, -0.854000, 998.447998)
GV data for lsm6dsv16x@6b 1680905766670ns (37.088001, -0.792999, 998.447998)
GV data for lsm6dsv16x@6b 1680972433336ns (36.904998, -0.670999, 998.447998)
GV data for lsm6dsv16x@6b 1681039100002ns (36.783000, -0.732000, 998.447998)
GV data for lsm6dsv16x@6b 1681105766668ns (36.722000, -0.548999, 998.447998)
GY GBIAS data for lsm6dsv16x@6b 1680572433340ns (0.000303, -0.000151, 0.004179)
GY GBIAS data for lsm6dsv16x@6b 1680639100006ns (0.000303, 0.000000, 0.004179)
GY GBIAS data for lsm6dsv16x@6b 1680705766672ns (0.000303, -0.000075, 0.004179)
GY GBIAS data for lsm6dsv16x@6b 1680772433338ns (0.000227, 0.000000, 0.004179)
GY GBIAS data for lsm6dsv16x@6b 1680839100004ns (0.000303, -0.000075, 0.004179)
GY GBIAS data for lsm6dsv16x@6b 1680905766670ns (0.000303, 0.000000, 0.004255)
GY GBIAS data for lsm6dsv16x@6b 1680972433336ns (0.000303, 0.000000, 0.004255)
GY GBIAS data for lsm6dsv16x@6b 1681039100002ns (0.000379, 0.000000, 0.004255)
XL data for lsm6dsv16x@6b 1681105766668ns (0.358874, -0.019139, 9.928874)
XL data for lsm6dsv16x@6b 1681172433334ns (0.382799, -0.004784, 9.962369)
XL data for lsm6dsv16x@6b 1681239100000ns (0.354089, 0.000000, 9.914519)
GY data for lsm6dsv16x@6b 1681105766668ns (0.000304, 0.002134, 0.004574)
GY data for lsm6dsv16x@6b 1681172433334ns (-0.000914, 0.000914, 0.004574)
GY data for lsm6dsv16x@6b 1681239100000ns (0.002744, -0.002439, 0.004879)
TP data for lsm6dsv16x@6b 1680839100004ns 24.339843 °C
TP data for lsm6dsv16x@6b 1680905766670ns 24.339843 °C
TP data for lsm6dsv16x@6b 1680972433336ns 24.289062 °C
TP data for lsm6dsv16x@6b 1681039100002ns 24.296875 °C
ROT data for lsm6dsv16x@6b 1681172433334ns (0.000049, -0.018310, 0.021697, 0.999596)
ROT data for lsm6dsv16x@6b 1681239100000ns (0.000020, -0.018371, 0.021697, 0.999595)
GV data for lsm6dsv16x@6b 1681172433334ns (36.539001, -0.670999, 998.447998)
GV data for lsm6dsv16x@6b 1681239100000ns (36.660999, -0.732000, 998.447998)
GY GBIAS data for lsm6dsv16x@6b 1681105766668ns (0.000379, 0.000000, 0.004331)
GY GBIAS data for lsm6dsv16x@6b 1681172433334ns (0.000303, 0.000075, 0.004331)
GY GBIAS data for lsm6dsv16x@6b 1681239100000ns (0.000379, 0.000000, 0.004331)
TP data for lsm6dsv16x@6b 1681105766668ns 24.289062 °C
TP data for lsm6dsv16x@6b 1681172433334ns 24.324218 °C
TP data for lsm6dsv16x@6b 1681239100000ns 24.281250 °C
```

> 译注——配置与输出：`sensortile_box_pro.overlay`分别配置加速度、陀螺仪、温度及SFLP数据的FIFO批处理率，并将`fifo-watermark`设为64。设备输出数据率、入FIFO的批处理率及FIFO水位是不同参数。原日志中的`XL`、`GY`、`TP`、`ROT`、`GV`和`GY GBIAS`分别对应上方六类通道，不能把它们都解释为加速度帧。

<a id="see-also"></a>

## 13.3 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/6dof_fifo_stream/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/6dof_fifo_stream/src/main.c)、[samples/sensor/6dof_fifo_stream/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/6dof_fifo_stream/prj.conf)、[samples/sensor/6dof_fifo_stream/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/6dof_fifo_stream/tests.yaml)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/6dof_fifo_stream/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/6dof_fifo_stream/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/6dof_fifo_stream/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/6dof_fifo_stream/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P012_六自由度运动数据就绪示例.md) · [返回大纲](大纲.md) · [下一章](P014_数据就绪触发的传感器流示例.md)
