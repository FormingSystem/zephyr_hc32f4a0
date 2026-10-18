---
id: learning.zephyr-docs.platform-rmt-openthread-binding-reference.page-7
title: openthread_config
kind: reference
status: maintained
domains: [zephyr, devicetree, platform]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/options/openthread,config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第7章\_openthread_config

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/options/openthread,config.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="openthread-config"></a>
<a id="dtbinding-openthread-config"></a>
<a id="std-dtcompatible-openthread-config"></a>

兼容字符串（Compatible String）：`openthread,config`。厂商：[ OpenThread.io ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-openthread)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=openthread,config)。

<a id="description"></a>

OpenThread配置节点（Configuration Node）。下方保留诊断及引导加载程序GPIO的使用原例。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 7.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `diag-gpios` | `phandle-array` | 启用诊断GPIO（Diagnostic GPIO）引脚访问。每项包含GPIO引脚配置：控制器节点引用（Phandle）、引脚编号和配置标志（Configuration Flags）。 |
| `bootloader-gpios` | `phandle-array` | 允许通过触发指定GPIO引脚，复位进入引导加载程序（Bootloader）。属性表示选定GPIO的配置：控制器节点引用（Phandle）、引脚编号和配置标志。 |

本页没有已弃用的节点专用属性。

## OpenThread配置节点原例

```dts
options {
  openthread {
    compatible = "openthread,config";
    diag-gpios = <&gpio0 0  GPIO_ACTIVE_HIGH>,
                 <&gpio1 0  GPIO_ACTIVE_LOW>;
    bootloader-gpios = <&gpio0 1 GPIO_ACTIVE_HIGH>;
  };
};
```

---

[上一章](P006_intel_adsp-dfpmccu.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P008_espressif_esp32-rmt.md)
