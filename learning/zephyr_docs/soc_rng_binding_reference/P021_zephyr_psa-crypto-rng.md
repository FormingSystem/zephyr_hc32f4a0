---
id: learning.zephyr-docs.soc-rng-binding-reference.page-21
title: zephyr_psa-crypto-rng
kind: reference
status: maintained
domains: [zephyr, devicetree, rng]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/rng/zephyr,psa-crypto-rng.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第21章\_zephyr_psa-crypto-rng

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/rng/zephyr,psa-crypto-rng.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-psa-crypto-rng"></a>
<a id="dtbinding-zephyr-psa-crypto-rng"></a>
<a id="std-dtcompatible-zephyr-psa-crypto-rng"></a>

兼容字符串（Compatible String）：`zephyr,psa-crypto-rng`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,psa-crypto-rng)。

驱动源码（Driver Source）：[drivers/entropy/entropy_psa_crypto.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/entropy/entropy_psa_crypto.c)。

<a id="description"></a>

PSA Crypto随机数发生器／熵（Random Number Generator/Entropy，RNG/Entropy）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 21.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

---

[上一章](P020_wch_rng.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
