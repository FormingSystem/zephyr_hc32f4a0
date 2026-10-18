---
id: learning.zephyr-docs.system-service-model-reference.page-80
title: smp_streamer_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsmp__streamer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第80章\_smp\_streamer\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsmp__streamer.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

解码、编码并传输简单管理协议（SMP）数据包。

```c
#include <zephyr/mgmt/mcumgr/smp/smp.h>
```

<a id="details"></a>

解码、编码并传输简单管理协议（SMP）数据包。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 80.1\_数据成员（Data Fields）

<a id="r_a478b0732071a888bd83ccd03bdd51e85"></a>

```c
struct smp_transport * smpt
```

相关声明：[smp_transport](P081_smp_transport_结构体.md)、[smpt](#a478b0732071a888bd83ccd03bdd51e85)。

<a id="r_ad5f6bcfcea32075ff61afc1b6c4972be"></a>

```c
struct cbor_nb_reader * reader
```

相关声明：[cbor_nb_reader](P001_cbor_nb_reader_结构体.md)、[reader](#ad5f6bcfcea32075ff61afc1b6c4972be)。

<a id="r_a00f6b8731e1a789939eaec106d746daf"></a>

```c
struct cbor_nb_writer * writer
```

相关声明：[cbor_nb_writer](P002_cbor_nb_writer_结构体.md)、[writer](#a00f6b8731e1a789939eaec106d746daf)。

## 80.2\_详细说明（Detailed Documentation）

<a id="ad5f6bcfcea32075ff61afc1b6c4972be"></a>

### `reader`

```c
struct cbor_nb_reader* smp_streamer::reader
```

<a id="a478b0732071a888bd83ccd03bdd51e85"></a>

### `smpt`

```c
struct smp_transport* smp_streamer::smpt
```

<a id="a00f6b8731e1a789939eaec106d746daf"></a>

### `writer`

```c
struct cbor_nb_writer* smp_streamer::writer
```

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/smp/smp.h`

## 80.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/smp/smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h_source.html)
- [smp_transport](P081_smp_transport_结构体.md)
- [cbor_nb_reader](P001_cbor_nb_reader_结构体.md)
- [cbor_nb_writer](P002_cbor_nb_writer_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P079_smp_client_transport_entry_结构体.md) · [返回大纲](大纲.md) · [下一章](P081_smp_transport_结构体.md)
