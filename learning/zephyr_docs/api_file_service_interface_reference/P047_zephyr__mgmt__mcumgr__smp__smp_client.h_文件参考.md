---
id: learning.zephyr-docs.api-file-service-interface-reference.page-47
title: zephyr__mgmt__mcumgr__smp__smp_client.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_zephyr\_\_mgmt\_\_mcumgr\_\_smp\_\_smp\_client.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/smp__client_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr简单管理协议（SMP）客户端API的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
#include <mgmt/mcumgr/transport/smp_internal.h>
#include <zephyr/mgmt/mcumgr/smp/smp.h>
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

查看此文件的源码。

MCUmgr简单管理协议（SMP）客户端API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 47.1\_数据结构（Data Structures）

<a id="r_smp_5Fclient_5Fobject"></a>

```c
struct smp_client_object
```

相关声明：[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)。

简单管理协议（SMP）的客户端对象。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 47.2\_类型定义（Typedefs）

<a id="r_gae7974bf0e951403f6dfe8b33a2547acc"></a>

```c
typedef int(* smp_client_res_fn) (struct net_buf *nb, void *user_data)
```

相关声明：[smp_client_res_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gae7974bf0e951403f6dfe8b33a2547acc)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

简单管理协议（SMP）发送操作的响应回调（Response Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 47.3\_函数（Functions）

<a id="r_ga07f36d0ac230d158c2959e8010444e47"></a>

```c
int smp_client_object_init (struct smp_client_object *smp_client, int smp_type)
```

相关声明：[smp_client_object_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#ga07f36d0ac230d158c2959e8010444e47)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)。

初始化简单管理协议（SMP）客户端对象。

<a id="r_gaf4142d0950845de6a207d02aaa6a8982"></a>

```c
static void smp_client_object_set_data (struct smp_client_object *smp_client, void *data)
```

相关声明：[smp_client_object_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gaf4142d0950845de6a207d02aaa6a8982)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)。

设置 SMP 传输的私有数据（Private Data）。

<a id="r_ga9552e2cce2711d7d0ea19ca170661419"></a>

```c
static void * smp_client_object_get_data (struct smp_client_object *smp_client)
```

相关声明：[smp_client_object_get_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#ga9552e2cce2711d7d0ea19ca170661419)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)。

获取 SMP 传输的私有数据（Private Data）。

<a id="r_gae7818782c9eefcc78911c589078ece26"></a>

```c
int smp_client_single_response (const struct smp_transport *smpt, struct net_buf *nb, const struct smp_hdr *res_hdr)
```

相关声明：[smp_client_single_response](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gae7818782c9eefcc78911c589078ece26)、[smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

SMP 客户端响应处理程序（Response Handler）。

<a id="r_ga57ec028fc6bcb3591298815b1d9b8a3b"></a>

```c
struct net_buf * smp_client_buf_allocation (struct smp_client_object *smp_client, uint16_t group, uint8_t command_id, uint8_t op, enum smp_mcumgr_version_t version)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[smp_client_buf_allocation](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#ga57ec028fc6bcb3591298815b1d9b8a3b)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[group](../posix_system_model_reference/P003_group_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[smp_mcumgr_version_t](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html#aa05d01653e39ef61a93f33319c9a00ed)。

分配缓冲区并使用 SMP 消息头（Header）进行初始化。

<a id="r_gace302f95e5f45076db72fbecf190f0f5"></a>

```c
void smp_client_buf_free (struct net_buf *nb)
```

相关声明：[smp_client_buf_free](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gace302f95e5f45076db72fbecf190f0f5)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

释放 SMP 客户端缓冲区（Buffer）。

<a id="r_gaeb20d13ddf14ddb924b0a84a014abda5"></a>

```c
int smp_client_send_cmd (struct smp_client_object *smp_client, struct net_buf *nb, smp_client_res_fn cb, void *user_data, int timeout_in_sec)
```

相关声明：[smp_client_send_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gaeb20d13ddf14ddb924b0a84a014abda5)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[smp_client_res_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gae7974bf0e951403f6dfe8b33a2547acc)。

SMP 客户端数据发送请求（Data Send Request）。


## 47.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/smp/smp.h](../api_source_supplement_reference/P113_smp.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/transport/smp.h](../api_source_system_reference/P018_smp.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P795_smp_client.h_源码浏览.md)
- [smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)
- [smp_client_res_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gae7974bf0e951403f6dfe8b33a2547acc)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [smp_client_object_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#ga07f36d0ac230d158c2959e8010444e47)
- [smp_client_object_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gaf4142d0950845de6a207d02aaa6a8982)
- [smp_client_object_get_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#ga9552e2cce2711d7d0ea19ca170661419)
- [smp_client_single_response](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gae7818782c9eefcc78911c589078ece26)
- [smp_transport](../system_service_model_reference/P081_smp_transport_结构体.md)
- [smp_client_buf_allocation](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#ga57ec028fc6bcb3591298815b1d9b8a3b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [smp_mcumgr_version_t](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html#aa05d01653e39ef61a93f33319c9a00ed)
- [smp_client_buf_free](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gace302f95e5f45076db72fbecf190f0f5)
- [smp_client_send_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__smp__client.html#gaeb20d13ddf14ddb924b0a84a014abda5)

<a id="header-details"></a>

---

[上一章](P046_zephyr__drivers__firmware__scmi__shmem.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P048_zephyr__net__ssh__server.h_文件参考.md)
