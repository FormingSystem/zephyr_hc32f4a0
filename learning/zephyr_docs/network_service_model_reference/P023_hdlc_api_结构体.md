---
id: learning.zephyr-docs.network-service-model-reference.page-23
title: hdlc_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhdlc__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_hdlc\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhdlc__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

高级数据链路控制（HDLC）接口的配置数据。

```c
#include <zephyr/net/hdlc_rcp_if/hdlc_rcp_if.h>
```

<a id="details"></a>

高级数据链路控制（HDLC）接口的配置数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_abeb64661526d0a3e241e6515707284de"></a>

```c
struct net_if_api iface_api
```

相关声明：[iface_api](#abeb64661526d0a3e241e6515707284de)。

高级数据链路控制（HDLC）接口 API。

<a id="r_a2b18e7cd6dc393769b3d3ad2c8bf63ed"></a>

```c
int(* register_rx_cb )(hdlc_rx_callback_t hdlc_rx_callback, void *param)
```

相关声明：[register_rx_cb](#a2b18e7cd6dc393769b3d3ad2c8bf63ed)、[hdlc_rx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/hdlc__rcp__if_8h.html#a31b4a1434d2faad2878344367caf1b53)。

注册 Spinel HDLC 接收（RX）回调。

<a id="r_a5a1958253b254008cd142c2c3ab33d2a"></a>

```c
int(* send )(const uint8_t *frame, uint16_t length)
```

相关声明：[send](#a5a1958253b254008cd142c2c3ab33d2a)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

发送一个 HDLC 帧。

<a id="r_a33486d7c73df2958bf89bfe500b27464"></a>

```c
int(* deinit )(void)
```

相关声明：[deinit](#a33486d7c73df2958bf89bfe500b27464)。

反初始化设备（Deinitialize）。

<a id="r_ac9054a3a7bf0b2e364857334a62e4c08"></a>

```c
int(* deferred_init )(void)
```

相关声明：[deferred_init](#ac9054a3a7bf0b2e364857334a62e4c08)。

可选：在延迟初始化（deferred init）模式下完成无线协处理器（RCP）接口初始化。

## 23.2\_详细说明（Detailed Documentation）

<a id="ac9054a3a7bf0b2e364857334a62e4c08"></a>

### `deferred_init`

```c
int(* hdlc_api::deferred_init) (void)
```

可选：在延迟初始化（deferred init）模式下完成无线协处理器（RCP）接口初始化。

如果为 `NULL`，接口在初始化时自动启动。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 接口已成功启动。 |
| `-EIO` | 接口无法启动。 |

<a id="a33486d7c73df2958bf89bfe500b27464"></a>

### `deinit`

```c
int(* hdlc_api::deinit) (void)
```

反初始化设备（Deinitialize）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 接口已成功停止。 |
| `-EIO` | 接口无法停止。 |

<a id="abeb64661526d0a3e241e6515707284de"></a>

### `iface_api`

```c
struct net_if_api hdlc_api::iface_api
```

高级数据链路控制（HDLC）接口 API。

<a id="a2b18e7cd6dc393769b3d3ad2c8bf63ed"></a>

### `register_rx_cb`

```c
int(* hdlc_api::register_rx_cb) (hdlc_rx_callback_t hdlc_rx_callback, void *param)
```

注册 Spinel HDLC 接收（RX）回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hdlc_rx_callback` | 指向 Spinel HDLC 接收回调的指针。 |
| `param` | 指向 Spinel HDLC 接口的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 回调已成功注册。 |
| `-EIO` | 回调无法注册。 |

<a id="a5a1958253b254008cd142c2c3ab33d2a"></a>

### `send`

```c
int(* hdlc_api::send) (const uint8_t *frame, uint16_t length)
```

发送一个 HDLC 帧。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `frame` | 指向待发送 HDLC 帧的指针。 |
| `length` | 待发送 HDLC 帧的长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 帧已成功发送。 |
| `-EIO` | 由于某个未具体指明的接口错误，例如接口忙，无法发送此帧。 |

本数据类型文档由以下文件生成：

- `zephyr/net/hdlc_rcp_if/hdlc_rcp_if.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/net/hdlc_rcp_if/hdlc_rcp_if.h](https://docs.zephyrproject.org/latest/doxygen/html/hdlc__rcp__if_8h_source.html)
- [hdlc_rx_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/hdlc__rcp__if_8h.html#a31b4a1434d2faad2878344367caf1b53)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_hci_cp_le_conn_update_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_http2_settings_field_结构体.md)
