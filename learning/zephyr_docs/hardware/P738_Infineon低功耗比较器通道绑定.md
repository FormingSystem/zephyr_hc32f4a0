---
id: learning.zephyr-docs.hardware.compifx-3
title: Infineon低功耗比较器通道绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/infineon,lp-comp-channel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第738章\_Infineon低功耗比较器通道绑定

<a id="dtbinding-infineon-lp-comp-channel"></a>

原文：[infineon,lp-comp-channel](https://docs.zephyrproject.org/latest/build/dts/api/bindings/comparator/infineon,lp-comp-channel.html)。读取日期：2026-10-13，`latest`。

`infineon,lp-comp-channel` 是Infineon Technologies的设备树绑定（Devicetree Binding），描述低功耗比较器（Low Power Comparator，LPComp）通道节点，设备节点必须是兼容字符串为 `infineon,lp-comp` 的节点的子节点，参见[LPComp父设备](P737_Infineon低功耗比较器绑定.md)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,lp-comp-channel)。

本页DSI指数字信号互连（Digital Signal Interconnect）；该术语展开见Infineon[时钟路径来源说明](https://infineon.github.io/psoc6pdl/pdl_api_reference_manual/html/group__group__sysclk__path__src.html)。

## 738.1\_节点专用属性

`int` 为整数，`string` 为字符串，`boolean` 为布尔属性。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `channel` | `int` | **必需**。低功耗比较器通道索引（Channel Index），为0或1 |
| `power` | `string` | 比较器通道功耗模式：`off` 断电；`ulp` 为超低功耗（Ultra Low Power），使用本地偏置电流（Bias Current，Ibias）；`lp` 为低功耗（Low Power）；`normal` 为正常模式（Normal Mode）；合法值：`off, ulp, lp, normal` |
| `hysteresis` | `boolean` | 启用或禁用迟滞（Hysteresis） |
| `output-mode` | `string` | 输出模式：`pulse` 使用DSI的脉冲（Pulse）选项，不旁路；`direct` 为旁路（Bypass）模式，直接输出比较器结果；`sync` 使用DSI的电平（Level）选项，与旁路类似，但比旁路慢1个周期；合法值：`pulse, direct, sync` |
| `intr-type` | `string` | 中断触发类型（Interrupt Trigger Type）：`disable` 禁用；`rising` 上升沿；`falling` 下降沿；`both` 双边沿；合法值：`disable, rising, falling, both` |
| `input-p` | `string` | 比较器正输入（Positive Input）选择：`open` 不连接；`gpio` 连接通用输入输出（General-Purpose Input/Output，GPIO）引脚；`amux_a` 连接模拟多路复用总线A（Analog Multiplexer Bus A，AMUXBUSA）；`amux_b` 连接模拟多路复用总线B（AMUXBUSB）；`local_vref` 连接本地参考电压（Voltage Reference，VREF）；合法值：`open, gpio, amux_a, amux_b, local_vref` |
| `input-n` | `string` | 比较器负输入（Negative Input）选择：`open` 不连接；`gpio` 连接通用输入输出（General-Purpose Input/Output，GPIO）引脚；`amux_a` 连接模拟多路复用总线A（Analog Multiplexer Bus A，AMUXBUSA）；`amux_b` 连接模拟多路复用总线B（AMUXBUSB）；`local_vref` 连接本地参考电压（Voltage Reference，VREF）；合法值：`open, gpio, amux_a, amux_b, local_vref` |

原页没有列出已弃用属性，也没有列出继承的基础属性。除 `channel` 外，其余字段未标为必需；原页未为这些字段声明默认值。



---

[上一章：Infineon低功耗比较器绑定](P737_Infineon低功耗比较器绑定.md) · [下一章：STM32比较器绑定](P739_STM32比较器绑定.md) · [返回大纲](大纲.md)
