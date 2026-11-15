---
id: learning.zephyr-docs.api-protocol-topic-reference.page-33
title: 蜂窝调制解调器辅助功能（Cellular modem helpers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cellular__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_蜂窝调制解调器辅助功能（Cellular modem helpers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cellular__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

使用通用的 AT 交互（Chat）、连接多路复用（CMUX）、点对点协议（PPP）和电源管理支持，实现供应商特定的蜂窝调制解调器驱动。

<a id="details"></a>

使用通用的 AT 交互（Chat）、连接多路复用（CMUX）、点对点协议（PPP）和电源管理支持，实现供应商特定的蜂窝调制解调器驱动。

<a id="header-groups"></a>
<a id="groups"></a>

## 33.1\_主题（Topics）

<a id="r_modem_5Fdriver_5Fmacros"></a>

相关声明：[蜂窝调制解调器驱动定义宏（Driver definition macros）](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html)。

定义使用蜂窝调制解调器驱动的设备实例。

<a id="header-files"></a>
<a id="files"></a>

## 33.2\_文件（Files）

<a id="r_modem_5Fcellular_2Eh"></a>

```c
file modem_cellular.h
```

相关声明：[modem_cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/modem__cellular_8h.html)。

用于实现蜂窝调制解调器驱动（Cellular Modem Drivers）的后端辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 33.3\_数据结构（Data Structures）

<a id="r_modem_5Fcellular_5Fdata"></a>

```c
struct modem_cellular_data
```

相关声明：[modem_cellular_data](../modem_wireless_model_reference/P050_modem_cellular_data_结构体.md)。

蜂窝调制解调器（Cellular Modem）驱动实例的运行时数据。

<a id="r_modem_5Fcellular_5Fconfig_5Fscripts"></a>

```c
struct modem_cellular_config_scripts
```

相关声明：[modem_cellular_config_scripts](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md)。

蜂窝调制解调器（Cellular Modem）的交互脚本（Chat Scripts）。

<a id="r_modem_5Fcellular_5Fvendor_5Fconfig"></a>

```c
struct modem_cellular_vendor_config
```

相关声明：[modem_cellular_vendor_config](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md)。

厂商专用的蜂窝调制解调器（Cellular Modem）配置。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 33.4\_函数（Functions）

<a id="r_ga02b8a8d17bca3f6a5bf361fdd6362b33"></a>

```c
void modem_cellular_chat_callback_handler (struct modem_chat *chat, enum modem_chat_script_result result, const struct modem_chat_script_completion_info *info, void *user_data)
```

相关声明：[modem_cellular_chat_callback_handler](#ga02b8a8d17bca3f6a5bf361fdd6362b33)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[modem_chat_script_result](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga4035be227ddec8424311575305647d3e)、[modem_chat_script_completion_info](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md)。

处理调制解调器交互脚本（modem chat script）的完成事件。

## 33.5\_详细说明（Detailed Documentation）

<a id="ga02b8a8d17bca3f6a5bf361fdd6362b33"></a>

### `modem_cellular_chat_callback_handler()`

```c
void modem_cellular_chat_callback_handler ( struct modem_chat * chat, enum modem_chat_script_result result, const struct modem_chat_script_completion_info * info, void * user_data )
```

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

处理调制解调器交互脚本（modem chat script）的完成事件。

将此函数用作蜂窝调制解调器状态机（cellular modem state machine）执行生命周期脚本（lifecycle scripts）时的回调。该回调将交互结果（chat result）转换为相应的内部状态机事件。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat` | 完成该脚本的交互实例（chat instance），不得为 `NULL`。 |
| `result` | 脚本完成结果（script completion result）。 |
| `info` | 额外的脚本完成信息，不得为 `NULL`。 |
| `user_data` | 指向关联 `modem_cellular_data` 对象的指针，不得为 `NULL`。 |


## 33.6\_原页交叉引用（Cross References）

- [蜂窝调制解调器驱动定义宏（Driver definition macros）](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html)
- [modem_cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/modem__cellular_8h.html)
- [modem_cellular_data](../modem_wireless_model_reference/P050_modem_cellular_data_结构体.md)
- [modem_cellular_config_scripts](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md)
- [modem_cellular_vendor_config](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md)
- [modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)
- [modem_chat_script_result](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga4035be227ddec8424311575305647d3e)
- [modem_chat_script_completion_info](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P032_MFD Infineon MXCRYPTOLITE 接口.md) · [返回大纲](大纲.md) · [下一章](P034_分派（Dispatches）.md)
