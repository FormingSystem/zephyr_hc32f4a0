---
id: learning.zephyr-docs.system-service-model-reference.page-1
title: cbor_nb_reader_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcbor__nb__reader.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_cbor\_nb\_reader\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcbor__nb__reader.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/mgmt/mcumgr/smp/smp.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_a1bfa99724cc6de5d93d88415e5231d09"></a>

```c
struct net_buf * nb
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[nb](#a1bfa99724cc6de5d93d88415e5231d09)。

<a id="r_a7cbec04a9c1fd8a1f8feed0de8d1be1d"></a>

```c
zcbor_state_t zs [CONFIG_MCUMGR_SMP_CBOR_MAX_DECODING_LEVELS+2]
```

相关声明：[zs](#a7cbec04a9c1fd8a1f8feed0de8d1be1d)。

## 1.2\_详细说明（Detailed Documentation）

<a id="a1bfa99724cc6de5d93d88415e5231d09"></a>

### `nb`

```c
struct net_buf* cbor_nb_reader::nb
```

<a id="a7cbec04a9c1fd8a1f8feed0de8d1be1d"></a>

### `zs`

```c
zcbor_state_t cbor_nb_reader::zs[CONFIG_MCUMGR_SMP_CBOR_MAX_DECODING_LEVELS+2]
```

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/smp/smp.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/smp/smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h_source.html)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_cbor_nb_writer_结构体.md)
