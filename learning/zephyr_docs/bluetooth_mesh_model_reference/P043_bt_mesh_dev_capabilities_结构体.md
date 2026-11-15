---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-43
title: bt_mesh_dev_capabilities_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dev__capabilities.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_bt\_mesh\_dev\_capabilities\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dev__capabilities.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设备能力（Device Capabilities）。

```c
#include <zephyr/bluetooth/mesh/main.h>
```

<a id="details"></a>

设备能力（Device Capabilities）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_acfef4ecf5ca9324ddc584b9cb910bfe0"></a>

```c
uint8_t elem_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[elem_count](#acfef4ecf5ca9324ddc584b9cb910bfe0)。

设备支持的元素数量（Number of elements）。

<a id="r_a762786d98c070d0ae79e09f22bad4b33"></a>

```c
uint16_t algorithms
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[algorithms](#a762786d98c070d0ae79e09f22bad4b33)。

支持的算法及其他能力（Supported algorithms and other capabilities）。

<a id="r_a7f549f5b3923c0b4249e1b21368ee857"></a>

```c
uint8_t pub_key_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pub_key_type](#a7f549f5b3923c0b4249e1b21368ee857)。

支持的公钥类型（Public key types）。

<a id="r_a744703091988432baa14a84347309bcf"></a>

```c
uint8_t oob_type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[oob_type](#a744703091988432baa14a84347309bcf)。

支持的带外类型（OOB Types）。

<a id="r_a359caeaf64f45783b0c576ef8ef14975"></a>

```c
bt_mesh_output_action_t output_actions
```

相关声明：[bt_mesh_output_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga5512b81ef7eeb45b0a12ef62234c8795)、[output_actions](#a359caeaf64f45783b0c576ef8ef14975)。

支持的输出带外操作（Output OOB Actions）。

<a id="r_a6132c85094980f839cf9dca57d7969ea"></a>

```c
bt_mesh_input_action_t input_actions
```

相关声明：[bt_mesh_input_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf71f3dbdef6b8c085e9a4f068e1f60c5)、[input_actions](#a6132c85094980f839cf9dca57d7969ea)。

支持的输入带外操作（Input OOB Actions）。

<a id="r_a59c959cbd8b1a2aa4e548e7f990cf1f4"></a>

```c
uint8_t output_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[output_size](#a59c959cbd8b1a2aa4e548e7f990cf1f4)。

支持的输出带外数据最大大小（Maximum Output OOB size）。

<a id="r_ac9097c4d634683120509f4c1ac732928"></a>

```c
uint8_t input_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[input_size](#ac9097c4d634683120509f4c1ac732928)。

支持的输入带外数据最大大小（Maximum Input OOB size），以八位组（Octets）为单位。

## 43.2\_详细说明（Detailed Documentation）

<a id="a762786d98c070d0ae79e09f22bad4b33"></a>

### `algorithms`

```c
uint16_t bt_mesh_dev_capabilities::algorithms
```

支持的算法及其他能力（Supported algorithms and other capabilities）。

<a id="acfef4ecf5ca9324ddc584b9cb910bfe0"></a>

### `elem_count`

```c
uint8_t bt_mesh_dev_capabilities::elem_count
```

设备支持的元素数量（Number of elements）。

<a id="a6132c85094980f839cf9dca57d7969ea"></a>

### `input_actions`

```c
bt_mesh_input_action_t bt_mesh_dev_capabilities::input_actions
```

支持的输入带外操作（Input OOB Actions）。

<a id="ac9097c4d634683120509f4c1ac732928"></a>

### `input_size`

```c
uint8_t bt_mesh_dev_capabilities::input_size
```

支持的输入带外数据最大大小（Maximum Input OOB size），以八位组（Octets）为单位。

<a id="a744703091988432baa14a84347309bcf"></a>

### `oob_type`

```c
uint8_t bt_mesh_dev_capabilities::oob_type
```

支持的带外类型（OOB Types）。

<a id="a359caeaf64f45783b0c576ef8ef14975"></a>

### `output_actions`

```c
bt_mesh_output_action_t bt_mesh_dev_capabilities::output_actions
```

支持的输出带外操作（Output OOB Actions）。

<a id="a59c959cbd8b1a2aa4e548e7f990cf1f4"></a>

### `output_size`

```c
uint8_t bt_mesh_dev_capabilities::output_size
```

支持的输出带外数据最大大小（Maximum Output OOB size）。

<a id="a7f549f5b3923c0b4249e1b21368ee857"></a>

### `pub_key_type`

```c
uint8_t bt_mesh_dev_capabilities::pub_key_type
```

支持的公钥类型（Public key types）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/main.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/main.h](https://docs.zephyrproject.org/latest/doxygen/html/main_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_output_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga5512b81ef7eeb45b0a12ef62234c8795)
- [bt_mesh_input_action_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf71f3dbdef6b8c085e9a4f068e1f60c5)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_bt_mesh_comp_p2_record_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_bt_mesh_dfd_srv_结构体.md)
