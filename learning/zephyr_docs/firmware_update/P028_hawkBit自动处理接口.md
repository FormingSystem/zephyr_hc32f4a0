---
id: learning.zephyr-docs.firmware_update.fwapi-hawkbit__autohandler
title: hawkBit自动处理接口
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第28章\_hawkBit自动处理接口

原文：[group__hawkbit__autohandler](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html)。读取日期：2026-10-13，`latest`。

## 28.1\_自动处理接口

hawkBit **自动处理器（Autohandler）**按预定时间间隔处理更新查询与升级全过程。本章的 **应用程序编程接口（Application Programming Interface，API）**位于头文件 [`zephyr/mgmt/hawkbit/autohandler.h`](https://docs.zephyrproject.org/latest/doxygen/html/autohandler_8h.html)，返回的hawkBit状态详见[主接口](P027_hawkBit接口.md)。

## 28.2\_运行与重新调度

函数 [`hawkbit_autohandler()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#ga41865255aa3020a34816c23ae7977f20) 自动执行查询和更新：

```c
void hawkbit_autohandler(bool auto_reschedule);
```

参数 `auto_reschedule=true` 表示处理器会重新调度自己，继续按预定间隔运行。

## 28.3\_等待结果

函数 [`hawkbit_autohandler_wait()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#ga6d13b3d7b9a61d06a6eaa346189a08c6) 等待自动处理器完成或出现所需结果：

```c
enum hawkbit_response hawkbit_autohandler_wait(uint32_t events, k_timeout_t timeout);
```

`events` 为希望等待的事件集合。常量 [`UINT32_MAX`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ab5eb23180f7cc12b7d6c04a8ec067fdd) 选择等待自动处理器完成一次运行；也可用 **位掩码（Bitmask）**构造宏 [`BIT()`](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c) 配合 [`hawkbit_response`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga96c59c754178451d8dbd08b32813220b) 的某个值，选择具体结果位。

`timeout` 为等待时间，类型 [`k_timeout_t`](../timer_reference/P087_内核超时类型.md) 表达内核超时；常量 [`K_NO_WAIT`](../timer_reference/P086_系统时钟公共接口.md) 表示不等待，[`K_FOREVER`](../timer_reference/P086_系统时钟公共接口.md) 表示一直等待。函数返回一个 [`hawkbit_response`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga96c59c754178451d8dbd08b32813220b) 枚举值。

> 译注：这里的位位置来自响应枚举，不能替换成[事件API](P030_hawkBit事件接口.md)的 `hawkbit_event_type`，也不是直接把响应枚举整数作为掩码。原参考没有承诺这个等待调用会新发起一次查询；开始自动处理与等待结果是两个动作。

## 28.4\_取消自动处理

函数 [`hawkbit_autohandler_cancel()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#gabc27308bb974d6e0b9650476243e5e9a) 取消自动处理器的运行安排：

```c
int hawkbit_autohandler_cancel(void);
```

返回内核 **可延迟工作（Delayable Work）**取消函数 [`k_work_cancel_delayable()`](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#ga92355914ee178d4c3e848a1946bed3e4) 的结果。

> 译注：这是工作调度层的取消接口，不应当作能够中途强制终止任意正在进行的网络或闪存操作的保证；具体边界遵循底层工作队列接口。

## 28.5\_调整下一次延迟

函数 [`hawkbit_autohandler_set_delay()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#ga47fe3e9cd227fd4da332e9eeff81f991) 设置下一次执行的延迟：

```c
int hawkbit_autohandler_set_delay(k_timeout_t timeout, bool if_bigger);
```

`timeout` 是新延迟。`if_bigger=true` 时，仅当新延迟大于当前延迟才应用；否则按新值安排。此调整只影响下一次运行，处理器运行后不会继续保留该延迟。

原文返回规则：若 `if_bigger` 为真且当前延迟大于新延迟，返回0；其他情况返回重新调度函数 [`k_work_reschedule()`](https://docs.zephyrproject.org/latest/doxygen/html/group__workqueue__apis.html#gaacaab408fb7c848d466ad1f069dfa648) 的结果。**译注：**本地实现严格比较“大于”，两者相等时也不重新调度并返回0。

[上一章：hawkBit接口](P027_hawkBit接口.md) · [下一章：hawkBit配置接口](P029_hawkBit配置接口.md) · [返回大纲](大纲.md)
