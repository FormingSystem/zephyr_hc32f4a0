---
id: learning.zephyr-docs.hardware.pwmapi-2
title: PWM事件回调结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpwm__event__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第257章\_PWM事件回调结构

原文：[structpwm__event__callback](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__event__callback.html)。读取日期：2026-10-13，`latest`。

## 257.1\_用途与生命周期

结构 [`pwm_event_callback`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__event__callback.html) 是 **脉宽调制（Pulse Width Modulation，PWM）**的 **事件回调（Event Callback）**结构，定义来自 `zephyr/drivers/pwm.h`，用于向驱动实例的回调列表注册回调。

可以按需添加多个回调，但每一个都必须使用不同的 `struct pwm_event_callback` 指针。**不要在栈（Stack）上分配这个结构。**可用辅助函数 [`pwm_init_event_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gaf87ef431d50a482910e77e49d52a2e13) 初始化，接口见[PWM公共接口](P255_PWM公共接口.md)。

## 257.2\_数据字段（Data Fields）

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a56f5f3b2589dffb88a8d893fe7d259ab"></a>[`handler`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__event__callback.html#a56f5f3b2589dffb88a8d893fe7d259ab) | [`pwm_event_callback_handler_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gaedacc300332a9c01da48671f92bf0097) | 相关事件发生时实际调用的处理函数。 |
| <a id="a0f14cc1f7e4735e88f28ff4cfecbcec5"></a>[`channel`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__event__callback.html#a0f14cc1f7e4735e88f28ff4cfecbcec5) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 回调关注的通道。 |
| <a id="a304e9ea24d4eb8f5d618aea8c3600223"></a>[`event_mask`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__event__callback.html#a304e9ea24d4eb8f5d618aea8c3600223) | [`pwm_events_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga5bc9607de7643cb78476ed354c51560b) | 回调关注的事件掩码（Event Mask）。 |

---

[上一章：PWM设备树描述](P256_PWM设备树描述.md) · [下一章：PWM驱动后端接口](P258_PWM驱动后端接口.md) · [返回大纲](大纲.md)
