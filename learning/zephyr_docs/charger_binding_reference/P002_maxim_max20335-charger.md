---
id: learning.zephyr-docs.charger-binding-reference.page-2
title: maxim_max20335-charger
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/maxim,max20335-charger.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第2章\_maxim_max20335-charger

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/maxim,max20335-charger.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="maxim-max20335-charger"></a>
<a id="dtbinding-maxim-max20335-charger"></a>
<a id="std-dtcompatible-maxim-max20335-charger"></a>

兼容字符串（Compatible String）：`maxim,max20335-charger`。厂商：[ Maxim Integrated ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-maxim)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=maxim,max20335-charger)。

驱动源码（Driver Source）：[drivers/charger/charger_max20335.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/charger_max20335.c)。

<a id="description"></a>

Maxim MAX20335电池充电器（Battery Charger）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 2.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `constant-charge-voltage-max-microvolt` | `int` | **必需**。最大恒定输入电压（Maximum Constant Input Voltage）；合法值：`4050000, 4100000, 4150000, 4200000, 4250000, 4300000, 4350000, 4400000, 4450000, 4500000, 4550000, 4600000` |
| `chgin-to-sys-current-limit-microamp` | `int` | **必需**。CHGIN至SYS路径限流器（Current Limiter）配置，详情参见ILimCntl寄存器说明；合法值：`0, 100000, 500000, 1000000` |
| `system-voltage-min-threshold-microvolt` | `int` | **必需**。系统电压最小阈值（Minimum Threshold）。SYS路径电压降至此值时，降低充电电流以防止电池损坏；合法值：`3600000, 3700000, 3800000, 3900000, 4000000, 4100000, 4200000, 4300000` |
| `re-charge-threshold-microvolt` | `int` | **必需**。相对于BatReg的再充电阈值（Recharge Threshold），详情参见ChgCntlA寄存器说明；合法值：`70000, 120000, 170000, 220000` |
| `thermistor-monitoring-mode` | `string` | **必需**。热敏电阻监测模式（Thermistor Monitoring Mode），详情参见ThrmCfg寄存器说明及表2；合法值：`disabled, thermistor, JEITA-1, JEITA-2` |
| `int-gpios` | `phandle-array` | **必需**。中断引脚（Interrupt Pin） |
| `device-chemistry` | `string` | 描述电池的化学体系（Chemical Technology）。lithium-ion是所有锂离子电池（Lithium-ion Battery）的通用类型；未知具体化学体系时，可使用此值代替更精确的lithium-ion-X选项；合法值：`nickel-cadmium, nickel-metal-hydride, lithium-ion, lithium-ion-polymer, lithium-ion-iron-phosphate, lithium-ion-manganese-oxide` |
| `ocv-capacity-table-0` | `array` | 开路电压（Open-circuit Voltage，OCV）数组，根据当前OCV值查询电池容量，电压单位微伏。与Linux对应属性不同，此数组必须恰有11个元素，以10%为步进，表示0%至100%电量所对应的电压 |
| `charge-full-design-microamp-hours` | `int` | 电池设计容量（Battery Design Capacity） |
| `re-charge-voltage-microvolt` | `int` | 自动重新开始充电的阈值 |
| `precharge-current-microamp` | `int` | 预充电阶段（Pre-charge Phase）的电流 |
| `charge-term-current-microamp` | `int` | 充电终止阶段（Charge Termination Phase）的电流 |
| `constant-charge-current-max-microamp` | `int` | 最大恒定输入电流（Maximum Constant Input Current） |
| `factory-internal-resistance-micro-ohms` | `int` | 电池出厂内阻（Factory Internal Resistance） |

本页没有已弃用的节点专用属性。

---

[上一章](P001_adi_adp5360-charger.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_nordic_npm10xx-charger.md)
