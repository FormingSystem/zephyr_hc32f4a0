---
id: learning.zephyr-docs.shell-transport-reference.page-4
title: Shell_MQTT后端接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__shell__mqtt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_Shell\_MQTT后端接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__shell__mqtt.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入ADSP内存窗口、MQTT、Telnet和WebSocket后端的参考与源码。源码跟踪译注与官方原文分开标示。

通过消息队列遥测传输协议（MQTT）连接访问Shell。

<a id="details"></a>

通过消息队列遥测传输协议（MQTT）连接访问Shell。

<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_shell_5Fmqtt_2Eh"></a>

```c
file shell_mqtt.h
```

相关声明：[shell_mqtt.h](P005_Shell_MQTT后端头文件参考.md)。

Shell MQTT后端（MQTT Backend）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_gad9508e0c183f9ec9aa08448e48b2082c"></a>

```c
#define SHELL_MQTT_DEFINE(_name)
```

相关声明：[SHELL_MQTT_DEFINE](#gad9508e0c183f9ec9aa08448e48b2082c)。

定义Shell MQTT传输实例（Transport Instance）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_gac3adcf640952f93e747c303724fc31bb"></a>

```c
const struct shell * shell_backend_mqtt_get_ptr (void)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_mqtt_get_ptr](#gac3adcf640952f93e747c303724fc31bb)。

此函数提供Shell MQTT后端实例的指针。

<a id="r_ga96c08138bf623c1b6ddabfb3742f6f18"></a>

```c
bool shell_mqtt_get_devid (char *id, int id_max_len)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[shell_mqtt_get_devid](#ga96c08138bf623c1b6ddabfb3742f6f18)。

定义设备标识符（Device ID，devid）的函数；Shell MQTT后端连接到代理（Broker）时，将其用作客户端标识符（Client ID）。

## 4.4\_详细说明（Detailed Documentation）

<a id="gad9508e0c183f9ec9aa08448e48b2082c"></a>

### `SHELL_MQTT_DEFINE`

```c
#define SHELL_MQTT_DEFINE ( _name)
```

```c
#include <zephyr/shell/shell_mqtt.h>
```

展开值（Value）：

```c
static struct shell_mqtt _name##_shell_mqtt;                                               \
struct shell_transport _name = { .api = &shell_mqtt_transport_api,                         \
                                 .ctx = (struct shell_mqtt *)&_name##_shell_mqtt }
```

定义Shell MQTT传输实例（Transport Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 传输实例名称（Transport Instance Name）。 |

<a id="gac3adcf640952f93e747c303724fc31bb"></a>

### `shell_backend_mqtt_get_ptr()`

```c
const struct shell * shell_backend_mqtt_get_ptr ( void )
```

```c
#include <zephyr/shell/shell_mqtt.h>
```

此函数提供Shell MQTT后端实例的指针。

函数返回Shell MQTT实例的指针。随后可将该实例传给shell_execute_cmd函数，以测试命令行为。

返回（Returns）：Shell实例指针。

<a id="ga96c08138bf623c1b6ddabfb3742f6f18"></a>

### `shell_mqtt_get_devid()`

```c
bool shell_mqtt_get_devid ( char * id, int id_max_len )
```

```c
#include <zephyr/shell/shell_mqtt.h>
```

定义设备标识符（Device ID，devid）的函数；Shell MQTT后端连接到代理（Broker）时，将其用作客户端标识符（Client ID）。

它将输出发布（Publish）到devid_tx，并订阅（Subscribe）devid_rx以接收输入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 指向devid缓冲区的指针。 |
| `id_max_len` | devid缓冲区的最大大小，由DEVICE_ID_HEX_MAX_SIZE定义。 |

说明（Note）：这是弱链接函数（Weak-linked Function），需要时可以覆盖。

返回（Returns）：devid长度大于0时为true。

## 4.5\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_mqtt.h](../../../include/zephyr/shell/shell_mqtt.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：默认弱函数通过硬件信息接口（Hardware Information）取得二进制设备编号，再用bin2hex转为十六进制文本。默认实现失败时返回false；当前后端初始化随后使用dummy作为替代编号。需要设备间不同的客户端编号时，应结合实际硬件信息或覆盖函数的行为核对。

> 译注——源码核对：官方接口说明使用devid_tx和devid_rx描述主题。当前实现将设备编号分别与CONFIG_SHELL_MQTT_TOPIC_TX_ID和CONFIG_SHELL_MQTT_TOPIC_RX_ID拼接，因此实际后缀由配置决定。get_devid返回true仅表示形成了非空编号，不表示已连接代理或订阅成功。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.6\_原页交叉引用（Cross References）

- [shell_mqtt.h](P005_Shell_MQTT后端头文件参考.md)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [shell_transport](../shell_core_reference/P009_Shell传输实例.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructshell__transport_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_Shell_ADSP内存窗口后端头文件源码.md) · [返回大纲](大纲.md) · [下一章](P005_Shell_MQTT后端头文件参考.md)
