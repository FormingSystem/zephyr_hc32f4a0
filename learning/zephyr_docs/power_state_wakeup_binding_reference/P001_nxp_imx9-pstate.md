---
id: learning.zephyr-docs.power-state-wakeup-binding-reference.page-1
title: nxp_imx9-pstate
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/p_state/nxp,imx9-pstate.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第1章\_nxp_imx9-pstate

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/p_state/nxp,imx9-pstate.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-imx9-pstate"></a>
<a id="dtbinding-nxp-imx9-pstate"></a>
<a id="std-dtcompatible-nxp-imx9-pstate"></a>

兼容字符串（Compatible String）：`nxp,imx9-pstate`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,imx9-pstate)。

<a id="description"></a>

NXP i.MX9 Cortex-A应用内核的性能状态（Performance State，P-state）。本绑定由i.MX9系列共享，包括i.MX91、i.MX93、i.MX95、i.MX943及其衍生产品。每个P-state选择一个内核时钟频率，SoC驱动在进入该状态时应用。可用频率因SoC而异，只能请求驱动实现的频率，其他值在构建时会被拒绝。

SoC驱动可能只更改内核时钟，而让供电电压保持引导加载程序（Boot Loader）设定的电平；此时设备树所列全部频率都必须适用于该电压。如果簇（Cluster）内各核共享时钟源，则P-state作用于整个簇，SoC驱动要求对称多处理（Symmetric Multiprocessing，SMP）构建。配置原例见下文。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 1.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `load-threshold` | `int` | **必需**。进入此性能状态的CPU负载阈值（Load Threshold），单位百分比。CPU负载超过阈值后，该状态才成为P-state驱动可以切换到的有效状态 |
| `clock-frequency` | `int` | **必需**。选择此性能状态时采用的内核时钟频率（Core Clock Frequency），单位Hz。可接受值由SoC的P-state驱动定义 |

本页没有已弃用的节点专用属性。

## 性能状态配置原例

```dts
performance-states {
        pstate_0: pstate-0 {
                compatible = "nxp,imx9-pstate";
                load-threshold = <60>;
                clock-frequency = <DT_FREQ_M(1692)>;
        };
        pstate_1: pstate-1 {
                compatible = "nxp,imx9-pstate";
                load-threshold = <0>;
                clock-frequency = <DT_FREQ_M(900)>;
        };
};
```

---

[本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_nxp_mcxn-pstate.md)
