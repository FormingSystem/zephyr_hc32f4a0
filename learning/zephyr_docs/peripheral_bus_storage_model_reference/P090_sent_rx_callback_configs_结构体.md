---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-90
title: sent_rx_callback_configs_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsent__rx__callback__configs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第90章\_sent\_rx\_callback\_configs\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsent__rx__callback__configs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接收回调（RX Callback）注册的组合配置结构。

```c
#include <zephyr/drivers/sent/sent.h>
```

<a id="details"></a>

接收回调（RX Callback）注册的组合配置结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 90.1\_数据成员（Data Fields）

<a id="r_a631882e363de3c8cc693336028561c1b"></a>

```c
struct sent_rx_callback_config * serial
```

相关声明：[sent_rx_callback_config](P089_sent_rx_callback_config_结构体.md)、[serial](#a631882e363de3c8cc693336028561c1b)。

串行消息回调的配置。

<a id="r_a0f4d0261c97b21430de9782e20d1c244"></a>

```c
struct sent_rx_callback_config * fast
```

相关声明：[sent_rx_callback_config](P089_sent_rx_callback_config_结构体.md)、[fast](#a0f4d0261c97b21430de9782e20d1c244)。

快速消息回调的配置。

## 90.2\_详细说明（Detailed Documentation）

<a id="a0f4d0261c97b21430de9782e20d1c244"></a>

### `fast`

```c
struct sent_rx_callback_config* sent_rx_callback_configs::fast
```

快速消息回调的配置。

<a id="a631882e363de3c8cc693336028561c1b"></a>

### `serial`

```c
struct sent_rx_callback_config* sent_rx_callback_configs::serial
```

串行消息回调的配置。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sent/sent.h`

## 90.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sent/sent.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sent_2sent_8h_source.html)
- [sent_rx_callback_config](P089_sent_rx_callback_config_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P089_sent_rx_callback_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P091_smbus_callback_结构体.md)
