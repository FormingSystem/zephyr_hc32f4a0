---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-173
title: bt_tbs_client_call_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__tbs__client__call.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第173章\_bt\_tbs\_client\_call\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__tbs__client__call.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电话承载服务客户端（Telephone Bearer Service Client）保存一次呼叫的结构。

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

<a id="details"></a>

电话承载服务客户端（Telephone Bearer Service Client）保存一次呼叫的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 173.1\_数据成员（Data Fields）

<a id="r_a480279fea551db1bcb260de81edd6571"></a>

```c
struct bt_tbs_client_call_state call_info
```

相关声明：[bt_tbs_client_call_state](P174_bt_tbs_client_call_state_结构体.md)、[call_info](#a480279fea551db1bcb260de81edd6571)。

通话信息（Call information）。

<a id="r_af04f0576e786250526c12e1436a60c4e"></a>

```c
char * remote_uri
```

相关声明：[remote_uri](#af04f0576e786250526c12e1436a60c4e)。

移除 URI（remove URI）。

译注：官方原文此处写作“The remove URI”，可能是“remote URI（远端 URI）”的笔误；此处保留原文表述供对照。

## 173.2\_详细说明（Detailed Documentation）

<a id="a480279fea551db1bcb260de81edd6571"></a>

### `call_info`

```c
struct bt_tbs_client_call_state bt_tbs_client_call::call_info
```

通话信息（Call information）。

<a id="af04f0576e786250526c12e1436a60c4e"></a>

### `remote_uri`

```c
char* bt_tbs_client_call::remote_uri
```

移除 URI（remove URI）。

译注：官方原文此处写作“The remove URI”，可能是“remote URI（远端 URI）”的笔误；此处保留原文表述供对照。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/tbs.h`

## 173.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/tbs.h](https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h_source.html)
- [bt_tbs_client_call_state](P174_bt_tbs_client_call_state_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P172_bt_tbs_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P174_bt_tbs_client_call_state_结构体.md)
