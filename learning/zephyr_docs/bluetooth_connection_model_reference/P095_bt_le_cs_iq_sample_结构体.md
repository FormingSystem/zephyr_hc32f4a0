---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-95
title: bt_le_cs_iq_sample_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__iq__sample.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第95章\_bt\_le\_cs\_iq\_sample\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__iq__sample.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

从步骤数据中提取并完成符号扩展的同相/正交（IQ）值。

```c
#include <zephyr/bluetooth/cs.h>
```

<a id="details"></a>

从步骤数据中提取并完成符号扩展的同相/正交（IQ）值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 95.1\_数据成员（Data Fields）

<a id="r_ab25db98b90a2f3c9a20a40efb1050c29"></a>

```c
int16_t i
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[i](#ab25db98b90a2f3c9a20a40efb1050c29)。

<a id="r_a33dd41ba3b8027035bde1610c4a77a98"></a>

```c
int16_t q
```

相关声明：[int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)、[q](#a33dd41ba3b8027035bde1610c4a77a98)。

## 95.2\_详细说明（Detailed Documentation）

<a id="ab25db98b90a2f3c9a20a40efb1050c29"></a>

### `i`

```c
int16_t bt_le_cs_iq_sample::i
```

<a id="a33dd41ba3b8027035bde1610c4a77a98"></a>

### `q`

```c
int16_t bt_le_cs_iq_sample::q
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/cs.h`

## 95.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/cs.h](https://docs.zephyrproject.org/latest/doxygen/html/cs_8h_source.html)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P094_bt_le_cs_create_config_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P096_bt_le_cs_procedure_enable_param_结构体.md)
