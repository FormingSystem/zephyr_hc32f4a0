---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-90
title: bt_mesh_rpr_caps_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__caps.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第90章\_bt\_mesh\_rpr\_caps\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__caps.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

远程配网服务器（Remote Provisioning Server）的扫描能力。

```c
#include <zephyr/bluetooth/mesh/rpr_cli.h>
```

<a id="details"></a>

远程配网服务器（Remote Provisioning Server）的扫描能力。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 90.1\_数据成员（Data Fields）

<a id="r_af14cce916d388c18ca33d4fc9adb36b5"></a>

```c
uint8_t max_devs
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_devs](#af14cce916d388c18ca33d4fc9adb36b5)。

可扫描设备的最大数量（Max scannable devices）。

<a id="r_a2de75ef667698a6094051a71ba9808ce"></a>

```c
bool active_scan
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[active_scan](#a2de75ef667698a6094051a71ba9808ce)。

支持主动扫描（Active scan）。

## 90.2\_详细说明（Detailed Documentation）

<a id="a2de75ef667698a6094051a71ba9808ce"></a>

### `active_scan`

```c
bool bt_mesh_rpr_caps::active_scan
```

支持主动扫描（Active scan）。

<a id="af14cce916d388c18ca33d4fc9adb36b5"></a>

### `max_devs`

```c
uint8_t bt_mesh_rpr_caps::max_devs
```

可扫描设备的最大数量（Max scannable devices）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/rpr_cli.h`

## 90.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/rpr_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/rpr__cli_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P089_bt_mesh_proxy_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P091_bt_mesh_rpr_cli_结构体.md)
