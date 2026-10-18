---
id: learning.zephyr-docs.network-core-model-reference.page-187
title: wifi_status_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第187章\_wifi\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

命令与事件通用的Wi-Fi状态（Status）。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

命令与事件通用的Wi-Fi状态（Status）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 187.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_ae9fea679194c94cd5fcdc73fc2be989d"></a>

```c
int status
```

相关声明：[status](#aa1dbff8154400f8353693d387977008b)。

状态值（Status value）。

<a id="r_a56f0f3022c0b59c203e0455a1b323833"></a>

```c
enum wifi_conn_status conn_status
```

相关声明：[wifi_conn_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga86a5741e54aeb3e290142b0de217b8a8)、[conn_status](#a8f885e78366d0499e4ba8e15bef275ac)。

连接状态（Connection status）。

<a id="r_a30f4ed05192d1ad429a9693faf60fa67"></a>

```c
enum wifi_disconn_reason disconn_reason
```

相关声明：[wifi_disconn_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac782af0a60b202fd19597cabb7bd3a9a)、[disconn_reason](#aa04b5033d93274badd27f702af9830bc)。

断开连接原因状态（Disconnection reason status）。

<a id="r_a3551062761f030a6211846731188a3cb"></a>

```c
enum wifi_ap_status ap_status
```

相关声明：[wifi_ap_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaaf730bf76adc06434c7ac63bf0417884)、[ap_status](#a02f0fcc7ef57661ca95d0c99f045aef1)。

接入点状态（Access point status）。

<a id="r_a09c151ea393c9c1fa2cc9f5f75eab66a"></a>

```c
};
```

命令或事件特定状态（Command or event specific status）。

<a id="r_ac8a85738dcfa60dfaf502d86b8294f78"></a>

```c
uint16_t status_code
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[status_code](#ac8a85738dcfa60dfaf502d86b8294f78)。

最近一次认证响应帧（Authentication Response）或（重新）关联响应帧（(Re)Association Response）中的 IEEE 802.11 状态码（Status code）；不可用时为 `0`。

<a id="r_a8c63d5fecc9d532366c144b4dd7bb2ad"></a>

```c
uint16_t reason_code
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[reason_code](#a8c63d5fecc9d532366c144b4dd7bb2ad)。

最近一次解除认证帧（Deauthentication）或解除关联帧（Disassociation）中的 IEEE 802.11 原因码（Reason code）；不可用时为 `0`。

## 187.2\_详细说明（Detailed Documentation）

<a id="a09c151ea393c9c1fa2cc9f5f75eab66a"></a>

### `[union]`

```c
union { ... } wifi_status
```

命令或事件特定状态（Command or event specific status）。

<a id="a02f0fcc7ef57661ca95d0c99f045aef1"></a>

### `ap_status`

```c
enum wifi_ap_status wifi_status::ap_status
```

接入点状态（Access point status）。

<a id="a8f885e78366d0499e4ba8e15bef275ac"></a>

### `conn_status`

```c
enum wifi_conn_status wifi_status::conn_status
```

连接状态（Connection status）。

<a id="aa04b5033d93274badd27f702af9830bc"></a>

### `disconn_reason`

```c
enum wifi_disconn_reason wifi_status::disconn_reason
```

断开连接原因状态（Disconnection reason status）。

<a id="a8c63d5fecc9d532366c144b4dd7bb2ad"></a>

### `reason_code`

```c
uint16_t wifi_status::reason_code
```

最近一次解除认证帧（Deauthentication）或解除关联帧（Disassociation）中的 IEEE 802.11 原因码（Reason code）；不可用时为 `0`。

参见 IEEE Std 802.11-2020 表 9-90。

<a id="aa1dbff8154400f8353693d387977008b"></a>

### `status`

```c
int wifi_status::status
```

状态值（Status value）。

<a id="ac8a85738dcfa60dfaf502d86b8294f78"></a>

### `status_code`

```c
uint16_t wifi_status::status_code
```

最近一次认证响应帧（Authentication Response）或（重新）关联响应帧（(Re)Association Response）中的 IEEE 802.11 状态码（Status code）；不可用时为 `0`。

参见 IEEE Std 802.11-2020 表 9-50。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 187.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_conn_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga86a5741e54aeb3e290142b0de217b8a8)
- [wifi_disconn_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gac782af0a60b202fd19597cabb7bd3a9a)
- [wifi_ap_status](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaaf730bf76adc06434c7ac63bf0417884)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [wifi_status](P187_wifi_status_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P186_wifi_scan_result_结构体.md) · [返回大纲](大纲.md) · [下一章](P188_wifi_twt_flow_info_结构体.md)
