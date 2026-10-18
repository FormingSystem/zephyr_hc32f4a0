---
id: learning.zephyr-docs.system-service-model-reference.page-42
title: img_gr_upload_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structimg__gr__upload.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_img\_gr\_upload\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structimg__gr__upload.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

映像管理（IMG Management）客户端的上传结构。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

<a id="details"></a>

映像管理（IMG mgmt）客户端上传结构体，供客户端内部使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_a773dfcf2f4ceccb771020f29f2e44c92"></a>

```c
char sha256 [32]
```

相关声明：[sha256](#a773dfcf2f4ceccb771020f29f2e44c92)。

映像的 256 位哈希。

<a id="r_af71ec58c3a2c39e1549c41f7692b1319"></a>

```c
bool hash_initialized
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[hash_initialized](#af71ec58c3a2c39e1549c41f7692b1319)。

已配置哈希时为 `true`，否则为 `false`。

<a id="r_a093b1897e492545ab5b92d91bde727fb"></a>

```c
size_t image_size
```

相关声明：[image_size](#a093b1897e492545ab5b92d91bde727fb)。

映像大小。

<a id="r_a71736f17ef73d50d0e61049d356e2ce2"></a>

```c
size_t offset
```

相关声明：[offset](#a71736f17ef73d50d0e61049d356e2ce2)。

映像上传偏移状态。

<a id="r_ae5245e6622c991cbd207b3f69f7548f3"></a>

```c
size_t upload_header_size
```

相关声明：[upload_header_size](#ae5245e6622c991cbd207b3f69f7548f3)。

最坏情况下的初始上传消息大小。

<a id="r_a457e54010e9980b96bc970f6d43bd127"></a>

```c
uint32_t image_num
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[image_num](#a457e54010e9980b96bc970f6d43bd127)。

映像槽位编号。

## 42.2\_详细说明（Detailed Documentation）

<a id="af71ec58c3a2c39e1549c41f7692b1319"></a>

### `hash_initialized`

```c
bool img_gr_upload::hash_initialized
```

已配置哈希时为 `true`，否则为 `false`。

<a id="a457e54010e9980b96bc970f6d43bd127"></a>

### `image_num`

```c
uint32_t img_gr_upload::image_num
```

映像槽位编号。

<a id="a093b1897e492545ab5b92d91bde727fb"></a>

### `image_size`

```c
size_t img_gr_upload::image_size
```

映像大小。

<a id="a71736f17ef73d50d0e61049d356e2ce2"></a>

### `offset`

```c
size_t img_gr_upload::offset
```

映像上传偏移状态。

<a id="a773dfcf2f4ceccb771020f29f2e44c92"></a>

### `sha256`

```c
char img_gr_upload::sha256[32]
```

映像的 256 位哈希。

<a id="ae5245e6622c991cbd207b3f69f7548f3"></a>

### `upload_header_size`

```c
size_t img_gr_upload::upload_header_size
```

最坏情况下的初始上传消息大小。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__client_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_gdb_mem_region_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_img_mgmt_client_结构体.md)
