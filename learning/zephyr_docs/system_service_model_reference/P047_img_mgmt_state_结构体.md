---
id: learning.zephyr-docs.system-service-model-reference.page-47
title: img_mgmt_state_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_img\_mgmt\_state\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__state.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

进行中的上传所用的全局状态（Global State）。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

<a id="details"></a>

进行中的上传所用的全局状态（Global State）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_a4da29c0c4b525463cce3f0d3ffbed633"></a>

```c
int area_id
```

相关声明：[area_id](#a4da29c0c4b525463cce3f0d3ffbed633)。

正在写入的 Flash 区域；没有上传正在进行时为 -1。

<a id="r_a965b6426ea57beac531af3bb9d2f0d0e"></a>

```c
size_t off
```

相关声明：[off](#a965b6426ea57beac531af3bb9d2f0d0e)。

下一个数据块的 Flash 偏移量。

<a id="r_a40619a325f216e1c27e45fd19ccd6db3"></a>

```c
size_t size
```

相关声明：[size](#a40619a325f216e1c27e45fd19ccd6db3)。

映像数据的总大小。

<a id="r_a6a3cbeb401f057fb1510e1acbdf7d71c"></a>

```c
uint8_t data_sha_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_sha_len](#a6a3cbeb401f057fb1510e1acbdf7d71c)。

映像数据的哈希，用于恢复尚未完成的上传。

<a id="r_a1c357f22c420a310c234c96a9bc7143f"></a>

```c
uint8_t data_sha [32]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_sha](#a1c357f22c420a310c234c96a9bc7143f)。

## 47.2\_详细说明（Detailed Documentation）

<a id="a4da29c0c4b525463cce3f0d3ffbed633"></a>

### `area_id`

```c
int img_mgmt_state::area_id
```

正在写入的 Flash 区域；没有上传正在进行时为 -1。

<a id="a1c357f22c420a310c234c96a9bc7143f"></a>

### `data_sha`

```c
uint8_t img_mgmt_state::data_sha[32]
```

<a id="a6a3cbeb401f057fb1510e1acbdf7d71c"></a>

### `data_sha_len`

```c
uint8_t img_mgmt_state::data_sha_len
```

映像数据的哈希，用于恢复尚未完成的上传。

<a id="a965b6426ea57beac531af3bb9d2f0d0e"></a>

### `off`

```c
size_t img_mgmt_state::off
```

下一个数据块的 Flash 偏移量。

<a id="a40619a325f216e1c27e45fd19ccd6db3"></a>

### `size`

```c
size_t img_mgmt_state::size
```

映像数据的总大小。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_img_mgmt_slot_info_slot_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_img_mgmt_state_slot_encode_结构体.md)
