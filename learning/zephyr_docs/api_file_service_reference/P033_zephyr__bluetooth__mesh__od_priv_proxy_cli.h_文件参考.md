---
id: learning.zephyr-docs.api-file-service-reference.page-33
title: zephyr__bluetooth__mesh__od_priv_proxy_cli.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/od__priv__proxy__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_zephyr\_\_bluetooth\_\_mesh\_\_od\_priv\_proxy\_cli.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/od__priv__proxy__cli_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh按需私有GATT代理客户端（On-Demand Private GATT Proxy Client）模型API的头文件。

<a id="details"></a>

```c
#include <zephyr/bluetooth/mesh.h>
```

查看此文件的源码。

蓝牙Mesh按需私有GATT代理客户端（On-Demand Private GATT Proxy Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 33.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fod_5Fpriv_5Fproxy_5Fcli"></a>

```c
struct bt_mesh_od_priv_proxy_cli
```

相关声明：[bt_mesh_od_priv_proxy_cli](../bluetooth_mesh_model_reference/P083_bt_mesh_od_priv_proxy_cli_结构体.md)。

按需私有代理客户端（On-Demand Private Proxy Client）的模型上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 33.2\_宏定义（Macros）

<a id="r_ga037391820efab2b953805f6373431ca9"></a>

```c
#define BT_MESH_MODEL_OD_PRIV_PROXY_CLI(cli_data)
```

相关声明：[BT_MESH_MODEL_OD_PRIV_PROXY_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html#ga037391820efab2b953805f6373431ca9)。

按需私有代理客户端模型（On-Demand Private Proxy Client Model）的组成数据条目（Composition Data Entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 33.3\_函数（Functions）

<a id="r_ga11357595b2d837f6172a2ec98d1e9973"></a>

```c
int bt_mesh_od_priv_proxy_cli_get (uint16_t net_idx, uint16_t addr, uint8_t *val_rsp)
```

相关声明：[bt_mesh_od_priv_proxy_cli_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html#ga11357595b2d837f6172a2ec98d1e9973)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取目标的按需私有通用属性配置文件代理状态（On-Demand Private GATT Proxy State）。

<a id="r_ga9b239c221f8c74108e2a7e5276122e1f"></a>

```c
int bt_mesh_od_priv_proxy_cli_set (uint16_t net_idx, uint16_t addr, uint8_t val, uint8_t *val_rsp)
```

相关声明：[bt_mesh_od_priv_proxy_cli_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html#ga9b239c221f8c74108e2a7e5276122e1f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置目标的按需私有通用属性配置文件代理状态（On-Demand Private GATT Proxy State）。

<a id="r_gad613c78e708f0df5aabda9e16fae6a2c"></a>

```c
void bt_mesh_od_priv_proxy_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_od_priv_proxy_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html#gad613c78e708f0df5aabda9e16fae6a2c)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。


## 33.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh.h](../api_source_reference/P514_mesh.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P631_od_priv_proxy_cli.h_源码浏览.md)
- [bt_mesh_od_priv_proxy_cli](../bluetooth_mesh_model_reference/P083_bt_mesh_od_priv_proxy_cli_结构体.md)
- [BT_MESH_MODEL_OD_PRIV_PROXY_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html#ga037391820efab2b953805f6373431ca9)
- [bt_mesh_od_priv_proxy_cli_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html#ga11357595b2d837f6172a2ec98d1e9973)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_od_priv_proxy_cli_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html#ga9b239c221f8c74108e2a7e5276122e1f)
- [bt_mesh_od_priv_proxy_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__od__priv__proxy__cli.html#gad613c78e708f0df5aabda9e16fae6a2c)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)

<a id="header-details"></a>

---

[上一章](P032_zephyr__dt-bindings__gpio__nxp-siul2-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P034_zephyr__drivers__otp.h_文件参考.md)
