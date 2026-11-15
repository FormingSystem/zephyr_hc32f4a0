---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-96
title: bt_l2cap_br_chan_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__chan.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第96章\_bt\_l2cap\_br\_chan\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__chan.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基本速率/增强数据速率（BR/EDR）的L2CAP信道结构。

```c
#include <zephyr/bluetooth/l2cap.h>
```

<a id="details"></a>

基本速率/增强数据速率（BR/EDR）的L2CAP信道结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 96.1\_数据成员（Data Fields）

<a id="r_a28ed2b2541697390c325c706d4ad8f0b"></a>

```c
struct bt_l2cap_chan chan
```

相关声明：[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)、[chan](#a28ed2b2541697390c325c706d4ad8f0b)。

通用 L2CAP 通道引用对象。

<a id="r_a00d49d2d73f2dafdc73a9f7b9393b98d"></a>

```c
struct bt_l2cap_br_endpoint rx
```

相关声明：[bt_l2cap_br_endpoint](P099_bt_l2cap_br_endpoint_结构体.md)、[rx](#a00d49d2d73f2dafdc73a9f7b9393b98d)。

通道接收端点（Receiving Endpoint）。

<a id="r_a67aec1f3bef3afe689c164185bd77f98"></a>

```c
struct bt_l2cap_br_endpoint tx
```

相关声明：[bt_l2cap_br_endpoint](P099_bt_l2cap_br_endpoint_结构体.md)、[tx](#a67aec1f3bef3afe689c164185bd77f98)。

通道发送端点（Transmission Endpoint）。

<a id="r_a09ded589b7e1571fc5d021ceafa68b5f"></a>

```c
atomic_t flags [1]
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[flags](#a09ded589b7e1571fc5d021ceafa68b5f)。

<a id="r_a556858a2e539bd4d5ed2ae66f392dc74"></a>

```c
bt_l2cap_chan_state_t state
```

相关声明：[bt_l2cap_chan_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga5a80330e52ea0fa4ee3266094570bb16)、[state](#a556858a2e539bd4d5ed2ae66f392dc74)。

<a id="r_a1ca3ed81f6f8edafc2993941de4c9771"></a>

```c
uint16_t psm
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[psm](#a1ca3ed81f6f8edafc2993941de4c9771)。

要连接的远端协议/服务复用器（PSM）。

<a id="r_ace996412a41a168c37d60d5e4096dc94"></a>

```c
uint8_t ident
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ident](#ace996412a41a168c37d60d5e4096dc94)。

在基于信用的连接（CoC）期间帮助匹配请求上下文。

<a id="r_a19bb2e243fb616b73d8b082df7c4a394"></a>

```c
bt_security_t required_sec_level
```

相关声明：[bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)、[required_sec_level](#a19bb2e243fb616b73d8b082df7c4a394)。

<a id="r_a0e637544c14d7d2b0ccd2af5424555fb"></a>

```c
struct k_work_delayable rtx_work
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[rtx_work](#a0e637544c14d7d2b0ccd2af5424555fb)。

<a id="r_a21224ab26501eca21aaed468681d6274"></a>

```c
struct k_work_sync rtx_sync
```

相关声明：[k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)、[rtx_sync](#a21224ab26501eca21aaed468681d6274)。

<a id="r_a96cb3a6bb3f3c97372c314eb1bfca32b"></a>

```c
struct bt_l2cap_br_window tx_win [CONFIG_BT_L2CAP_MAX_WINDOW_SIZE]
```

相关声明：[bt_l2cap_br_window](P100_bt_l2cap_br_window_结构体.md)、[tx_win](#a96cb3a6bb3f3c97372c314eb1bfca32b)。

<a id="r_ad4c352f1d43dce110ddf47c665b7ae17"></a>

```c
uint16_t tx_seq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_seq](#ad4c352f1d43dce110ddf47c665b7ae17)。

<a id="r_a6e559e94251ce9ef1c7d139695adf7ef"></a>

```c
uint16_t next_tx_seq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[next_tx_seq](#a6e559e94251ce9ef1c7d139695adf7ef)。

<a id="r_ae48194e987caf3153738f3027ec7022d"></a>

```c
uint16_t expected_ack_seq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[expected_ack_seq](#ae48194e987caf3153738f3027ec7022d)。

<a id="r_afa3dcfc293485a09d76a67c30ee0acf8"></a>

```c
uint16_t req_seq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[req_seq](#afa3dcfc293485a09d76a67c30ee0acf8)。

<a id="r_a734b9699538989fa8e5cec11eb84609e"></a>

```c
uint16_t expected_tx_seq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[expected_tx_seq](#a734b9699538989fa8e5cec11eb84609e)。

<a id="r_aa1fd44c5eb136e1fbd0f46f09d5fde0a"></a>

```c
uint16_t buffer_seq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[buffer_seq](#aa1fd44c5eb136e1fbd0f46f09d5fde0a)。

<a id="r_a3f9621b9d02b70f1dc9492520ff7cd03"></a>

```c
uint16_t retry_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[retry_count](#a3f9621b9d02b70f1dc9492520ff7cd03)。

<a id="r_a97266be01c9ee7e5f64f182173d50418"></a>

```c
uint16_t srej_save_req_seq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[srej_save_req_seq](#a97266be01c9ee7e5f64f182173d50418)。

<a id="r_a6a1788de2f5c037b46070a65c2a1111d"></a>

```c
struct k_work_delayable ret_work
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[ret_work](#a6a1788de2f5c037b46070a65c2a1111d)。

<a id="r_ac887d3192240594de4d6cb8d4af9553b"></a>

```c
struct k_work_delayable monitor_work
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[monitor_work](#ac887d3192240594de4d6cb8d4af9553b)。

## 96.2\_详细说明（Detailed Documentation）

<a id="aa1fd44c5eb136e1fbd0f46f09d5fde0a"></a>

### `buffer_seq`

```c
uint16_t bt_l2cap_br_chan::buffer_seq
```

<a id="a28ed2b2541697390c325c706d4ad8f0b"></a>

### `chan`

```c
struct bt_l2cap_chan bt_l2cap_br_chan::chan
```

通用 L2CAP 通道引用对象。

<a id="ae48194e987caf3153738f3027ec7022d"></a>

### `expected_ack_seq`

```c
uint16_t bt_l2cap_br_chan::expected_ack_seq
```

<a id="a734b9699538989fa8e5cec11eb84609e"></a>

### `expected_tx_seq`

```c
uint16_t bt_l2cap_br_chan::expected_tx_seq
```

<a id="a09ded589b7e1571fc5d021ceafa68b5f"></a>

### `flags`

```c
atomic_t bt_l2cap_br_chan::flags[1]
```

<a id="ace996412a41a168c37d60d5e4096dc94"></a>

### `ident`

```c
uint8_t bt_l2cap_br_chan::ident
```

在基于信用的连接（CoC）期间帮助匹配请求上下文。

<a id="ac887d3192240594de4d6cb8d4af9553b"></a>

### `monitor_work`

```c
struct k_work_delayable bt_l2cap_br_chan::monitor_work
```

<a id="a6e559e94251ce9ef1c7d139695adf7ef"></a>

### `next_tx_seq`

```c
uint16_t bt_l2cap_br_chan::next_tx_seq
```

<a id="a1ca3ed81f6f8edafc2993941de4c9771"></a>

### `psm`

```c
uint16_t bt_l2cap_br_chan::psm
```

要连接的远端协议/服务复用器（PSM）。

<a id="afa3dcfc293485a09d76a67c30ee0acf8"></a>

### `req_seq`

```c
uint16_t bt_l2cap_br_chan::req_seq
```

<a id="a19bb2e243fb616b73d8b082df7c4a394"></a>

### `required_sec_level`

```c
bt_security_t bt_l2cap_br_chan::required_sec_level
```

<a id="a6a1788de2f5c037b46070a65c2a1111d"></a>

### `ret_work`

```c
struct k_work_delayable bt_l2cap_br_chan::ret_work
```

<a id="a3f9621b9d02b70f1dc9492520ff7cd03"></a>

### `retry_count`

```c
uint16_t bt_l2cap_br_chan::retry_count
```

<a id="a21224ab26501eca21aaed468681d6274"></a>

### `rtx_sync`

```c
struct k_work_sync bt_l2cap_br_chan::rtx_sync
```

<a id="a0e637544c14d7d2b0ccd2af5424555fb"></a>

### `rtx_work`

```c
struct k_work_delayable bt_l2cap_br_chan::rtx_work
```

<a id="a00d49d2d73f2dafdc73a9f7b9393b98d"></a>

### `rx`

```c
struct bt_l2cap_br_endpoint bt_l2cap_br_chan::rx
```

通道接收端点（Receiving Endpoint）。

<a id="a97266be01c9ee7e5f64f182173d50418"></a>

### `srej_save_req_seq`

```c
uint16_t bt_l2cap_br_chan::srej_save_req_seq
```

<a id="a556858a2e539bd4d5ed2ae66f392dc74"></a>

### `state`

```c
bt_l2cap_chan_state_t bt_l2cap_br_chan::state
```

<a id="a67aec1f3bef3afe689c164185bd77f98"></a>

### `tx`

```c
struct bt_l2cap_br_endpoint bt_l2cap_br_chan::tx
```

通道发送端点（Transmission Endpoint）。

<a id="ad4c352f1d43dce110ddf47c665b7ae17"></a>

### `tx_seq`

```c
uint16_t bt_l2cap_br_chan::tx_seq
```

<a id="a96cb3a6bb3f3c97372c314eb1bfca32b"></a>

### `tx_win`

```c
struct bt_l2cap_br_window bt_l2cap_br_chan::tx_win[CONFIG_BT_L2CAP_MAX_WINDOW_SIZE]
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/l2cap.h`

## 96.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h_source.html)
- [bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)
- [bt_l2cap_br_endpoint](P099_bt_l2cap_br_endpoint_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [bt_l2cap_chan_state_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga5a80330e52ea0fa4ee3266094570bb16)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [k_work_sync](../kernel_runtime_model_reference/P012_k_work_sync_结构体.md)
- [bt_l2cap_br_window](P100_bt_l2cap_br_window_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P095_bt_ias_client_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P097_bt_l2cap_br_connless_cb_结构体.md)
