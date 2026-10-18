---
id: learning.zephyr-docs.hardware.stepext-6
title: Trinamic斜坡发生器参数
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第243章\_Trinamic斜坡发生器参数

原文：[structtmc__ramp__generator__data](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html)。读取日期：2026-10-13，`latest`。

## 243.1\_用途

结构 [`tmc_ramp_generator_data`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html) 保存 Trinamic **步进斜坡发生器（Stepper Ramp Generator）**数据，来自 `zephyr/drivers/stepper/stepper_trinamic.h`。设备树初始化宏与配置函数见[Trinamic步进扩展](P240_Trinamic步进扩展.md)。

## 243.2\_通用数据字段（Data Fields）

原文中的 `VSTART`、`V1`、`VMAX`、`VSTOP` 是各阶段速度名称，分别对应起动速度、第一阶段阈值、目标速度和停止速度。`IHOLD_IRUN` 是组合保持/运行电流的寄存器名。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`vstart`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a6b861b90bb7e4c637b21b7809608152f) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 电机起动速度（Start Velocity）。 |
| [`v1`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#ae9377878720cc03760d207b750997997) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 第一加速/减速阶段的阈值速度。 |
| [`vmax`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a54558710f19a1781bbec3dc857cb8fcf) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 运动斜坡目标速度（Target Velocity）。 |
| [`a1`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#aff69cc918c9ed7e067d728a936b9a5f0) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | VSTART 到 V1 之间的第一段加速度。 |
| [`amax`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a277403bbb0bbc8a7562bf7b6c3e22333) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | V1 到 VMAX 之间的第二段加速度。 |
| [`d1`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a8672451e2bff4af7f13b72f8a4bc4ed1) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | V1 到 VSTOP 之间的减速度。 |
| [`dmax`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a34bc24f327a5c1a6315fa4869c5418df) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | VMAX 到 V1 之间的减速度。 |
| [`vstop`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a5f4a921ae3ba0fec18633e659ad42573) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 电机停止速度（Stop Velocity）。 |
| [`tzerowait`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#ad3846d55690f835623fceca620ec3b23) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 减速到零后、开始下一次运动前的等待时间。 |
| [`iholdrun`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#acd7d7b5170ce3ce8839272ecc4dccd52) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 保持与运行电流设置，即组合的 IHOLD_IRUN 寄存器值。 |

## 243.3\_控制器系列专用参数

结构包含一个匿名 **联合体（Union）**，其中两组结构分别保存 TMC50XX 与 TMC51XX 专用参数。CoolStep、StallGuard 和 StealthChop 是原文保留的器件功能名称；斩波模式（Chopper Mode）和 **脉宽调制（Pulse-Width Modulation，PWM）**按下表使用。

| 系列 | 字段 | 类型 | 含义 |
| --- | --- | --- | --- |
| TMC50XX | [`vcoolthrs`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a522f3c11bcac25852a0d7088795f46bd) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 开启 CoolStep 与 StallGuard 的速度下阈值。 |
| TMC50XX | [`vhigh`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a5ee17564fb78bbbfd1097c6b440bd30c) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 切换到另一斩波模式的速度阈值。 |
| TMC51XX | [`tpowerdown`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a3b7d2176725aef71e12950fde1ae3ee0) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 从静止到降低电机电流之间的延迟时间。 |
| TMC51XX | [`tpwmthrs`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a94352ae1924cbc900545065c7302379b) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | StealthChop 电压 PWM 模式的速度上阈值。 |
| TMC51XX | [`tcoolthrs`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a871cb11fb3d1aacfd29b85f8ea42b502) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 开启 CoolStep 与 StallGuard 的速度下阈值。 |
| TMC51XX | [`thigh`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html#a8045473482ca1272a75e99938564a700) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 切换到另一斩波模式的速度阈值。 |

> 译注：原结构页未列字段换算单位；这些器件专用参数不应直接套用[通用速度斜坡结构](P231_步进速度斜坡结构.md)的单位。

---

[上一章：Trinamic堵转检测设置](P242_Trinamic堵转检测设置.md) · [下一章：MIPI显示接口定义](P244_MIPI显示接口定义.md) · [返回大纲](大纲.md)
