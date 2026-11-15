---
id: learning.zephyr-docs.api-file-configuration-reference.page-35
title: zephyr__mgmt__mcumgr__mgmt__handlers.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/handlers_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_zephyr\_\_mgmt\_\_mcumgr\_\_mgmt\_\_handlers.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/handlers_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr命令处理程序注册（Command Handler Registration）API的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

MCUmgr命令处理程序注册（Command Handler Registration）API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 35.1\_宏定义（Macros）

<a id="r_ga59833a6c16520816e4488210308b7c7b"></a>

```c
#define MCUMGR_HANDLER_DEFINE(name, _init)
```

相关声明：[MCUMGR_HANDLER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__handler__api.html#ga59833a6c16520816e4488210308b7c7b)。

定义待注册的 MCUmgr 处理器（Handler）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 35.2\_类型定义（Typedefs）

<a id="r_gaceb63293a54178de29ce0cdf6a03083a"></a>

```c
typedef void(* mcumgr_handler_init_t) (void)
```

相关声明：[mcumgr_handler_init_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__handler__api.html#gaceb63293a54178de29ce0cdf6a03083a)。

MCUmgr 处理器初始化函数（Handler Initialisation Function）的类型定义（Type Definition）。


## 35.3\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P084_handlers.h_源码浏览.md)
- [MCUMGR_HANDLER_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__handler__api.html#ga59833a6c16520816e4488210308b7c7b)
- [mcumgr_handler_init_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__handler__api.html#gaceb63293a54178de29ce0cdf6a03083a)

<a id="header-details"></a>

---

[上一章](P034_zephyr__drivers__gpio__gpio_sx1509b.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P036_zephyr__bluetooth__hci_raw.h_文件参考.md)
