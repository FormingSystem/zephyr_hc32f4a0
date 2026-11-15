---
id: learning.zephyr-docs.system-service-model-reference.page-67
title: mgmt_evt_op_cmd_arg_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmgmt__evt__op__cmd__arg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_mgmt\_evt\_op\_cmd\_arg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmgmt__evt__op__cmd__arg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MGMT_EVT_OP_CMD_RECV、MGMT_EVT_OP_CMD_STATUS和MGMT_EVT_OP_CMD_DONE的参数。

```c
#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>
```

<a id="details"></a>

MGMT_EVT_OP_CMD_RECV、MGMT_EVT_OP_CMD_STATUS和MGMT_EVT_OP_CMD_DONE的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_a0607126986dc0a1e9a0dae348d278741"></a>

```c
uint16_t group
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[group](#a0607126986dc0a1e9a0dae348d278741)。

管理组类型：`mcumgr_group_t`。

<a id="r_ac461e832ea0997ae19be72df4caf0bb7"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#ac461e832ea0997ae19be72df4caf0bb7)。

组内消息 ID。

```c
union {
```

<a id="r_a374fff2d989fe7748484acedf296d53b"></a>

```c
uint8_t op
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[op](#acbd58ae2efe86685df33e58450753fe1)。

用于 `MGMT_EVT_OP_CMD_RECV` 的 `mcumgr_op_t`。

<a id="r_ac4157fdd2fcbf875b8acd7357d382c09"></a>

```c
int err
```

相关声明：[err](#a7e7a469f944d27d92e25e42d56fa32d2)。

用于 `MGMT_EVT_OP_CMD_DONE` 的 `mcumgr_err_t`。

<a id="r_ae8b840c899113d1355e0a718abf8d805"></a>

```c
int status
```

相关声明：[status](#a4d08fca41a60aee6c458d510d528a307)。

用于 `MGMT_EVT_OP_CMD_STATUS` 的 `img_mgmt_id_upload_t`。

<a id="r_a934015f5837ffb19da82a2d175e68b03"></a>

```c
};
```

## 67.2\_详细说明（Detailed Documentation）

<a id="a934015f5837ffb19da82a2d175e68b03"></a>

### `[union]`

```c
union { ... } mgmt_evt_op_cmd_arg
```

<a id="a7e7a469f944d27d92e25e42d56fa32d2"></a>

### `err`

```c
int mgmt_evt_op_cmd_arg::err
```

用于 `MGMT_EVT_OP_CMD_DONE` 的 `mcumgr_err_t`。

<a id="a0607126986dc0a1e9a0dae348d278741"></a>

### `group`

```c
uint16_t mgmt_evt_op_cmd_arg::group
```

管理组类型：`mcumgr_group_t`。

<a id="ac461e832ea0997ae19be72df4caf0bb7"></a>

### `id`

```c
uint8_t mgmt_evt_op_cmd_arg::id
```

组内消息 ID。

<a id="acbd58ae2efe86685df33e58450753fe1"></a>

### `op`

```c
uint8_t mgmt_evt_op_cmd_arg::op
```

用于 `MGMT_EVT_OP_CMD_RECV` 的 `mcumgr_op_t`。

<a id="a4d08fca41a60aee6c458d510d528a307"></a>

### `status`

```c
int mgmt_evt_op_cmd_arg::status
```

用于 `MGMT_EVT_OP_CMD_STATUS` 的 `img_mgmt_id_upload_t`。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/mgmt/callbacks.h`

## 67.3\_原页交叉引用（Cross References）

- [MGMT_EVT_OP_CMD_RECV](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28)
- [MGMT_EVT_OP_CMD_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770)
- [MGMT_EVT_OP_CMD_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api.html#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12)
- [zephyr/mgmt/mcumgr/mgmt/callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/callbacks_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [mcumgr_group_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga81f98b9a0c3810f7d607b783f8e259b5)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mcumgr_op_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gae06a618f492f18e856742b4affab80dd)
- [mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)
- [img_mgmt_id_upload_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__img__mgmt.html#ga1d239fef127e65b11b71360eadfa1ede)
- [mgmt_evt_op_cmd_arg](P067_mgmt_evt_op_cmd_arg_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_mgmt_callback_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_mgmt_group_结构体.md)
