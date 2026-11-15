---
id: learning.zephyr-docs.api-extension-topic-reference.page-16
title: 操作系统管理客户端（OS Management Client）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_操作系统管理客户端（OS Management Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 操作系统管理客户端 API

<a id="details"></a>

MCUmgr 操作系统管理客户端 API

<a id="header-files"></a>
<a id="files"></a>

## 16.1\_文件（Files）

<a id="r_os_5Fmgmt_5Fclient_2Eh"></a>

```c
file os_mgmt_client.h
```

相关声明：[os_mgmt_client.h](../api_file_runtime_reference/P050_zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt_client.h_文件参考.md)。

MCUmgr操作系统管理客户端（OS Management Client）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.2\_数据结构（Data Structures）

<a id="r_os_5Fmgmt_5Fclient"></a>

```c
struct os_mgmt_client
```

相关声明：[os_mgmt_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md)。

操作系统管理（OS Management）的客户端对象。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.3\_函数（Functions）

<a id="r_gafab4d3da30fa2bf855110d541b8fee08"></a>

```c
void os_mgmt_client_init (struct os_mgmt_client *client, struct smp_client_object *smp_client)
```

相关声明：[os_mgmt_client_init](#gafab4d3da30fa2bf855110d541b8fee08)、[os_mgmt_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)。

初始化操作系统管理客户端（OS Management Client）。

<a id="r_ga2dd2edb7c3952413c361b3d38dc2eaad"></a>

```c
int os_mgmt_client_echo (struct os_mgmt_client *client, const char *echo_string, size_t max_len)
```

相关声明：[os_mgmt_client_echo](#ga2dd2edb7c3952413c361b3d38dc2eaad)、[os_mgmt_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md)。

发送回显命令（Echo Command）的简单管理协议消息（SMP Message）。

<a id="r_ga5cb153bf30c40e82e8f55ac18a45fa09"></a>

```c
int os_mgmt_client_reset (struct os_mgmt_client *client)
```

相关声明：[os_mgmt_client_reset](#ga5cb153bf30c40e82e8f55ac18a45fa09)、[os_mgmt_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md)。

发送简单管理协议复位命令（SMP Reset Command）。

## 16.4\_详细说明（Detailed Documentation）

<a id="ga2dd2edb7c3952413c361b3d38dc2eaad"></a>

### `os_mgmt_client_echo()`

```c
int os_mgmt_client_echo ( struct os_mgmt_client * client, const char * echo_string, size_t max_len )
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_client.h>
```

发送回显命令（Echo Command）的简单管理协议消息（SMP Message）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 操作系统管理（OS Management）的客户端对象。 |
| `echo_string` | 回显字符串（Echo String）。 |
| `max_len` | `echo_string` 的最大长度（Maximum Length）。 |

返回（Returns）：成功时为 0；失败时为 `mcumgr_err_t` 错误码。

<a id="gafab4d3da30fa2bf855110d541b8fee08"></a>

### `os_mgmt_client_init()`

```c
void os_mgmt_client_init ( struct os_mgmt_client * client, struct smp_client_object * smp_client )
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_client.h>
```

初始化操作系统管理客户端（OS Management Client）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 操作系统管理（OS Management）的客户端对象。 |
| `smp_client` | 简单管理协议（SMP）的客户端对象。 |

<a id="ga5cb153bf30c40e82e8f55ac18a45fa09"></a>

### `os_mgmt_client_reset()`

```c
int os_mgmt_client_reset ( struct os_mgmt_client * client)
```

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_client.h>
```

发送简单管理协议复位命令（SMP Reset Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 操作系统管理（OS Management）的客户端对象。 |

返回（Returns）：成功时为 0；失败时为 `mcumgr_err_t` 错误码。


## 16.5\_原页交叉引用（Cross References）

- [os_mgmt_client.h](../api_file_runtime_reference/P050_zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt_client.h_文件参考.md)
- [os_mgmt_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md)
- [smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)
- [mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_处理程序（Handlers）.md) · [返回大纲](大纲.md) · [下一章](P017_UDP 传输.md)
