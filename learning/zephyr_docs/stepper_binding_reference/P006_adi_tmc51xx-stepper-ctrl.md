---
id: learning.zephyr-docs.stepper-binding-reference.page-6
title: adi_tmc51xx-stepper-ctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, stepper]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/adi/adi,tmc51xx-stepper-ctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第6章\_adi_tmc51xx-stepper-ctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/stepper/adi/adi,tmc51xx-stepper-ctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="adi-tmc51xx-stepper-ctrl"></a>
<a id="dtbinding-adi-tmc51xx-stepper-ctrl"></a>
<a id="std-dtcompatible-adi-tmc51xx-stepper-ctrl"></a>

兼容字符串（Compatible String）：`adi,tmc51xx-stepper-ctrl`。厂商：[ Analog Devices ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-adi)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=adi,tmc51xx-stepper-ctrl)。

驱动源码（Driver Source）：[drivers/stepper/adi_tmc/tmc51xx/tmc51xx_stepper_ctrl.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmc51xx/tmc51xx_stepper_ctrl.c)。

<a id="description"></a>

Trinamic步进控制器的斜坡发生器运动控制寄存器组（Ramp Generator Motion Control Register-Set）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 6.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `vstart` | `int` | 电机起始速度（Start Velocity），无符号值，单位`µsteps/t`。通常应设置`VSTOP ≥ VSTART`；若移动距离足以减速至VSTOP，也可将VSTART设为更高值。；默认值：`1`；范围：`0 to 0x3ffff` |
| `a1` | `int` | VSTART至V1之间的第一阶段加速度（First Acceleration），无符号值，单位`µsteps/ta²`。；默认值：`0`；范围：`0 to 0xffff` |
| `v1` | `int` | 第一加速／减速阶段的阈值速度（Threshold Velocity），无符号值，单位`µsteps/t`。0表示禁用A1和D1阶段，只使用AMAX、DMAX。；默认值：`0`；范围：`0 to 0xfffff` |
| `amax` | `int` | V1至VMAX之间的第二阶段加速度（Second Acceleration），无符号值，单位`µsteps/ta²`。在速度模式（Velocity Mode）下，它同时用作加速度和减速度。；默认值：`0`；范围：`0 to 0xffff` |
| `vmax` | `int` | 运动斜坡目标速度（Motion Ramp Target Velocity），无符号值，单位`µsteps/t`；定位时须保证`VMAX ≥ VSTART`。这是速度模式的目标速度，可在运动过程中随时修改。；默认值：`0`；范围：`0 to 0x7ffdff` |
| `dmax` | `int` | VMAX至V1之间的减速度（Deceleration），无符号值，单位`µsteps/ta²`。；默认值：`0`；范围：`0 to 0xffff` |
| `d1` | `int` | V1至VSTOP之间的减速度，无符号值，单位`µsteps/ta²`。**定位模式（Positioning Mode）下不得设为0，即使V1为0也不例外。**；默认值：`1`；范围：`1 to 0xffff` |
| `vstop` | `int` | 电机停止速度（Stop Velocity），无符号值，单位`µsteps/t`。**设置`VSTOP ≥ VSTART`；定位模式下不得设为0，建议至少为10。**；默认值：`10`；范围：`1 to 0x3ffff` |
| `tzerowait` | `int` | 斜坡减速到零之后、允许下次运动或方向反转以及开始电机降功率之前的等待时间，范围约0至2秒。此设置避免过大的加速度，例如从VSTOP变为负VSTART。；默认值：`0`；范围：`0 to 0xfdff` |
| `ihold` | `int` | 保持电流（Hold Current），原文以运行电流百分比0至100描述；同时给出静止电流（Standstill Current）编码`0=1/32…31=32/32`。配合StealthChop模式，设置`IHOLD=0`可在电机静止时选择自由转动（Freewheeling）或线圈短路（Coil Short Circuit）。译注：百分比描述与寄存器编码均按原文保留，属性合法范围见本行约束。；默认值：`0`；范围：`0 to 0x1f` |
| `irun` | `int` | 电机运行电流（Run Current），编码`0=1/32…31=32/32`。建议选择合适的电流采样电阻（Sense Resistor），使正常IRUN处于16至31，以获得最佳微步性能。；默认值：`0`；范围：`0 to 0x1f` |
| `iholddelay` | `int` | 运动结束且TZEROWAIT到期后，控制电机降功率的时钟周期数。平滑过渡可避免降功率时电机突然抖动（Jerk）。0表示立即降功率；1至15表示每个电流降低步的延迟，为`2^18`个时钟的相应倍数。；默认值：`0`；范围：`0 to 0xf` |
| `tcoolthrs` | `int` | 启用智能节能CoolStep与StallGuard的下限速度，无符号值；用于在CoolStep无法可靠工作的低速范围禁用它。超过此速度后启用遇堵转停止及堵转输出；使用内部运动控制器时，通过`sg_stop`启用停止功能。非DcStep模式下，速度降回阈值以下时再次禁用。<br>`TCOOLTHRS ≥ TSTEP ≥ THIGH`：若已配置，启用CoolStep；禁用StealthChop电压PWM模式。<br>`TCOOLTHRS ≥ TSTEP`：若已配置，启用遇堵转停止及DIAG0／1堵转输出。；默认值：`0`；范围：`0 to 0xfffff` |
| `thigh` | `int` | 该无符号速度设置允许按速度切换斩波模式与整步，以获得最大转矩。每次越过THIGH阈值时，暂时关闭堵转检测2至3个电周期（Electrical Period），补偿模式切换的影响。<br>`TSTEP ≤ THIGH`：禁用CoolStep，电机按正常电流比例运行；禁用StealthChop电压PWM模式；若设置`vhighchm`，斩波器切到`chm=1`、`TFD=0`，即仅采用慢衰减的恒定关断时间；若设置`vhighfs`，电机进入整步模式，堵转检测切换为DcStep堵转检测。；默认值：`0`；范围：`0 to 0xfffff` |
| `tpwmthrs` | `int` | StealthChop电压PWM模式的上限速度。<br>`TSTEP ≥ TPWMTHRS`时：若已配置，启用StealthChop PWM模式；禁用DcStep。；默认值：`0`；范围：`0 to 0xfffff` |
| `tpowerdown` | `int` | TPOWERDOWN设置电机静止（`stst`）后到降低电机电流的延迟，范围约0至4秒。**为允许StealthChop自动调谐`PWM_OFS_AUTO`，设置值至少为2。**复位默认值为10；原文时间表达式为`0…((2^8)-1) * 2^18 tCLK`。；默认值：`10`；范围：`0 to 0xff` |

本页没有已弃用的节点专用属性。

---

[上一章](P005_adi_tmc51xx-spi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_adi_tmc51xx-stepper-driver.md)
