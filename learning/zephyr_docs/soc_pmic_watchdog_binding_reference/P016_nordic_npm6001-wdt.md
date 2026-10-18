---
id: learning.zephyr-docs.soc-pmic-watchdog-binding-reference.page-16
title: nordic_npm6001-wdt
kind: reference
status: maintained
domains: [zephyr, devicetree, watchdog]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/watchdog/nordic,npm6001-wdt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第16章\_nordic_npm6001-wdt

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/watchdog/nordic,npm6001-wdt.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nordic-npm6001-wdt"></a>
<a id="dtbinding-nordic-npm6001-wdt"></a>
<a id="std-dtcompatible-nordic-npm6001-wdt"></a>

兼容字符串（Compatible String）：`nordic,npm6001-wdt`。厂商：[ Nordic Semiconductor ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nordic)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nordic,npm6001-wdt)。

驱动源码（Driver Source）：[drivers/watchdog/wdt_npm6001.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/watchdog/wdt_npm6001.c)。

<a id="description"></a>

nPM6001看门狗（Watchdog）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

没有顶层属性（No Top-level Properties）。

---

[上一章](P015_nordic_npm2100-wdt.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
