---
id: learning.zephyr-docs.system-service-model-reference.page-9
title: ec_host_cmd_backend_api_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__backend__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_ec\_host\_cmd\_backend\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__backend__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：主机命令（Host Command）驱动操作。

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：主机命令（Host Command）驱动操作。这是每个主机命令驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_ae2619efe5d809f7aa51252727b1a05c4"></a>

```c
ec_host_cmd_backend_api_init init
```

相关声明：[ec_host_cmd_backend_api_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga811b9c355942811f0fee22c1fa8a5787)、[init](#ae2619efe5d809f7aa51252727b1a05c4)。

必需（REQ）：初始化主机命令后端。

<a id="r_afed14f2aa633e836c90c8c559a9fe7bb"></a>

```c
ec_host_cmd_backend_api_send send
```

相关声明：[ec_host_cmd_backend_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)、[send](#afed14f2aa633e836c90c8c559a9fe7bb)。

必需（REQ）：向主机发送数据。

## 9.2\_详细说明（Detailed Documentation）

<a id="ae2619efe5d809f7aa51252727b1a05c4"></a>

### `init`

```c
ec_host_cmd_backend_api_init ec_host_cmd_backend_api::init
```

必需（REQ）：初始化主机命令后端。

<a id="afed14f2aa633e836c90c8c559a9fe7bb"></a>

### `send`

```c
ec_host_cmd_backend_api_send ec_host_cmd_backend_api::send
```

必需（REQ）：向主机发送数据。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/ec_host_cmd/backend.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/ec_host_cmd/backend.h](https://docs.zephyrproject.org/latest/doxygen/html/backend_8h_source.html)
- [ec_host_cmd_backend_api_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga811b9c355942811f0fee22c1fa8a5787)
- [ec_host_cmd_backend_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_ec_host_cmd_backend_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_ec_host_cmd_handler_结构体.md)
