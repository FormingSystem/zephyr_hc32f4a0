---
id: learning.zephyr-docs.api-file-management-reference.page-42
title: zephyr__bluetooth__mesh__sar_cfg_cli.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg__cli_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_zephyr\_\_bluetooth\_\_mesh\_\_sar\_cfg\_cli.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sar__cfg__cli_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh分段与重组配置客户端模型（SAR Configuration Client Model）的API。

<a id="details"></a>

```c
#include <zephyr/bluetooth/mesh.h>
#include <zephyr/bluetooth/mesh/sar_cfg.h>
```

查看此文件的源码。

蓝牙Mesh分段与重组配置客户端模型（SAR Configuration Client Model）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 42.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fsar_5Fcfg_5Fcli"></a>

```c
struct bt_mesh_sar_cfg_cli
```

相关声明：[bt_mesh_sar_cfg_cli](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md)。

Mesh分段与重组配置客户端（SAR Configuration Client）的模型上下文。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 42.2\_宏定义（Macros）

<a id="r_ga742d31e7175e472f1a096ffa6a5acdc5"></a>

```c
#define BT_MESH_MODEL_SAR_CFG_CLI(_cli)
```

相关声明：[BT_MESH_MODEL_SAR_CFG_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga742d31e7175e472f1a096ffa6a5acdc5)。

分段与重组配置客户端（SAR Configuration Client）模型的组成数据条目（composition data entry）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 42.3\_函数（Functions）

<a id="r_ga893ef5861708bec12f87b9f9cc64b9fc"></a>

```c
int bt_mesh_sar_cfg_cli_transmitter_get (uint16_t net_idx, uint16_t addr, struct bt_mesh_sar_tx *rsp)
```

相关声明：[bt_mesh_sar_cfg_cli_transmitter_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga893ef5861708bec12f87b9f9cc64b9fc)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_sar_tx](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md)。

获取目标节点的 SAR 发送端（SAR Transmitter）状态。

<a id="r_ga32e2a580b24a41761911e88413e9664e"></a>

```c
int bt_mesh_sar_cfg_cli_transmitter_set (uint16_t net_idx, uint16_t addr, const struct bt_mesh_sar_tx *set, struct bt_mesh_sar_tx *rsp)
```

相关声明：[bt_mesh_sar_cfg_cli_transmitter_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga32e2a580b24a41761911e88413e9664e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_sar_tx](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md)、[bt_mesh_sar_tx](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md)。

设置目标节点的 SAR 发送端状态。

<a id="r_ga444c99254ef2ccdd10dac08a94219d79"></a>

```c
int bt_mesh_sar_cfg_cli_receiver_get (uint16_t net_idx, uint16_t addr, struct bt_mesh_sar_rx *rsp)
```

相关声明：[bt_mesh_sar_cfg_cli_receiver_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga444c99254ef2ccdd10dac08a94219d79)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_sar_rx](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md)。

获取目标节点的 SAR 接收端（SAR Receiver）状态。

<a id="r_ga884025b2baf8559950ba6dc83e9ef486"></a>

```c
int bt_mesh_sar_cfg_cli_receiver_set (uint16_t net_idx, uint16_t addr, const struct bt_mesh_sar_rx *set, struct bt_mesh_sar_rx *rsp)
```

相关声明：[bt_mesh_sar_cfg_cli_receiver_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga884025b2baf8559950ba6dc83e9ef486)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_sar_rx](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md)、[bt_mesh_sar_rx](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md)。

设置目标节点的 SAR 接收端状态。

<a id="r_ga998846e5735676dc5f79b387d02630d4"></a>

```c
int32_t bt_mesh_sar_cfg_cli_timeout_get (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[bt_mesh_sar_cfg_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga998846e5735676dc5f79b387d02630d4)。

获取当前传输超时值（transmission timeout）。

<a id="r_ga57d7c6a973b35f53689cbf8a065a538f"></a>

```c
void bt_mesh_sar_cfg_cli_timeout_set (int32_t timeout)
```

相关声明：[bt_mesh_sar_cfg_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga57d7c6a973b35f53689cbf8a065a538f)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置传输超时值（Transmission Timeout Value）。


## 42.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh.h](../api_source_reference/P514_mesh.h_源码浏览.md)
- [zephyr/bluetooth/mesh/sar_cfg.h](../api_source_supplement_reference/P174_sar_cfg.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P175_sar_cfg_cli.h_源码浏览.md)
- [bt_mesh_sar_cfg_cli](../bluetooth_mesh_model_reference/P096_bt_mesh_sar_cfg_cli_结构体.md)
- [BT_MESH_MODEL_SAR_CFG_CLI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga742d31e7175e472f1a096ffa6a5acdc5)
- [bt_mesh_sar_cfg_cli_transmitter_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga893ef5861708bec12f87b9f9cc64b9fc)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_sar_tx](../bluetooth_mesh_model_reference/P098_bt_mesh_sar_tx_结构体.md)
- [bt_mesh_sar_cfg_cli_transmitter_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga32e2a580b24a41761911e88413e9664e)
- [bt_mesh_sar_cfg_cli_receiver_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga444c99254ef2ccdd10dac08a94219d79)
- [bt_mesh_sar_rx](../bluetooth_mesh_model_reference/P097_bt_mesh_sar_rx_结构体.md)
- [bt_mesh_sar_cfg_cli_receiver_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga884025b2baf8559950ba6dc83e9ef486)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bt_mesh_sar_cfg_cli_timeout_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga998846e5735676dc5f79b387d02630d4)
- [bt_mesh_sar_cfg_cli_timeout_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__sar__cfg__cli.html#ga57d7c6a973b35f53689cbf8a065a538f)

<a id="header-details"></a>

---

[上一章](P041_zephyr__bluetooth__mesh__proxy.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P043_zephyr__shared_irq.h_文件参考.md)
