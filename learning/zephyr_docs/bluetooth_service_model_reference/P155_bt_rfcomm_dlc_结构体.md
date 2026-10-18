---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-155
title: bt_rfcomm_dlc_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__rfcomm__dlc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第155章\_bt\_rfcomm\_dlc\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__rfcomm__dlc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RFCOMM数据链路连接（DLC）结构。

```c
#include <zephyr/bluetooth/classic/rfcomm.h>
```

<a id="details"></a>

RFCOMM数据链路连接（DLC）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 155.1\_数据成员（Data Fields）

<a id="r_a0054c0b539b947688555b5663c585bb7"></a>

```c
struct bt_rfcomm_dlc_ops * ops
```

相关声明：[bt_rfcomm_dlc_ops](P156_bt_rfcomm_dlc_ops_结构体.md)、[ops](#a0054c0b539b947688555b5663c585bb7)。

指向此数据链路连接（DLC）的应用回调操作的指针。

<a id="r_ab298ebd444566533018eabdc5a69c8ba"></a>

```c
bt_security_t required_sec_level
```

相关声明：[bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)、[required_sec_level](#ab298ebd444566533018eabdc5a69c8ba)。

建立此 DLC 之前所需的最低安全级别。

<a id="r_a2334abbaacad9b98c2cb2c5650644854"></a>

```c
uint16_t mtu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mtu](#a2334abbaacad9b98c2cb2c5650644854)。

此 DLC 的最大传输单元（MTU），以字节为单位。

<a id="r_a27157f693d91aac6aaafe1bd70593404"></a>

```c
uint8_t rx_credit_limit
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_credit_limit](#a27157f693d91aac6aaafe1bd70593404)。

此 DLC 请求的初始接收信用数（receive credits）。

## 155.2\_详细说明（Detailed Documentation）

<a id="a2334abbaacad9b98c2cb2c5650644854"></a>

### `mtu`

```c
uint16_t bt_rfcomm_dlc::mtu
```

此 DLC 的最大传输单元（MTU），以字节为单位。

在参数协商（Parameter Negotiation，PN）过程中协商。传给 `bt_rfcomm_dlc_send` 的发送缓冲区不得超过此值。

<a id="a0054c0b539b947688555b5663c585bb7"></a>

### `ops`

```c
struct bt_rfcomm_dlc_ops* bt_rfcomm_dlc::ops
```

指向此数据链路连接（DLC）的应用回调操作的指针。

<a id="ab298ebd444566533018eabdc5a69c8ba"></a>

### `required_sec_level`

```c
bt_security_t bt_rfcomm_dlc::required_sec_level
```

建立此 DLC 之前所需的最低安全级别。

<a id="a27157f693d91aac6aaafe1bd70593404"></a>

### `rx_credit_limit`

```c
uint8_t bt_rfcomm_dlc::rx_credit_limit
```

此 DLC 请求的初始接收信用数（receive credits）。

设置 DLC 建立后本端愿意从远端接收的无编号信息头（UIH）帧数。协议栈在使用前将此值限制为 `MIN((BT_BUF_ACL_RX_COUNT - 1), 255)`。如果字段为 0，协议栈使用内部默认值 `MIN((BT_BUF_ACL_RX_COUNT - 1), 255)`。结果会写回此字段。此外，在参数协商（PN）命令或响应中发送时，此字段的值还会限制为 7。

仅在启用基于信用的流控制（CFC）时有意义。

**说明（Note）**：注意：如果值超过 `MIN((BT_BUF_ACL_RX_COUNT - 1), 255)`，则会被限制为 `MIN((BT_BUF_ACL_RX_COUNT - 1), 255)`。只有 DLC 处于未连接状态时才能修改此字段。这意味着从 `bt_rfcomm_server::accept` 返回开始，直到调用 `bt_rfcomm_dlc_ops::disconnected` 之前，都不能再修改。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/rfcomm.h`

## 155.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/rfcomm.h](https://docs.zephyrproject.org/latest/doxygen/html/rfcomm_8h_source.html)
- [bt_rfcomm_dlc_ops](P156_bt_rfcomm_dlc_ops_结构体.md)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_rfcomm_dlc_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html#ga593841aef52027598977b7b2bbd0237d)
- [bt_rfcomm_server::accept](P158_bt_rfcomm_server_结构体.md#ac08708bb8161f787737962f62d3c003f)
- [bt_rfcomm_dlc_ops::disconnected](P156_bt_rfcomm_dlc_ops_结构体.md#a4eeaf7b5db6c93e846a72797e6612d30)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P154_bt_pbap_pse_rfcomm_结构体.md) · [返回大纲](大纲.md) · [下一章](P156_bt_rfcomm_dlc_ops_结构体.md)
