---
id: learning.zephyr-docs.hardware.pwmbackend-1
title: PWM驱动函数表
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpwm__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第259章\_PWM驱动函数表

原文：[structpwm__driver__api](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__driver__api.html)。读取日期：2026-10-13，`latest`。

## 259.1\_用途与成员要求

结构 [`pwm_driver_api`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__driver__api.html) 是所有 **脉宽调制（Pulse Width Modulation，PWM）**驱动需要定义的 **驱动操作（Driver Operations）**表，包含实现操作的函数指针及驱动专用的其他常量数据，定义来自 `zephyr/drivers/pwm.h`。

标为 **必需（Required，REQ）**的成员必须设置；标为 **可选（Optional，OPT）**的成员按需提供。

## 259.2\_数据字段（Data Fields）

回调完整声明见[PWM驱动后端接口](P258_PWM驱动后端接口.md)。

| 字段 | 类型 | 要求 | 含义 |
| --- | --- | --- | --- |
| <a id="a5d4e7cb7f3610fcc7a9981baf4ec3654"></a>[`set_cycles`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__driver__api.html#a5d4e7cb7f3610fcc7a9981baf4ec3654) | [`pwm_set_cycles_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html#ga284f0aa783ab2f457b2239a87a9c1671) | REQ | 配置引脚周期（Period）与脉宽（Pulse Width）。 |
| <a id="a365761817898baf5ea52eb1ad63d67a6"></a>[`get_cycles_per_sec`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__driver__api.html#a365761817898baf5ea52eb1ad63d67a6) | [`pwm_get_cycles_per_sec_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html#ga6330ac4e97604ab4510c16a3c4d0437f) | REQ | 取得每秒时钟周期数，即时钟频率（Clock Rate）。 |
| <a id="a4d4b8080814e092e2bc5ac0a47baa182"></a>[`configure_capture`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__driver__api.html#a4d4b8080814e092e2bc5ac0a47baa182) | [`pwm_configure_capture_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html#ga8dedee6071801685cb618bacd8b51c57) | OPT | 配置单个输入的周期/脉宽捕获（Capture）。 |
| <a id="afedf4abee4341fde838eedb962d34368"></a>[`enable_capture`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__driver__api.html#afedf4abee4341fde838eedb962d34368) | [`pwm_enable_capture_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html#gaae83bb7862c019492c8bc154015f8e8c) | OPT | 启用单个输入的周期/脉宽捕获。 |
| <a id="a6b210f5e68353aef9594c2c585360e47"></a>[`disable_capture`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__driver__api.html#a6b210f5e68353aef9594c2c585360e47) | [`pwm_disable_capture_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html#ga471b1f0ed9992e372f1f01683b68f456) | OPT | 禁用单个输入的周期/脉宽捕获。 |
| <a id="aa97c7710a29e69af934e3b0f259c11b8"></a>[`manage_event_callback`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__driver__api.html#aa97c7710a29e69af934e3b0f259c11b8) | [`pwm_manage_event_callback_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface__backend.html#ga70ab8cd3c6d7b43890655405b3e6db3f) | OPT | 添加应用事件回调；对应回调类型也用于移除。 |

三个捕获成员 `configure_capture`、`enable_capture`、`disable_capture` 仅在启用配置系统 Kconfig 的 [`CONFIG_PWM_CAPTURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_CAPTURE) 时可用；`manage_event_callback` 仅在启用 [`CONFIG_PWM_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_EVENT) 时可用。

## 259.3\_相关定义宏

原文关联的设备与接口定义宏为 [`DEVICE_DT_INST_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)、[`DEVICE_DT_DEFINE()`](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)、[`DEVICE_API()`](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)。

---

[上一章：PWM驱动后端接口](P258_PWM驱动后端接口.md) · [下一章：PWM模拟控制器](P260_PWM模拟控制器.md) · [返回大纲](大纲.md)
