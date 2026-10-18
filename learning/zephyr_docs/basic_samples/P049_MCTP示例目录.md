---
id: learning.zephyr-docs.basic_samples.page-49
title: MCTP示例目录
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/pmci/mctp/mctp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mctp"></a>

# 第49章\_MCTP示例目录

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/pmci/mctp/mctp.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

这些示例展示如何在Zephyr中使用管理组件传输协议（Management Component Transport Protocol，MCTP）构建能够相互通信的固件。

- [MCTP串行端点（MCTP Endpoint Sample）](P050_MCTP串行端点示例.md#mctp_endpoint_sample)：通过UART创建MCTP端点。
- [MCTP串行主机（MCTP Host Sample）](P051_MCTP串行主机示例.md#mctp_host_sample)：通过UART创建MCTP主机。
- [MCTP I2C GPIO端点节点（MCTP I2C GPIO Endpoint Node Sample）](P052_MCTPI2C端点示例.md#mctp_i2c_bus_endpoint)：创建通过GPIO信号控制I2C的MCTP端点节点。
- [MCTP I2C GPIO顶层节点（MCTP I2C GPIO Top Node Sample）](P053_MCTPI2C顶层节点示例.md#mctp_i2c_bus_host)：创建通过GPIO信号控制I2C的MCTP顶层节点。
- [MCTP I3C端点节点（MCTP I3C Endpoint Node Sample）](P054_MCTPI3C端点示例.md#mctp_i3c_bus_endpoint)：通过I3C创建MCTP端点节点。
- [MCTP I3C顶层节点（MCTP I3C Top Node Sample）](P055_MCTPI3C顶层节点示例.md#mctp_i3c_bus_host)：创建控制I3C的MCTP顶层节点。
- [MCTP USB端点节点（MCTP USB Endpoint Node Sample）](../usb/P191_MCTPUSB端点示例.md#mctp-usb-endpoint)：通过USB设备接口创建MCTP端点节点。


对应官方文档源码：[samples/subsys/pmci/mctp/mctp.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/pmci/mctp/mctp.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/subsys/pmci/mctp/mctp.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P048_PMCI示例目录.md) · [返回大纲](大纲.md) · [下一章](P050_MCTP串行端点示例.md)
