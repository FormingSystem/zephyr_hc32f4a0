---
id: learning.zephyr-docs.charger-binding-reference.page-4
title: nxp_pca9422-charger
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/nxp,pca9422-charger.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第4章\_nxp_pca9422-charger

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/nxp,pca9422-charger.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-pca9422-charger"></a>
<a id="dtbinding-nxp-pca9422-charger"></a>
<a id="std-dtcompatible-nxp-pca9422-charger"></a>

兼容字符串（Compatible String）：`nxp,pca9422-charger`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,pca9422-charger)。

驱动源码（Driver Source）：[drivers/charger/charger_pca9422.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/charger_pca9422.c)。

<a id="description"></a>

NXP PCA9422电池充电器（Battery Charger）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 4.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `constant-charge-current-max-microamp` | `int` | **必需**。初始化时设置的快速充电电流，单位µA，可用范围2.5至640 mA。向下取整到最接近的硬件支持值；设为0（默认）时，驱动初始化跳过充电电流设置 |
| `constant-charge-voltage-max-microvolt` | `int` | **必需**。电池充电最高电压，默认4.2 V，与设备复位配置一致 |
| `precharge-current-percent` | `int` | 预充电电流占快速充电电流的百分比，可为7%或16%；详情参见CHARGER_CNTL_1寄存器说明；默认值：`16`；合法值：`7, 16` |
| `charge-termination-current-percent` | `int` | 补足充电电流（Top-off Current），按快速充电电流的百分比乘10编码，比例为2.5%、5.0%、7.5%或10.0%。电流低于此值时结束充电；详情参见CHARGER_CNTL_4寄存器说明；默认值：`25`；合法值：`25, 50, 75, 100` |
| `re-charge-threshold-microvolt` | `int` | 相对于Vbat_reg的再充电阈值，详情参见CHARGER_CNTL_4寄存器说明；默认值：`100000`；合法值：`100000, 150000, 200000` |
| `input-current-limit-microamp` | `int` | VIN输入电流限制，范围45至1195 mA；默认值：`470000` |
| `system-voltage-min-threshold-microvolt` | `int` | 系统稳压电压（System Regulation Voltage），比Vbat_reg高200 mV；Vbatreg受到Vsys_reg − 200 mV的钳位限制；默认值：`4550000` |
| `device-chemistry` | `string` | 描述电池的化学体系（Chemical Technology）。lithium-ion是所有锂离子电池（Lithium-ion Battery）的通用类型；未知具体化学体系时，可使用此值代替更精确的lithium-ion-X选项；合法值：`nickel-cadmium, nickel-metal-hydride, lithium-ion, lithium-ion-polymer, lithium-ion-iron-phosphate, lithium-ion-manganese-oxide` |
| `ocv-capacity-table-0` | `array` | 开路电压（Open-circuit Voltage，OCV）数组，根据当前OCV值查询电池容量，电压单位微伏。与Linux对应属性不同，此数组必须恰有11个元素，以10%为步进，表示0%至100%电量所对应的电压 |
| `charge-full-design-microamp-hours` | `int` | 电池设计容量（Battery Design Capacity） |
| `re-charge-voltage-microvolt` | `int` | 自动重新开始充电的阈值 |
| `precharge-current-microamp` | `int` | 预充电阶段（Pre-charge Phase）的电流 |
| `charge-term-current-microamp` | `int` | 充电终止阶段（Charge Termination Phase）的电流 |
| `factory-internal-resistance-micro-ohms` | `int` | 电池出厂内阻（Factory Internal Resistance） |

本页没有已弃用的节点专用属性。

---

[上一章](P003_nordic_npm10xx-charger.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_nxp_pf1550-charger.md)
