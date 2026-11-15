---
id: learning.zephyr-docs.api-file-runtime-reference.page-50
title: zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt_client.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__client_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_os\_mgmt\_\_os\_mgmt\_client.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__client_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr操作系统管理客户端（OS Management Client）API的头文件。

<a id="details"></a>

```c
#include <inttypes.h>
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
```

查看此文件的源码。

MCUmgr操作系统管理客户端（OS Management Client）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 50.1\_数据结构（Data Structures）

<a id="r_os_5Fmgmt_5Fclient"></a>

```c
struct os_mgmt_client
```

相关声明：[os_mgmt_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md)。

操作系统管理（OS Management）的客户端对象。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 50.2\_函数（Functions）

<a id="r_gafab4d3da30fa2bf855110d541b8fee08"></a>

```c
void os_mgmt_client_init (struct os_mgmt_client *client, struct smp_client_object *smp_client)
```

相关声明：[os_mgmt_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html#gafab4d3da30fa2bf855110d541b8fee08)、[os_mgmt_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)。

初始化操作系统管理客户端（OS Management Client）。

<a id="r_ga2dd2edb7c3952413c361b3d38dc2eaad"></a>

```c
int os_mgmt_client_echo (struct os_mgmt_client *client, const char *echo_string, size_t max_len)
```

相关声明：[os_mgmt_client_echo](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html#ga2dd2edb7c3952413c361b3d38dc2eaad)、[os_mgmt_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md)。

发送回显命令（Echo Command）的简单管理协议消息（SMP Message）。

<a id="r_ga5cb153bf30c40e82e8f55ac18a45fa09"></a>

```c
int os_mgmt_client_reset (struct os_mgmt_client *client)
```

相关声明：[os_mgmt_client_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html#ga5cb153bf30c40e82e8f55ac18a45fa09)、[os_mgmt_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md)。

发送简单管理协议复位命令（SMP Reset Command）。


## 50.3\_原页交叉引用（Cross References）

- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h_source.html)
- [zephyr/mgmt/mcumgr/smp/smp_client.h](../api_source_reference/P795_smp_client.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P638_os_mgmt_client.h_源码浏览.md)
- [os_mgmt_client](../system_service_model_reference/P071_os_mgmt_client_结构体.md)
- [os_mgmt_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html#gafab4d3da30fa2bf855110d541b8fee08)
- [smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)
- [os_mgmt_client_echo](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html#ga2dd2edb7c3952413c361b3d38dc2eaad)
- [os_mgmt_client_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt__client.html#ga5cb153bf30c40e82e8f55ac18a45fa09)

<a id="header-details"></a>

---

[上一章](P049_zephyr__net__offloaded_netdev.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P051_zephyr__sys__printk-hooks.h_文件参考.md)
