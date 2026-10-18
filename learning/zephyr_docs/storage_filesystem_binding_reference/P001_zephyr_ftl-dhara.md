---
id: learning.zephyr-docs.storage-filesystem-binding-reference.page-1
title: zephyr_ftl-dhara
kind: reference
status: maintained
domains: [zephyr, devicetree, storage]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/disk/zephyr,ftl-dhara.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第1章\_zephyr_ftl-dhara

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/disk/zephyr,ftl-dhara.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-ftl-dhara"></a>
<a id="dtbinding-zephyr-ftl-dhara"></a>
<a id="std-dtcompatible-zephyr-ftl-dhara"></a>

兼容字符串（Compatible String）：`zephyr,ftl-dhara`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,ftl-dhara)。

驱动源码（Driver Source）：[drivers/disk/ftl_dhara.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/ftl_dhara.c)。

<a id="description"></a>

在Flash分区上采用Dhara实现的闪存转换层（Flash Translation Layer，FTL）磁盘驱动。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 1.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `partition` | `phandle` | **必需**。用作后端存储（Backing Storage）的Flash Map分区。 |
| `disk-name` | `string` | **必需**。磁盘名称（Disk Name）。 |
| `buffer-size` | `int` | **必需**。FTL驱动缓冲区大小，单位为字节，必须大于或等于后端Flash的页大小（Page Size）。 |

本页没有已弃用的节点专用属性。

---

[本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_zephyr_memc-ram-disk.md)
