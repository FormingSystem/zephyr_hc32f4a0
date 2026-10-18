---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-16
title: bt_conn_le_cs_fae_table_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__cs__fae__table.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_bt\_conn\_le\_cs\_fae\_table\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__cs__fae__table.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

支持 CS 的 LE 连接的远端 FAE 表（FAE Table）。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

支持 CS 的 LE 连接的远端 FAE 表（FAE Table）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_a9d4a2fe09edc897143b6e479f30b7f65"></a>

```c
int8_t * remote_fae_table
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[remote_fae_table](#a9d4a2fe09edc897143b6e479f30b7f65)。

## 16.2\_详细说明（Detailed Documentation）

<a id="a9d4a2fe09edc897143b6e479f30b7f65"></a>

### `remote_fae_table`

```c
int8_t* bt_conn_le_cs_fae_table::remote_fae_table
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_bt_conn_le_cs_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_bt_conn_le_cs_procedure_enable_complete_结构体.md)
