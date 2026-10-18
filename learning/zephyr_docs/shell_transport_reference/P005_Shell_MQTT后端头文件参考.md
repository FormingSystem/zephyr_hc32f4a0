---
id: learning.zephyr-docs.shell-transport-reference.page-5
title: Shell_MQTT后端头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__mqtt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_Shell\_MQTT后端头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__mqtt_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入ADSP内存窗口、MQTT、Telnet和WebSocket后端的参考与源码。源码跟踪译注与官方原文分开标示。

Shell MQTT后端（MQTT Backend）的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/shell/shell.h>
#include <zephyr/net/socket.h>
#include <zephyr/net/net_mgmt.h>
#include <zephyr/net/net_event.h>
#include <zephyr/net/conn_mgr_monitor.h>
#include <zephyr/net/mqtt.h>
#include <zephyr/sys/ring_buffer.h>
```

查看此文件的源码。

Shell MQTT后端（MQTT Backend）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_gad9508e0c183f9ec9aa08448e48b2082c"></a>

```c
#define SHELL_MQTT_DEFINE(_name)
```

相关声明：[SHELL_MQTT_DEFINE](P004_Shell_MQTT后端接口.md#gad9508e0c183f9ec9aa08448e48b2082c)。

定义Shell MQTT传输实例（Transport Instance）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.2\_函数（Functions）

<a id="r_gac3adcf640952f93e747c303724fc31bb"></a>

```c
const struct shell * shell_backend_mqtt_get_ptr (void)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_mqtt_get_ptr](P004_Shell_MQTT后端接口.md#gac3adcf640952f93e747c303724fc31bb)。

此函数提供Shell MQTT后端实例的指针。

<a id="r_ga96c08138bf623c1b6ddabfb3742f6f18"></a>

```c
bool shell_mqtt_get_devid (char *id, int id_max_len)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[shell_mqtt_get_devid](P004_Shell_MQTT后端接口.md#ga96c08138bf623c1b6ddabfb3742f6f18)。

定义设备标识符（Device ID，devid）的函数；Shell MQTT后端连接到代理（Broker）时，将其用作客户端标识符（Client ID）。

## 5.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_mqtt.h](../../../include/zephyr/shell/shell_mqtt.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：默认弱函数通过硬件信息接口（Hardware Information）取得二进制设备编号，再用bin2hex转为十六进制文本。默认实现失败时返回false；当前后端初始化随后使用dummy作为替代编号。需要设备间不同的客户端编号时，应结合实际硬件信息或覆盖函数的行为核对。

> 译注——源码核对：官方接口说明使用devid_tx和devid_rx描述主题。当前实现将设备编号分别与CONFIG_SHELL_MQTT_TOPIC_TX_ID和CONFIG_SHELL_MQTT_TOPIC_RX_ID拼接，因此实际后缀由配置决定。get_devid返回true仅表示形成了非空编号，不表示已连接代理或订阅成功。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/shell/shell.h](../shell_core_reference/P003_Shell核心头文件源码.md)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h_source.html)
- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h_source.html)
- [zephyr/net/conn_mgr_monitor.h](https://docs.zephyrproject.org/latest/doxygen/html/conn__mgr__monitor_8h_source.html)
- [zephyr/net/mqtt.h](https://docs.zephyrproject.org/latest/doxygen/html/mqtt_8h_source.html)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P004_环形缓冲区头文件源码.md)
- [查看此文件的源码](P006_Shell_MQTT后端头文件源码.md)
- [SHELL_MQTT_DEFINE](P004_Shell_MQTT后端接口.md#gad9508e0c183f9ec9aa08448e48b2082c)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_backend_mqtt_get_ptr](P004_Shell_MQTT后端接口.md#gac3adcf640952f93e747c303724fc31bb)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [shell_mqtt_get_devid](P004_Shell_MQTT后端接口.md#ga96c08138bf623c1b6ddabfb3742f6f18)

<a id="header-details"></a>

---

[上一章](P004_Shell_MQTT后端接口.md) · [返回大纲](大纲.md) · [下一章](P006_Shell_MQTT后端头文件源码.md)
