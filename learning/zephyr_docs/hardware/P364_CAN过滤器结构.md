---
id: learning.zephyr-docs.hardware.canstruct-1
title: CAN过滤器结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcan__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第364章\_CAN过滤器结构

原文：[structcan__filter](https://docs.zephyrproject.org/latest/doxygen/html/structcan__filter.html)。读取日期：2026-10-13，`latest`。

## 364.1\_匹配标识符

[`can_filter`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__filter.html) 是控制器局域网（Controller Area Network，CAN）的过滤器（Filter）结构，声明来自 `zephyr/drivers/can.h`。它组合目标标识符、匹配掩码和过滤标志。

## 364.2\_字段与掩码规则

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="adf2b18eab11d360780707478a1f624b9"></a>[`id`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__filter.html#adf2b18eab11d360780707478a1f624b9) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 要匹配的 CAN 标识符 |
| <a id="a15632117f3f031fbbeb28ef562f9ac94"></a>[`mask`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__filter.html#a15632117f3f031fbbeb28ef562f9ac94) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 标识符匹配掩码（Mask） |
| <a id="a7616e21f33be5fb43094d44530a1c5de"></a>[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__filter.html#a7616e21f33be5fb43094d44530a1c5de) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 标志，见 [`CAN_FILTER_FLAGS`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#CAN_FILTER_FLAGS) |

如果 `mask` 中某一位为 0，过滤器就忽略 [`id`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__filter.html#adf2b18eab11d360780707478a1f624b9) 中对应位的值。

---

[上一章：CAN帧结构](P363_CAN帧结构.md) · [下一章：CAN错误计数结构](P365_CAN错误计数结构.md) · [返回大纲](大纲.md)
