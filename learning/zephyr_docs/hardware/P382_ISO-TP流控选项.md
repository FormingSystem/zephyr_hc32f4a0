---
id: learning.zephyr-docs.hardware.isotpstruct-1
title: ISO-TP流控选项
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structisotp__fc__opts.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第382章\_ISO-TP流控选项

原文：[structisotp__fc__opts](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__fc__opts.html)。读取日期：2026-10-13，`latest`。

## 382.1\_用途与声明

`struct isotp_fc_opts` 是 ISO-TP 传输协议（Transport Protocol）的帧流控选项结构，用于向绑定及发送函数传递选项。包含头文件 `zephyr/canbus/isotp.h`。

```c
struct isotp_fc_opts {
    uint8_t bs;
    uint8_t stmin;
};
```

## 382.2\_字段

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`bs`](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__fc__opts.html#a8f31bf5c95069352043da33541911b3c) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 块大小（Block Size，BS）。原字段说明为“发送下一个 CF 之前的 CF PDU 数量”。 |
| [`stmin`](https://docs.zephyrproject.org/latest/doxygen/html/structisotp__fc__opts.html#a5db0ceeed259c26d1d8fe0a901edcbca) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 最小间隔（Minimum Separation Time，STmin），即帧之间的最短时间。 |

> 译注：CF 是连续帧（Consecutive Frame），PDU 是协议数据单元（Protocol Data Unit）。原 `bs` 字段说明中的“下一个 CF”与[官方协议概述的块大小定义](P379_CAN_ISO-TP协议.md)不一致；协议概述明确，BS 表示等待下一流控帧（Flow Control Frame，FC）之前允许发送的连续帧数量。本页保留原字段说明并指出差异，避免把它误读为每个连续帧前都进行流控。原字段页没有给出 `stmin` 的数值编码规则，不应仅凭这个 [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) 类型把所有值解释为毫秒数。

---

[上一章：ISO-TP消息标识](P381_ISO-TP消息标识.md) · [下一章：I3C地址槽管理](P383_I3C地址槽管理.md) · [返回大纲](大纲.md)
