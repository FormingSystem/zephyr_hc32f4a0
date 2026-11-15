---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-2
title: 大型组成数据客户端模型（Large Composition Data Client model）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_大型组成数据客户端模型（Large Composition Data Client model）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 2.1\_文件（Files）

<a id="r_large_5Fcomp_5Fdata_5Fcli_2Eh"></a>

```c
file large_comp_data_cli.h
```

相关声明：[large_comp_data_cli.h](../api_file_runtime_reference/P032_zephyr__bluetooth__mesh__large_comp_data_cli.h_文件参考.md)。

蓝牙Mesh大型组成数据客户端（Large Composition Data Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.2\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Flarge_5Fcomp_5Fdata_5Frsp"></a>

```c
struct bt_mesh_large_comp_data_rsp
```

相关声明：[bt_mesh_large_comp_data_rsp](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md)。

大型组成数据（Large Composition Data）的响应。

<a id="r_bt_5Fmesh_5Flarge_5Fcomp_5Fdata_5Fcli_5Fcb"></a>

```c
struct bt_mesh_large_comp_data_cli_cb
```

相关声明：[bt_mesh_large_comp_data_cli_cb](../bluetooth_mesh_model_reference/P070_bt_mesh_large_comp_data_cli_cb_结构体.md)。

大型组成数据状态（Large Composition Data Status）消息的回调。

<a id="r_bt_5Fmesh_5Flarge_5Fcomp_5Fdata_5Fcli"></a>

```c
struct bt_mesh_large_comp_data_cli
```

相关声明：[bt_mesh_large_comp_data_cli](../bluetooth_mesh_model_reference/P069_bt_mesh_large_comp_data_cli_结构体.md)。

大型组成数据客户端（Large Composition Data Client）的模型上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.3\_宏定义（Macros）

<a id="r_ga5860da397d1cd830e8010946c5b32f1e"></a>

```c
#define BT_MESH_MODEL_LARGE_COMP_DATA_CLI(cli_data)
```

