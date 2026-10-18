---
id: learning.zephyr-docs.modem-wireless-model-reference.page-51
title: modem_cellular_vendor_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cellular__vendor__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_modem\_cellular\_vendor\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cellular__vendor__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

厂商专用的蜂窝调制解调器（Cellular Modem）配置。

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

<a id="details"></a>

供应商专用的蜂窝调制解调器配置。为每种调制解调器变体定义一个常量对象。引用的脚本和非请求消息匹配数组，必须在使用此配置的每个设备实例的整个生命周期内保持有效。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_a7dee75ad296954cc33932aa98186f0a6"></a>

```c
struct modem_cellular_config_scripts scripts
```

相关声明：[modem_cellular_config_scripts](P049_modem_cellular_config_scripts_结构体.md)、[scripts](#a7dee75ad296954cc33932aa98186f0a6)。

实现调制解调器生命周期的交互脚本（Chat scripts）。

```c
struct {
```

<a id="r_a89b5e76b28e3b06e9a739495f62b900c"></a>

```c
const struct modem_chat_match * matches
```

相关声明：[modem_chat_match](P054_modem_chat_match_结构体.md)、[matches](#a84e1ccc5a311240a4c7d356ec7d90f5f)。

非请求响应（unsolicited response）匹配项数组；大小为零时可为 `NULL`。

<a id="r_a2d77d0c6dd1f14c9f7abae97b0345725"></a>

```c
uint16_t size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[size](#a8d14f4c96be18fb575beffd5768bc16c)。

`matches` 中的元素数量。

<a id="r_affae7b69107c6f63f59bb6c64e844cdb"></a>

```c
} unsol_matches
```

相关声明：[unsol_matches](#affae7b69107c6f63f59bb6c64e844cdb)。

非请求调制解调器响应的匹配项。

<a id="r_a5b19228e384856ac3a57af617b4afcf0"></a>

```c
const char * chat_delimiter
```

相关声明：[chat_delimiter](#a5b19228e384856ac3a57af617b4afcf0)。

调制解调器使用的命令分隔符（delimiter），以空字符结尾的字符串表示。

<a id="r_a95eca8f1f380a97f64f46e0a80b58922"></a>

```c
const char * chat_filter
```

相关声明：[chat_filter](#a95eca8f1f380a97f64f46e0a80b58922)。

要从调制解调器响应中过滤的字符，以空字符结尾的字符串表示。

<a id="r_a90b312d50b585d13a3d56f9974e17251"></a>

```c
uint16_t power_pulse_duration_ms
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[power_pulse_duration_ms](#a90b312d50b585d13a3d56f9974e17251)。

调制解调器电源按键脉冲的持续时间，单位为毫秒。

<a id="r_a3b4fb8542f1a4903b54b49c667e2378c"></a>

```c
uint16_t reset_pulse_duration_ms
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[reset_pulse_duration_ms](#a3b4fb8542f1a4903b54b49c667e2378c)。

调制解调器复位脉冲的持续时间，单位为毫秒。

<a id="r_a967f56a3ec4e1c331db02e71ebf2fdeb"></a>

```c
uint16_t cmux_disconnect_timeout_ms
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cmux_disconnect_timeout_ms](#a967f56a3ec4e1c331db02e71ebf2fdeb)。

CMUX 断开后，等待调制解调器从 CMUX 返回 AT 模式的超时时间，单位为毫秒。

<a id="r_af37df7d8e6ef21cffc52fd4bc0b3dec2"></a>

```c
uint16_t startup_time_ms
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[startup_time_ms](#af37df7d8e6ef21cffc52fd4bc0b3dec2)。

调制解调器的最大启动延迟，单位为毫秒。

<a id="r_a2f6a9b8f14ddf2650562b3348cedabfd"></a>

```c
uint16_t shutdown_time_ms
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[shutdown_time_ms](#a2f6a9b8f14ddf2650562b3348cedabfd)。

调制解调器的最大关机延迟，单位为毫秒。

<a id="r_a52e33fceac79378e370675d567de2b5e"></a>

```c
bool force_autostart
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[force_autostart](#a52e33fceac79378e370675d567de2b5e)。

无论设备树中的 `autostarts` 属性如何设置，都强制自动启动。

## 51.2\_详细说明（Detailed Documentation）

<a id="a5b19228e384856ac3a57af617b4afcf0"></a>

### `chat_delimiter`

```c
const char* modem_cellular_vendor_config::chat_delimiter
```

调制解调器使用的命令分隔符（delimiter），以空字符结尾的字符串表示。

不得为 `NULL`，并且必须在设备的整个生命周期内保持有效。

<a id="a95eca8f1f380a97f64f46e0a80b58922"></a>

### `chat_filter`

```c
const char* modem_cellular_vendor_config::chat_filter
```

要从调制解调器响应中过滤的字符，以空字符结尾的字符串表示。

可设为 `NULL` 以禁用过滤；非 `NULL` 字符串必须在设备的整个生命周期内保持有效。

<a id="a967f56a3ec4e1c331db02e71ebf2fdeb"></a>

### `cmux_disconnect_timeout_ms`

```c
uint16_t modem_cellular_vendor_config::cmux_disconnect_timeout_ms
```

CMUX 断开后，等待调制解调器从 CMUX 返回 AT 模式的超时时间，单位为毫秒。

为了兼容旧行为，未指定时（`value == 0U`）默认使用 `reset_pulse_duration_ms`。

<a id="a52e33fceac79378e370675d567de2b5e"></a>

### `force_autostart`

```c
bool modem_cellular_vendor_config::force_autostart
```

无论设备树中的 `autostarts` 属性如何设置，都强制自动启动。

<a id="a84e1ccc5a311240a4c7d356ec7d90f5f"></a>

### `matches`

```c
const struct modem_chat_match* modem_cellular_vendor_config::matches
```

非请求响应（unsolicited response）匹配项数组；大小为零时可为 `NULL`。

<a id="a90b312d50b585d13a3d56f9974e17251"></a>

### `power_pulse_duration_ms`

```c
uint16_t modem_cellular_vendor_config::power_pulse_duration_ms
```

调制解调器电源按键脉冲的持续时间，单位为毫秒。

<a id="a3b4fb8542f1a4903b54b49c667e2378c"></a>

### `reset_pulse_duration_ms`

```c
uint16_t modem_cellular_vendor_config::reset_pulse_duration_ms
```

调制解调器复位脉冲的持续时间，单位为毫秒。

<a id="a7dee75ad296954cc33932aa98186f0a6"></a>

### `scripts`

```c
struct modem_cellular_config_scripts modem_cellular_vendor_config::scripts
```

实现调制解调器生命周期的交互脚本（Chat scripts）。

<a id="a2f6a9b8f14ddf2650562b3348cedabfd"></a>

### `shutdown_time_ms`

```c
uint16_t modem_cellular_vendor_config::shutdown_time_ms
```

调制解调器的最大关机延迟，单位为毫秒。

<a id="a8d14f4c96be18fb575beffd5768bc16c"></a>

### `size`

```c
uint16_t modem_cellular_vendor_config::size
```

`matches` 中的元素数量。

<a id="af37df7d8e6ef21cffc52fd4bc0b3dec2"></a>

### `startup_time_ms`

```c
uint16_t modem_cellular_vendor_config::startup_time_ms
```

调制解调器的最大启动延迟，单位为毫秒。

<a id="affae7b69107c6f63f59bb6c64e844cdb"></a>

### `[struct]`

```c
struct { ... } modem_cellular_vendor_config::unsol_matches
```

非请求调制解调器响应的匹配项。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/modem_cellular.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/modem_cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/modem__cellular_8h_source.html)
- [modem_cellular_config_scripts](P049_modem_cellular_config_scripts_结构体.md)
- [modem_chat_match](P054_modem_chat_match_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_modem_cellular_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_modem_chat_结构体.md)
