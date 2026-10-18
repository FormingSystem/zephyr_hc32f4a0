---
id: learning.zephyr-docs.system-service-model-reference.page-38
title: fota_http_progress_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfota__http__progress.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_fota\_http\_progress\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfota__http__progress.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

写入映像（Image）期间报告的传输状态。

```c
#include <zephyr/mgmt/fota_http.h>
```

<a id="details"></a>

写入映像（Image）期间报告的传输状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 38.1\_数据成员（Data Fields）

<a id="r_a9bc76de1cc1df4105a5ddb23a3968b50"></a>

```c
size_t written
```

相关声明：[written](#a9bc76de1cc1df4105a5ddb23a3968b50)。

截至目前槽位（slot）中已有的字节数，包括续传数据。

<a id="r_a4fde85b0d24bf84c7a5695acd69c7c97"></a>

```c
size_t total
```

相关声明：[total](#a4fde85b0d24bf84c7a5695acd69c7c97)。

映像总大小；服务器未声明大小时为 0。

<a id="r_ab93fb2eddbcf59556e92688dca0c6132"></a>

```c
int http_status
```

相关声明：[http_status](#ab93fb2eddbcf59556e92688dca0c6132)。

响应的 HTTP 状态码。

## 38.2\_详细说明（Detailed Documentation）

<a id="ab93fb2eddbcf59556e92688dca0c6132"></a>

### `http_status`

```c
int fota_http_progress::http_status
```

响应的 HTTP 状态码。

<a id="a4fde85b0d24bf84c7a5695acd69c7c97"></a>

### `total`

```c
size_t fota_http_progress::total
```

映像总大小；服务器未声明大小时为 0。

<a id="a9bc76de1cc1df4105a5ddb23a3968b50"></a>

### `written`

```c
size_t fota_http_progress::written
```

截至目前槽位（slot）中已有的字节数，包括续传数据。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/fota_http.h`

## 38.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/fota_http.h](https://docs.zephyrproject.org/latest/doxygen/html/fota__http_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P037_fota_http_download_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P039_fs_mgmt_file_access_结构体.md)
