---
id: learning.zephyr-docs.api-extension-topic-reference.page-15
title: 处理程序（Handlers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__handler__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_处理程序（Handlers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__handler__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 处理程序注册 API。

<a id="details"></a>

MCUmgr 处理程序注册 API。

<a id="header-files"></a>
<a id="files"></a>

## 15.1\_文件（Files）

<a id="r_handlers_2Eh"></a>

```c
file handlers.h
```

相关声明：[handlers.h](../api_file_configuration_reference/P035_zephyr__mgmt__mcumgr__mgmt__handlers.h_文件参考.md)。

MCUmgr命令处理程序注册（Command Handler Registration）API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_ga59833a6c16520816e4488210308b7c7b"></a>

```c
#define MCUMGR_HANDLER_DEFINE(name, _init)
```

相关声明：[MCUMGR_HANDLER_DEFINE](#ga59833a6c16520816e4488210308b7c7b)。

定义待注册的 MCUmgr 处理器（Handler）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.3\_类型定义（Typedefs）

<a id="r_gaceb63293a54178de29ce0cdf6a03083a"></a>

```c
typedef void(* mcumgr_handler_init_t) (void)
```

相关声明：[mcumgr_handler_init_t](#gaceb63293a54178de29ce0cdf6a03083a)。

MCUmgr 处理器初始化函数（Handler Initialisation Function）的类型定义（Type Definition）。

## 15.4\_详细说明（Detailed Documentation）

<a id="ga59833a6c16520816e4488210308b7c7b"></a>

### `MCUMGR_HANDLER_DEFINE`

```c
#define MCUMGR_HANDLER_DEFINE ( name, _init )
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/handlers.h>
```

展开值（Value）：

```c
const STRUCT_SECTION_ITERABLE(mcumgr_handler, name) = { \
        .init = _init,                                  \
}
```

定义待注册的 MCUmgr 处理器（Handler）。

向 MCUmgr 处理器（Handlers）的可迭代区段链接器列表（Iterable Section Linker List）添加新条目（Entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 待注册的 MCUmgr 处理器名称（Handler Name）。 |
| `_init` | 要调用的初始化函数（Init Function），类型为 `mcumgr_handler_init_t`。 |

<a id="gaceb63293a54178de29ce0cdf6a03083a"></a>

### `mcumgr_handler_init_t`

```c
typedef void(* mcumgr_handler_init_t) (void)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/handlers.h>
```

MCUmgr 处理器初始化函数（Handler Initialisation Function）的类型定义（Type Definition）。


## 15.5\_原页交叉引用（Cross References）

- [handlers.h](../api_file_configuration_reference/P035_zephyr__mgmt__mcumgr__mgmt__handlers.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P014_枚举管理回调（Enumeration Management Callbacks）.md) · [返回大纲](大纲.md) · [下一章](P016_操作系统管理客户端（OS Management Client）.md)
