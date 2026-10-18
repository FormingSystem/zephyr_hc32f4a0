---
id: learning.zephyr-docs.charger-binding-reference.page-1
title: adi_adp5360-charger
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/adi,adp5360-charger.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第1章\_adi_adp5360-charger

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/charger/adi,adp5360-charger.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="adi-adp5360-charger"></a>
<a id="dtbinding-adi-adp5360-charger"></a>
<a id="std-dtcompatible-adi-adp5360-charger"></a>

兼容字符串（Compatible String）：`adi,adp5360-charger`。厂商：[ Analog Devices, Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-adi)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=adi,adp5360-charger)。

驱动源码（Driver Source）：[drivers/charger/charger_adp5360.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/charger_adp5360.c)。

<a id="description"></a>

ADI ADP5360电池管理电源管理集成电路（Power Management Integrated Circuit，PMIC）。设备树（Devicetree，DT）将充电器建模为兼容字符串adi,adp5360节点的子设备。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 1.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `device-chemistry` | `string` | **必需**。描述电池的化学体系（Chemical Technology）。lithium-ion是所有锂离子电池（Lithium-ion Battery）的通用类型；未知具体化学体系时，可使用此值代替更精确的lithium-ion-X选项；合法值：`nickel-cadmium, nickel-metal-hydride, lithium-ion, lithium-ion-polymer, lithium-ion-iron-phosphate, lithium-ion-manganese-oxide` |
| `re-charge-voltage-microvolt` | `int` | 设备对此设置的默认值为120 mV；默认值：`120000` |
| `precharge-current-microamp` | `int` | 设备对此设置的默认值为5 mA；默认值：`5000` |
| `charge-term-current-microamp` | `int` | **必需**。充电终止阶段（Charge Termination Phase）的电流 |
| `constant-charge-current-max-microamp` | `int` | **必需**。最大恒定输入电流（Maximum Constant Input Current） |
| `constant-charge-voltage-max-microvolt` | `int` | **必需**。最大恒定输入电压（Maximum Constant Input Voltage） |
| `battery-name` | `string` | **必需**。连接到PMIC的电池名称 |
| `charger-init-adpichg-limit-uv` | `int` | 设置与VBUS电压阈值对应的初始自适应限流（Adaptive Current Limit），设备默认4.6 V；默认值：`4600000` |
| `battery-voltage-weak-threshold-uv` | `int` | 弱电池（Weak Battery）电压上升阈值，用于决定充电器模式。低于V_WEAK时进入弱电池充电（Weak Charge）模式，高于V_WEAK时进入快速充电（Fast Charge）模式；设备默认3 V；默认值：`3000000` |
| `charger-init-input-i-limit-ua` | `int` | VBUS的初始输入电流限制（Input Current Limit），设备默认100 mA；默认值：`100000` |
| `battery-voltage-cold-threshold-uv` | `int` | 电池低温（Cold Battery）状态的电压阈值，设备默认1.8 V；默认值：`1800000` |
| `battery-voltage-cool-threshold-uv` | `int` | 电池偏冷（Cool Battery）状态的电压阈值，设备默认1.13 V；默认值：`1130000` |
| `battery-voltage-warm-threshold-uv` | `int` | 电池偏热（Warm Battery）状态的电压阈值，设备默认286 mV；默认值：`286000` |
| `battery-voltage-hot-threshold-uv` | `int` | 电池高温（Hot Battery）状态的电压阈值，设备默认172 mV；默认值：`172000` |
| `thermistor-current-limit-ua` | `int` | 设置热敏电阻（Thermistor）电流ITHR，设备默认60 µA；默认值：`60`；合法值：`60, 12, 6` |
| `enable-thermistor-current` | `boolean` | 即使VBUS < VBUS_OK，也使能ITHR |
| `charger-voltage-trk-to-fast-uv` | `int` | 从涓流充电（Trickle Charge）切换至快速充电（Fast Charge）的电池电压阈值，设备默认2.5 V；默认值：`2500000`；合法值：`2000000, 2500000, 2600000, 2900000` |
| `disable-recharge` | `boolean` | 禁用充电器的再充电（Recharge）功能 |
| `enable-charge-complete-timer` | `boolean` | 使能充电完成定时器（Charge Complete Timer，tEND） |
| `enable-trickle-fast-charge-timer` | `boolean` | 使能涓流充电定时器tTRK和快速充电定时器tCHG |
| `trickle-fast-charge-timer-period` | `int` | 设置tTRK和tCHG周期：0对应15分钟与150分钟；1对应30分钟与300分钟；2对应45分钟与450分钟；3对应60分钟与600分钟。设备默认0；默认值：`0`；合法值：`0, 1, 2, 3` |
| `enable-jeita-temp-spec` | `boolean` | 启用日本电子信息技术产业协会（Japan Electronics and Information Technology Industries Association，JEITA）的锂离子电池温度充电规范 |
| `ilim-jeita-cool-10pct` | `boolean` | 电池偏冷时使用所编程ILIM的约10%；未设置时使用50% |
| `enable-voltage-adpichg` | `boolean` | 使能V_ADPICHG，以在充电期间进行自适应限流（Adaptive Current-limit） |
| `disable-end-of-charge` | `boolean` | 禁用充电结束（End of Charge）功能 |
| `set-vsys-5v` | `boolean` | 设置时将V_SYSTEM设为5 V，否则采用V_TRM + 200 mV |
| `disable-low-dropout` | `boolean` | 使能充电器低压差（Low-dropout，LDO）场效应管（Field-effect Transistor，FET）；充电器正常工作要求LDO处于活动状态。译注：原文说明写“使能”，与属性名disable-low-dropout相反，按原文保留，使用前应核对驱动与数据手册 |
| `disable-isofet` | `boolean` | 强制关断电池隔离场效应管（Battery Isolation FET） |
| `enable-battery-protection` | `boolean` | 使能充电器的电池保护（Battery Protection）功能 |
| `disable-charge-with-undervoltage` | `boolean` | 允许电池欠压（Undervoltage）时充电。译注：原文说明写“允许”，与属性名disable-charge-with-undervoltage相反，按原文保留 |
| `set-isofet-overcharge-off` | `boolean` | 过充事件（Overcharge Event）发生时关闭电池隔离FET；未设置时，过充会使其开启 |
| `set-overcurrent-discharge-hiccup` | `boolean` | 将放电过流保护（Overcurrent Discharge Protection）模式设为打嗝（Hiccup）模式；未设置时为锁存（Latch-up）模式 |
| `set-overcurrent-charge-hiccup` | `boolean` | 将充电过流保护（Overcurrent Charge Protection）模式设为打嗝（Hiccup）模式；未设置时为锁存（Latch-up）模式 |
| `battery-undervolt-discharge-threshold-uv` | `int` | 电池放电欠压阈值（Undervoltage Discharge Threshold），用于指示电池电压条件，设备默认2.5 V；默认值：`2500000` |
| `battery-undervolt-discharge-hysteresis` | `int` | 电池放电欠压迟滞（Hysteresis）百分比，表示相对放电欠压阈值的迟滞范围，设备默认2%；默认值：`2`；合法值：`2, 4, 6, 8` |
| `battery-undervolt-discharge-deglitch-ms` | `int` | 电池欠压去毛刺时间（Deglitch Time），表示电池电压越过阈值时的判定时间窗口，设备默认30 ms；默认值：`30`；合法值：`30, 60, 120, 240` |
| `battery-overcurrent-discharge-ua` | `int` | 电池放电过流阈值（Overcurrent Discharge Threshold），设备默认600 mA。原文随后称其指示电池充电条件（Battery Charging Condition），此处保留这一表述差异；默认值：`600000` |
| `battery-overcurrent-discharge-deglitch-us` | `int` | 电池过流去毛刺时间，表示放电电流越过阈值时的判定时间窗口，设备默认5 ms；默认值：`5000`；合法值：`500, 1000, 5000, 10000, 20000, 50000, 100000` |
| `battery-overvolt-charge-threshold-uv` | `int` | 电池充电过压阈值（Overvoltage Charge Threshold），指示电池电压条件，设备默认4.3 V；默认值：`4300000` |
| `battery-overvolt-charge-hysteresis` | `int` | 电池充电过压迟滞（Hysteresis）百分比，设备默认2%。原文称迟滞范围相对于电池放电欠压阈值，此处保留其与属性名的差异；默认值：`2`；合法值：`2, 4, 6, 8` |
| `battery-overvolt-charge-deglitch-ms` | `int` | 电池过压去毛刺时间，表示电池电压越过阈值时的判定时间窗口，设备默认500 ms；默认值：`500`；合法值：`500, 1000` |
| `battery-overcurrent-charge-ua` | `int` | 电池充电过流阈值（Overcurrent Charge Threshold），指示电池充电条件，设备默认150 mA；默认值：`150000` |
| `battery-overcurrent-charge-deglitch-ms` | `int` | 电池过流去毛刺时间，表示充电电流越过阈值时的判定时间窗口，设备默认10 ms；默认值：`10`；合法值：`5, 10, 20, 40` |

本页没有已弃用的节点专用属性。

---

[本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_maxim_max20335-charger.md)
