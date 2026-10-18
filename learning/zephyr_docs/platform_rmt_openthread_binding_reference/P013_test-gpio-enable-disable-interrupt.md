---
id: learning.zephyr-docs.platform-rmt-openthread-binding-reference.page-13
title: test-gpio-enable-disable-interrupt
kind: reference
status: maintained
domains: [zephyr, devicetree, platform]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/test/test-gpio-enable-disable-interrupt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第13章\_test-gpio-enable-disable-interrupt

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/test/test-gpio-enable-disable-interrupt.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="test-gpio-enable-disable-interrupt"></a>
<a id="dtbinding-test-gpio-enable-disable-interrupt"></a>
<a id="std-dtcompatible-test-gpio-enable-disable-interrupt"></a>

兼容字符串（Compatible String）：`test-gpio-enable-disable-interrupt`。厂商：[ Generic or vendor-independent ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-no-vendor)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=test-gpio-enable-disable-interrupt)。

<a id="description"></a>

此绑定提供在Zephyr中构建及运行 `tests/drivers/gpio/gpio_enable_disable_interrupt` 测试所需的资源。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 13.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `irq-gpios` | `phandle-array` | **必需**。将配置为中断输入（Interrupt Input）的GPIO标识。 |

本页没有已弃用的节点专用属性。

---

[上一章](P012_renesas_rx-swint.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_intel_adsp-uaol.md)
