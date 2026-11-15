---
id: learning.zephyr-docs.system-service-model-reference.page-62
title: mcumgr_image_list_flags_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmcumgr__image__list__flags.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_mcumgr\_image\_list\_flags\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmcumgr__image__list__flags.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

映像列表标志（Image List Flags）。

```c
#include <zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h>
```

<a id="details"></a>

映像列表标志（Image List Flags）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_acb12d5ae0c75e9dac48874e542784bd3"></a>

```c
bool bootable: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[bootable](#acb12d5ae0c75e9dac48874e542784bd3)。

可启动映像（Bootable image）。

<a id="r_a744597f98d3092de161512d0817bb1a2"></a>

```c
bool pending: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[pending](#a744597f98d3092de161512d0817bb1a2)。

待处理更新状态（Pending update state）。

<a id="r_ad3ff9c0acbcf2ebbb5f6820b38705bff"></a>

```c
bool confirmed: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[confirmed](#ad3ff9c0acbcf2ebbb5f6820b38705bff)。

已确认映像（Confirmed image）。

<a id="r_ade2a01aeeede96070bcdf33ce2d949fb"></a>

```c
bool active: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[active](#ade2a01aeeede96070bcdf33ce2d949fb)。

活动映像（Active image）。

<a id="r_af7c7b565ef02ea95c7486949a29164c1"></a>

```c
bool permanent: 1
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[permanent](#af7c7b565ef02ea95c7486949a29164c1)。

永久映像状态（Permanent image state）。

## 62.2\_详细说明（Detailed Documentation）

<a id="ade2a01aeeede96070bcdf33ce2d949fb"></a>

### `active`

```c
bool mcumgr_image_list_flags::active
```

活动映像（Active image）。

<a id="acb12d5ae0c75e9dac48874e542784bd3"></a>

### `bootable`

```c
bool mcumgr_image_list_flags::bootable
```

可启动映像（Bootable image）。

<a id="ad3ff9c0acbcf2ebbb5f6820b38705bff"></a>

### `confirmed`

```c
bool mcumgr_image_list_flags::confirmed
```

已确认映像（Confirmed image）。

<a id="a744597f98d3092de161512d0817bb1a2"></a>

### `pending`

```c
bool mcumgr_image_list_flags::pending
```

待处理更新状态（Pending update state）。

<a id="af7c7b565ef02ea95c7486949a29164c1"></a>

### `permanent`

```c
bool mcumgr_image_list_flags::permanent
```

永久映像状态（Permanent image state）。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt_client.h](https://docs.zephyrproject.org/latest/doxygen/html/img__mgmt__client_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_mcumgr_image_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_mcumgr_image_state_结构体.md)
