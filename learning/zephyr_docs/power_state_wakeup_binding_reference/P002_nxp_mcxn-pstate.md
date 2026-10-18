---
id: learning.zephyr-docs.power-state-wakeup-binding-reference.page-2
title: nxp_mcxn-pstate
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/p_state/nxp,mcxn-pstate.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第2章\_nxp_mcxn-pstate

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/p_state/nxp,mcxn-pstate.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-mcxn-pstate"></a>
<a id="dtbinding-nxp-mcxn-pstate"></a>
<a id="std-dtcompatible-nxp-mcxn-pstate"></a>

兼容字符串（Compatible String）：`nxp,mcxn-pstate`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,mcxn-pstate)。

<a id="description"></a>

NXP MCXN系列为性能状态（Performance State，P-state）实现的自定义属性。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 2.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `cpu-frequency-level` | `string` | 与此性能状态关联的CPU频率级别（Frequency Level），对应SoC支持的预定义CPU频率级别；合法值：`low, medium, high` |
| `load-threshold` | `int` | 进入此性能状态的CPU负载阈值（Load Threshold），单位百分比。CPU负载超过阈值后，该状态才成为P-state驱动可以切换到的有效状态 |

本页没有已弃用的节点专用属性。

---

[上一章](P001_nxp_imx9-pstate.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_arm_fvp-pwrc.md)
