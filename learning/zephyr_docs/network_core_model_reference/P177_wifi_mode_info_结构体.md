---
id: learning.zephyr-docs.network-core-model-reference.page-177
title: wifi_mode_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__mode__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第177章\_wifi\_mode\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__mode__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi模式设置（Mode Setup）。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi模式设置（Mode Setup）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 177.1\_数据成员（Data Fields）

<a id="r_aa29d3b88fc718aa3ac05daf38974707d"></a>

```c
uint8_t mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mode](#aa29d3b88fc718aa3ac05daf38974707d)。

特定工作模式的模式设置（Mode setting for a specific mode of operation）。

<a id="r_add58dd3b45fd2ddaf684d1b0de81bef9"></a>

```c
uint8_t if_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[if_index](#add58dd3b45fd2ddaf684d1b0de81bef9)。

接口索引（Interface index）。

<a id="r_a57c101db8b81ab0ac5dd0a158057a64a"></a>

```c
enum wifi_mgmt_op oper
```

相关声明：[wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)、[oper](#a57c101db8b81ab0ac5dd0a158057a64a)。

获取或设置操作（Get or set operation）。

## 177.2\_详细说明（Detailed Documentation）

<a id="add58dd3b45fd2ddaf684d1b0de81bef9"></a>

### `if_index`

```c
uint8_t wifi_mode_info::if_index
```

接口索引（Interface index）。

<a id="aa29d3b88fc718aa3ac05daf38974707d"></a>

### `mode`

```c
uint8_t wifi_mode_info::mode
```

特定工作模式的模式设置（Mode setting for a specific mode of operation）。

<a id="a57c101db8b81ab0ac5dd0a158057a64a"></a>

### `oper`

```c
enum wifi_mgmt_op wifi_mode_info::oper
```

获取或设置操作（Get or set operation）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 177.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P176_wifi_mgmt_ops_结构体.md) · [返回大纲](大纲.md) · [下一章](P178_wifi_nm_instance_结构体.md)
