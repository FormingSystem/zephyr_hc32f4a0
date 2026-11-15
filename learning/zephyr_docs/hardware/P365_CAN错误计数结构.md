---
id: learning.zephyr-docs.hardware.canstruct-2
title: CAN错误计数结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcan__bus__err__cnt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第365章\_CAN错误计数结构

原文：[structcan__bus__err__cnt](https://docs.zephyrproject.org/latest/doxygen/html/structcan__bus__err__cnt.html)。读取日期：2026-10-13，`latest`。

## 365.1\_控制器错误计数

[`can_bus_err_cnt`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__bus__err__cnt.html) 保存控制器局域网（Controller Area Network，CAN）控制器的错误计数，声明来自 `zephyr/drivers/can.h`。它区分发送（Transmit，TX）和接收（Receive，RX）两个方向。

## 365.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a01bb2cb16656d0fd4f99cfbfa1f30e98"></a>[`tx_err_cnt`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__bus__err__cnt.html#a01bb2cb16656d0fd4f99cfbfa1f30e98) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 控制器发送错误计数器的值 |
| <a id="a6be6ce6b592641ba0dce36fe1cd8902a"></a>[`rx_err_cnt`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__bus__err__cnt.html#a6be6ce6b592641ba0dce36fe1cd8902a) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 控制器接收错误计数器的值 |

---

[上一章：CAN过滤器结构](P364_CAN过滤器结构.md) · [下一章：CAN时序结构](P366_CAN时序结构.md) · [返回大纲](大纲.md)
