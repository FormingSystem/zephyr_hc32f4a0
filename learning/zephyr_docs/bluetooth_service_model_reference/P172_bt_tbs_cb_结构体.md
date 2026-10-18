---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-172
title: bt_tbs_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__tbs__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第172章\_bt\_tbs\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__tbs__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存电话承载服务（Telephone Bearer Service）回调的结构。

```c
#include <zephyr/bluetooth/audio/tbs.h>
```

<a id="details"></a>

保存电话承载服务（Telephone Bearer Service，TBS）回调的结构体。可通过 `bt_tbs_register_cb()` 注册这些回调供使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 172.1\_数据成员（Data Fields）

<a id="r_a566504bee9c7334c53a23223e544855f"></a>

```c
bt_tbs_originate_call_cb originate_call
```

相关声明：[bt_tbs_originate_call_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga60e9e143f247bb7e668293f0233ce300)、[originate_call](#a566504bee9c7334c53a23223e544855f)。

客户端发起通话（originating call）。

<a id="r_ab065a5c58db19feb2a1d3013983ed5aa"></a>

```c
bt_tbs_terminate_call_cb terminate_call
```

相关声明：[bt_tbs_terminate_call_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga69e93b48b2a48e8a6552882660b791cc)、[terminate_call](#ab065a5c58db19feb2a1d3013983ed5aa)。

客户端终止通话（terminating call）。

<a id="r_a8b76dd9243e97d22e0d6c2ac578aa383"></a>

```c
bt_tbs_call_change_cb hold_call
```

相关声明：[bt_tbs_call_change_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga2fa85f3cd96f25f6bb4f449fc9210fa1)、[hold_call](#a8b76dd9243e97d22e0d6c2ac578aa383)。

客户端保持通话（holding call）。

<a id="r_a798c09c04a563800c4d9328c1d9e2de6"></a>

```c
bt_tbs_call_change_cb accept_call
```

相关声明：[bt_tbs_call_change_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga2fa85f3cd96f25f6bb4f449fc9210fa1)、[accept_call](#a798c09c04a563800c4d9328c1d9e2de6)。

客户端接受通话（accepting call）。

<a id="r_ad543a2f26d1749eba0774e2352b53692"></a>

```c
bt_tbs_call_change_cb retrieve_call
```

相关声明：[bt_tbs_call_change_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga2fa85f3cd96f25f6bb4f449fc9210fa1)、[retrieve_call](#ad543a2f26d1749eba0774e2352b53692)。

客户端恢复通话（retrieving call）。

<a id="r_ac1a99a703687a3ef5ebc12eca5f6c2e7"></a>

```c
bt_tbs_join_calls_cb join_calls
```

相关声明：[bt_tbs_join_calls_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa45b3f4837165d722c2df6f202a39058)、[join_calls](#ac1a99a703687a3ef5ebc12eca5f6c2e7)。

客户端合并通话（joining calls）。

<a id="r_ab7c859ffaebcf16db71c5d54bd4f5802"></a>

```c
bt_tbs_authorize_cb authorize
```

相关声明：[bt_tbs_authorize_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga1cc9e7140531b07bf6a8dedbc17f24c0)、[authorize](#ab7c859ffaebcf16db71c5d54bd4f5802)。

对客户端进行授权（authorize）的回调。

## 172.2\_详细说明（Detailed Documentation）

<a id="a798c09c04a563800c4d9328c1d9e2de6"></a>

### `accept_call`

```c
bt_tbs_call_change_cb bt_tbs_cb::accept_call
```

客户端接受通话（accepting call）。

<a id="ab7c859ffaebcf16db71c5d54bd4f5802"></a>

### `authorize`

```c
bt_tbs_authorize_cb bt_tbs_cb::authorize
```

对客户端进行授权（authorize）的回调。

<a id="a8b76dd9243e97d22e0d6c2ac578aa383"></a>

### `hold_call`

```c
bt_tbs_call_change_cb bt_tbs_cb::hold_call
```

客户端保持通话（holding call）。

<a id="ac1a99a703687a3ef5ebc12eca5f6c2e7"></a>

### `join_calls`

```c
bt_tbs_join_calls_cb bt_tbs_cb::join_calls
```

客户端合并通话（joining calls）。

<a id="a566504bee9c7334c53a23223e544855f"></a>

### `originate_call`

```c
bt_tbs_originate_call_cb bt_tbs_cb::originate_call
```

客户端发起通话（originating call）。

<a id="ad543a2f26d1749eba0774e2352b53692"></a>

### `retrieve_call`

```c
bt_tbs_call_change_cb bt_tbs_cb::retrieve_call
```

客户端恢复通话（retrieving call）。

<a id="ab065a5c58db19feb2a1d3013983ed5aa"></a>

### `terminate_call`

```c
bt_tbs_terminate_call_cb bt_tbs_cb::terminate_call
```

客户端终止通话（terminating call）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/tbs.h`

## 172.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/tbs.h](https://docs.zephyrproject.org/latest/doxygen/html/tbs_8h_source.html)
- [bt_tbs_originate_call_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga60e9e143f247bb7e668293f0233ce300)
- [bt_tbs_terminate_call_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga69e93b48b2a48e8a6552882660b791cc)
- [bt_tbs_call_change_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga2fa85f3cd96f25f6bb4f449fc9210fa1)
- [bt_tbs_join_calls_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#gaa45b3f4837165d722c2df6f202a39058)
- [bt_tbs_authorize_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga1cc9e7140531b07bf6a8dedbc17f24c0)
- [bt_tbs_register_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html#ga76f120dba549225a6f2c2c22be08edfc)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P171_bt_sdp_record_结构体.md) · [返回大纲](大纲.md) · [下一章](P173_bt_tbs_client_call_结构体.md)
