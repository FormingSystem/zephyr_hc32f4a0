---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-35
title: bt_mesh_comp_p0_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p0.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_bt\_mesh\_comp\_p0\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__comp__p0.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

解析后的组成数据（Composition Data）第0页表示。

```c
#include <zephyr/bluetooth/mesh/cfg_cli.h>
```

<a id="details"></a>

解析后的组成数据第 0 页表示（Parsed Composition data page 0 representation）。应使用 `bt_mesh_comp_p0_get` 从传给 `bt_mesh_cfg_cli_comp_data_get` 的返回缓冲区中提取。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_a3ed8f5ac643443bbcca308baff1c539c"></a>

```c
uint16_t cid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cid](#a3ed8f5ac643443bbcca308baff1c539c)。

公司标识符（Company ID）。

<a id="r_a009806e046583c99f56d271ecebbb8a3"></a>

```c
uint16_t pid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pid](#a009806e046583c99f56d271ecebbb8a3)。

产品标识符（Product ID）。

<a id="r_a27d910cdeb7b6b9d038898e3824dfb57"></a>

```c
uint16_t vid
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[vid](#a27d910cdeb7b6b9d038898e3824dfb57)。

版本标识符（Version ID）。

<a id="r_a32bfead26f338aba892a5459615a65a2"></a>

```c
uint16_t crpl
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[crpl](#a32bfead26f338aba892a5459615a65a2)。

重放保护列表大小（Replay protection list size）。

<a id="r_a0a44e3778f9d134a5c056ca184c3b527"></a>

```c
uint16_t feat
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[feat](#a0a44e3778f9d134a5c056ca184c3b527)。

支持的特性（Supported features），参见 `BT_MESH_FEAT_SUPPORTED`。

## 35.2\_详细说明（Detailed Documentation）

<a id="a3ed8f5ac643443bbcca308baff1c539c"></a>

### `cid`

```c
uint16_t bt_mesh_comp_p0::cid
```

公司标识符（Company ID）。

<a id="a32bfead26f338aba892a5459615a65a2"></a>

### `crpl`

```c
uint16_t bt_mesh_comp_p0::crpl
```

重放保护列表大小（Replay protection list size）。

<a id="a0a44e3778f9d134a5c056ca184c3b527"></a>

### `feat`

```c
uint16_t bt_mesh_comp_p0::feat
```

支持的特性（Supported features），参见 `BT_MESH_FEAT_SUPPORTED`。

<a id="a009806e046583c99f56d271ecebbb8a3"></a>

### `pid`

```c
uint16_t bt_mesh_comp_p0::pid
```

产品标识符（Product ID）。

<a id="a27d910cdeb7b6b9d038898e3824dfb57"></a>

### `vid`

```c
uint16_t bt_mesh_comp_p0::vid
```

版本标识符（Version ID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cfg_cli.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cfg_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/cfg__cli_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_MESH_FEAT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#gac337fd8688d70e862974e010ad42a11b)
- [bt_mesh_cfg_cli_comp_data_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga36259e9c811a8f1a21d642739cf297df)
- [bt_mesh_comp_p0_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__cfg__cli.html#ga1f79d98273a984f1c49b4d5dd5bf8d30)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_bt_mesh_comp2_record_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_bt_mesh_comp_p0_elem_结构体.md)
