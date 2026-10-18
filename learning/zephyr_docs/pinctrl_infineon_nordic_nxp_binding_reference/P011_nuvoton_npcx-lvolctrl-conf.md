---
id: learning.zephyr-docs.pinctrl-infineon-nordic-nxp-binding-reference.page-11
title: nuvoton_npcx-lvolctrl-conf
kind: reference
status: maintained
domains: [zephyr, devicetree, pinctrl]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/nuvoton,npcx-lvolctrl-conf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第11章\_nuvoton_npcx-lvolctrl-conf

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pinctrl/nuvoton,npcx-lvolctrl-conf.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nuvoton-npcx-lvolctrl-conf"></a>
<a id="dtbinding-nuvoton-npcx-lvolctrl-conf"></a>
<a id="std-dtcompatible-nuvoton-npcx-lvolctrl-conf"></a>

兼容字符串（Compatible String）：`nuvoton,npcx-lvolctrl-conf`。厂商：[ Nuvoton Technology Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nuvoton)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nuvoton,npcx-lvolctrl-conf)。

<a id="description"></a>

Nuvoton NPCX7低电压电平检测配置映射（Low-Voltage Level Detection Configuration Map），连接NPCX GPIO与低电压控制器（LV_GPIO_CTL）的驱动实例。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 11.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `lvols` | `phandle-array` | **必需**。I/O与低电压控制器之间的配置映射列表。 |

---

[上一章](P010_nuvoton_npcx-leakage-io.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_nuvoton_npcx-pinctrl-conf.md)
