---
id: learning.zephyr-docs.power-control-binding-reference.page-12
title: nuvoton_npcx-power-state
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/power/nuvoton,npcx-power-state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第12章\_nuvoton_npcx-power-state

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/power/nuvoton,npcx-power-state.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nuvoton-npcx-power-state"></a>
<a id="dtbinding-nuvoton-npcx-power-state"></a>
<a id="std-dtcompatible-nuvoton-npcx-power-state"></a>

兼容字符串（Compatible String）：`nuvoton,npcx-power-state`。厂商：[ Nuvoton Technology Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nuvoton)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nuvoton,npcx-power-state)。

<a id="description"></a>

NPCX电源管理空闲状态（Power Management Idle State），为通用电源状态扩展NPCX深度睡眠子状态（Deep Sleep Sub-state）的专用属性。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 12.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `unlimited-instant-wakeup` | `boolean` | 深度睡眠驻留时间（Residency）无论多长，即时唤醒（Instant Wake-up）路径都保持有效。省略时，仅保证驻留短于200 ms可即时唤醒，超过时必须使用标准唤醒子状态。仅NPCX4及之后系列支持，早期系列无此控制位并忽略本属性 |

本页没有已弃用的节点专用属性。

## 12.2\_基础属性

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

[上一章](P011_nuvoton_npcx-power-psl.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_nxp_aon-wakeup-pin.md)
