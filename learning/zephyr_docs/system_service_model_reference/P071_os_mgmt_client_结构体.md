---
id: learning.zephyr-docs.system-service-model-reference.page-71
title: os_mgmt_client_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structos__mgmt__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_os\_mgmt\_client\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structos__mgmt__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

操作系统管理（OS Management）的客户端对象。

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_client.h>
```

<a id="details"></a>

操作系统管理（OS Management）的客户端对象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 71.1\_数据成员（Data Fields）

<a id="r_ada340aa0c6da9632410c36695adc0c33"></a>

```c
struct smp_client_object * smp_client
```

相关声明：[smp_client_object](P078_smp_client_object_结构体.md)、[smp_client](#ada340aa0c6da9632410c36695adc0c33)。

简单管理协议（SMP）的客户端对象。

<a id="r_ac177e863befa59a099efd3ee7de0acc3"></a>

```c
int status
```

相关声明：[status](#ac177e863befa59a099efd3ee7de0acc3)。

命令状态。

## 71.2\_详细说明（Detailed Documentation）

<a id="ada340aa0c6da9632410c36695adc0c33"></a>

### `smp_client`

```c
struct smp_client_object* os_mgmt_client::smp_client
```

简单管理协议（SMP）的客户端对象。

<a id="ac177e863befa59a099efd3ee7de0acc3"></a>

### `status`

```c
int os_mgmt_client::status
```

命令状态。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_client.h`

## 71.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_client.h](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__client_8h_source.html)
- [smp_client_object](P078_smp_client_object_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P070_os_mgmt_bootloader_info_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P072_os_mgmt_info_append_结构体.md)
