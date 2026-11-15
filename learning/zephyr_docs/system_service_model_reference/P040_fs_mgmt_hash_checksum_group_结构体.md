---
id: learning.zephyr-docs.system-service-model-reference.page-40
title: fs_mgmt_hash_checksum_group_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfs__mgmt__hash__checksum__group.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_fs\_mgmt\_hash\_checksum\_group\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfs__mgmt__hash__checksum__group.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

整个哈希/校验和组（Hash/Checksum Group）的处理程序集合。

```c
#include <zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt_hash_checksum.h>
```

<a id="details"></a>

整个哈希/校验和组（Hash/Checksum Group）的处理程序集合。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_a620d92183c78b36ad83793b9ceb9d098"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a620d92183c78b36ad83793b9ceb9d098)。

条目列表节点（Entry list node）。

<a id="r_a5f55c7a9e8905b3ca497cc4711527a2a"></a>

```c
const char * group_name
```

相关声明：[group_name](#a5f55c7a9e8905b3ca497cc4711527a2a)。

处理函数数组，每个名称对应一个条目。

<a id="r_aa9bb8702720e6a8287ec6c88da46afff"></a>

```c
bool byte_string
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[byte_string](#aa9bb8702720e6a8287ec6c88da46afff)。

以字节串（byte string）或数值形式输出。

<a id="r_a8f6ef7d183c6b41c067b2a8544e79e7e"></a>

```c
uint8_t output_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[output_size](#a8f6ef7d183c6b41c067b2a8544e79e7e)。

输出大小，单位为字节。

<a id="r_a003712f5384e918e5d7d51d9b7acfcb4"></a>

```c
fs_mgmt_hash_checksum_handler_fn function
```

相关声明：[fs_mgmt_hash_checksum_handler_fn](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h.html#a1a3db209871cb21f90c7feb5fda4db62)、[function](#a003712f5384e918e5d7d51d9b7acfcb4)。

哈希/校验和（hash/checksum）函数指针。

## 40.2\_详细说明（Detailed Documentation）

<a id="aa9bb8702720e6a8287ec6c88da46afff"></a>

### `byte_string`

```c
bool fs_mgmt_hash_checksum_group::byte_string
```

以字节串（byte string）或数值形式输出。

<a id="a003712f5384e918e5d7d51d9b7acfcb4"></a>

### `function`

```c
fs_mgmt_hash_checksum_handler_fn fs_mgmt_hash_checksum_group::function
```

哈希/校验和（hash/checksum）函数指针。

<a id="a5f55c7a9e8905b3ca497cc4711527a2a"></a>

### `group_name`

```c
const char* fs_mgmt_hash_checksum_group::group_name
```

处理函数数组，每个名称对应一个条目。

<a id="a620d92183c78b36ad83793b9ceb9d098"></a>

### `node`

```c
sys_snode_t fs_mgmt_hash_checksum_group::node
```

条目列表节点（Entry list node）。

<a id="a8f6ef7d183c6b41c067b2a8544e79e7e"></a>

### `output_size`

```c
uint8_t fs_mgmt_hash_checksum_group::output_size
```

输出大小，单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt_hash_checksum.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt_hash_checksum.h](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [fs_mgmt_hash_checksum_handler_fn](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h.html#a1a3db209871cb21f90c7feb5fda4db62)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_fs_mgmt_file_access_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_gdb_mem_region_结构体.md)
