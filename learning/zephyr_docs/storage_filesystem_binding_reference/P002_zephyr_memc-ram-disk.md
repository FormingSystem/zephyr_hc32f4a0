---
id: learning.zephyr-docs.storage-filesystem-binding-reference.page-2
title: zephyr_memc-ram-disk
kind: reference
status: maintained
domains: [zephyr, devicetree, storage]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/disk/zephyr,memc-ram-disk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第2章\_zephyr_memc-ram-disk

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/disk/zephyr,memc-ram-disk.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-memc-ram-disk"></a>
<a id="dtbinding-zephyr-memc-ram-disk"></a>
<a id="std-dtcompatible-zephyr-memc-ram-disk"></a>

兼容字符串（Compatible String）：`zephyr,memc-ram-disk`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,memc-ram-disk)。

驱动源码（Driver Source）：[drivers/disk/memc_ramdisk.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/memc_ramdisk.c)。

<a id="description"></a>

以外部存储器设备作为后端的RAM磁盘（RAM Disk），通过存储器控制器（Memory Controller，MEMC）子系统API `memc_read`／`memc_write`访问。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 2.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `memc` | `phandle` | **必需**。管理后端存储器的MEMC设备节点引用（Phandle）；所引用设备必须实现MEMC驱动API。 |
| `disk-name` | `string` | **必需**。磁盘名称（Disk Name）。 |
| `sector-size` | `int` | **必需**。磁盘扇区大小（Sector Size），单位为字节。；合法值：`512, 1024, 2048, 4096, 8192, 16384, 32768, 65536` |
| `sector-count` | `int` | **必需**。扇区数量。 |

本页没有已弃用的节点专用属性。

---

[上一章](P001_zephyr_ftl-dhara.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_zephyr_ram-disk.md)
