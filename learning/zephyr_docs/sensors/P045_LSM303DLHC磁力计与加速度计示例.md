---
id: learning.zephyr-docs.sensors.page-45
title: LSM303DLHC磁力计与加速度计示例
kind: reference
status: maintained
domains: [zephyr, sensors, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/sensor/lsm303dlhc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lsmd303dlhc"></a>

# 第45章\_LSM303DLHC磁力计与加速度计示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/sensor/lsm303dlhc/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 45.1 概述（Overview）

本示例周期性读取LSM303DLHC电子罗盘（eCompass）模块中磁力计（Magnetometer）和加速度计（Accelerometer）的数据，并在控制台显示。

<a id="requirements"></a>

## 45.2 要求（Requirements）

本示例使用LSM303DLHC。该ST微机电系统（MEMS）系统级封装（System-in-package）包含三维数字线性加速度传感器（3D digital linear acceleration sensor）和三维数字磁场传感器（3D digital magnetic sensor），通过I2C接口控制。

<a id="references"></a>

## 45.3 参考资料（References）

关于LSM303DLHC电子罗盘模块的更多信息，参阅[ST官方产品资料](https://www.st.com/en/mems-and-sensors/lsm303dlhc.html)。

<a id="building-and-running"></a>

## 45.4 构建与运行（Building and Running）

> 译注——执行位置：主机构建命令从读者自己的Zephyr源码根目录执行，终端及工具链按官方入门说明准备。读取真实传感器还需要对应目标板、设备树节点和接线；下面的命令与日志来自官方文档，本次没有执行硬件实验。

项目向控制台输出传感器数据，需要LSM303DLHC器件；`stm32f3_disco`开发板具有该器件。

```sh
west build -b stm32f3_disco samples/sensor/lsm303dlhc
```

> 译注——两个设备接口：当前实现分别取得`st_lis2dh`加速度计和`st_lsm303dlhc_magn`磁力计设备，检查两者就绪后依次读取，每轮休眠2秒。一个物理封装中的两个功能在Zephyr中由不同设备接口访问，设备树节点与驱动配置都需要对应。

<a id="sample-output"></a>

### 45.4.1 示例输出（Sample Output）

```text
Magnetometer data:
( x y z ) = ( 0.531818  -0.435454  -0.089090 )
Accelerometer data:
( x y z ) = ( -0.078127  -0.347666  1.105502 )
Magnetometer data:
( x y z ) = ( -0.003636  0.297272  -0.255454 )
Accelerometer data:
( x y z ) = ( 0.074221  -0.304696  0.972685 )

<repeats endlessly every 2 seconds>
```

以上输出每2秒不断重复（`<repeats endlessly every 2 seconds>`）。

> 译注——单位：原日志没有打印单位，数值也不足以证明其生成版本使用何种缩放。当前Zephyr传感器API定义磁场通道单位为高斯（Gauss，G），加速度通道为m/s²。对照当前代码时，应按通道定义及相应驱动转换核对，不应仅凭旧日志约为1的数值就认定加速度单位为g。

<a id="see-also"></a>

## 45.5 另请参阅（See also）

[传感器API（Sensor）](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。


> 译注——实现依据：[samples/sensor/lsm303dlhc/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lsm303dlhc/src/main.c)、[samples/sensor/lsm303dlhc/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lsm303dlhc/prj.conf)、[samples/sensor/lsm303dlhc/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lsm303dlhc/tests.yaml)、[include/zephyr/drivers/sensor.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/sensor.h)。以上为本次核对的官方main分支来源；与本仓库参照版本可能不同，保存快照的摘要见[来源记录](../SOURCES.md)。

对应官方文档源码：[samples/sensor/lsm303dlhc/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/sensor/lsm303dlhc/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/sensor/lsm303dlhc/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/sensor/lsm303dlhc/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P044_LIS2DH运动传感器示例.md) · [返回大纲](大纲.md) · [下一章](P046_LSM6DSL惯性测量单元示例.md)
