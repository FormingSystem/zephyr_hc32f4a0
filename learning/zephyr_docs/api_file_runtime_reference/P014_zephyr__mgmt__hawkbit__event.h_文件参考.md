---
id: learning.zephyr-docs.api-file-runtime-reference.page-14
title: zephyr__mgmt__hawkbit__event.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/event_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_mgmt\_\_hawkbit\_\_event.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/event_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

hawkBit事件（Event）的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

hawkBit事件（Event）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.1\_宏定义（Macros）

<a id="r_ga05eec89437dfd13a022ba2eac6b1e0d9"></a>

```c
#define HAWKBIT_EVENT_CREATE_CALLBACK(_callback, _handler, _event)
```

相关声明：[HAWKBIT_EVENT_CREATE_CALLBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga05eec89437dfd13a022ba2eac6b1e0d9)。

用于正确创建并初始化 `struct hawkbit_event_callback` 的宏（Macro）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 14.2\_类型定义（Typedefs）

<a id="r_ga49064aef93c5383f24ea41819b78c458"></a>

```c
typedef void(* hawkbit_event_callback_handler_t) (struct hawkbit_event_callback *cb, enum hawkbit_event_type event)
```

相关声明：[hawkbit_event_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga49064aef93c5383f24ea41819b78c458)、[hawkbit_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga794d232d73d105bd170b222ab17ce2af)。

定义应用程序回调处理函数的签名（Function Signature）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.3\_枚举（Enumerations）

<a id="r_ga794d232d73d105bd170b222ab17ce2af"></a>

```c
enum hawkbit_event_type { HAWKBIT_EVENT_ERROR , HAWKBIT_EVENT_ERROR_NETWORKING , HAWKBIT_EVENT_ERROR_PERMISSION , HAWKBIT_EVENT_ERROR_METADATA , HAWKBIT_EVENT_ERROR_DOWNLOAD , HAWKBIT_EVENT_ERROR_ALLOC , HAWKBIT_EVENT_UPDATE_DOWNLOADED , HAWKBIT_EVENT_NO_UPDATE , HAWKBIT_EVENT_CANCEL_UPDATE , HAWKBIT_EVENT_START_DOWNLOAD , HAWKBIT_EVENT_END_DOWNLOAD , HAWKBIT_EVENT_START_RUN , HAWKBIT_EVENT_END_RUN , HAWKBIT_EVENT_BEFORE_REBOOT , HAWKBIT_EVENT_CONFIRMED_CURRENT_IMAGE }
```

相关声明：[hawkbit_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga794d232d73d105bd170b222ab17ce2af)、[HAWKBIT_EVENT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa4ab9fcb6bebf167eff6fb2311da735dd)、[HAWKBIT_EVENT_ERROR_NETWORKING](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afad8ed1ca4798bcd479f11d613a20e2214)、[HAWKBIT_EVENT_ERROR_PERMISSION](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa435e07a36fec3d4a1d94926d8caa9d7a)、[HAWKBIT_EVENT_ERROR_METADATA](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afafc267582eeed1249830e888e0f8a6bd8)、[HAWKBIT_EVENT_ERROR_DOWNLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa70e2d5b23859484b758c446d0e7c624c)、[HAWKBIT_EVENT_ERROR_ALLOC](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa0a6f33bbaeff8c0e3b1c6aba0cdf0639)、[HAWKBIT_EVENT_UPDATE_DOWNLOADED](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa645bec5a542a24f3696241921f89d3a4)、[HAWKBIT_EVENT_NO_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa516265be2515ca5f1b95517b04d0522e)、[HAWKBIT_EVENT_CANCEL_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afae7cbf7ba78059186080e633965244e8b)、[HAWKBIT_EVENT_START_DOWNLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afaaa1680961ce8487c98dc4299003b0b55)、[HAWKBIT_EVENT_END_DOWNLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa9f01289c7aa75e335e1fb8b05e5ec984)、[HAWKBIT_EVENT_START_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afab6e6a48faa3ed32b8fef2b4cce4c29d3)、[HAWKBIT_EVENT_END_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa0b5b571646812e7b31953899d512b4e2)、[HAWKBIT_EVENT_BEFORE_REBOOT](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa27254d0c181c7736de5fa9c281fc92cf)、[HAWKBIT_EVENT_CONFIRMED_CURRENT_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa55dd61e8016fe6b69339e136d5ff279e)。

