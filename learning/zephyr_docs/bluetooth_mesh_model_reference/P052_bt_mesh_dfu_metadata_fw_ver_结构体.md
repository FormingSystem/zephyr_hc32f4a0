---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-52
title: bt_mesh_dfu_metadata_fw_ver_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__metadata__fw__ver.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_bt\_mesh\_dfu\_metadata\_fw\_ver\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__metadata__fw__ver.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固件版本（Firmware Version）。

```c
#include <zephyr/bluetooth/mesh/dfu_metadata.h>
```

<a id="details"></a>

固件版本（Firmware Version）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 52.1\_数据成员（Data Fields）

<a id="r_ad4bcde436cbf014cf24fa84888408cc1"></a>

```c
uint8_t major
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[major](#ad4bcde436cbf014cf24fa84888408cc1)。

固件主版本（Firmware major version）。

<a id="r_a3386d56c363d631e4b4e77ea49bd9e8d"></a>

```c
uint8_t minor
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[minor](#a3386d56c363d631e4b4e77ea49bd9e8d)。

固件次版本（Firmware minor version）。

<a id="r_aadeed181c571412b42fbad8111f0d53d"></a>

```c
uint16_t revision
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[revision](#aadeed181c571412b42fbad8111f0d53d)。

固件修订版本（Firmware revision）。

<a id="r_a7c21ae9b7340a1f13d107bf31aeeca90"></a>

```c
uint32_t build_num
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[build_num](#a7c21ae9b7340a1f13d107bf31aeeca90)。

固件构建编号（Firmware build number）。

## 52.2\_详细说明（Detailed Documentation）

<a id="a7c21ae9b7340a1f13d107bf31aeeca90"></a>

### `build_num`

```c
uint32_t bt_mesh_dfu_metadata_fw_ver::build_num
```

固件构建编号（Firmware build number）。

<a id="ad4bcde436cbf014cf24fa84888408cc1"></a>

### `major`

```c
uint8_t bt_mesh_dfu_metadata_fw_ver::major
```

固件主版本（Firmware major version）。

<a id="a3386d56c363d631e4b4e77ea49bd9e8d"></a>

### `minor`

```c
uint8_t bt_mesh_dfu_metadata_fw_ver::minor
```

固件次版本（Firmware minor version）。

<a id="aadeed181c571412b42fbad8111f0d53d"></a>

### `revision`

```c
uint16_t bt_mesh_dfu_metadata_fw_ver::revision
```

固件修订版本（Firmware revision）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu_metadata.h`

## 52.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu_metadata.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__metadata_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P051_bt_mesh_dfu_metadata_结构体.md) · [返回大纲](大纲.md) · [下一章](P053_bt_mesh_dfu_metadata_status_结构体.md)
