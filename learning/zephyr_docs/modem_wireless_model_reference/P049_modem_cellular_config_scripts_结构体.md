---
id: learning.zephyr-docs.modem-wireless-model-reference.page-49
title: modem_cellular_config_scripts_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cellular__config__scripts.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_modem\_cellular\_config\_scripts\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__cellular__config__scripts.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蜂窝调制解调器（Cellular Modem）的交互脚本（Chat Scripts）。

```c
#include <zephyr/drivers/modem/modem_cellular.h>
```

<a id="details"></a>

蜂窝调制解调器的交互脚本（Chat scripts）。只有初始化（init）脚本和拨号（dial）脚本是必需的，其他脚本均可选。如果提供了网络（network）脚本，会先用它等待网络注册，然后执行拨号脚本；如果未提供网络脚本，则要求拨号脚本配置网络注册，调制解调器会在拨号脚本完成后等待注册。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

<a id="r_a3f9a561d25bbabe27e0dc5920eb9eed5"></a>

```c
const struct modem_chat_script * set_baudrate
```

相关声明：[modem_chat_script](P055_modem_chat_script_结构体.md)、[set_baudrate](#a3f9a561d25bbabe27e0dc5920eb9eed5)。

可选脚本，用于配置调制解调器的 UART 波特率。

<a id="r_ae52b436497e5250c7df4ed18d4819436"></a>

```c
const struct modem_chat_script * init
```

相关声明：[modem_chat_script](P055_modem_chat_script_结构体.md)、[init](#ae52b436497e5250c7df4ed18d4819436)。

初始化调制解调器并启用 CMUX 的脚本。

<a id="r_a1d1e340cef1848413eb9269094d4502d"></a>

```c
const struct modem_chat_script * network
```

相关声明：[modem_chat_script](P055_modem_chat_script_结构体.md)、[network](#a1d1e340cef1848413eb9269094d4502d)。

可选脚本，在拨号前等待网络注册。

<a id="r_a1a7cd1d3932f81ef30714d4d9d50e2ee"></a>

```c
const struct modem_chat_script * dial
```

相关声明：[modem_chat_script](P055_modem_chat_script_结构体.md)、[dial](#a1a7cd1d3932f81ef30714d4d9d50e2ee)。

启动点对点协议（PPP）数据连接的脚本。

<a id="r_a10d764e69608d3cf70178eaa9f82cb86"></a>

```c
const struct modem_chat_script * periodic
```

相关声明：[modem_chat_script](P055_modem_chat_script_结构体.md)、[periodic](#a10d764e69608d3cf70178eaa9f82cb86)。

可选脚本，在已注册期间周期性轮询调制解调器状态。

<a id="r_a900207cd3ef0a6003fad53a7d47773ee"></a>

```c
const struct modem_chat_script * shutdown
```

相关声明：[modem_chat_script](P055_modem_chat_script_结构体.md)、[shutdown](#a900207cd3ef0a6003fad53a7d47773ee)。

可选脚本，为调制解调器关机作准备。

<a id="r_ae92a8fb7e262369c1110d9a47a54a6ca"></a>

```c
const struct modem_chat_script * dlci_setup
```

相关声明：[modem_chat_script](P055_modem_chat_script_结构体.md)、[dlci_setup](#ae92a8fb7e262369c1110d9a47a54a6ca)。

可选脚本，在数据链路连接标识符（DLCI）通道打开后进行配置。

## 49.2\_详细说明（Detailed Documentation）

<a id="a1a7cd1d3932f81ef30714d4d9d50e2ee"></a>

### `dial`

```c
const struct modem_chat_script* modem_cellular_config_scripts::dial
```

启动点对点协议（PPP）数据连接的脚本。

不得为 `NULL`。

<a id="ae92a8fb7e262369c1110d9a47a54a6ca"></a>

### `dlci_setup`

```c
const struct modem_chat_script* modem_cellular_config_scripts::dlci_setup
```

可选脚本，在数据链路连接标识符（DLCI）通道打开后进行配置。

<a id="ae52b436497e5250c7df4ed18d4819436"></a>

### `init`

```c
const struct modem_chat_script* modem_cellular_config_scripts::init
```

初始化调制解调器并启用 CMUX 的脚本。

不得为 `NULL`。

<a id="a1d1e340cef1848413eb9269094d4502d"></a>

### `network`

```c
const struct modem_chat_script* modem_cellular_config_scripts::network
```

可选脚本，在拨号前等待网络注册。

<a id="a10d764e69608d3cf70178eaa9f82cb86"></a>

### `periodic`

```c
const struct modem_chat_script* modem_cellular_config_scripts::periodic
```

可选脚本，在已注册期间周期性轮询调制解调器状态。

<a id="a3f9a561d25bbabe27e0dc5920eb9eed5"></a>

### `set_baudrate`

```c
const struct modem_chat_script* modem_cellular_config_scripts::set_baudrate
```

可选脚本，用于配置调制解调器的 UART 波特率。

<a id="a900207cd3ef0a6003fad53a7d47773ee"></a>

### `shutdown`

```c
const struct modem_chat_script* modem_cellular_config_scripts::shutdown
```

可选脚本，为调制解调器关机作准备。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/modem_cellular.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/modem_cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/modem__cellular_8h_source.html)
- [modem_chat_script](P055_modem_chat_script_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_modem_cellular_board_init_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_modem_cellular_data_结构体.md)