hawkBit 事件类型（Event Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.4\_函数（Functions）

<a id="r_ga0ec141ff3e11c0e1d0e3f8757ace5010"></a>

```c
static void hawkbit_event_init_callback (struct hawkbit_event_callback *callback, hawkbit_event_callback_handler_t handler, enum hawkbit_event_type event)
```

相关声明：[hawkbit_event_init_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga0ec141ff3e11c0e1d0e3f8757ace5010)、[hawkbit_event_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga49064aef93c5383f24ea41819b78c458)、[hawkbit_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga794d232d73d105bd170b222ab17ce2af)。

用于正确初始化 `struct hawkbit_event_callback` 的辅助函数（Helper）。

<a id="r_ga646c72464b0761009f42393fa313c880"></a>

```c
int hawkbit_event_add_callback (struct hawkbit_event_callback *cb)
```

相关声明：[hawkbit_event_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga646c72464b0761009f42393fa313c880)。

添加应用回调。

<a id="r_gaa19bb74cb46e9aff7742907a86c96359"></a>

```c
int hawkbit_event_remove_callback (struct hawkbit_event_callback *cb)
```

相关声明：[hawkbit_event_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gaa19bb74cb46e9aff7742907a86c96359)。

移除应用回调。


## 14.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P249_event.h_源码浏览.md)
- [HAWKBIT_EVENT_CREATE_CALLBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga05eec89437dfd13a022ba2eac6b1e0d9)
- [hawkbit_event_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga49064aef93c5383f24ea41819b78c458)
- [hawkbit_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga794d232d73d105bd170b222ab17ce2af)
- [HAWKBIT_EVENT_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa4ab9fcb6bebf167eff6fb2311da735dd)
- [HAWKBIT_EVENT_ERROR_NETWORKING](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afad8ed1ca4798bcd479f11d613a20e2214)
- [HAWKBIT_EVENT_ERROR_PERMISSION](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa435e07a36fec3d4a1d94926d8caa9d7a)
- [HAWKBIT_EVENT_ERROR_METADATA](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afafc267582eeed1249830e888e0f8a6bd8)
- [HAWKBIT_EVENT_ERROR_DOWNLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa70e2d5b23859484b758c446d0e7c624c)
- [HAWKBIT_EVENT_ERROR_ALLOC](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa0a6f33bbaeff8c0e3b1c6aba0cdf0639)
- [HAWKBIT_EVENT_UPDATE_DOWNLOADED](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa645bec5a542a24f3696241921f89d3a4)
- [HAWKBIT_EVENT_NO_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa516265be2515ca5f1b95517b04d0522e)
- [HAWKBIT_EVENT_CANCEL_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afae7cbf7ba78059186080e633965244e8b)
- [HAWKBIT_EVENT_START_DOWNLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afaaa1680961ce8487c98dc4299003b0b55)
- [HAWKBIT_EVENT_END_DOWNLOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa9f01289c7aa75e335e1fb8b05e5ec984)
- [HAWKBIT_EVENT_START_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afab6e6a48faa3ed32b8fef2b4cce4c29d3)
- [HAWKBIT_EVENT_END_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa0b5b571646812e7b31953899d512b4e2)
- [HAWKBIT_EVENT_BEFORE_REBOOT](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa27254d0c181c7736de5fa9c281fc92cf)
- [HAWKBIT_EVENT_CONFIRMED_CURRENT_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gga794d232d73d105bd170b222ab17ce2afa55dd61e8016fe6b69339e136d5ff279e)
- [hawkbit_event_init_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga0ec141ff3e11c0e1d0e3f8757ace5010)
- [hawkbit_event_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#ga646c72464b0761009f42393fa313c880)
- [hawkbit_event_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__event.html#gaa19bb74cb46e9aff7742907a86c96359)

<a id="header-details"></a>

---

[上一章](P013_zephyr__net__dsa_core.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__authentication__fido2__fido2_up.h_文件参考.md)
