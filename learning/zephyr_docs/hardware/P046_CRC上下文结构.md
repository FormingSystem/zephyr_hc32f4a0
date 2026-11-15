---
id: learning.zephyr-docs.hardware.backend-0
title: CRC上下文结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第46章\_CRC上下文结构

原文：[structcrc__ctx](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html)。读取日期：2026-10-13，`latest`。

## 46.1\_计算上下文

`struct crc_ctx` 是 **循环冗余校验（Cyclic Redundancy Check，CRC）**的 **上下文（Context）**结构，声明于官方头文件 `zephyr/drivers/crc.h`。它保存计算所需的状态，包括正在计算的CRC类型、当前状态、多项式、初始种子值以及计算结果。

上下文由[CRC驱动接口](P038_CRC驱动接口参考.md)传入开始、更新和结束函数；它把一次计算相关的数据放在一起，不是另一个设备实例。

## 46.2\_字段说明

原页列出以下六个字段。C声明中的类型和字段名称保持原样。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`type`](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#afdbc947c22f2a0c048d841ef1ce50cd6) | `enum crc_type` | CRC计算类型。 |
| [`state`](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#a4f30eca04c874cf473f48c0324fab4ae) | `enum crc_state` | 当前CRC设备状态。 |
| [`reversed`](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#aca061dba391e5b236f6ad426815248ba) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | CRC输入／输出反转标志。 |
| [`polynomial`](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#a332fc129740671c28628dad7a86d3626) | [`crc_poly_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga938a05769aa6a61c22217611fb375218) | CRC多项式。 |
| [`seed`](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#ac1319345dc28aed6c72422e3e076d3cd) | [`crc_init_val_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga45ff64f03c4bfadd47ba66ce944c09bf) | CRC初始种子值。 |
| [`result`](https://docs.zephyrproject.org/latest/doxygen/html/structcrc__ctx.html#aee1dc43966d4f418139be8d52f9fdcba) | [`crc_result_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__crc__interface.html#ga7c6663d361406882a73e8ba171840adc) | CRC计算结果。 |

原页逐字段说明与上表一致；状态枚举、输入／输出反转标志和三个CRC值类型的含义见[CRC驱动接口参考](P038_CRC驱动接口参考.md)。原文未在此给出默认初始值，因此不能仅凭字段名推断可省略初始化或任意组合不同CRC类型的参数。

本结构参考由官方 `zephyr/drivers/crc.h` 的文档生成。

[上一章：CAN持续发送示例](P045_CAN持续发送示例.md) · [下一章：CRC驱动后端接口](P047_CRC驱动后端接口.md) · [返回大纲](大纲.md)
