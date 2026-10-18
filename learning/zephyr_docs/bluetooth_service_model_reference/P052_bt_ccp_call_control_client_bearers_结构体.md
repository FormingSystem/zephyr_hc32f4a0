---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-52
title: bt_ccp_call_control_client_bearers_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ccp__call__control__client__bearers.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_bt\_ccp\_call\_control\_client\_bearers\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ccp__call__control__client__bearers.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

包含客户端承载信息的结构体。

```c
#include <zephyr/bluetooth/audio/ccp.h>
```

<a id="details"></a>

包含客户端承载信息的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_a0d5936c39146ec97875c01a6d6bf1b26"></a>

```c
struct bt_ccp_call_control_client_bearer * gtbs_bearer
```

相关声明：[bt_ccp_call_control_client_bearer](P051_bt_ccp_call_control_client_bearer_结构体.md)、[gtbs_bearer](#a0d5936c39146ec97875c01a6d6bf1b26)。

通用电话承载服务承载（GTBS bearer）。

<a id="r_a100c4024c0086016ec87bc9feebacc52"></a>

```c
size_t tbs_count
```

相关声明：[tbs_count](#a100c4024c0086016ec87bc9feebacc52)。

`tbs_bearers` 中的电话承载服务承载数量（TBS bearers）。

<a id="r_a1574714c19259a291c4557c0176462a4"></a>

```c
struct bt_ccp_call_control_client_bearer * tbs_bearers [CONFIG_BT_CCP_CALL_CONTROL_CLIENT_BEARER_COUNT]
```

相关声明：[bt_ccp_call_control_client_bearer](P051_bt_ccp_call_control_client_bearer_结构体.md)、[tbs_bearers](#a1574714c19259a291c4557c0176462a4)。

电话承载服务承载指针数组（TBS bearer pointers）。

## 52.2\_详细说明（Detailed Documentation）

<a id="a0d5936c39146ec97875c01a6d6bf1b26"></a>

### `gtbs_bearer`

```c
struct bt_ccp_call_control_client_bearer* bt_ccp_call_control_client_bearers::gtbs_bearer
```

通用电话承载服务承载（GTBS bearer）。

<a id="a1574714c19259a291c4557c0176462a4"></a>

### `tbs_bearers`

```c
struct bt_ccp_call_control_client_bearer* bt_ccp_call_control_client_bearers::tbs_bearers[CONFIG_BT_CCP_CALL_CONTROL_CLIENT_BEARER_COUNT]
```

电话承载服务承载指针数组（TBS bearer pointers）。

<a id="a100c4024c0086016ec87bc9feebacc52"></a>

### `tbs_count`

```c
size_t bt_ccp_call_control_client_bearers::tbs_count
```

`tbs_bearers` 中的电话承载服务承载数量（TBS bearers）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/ccp.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/ccp.h](https://docs.zephyrproject.org/latest/doxygen/html/ccp_8h_source.html)
- [bt_ccp_call_control_client_bearer](P051_bt_ccp_call_control_client_bearer_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_bt_ccp_call_control_client_bearer_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_bt_ccp_call_control_client_cb_结构体.md)
