---
id: learning.zephyr-docs.hardware.canback-3
title: CAN驱动公共数据
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第372章\_CAN驱动公共数据

原文：[structcan__driver__data](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__data.html)。读取日期：2026-10-13，`latest`。

## 372.1\_运行时数据的首成员

[`can_driver_data`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__data.html) 是所有控制器局域网（Controller Area Network，CAN）控制器驱动共用的数据结构，声明来自 `zephyr/drivers/can.h`。它应当是驱动 `struct driver_data` 声明中的第一个成员。

本结构保存当前模式、启动状态，以及状态变化回调（Callback）的管理信息。旧式（Legacy）单回调接口使用独立的兼容字段；回调列表通过自旋锁（Spinlock）保护修改。

## 372.2\_字段定义

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="a1f01de3a78be9193263a47acf4181b93"></a>[`mode`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__data.html#a1f01de3a78be9193263a47acf4181b93) | [`can_mode_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga0b2a1456e66f4522a30cf1400fdfced7) | 当前控制器模式 |
| <a id="a5b3983ca54213c84f8278ec36f0fb0ce"></a>[`started`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__data.html#a5b3983ca54213c84f8278ec36f0fb0ce) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 已启动为 `true`，否则为 `false` |
| <a id="a281054c5102f22c362691b81efbb8162"></a>[`legacy_state_change_cb`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__data.html#a281054c5102f22c362691b81efbb8162) | `struct can_state_change_callback` | 旧式状态变化回调 |
| <a id="af6a94bfe3b21502dc70548b470f732b4"></a>[`legacy_state_change_cb_handler`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__data.html#af6a94bfe3b21502dc70548b470f732b4) | [`can_state_change_callback_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__controller.html#ga002ff7ba1f5be374510a902459dd9d3d) | 旧式回调函数指针，或 `NULL` |
| <a id="a646e5422136017bed629e5a0f80d4824"></a>[`legacy_state_change_cb_user_data`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__data.html#a646e5422136017bed629e5a0f80d4824) | `void *` | 旧式回调用户数据指针，或 `NULL` |
| <a id="a5b8a964383a759a0144a1b72bb8835cc"></a>[`state_change_callback_lock`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__data.html#a5b8a964383a759a0144a1b72bb8835cc) | `struct k_spinlock` | 修改状态变化回调列表时使用的锁 |
| <a id="afce7bbd484eea2660fe71f0322103265"></a>[`state_change_callbacks`](https://docs.zephyrproject.org/latest/doxygen/html/structcan__driver__data.html#afce7bbd484eea2660fe71f0322103265) | [`sys_slist_t`](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8) | 状态变化回调单向链表（Singly Linked List） |

---

[上一章：CAN驱动公共配置](P371_CAN驱动公共配置.md) · [下一章：CAN设备树宏](P373_CAN设备树宏.md) · [返回大纲](大纲.md)
