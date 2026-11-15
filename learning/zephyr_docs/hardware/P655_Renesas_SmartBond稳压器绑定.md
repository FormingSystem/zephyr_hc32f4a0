---
id: learning.zephyr-docs.hardware.reginternal-9
title: Renesas_SmartBond稳压器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/regulator/renesas,smartbond-regulator.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第655章\_Renesas_SmartBond稳压器绑定

<a id="dtbinding-renesas-smartbond-regulator"></a>

原文：[renesas,smartbond-regulator](https://docs.zephyrproject.org/latest/build/dts/api/bindings/regulator/renesas,smartbond-regulator.html)。读取日期：2026-10-13，`latest`。

`renesas,smartbond-regulator` 是设备树绑定（Devicetree Binding），描述Renesas Electronics Corporation的SmartBond™低压差稳压器（Low-Dropout Regulator，LDO）和直流转换器（DC-DC Converter，DCDC）。V30、VBAT和VBUS是原文使用的供电节点名称，其中VBAT表示电池电源，VBUS表示总线电源。

驱动为 [`drivers/regulator/regulator_da1469x.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/regulator_da1469x.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=renesas,smartbond-regulator)。

## 655.1\_子节点属性

原页没有顶层属性（Top-Level Properties）。下表全部属于子节点属性（Child Node Properties）。

本页 `int` 为整数，`string` 为字符串，`boolean` 为布尔属性，`array` 为数值数组，`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明单元数组，`string-array` 为字符串数组。电压的 `microvolt` 单位为微伏（Microvolt，µV），电流的 `microamp` 单位为微安（Microampere，µA），时间的 `us` 单位为微秒（Microsecond，µs），温度的 `kelvin` 单位为开尔文（Kelvin，K）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `renesas,regulator-v30-ref-bandgap` | `boolean` | 为V30低压差稳压器选择带隙（Bandgap）输出作为参考源 |
| `renesas,regulator-v30-clamp` | `boolean` | 启用可由VBAT为V30供电的钳位（Clamp）电路 |
| `renesas,regulator-v30-vbus` | `boolean` | 允许由VBUS为V30供电 |
| `renesas,regulator-v30-vbat` | `boolean` | 允许由VBAT为V30供电 |
| `renesas,regulator-dcdc-vbat-high` | `boolean` | 在高电池电压模式下启用直流转换器 |
| `renesas,regulator-dcdc-vbat-low` | `boolean` | 在低电池电压模式下启用直流转换器 |
| `renesas,regulator-sleep-ldo` | `boolean` | 在睡眠模式下启用低压差稳压器 |
| `regulator-init-microvolt` | `int` | 初始化时设置的电压 |
| `regulator-max-microamp` | `int` | 用电方可以设置的最大电流 |
| `regulator-always-on` | `boolean` | 稳压器始终开启，不应被禁用 |
| `regulator-boot-on` | `boolean` | 引导加载器（Bootloader）／固件已启用稳压器，预期引导加载器会让它保持开启。若没有保持开启，操作系统（Operating System，OS）应在启动时打开它，但不应阻止之后关闭。本属性仅用于软件无法读取稳压器状态的设备 |
| `regulator-initial-mode` | `int` | 初始工作模式（Initial Operating Mode）。可用模式取决于具体硬件能力，各设备绑定文档说明其稳压器支持的取值 |

原页没有列出已弃用的节点专用属性或通用基础属性，也未把上述属性标为必需。



---

[上一章：RaspberryPi内核供电稳压器绑定](P654_RaspberryPi内核供电稳压器绑定.md) · [下一章：SF32LB52X低压差稳压器绑定](P656_SF32LB52X低压差稳压器绑定.md) · [返回大纲](大纲.md)
