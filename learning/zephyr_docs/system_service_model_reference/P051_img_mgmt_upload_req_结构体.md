---
id: learning.zephyr-docs.system-service-model-reference.page-51
title: img_mgmt_upload_req_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__upload__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_img\_mgmt\_upload\_req\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__upload__req.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示单个上传请求（Upload Request）。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h>
```

<a id="details"></a>

表示单个上传请求（Upload Request）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_ad61f8c732f0b2150bd252e47eb539bb1"></a>

```c
uint32_t image
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[image](#ad61f8c732f0b2150bd252e47eb539bb1)。

<a id="r_ae9c67210faa7dfc55a73f66defc00195"></a>

```c
size_t off
```

相关声明：[off](#ae9c67210faa7dfc55a73f66defc00195)。

<a id="r_a25cdcd55c77cde43af1a9ec9b414cecb"></a>

```c
size_t size
```

相关声明：[size](#a25cdcd55c77cde43af1a9ec9b414cecb)。

<a id="r_ade363ed09134ff2f3a1fcb20a6305cfa"></a>

```c
struct zcbor_string img_data
```

相关声明：[img_data](#ade363ed09134ff2f3a1fcb20a6305cfa)。

<a id="r_ae30c1fc9257f04c88216ba92f8453dac"></a>

```c
struct zcbor_string data_sha
```

相关声明：[data_sha](#ae30c1fc9257f04c88216ba92f8453dac)。

<a id="r_a439504202c945a1dd74b75c35a1a8017"></a>

```c
bool upgrade
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[upgrade](#a439504202c945a1dd74b75c35a1a8017)。

## 51.2\_详细说明（Detailed Documentation）

<a id="ae30c1fc9257f04c88216ba92f8453dac"></a>

### `data_sha`

```c
struct zcbor_string img_mgmt_upload_req::data_sha
```

<a id="ad61f8c732f0b2150bd252e47eb539bb1"></a>

### `image`

```c
uint32_t img_mgmt_upload_req::image
```

<a id="ade363ed09134ff2f3a1fcb20a6305cfa"></a>

### `img_data`

```c
struct zcbor_string img_mgmt_upload_req::img_data
```

<a id="ae9c67210faa7dfc55a73f66defc00195"></a>

### `off`

```c
size_t img_mgmt_upload_req::off
```

<a id="a25cdcd55c77cde43af1a9ec9b414cecb"></a>

### `size`

```c
size_t img_mgmt_upload_req::size
```

<a id="a439504202c945a1dd74b75c35a1a8017"></a>

### `upgrade`

```c
bool img_mgmt_upload_req::upgrade
```

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_img_mgmt_upload_check_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_input_callback_结构体.md)
