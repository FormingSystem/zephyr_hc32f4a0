---
id: learning.zephyr-docs.modem-wireless-model-reference.page-36
title: mdm_hl7800_callback_agent_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmdm__hl7800__callback__agent.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_mdm\_hl7800\_callback\_agent\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmdm__hl7800__callback__agent.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

事件回调注册（Event Callback Registration）。

```c
#include <zephyr/drivers/modem/hl7800.h>
```

<a id="details"></a>

事件回调注册（Event Callback Registration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 36.1\_数据成员（Data Fields）

<a id="r_a5b69a3952ee320ee88fd99220bac3ef5"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a5b69a3952ee320ee88fd99220bac3ef5)。

为驱动保留，请勿修改。

<a id="r_adb1eb808c084c9afb6077b04aa1bb026"></a>

```c
mdm_hl7800_event_callback_t event_callback
```

相关声明：[mdm_hl7800_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gafa044d03d9bfbc2f63088da4f094edfc)、[event_callback](#adb1eb808c084c9afb6077b04aa1bb026)。

调制解调器事件发生时调用的回调。

## 36.2\_详细说明（Detailed Documentation）

<a id="adb1eb808c084c9afb6077b04aa1bb026"></a>

### `event_callback`

```c
mdm_hl7800_event_callback_t mdm_hl7800_callback_agent::event_callback
```

调制解调器事件发生时调用的回调。

<a id="a5b69a3952ee320ee88fd99220bac3ef5"></a>

### `node`

```c
sys_snode_t mdm_hl7800_callback_agent::node
```

为驱动保留，请勿修改。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl7800.h`

## 36.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl7800.h](https://docs.zephyrproject.org/latest/doxygen/html/hl7800_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [mdm_hl7800_event_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__hl7800__interface.html#gafa044d03d9bfbc2f63088da4f094edfc)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P035_mdm_hl7800_apn_结构体.md) · [返回大纲](大纲.md) · [下一章](P037_mdm_hl7800_compound_event_结构体.md)
