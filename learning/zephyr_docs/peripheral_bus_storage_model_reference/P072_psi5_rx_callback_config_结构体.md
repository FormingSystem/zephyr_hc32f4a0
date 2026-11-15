---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-72
title: psi5_rx_callback_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpsi5__rx__callback__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第72章\_psi5\_rx\_callback\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpsi5__rx__callback__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接收回调（RX Callback）的配置结构。

```c
#include <zephyr/drivers/psi5/psi5.h>
```

<a id="details"></a>

接收回调（RX Callback）的配置结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 72.1\_数据成员（Data Fields）

<a id="r_ad7811862b9f6f7f010eb232fc319bcfb"></a>

```c
psi5_rx_frame_callback_t callback
```

相关声明：[psi5_rx_frame_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga5f43079d704d882ae014c7a15bde6406)、[callback](#ad7811862b9f6f7f010eb232fc319bcfb)。

收到帧时调用的回调函数。

<a id="r_a97356b621ae2c142104320c588fa316f"></a>

```c
struct psi5_frame * frame
```

相关声明：[psi5_frame](P071_psi5_frame_结构体.md)、[frame](#a97356b621ae2c142104320c588fa316f)。

指向用于存储接收帧的缓冲区的指针。

<a id="r_a53035b05d9e60b090d6329487af27541"></a>

```c
uint32_t max_num_frame
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[max_num_frame](#a53035b05d9e60b090d6329487af27541)。

最多存储的帧数。

<a id="r_ad2b224c07eaaf7aef22c94a0e78353c1"></a>

```c
void * user_data
```

相关声明：[user_data](#ad2b224c07eaaf7aef22c94a0e78353c1)。

指向传给回调函数的用户数据的指针。

## 72.2\_详细说明（Detailed Documentation）

<a id="ad7811862b9f6f7f010eb232fc319bcfb"></a>

### `callback`

```c
psi5_rx_frame_callback_t psi5_rx_callback_config::callback
```

收到帧时调用的回调函数。

<a id="a97356b621ae2c142104320c588fa316f"></a>

### `frame`

```c
struct psi5_frame* psi5_rx_callback_config::frame
```

指向用于存储接收帧的缓冲区的指针。

<a id="a53035b05d9e60b090d6329487af27541"></a>

### `max_num_frame`

```c
uint32_t psi5_rx_callback_config::max_num_frame
```

最多存储的帧数。

<a id="ad2b224c07eaaf7aef22c94a0e78353c1"></a>

### `user_data`

```c
void* psi5_rx_callback_config::user_data
```

指向传给回调函数的用户数据的指针。

本数据类型文档由以下文件生成：

- `zephyr/drivers/psi5/psi5.h`

## 72.3\_原页交叉引用（Cross References）

- [zephyr/drivers/psi5/psi5.h](https://docs.zephyrproject.org/latest/doxygen/html/psi5_8h_source.html)
- [psi5_rx_frame_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__psi5__interface.html#ga5f43079d704d882ae014c7a15bde6406)
- [psi5_frame](P071_psi5_frame_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P071_psi5_frame_结构体.md) · [返回大纲](大纲.md) · [下一章](P073_psi5_rx_callback_configs_结构体.md)
