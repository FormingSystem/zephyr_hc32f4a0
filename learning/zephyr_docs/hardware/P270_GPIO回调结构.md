---
id: learning.zephyr-docs.hardware.gpiostruct-3
title: GPIO回调结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgpio__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第270章\_GPIO回调结构

原文：[structgpio__callback](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__callback.html)。读取日期：2026-10-13，`latest`。

## 270.1\_注册与生命周期

结构 [`gpio_callback`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__callback.html) 是 **通用输入/输出（General Purpose Input/Output，GPIO）**回调（Callback）结构，声明来自 `zephyr/drivers/gpio.h`。它用于向驱动实例的回调链表注册回调。

可以按需添加任意数量的回调，但每个回调必须对应独立的 [`gpio_callback`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__callback.html) 结构指针。**不要在栈上分配这个结构。**辅助函数 [`gpio_init_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7a7dd7c1f3a2135a9f378e1c34b6232c) 用于正确初始化它，参见[GPIO公共接口](P266_GPIO公共接口.md)。

## 270.2\_字段

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="ab60e7093072964bd818d536c746211e4"></a>[`node`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__callback.html#ab60e7093072964bd818d536c746211e4) | [`sys_snode_t`](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493) | 驱动内部使用的单向链表节点（Singly Linked List Node）；用户不应修改，参见 `drivers/gpio/gpio_utils.h` |
| <a id="af89dc41cbd610d81ac03cae7ab764ceb"></a>[`handler`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__callback.html#af89dc41cbd610d81ac03cae7ab764ceb) | [`gpio_callback_handler_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaf0aa40279d32b1b8332f2f23a39510af) | 对应事件发生时实际调用的回调处理函数 |
| <a id="ace5c2b83f1d51f73877a1f2c54ba8c67"></a>[`pin_mask`](https://docs.zephyrproject.org/latest/doxygen/html/structgpio__callback.html#ace5c2b83f1d51f73877a1f2c54ba8c67) | [`gpio_port_pins_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7f40ed51f14fd8000e9b52ab347b273f) | 此回调关注的引脚位掩码（Bitmask）；为0时回调永远不会被调用 |

所有者可根据需要修改 `pin_mask`，这会影响处理函数是否被调用。掩码中选中的引脚必须配置为能触发中断（Interrupt）。

---

[上一章：GPIO公共驱动数据](P269_GPIO公共驱动数据.md) · [下一章：GPIO驱动后端](P271_GPIO驱动后端.md) · [返回大纲](大纲.md)
