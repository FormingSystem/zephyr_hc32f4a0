---
id: learning.zephyr-docs.power-control-binding-reference.page-15
title: nxp_pdcfg-power
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/power/nxp,pdcfg-power.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第15章\_nxp_pdcfg-power

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/power/nxp,pdcfg-power.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-pdcfg-power"></a>
<a id="dtbinding-nxp-pdcfg-power"></a>
<a id="std-dtcompatible-nxp-pdcfg-power"></a>

兼容字符串（Compatible String）：`nxp,pdcfg-power`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,pdcfg-power)。

<a id="description"></a>

通过PDCFG寄存器进行NXP电源管理（Power Management）的属性。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 15.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `deep-sleep-config` | `array` | 写入PDSLEEPCFG寄存器的值数组，用于控制CPU深度睡眠期间各模块的供电；这些值在进入深度睡眠前写入睡眠配置寄存器 |

本页没有已弃用的节点专用属性。

## 15.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

以下是通用电源状态（Generic Power State）的基础属性。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `power-state-name` | `string` | **必需**。表示电源状态（Power State）；合法值：`active, runtime-idle, suspend-to-idle, standby, suspend-to-ram, suspend-to-disk, soft-off` |
| `substate-id` | `int` | 平台专用标识（Platform-specific Identification） |
| `min-residency-us` | `int` | 最短驻留时间（Minimum Residency Duration），单位微秒。包含进入状态所需时间，表示从能耗角度值得进入该空闲状态的最低时长。与选择浅一级状态相比，此时间是使实际节能抵偿进入和退出所耗时间与能量的收支平衡（Break-even）点 |
| `exit-latency-us` | `int` | 退出空闲状态所需的最坏情况延迟（Worst-case Latency），单位微秒 |
| `zephyr,pm-device-disabled` | `boolean` | 为此状态禁用系统管理的设备电源管理（System-managed Device Power Management）。设置后，电源管理子系统进入此状态前不会挂起设备 |

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

---

[上一章](P014_nxp_cmc.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_nxp_rw-pmu.md)
