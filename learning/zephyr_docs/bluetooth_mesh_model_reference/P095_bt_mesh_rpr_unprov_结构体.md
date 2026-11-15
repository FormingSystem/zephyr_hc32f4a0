---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-95
title: bt_mesh_rpr_unprov_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__unprov.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第95章\_bt\_mesh\_rpr\_unprov\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__unprov.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

未配网设备（Unprovisioned Device）。

```c
#include <zephyr/bluetooth/mesh/rpr.h>
```

<a id="details"></a>

未配网设备（Unprovisioned Device）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 95.1\_数据成员（Data Fields）

<a id="r_aa5fe6bad39edcb45d2e024c1c890c680"></a>

```c
uint8_t uuid [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](#aa5fe6bad39edcb45d2e024c1c890c680)。

未配网设备的通用唯一标识符（UUID）。

<a id="r_a9d0103e4899b445c2c20d62749889e3e"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#a9d0103e4899b445c2c20d62749889e3e)。

标志（Flags），参见 `BT_MESH_RPR_UNPROV_*` 标志。

<a id="r_a26ffffb174704a0a6a35418886e2a971"></a>

```c
int8_t rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi](#a26ffffb174704a0a6a35418886e2a971)。

服务器接收未配网设备信号时的接收信号强度指示（RSSI）。

<a id="r_a51e9bfeb3145c29644378d6ec5400e75"></a>

```c
bt_mesh_prov_oob_info_t oob
```

相关声明：[bt_mesh_prov_oob_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf93f7b49dada5c3f7accc54663648e48)、[oob](#a51e9bfeb3145c29644378d6ec5400e75)。

带外信息（Out of band information）。

<a id="r_ade58aed40bfaffb6f23a4e0570e370dd"></a>

```c
uint32_t hash
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[hash](#ade58aed40bfaffb6f23a4e0570e370dd)。

未配网信标（Unprovisioned beacon）中的统一资源标识符哈希（URI hash）。

## 95.2\_详细说明（Detailed Documentation）

<a id="a9d0103e4899b445c2c20d62749889e3e"></a>

### `flags`

```c
uint8_t bt_mesh_rpr_unprov::flags
```

标志（Flags），参见 `BT_MESH_RPR_UNPROV_*` 标志。

<a id="ade58aed40bfaffb6f23a4e0570e370dd"></a>

### `hash`

```c
uint32_t bt_mesh_rpr_unprov::hash
```

未配网信标（Unprovisioned beacon）中的统一资源标识符哈希（URI hash）。

仅当 `flags` 中设置了 `BT_MESH_RPR_UNPROV_HASH` 时有效。

<a id="a51e9bfeb3145c29644378d6ec5400e75"></a>

### `oob`

```c
bt_mesh_prov_oob_info_t bt_mesh_rpr_unprov::oob
```

带外信息（Out of band information）。

<a id="a26ffffb174704a0a6a35418886e2a971"></a>

### `rssi`

```c
int8_t bt_mesh_rpr_unprov::rssi
```

服务器接收未配网设备信号时的接收信号强度指示（RSSI）。

<a id="aa5fe6bad39edcb45d2e024c1c890c680"></a>

### `uuid`

```c
uint8_t bt_mesh_rpr_unprov::uuid[16]
```

未配网设备的通用唯一标识符（UUID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/rpr.h`

## 95.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/rpr.h](https://docs.zephyrproject.org/latest/doxygen/html/rpr_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [bt_mesh_prov_oob_info_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf93f7b49dada5c3f7accc54663648e48)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [BT_MESH_RPR_UNPROV_HASH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga94522cf0b3832b576100b787808474bd)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P094_bt_mesh_rpr_scan_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P096_bt_mesh_sar_cfg_cli_结构体.md)
