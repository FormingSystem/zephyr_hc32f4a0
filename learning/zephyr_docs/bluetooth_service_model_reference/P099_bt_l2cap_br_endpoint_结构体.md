---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-99
title: bt_l2cap_br_endpoint_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__endpoint.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_bt\_l2cap\_br\_endpoint\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__endpoint.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基本速率/增强数据速率（BR/EDR）的L2CAP端点结构。

```c
#include <zephyr/bluetooth/l2cap.h>
```

<a id="details"></a>

基本速率/增强数据速率（BR/EDR）的L2CAP端点结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 99.1\_数据成员（Data Fields）

<a id="r_acbe4f6cc15bb20703fca53e7084b2ea7"></a>

```c
uint16_t cid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cid](#acbe4f6cc15bb20703fca53e7084b2ea7)。

端点通道标识符（Channel Identifier，CID）。

<a id="r_aaeb46128990fe08c926d34049bbc2d6a"></a>

```c
uint16_t mtu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mtu](#aaeb46128990fe08c926d34049bbc2d6a)。

端点最大传输单元（Maximum Transmission Unit，MTU）。

<a id="r_af49eacd8794e580adc285d95613547f6"></a>

```c
uint8_t mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode](#af49eacd8794e580adc285d95613547f6)。

端点链路模式（Link Mode）。

<a id="r_af64e45ea279960b3db213c9ad3e1828c"></a>

```c
bool optional
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[optional](#af64e45ea279960b3db213c9ad3e1828c)。

端点链路模式是否可选。如果 `optional` 为 `true`，则可根据扩展特性，以及 L2CAP 配置响应和请求中的对端配置，更改此模式。

<a id="r_a8c66377adf1681079fa446b05eff7e8a"></a>

```c
uint8_t max_transmit
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_transmit](#a8c66377adf1681079fa446b05eff7e8a)。

端点最大发送次数（Maximum Transmit）。此字段用于设置最大重传次数。

<a id="r_ae5cdb992cd40ce925863e05c7f647f5e"></a>

```c
uint16_t ret_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ret_timeout](#ae5cdb992cd40ce925863e05c7f647f5e)。

端点重传超时（Retransmission Timeout）。此字段由 `CONFIG_BT_L2CAP_BR_RET_TIMEOUT` 配置，其值不得大于 `monitor_timeout` 字段。

<a id="r_a4f272e96d31b00a3e50d8dcbc2303c57"></a>

```c
uint16_t monitor_timeout
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[monitor_timeout](#a4f272e96d31b00a3e50d8dcbc2303c57)。

端点监视超时（Monitor Timeout）。此字段由 `CONFIG_BT_L2CAP_BR_MONITOR_TIMEOUT` 配置。

<a id="r_ab5789c43d09f18f89bffdd829af90a7b"></a>

```c
uint16_t mps
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mps](#ab5789c43d09f18f89bffdd829af90a7b)。

端点最大协议数据单元（PDU）载荷大小。

<a id="r_a2b27b7017ddc68d5b8a597d4be45074c"></a>

```c
uint16_t max_window
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_window](#a2b27b7017ddc68d5b8a597d4be45074c)。

端点最大窗口大小（Maximum Window Size）。所支持的最大窗口大小由 `CONFIG_BT_L2CAP_MAX_WINDOW_SIZE` 配置。

<a id="r_ac63ef5c2ae54fbcce9380a379a551595"></a>

```c
uint8_t fcs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[fcs](#ac63ef5c2ae54fbcce9380a379a551595)。

端点帧校验序列（FCS）类型。取值定义为 `BT_L2CAP_BR_FCS_*`；默认设置应为 `BT_L2CAP_BR_FCS_16BIT`。

<a id="r_aba3184618ab6e8a3db1808041d3a0f8d"></a>

```c
bool extended_control
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[extended_control](#aba3184618ab6e8a3db1808041d3a0f8d)。

端点扩展控制（Extended Control）。

## 99.2\_详细说明（Detailed Documentation）

<a id="acbe4f6cc15bb20703fca53e7084b2ea7"></a>

### `cid`

```c
uint16_t bt_l2cap_br_endpoint::cid
```

端点通道标识符（Channel Identifier，CID）。

<a id="aba3184618ab6e8a3db1808041d3a0f8d"></a>

### `extended_control`

```c
bool bt_l2cap_br_endpoint::extended_control
```

端点扩展控制（Extended Control）。

如果此字段为 `true`，且双方均支持扩展窗口大小（Extended Window Size）特性，本端将在配置请求包中包含扩展窗口大小选项。

<a id="ac63ef5c2ae54fbcce9380a379a551595"></a>

### `fcs`

```c
uint8_t bt_l2cap_br_endpoint::fcs
```

端点帧校验序列（FCS）类型。取值定义为 `BT_L2CAP_BR_FCS_*`；默认设置应为 `BT_L2CAP_BR_FCS_16BIT`。

对于流控制（FC）和重传（RET）模式，FCS 类型应为 `BT_L2CAP_BR_FCS_16BIT`。对于增强重传（ERET）和流式（STREAM）模式，FCS 类型可选。如果此字段不是默认值，并且双方都支持 FCS 选项，本端将在配置请求包中包含 FCS 选项。

<a id="a8c66377adf1681079fa446b05eff7e8a"></a>

### `max_transmit`

```c
uint8_t bt_l2cap_br_endpoint::max_transmit
```

端点最大发送次数（Maximum Transmit）。此字段用于设置最大重传次数。

对于 RET、FC 和 ERET 模式，此值不得小于 1；对于 STREAM 模式，此值应为 0。

<a id="a2b27b7017ddc68d5b8a597d4be45074c"></a>

### `max_window`

```c
uint16_t bt_l2cap_br_endpoint::max_window
```

端点最大窗口大小（Maximum Window Size）。所支持的最大窗口大小由 `CONFIG_BT_L2CAP_MAX_WINDOW_SIZE` 配置。

此字段不得大于 `CONFIG_BT_L2CAP_MAX_WINDOW_SIZE`。

<a id="af49eacd8794e580adc285d95613547f6"></a>

### `mode`

```c
uint8_t bt_l2cap_br_endpoint::mode
```

端点链路模式（Link Mode）。

取值定义为 `BT_L2CAP_BR_LINK_MODE_*`。

<a id="a4f272e96d31b00a3e50d8dcbc2303c57"></a>

### `monitor_timeout`

```c
uint16_t bt_l2cap_br_endpoint::monitor_timeout
```

端点监视超时（Monitor Timeout）。此字段由 `CONFIG_BT_L2CAP_BR_MONITOR_TIMEOUT` 配置。

<a id="ab5789c43d09f18f89bffdd829af90a7b"></a>

### `mps`

```c
uint16_t bt_l2cap_br_endpoint::mps
```

端点最大协议数据单元（PDU）载荷大小。

<a id="aaeb46128990fe08c926d34049bbc2d6a"></a>

### `mtu`

```c
uint16_t bt_l2cap_br_endpoint::mtu
```

端点最大传输单元（Maximum Transmission Unit，MTU）。

<a id="af64e45ea279960b3db213c9ad3e1828c"></a>

### `optional`

```c
bool bt_l2cap_br_endpoint::optional
```

端点链路模式是否可选。如果 `optional` 为 `true`，则可根据扩展特性，以及 L2CAP 配置响应和请求中的对端配置，更改此模式。

否则，如果通道配置过程无法满足所设置的模式，将断开 L2CAP 通道。

<a id="ae5cdb992cd40ce925863e05c7f647f5e"></a>

### `ret_timeout`

```c
uint16_t bt_l2cap_br_endpoint::ret_timeout
```

端点重传超时（Retransmission Timeout）。此字段由 `CONFIG_BT_L2CAP_BR_RET_TIMEOUT` 配置，其值不得大于 `monitor_timeout` 字段。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/l2cap.h`

## 99.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [CONFIG_BT_L2CAP_BR_RET_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_BR_RET_TIMEOUT)
- [CONFIG_BT_L2CAP_BR_MONITOR_TIMEOUT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_BR_MONITOR_TIMEOUT)
- [CONFIG_BT_L2CAP_MAX_WINDOW_SIZE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_MAX_WINDOW_SIZE)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P098_bt_l2cap_br_echo_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P100_bt_l2cap_br_window_结构体.md)
