---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-12
title: 简单管理协议客户端（SMP client）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_简单管理协议客户端（SMP client）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr SMP 客户端 API

<a id="details"></a>

MCUmgr SMP 客户端 API

<a id="header-files"></a>
<a id="files"></a>

## 12.1\_文件（Files）

<a id="r_smp_5Fclient_2Eh"></a>

```c
file smp_client.h
```

相关声明：[smp_client.h](../api_file_service_interface_reference/P047_zephyr__mgmt__mcumgr__smp__smp_client.h_文件参考.md)。

MCUmgr简单管理协议（SMP）客户端API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.2\_数据结构（Data Structures）

<a id="r_smp_5Fclient_5Fobject"></a>

```c
struct smp_client_object
```

相关声明：[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)。

简单管理协议（SMP）的客户端对象。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 12.3\_类型定义（Typedefs）

<a id="r_gae7974bf0e951403f6dfe8b33a2547acc"></a>

```c
typedef int(* smp_client_res_fn) (struct net_buf *nb, void *user_data)
```

相关声明：[smp_client_res_fn](#gae7974bf0e951403f6dfe8b33a2547acc)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

简单管理协议（SMP）发送操作的响应回调（Response Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.4\_函数（Functions）

<a id="r_ga07f36d0ac230d158c2959e8010444e47"></a>

```c
int smp_client_object_init (struct smp_client_object *smp_client, int smp_type)
```

相关声明：[smp_client_object_init](#ga07f36d0ac230d158c2959e8010444e47)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)。

初始化简单管理协议（SMP）客户端对象。

<a id="r_gaf4142d0950845de6a207d02aaa6a8982"></a>

```c
static void smp_client_object_set_data (struct smp_client_object *smp_client, void *data)
```

相关声明：[smp_client_object_set_data](#gaf4142d0950845de6a207d02aaa6a8982)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)。

设置 SMP 传输的私有数据（Private Data）。

<a id="r_ga9552e2cce2711d7d0ea19ca170661419"></a>

```c
static void * smp_client_object_get_data (struct smp_client_object *smp_client)
```

相关声明：[smp_client_object_get_data](#ga9552e2cce2711d7d0ea19ca170661419)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)。

获取 SMP 传输的私有数据（Private Data）。

<a id="r_gae7818782c9eefcc78911c589078ece26"></a>

```c
int smp_client_single_response (const struct smp_transport *smpt, struct net_buf *nb, const struct smp_hdr *res_hdr)
```

相关声明：[smp_client_single_response](#gae7818782c9eefcc78911c589078ece26)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

SMP 客户端响应处理程序（Response Handler）。

<a id="r_ga57ec028fc6bcb3591298815b1d9b8a3b"></a>

```c
struct net_buf * smp_client_buf_allocation (struct smp_client_object *smp_client, uint16_t group, uint8_t command_id, uint8_t op, enum smp_mcumgr_version_t version)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[smp_client_buf_allocation](#ga57ec028fc6bcb3591298815b1d9b8a3b)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[group](../posix_system_model_reference/P003_group_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[smp_mcumgr_version_t](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html#aa05d01653e39ef61a93f33319c9a00ed)。

分配缓冲区并使用 SMP 消息头（Header）进行初始化。

<a id="r_gace302f95e5f45076db72fbecf190f0f5"></a>

```c
void smp_client_buf_free (struct net_buf *nb)
```

相关声明：[smp_client_buf_free](#gace302f95e5f45076db72fbecf190f0f5)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

释放 SMP 客户端缓冲区（Buffer）。

<a id="r_gaeb20d13ddf14ddb924b0a84a014abda5"></a>

```c
int smp_client_send_cmd (struct smp_client_object *smp_client, struct net_buf *nb, smp_client_res_fn cb, void *user_data, int timeout_in_sec)
```

相关声明：[smp_client_send_cmd](#gaeb20d13ddf14ddb924b0a84a014abda5)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[smp_client_res_fn](#gae7974bf0e951403f6dfe8b33a2547acc)。

SMP 客户端数据发送请求（Data Send Request）。

## 12.5\_详细说明（Detailed Documentation）

<a id="gae7974bf0e951403f6dfe8b33a2547acc"></a>

### `smp_client_res_fn`

```c
typedef int(* smp_client_res_fn) (struct net_buf *nb, void *user_data)
```

```c
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
```

简单管理协议（SMP）发送操作的响应回调（Response Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nb` | 用于响应的网络缓冲区（net_buf）。 |
| `user_data` | 与请求中提供的相同用户数据（User Data）。 |

返回（Returns）：成功时为 0；失败时为 `mcumgr_err_t` 错误码。

<a id="ga57ec028fc6bcb3591298815b1d9b8a3b"></a>

### `smp_client_buf_allocation()`

```c
struct net_buf * smp_client_buf_allocation ( struct smp_client_object * smp_client, uint16_t group, uint8_t command_id, uint8_t op, enum smp_mcumgr_version_t version )
```

```c
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
```

分配缓冲区并使用 SMP 消息头（Header）进行初始化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `smp_client` | 简单管理协议（SMP）的客户端对象。 |
| `group` | 简单管理协议（SMP）组 ID。 |
| `command_id` | SMP 命令 ID（Command ID）。 |
| `op` | SMP 操作类型（Operation Type）。 |
| `version` | SMP MCUmgr 版本（Version）。 |

**返回（Returns）**：返回值：成功返回新分配的 `net_buf` 缓冲区，失败返回 `NULL`。

<a id="gace302f95e5f45076db72fbecf190f0f5"></a>

### `smp_client_buf_free()`

```c
void smp_client_buf_free ( struct net_buf * nb)
```

```c
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
```

释放 SMP 客户端缓冲区（Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nb` | 要释放的 `net_buf`。 |

<a id="ga9552e2cce2711d7d0ea19ca170661419"></a>

### `smp_client_object_get_data()`

```c
void * smp_client_object_get_data ( struct smp_client_object * smp_client)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
```

获取 SMP 传输的私有数据（Private Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `smp_client` | 要为其设置私有数据（Private Data）的客户端（Client）。 |

<a id="ga07f36d0ac230d158c2959e8010444e47"></a>

### `smp_client_object_init()`

```c
int smp_client_object_init ( struct smp_client_object * smp_client, int smp_type )
```

```c
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
```

初始化简单管理协议（SMP）客户端对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `smp_client` | 要构造的客户端（Client）。 |
| `smp_type` | 用于发现传输对象（Transport Object）的 SMP 传输类型（Transport Type）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 `mcumgr_err_t` 错误码。

<a id="gaf4142d0950845de6a207d02aaa6a8982"></a>

### `smp_client_object_set_data()`

```c
void smp_client_object_set_data ( struct smp_client_object * smp_client, void * data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
```

设置 SMP 传输的私有数据（Private Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `smp_client` | 要为其设置私有数据（Private Data）的客户端（Client）。 |
| `data` | SMP 传输私有数据（Transport Private Data）。 |

<a id="gaeb20d13ddf14ddb924b0a84a014abda5"></a>

### `smp_client_send_cmd()`

```c
int smp_client_send_cmd ( struct smp_client_object * smp_client, struct net_buf * nb, smp_client_res_fn cb, void * user_data, int timeout_in_sec )
```

```c
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
```

SMP 客户端数据发送请求（Data Send Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `smp_client` | 简单管理协议（SMP）的客户端对象。 |
| `nb` | 用于发送的 `net_buf` 数据包。 |
| `cb` | 响应处理回调（Response Handler Callback）。 |
| `user_data` | 用户定义的数据指针（User Data Pointer），会回传给响应回调。 |
| `timeout_in_sec` | 发送过程的超时（Timeout），单位为秒。客户端依据 `CONFIG_SMP_CMD_RETRY_TIME` 重试传输。 |

返回（Returns）：成功时为 0；失败时为 `mcumgr_err_t` 错误码。

<a id="gae7818782c9eefcc78911c589078ece26"></a>

### `smp_client_single_response()`

```c
int smp_client_single_response ( const struct smp_transport * smpt, struct net_buf * nb, const struct smp_hdr * res_hdr )
```

```c
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
```

SMP 客户端响应处理程序（Response Handler）。

响应只会完成通过 `smpt` 发送、且组 ID 和命令 ID 都相同的待完成命令（Pending Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `smpt` | 收到响应的 SMP 传输（Transport）。 |
| `nb` | 响应 `net_buf` 缓冲区。 |
| `res_hdr` | 已解析的 SMP 头部（Header），采用主机字节序（Host Byte Order）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_ERR_EOK` | 此响应完成了一个待完成命令（Pending Command）。 |
| `MGMT_ERR_ENOENT` | 没有带回调的待完成命令（Pending Command）与该响应匹配。 |


## 12.6\_原页交叉引用（Cross References）

- [smp_client.h](../api_file_service_interface_reference/P047_zephyr__mgmt__mcumgr__smp__smp_client.h_文件参考.md)
- [smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [smp_mcumgr_version_t](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html#aa05d01653e39ef61a93f33319c9a00ed)
- [mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)
- [MGMT_ERR_EOK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f)
- [MGMT_ERR_ENOENT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a54ad7a80506d328de6b6d0a0e37fad9e)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_MCP9600 API主题.md) · [返回大纲](大纲.md) · [下一章](P013_数据报分组层路径 MTU 发现 API（Datagram PLPMTUD API）.md)
