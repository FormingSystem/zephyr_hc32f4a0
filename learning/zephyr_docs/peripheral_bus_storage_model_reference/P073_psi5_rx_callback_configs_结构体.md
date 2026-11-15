---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-73
title: psi5_rx_callback_configs_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpsi5__rx__callback__configs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_psi5\_rx\_callback\_configs\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpsi5__rx__callback__configs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接收回调（RX Callback）注册的组合配置结构。

```c
#include <zephyr/drivers/psi5/psi5.h>
```

<a id="details"></a>

接收回调（RX Callback）注册的组合配置结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 73.1\_数据成员（Data Fields）

<a id="r_a0c72a2df8fbbfc9353b37a79ae4f5e6e"></a>

```c
struct psi5_rx_callback_config * serial_frame
```

相关声明：[psi5_rx_callback_config](P072_psi5_rx_callback_config_结构体.md)、[serial_frame](#a0c72a2df8fbbfc9353b37a79ae4f5e6e)。

串行消息回调的配置。

<a id="r_a600f5e9d7d28b9a5882252765be51307"></a>

```c
struct psi5_rx_callback_config * data_frame
```

相关声明：[psi5_rx_callback_config](P072_psi5_rx_callback_config_结构体.md)、[data_frame](#a600f5e9d7d28b9a5882252765be51307)。

数据消息回调的配置。

## 73.2\_详细说明（Detailed Documentation）

<a id="a600f5e9d7d28b9a5882252765be51307"></a>

### `data_frame`

```c
struct psi5_rx_callback_config* psi5_rx_callback_configs::data_frame
```

数据消息回调的配置。

<a id="a0c72a2df8fbbfc9353b37a79ae4f5e6e"></a>

### `serial_frame`

```c
struct psi5_rx_callback_config* psi5_rx_callback_configs::serial_frame
```

串行消息回调的配置。

本数据类型文档由以下文件生成：

- `zephyr/drivers/psi5/psi5.h`

## 73.3\_原页交叉引用（Cross References）

- [zephyr/drivers/psi5/psi5.h](https://docs.zephyrproject.org/latest/doxygen/html/psi5_8h_source.html)
- [psi5_rx_callback_config](P072_psi5_rx_callback_config_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P072_psi5_rx_callback_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P074_sd_card_结构体.md)
