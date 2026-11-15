---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-333
title: bt_hci_pkt_cmd_rsp_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__pkt__cmd__rsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第333章\_bt\_hci\_pkt\_cmd\_rsp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__pkt__cmd__rsp.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

已解码的 HCI 命令响应（Decoded HCI Command Response）。

```c
#include <zephyr/bluetooth/hci_pkt.h>
```

<a id="details"></a>

已解码的 HCI 命令响应。由 `bt_hci_pkt_pull_cmd_complete()`、`bt_hci_pkt_pull_cmd_status()` 和 `bt_hci_pkt_parse_cmd_rsp()` 根据 `HCI_Command_Complete` 或 `HCI_Command_Status` 事件填充。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 333.1\_数据成员（Data Fields）

<a id="r_a28f51c385cac564330fef45c3fca84cc"></a>

```c
uint16_t opcode
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[opcode](#a28f51c385cac564330fef45c3fca84cc)。

该事件所响应命令的操作码（Opcode）。

<a id="r_a2a276baa7340943d9b72ae59f85b86db"></a>

```c
uint8_t ncmd
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ncmd](#a2a276baa7340943d9b72ae59f85b86db)。

`Num_HCI_Command_Packets`，即控制器可接受的 HCI 命令包数量。

<a id="r_a0f381a50b06e919ee4b66d7781750ee4"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a0f381a50b06e919ee4b66d7781750ee4)。

状态码（`BT_HCI_ERR_*`）。

<a id="r_a16a24c4f86c12dcb5fba854609b9bb96"></a>

```c
const uint8_t * rp
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rp](#a16a24c4f86c12dcb5fba854609b9bb96)。

命令的返回参数（Return Parameters）。

<a id="r_a51769d2ade34c7563fb30c1a31cf26b0"></a>

```c
size_t rp_len
```

相关声明：[rp_len](#a51769d2ade34c7563fb30c1a31cf26b0)。

`rp` 的长度，单位为字节。

## 333.2\_详细说明（Detailed Documentation）

<a id="a2a276baa7340943d9b72ae59f85b86db"></a>

### `ncmd`

```c
uint8_t bt_hci_pkt_cmd_rsp::ncmd
```

`Num_HCI_Command_Packets`，即控制器可接受的 HCI 命令包数量。

控制器还能接受的 HCI 命令包数量。

<a id="a28f51c385cac564330fef45c3fca84cc"></a>

### `opcode`

```c
uint16_t bt_hci_pkt_cmd_rsp::opcode
```

该事件所响应命令的操作码（Opcode）。

事件不响应任何命令、仅更新控制器可接受的命令包数量时，使用 `BT_OP_NOP`。

<a id="a16a24c4f86c12dcb5fba854609b9bb96"></a>

### `rp`

```c
const uint8_t* bt_hci_pkt_cmd_rsp::rp
```

命令的返回参数（Return Parameters）。

指向已解码事件内部，以状态值开头，与 `bt_hci_rp_*` 结构体相同。`HCI_Command_Status` 不携带返回参数：此时 `rp_len` 为 0，`rp` 指向事件参数之后的紧邻位置，使零长度复制仍具有明确行为。

<a id="a51769d2ade34c7563fb30c1a31cf26b0"></a>

### `rp_len`

```c
size_t bt_hci_pkt_cmd_rsp::rp_len
```

`rp` 的长度，单位为字节。

<a id="a0f381a50b06e919ee4b66d7781750ee4"></a>

### `status`

```c
uint8_t bt_hci_pkt_cmd_rsp::status
```

状态码（`BT_HCI_ERR_*`）。

对于 `HCI_Command_Complete`，这是第一个返回参数。仅当 `opcode` 不是 `BT_OP_NOP` 时才有意义；`BT_OP_NOP` 事件不响应任何命令，也不携带状态，此时该字段为 `BT_HCI_ERR_SUCCESS`。应先匹配 `opcode` 再使用此状态。如果某个命令的 `HCI_Command_Complete` 缺少返回参数开头应有的状态值，解码器会报告 `-ENODATA`，并将该字段设为 `BT_HCI_ERR_UNSPECIFIED`。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_pkt.h`

## 333.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__pkt_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_pkt_pull_cmd_complete()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga5494d5cdc68840408f6b4b254dd474c9)
- [bt_hci_pkt_pull_cmd_status()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga591c10d3d94a29be93ff5c4eb690201f)
- [bt_hci_pkt_parse_cmd_rsp()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga588ed90a133f526c4abfa3fcd87ad8e5)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P332_bt_hci_op_le_set_default_rate_parameters_结构体.md) · [返回大纲](大纲.md) · [下一章](P334_bt_hci_rp_configure_data_path_结构体.md)
