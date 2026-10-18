---
id: learning.zephyr-docs.kconfig-reference.page-422
title: "`subsys/sensing`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第422章\_`subsys/sensing`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/sensing` 的 12 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SENSING"></a>

## 422.1 `CONFIG_SENSING`

**提示（Prompt）**：感知子系统（Sensing Subsystem）

**说明（Help）**

启用感知子系统（Sensing Subsystem）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_SENSING_ENABLED
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RTIO
CONFIG_RTIO_CONSUME_SEM
CONFIG_SENSOR
CONFIG_SENSOR_ASYNC_API
```

**定义位置（Location）**：[`subsys/sensing/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sensing/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_RTIO`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO)、[`CONFIG_RTIO_CONSUME_SEM`](P419_subsys_rtio_配置项参考.md#CONFIG_RTIO_CONSUME_SEM)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_SENSOR_ASYNC_API`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR_ASYNC_API)。

<a id="CONFIG_SENSING_DISPATCH_THREAD_PRIORITY"></a>

## 422.2 `CONFIG_SENSING_DISPATCH_THREAD_PRIORITY`

**提示（Prompt）**：传感器分派线程（Sensor dispatch thread）的优先级

**说明（Help）**

感知子系统分派线程（Dispatch thread）的优先级。应尽快取出环形缓冲区（Ring buffer）数据，因此分派线程优先级应高于运行时线程（Runtime thread）。典型配置值为 8。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSING && CONFIG_SENSING
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/sensing/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sensing/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<a id="CONFIG_SENSING_DISPATCH_THREAD_STACK_SIZE"></a>

## 422.3 `CONFIG_SENSING_DISPATCH_THREAD_STACK_SIZE`

**提示（Prompt）**：传感器分派线程（Sensor dispatch thread）的栈大小

**说明（Help）**

传感器分派线程（Sensor dispatch thread）的栈大小，典型值为 1024。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSING && CONFIG_SENSING
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/sensing/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sensing/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<a id="CONFIG_SENSING_MAX_SENSITIVITY_COUNT"></a>

## 422.4 `CONFIG_SENSING_MAX_SENSITIVITY_COUNT`

**提示（Prompt）**：单个传感器支持的灵敏度（Sensitivity）最大数量

**说明（Help）**

单个传感器可支持的灵敏度（Sensitivity）最大数量。某些传感器，例如环境光传感器（Ambient Light Sensor，ALS），可为各个数据字段定义不同灵敏度，因此需要此数量上限。典型值为 6。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSING && CONFIG_SENSING
```

**默认值（Defaults）**

```text
6
```

**定义位置（Location）**：[`subsys/sensing/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sensing/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<a id="CONFIG_SENSING_RTIO_BLOCK_COUNT"></a>

## 422.5 `CONFIG_SENSING_RTIO_BLOCK_COUNT`

**提示（Prompt）**：RTIO 上下文（Context）的内存块数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSING
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/sensing/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sensing/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<a id="CONFIG_SENSING_RTIO_BLOCK_SIZE"></a>

## 422.6 `CONFIG_SENSING_RTIO_BLOCK_SIZE`

**提示（Prompt）**：RTIO 上下文（Context）的块大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSING
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/sensing/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sensing/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<a id="CONFIG_SENSING_RTIO_CQE_NUM"></a>

## 422.7 `CONFIG_SENSING_RTIO_CQE_NUM`

**提示（Prompt）**：感知系统 RTIO 提交队列项（SQE）的数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSING
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/sensing/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sensing/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<a id="CONFIG_SENSING_RTIO_SQE_NUM"></a>

## 422.8 `CONFIG_SENSING_RTIO_SQE_NUM`

**提示（Prompt）**：感知系统 RTIO 提交队列项（SQE）的数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSING
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/sensing/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sensing/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<a id="CONFIG_SENSING_RUNTIME_THREAD_PRIORITY"></a>

## 422.9 `CONFIG_SENSING_RUNTIME_THREAD_PRIORITY`

**提示（Prompt）**：感知子系统运行时线程（Runtime thread）的优先级

**说明（Help）**

感知子系统运行时线程（Runtime thread）的优先级。运行时线程存入环形缓冲区（Ring buffer）数据后，通过释放信号量（Semaphore）通知分派线程（Dispatch thread）。运行时线程优先级应低于分派线程，以保证发出信号量后，分派线程能够立即获取数据。例如，若运行时线程优先级更高，且始终满负荷运行、不休眠，分派线程就无法取得执行机会；数据不断加入环形缓冲区，最终溢出。典型配置值为 9。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSING && CONFIG_SENSING
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`subsys/sensing/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sensing/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<a id="CONFIG_SENSING_RUNTIME_THREAD_STACK_SIZE"></a>

## 422.10 `CONFIG_SENSING_RUNTIME_THREAD_STACK_SIZE`

**提示（Prompt）**：感知子系统运行时线程（Runtime thread）的栈大小

**说明（Help）**

感知子系统运行时线程（Runtime thread）的栈大小，典型值为 4096。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SENSING && CONFIG_SENSING
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/sensing/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sensing/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<a id="CONFIG_SENSING_SENSOR_HINGE_ANGLE"></a>

## 422.11 `CONFIG_SENSING_SENSOR_HINGE_ANGLE`

**提示（Prompt）**：感知系统铰链角度传感器（Hinge angle sensor）

**说明（Help）**

启用感知系统的铰链角度传感器（Hinge angle sensor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_SENSING_HINGE_ANGLE_ENABLED && CONFIG_SENSING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/sensing/sensor/hinge_angle/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sensing/sensor/hinge_angle/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<a id="CONFIG_SENSING_SENSOR_PHY_3D_SENSOR"></a>

## 422.12 `CONFIG_SENSING_SENSOR_PHY_3D_SENSOR`

**提示（Prompt）**：感知子系统三维物理传感器：加速度计、陀螺仪、磁力计（Accel, gyro, mag）

**说明（Help）**

启用感知子系统的三维物理传感器，即加速度计（Accelerometer）、陀螺仪（Gyroscope）和磁力计（Magnetometer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_SENSING_PHY_3D_SENSOR_ENABLED && CONFIG_SENSING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/sensing/sensor/phy_3d_sensor/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sensing/sensor/phy_3d_sensor/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 感知子系统（Sensing Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_SENSING`](P422_subsys_sensing_配置项参考.md#CONFIG_SENSING)。

<!-- kconfig-navigation -->

[上一章](P421_subsys_secure_storage_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P423_subsys_settings_配置项参考.md)
