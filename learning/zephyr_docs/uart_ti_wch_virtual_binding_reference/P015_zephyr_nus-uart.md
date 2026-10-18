---
id: learning.zephyr-docs.uart-ti-wch-virtual-binding-reference.page-15
title: zephyr_nus-uart
kind: reference
status: maintained
domains: [zephyr, devicetree, uart]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/serial/zephyr,nus-uart.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第15章\_zephyr_nus-uart

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/serial/zephyr,nus-uart.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-nus-uart"></a>
<a id="dtbinding-zephyr-nus-uart"></a>
<a id="std-dtcompatible-zephyr-nus-uart"></a>

兼容字符串（Compatible String）：`zephyr,nus-uart`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,nus-uart)。

驱动源码（Driver Source）：[drivers/serial/uart_bt.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/serial/uart_bt.c)。

<a id="description"></a>

通过Nordic UART服务（Nordic UART Service，NUS）提供UART，传输使用低功耗蓝牙（Bluetooth Low Energy，Bluetooth LE）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 15.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `tx-fifo-size` | `int` | 虚拟UART发送FIFO的大小。；默认值：`1024` |
| `rx-fifo-size` | `int` | 虚拟UART接收FIFO的大小。；默认值：`1024` |

本页没有已弃用的节点专用属性。

---

[上一章](P014_zephyr_native-tty-uart.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_zephyr_uart-bitbang.md)
