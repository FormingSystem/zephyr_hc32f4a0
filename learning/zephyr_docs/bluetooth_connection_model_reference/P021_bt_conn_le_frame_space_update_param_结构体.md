---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-21
title: bt_conn_le_frame_space_update_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__frame__space__update__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_bt\_conn\_le\_frame\_space\_update\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__frame__space__update__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

帧间隔更新（Frame Space Update）参数。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

帧间隔更新（Frame Space Update）参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

<a id="r_a67adb4f731d9a1822b400af9f30bcf43"></a>

```c
uint8_t phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phys](#a67adb4f731d9a1822b400af9f30bcf43)。

要更新的物理层掩码（PHY mask）。

<a id="r_a1e5bd6b331c1c7c4881e2875b1adfd3d"></a>

```c
uint16_t spacing_types
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[spacing_types](#a1e5bd6b331c1c7c4881e2875b1adfd3d)。

要更新的间隔类型掩码（Spacing types mask）。

<a id="r_a7d3f1ee0c43797ab100b24c3919f304f"></a>

```c
uint16_t frame_space_min
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[frame_space_min](#a7d3f1ee0c43797ab100b24c3919f304f)。

最小帧间隔（Minimum frame space），单位为微秒。

<a id="r_a90e83dca82b557ef1476d5e4919fb170"></a>

```c
uint16_t frame_space_max
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[frame_space_max](#a90e83dca82b557ef1476d5e4919fb170)。

最大帧间隔（Maximum frame space），单位为微秒。

## 21.2\_详细说明（Detailed Documentation）

<a id="a90e83dca82b557ef1476d5e4919fb170"></a>

### `frame_space_max`

```c
uint16_t bt_conn_le_frame_space_update_param::frame_space_max
```

最大帧间隔（Maximum frame space），单位为微秒。

蓝牙核心规范（Bluetooth Core Specification）第 4 卷 E 部分第 7.8.151 节允许帧间隔（Frame space）在 0–10000 微秒范围内。实际支持的帧间隔值取决于控制器能力。

<a id="a7d3f1ee0c43797ab100b24c3919f304f"></a>

### `frame_space_min`

```c
uint16_t bt_conn_le_frame_space_update_param::frame_space_min
```

最小帧间隔（Minimum frame space），单位为微秒。

蓝牙核心规范（Bluetooth Core Specification）第 4 卷 E 部分第 7.8.151 节允许帧间隔（Frame space）在 0–10000 微秒范围内。实际支持的帧间隔值取决于控制器能力。

<a id="a67adb4f731d9a1822b400af9f30bcf43"></a>

### `phys`

```c
uint8_t bt_conn_le_frame_space_update_param::phys
```

要更新的物理层掩码（PHY mask）。

取值参见 `BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_*`。

<a id="a1e5bd6b331c1c7c4881e2875b1adfd3d"></a>

### `spacing_types`

```c
uint16_t bt_conn_le_frame_space_update_param::spacing_types
```

要更新的间隔类型掩码（Spacing types mask）。

取值参见 `BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_*` 和 `BT_CONN_LE_FRAME_SPACE_TYPES_MASK_*`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_bt_conn_le_data_len_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_bt_conn_le_frame_space_updated_结构体.md)
