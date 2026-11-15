---
id: learning.zephyr-docs.api-file-service-interface-reference.page-13
title: zephyr__modem__cmux.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cmux_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_modem\_\_cmux.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cmux_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/sys/ring_buffer.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/util.h>
#include <zephyr/modem/pipe.h>
#include <zephyr/modem/stats.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.1\_数据结构（Data Structures）

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

## 13.2\_类型定义（Typedefs）

<a id="r_ga998b334620c9970ebbb0bcf620ea5923"></a>

```c
typedef void(* modem_cmux_callback) (struct modem_cmux *cmux, enum modem_cmux_event event, void *user_data)
```

相关声明：[modem_cmux_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga998b334620c9970ebbb0bcf620ea5923)、[modem_cmux_event](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gab60ea756d37bd9ed59f07c6380952d36)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.3\_枚举（Enumerations）

<a id="r_gab60ea756d37bd9ed59f07c6380952d36"></a>

```c
enum modem_cmux_event { MODEM_CMUX_EVENT_CONNECTED = 0 , MODEM_CMUX_EVENT_DISCONNECTED }
```

相关声明：[modem_cmux_event](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gab60ea756d37bd9ed59f07c6380952d36)、[MODEM_CMUX_EVENT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2)、[MODEM_CMUX_EVENT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.4\_函数（Functions）

<a id="r_gad72973ad82504ae64d184ce11572ab88"></a>

```c
void modem_cmux_init (struct modem_cmux *cmux, const struct modem_cmux_config *config)
```

相关声明：[modem_cmux_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gad72973ad82504ae64d184ce11572ab88)、[modem_cmux_config](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md)。

初始化串行多路复用（CMUX）实例。

<a id="r_gabfd8e728eb8940b4093ae132b7add7d7"></a>

```c
struct modem_pipe * modem_cmux_dlci_init (struct modem_cmux *cmux, struct modem_cmux_dlci *dlci, const struct modem_cmux_dlci_config *config)
```

相关声明：[modem_cmux_dlci_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gabfd8e728eb8940b4093ae132b7add7d7)、[modem_cmux_dlci_config](../modem_wireless_model_reference/P059_modem_cmux_dlci_config_结构体.md)。

初始化数据链路连接标识（DLCI）实例，并将其注册到 CMUX 实例。

<a id="r_gab85f5c71a3cf131ff97aa47749197cb3"></a>

```c
int modem_cmux_attach (struct modem_cmux *cmux, struct modem_pipe *pipe)
```

相关声明：[modem_cmux_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gab85f5c71a3cf131ff97aa47749197cb3)。

将 CMUX 实例附接到管道（Pipe）。

<a id="r_ga362cd4b2dff122e3bbaee02b378dd226"></a>

```c
int modem_cmux_connect (struct modem_cmux *cmux)
```

相关声明：[modem_cmux_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga362cd4b2dff122e3bbaee02b378dd226)。

连接 CMUX 实例。

<a id="r_ga9fa4a1cd9cf1e1c253e621c650a611d0"></a>

```c
int modem_cmux_connect_async (struct modem_cmux *cmux)
```

相关声明：[modem_cmux_connect_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga9fa4a1cd9cf1e1c253e621c650a611d0)。

异步连接 CMUX 实例。

<a id="r_ga482171f67db206780d0b8a2cf5b32a93"></a>

```c
int modem_cmux_disconnect (struct modem_cmux *cmux)
```

相关声明：[modem_cmux_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga482171f67db206780d0b8a2cf5b32a93)。

关闭并断开 CMUX 实例。

<a id="r_ga988c8efbebf63871730918d862b7c490"></a>

```c
int modem_cmux_disconnect_async (struct modem_cmux *cmux)
```

相关声明：[modem_cmux_disconnect_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga988c8efbebf63871730918d862b7c490)。

异步关闭并断开 CMUX 实例。

<a id="r_gadc7c6ff92b7ac52717151bd6bf1efdff"></a>

```c
void modem_cmux_release (struct modem_cmux *cmux)
```

相关声明：[modem_cmux_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gadc7c6ff92b7ac52717151bd6bf1efdff)。

从管道（Pipe）释放 CMUX 实例。


## 13.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P004_环形缓冲区头文件源码.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/modem/pipe.h](../api_source_supplement_reference/P145_pipe.h_源码浏览.md)
- [zephyr/modem/stats.h](../api_source_reference/P539_stats.h_源码浏览.md)
- [查看此文件的源码。](../api_source_timing_sensor_reference/P002_cmux.h_源码浏览.md)
- [modem_cmux_config](../modem_wireless_model_reference/P058_modem_cmux_config_结构体.md)
- [modem_cmux_dlci_config](../modem_wireless_model_reference/P059_modem_cmux_dlci_config_结构体.md)
- [modem_cmux_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga998b334620c9970ebbb0bcf620ea5923)
- [modem_cmux_event](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gab60ea756d37bd9ed59f07c6380952d36)
- [MODEM_CMUX_EVENT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2)
- [MODEM_CMUX_EVENT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21)
- [modem_cmux_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gad72973ad82504ae64d184ce11572ab88)
- [modem_cmux_dlci_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gabfd8e728eb8940b4093ae132b7add7d7)
- [modem_cmux_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gab85f5c71a3cf131ff97aa47749197cb3)
- [modem_cmux_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga362cd4b2dff122e3bbaee02b378dd226)
- [modem_cmux_connect_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga9fa4a1cd9cf1e1c253e621c650a611d0)
- [modem_cmux_disconnect](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga482171f67db206780d0b8a2cf5b32a93)
- [modem_cmux_disconnect_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#ga988c8efbebf63871730918d862b7c490)
- [modem_cmux_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__cmux.html#gadc7c6ff92b7ac52717151bd6bf1efdff)

---

[上一章](P012_zephyr__drivers__clock_control__clock_control_ti_cdce9xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__bluetooth__mesh__dfu_srv.h_文件参考.md)
