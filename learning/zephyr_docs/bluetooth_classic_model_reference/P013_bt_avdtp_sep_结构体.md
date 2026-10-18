---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-13
title: bt_avdtp_sep_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avdtp__sep.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_bt\_avdtp\_sep\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avdtp__sep.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

AVDTP 流端点（Stream End Point）。

```c
#include <zephyr/bluetooth/classic/avdtp.h>
```

<a id="details"></a>

AVDTP 流端点（Stream End Point）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_a0258b35f0834479a2dccdcad9b3854b9"></a>

```c
struct bt_avdtp_sep_info sep_info
```

相关声明：[bt_avdtp_sep_info](P014_bt_avdtp_sep_info_结构体.md)、[sep_info](#a0258b35f0834479a2dccdcad9b3854b9)。

流端点信息（Stream End Point Information）。

<a id="r_a33e4959b5d7c5f53469ed59af4cae022"></a>

```c
struct bt_l2cap_br_chan chan
```

相关声明：[bt_l2cap_br_chan](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__chan.html)、[chan](#a33e4959b5d7c5f53469ed59af4cae022)。

媒体传输通道（Media Transport Channel）。

<a id="r_acff70f1a2d29b987f57af88ac75afc3e"></a>

```c
struct k_sem sem_lock
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[sem_lock](#acff70f1a2d29b987f57af88ac75afc3e)。

<a id="r_a5c1afb8231c42d39156023939583681a"></a>

```c
struct bt_avdtp * session
```

相关声明：[session](#a5c1afb8231c42d39156023939583681a)。

AVDTP 会话（Session）。

<a id="r_a1d9cb5bedeae1fdea1ee63e656d06503"></a>

```c
const struct bt_avdtp_sep_ops * ops
```

相关声明：[bt_avdtp_sep_ops](P015_bt_avdtp_sep_ops_结构体.md)、[ops](#a1d9cb5bedeae1fdea1ee63e656d06503)。

流端点操作（SEP Operations）。

<a id="r_a2405b59cc7ed23c9cb221a9a684dc386"></a>

```c
uint8_t state
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](#a2405b59cc7ed23c9cb221a9a684dc386)。

流端点状态（SEP State）。

## 13.2\_详细说明（Detailed Documentation）

<a id="a33e4959b5d7c5f53469ed59af4cae022"></a>

### `chan`

```c
struct bt_l2cap_br_chan bt_avdtp_sep::chan
```

媒体传输通道（Media Transport Channel）。

<a id="a1d9cb5bedeae1fdea1ee63e656d06503"></a>

### `ops`

```c
const struct bt_avdtp_sep_ops* bt_avdtp_sep::ops
```

流端点操作（SEP Operations）。

<a id="acff70f1a2d29b987f57af88ac75afc3e"></a>

### `sem_lock`

```c
struct k_sem bt_avdtp_sep::sem_lock
```

<a id="a0258b35f0834479a2dccdcad9b3854b9"></a>

### `sep_info`

```c
struct bt_avdtp_sep_info bt_avdtp_sep::sep_info
```

流端点信息（Stream End Point Information）。

<a id="a5c1afb8231c42d39156023939583681a"></a>

### `session`

```c
struct bt_avdtp* bt_avdtp_sep::session
```

AVDTP 会话（Session）。

<a id="a2405b59cc7ed23c9cb221a9a684dc386"></a>

### `state`

```c
uint8_t bt_avdtp_sep::state
```

流端点状态（SEP State）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avdtp.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avdtp.h](https://docs.zephyrproject.org/latest/doxygen/html/avdtp_8h_source.html)
- [bt_avdtp_sep_info](P014_bt_avdtp_sep_info_结构体.md)
- [bt_l2cap_br_chan](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__chan.html)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [bt_avdtp_sep_ops](P015_bt_avdtp_sep_ops_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_bt_addr_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_bt_avdtp_sep_info_结构体.md)
