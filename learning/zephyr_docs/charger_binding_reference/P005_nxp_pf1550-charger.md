---
id: learning.zephyr-docs.charger-binding-reference.page-5
title: nxp_pf1550-charger
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/nxp,pf1550-charger.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第5章\_nxp_pf1550-charger

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/nxp,pf1550-charger.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-pf1550-charger"></a>
<a id="dtbinding-nxp-pf1550-charger"></a>
<a id="std-dtcompatible-nxp-pf1550-charger"></a>

兼容字符串（Compatible String）：`nxp,pf1550-charger`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,pf1550-charger)。

驱动源码（Driver Source）：[drivers/charger/charger_pf1550.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/charger_pf1550.c)。

<a id="description"></a>

NXP PF1550电池充电器（Battery Charger）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 5.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `constant-charge-voltage-max-microvolt` | `int` | **必需**。最大恒定输入电压（Maximum Constant Input Voltage） |
| `constant-charge-current-max-microamp` | `int` | **必需**。最大恒定输入电流（Maximum Constant Input Current） |
| `pf1550,vbus-current-limit-microamp` | `int` | **必需**。VBUS电流限制，单位微安 |
| `pf1550,system-voltage-min-threshold-microvolt` | `int` | **必需**。系统电压最小阈值（Minimum Threshold）；合法值：`3500000, 3700000, 4300000` |
| `pf1550,thermistor-monitoring-mode` | `string` | **必需**。热敏电阻监测模式（Thermistor Monitoring Mode），详情参见ThrmCfg寄存器说明及表2；合法值：`disabled, thermistor, JEITA-1, JEITA-2` |
| `pf1550,int-gpios` | `phandle-array` | **必需**。中断引脚（Interrupt Pin） |
| `pf1550,led-behaviour` | `string` | **必需**。充电器LED的行为（Behaviour）；合法值：`on-in-charging-flash-in-fault, flash-in-charging-on-in-fault, manual-off` |
| `device-chemistry` | `string` | 描述电池的化学体系（Chemical Technology）。lithium-ion是所有锂离子电池（Lithium-ion Battery）的通用类型；未知具体化学体系时，可使用此值代替更精确的lithium-ion-X选项；合法值：`nickel-cadmium, nickel-metal-hydride, lithium-ion, lithium-ion-polymer, lithium-ion-iron-phosphate, lithium-ion-manganese-oxide` |
| `ocv-capacity-table-0` | `array` | 开路电压（Open-circuit Voltage，OCV）数组，根据当前OCV值查询电池容量，电压单位微伏。与Linux对应属性不同，此数组必须恰有11个元素，以10%为步进，表示0%至100%电量所对应的电压 |
| `charge-full-design-microamp-hours` | `int` | 电池设计容量（Battery Design Capacity） |
| `re-charge-voltage-microvolt` | `int` | 自动重新开始充电的阈值 |
| `precharge-current-microamp` | `int` | 预充电阶段（Pre-charge Phase）的电流 |
| `charge-term-current-microamp` | `int` | 充电终止阶段（Charge Termination Phase）的电流 |
| `factory-internal-resistance-micro-ohms` | `int` | 电池出厂内阻（Factory Internal Resistance） |

本页没有已弃用的节点专用属性。

---

[上一章](P004_nxp_pca9422-charger.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_sbs_sbs-charger.md)
