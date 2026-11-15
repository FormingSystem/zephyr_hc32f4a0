---
id: learning.zephyr-docs.modem-wireless-model-reference.page-58
title: modem_cmux_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cmux__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_modem\_cmux\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cmux__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

包含CMUX实例的配置数据。

```c
#include <zephyr/modem/cmux.h>
```

<a id="details"></a>

包含CMUX实例的配置数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_a2cba948c704f02429022d360326b9838"></a>

```c
modem_cmux_callback callback
```

相关声明：[modem_cmux_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga998b334620c9970ebbb0bcf620ea5923)、[callback](#a2cba948c704f02429022d360326b9838)。

事件发生时调用。

<a id="r_a6714790f733ba7e4431353b6cdbbe3ee"></a>

```c
void * user_data
```

相关声明：[user_data](#a6714790f733ba7e4431353b6cdbbe3ee)。

可自由使用的指针，在调用事件处理函数时传入。

<a id="r_a2935694a75a95da8571b1c520a9800c8"></a>

```c
uint8_t * receive_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[receive_buf](#a2935694a75a95da8571b1c520a9800c8)。

接收缓冲区。

<a id="r_a2fcf4ba7f088701ec6c5b750c8af3a89"></a>

```c
uint16_t receive_buf_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[receive_buf_size](#a2fcf4ba7f088701ec6c5b750c8af3a89)。

接收缓冲区大小，单位为字节，范围从 127 开始。

<a id="r_a6920bf8f7c52522e8b76ba09051887c5"></a>

```c
uint8_t * transmit_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transmit_buf](#a6920bf8f7c52522e8b76ba09051887c5)。

发送缓冲区。

<a id="r_ae028b4dde63311a810c67686dc662154"></a>

```c
uint16_t transmit_buf_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[transmit_buf_size](#ae028b4dde63311a810c67686dc662154)。

发送缓冲区大小，单位为字节，范围从 149 开始。

<a id="r_a1f955b28efb6f3e1a2a6e6eac66d687e"></a>

```c
bool enable_runtime_power_management
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable_runtime_power_management](#a1f955b28efb6f3e1a2a6e6eac66d687e)。

启用运行时电源管理（runtime power management）。

<a id="r_acf451afdc3033fffac12d546f7e7c6c0"></a>

```c
bool close_pipe_on_power_save
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[close_pipe_on_power_save](#acf451afdc3033fffac12d546f7e7c6c0)。

进入节能状态时关闭管道（pipe）。

<a id="r_a11333197710a1fc3c6c1d1ac5f706b09"></a>

```c
bool no_powersave_handshake
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[no_powersave_handshake](#a11333197710a1fc3c6c1d1ac5f706b09)。

进入和退出节能状态时都跳过带内节能握手（in-band power-save handshake）。

<a id="r_aade573d6cd09b2b2ca0efbefc25f0759"></a>

```c
k_timeout_t idle_timeout
```

相关声明：[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[idle_timeout](#aade573d6cd09b2b2ca0efbefc25f0759)。

进入节能状态的空闲超时时间。

## 58.2\_详细说明（Detailed Documentation）

<a id="a2cba948c704f02429022d360326b9838"></a>

### `callback`

```c
modem_cmux_callback modem_cmux_config::callback
```

事件发生时调用。

<a id="acf451afdc3033fffac12d546f7e7c6c0"></a>

### `close_pipe_on_power_save`

```c
bool modem_cmux_config::close_pipe_on_power_save
```

进入节能状态时关闭管道（pipe）。

<a id="a1f955b28efb6f3e1a2a6e6eac66d687e"></a>

### `enable_runtime_power_management`

```c
bool modem_cmux_config::enable_runtime_power_management
```

启用运行时电源管理（runtime power management）。

<a id="aade573d6cd09b2b2ca0efbefc25f0759"></a>

### `idle_timeout`

```c
k_timeout_t modem_cmux_config::idle_timeout
```

进入节能状态的空闲超时时间。

<a id="a11333197710a1fc3c6c1d1ac5f706b09"></a>

### `no_powersave_handshake`

```c
bool modem_cmux_config::no_powersave_handshake
```

进入和退出节能状态时都跳过带内节能握手（in-band power-save handshake）。

<a id="a2935694a75a95da8571b1c520a9800c8"></a>

### `receive_buf`

```c
uint8_t* modem_cmux_config::receive_buf
```

接收缓冲区。

<a id="a2fcf4ba7f088701ec6c5b750c8af3a89"></a>

### `receive_buf_size`

```c
uint16_t modem_cmux_config::receive_buf_size
```

接收缓冲区大小，单位为字节，范围从 127 开始。

<a id="a6920bf8f7c52522e8b76ba09051887c5"></a>

### `transmit_buf`

```c
uint8_t* modem_cmux_config::transmit_buf
```

发送缓冲区。

<a id="ae028b4dde63311a810c67686dc662154"></a>

### `transmit_buf_size`

```c
uint16_t modem_cmux_config::transmit_buf_size
```

发送缓冲区大小，单位为字节，范围从 149 开始。

<a id="a6714790f733ba7e4431353b6cdbbe3ee"></a>

### `user_data`

```c
void* modem_cmux_config::user_data
```

可自由使用的指针，在调用事件处理函数时传入。

本数据类型文档由以下文件生成：

- `zephyr/modem/cmux.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/modem/cmux.h](https://docs.zephyrproject.org/latest/doxygen/html/cmux_8h_source.html)
- [modem_cmux_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga998b334620c9970ebbb0bcf620ea5923)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_modem_chat_script_completion_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_modem_cmux_dlci_config_结构体.md)
