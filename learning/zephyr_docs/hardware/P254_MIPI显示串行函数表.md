---
id: learning.zephyr-docs.hardware.mipibackend-3
title: MIPI显示串行函数表
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第254章\_MIPI显示串行函数表

原文：[structmipi__dsi__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__driver__api.html)。读取日期：2026-10-13，`latest`。

## 254.1\_用途与成员要求

结构 [`mipi_dsi_driver_api`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__driver__api.html) 是每个 MIPI **显示串行接口（Display Serial Interface，DSI）**驱动需要定义的 **驱动操作（Driver Operations）**表，包含实现的操作函数指针及驱动专用的其他常量数据，定义来自 `zephyr/drivers/mipi_dsi.h`。

标为 **必需（Required，REQ）**的成员必须设置；标为 **可选（Optional，OPT）**的成员按需提供。

本表 [`attach`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__driver__api.html#a246757a8c84029b7c2f75962558dd4dd) 与 [`transfer`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__driver__api.html#af8d27427074067a34938600d58c53df4) 为必需，[`detach`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dsi__driver__api.html#a264e060eb462dc4b125cfbb1480cb2fd) 为可选。

## 254.2\_数据字段（Data Fields）

回调类型的完整声明见[后端接口](P253_MIPI显示串行后端.md)。

| 字段 | 类型 | 要求 | 含义 |
| --- | --- | --- | --- |
| `attach` | [`mipi_dsi_api_attach_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#ga9abb63e5c7cdb7597376a237a420c2b5) | REQ | 将新设备连接到 DSI 总线。 |
| `transfer` | [`mipi_dsi_api_transfer_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#ga9ebc67e63c629c75ff61fa220a2787a0) | REQ | 向总线上连接的设备传输数据或从其接收数据。 |
| `detach` | [`mipi_dsi_api_detach_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dsi__interface__backend.html#gaf5e12800d2a80e8a78da16cb5a71b008) | OPT | 将设备从 DSI 总线分离。 |

## 254.3\_相关定义宏

原文关联的设备与接口定义宏为 [`DEVICE_DT_INST_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)、[`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)、[`DEVICE_API()`](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)。

---

[上一章：MIPI显示串行后端](P253_MIPI显示串行后端.md) · [下一章：PWM公共接口](P255_PWM公共接口.md) · [返回大纲](大纲.md)
