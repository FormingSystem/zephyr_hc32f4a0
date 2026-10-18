---
id: learning.zephyr-docs.network-service-model-reference.page-39
title: openthread_state_changed_callback_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structopenthread__state__changed__callback.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_openthread\_state\_changed\_callback\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structopenthread__state__changed__callback.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

OpenThread状态变化（State Change）的回调。

```c
#include </__w/zephyr/zephyr/modules/openthread/include/openthread.h>
```

<a id="details"></a>

OpenThread 状态变化回调结构体，用于将回调注册到回调列表。可按需添加任意多个回调，只要每个回调都使用唯一的 `struct openthread_state_changed_callback` 指针。注意：只有从回调列表注销后，才能销毁该对象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_a8bf9761ba1e70d9bfcdcda108109d52f"></a>

```c
otStateChangedCallback otCallback
```

相关声明：[otCallback](#a8bf9761ba1e70d9bfcdcda108109d52f)。

通知配置或状态变化的回调。

<a id="r_ae5a1648859eeb3df7a285becf33c8219"></a>

```c
void * user_data
```

相关声明：[user_data](#ae5a1648859eeb3df7a285becf33c8219)。

按需使用的用户数据。

<a id="r_a5c36164b8db65f2493c17a61c3434128"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a5c36164b8db65f2493c17a61c3434128)。

用于链表处理（List handling）的内部字段。

## 39.2\_详细说明（Detailed Documentation）

<a id="a5c36164b8db65f2493c17a61c3434128"></a>

### `node`

```c
sys_snode_t openthread_state_changed_callback::node
```

用于链表处理（List handling）的内部字段。

- 用户不得直接修改。

<a id="a8bf9761ba1e70d9bfcdcda108109d52f"></a>

### `otCallback`

```c
otStateChangedCallback openthread_state_changed_callback::otCallback
```

通知配置或状态变化的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otCallback` | 要注册的 OpenThread 回调。详情参见 https://openthread.io/reference/group/api-instance#otstatechangedcallback 。 |

<a id="ae5a1648859eeb3df7a285becf33c8219"></a>

### `user_data`

```c
void* openthread_state_changed_callback::user_data
```

按需使用的用户数据。

本数据类型文档由以下文件生成：

- `/__w/zephyr/zephyr/modules/openthread/include/openthread.h`

## 39.3\_原页交叉引用（Cross References）

- [/__w/zephyr/zephyr/modules/openthread/include/openthread.h](https://docs.zephyrproject.org/latest/doxygen/html/modules_2openthread_2include_2openthread_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [openthread_state_changed_callback](P039_openthread_state_changed_callback_结构体.md)
- [https://openthread.io/reference/group/api-instance#otstatechangedcallback](https://openthread.io/reference/group/api-instance#otstatechangedcallback)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_offloaded_if_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_phy_link_state_结构体.md)
