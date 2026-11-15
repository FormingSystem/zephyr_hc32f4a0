---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-89
title: sent_rx_callback_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsent__rx__callback__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第89章\_sent\_rx\_callback\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsent__rx__callback__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接收回调（RX Callback）的配置结构。

```c
#include <zephyr/drivers/sent/sent.h>
```

<a id="details"></a>

接收回调（RX Callback）的配置结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 89.1\_数据成员（Data Fields）

<a id="r_afcf63b8116f8dca5839c5b44b5fd1b39"></a>

```c
sent_rx_frame_callback_t callback
```

相关声明：[sent_rx_frame_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga47d05656177dae0a388e1155be82494f)、[callback](#afcf63b8116f8dca5839c5b44b5fd1b39)。

收到帧时调用的回调函数。

<a id="r_a251257c08668ced3773bec6895fbd467"></a>

```c
struct sent_frame * frame
```

相关声明：[sent_frame](P088_sent_frame_结构体.md)、[frame](#a251257c08668ced3773bec6895fbd467)。

指向用于存储接收帧的缓冲区的指针。

<a id="r_a45b6353ae6f2177d2267cc343c798726"></a>

```c
uint32_t max_num_frame
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_num_frame](#a45b6353ae6f2177d2267cc343c798726)。

最多存储的帧数。

<a id="r_a67e2cd95a91793a1cfbb73f86862ff04"></a>

```c
void * user_data
```

相关声明：[user_data](#a67e2cd95a91793a1cfbb73f86862ff04)。

指向传给回调函数的用户数据的指针。

## 89.2\_详细说明（Detailed Documentation）

<a id="afcf63b8116f8dca5839c5b44b5fd1b39"></a>

### `callback`

```c
sent_rx_frame_callback_t sent_rx_callback_config::callback
```

收到帧时调用的回调函数。

<a id="a251257c08668ced3773bec6895fbd467"></a>

### `frame`

```c
struct sent_frame* sent_rx_callback_config::frame
```

指向用于存储接收帧的缓冲区的指针。

<a id="a45b6353ae6f2177d2267cc343c798726"></a>

### `max_num_frame`

```c
uint32_t sent_rx_callback_config::max_num_frame
```

最多存储的帧数。

<a id="a67e2cd95a91793a1cfbb73f86862ff04"></a>

### `user_data`

```c
void* sent_rx_callback_config::user_data
```

指向传给回调函数的用户数据的指针。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sent/sent.h`

## 89.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sent/sent.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sent_2sent_8h_source.html)
- [sent_rx_frame_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sent__interface.html#ga47d05656177dae0a388e1155be82494f)
- [sent_frame](P088_sent_frame_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P088_sent_frame_结构体.md) · [返回大纲](大纲.md) · [下一章](P090_sent_rx_callback_configs_结构体.md)
