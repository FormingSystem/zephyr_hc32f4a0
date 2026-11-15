---
id: learning.zephyr-docs.hardware.canstruct-5
title: CAN设备状态结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcan__device__state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第368章\_CAN设备状态结构

原文：[structcan__device__state](https://docs.zephyrproject.org/latest/doxygen/html/structcan__device__state.html)。读取日期：2026-10-13，`latest`。

## 368.1\_CAN类别专用状态

[`can_device_state`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__device__state.html) 为控制器局域网（Controller Area Network，CAN）设备类别提供专用状态扩展，声明来自 `zephyr/drivers/can.h`。只有启用 Kconfig 配置项 [`CONFIG_CAN_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_STATS) 时才可用。

## 368.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a28061ff1193176dd01b7bb9a88f402ec"></a>[`devstate`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__device__state.html#a28061ff1193176dd01b7bb9a88f402ec) | `struct device_state` | 通用设备状态 |
| <a id="ae05c85eae4f6bee075ffdc4f0ab56f47"></a>[`stats`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__device__state.html#ae05c85eae4f6bee075ffdc4f0ab56f47) | `struct stats_can` | CAN 设备统计（Statistics） |

---

[上一章：CAN状态变化回调结构](P367_CAN状态变化回调结构.md) · [下一章：CAN控制器后端接口](P369_CAN控制器后端接口.md) · [返回大纲](大纲.md)
