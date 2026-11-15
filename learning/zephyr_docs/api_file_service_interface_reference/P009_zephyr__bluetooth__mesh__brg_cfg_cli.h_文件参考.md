---
id: learning.zephyr-docs.api-file-service-interface-reference.page-9
title: zephyr__bluetooth__mesh__brg_cfg_cli.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_bluetooth\_\_mesh\_\_brg\_cfg\_cli.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/brg__cfg__cli_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh桥接配置客户端（Bridge Configuration Client）模型API的头文件。

<a id="details"></a>

```c
#include <zephyr/bluetooth/mesh/brg_cfg.h>
```

查看此文件的源码。

蓝牙Mesh桥接配置客户端（Bridge Configuration Client）模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fbrg_5Fcfg_5Fcli_5Fcb"></a>

```c
struct bt_mesh_brg_cfg_cli_cb
```

相关声明：[bt_mesh_brg_cfg_cli_cb](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md)。

Mesh桥接配置客户端（Bridge Configuration Client）状态消息的回调。

<a id="r_bt_5Fmesh_5Fbrg_5Fcfg_5Fcli"></a>

```c
struct bt_mesh_brg_cfg_cli
```

相关声明：[bt_mesh_brg_cfg_cli](../bluetooth_mesh_model_reference/P016_bt_mesh_brg_cfg_cli_结构体.md)。

桥接配置客户端（Bridge Configuration Client）的模型上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_ga4cf994be4732bd99b2c8a4642f670efe"></a>

```c
#define BT_MESH_MODEL_BRG_CFG_CLI(_cli)
```

相关声明：[BT_MESH_MODEL_BRG_CFG_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga4cf994be4732bd99b2c8a4642f670efe)。

桥接配置客户端模型（Bridge Configuration Client Model）的组合数据（Composition Data）条目。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.3\_函数（Functions）

<a id="r_ga6a4507190e425013a9d21ea0a1be1b5c"></a>

```c
int bt_mesh_brg_cfg_cli_get (uint16_t net_idx, uint16_t addr, enum bt_mesh_brg_cfg_state *status)
```

相关声明：[bt_mesh_brg_cfg_cli_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga6a4507190e425013a9d21ea0a1be1b5c)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_state](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#ga7bddcbe2b1196df6a1c80d8c213866f9)。

向指定目标地址发送子网桥接获取（Subnet Bridge Get）消息。

<a id="r_ga6643d4d043af4b0cb30470a5c9a46f38"></a>

```c
int bt_mesh_brg_cfg_cli_set (uint16_t net_idx, uint16_t addr, enum bt_mesh_brg_cfg_state val, enum bt_mesh_brg_cfg_state *status)
```

相关声明：[bt_mesh_brg_cfg_cli_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga6643d4d043af4b0cb30470a5c9a46f38)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_state](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#ga7bddcbe2b1196df6a1c80d8c213866f9)、[bt_mesh_brg_cfg_state](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#ga7bddcbe2b1196df6a1c80d8c213866f9)。

使用指定参数向指定目标地址发送子网桥接设置（Subnet Bridge Set）消息。

<a id="r_ga99951987bd6787e3e1348d8e51e64fe5"></a>

```c
int bt_mesh_brg_cfg_cli_table_size_get (uint16_t net_idx, uint16_t addr, uint16_t *size)
```

相关声明：[bt_mesh_brg_cfg_cli_table_size_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga99951987bd6787e3e1348d8e51e64fe5)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

使用指定参数向指定目标地址发送桥接表大小获取（Bridging Table Size Get）消息。

<a id="r_ga8f055e8ee384e8ea4887a56720959b26"></a>

```c
int bt_mesh_brg_cfg_cli_table_add (uint16_t net_idx, uint16_t addr, struct bt_mesh_brg_cfg_table_entry *entry, struct bt_mesh_brg_cfg_table_status *rsp)
```

相关声明：[bt_mesh_brg_cfg_cli_table_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga8f055e8ee384e8ea4887a56720959b26)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_table_entry](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md)、[bt_mesh_brg_cfg_table_status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md)。

使用指定参数向指定目标地址发送桥接表添加（Bridging Table Add）消息。

<a id="r_gabdb919dcf177b8d5c8a28b057469bf18"></a>

```c
int bt_mesh_brg_cfg_cli_table_remove (uint16_t net_idx, uint16_t addr, uint16_t net_idx1, uint16_t net_idx2, uint16_t addr1, uint16_t addr2, struct bt_mesh_brg_cfg_table_status *rsp)
```

