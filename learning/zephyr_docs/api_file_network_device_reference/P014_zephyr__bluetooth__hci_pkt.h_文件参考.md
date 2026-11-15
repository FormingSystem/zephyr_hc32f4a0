---
id: learning.zephyr-docs.api-file-network-device-reference.page-14
title: zephyr__bluetooth__hci_pkt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__pkt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_bluetooth\_\_hci\_pkt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hci__pkt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙HCI数据包辅助接口（Packet Helpers）。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/bluetooth/hci_types.h>
#include <zephyr/net_buf.h>
```

查看此文件的源码。

蓝牙HCI数据包辅助接口（Packet Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_bt_5Fhci_5Fpkt_5Fcmd_5Frsp"></a>

```c
struct bt_hci_pkt_cmd_rsp
```

相关声明：[bt_hci_pkt_cmd_rsp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md)。

已解码的 HCI 命令响应（Decoded HCI Command Response）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="r_ga97349aa18498cfd9a61817f1d149aa29"></a>

```c
#define BT_HCI_PKT_CMD_HDR_SIZE (sizeof(uint8_t) + BT_HCI_CMD_HDR_SIZE)
```

相关声明：[BT_HCI_PKT_CMD_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga97349aa18498cfd9a61817f1d149aa29)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[BT_HCI_CMD_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#acdf2b6de1459a7492415a8987ad9a896)。

HCI 命令数据包前缀（Prefix）的大小。

<a id="r_ga08079006c088d639abc45077c7a09532"></a>

```c
#define BT_HCI_PKT_CMD_SIZE(param_len)
```

相关声明：[BT_HCI_PKT_CMD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga08079006c088d639abc45077c7a09532)。

带有 `param_len` 字节参数的 HCI 命令数据包大小。

<a id="r_ga5c26db578cf6b427e7009fbbd692253e"></a>

```c
#define BT_HCI_PKT_CMD_DEFINE(_name, _max_param_len)
```

相关声明：[BT_HCI_PKT_CMD_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga5c26db578cf6b427e7009fbbd692253e)。

定义用于 HCI 命令数据包的缓冲区（Buffer）。

<a id="r_ga0cc8ce4451e316f72cceda47c3a68b10"></a>

```c
#define BT_HCI_PKT_CMD_DEFINE_STATIC(_name, _max_param_len)
```

相关声明：[BT_HCI_PKT_CMD_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga0cc8ce4451e316f72cceda47c3a68b10)。

定义用于 HCI 命令数据包的静态缓冲区（Static Buffer）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.3\_函数（Functions）

<a id="r_ga7f6c2d3674275bb9ce6752cf3f7e3228"></a>

```c
void bt_hci_pkt_reset_cmd (struct net_buf_simple *buf)
```

相关声明：[bt_hci_pkt_reset_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga7f6c2d3674275bb9ce6752cf3f7e3228)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

为新的 HCI 命令数据包重置缓冲区（Reset Buffer）。

<a id="r_gac9d4ade374ccf35895cf601cdd6b3f79"></a>

```c
int bt_hci_pkt_push_cmd_hdr (struct net_buf_simple *buf, uint16_t opcode)
```

相关声明：[bt_hci_pkt_push_cmd_hdr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#gac9d4ade374ccf35895cf601cdd6b3f79)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

压入 HCI 命令数据包的包指示符（Packet Indicator）和命令头（Command Header）。

<a id="r_ga5494d5cdc68840408f6b4b254dd474c9"></a>

```c
int bt_hci_pkt_pull_cmd_complete (struct net_buf_simple *buf, struct bt_hci_pkt_cmd_rsp *rsp)
```

相关声明：[bt_hci_pkt_pull_cmd_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga5494d5cdc68840408f6b4b254dd474c9)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_hci_pkt_cmd_rsp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md)。

取出 `HCI_Command_Complete` 事件。

<a id="r_ga591c10d3d94a29be93ff5c4eb690201f"></a>

```c
int bt_hci_pkt_pull_cmd_status (struct net_buf_simple *buf, struct bt_hci_pkt_cmd_rsp *rsp)
```

相关声明：[bt_hci_pkt_pull_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga591c10d3d94a29be93ff5c4eb690201f)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_hci_pkt_cmd_rsp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md)。

取出 `HCI_Command_Status` 事件。

<a id="r_ga588ed90a133f526c4abfa3fcd87ad8e5"></a>

```c
int bt_hci_pkt_parse_cmd_rsp (const uint8_t *pkt, size_t len, struct bt_hci_pkt_cmd_rsp *rsp)
```

相关声明：[bt_hci_pkt_parse_cmd_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga588ed90a133f526c4abfa3fcd87ad8e5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_hci_pkt_cmd_rsp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md)。

从完整 HCI 数据包中解析 HCI 命令响应（Command Response）。


## 14.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/hci_types.h](../api_source_hci_multifunction_reference/P001_hci_types.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P311_hci_pkt.h_源码浏览.md)
- [bt_hci_pkt_cmd_rsp](../bluetooth_hci_model_reference/P333_bt_hci_pkt_cmd_rsp_结构体.md)
- [BT_HCI_PKT_CMD_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga97349aa18498cfd9a61817f1d149aa29)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_HCI_CMD_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#acdf2b6de1459a7492415a8987ad9a896)
- [BT_HCI_PKT_CMD_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga08079006c088d639abc45077c7a09532)
- [BT_HCI_PKT_CMD_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga5c26db578cf6b427e7009fbbd692253e)
- [BT_HCI_PKT_CMD_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga0cc8ce4451e316f72cceda47c3a68b10)
- [bt_hci_pkt_reset_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga7f6c2d3674275bb9ce6752cf3f7e3228)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_hci_pkt_push_cmd_hdr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#gac9d4ade374ccf35895cf601cdd6b3f79)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_hci_pkt_pull_cmd_complete](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga5494d5cdc68840408f6b4b254dd474c9)
- [bt_hci_pkt_pull_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga591c10d3d94a29be93ff5c4eb690201f)
- [bt_hci_pkt_parse_cmd_rsp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html#ga588ed90a133f526c4abfa3fcd87ad8e5)

<a id="header-details"></a>

---

[上一章](P013_zephyr__xen__gnttab.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__net__http__server.h_文件参考.md)
