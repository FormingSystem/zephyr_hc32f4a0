---
id: learning.zephyr-docs.system-service-model-reference.page-61
title: mcumgr_image_data_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmcumgr__image__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_mcumgr\_image\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmcumgr__image__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

映像列表数据（Image List Data）。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

<a id="details"></a>

映像列表数据（Image List Data）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_a713cff86339e08b2f74b564dca4c521e"></a>

```c
uint32_t slot_num
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[slot_num](#a713cff86339e08b2f74b564dca4c521e)。

映像槽位编号。

<a id="r_ac394e1e5a0e0425b27926a3405d8bb2d"></a>

```c
uint32_t img_num
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[img_num](#ac394e1e5a0e0425b27926a3405d8bb2d)。

映像编号。

<a id="r_a78c32a6ee0d614bd47352e1d65c773a6"></a>

```c
char hash [64]
```

相关声明：[hash](#a78c32a6ee0d614bd47352e1d65c773a6)。

映像摘要（digest），使用 SHA-256 或 SHA-512。

<a id="r_ab8e2cb7030c755bfae8fda97972df4c2"></a>

```c
size_t hash_len
```

相关声明：[hash_len](#ab8e2cb7030c755bfae8fda97972df4c2)。

摘要长度，单位为字节。

<a id="r_aa75e38d37c9b12a2ccf32af6a47df814"></a>

```c
char version [(sizeof("255.255.65535.4294967295"))+1]
```

相关声明：[version](#aa75e38d37c9b12a2ccf32af6a47df814)。

映像版本（Image Version）。

<a id="r_a24f83149d88a3709b4f58bc72ee932be"></a>

```c
struct mcumgr_image_list_flags flags
```

相关声明：[mcumgr_image_list_flags](P062_mcumgr_image_list_flags_结构体.md)、[flags](#a24f83149d88a3709b4f58bc72ee932be)。

映像标志（Image Flags）。

## 61.2\_详细说明（Detailed Documentation）

<a id="a24f83149d88a3709b4f58bc72ee932be"></a>

### `flags`

```c
struct mcumgr_image_list_flags mcumgr_image_data::flags
```

映像标志（Image Flags）。

<a id="a78c32a6ee0d614bd47352e1d65c773a6"></a>

### `hash`

```c
char mcumgr_image_data::hash[64]
```

映像摘要（digest），使用 SHA-256 或 SHA-512。

<a id="ab8e2cb7030c755bfae8fda97972df4c2"></a>

### `hash_len`

```c
size_t mcumgr_image_data::hash_len
```

摘要长度，单位为字节。

<a id="ac394e1e5a0e0425b27926a3405d8bb2d"></a>

### `img_num`

```c
uint32_t mcumgr_image_data::img_num
```

映像编号。

<a id="a713cff86339e08b2f74b564dca4c521e"></a>

### `slot_num`

```c
uint32_t mcumgr_image_data::slot_num
```

映像槽位编号。

<a id="aa75e38d37c9b12a2ccf32af6a47df814"></a>

### `version`

```c
char mcumgr_image_data::version[(sizeof("255.255.65535.4294967295"))+1]
```

映像版本（Image Version）。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__client_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mcumgr_image_list_flags](P062_mcumgr_image_list_flags_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_linear_range_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_mcumgr_image_list_flags_结构体.md)
