---
id: learning.zephyr-docs.hardware.canstruct-0
title: CAN帧结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcan__frame.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第363章\_CAN帧结构

原文：[structcan__frame](https://docs.zephyrproject.org/latest/doxygen/html/structcan__frame.html)。读取日期：2026-10-13，`latest`。

## 363.1\_帧头与负载

[`can_frame`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__frame.html) 是控制器局域网（Controller Area Network，CAN）的帧（Frame）结构，声明来自 `zephyr/drivers/can.h`。标识符与标志描述帧类型，数据长度码（Data Length Code，DLC）表示负载长度，负载（Payload）可按 8 位或 32 位值访问。

## 363.2\_字段定义

| 字段 | 类型或声明 | 含义 |
| --- | --- | --- |
| <a id="a7ad0d8d62322affafbfd23839ee81d5d"></a>[`id`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__frame.html#a7ad0d8d62322affafbfd23839ee81d5d) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 标准 11 位或扩展 29 位 CAN 标识符 |
| <a id="a014c42277e886906e6c761bc6f21fb47"></a>[`dlc`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__frame.html#a014c42277e886906e6c761bc6f21fb47) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 表示数据字节长度的 DLC |
| <a id="a1e71125342a01a6e5a68a14cb075ce7c"></a>[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__frame.html#a1e71125342a01a6e5a68a14cb075ce7c) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 帧标志，见 [`CAN_FRAME_FLAGS`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#CAN_FRAME_FLAGS) |
| <a id="ae46f8b0821c638517959274bbbda5932"></a>[`timestamp`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__frame.html#ae46f8b0821c638517959274bbbda5932) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 接收该帧时捕获的控制器自由运行计时器值 |
| <a id="ac4b43443b2a338d35f0e1d3ef8355960"></a>[`data`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__frame.html#ac4b43443b2a338d35f0e1d3ef8355960) | `uint8_t data[CAN_MAX_DLEN]` | 按无符号 8 位值访问负载 |
| <a id="ad88af93a2171e4c9d617b91b403d842a"></a>[`data_32`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__frame.html#ad88af93a2171e4c9d617b91b403d842a) | `uint32_t data_32[DIV_ROUND_UP(CAN_MAX_DLEN, sizeof(uint32_t))]` | 按无符号 32 位值访问负载 |

`data` 与 `data_32` 位于匿名联合体（Anonymous Union）中，代表同一份帧负载。`CAN_MAX_DLEN` 是数据容量宏，[`DIV_ROUND_UP`](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37) 将容量除以 32 位元素大小并向上取整；本页未给出容量宏的具体值。

> 译注：DLC 是长度编码，不能据“字节长度”措辞就把所有 DLC 值直接当成字节数。公共接口提供 `can_dlc_to_bytes` 与 `can_bytes_to_dlc` 完成转换。

## 363.3\_接收时间戳

`timestamp` 只有在启用 Kconfig 配置项 [`CONFIG_CAN_RX_TIMESTAMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CAN_RX_TIMESTAMP) 时才存在。控制器的自由运行计时器（Free-Running Timer）每个位时间递增一次，在帧起始位（Start Of Frame，SOF）捕获其值，作为接收时间戳（Timestamp）。

---

[上一章：CAN控制器接口](P362_CAN控制器接口.md) · [下一章：CAN过滤器结构](P364_CAN过滤器结构.md) · [返回大纲](大纲.md)
