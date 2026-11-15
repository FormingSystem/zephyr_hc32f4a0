---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-11
title: 调制解调器串口复用（Modem CMUX）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_调制解调器串口复用（Modem CMUX）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

调制解调器串口复用（Modem CMUX）

<a id="details"></a>

调制解调器串行多路复用（Modem CMUX）。**引入版本（Since）：**3.5。**版本（Version）：**1.0.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_modem_5Fcmux_5Fconfig"></a>

```c
struct modem_cmux_config
```

相关声明：[modem_cmux_config](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md)。

包含CMUX实例的配置数据。

<a id="r_modem_5Fcmux_5Fdlci_5Fconfig"></a>

```c
struct modem_cmux_dlci_config
```

相关声明：[modem_cmux_dlci_config](../modem_wireless_model_reference/P059_modem_cmux_dlci_config_结构体.md)。

CMUX数据链路连接标识符（DLCI）的配置。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.2\_类型定义（Typedefs）

<a id="r_ga998b334620c9970ebbb0bcf620ea5923"></a>

```c
typedef void(* modem_cmux_callback) (struct modem_cmux *cmux, enum modem_cmux_event event, void *user_data)
```

相关声明：[modem_cmux_callback](#ga998b334620c9970ebbb0bcf620ea5923)、[modem_cmux_event](#gab60ea756d37bd9ed59f07c6380952d36)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.3\_枚举（Enumerations）

<a id="r_gab60ea756d37bd9ed59f07c6380952d36"></a>

```c
enum modem_cmux_event { MODEM_CMUX_EVENT_CONNECTED = 0 , MODEM_CMUX_EVENT_DISCONNECTED }
```

相关声明：[modem_cmux_event](#gab60ea756d37bd9ed59f07c6380952d36)、[MODEM_CMUX_EVENT_CONNECTED](#ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2)、[MODEM_CMUX_EVENT_DISCONNECTED](#ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.4\_函数（Functions）

<a id="r_gad72973ad82504ae64d184ce11572ab88"></a>

```c
void modem_cmux_init (struct modem_cmux *cmux, const struct modem_cmux_config *config)
```

相关声明：[modem_cmux_init](#gad72973ad82504ae64d184ce11572ab88)、[modem_cmux_config](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md)。

初始化串行多路复用（CMUX）实例。

<a id="r_gabfd8e728eb8940b4093ae132b7add7d7"></a>

```c
struct modem_pipe * modem_cmux_dlci_init (struct modem_cmux *cmux, struct modem_cmux_dlci *dlci, const struct modem_cmux_dlci_config *config)
```

相关声明：[modem_cmux_dlci_init](#gabfd8e728eb8940b4093ae132b7add7d7)、[modem_cmux_dlci_config](../modem_wireless_model_reference/P059_modem_cmux_dlci_config_结构体.md)。

初始化数据链路连接标识（DLCI）实例，并将其注册到 CMUX 实例。

<a id="r_gab85f5c71a3cf131ff97aa47749197cb3"></a>

```c
int modem_cmux_attach (struct modem_cmux *cmux, struct modem_pipe *pipe)
```

相关声明：[modem_cmux_attach](#gab85f5c71a3cf131ff97aa47749197cb3)。

将 CMUX 实例附接到管道（Pipe）。

<a id="r_ga362cd4b2dff122e3bbaee02b378dd226"></a>

```c
int modem_cmux_connect (struct modem_cmux *cmux)
```

相关声明：[modem_cmux_connect](#ga362cd4b2dff122e3bbaee02b378dd226)。

连接 CMUX 实例。

<a id="r_ga9fa4a1cd9cf1e1c253e621c650a611d0"></a>

```c
int modem_cmux_connect_async (struct modem_cmux *cmux)
```

相关声明：[modem_cmux_connect_async](#ga9fa4a1cd9cf1e1c253e621c650a611d0)。

异步连接 CMUX 实例。

<a id="r_ga482171f67db206780d0b8a2cf5b32a93"></a>

```c
int modem_cmux_disconnect (struct modem_cmux *cmux)
```

相关声明：[modem_cmux_disconnect](#ga482171f67db206780d0b8a2cf5b32a93)。

关闭并断开 CMUX 实例。

<a id="r_ga988c8efbebf63871730918d862b7c490"></a>

```c
int modem_cmux_disconnect_async (struct modem_cmux *cmux)
```

相关声明：[modem_cmux_disconnect_async](#ga988c8efbebf63871730918d862b7c490)。

异步关闭并断开 CMUX 实例。

<a id="r_gadc7c6ff92b7ac52717151bd6bf1efdff"></a>

```c
void modem_cmux_release (struct modem_cmux *cmux)
```

相关声明：[modem_cmux_release](#gadc7c6ff92b7ac52717151bd6bf1efdff)。

从管道（Pipe）释放 CMUX 实例。

## 11.5\_详细说明（Detailed Documentation）

<a id="ga998b334620c9970ebbb0bcf620ea5923"></a>

### `modem_cmux_callback`

```c
typedef void(* modem_cmux_callback) (struct modem_cmux *cmux, enum modem_cmux_event event, void *user_data)
```

```c
#include <zephyr/modem/cmux.h>
```

<a id="gab60ea756d37bd9ed59f07c6380952d36"></a>

### `modem_cmux_event`

```c
enum modem_cmux_event
```

```c
#include <zephyr/modem/cmux.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MODEM_CMUX_EVENT_CONNECTED` |  |
| `MODEM_CMUX_EVENT_DISCONNECTED` |  |

<a id="gab85f5c71a3cf131ff97aa47749197cb3"></a>

### `modem_cmux_attach()`

```c
int modem_cmux_attach ( struct modem_cmux * cmux, struct modem_pipe * pipe )
```

```c
#include <zephyr/modem/cmux.h>
```

将 CMUX 实例附接到管道（Pipe）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cmux` | 串行多路复用（CMUX）实例。 |
| `pipe` | CMUX 实例要附接到的管道（Pipe）实例。 |

<a id="ga362cd4b2dff122e3bbaee02b378dd226"></a>

### `modem_cmux_connect()`

```c
int modem_cmux_connect ( struct modem_cmux * cmux)
```

```c
#include <zephyr/modem/cmux.h>
```

连接 CMUX 实例。

向串行总线上的目标发送 CMUX 连接请求；成功后，可通过 `modem_pipe_open()` 打开数据链路连接标识（DLCI）通道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cmux` | 串行多路复用（CMUX）实例。 |

**说明（Note）**：**注意（Note）：**连接建立后，不得直接使用总线管道（Bus Pipe）。

<a id="ga9fa4a1cd9cf1e1c253e621c650a611d0"></a>

### `modem_cmux_connect_async()`

```c
int modem_cmux_connect_async ( struct modem_cmux * cmux)
```

```c
#include <zephyr/modem/cmux.h>
```

异步连接 CMUX 实例。

向串行总线上的目标发送 CMUX 连接请求；成功后，可通过 `modem_pipe_open()` 打开数据链路连接标识（DLCI）通道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cmux` | 串行多路复用（CMUX）实例。 |

**说明（Note）**：**注意（Note）：**连接建立后，不得直接使用总线管道（Bus Pipe）。

<a id="ga482171f67db206780d0b8a2cf5b32a93"></a>

### `modem_cmux_disconnect()`

```c
int modem_cmux_disconnect ( struct modem_cmux * cmux)
```

```c
#include <zephyr/modem/cmux.h>
```

关闭并断开 CMUX 实例。

关闭所有已打开的数据链路连接标识（DLCI）通道，并关闭 CMUX 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cmux` | 串行多路复用（CMUX）实例。 |

**说明（Note）**：**注意（Note）：**断开连接后，必须先通过 `modem_cmux_release()` 释放总线管道，才能复用它。

<a id="ga988c8efbebf63871730918d862b7c490"></a>

### `modem_cmux_disconnect_async()`

```c
int modem_cmux_disconnect_async ( struct modem_cmux * cmux)
```

```c
#include <zephyr/modem/cmux.h>
```

异步关闭并断开 CMUX 实例。

关闭所有已打开的数据链路连接标识（DLCI）通道，并关闭 CMUX 连接。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cmux` | 串行多路复用（CMUX）实例。 |

**说明（Note）**：**注意（Note）：**断开连接后，必须先通过 `modem_cmux_release()` 释放总线管道，才能复用它。

<a id="gabfd8e728eb8940b4093ae132b7add7d7"></a>

### `modem_cmux_dlci_init()`

```c
struct modem_pipe * modem_cmux_dlci_init ( struct modem_cmux * cmux, struct modem_cmux_dlci * dlci, const struct modem_cmux_dlci_config * config )
```

```c
#include <zephyr/modem/cmux.h>
```

初始化数据链路连接标识（DLCI）实例，并将其注册到 CMUX 实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cmux` | 要注册 DLCI 的 CMUX 实例。 |
| `dlci` | 待注册和配置的 DLCI 实例。 |
| `config` | 要应用到 DLCI 实例的配置（Configuration）。 |

<a id="gad72973ad82504ae64d184ce11572ab88"></a>

### `modem_cmux_init()`

```c
void modem_cmux_init ( struct modem_cmux * cmux, const struct modem_cmux_config * config )
```

```c
#include <zephyr/modem/cmux.h>
```

初始化串行多路复用（CMUX）实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cmux` | 串行多路复用（CMUX）实例。 |
| `config` | 要应用到 CMUX 实例的配置（Configuration）。 |

<a id="gadc7c6ff92b7ac52717151bd6bf1efdff"></a>

### `modem_cmux_release()`

```c
void modem_cmux_release ( struct modem_cmux * cmux)
```

```c
#include <zephyr/modem/cmux.h>
```

从管道（Pipe）释放 CMUX 实例。

释放管道，并在内部硬复位（Hard Reset）CMUX 实例。应先使用 `modem_cmux_disconnect()` 断开 CMUX。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cmux` | 串行多路复用（CMUX）实例。 |

**说明（Note）**：**注意（Note）：**CMUX 实例释放后，可再次直接使用总线管道（Bus Pipe）。


## 11.6\_原页交叉引用（Cross References）

- [modem_cmux_config](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md)
- [modem_cmux_dlci_config](../modem_wireless_model_reference/P059_modem_cmux_dlci_config_结构体.md)
- [zephyr/modem/cmux.h](../api_file_service_interface_reference/P013_zephyr__modem__cmux.h_文件参考.md)
- [modem_pipe_open()](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga7521ac0aeda8027c47741237e8312bf0)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2"></a>
<a id="ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_MFD PCA9422 接口.md) · [返回大纲](大纲.md) · [下一章](P012_应用接收端（Application sinks）.md)
