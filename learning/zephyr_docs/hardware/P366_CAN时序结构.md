---
id: learning.zephyr-docs.hardware.canstruct-3
title: CAN时序结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcan__timing.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第366章\_CAN时序结构

原文：[structcan__timing](https://docs.zephyrproject.org/latest/doxygen/html/structcan__timing.html)。读取日期：2026-10-13，`latest`。

## 366.1\_位时间如何组成

[`can_timing`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__timing.html) 是控制器局域网（Controller Area Network，CAN）总线时序结构，声明来自 `zephyr/drivers/can.h`，用于向配置和比特率计算函数传递总线时序值。

传播段（Propagation Segment）表示信号传播时间，相位段 1 和相位段 2（Phase Segment 1/2）定义采样点（Sampling Point）。[`prop_seg`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__timing.html#ac009d40fee9788b663963978498b2ee9) 与 [`phase_seg1`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__timing.html#a9941688e79fa4ce01c4b498433319089) 对采样点的影响相同，因此有些控制器仅为二者之和提供寄存器。同步段（Synchronization Segment，图中 `sync_seg`）始终为一个时间量子（Time Quantum，tq）。

原文时序图以字符绘制，完整保留如下：

```text
+---------+----------+------------+------------+
|sync_seg | prop_seg | phase_seg1 | phase_seg2 |
+---------+----------+------------+------------+
                                  ^
                            Sampling-Point
```

## 366.2\_时间量子与比特率

一个 tq 的时长为 `1 / (core_clock / prescaler)`，其中 `core_clock` 为核心时钟频率，[`prescaler`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__timing.html#a74fb8341cbb6d97721c9d0afbc7e1f3a) 为预分频值。比特率（Bitrate）等于预分频后的时钟再除以各段长度之和，原公式为：

```text
br = (core_clock / prescaler) / (1 + prop_seg + phase_seg1 + phase_seg2)
```

同步跳转宽度（Synchronization Jump Width，SJW）规定采样点最多可以移动多少个时间量子；需要重新同步（Resynchronization）时，采样点会发生移动。

## 366.3\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a5af76a4ee9c741642ec19265a47fceb5"></a>[`sjw`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__timing.html#a5af76a4ee9c741642ec19265a47fceb5) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 同步跳转宽度 |
| <a id="ac009d40fee9788b663963978498b2ee9"></a>[`prop_seg`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__timing.html#ac009d40fee9788b663963978498b2ee9) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 传播段 |
| <a id="a9941688e79fa4ce01c4b498433319089"></a>[`phase_seg1`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__timing.html#a9941688e79fa4ce01c4b498433319089) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 相位段 1 |
| <a id="a6ca0caf618d28a761c3c8859ed3a68d6"></a>[`phase_seg2`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__timing.html#a6ca0caf618d28a761c3c8859ed3a68d6) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 相位段 2 |
| <a id="a74fb8341cbb6d97721c9d0afbc7e1f3a"></a>`prescaler` | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 预分频值 |

---

[上一章：CAN错误计数结构](P365_CAN错误计数结构.md) · [下一章：CAN状态变化回调结构](P367_CAN状态变化回调结构.md) · [返回大纲](大纲.md)
