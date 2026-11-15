---
id: learning.zephyr-docs.modem-wireless-model-reference.page-39
title: mdm_hl7800_polte_registration_event_data_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmdm__hl7800__polte__registration__event__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_mdm\_hl7800\_polte\_registration\_event\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmdm__hl7800__polte__registration__event__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PoLTE注册结果（Registration Result）。

```c
#include <zephyr/drivers/modem/hl7800.h>
```

<a id="details"></a>

PoLTE注册结果（Registration Result）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_a1d591b3a469fb6fed674fb07455ed8d0"></a>

```c
int status
```

相关声明：[status](#a1d591b3a469fb6fed674fb07455ed8d0)。

负值表示 `errno`，0 表示成功。

<a id="r_adc8d2cee46aae9ed0736d85ab5805cb0"></a>

```c
char * user
```

相关声明：[user](#adc8d2cee46aae9ed0736d85ab5805cb0)。

PoLTE 用户名；`status` 非零时无效。

<a id="r_ad551f94f2488544e69f622d7d26f87d9"></a>

```c
char * password
```

相关声明：[password](#ad551f94f2488544e69f622d7d26f87d9)。

PoLTE 密码；`status` 非零时无效。

## 39.2\_详细说明（Detailed Documentation）

<a id="ad551f94f2488544e69f622d7d26f87d9"></a>

### `password`

```c
char* mdm_hl7800_polte_registration_event_data::password
```

PoLTE 密码；`status` 非零时无效。

<a id="a1d591b3a469fb6fed674fb07455ed8d0"></a>

### `status`

```c
int mdm_hl7800_polte_registration_event_data::status
```

负值表示 `errno`，0 表示成功。

<a id="adc8d2cee46aae9ed0736d85ab5805cb0"></a>

### `user`

```c
char* mdm_hl7800_polte_registration_event_data::user
```

PoLTE 用户名；`status` 非零时无效。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl7800.h`

## 39.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl7800.h](https://docs.zephyrproject.org/latest/doxygen/html/hl7800_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_mdm_hl7800_polte_location_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_mdm_hl7800_site_survey_结构体.md)
