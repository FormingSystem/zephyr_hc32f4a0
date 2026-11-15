---
id: learning.zephyr-docs.api-file-network-device-reference.page-24
title: zephyr__drivers__modem__modem_cellular.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modem__cellular_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_drivers\_\_modem\_\_modem\_cellular.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/modem__cellular_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于实现蜂窝调制解调器驱动（Cellular Modem Drivers）的后端辅助接口。

<a id="details"></a>

```c
#include <zephyr/drivers/cellular.h>
#include <zephyr/modem/backend/uart.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/pm/device.h>
#include <zephyr/modem/chat.h>
#include <zephyr/modem/cmux.h>
#include <zephyr/modem/pipe.h>
#include <zephyr/modem/pipelink.h>
#include <zephyr/modem/ppp.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/atomic.h>
```

查看此文件的源码。

用于实现蜂窝调制解调器驱动（Cellular Modem Drivers）的后端辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 24.1\_数据结构（Data Structures）

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

<a id="r_modem_5Fcellular_5Fboard_5Finit"></a>

```c
struct modem_cellular_board_init
```

相关声明：[modem_cellular_board_init](../modem_wireless_model_reference/P048_modem_cellular_board_init_结构体.md)。

将开发板提供的初始化脚本（Init Script）绑定到调制解调器实例的描述符。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 24.2\_宏定义（Macros）

<a id="r_ga5cf681cc8970ee193b960d5e964aee32"></a>

```c
#define MODEM_CELLULAR_INST_NAME(name, inst)
```