相关声明：[BT_MESH_MODEL_LARGE_COMP_DATA_CLI](#ga5860da397d1cd830e8010946c5b32f1e)。

大型组成数据客户端模型（Large Composition Data Client Model）的组成数据条目（Composition Data Entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_gaf505ee14246746fc245a34328443d1c6"></a>

```c
int bt_mesh_large_comp_data_get (uint16_t net_idx, uint16_t addr, uint8_t page, size_t offset, struct bt_mesh_large_comp_data_rsp *rsp)
```

相关声明：[bt_mesh_large_comp_data_get](#gaf505ee14246746fc245a34328443d1c6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_large_comp_data_rsp](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md)。

发送大型组成数据获取消息（Large Composition Data Get Message）。

<a id="r_ga4073eb48c43460804705d80ac0919864"></a>

```c
int bt_mesh_models_metadata_get (uint16_t net_idx, uint16_t addr, uint8_t page, size_t offset, struct bt_mesh_large_comp_data_rsp *rsp)
```

相关声明：[bt_mesh_models_metadata_get](#ga4073eb48c43460804705d80ac0919864)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_large_comp_data_rsp](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md)。

发送模型元数据获取消息（Models Metadata Get Message）。

## 2.5\_详细说明（Detailed Documentation）

<a id="ga5860da397d1cd830e8010946c5b32f1e"></a>

### `BT_MESH_MODEL_LARGE_COMP_DATA_CLI`

```c
#define BT_MESH_MODEL_LARGE_COMP_DATA_CLI ( cli_data)
```

```c
#include <zephyr/bluetooth/mesh/large_comp_data_cli.h>
```

展开值（Value）：

```c
BT_MESH_MODEL_CB(BT_MESH_MODEL_ID_LARGE_COMP_DATA_CLI,                                     \
                 _bt_mesh_large_comp_data_cli_op, NULL, cli_data,                          \
                 &_bt_mesh_large_comp_data_cli_cb)
```

大型组成数据客户端模型（Large Composition Data Client Model）的组成数据条目（Composition Data Entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cli_data` | 指向大型组合数据客户端模型（Large Composition Data Client Model）实例的指针。 |

<a id="gaf505ee14246746fc245a34328443d1c6"></a>

### `bt_mesh_large_comp_data_get()`

```c
int bt_mesh_large_comp_data_get ( uint16_t net_idx, uint16_t addr, uint8_t page, size_t offset, struct bt_mesh_large_comp_data_rsp * rsp )
```

```c
#include <zephyr/bluetooth/mesh/large_comp_data_cli.h>
```

发送大型组成数据获取消息（Large Composition Data Get Message）。

本 API 用于读取组合数据页（Composition Data Page）的一部分。

将 `rsp` 设为 `NULL` 可异步使用本 API，此时函数不等待响应，而是在发送命令后立即返回。

设置 `rsp` 时，用户必须通过 `bt_mesh_large_comp_data_rsp::data` 为组合数据（Composition Data）提供缓冲区。若未提供缓冲区，元数据（Metadata）不会被复制。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点的元素地址（Element Address）。 |
| `page` | 要读取的组合数据页（Composition Data Page）。 |
| `offset` | 组合数据页（Composition Data Page）内的偏移量。 |
| `rsp` | 指向保存服务器响应的结构体的指针；设为 `NULL` 则不等待响应。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="ga4073eb48c43460804705d80ac0919864"></a>

### `bt_mesh_models_metadata_get()`

```c
int bt_mesh_models_metadata_get ( uint16_t net_idx, uint16_t addr, uint8_t page, size_t offset, struct bt_mesh_large_comp_data_rsp * rsp )
```

```c
#include <zephyr/bluetooth/mesh/large_comp_data_cli.h>
```

发送模型元数据获取消息（Models Metadata Get Message）。

本 API 用于读取模型元数据页（Models Metadata Page）的一部分。

将 `rsp` 设为 `NULL` 可异步使用本 API，此时函数不等待响应，而是在发送命令后立即返回。

设置 `rsp` 时，用户必须通过 `bt_mesh_large_comp_data_rsp::data` 为元数据（Metadata）提供缓冲区。若未提供缓冲区，元数据不会被复制。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 用于加密的网络索引（network index）。 |
| `addr` | 目标节点的元素地址（Element Address）。 |
| `page` | 要读取的模型元数据页（Models Metadata Page）。 |
| `offset` | 模型元数据页（Models Metadata Page）内的偏移量。 |
| `rsp` | 指向保存服务器响应的结构体的指针；设为 `NULL` 则不等待响应。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。


## 2.6\_原页交叉引用（Cross References）

- [large_comp_data_cli.h](../api_file_runtime_reference/P032_zephyr__bluetooth__mesh__large_comp_data_cli.h_文件参考.md)
- [bt_mesh_large_comp_data_rsp](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md)
- [bt_mesh_large_comp_data_cli_cb](../bluetooth_mesh_model_reference/P070_bt_mesh_large_comp_data_cli_cb_结构体.md)
- [bt_mesh_large_comp_data_cli](../bluetooth_mesh_model_reference/P069_bt_mesh_large_comp_data_cli_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_MESH_MODEL_CB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gac062c101b7310020e11a527de9c40d3a)
- [BT_MESH_MODEL_ID_LARGE_COMP_DATA_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__mesh.html#ga729d67e4183457932e4c837d65abd842)
- [大型组成数据客户端模型（Large Composition Data Client model）](P002_大型组成数据客户端模型（Large Composition Data Client model）.md)
- [bt_mesh_large_comp_data_rsp::data](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md#a02d92a210b5b7a26b1df4f5076ed99d8)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__assigned__numbers__mesh_html_ga729d67e4183457932e4c837d65abd842"></a>
<a id="agroup__bt__mesh__access_html_gac062c101b7310020e11a527de9c40d3a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_固件更新服务器模型（Firmware Update Server model）.md) · [返回大纲](大纲.md) · [下一章](P003_瑞萨（Renesas）SmartBond.md)
