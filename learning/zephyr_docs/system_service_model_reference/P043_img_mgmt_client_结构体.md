---
id: learning.zephyr-docs.system-service-model-reference.page-43
title: img_mgmt_client_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_img\_mgmt\_client\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structimg__mgmt__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

映像管理（IMG Management）客户端对象。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

<a id="details"></a>

映像管理（IMG Management）客户端对象。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_a36abd266bbd1ea35849423708f9e816d"></a>

```c
struct smp_client_object * smp_client
```

相关声明：[smp_client_object](P078_smp_client_object_结构体.md)、[smp_client](#a36abd266bbd1ea35849423708f9e816d)。

简单管理协议（SMP）的客户端对象。

<a id="r_a77559218adc5f7873366c56f9a02750e"></a>

```c
struct img_gr_upload upload
```

相关声明：[img_gr_upload](P042_img_gr_upload_结构体.md)、[upload](#a77559218adc5f7873366c56f9a02750e)。

供客户端内部使用的映像上传状态数据。

<a id="r_a2a2097f05111d6242d623a68959ecca9"></a>

```c
int image_list_length
```

相关声明：[image_list_length](#a2a2097f05111d6242d623a68959ecca9)。

客户端映像列表缓冲区大小。

<a id="r_a654c94fafac9cd72465a413de8266005"></a>

```c
struct mcumgr_image_data * image_list
```

相关声明：[mcumgr_image_data](P061_mcumgr_image_data_结构体.md)、[image_list](#a654c94fafac9cd72465a413de8266005)。

映像列表缓冲区。

<a id="r_a4fb8d168a6faf48c32903b71fc8c8097"></a>

```c
int status
```

相关声明：[status](#a4fb8d168a6faf48c32903b71fc8c8097)。

命令状态。

## 43.2\_详细说明（Detailed Documentation）

<a id="a654c94fafac9cd72465a413de8266005"></a>

### `image_list`

```c
struct mcumgr_image_data* img_mgmt_client::image_list
```

映像列表缓冲区。

<a id="a2a2097f05111d6242d623a68959ecca9"></a>

### `image_list_length`

```c
int img_mgmt_client::image_list_length
```

客户端映像列表缓冲区大小。

<a id="a36abd266bbd1ea35849423708f9e816d"></a>

### `smp_client`

```c
struct smp_client_object* img_mgmt_client::smp_client
```

简单管理协议（SMP）的客户端对象。

<a id="a4fb8d168a6faf48c32903b71fc8c8097"></a>

### `status`

```c
int img_mgmt_client::status
```

命令状态。

<a id="a77559218adc5f7873366c56f9a02750e"></a>

### `upload`

```c
struct img_gr_upload img_mgmt_client::upload
```

供客户端内部使用的映像上传状态数据。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__client_8h_source.html)
- [smp_client_object](P078_smp_client_object_结构体.md)
- [img_gr_upload](P042_img_gr_upload_结构体.md)
- [mcumgr_image_data](P061_mcumgr_image_data_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_img_gr_upload_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_img_mgmt_image_confirmed_结构体.md)
