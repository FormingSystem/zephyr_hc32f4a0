---
id: learning.zephyr-docs.api-file-runtime-reference.page-32
title: zephyr__bluetooth__mesh__large_comp_data_cli.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_zephyr\_\_bluetooth\_\_mesh\_\_large\_comp\_data\_cli.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/large__comp__data__cli_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh大型组成数据客户端（Large Composition Data Client）模型API的头文件。

<a id="details"></a>

```c
#include <zephyr/bluetooth/mesh.h>
```

查看此文件的源码。

蓝牙Mesh大型组成数据客户端（Large Composition Data Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 32.1\_数据结构（Data Structures）

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

## 32.2\_宏定义（Macros）

<a id="r_ga5860da397d1cd830e8010946c5b32f1e"></a>

```c
#define BT_MESH_MODEL_LARGE_COMP_DATA_CLI(cli_data)
```

相关声明：[BT_MESH_MODEL_LARGE_COMP_DATA_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html#ga5860da397d1cd830e8010946c5b32f1e)。

大型组成数据客户端模型（Large Composition Data Client Model）的组成数据条目（Composition Data Entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 32.3\_函数（Functions）

<a id="r_gaf505ee14246746fc245a34328443d1c6"></a>

```c
int bt_mesh_large_comp_data_get (uint16_t net_idx, uint16_t addr, uint8_t page, size_t offset, struct bt_mesh_large_comp_data_rsp *rsp)
```

相关声明：[bt_mesh_large_comp_data_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html#gaf505ee14246746fc245a34328443d1c6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_large_comp_data_rsp](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md)。

发送大型组成数据获取消息（Large Composition Data Get Message）。

<a id="r_ga4073eb48c43460804705d80ac0919864"></a>

```c
int bt_mesh_models_metadata_get (uint16_t net_idx, uint16_t addr, uint8_t page, size_t offset, struct bt_mesh_large_comp_data_rsp *rsp)
```

相关声明：[bt_mesh_models_metadata_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html#ga4073eb48c43460804705d80ac0919864)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_large_comp_data_rsp](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md)。

发送模型元数据获取消息（Models Metadata Get Message）。


## 32.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh.h](../api_source_reference/P514_mesh.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P435_large_comp_data_cli.h_源码浏览.md)
- [bt_mesh_large_comp_data_rsp](../bluetooth_mesh_model_reference/P071_bt_mesh_large_comp_data_rsp_结构体.md)
- [bt_mesh_large_comp_data_cli_cb](../bluetooth_mesh_model_reference/P070_bt_mesh_large_comp_data_cli_cb_结构体.md)
- [bt_mesh_large_comp_data_cli](../bluetooth_mesh_model_reference/P069_bt_mesh_large_comp_data_cli_结构体.md)
- [BT_MESH_MODEL_LARGE_COMP_DATA_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html#ga5860da397d1cd830e8010946c5b32f1e)
- [bt_mesh_large_comp_data_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html#gaf505ee14246746fc245a34328443d1c6)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_models_metadata_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__large__comp__data__cli.html#ga4073eb48c43460804705d80ac0919864)

<a id="header-details"></a>

---

[上一章](P031_zephyr__psa__its_ids.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P033_zephyr__drivers__lin__transceiver.h_文件参考.md)
