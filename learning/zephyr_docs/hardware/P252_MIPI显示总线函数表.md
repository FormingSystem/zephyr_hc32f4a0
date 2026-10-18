---
id: learning.zephyr-docs.hardware.mipibackend-1
title: MIPI显示总线函数表
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第252章\_MIPI显示总线函数表

原文：[structmipi__dbi__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html)。读取日期：2026-10-13，`latest`。

## 252.1\_用途与成员要求

结构 [`mipi_dbi_driver_api`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html) 是每个 MIPI **显示总线接口（Display Bus Interface，DBI）**驱动需要定义的 **驱动操作（Driver Operations）**表，包含实现的操作函数指针及驱动专用的其他常量数据，定义来自 `zephyr/drivers/mipi_dbi.h`。

标为 **必需（Required，REQ）**的成员必须设置；标为 **可选（Optional，OPT）**的成员按需提供。

本表六项成员都标为 OPT；TE 指撕裂效应同步信号（Tearing Effect）。

## 252.2\_数据字段（Data Fields）

回调类型的完整声明见[后端接口](P251_MIPI显示总线后端.md)。

| 字段 | 类型 | 要求 | 含义 |
| --- | --- | --- | --- |
| [`command_write`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#a62eb8d9e45d888a9db25e0a44374e098) | [`mipi_dbi_command_write_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga3ea6251e2fe3a18c8daba66c4ded41d6) | OPT | 向显示控制器写入命令。 |
| [`command_read`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#a8987136f1e4f903cb0177fe9b16094d3) | [`mipi_dbi_command_read_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga7c6f09c6fece9c343aa4717150ca170e) | OPT | 读取显示控制器的命令响应。 |
| [`write_display`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#a33702cb0358588ffebeb11bd97b287c5) | [`mipi_dbi_write_display_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#gad973c1d30050ea3b6c3f9e1032e5383c) | OPT | 向显示控制器写入显示缓冲区。 |
| [`reset`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#a74275012d87749477c7c05a437b0a8d4) | [`mipi_dbi_reset_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga37ac264a3130d34a8d594c7482b09870) | OPT | 复位所连接的显示控制器。 |
| [`release`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#ab53ff7394b4b56128fd17e2a0bfa2045) | [`mipi_dbi_release_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga12f0446626ab4feb996f33fcea4129dd) | OPT | 释放锁定的 DBI 设备。 |
| [`configure_te`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__dbi__driver__api.html#aa615fbe9f882fd10d967c4693bb7664f) | [`mipi_dbi_configure_te_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__dbi__interface__backend.html#ga2000c1dc2ac1efe0eb6179a18da1e5c2) | OPT | 配置撕裂效应同步信号。 |

## 252.3\_相关定义宏

原文关联的设备与接口定义宏为 [`DEVICE_DT_INST_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)、[`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)、[`DEVICE_API()`](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)。

---

[上一章：MIPI显示总线后端](P251_MIPI显示总线后端.md) · [下一章：MIPI显示串行后端](P253_MIPI显示串行后端.md) · [返回大纲](大纲.md)
