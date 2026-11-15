---
id: learning.zephyr-docs.firmware_update.fwapi-hawkbit__event
title: hawkBit事件接口
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第30章\_hawkBit事件接口

原文：[group__hawkbit__event](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html)。读取日期：2026-10-13，`latest`。

## 30.1\_事件与回调

hawkBit **事件（Event）**API用于注册应用的 **回调（Callback）**，在升级流程的特定阶段通知应用。API为 **应用程序编程接口（Application Programming Interface）**，头文件是 [`zephyr/mgmt/hawkbit/event.h`](https://docs.zephyrproject.org/latest/doxygen/html/event_8h.html)。

结构体 `hawkbit_event_callback` 保存回调对象，函数指针类型 [`hawkbit_event_callback_handler_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga49064aef93c5383f24ea41819b78c458) 定义处理函数签名，枚举 [`hawkbit_event_type`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga794d232d73d105bd170b222ab17ce2af) 选择触发事件。三者分别是状态对象、调用入口类型和事件类别，不是同一个符号。

## 30.2\_创建回调对象的宏

宏 [`HAWKBIT_EVENT_CREATE_CALLBACK`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga05eec89437dfd13a022ba2eac6b1e0d9) 创建并初始化回调对象，可代替初始化函数 [`hawkbit_event_init_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga0ec141ff3e11c0e1d0e3f8757ace5010)：

```c
#define HAWKBIT_EVENT_CREATE_CALLBACK(_callback, _handler, _event)
```

上面为原参考的参数签名，下列是原宏体：

```c
struct hawkbit_event_callback _callback = {                                                \
        .handler = _handler,                                                               \
        .event = _event,                                                                   \
}
```

`_callback` 为回调结构的变量名，`_handler` 为有效的处理函数指针，`_event` 为触发回调的 [`hawkbit_event_type`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga794d232d73d105bd170b222ab17ce2af) 枚举值。**译注：**签名和宏体分列是文档的展示方式，不能把空的签名行当作完整可用宏定义复制。

## 30.3\_处理函数签名与私有数据

```c
typedef void (*hawkbit_event_callback_handler_t)(
    struct hawkbit_event_callback *cb, enum hawkbit_event_type event);
```

参数 `cb` 指向拥有此处理函数的原回调对象，`event` 为本次触发事件。若回调对象嵌入应用的私有结构，可通过 **容器反查宏（Container-of Macro）** [`CONTAINER_OF()`](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f) 从 `cb` 找到外层结构，再访问私有数据。

## 30.4\_全部事件类别

枚举 [`hawkbit_event_type`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga794d232d73d105bd170b222ab17ce2af) 的下列项目用于注册事件回调。保留名称不变，中文列解释触发时机。

| 枚举项 | 触发条件 |
| --- | --- |
| [`HAWKBIT_EVENT_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa4ab9fcb6bebf167eff6fb2311da735dd) | 发生错误。 |
| [`HAWKBIT_EVENT_ERROR_NETWORKING`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afad8ed1ca4798bcd479f11d613a20e2214) | 发生网络错误。 |
| [`HAWKBIT_EVENT_ERROR_PERMISSION`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa435e07a36fec3d4a1d94926d8caa9d7a) | 发生权限错误。 |
| [`HAWKBIT_EVENT_ERROR_METADATA`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afafc267582eeed1249830e888e0f8a6bd8) | 发生元数据错误。 |
| [`HAWKBIT_EVENT_ERROR_DOWNLOAD`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa70e2d5b23859484b758c446d0e7c624c) | 发生下载错误。 |
| [`HAWKBIT_EVENT_ERROR_ALLOC`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa0a6f33bbaeff8c0e3b1c6aba0cdf0639) | 发生内存分配错误。 |
| [`HAWKBIT_EVENT_UPDATE_DOWNLOADED`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa645bec5a542a24f3696241921f89d3a4) | 新更新已下载。 |
| [`HAWKBIT_EVENT_NO_UPDATE`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa516265be2515ca5f1b95517b04d0522e) | 没有可用更新。 |
| [`HAWKBIT_EVENT_CANCEL_UPDATE`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afae7cbf7ba78059186080e633965244e8b) | 服务器取消了更新。 |
| [`HAWKBIT_EVENT_START_DOWNLOAD`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afaaa1680961ce8487c98dc4299003b0b55) | 下载开始前。 |
| [`HAWKBIT_EVENT_END_DOWNLOAD`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa9f01289c7aa75e335e1fb8b05e5ec984) | 下载结束后。 |
| [`HAWKBIT_EVENT_START_RUN`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afab6e6a48faa3ed32b8fef2b4cce4c29d3) | 一次hawkBit运行开始前。 |
| [`HAWKBIT_EVENT_END_RUN`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa0b5b571646812e7b31953899d512b4e2) | 一次hawkBit运行结束后。 |
| [`HAWKBIT_EVENT_BEFORE_REBOOT`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa27254d0c181c7736de5fa9c281fc92cf) | hawkBit执行重启前。 |
| [`HAWKBIT_EVENT_CONFIRMED_CURRENT_IMAGE`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa55dd61e8016fe6b69339e136d5ff279e) | 初始化期间确认当前镜像并擦除旧镜像时。 |

## 30.5\_初始化与注册

函数 [`hawkbit_event_init_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga0ec141ff3e11c0e1d0e3f8757ace5010) 初始化已存在的回调结构：

```c
static inline void hawkbit_event_init_callback(
    struct hawkbit_event_callback *callback,
    hawkbit_event_callback_handler_t handler,
    enum hawkbit_event_type event);
```

`callback` 为有效应用回调结构指针，`handler` 为有效处理函数指针，`event` 为要触发的事件类别。函数无返回值。

函数 [`hawkbit_event_add_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga646c72464b0761009f42393fa313c880) 添加应用回调：

```c
int hawkbit_event_add_callback(struct hawkbit_event_callback *cb);
```

`cb` 必须指向有效应用回调结构；成功返回0，失败返回负 `errno` 错误值。

## 30.6\_移除回调

函数 [`hawkbit_event_remove_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gaa19bb74cb46e9aff7742907a86c96359) 移除应用回调：

```c
int hawkbit_event_remove_callback(struct hawkbit_event_callback *cb);
```

参数 `cb` 是有效应用回调结构指针；成功返回0，失败返回负 `errno`。**译注：**创建或初始化对象与加入回调列表是两个步骤；注册期间对象必须持续有效，不能注册局部对象后让其生命周期结束。

[上一章：hawkBit配置接口](P029_hawkBit配置接口.md) · [下一章：UpdateHub接口](P031_UpdateHub接口.md) · [返回大纲](大纲.md)