相关声明：[MODEM_CELLULAR_INST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#ga5cf681cc8970ee193b960d5e964aee32)。

为调制解调器实例对象（Modem Instance Object）生成唯一的 C 标识符。

<a id="r_gab6cc63dc914ee95542a0b5a4a2ebd7f9"></a>

```c
#define MODEM_CELLULAR_DEFINE_AND_INIT_USER_PIPES(inst, ...)
```

相关声明：[MODEM_CELLULAR_DEFINE_AND_INIT_USER_PIPES](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#gab6cc63dc914ee95542a0b5a4a2ebd7f9)。

为调制解调器实例定义额外的 CMUX 用户管道（User Pipes）。

<a id="r_gac2990fadd342efc0394ec7dadb8e3c82"></a>

```c
#define MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE(_sym, _match, _separators, _callback)
```

相关声明：[MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#gac2990fadd342efc0394ec7dadb8e3c82)。

定义多重匹配对象（Multiple Match Object），预期先收到一个响应，再收到 `OK`。

<a id="r_gacc9e3af4dacf62f956f68839eefc6862"></a>

```c
#define MODEM_CELLULAR_COMMON_CHAT_MATCHES()
```

相关声明：[MODEM_CELLULAR_COMMON_CHAT_MATCHES](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#gacc9e3af4dacf62f956f68839eefc6862)。

定义蜂窝调制解调器脚本使用的通用聊天匹配项（Chat Matches）。

<a id="r_ga4fd2f91635f03a6e1fa4a0bddc7c7cdf"></a>

```c
#define MODEM_CELLULAR_COMMON_UNSOL_MATCHES
```

相关声明：[MODEM_CELLULAR_COMMON_UNSOL_MATCHES](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#ga4fd2f91635f03a6e1fa4a0bddc7c7cdf)。

展开为通用非请求响应匹配项（Unsolicited Response Matches）。

<a id="r_ga4b61e995f86377dfbab0ca81d1efe492"></a>

```c
#define MODEM_CELLULAR_DEFINE_INSTANCE(inst, vendor_config, _vendor_specific)
```

相关声明：[MODEM_CELLULAR_DEFINE_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#ga4b61e995f86377dfbab0ca81d1efe492)。

定义蜂窝调制解调器设备实例（Cellular Modem Device Instance）。

<a id="r_ga5b16137fbab1b7199075e88422a0b9b4"></a>

```c
#define MODEM_CELLULAR_BOARD_INIT_DEFINE(node_id, _script)
```

相关声明：[MODEM_CELLULAR_BOARD_INIT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#ga5b16137fbab1b7199075e88422a0b9b4)。

为调制解调器实例注册开发板专用初始化脚本（Board-specific Init Script）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.3\_函数（Functions）

<a id="r_ga02b8a8d17bca3f6a5bf361fdd6362b33"></a>

```c
void modem_cellular_chat_callback_handler (struct modem_chat *chat, enum modem_chat_script_result result, const struct modem_chat_script_completion_info *info, void *user_data)
```

相关声明：[modem_cellular_chat_callback_handler](../api_protocol_topic_reference/P033_蜂窝调制解调器辅助功能（Cellular modem helpers）.md#ga02b8a8d17bca3f6a5bf361fdd6362b33)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[modem_chat_script_result](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga4035be227ddec8424311575305647d3e)、[modem_chat_script_completion_info](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md)。

处理调制解调器交互脚本（modem chat script）的完成事件。

<a id="r_ga2ae42cd17e07ca8e24aa75352c07e5fe"></a>

```c
int cellular_modem_pause_periodic_script (const struct device *dev)
```

相关声明：[cellular_modem_pause_periodic_script](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga2ae42cd17e07ca8e24aa75352c07e5fe)、[device](../device_reference/P002_设备对象结构.md)。

暂停 `cellular_modem` 驱动的周期聊天脚本（Periodic Chat Script）。

<a id="r_ga5dc375b9ab33b2468846b8ca77a2106b"></a>

```c
int cellular_modem_resume_periodic_script (const struct device *dev)
```

相关声明：[cellular_modem_resume_periodic_script](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga5dc375b9ab33b2468846b8ca77a2106b)、[device](../device_reference/P002_设备对象结构.md)。

恢复 `cellular_modem` 驱动的周期聊天脚本（Periodic Chat Script）。


## 24.4\_原页交叉引用（Cross References）

- [zephyr/drivers/cellular.h](../api_source_supplement_reference/P025_cellular.h_源码浏览.md)
- [zephyr/modem/backend/uart.h](../api_source_supplement_reference/P116_uart.h_源码浏览.md)
- [zephyr/drivers/uart.h](../uart_driver_reference/P002_UART驱动头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [zephyr/pm/device.h](../api_source_configuration_reference/P071_device.h_源码浏览.md)
- [zephyr/modem/chat.h](../api_source_interrupt_modem_reference/P002_chat.h_源码浏览.md)
- [zephyr/modem/cmux.h](../api_source_timing_sensor_reference/P002_cmux.h_源码浏览.md)
- [zephyr/modem/pipe.h](../api_source_supplement_reference/P145_pipe.h_源码浏览.md)
- [zephyr/modem/pipelink.h](../api_source_reference/P661_pipelink.h_源码浏览.md)
- [zephyr/modem/ppp.h](../api_source_interrupt_modem_reference/P005_ppp.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [查看此文件的源码。](../api_source_interrupt_modem_reference/P006_modem_cellular.h_源码浏览.md)
- [modem_cellular_data](../modem_wireless_model_reference/P050_modem_cellular_data_结构体.md)
- [modem_cellular_config_scripts](../modem_wireless_model_reference/P049_modem_cellular_config_scripts_结构体.md)
- [modem_cellular_vendor_config](../modem_wireless_model_reference/P051_modem_cellular_vendor_config_结构体.md)
- [modem_cellular_board_init](../modem_wireless_model_reference/P048_modem_cellular_board_init_结构体.md)
- [MODEM_CELLULAR_INST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#ga5cf681cc8970ee193b960d5e964aee32)
- [MODEM_CELLULAR_DEFINE_AND_INIT_USER_PIPES](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#gab6cc63dc914ee95542a0b5a4a2ebd7f9)
- [MODEM_CELLULAR_OK_CHAT_MATCH_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#gac2990fadd342efc0394ec7dadb8e3c82)
- [MODEM_CELLULAR_COMMON_CHAT_MATCHES](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#gacc9e3af4dacf62f956f68839eefc6862)
- [MODEM_CELLULAR_COMMON_UNSOL_MATCHES](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#ga4fd2f91635f03a6e1fa4a0bddc7c7cdf)
- [MODEM_CELLULAR_DEFINE_INSTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#ga4b61e995f86377dfbab0ca81d1efe492)
- [MODEM_CELLULAR_BOARD_INIT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__driver__macros.html#ga5b16137fbab1b7199075e88422a0b9b4)
- [modem_cellular_chat_callback_handler](../api_protocol_topic_reference/P033_蜂窝调制解调器辅助功能（Cellular modem helpers）.md#ga02b8a8d17bca3f6a5bf361fdd6362b33)
- [modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)
- [modem_chat_script_result](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__chat.html#ga4035be227ddec8424311575305647d3e)
- [modem_chat_script_completion_info](../modem_wireless_model_reference/P057_modem_chat_script_completion_info_结构体.md)
- [cellular_modem_pause_periodic_script](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga2ae42cd17e07ca8e24aa75352c07e5fe)
- [device](../device_reference/P002_设备对象结构.md)
- [cellular_modem_resume_periodic_script](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga5dc375b9ab33b2468846b8ca77a2106b)

<a id="header-details"></a>

---

[上一章](P023_zephyr__mgmt__mcumgr__mgmt__mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__mpipe__utils__mpipe_player.h_文件参考.md)