相关声明：[bt_mesh_brg_cfg_cli_table_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#gabdb919dcf177b8d5c8a28b057469bf18)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_table_status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md)。

使用指定参数向指定目标地址发送桥接表移除（Bridging Table Remove）消息。

<a id="r_ga04bb227d14d4f478e4f32a8ca87d2c38"></a>

```c
int bt_mesh_brg_cfg_cli_subnets_get (uint16_t net_idx, uint16_t addr, struct bt_mesh_brg_cfg_filter_netkey filter_net_idx, uint8_t start_idx, struct bt_mesh_brg_cfg_subnets_list *rsp)
```

相关声明：[bt_mesh_brg_cfg_cli_subnets_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga04bb227d14d4f478e4f32a8ca87d2c38)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_filter_netkey](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_brg_cfg_subnets_list](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md)。

使用指定参数向指定目标地址发送已桥接子网获取（Bridged Subnets Get）消息。

<a id="r_gacd3811be7b87d2d9187aed6c50945b85"></a>

```c
int bt_mesh_brg_cfg_cli_table_get (uint16_t net_idx, uint16_t addr, uint16_t net_idx1, uint16_t net_idx2, uint16_t start_idx, struct bt_mesh_brg_cfg_table_list *rsp)
```

相关声明：[bt_mesh_brg_cfg_cli_table_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#gacd3811be7b87d2d9187aed6c50945b85)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_brg_cfg_table_list](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md)。

使用指定参数向指定目标地址发送桥接表获取（Bridging Table Get）消息。

<a id="r_ga252994dd3119387703af45c0932ef253"></a>

```c
int32_t bt_mesh_brg_cfg_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_brg_cfg_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga252994dd3119387703af45c0932ef253)。

获取当前传输超时值（transmission timeout）。

<a id="r_gad30102a29983545ec79f178b1390ce74"></a>

```c
void bt_mesh_brg_cfg_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_brg_cfg_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#gad30102a29983545ec79f178b1390ce74)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。


## 9.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/brg_cfg.h](../api_source_system_reference/P004_brg_cfg.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P077_brg_cfg_cli.h_源码浏览.md)
- [bt_mesh_brg_cfg_cli_cb](../bluetooth_mesh_model_reference/P017_bt_mesh_brg_cfg_cli_cb_结构体.md)
- [bt_mesh_brg_cfg_cli](../bluetooth_mesh_model_reference/P016_bt_mesh_brg_cfg_cli_结构体.md)
- [BT_MESH_MODEL_BRG_CFG_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga4cf994be4732bd99b2c8a4642f670efe)
- [bt_mesh_brg_cfg_cli_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga6a4507190e425013a9d21ea0a1be1b5c)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_brg_cfg_state](../api_extension_topic_reference/P003_桥接配置公共头文件（Bridge Configuration common header）.md#ga7bddcbe2b1196df6a1c80d8c213866f9)
- [bt_mesh_brg_cfg_cli_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga6643d4d043af4b0cb30470a5c9a46f38)
- [bt_mesh_brg_cfg_cli_table_size_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga99951987bd6787e3e1348d8e51e64fe5)
- [bt_mesh_brg_cfg_cli_table_add](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga8f055e8ee384e8ea4887a56720959b26)
- [bt_mesh_brg_cfg_table_entry](../bluetooth_mesh_model_reference/P020_bt_mesh_brg_cfg_table_entry_结构体.md)
- [bt_mesh_brg_cfg_table_status](../bluetooth_mesh_model_reference/P022_bt_mesh_brg_cfg_table_status_结构体.md)
- [bt_mesh_brg_cfg_cli_table_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#gabdb919dcf177b8d5c8a28b057469bf18)
- [bt_mesh_brg_cfg_cli_subnets_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga04bb227d14d4f478e4f32a8ca87d2c38)
- [bt_mesh_brg_cfg_filter_netkey](../bluetooth_mesh_model_reference/P018_bt_mesh_brg_cfg_filter_netkey_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_brg_cfg_subnets_list](../bluetooth_mesh_model_reference/P019_bt_mesh_brg_cfg_subnets_list_结构体.md)
- [bt_mesh_brg_cfg_cli_table_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#gacd3811be7b87d2d9187aed6c50945b85)
- [bt_mesh_brg_cfg_table_list](../bluetooth_mesh_model_reference/P021_bt_mesh_brg_cfg_table_list_结构体.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_brg_cfg_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#ga252994dd3119387703af45c0932ef253)
- [bt_mesh_brg_cfg_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__brg__cfg__cli.html#gad30102a29983545ec79f178b1390ce74)

<a id="header-details"></a>

---

[上一章](P008_zephyr__dsp__basicmath_f16.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__busy_sim.h_文件参考.md)
