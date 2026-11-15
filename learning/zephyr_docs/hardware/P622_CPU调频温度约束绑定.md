---
id: learning.zephyr-docs.hardware.thermalbinding-0
title: CPU调频温度约束绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/cpu_freq/zephyr,cpu-freq-thermal-cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第622章\_CPU调频温度约束绑定

<a id="dtbinding-zephyr-cpu-freq-thermal-cap"></a>

原文：[zephyr,cpu-freq-thermal-cap](https://docs.zephyrproject.org/latest/build/dts/api/bindings/cpu_freq/zephyr,cpu-freq-thermal-cap.html)。读取日期：2026-10-13，`latest`。

`zephyr,cpu-freq-thermal-cap` 定义中央处理器（Central Processing Unit，CPU）调频温度约束（Thermal Cap），提供方为 Zephyr Project。使用此兼容标识的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,cpu-freq-thermal-cap)。

## 622.1\_性能状态顺序

温度约束将 `performance-states` 子节点的顺序作为 CPU 频率顺序：索引较小的性能状态（Performance State，P-state）被视为较高性能状态；索引较大的状态被视为较低性能状态，限制也更严格。

## 622.2\_顶层节点属性

以下是节点自身的专用属性，类型名按绑定原文保留。`phandle` 表示节点引用（Phandle），`string` 表示字符串，`int` 表示整数。

| 属性 | 类型 | 必需性与默认值 | 完整说明 |
| --- | --- | --- | --- |
| `sensor` | `phandle` | 必需 | 用于计算 CPU 调频温度约束的温度传感器 |
| `sensor-channel` | `string` | 默认 `die-temp`；合法值为 `die-temp`、`ambient-temp` | 温度采样使用的传感器通道（Sensor Channel）；两个值分别对应裸片温度（Die Temperature）与环境温度（Ambient Temperature） |
| `polling-delay-ms` | `int` | 默认 `1000` | 没有温度触发点（Thermal Trip）生效时的轮询间隔，单位为毫秒 |
| `trip-active-polling-delay-ms` | `int` | 默认 `100` | 一个或多个温度触发点生效时的轮询间隔，单位为毫秒。通常短于 `polling-delay-ms`，以便及时反映限制变化及解除决定 |

原页没有已弃用的节点专用属性，也没有从基础绑定继承的属性。

## 622.3\_子节点属性

| 属性 | 类型 | 必需性 | 完整说明 |
| --- | --- | --- | --- |
| `temperature-millicelsius` | `int` | 必需 | 温度阈值，单位为毫摄氏度（Millicelsius）。达到阈值时，此触发点生效，将 CPU 频率限制为 `cap-pstate` 所指的性能状态或更低状态 |
| `hysteresis-millicelsius` | `int` | 必需 | 温度滞回（Hysteresis），单位为毫摄氏度。实测温度下降到 `temperature-millicelsius` 减去本属性值时，解除已生效的触发点 |
| `cap-pstate` | `phandle` | 必需 | 此触发点生效期间允许的最高性能状态；引用的状态必须属于有序的 `performance-states` 表 |

运行机制见[CPU调频温度上限](../power/P017_CPU调频温度上限.md)，完整示例见[温度上限示例](../power/P022_CPU调频温度上限示例.md)。

---

[上一章：Xtensa开发指南](P621_Xtensa开发指南.md) · [下一章：Arm_PSCI_0_2绑定](P623_Arm_PSCI_0_2绑定.md) · [返回大纲](大纲.md)
