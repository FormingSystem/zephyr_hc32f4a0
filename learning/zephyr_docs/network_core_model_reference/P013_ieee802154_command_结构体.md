---
id: learning.zephyr-docs.network-core-model-reference.page-13
title: ieee802154_command_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__command.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_ieee802154\_command\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__command.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已解析的MAC命令帧（Command Frame）载荷。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

已解析的MAC命令帧载荷（Command Frame Payload）。命令载荷位于命令帧标识符（CFI）之后，见第7.5节。数据请求、PAN ID冲突通知、孤儿通知和信标请求除CFI外不携带附加载荷。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_a1bc60b61ef82a58d080b07c1a0b27626"></a>

```c
uint8_t cfi
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cfi](#a1bc60b61ef82a58d080b07c1a0b27626)。

命令帧标识符（Command Frame Identifier），见ieee802154_cfi。

```c
union {
```

<a id="r_aa552affcaf73c081f1a97054595efd4b"></a>

```c
struct ieee802154_cmd_assoc_req assoc_req
```

相关声明：[ieee802154_cmd_assoc_req](P009_ieee802154_cmd_assoc_req_结构体.md)、[assoc_req](#aa21a32878e544c284f6efb7c78ed079a)。

关联请求命令（Association Request Command）。

<a id="r_aa6d3ed87f06d61b48328ee384b958a83"></a>

```c
struct ieee802154_cmd_assoc_res assoc_res
```

相关声明：[ieee802154_cmd_assoc_res](P010_ieee802154_cmd_assoc_res_结构体.md)、[assoc_res](#addbd05e3e770199f71ecf20dd0b716a9)。

关联响应命令（Association Response Command）。

<a id="r_abfce07c33a099361d8e1a5690c76164e"></a>

```c
struct ieee802154_cmd_disassoc_note disassoc_note
```

相关声明：[ieee802154_cmd_disassoc_note](P012_ieee802154_cmd_disassoc_note_结构体.md)、[disassoc_note](#a61700791f0e2148e23836340cbf9d0b8)。

解除关联通知命令（Disassociation Notification Command）。

<a id="r_a8b7cc4371756d4322c7f70a8cee8b220"></a>

```c
struct ieee802154_cmd_coord_realign coord_realign
```

相关声明：[ieee802154_cmd_coord_realign](P011_ieee802154_cmd_coord_realign_结构体.md)、[coord_realign](#ae5b9b8f7dc12ac73d2b392052a60b48d)。

协调器重对齐命令（Coordinator Realignment Command）。

<a id="r_acf1b0c29f6a53934721f70f8311535b6"></a>

```c
struct ieee802154_gts_request gts_request
```

相关声明：[ieee802154_gts_request](P021_ieee802154_gts_request_结构体.md)、[gts_request](#a6ad0a1fa2c4985b10e35ac282d27e3d1)。

保证时隙请求命令（GTS Request Command）。

<a id="r_ab05d89a3661b13354b9b1c6ce2a430b1"></a>

```c
};
```

所选命令标识符对应的命令专用载荷（Command-Specific Payload）。

## 13.2\_详细说明（Detailed Documentation）

<a id="ab05d89a3661b13354b9b1c6ce2a430b1"></a>

### `[union]`

```c
union { ... } ieee802154_command
```

所选命令标识符对应的命令专用载荷（Command-Specific Payload）。

见第7.5节。

<a id="aa21a32878e544c284f6efb7c78ed079a"></a>

### `assoc_req`

```c
struct ieee802154_cmd_assoc_req ieee802154_command::assoc_req
```

关联请求命令（Association Request Command）。

<a id="addbd05e3e770199f71ecf20dd0b716a9"></a>

### `assoc_res`

```c
struct ieee802154_cmd_assoc_res ieee802154_command::assoc_res
```

关联响应命令（Association Response Command）。

<a id="a1bc60b61ef82a58d080b07c1a0b27626"></a>

### `cfi`

```c
uint8_t ieee802154_command::cfi
```

命令帧标识符（Command Frame Identifier），见ieee802154_cfi。

<a id="ae5b9b8f7dc12ac73d2b392052a60b48d"></a>

### `coord_realign`

```c
struct ieee802154_cmd_coord_realign ieee802154_command::coord_realign
```

协调器重对齐命令（Coordinator Realignment Command）。

<a id="a61700791f0e2148e23836340cbf9d0b8"></a>

### `disassoc_note`

```c
struct ieee802154_cmd_disassoc_note ieee802154_command::disassoc_note
```

解除关联通知命令（Disassociation Notification Command）。

<a id="a6ad0a1fa2c4985b10e35ac282d27e3d1"></a>

### `gts_request`

```c
struct ieee802154_gts_request ieee802154_command::gts_request
```

保证时隙请求命令（GTS Request Command）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [ieee802154_cfi](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a7efde78911de6991098ba5d837157199)
- [ieee802154_cmd_assoc_req](P009_ieee802154_cmd_assoc_req_结构体.md)
- [ieee802154_cmd_assoc_res](P010_ieee802154_cmd_assoc_res_结构体.md)
- [ieee802154_cmd_disassoc_note](P012_ieee802154_cmd_disassoc_note_结构体.md)
- [ieee802154_cmd_coord_realign](P011_ieee802154_cmd_coord_realign_结构体.md)
- [ieee802154_gts_request](P021_ieee802154_gts_request_结构体.md)
- [ieee802154_command](P013_ieee802154_command_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_ieee802154_cmd_disassoc_note_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_ieee802154_config_结构体.md)
