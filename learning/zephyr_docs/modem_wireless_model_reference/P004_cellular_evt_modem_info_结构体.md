---
id: learning.zephyr-docs.modem-wireless-model-reference.page-4
title: cellular_evt_modem_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcellular__evt__modem__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_cellular\_evt\_modem\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcellular__evt__modem__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CELLULAR_EVENT_MODEM_INFO_CHANGED事件的载荷（Payload）。

```c
#include <zephyr/drivers/cellular.h>
```

<a id="details"></a>

CELLULAR_EVENT_MODEM_INFO_CHANGED事件的载荷（Payload）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a4dde2a070347472bff450618ec6edc58"></a>

```c
enum cellular_modem_info_type field
```

相关声明：[cellular_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad6e38e31d82075c51933fcbb2ff2de30)、[field](#a4dde2a070347472bff450618ec6edc58)。

发生变化的字段。

## 4.2\_详细说明（Detailed Documentation）

<a id="a4dde2a070347472bff450618ec6edc58"></a>

### `field`

```c
enum cellular_modem_info_type cellular_evt_modem_info::field
```

发生变化的字段。

本数据类型文档由以下文件生成：

- `zephyr/drivers/cellular.h`

## 4.3\_原页交叉引用（Cross References）

- [CELLULAR_EVENT_MODEM_INFO_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411ab9c60898496e94d18b7c2535a0e904eb)
- [zephyr/drivers/cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h_source.html)
- [cellular_modem_info_type](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gad6e38e31d82075c51933fcbb2ff2de30)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_cellular_evt_modem_comms_check_result_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_cellular_evt_network_status_结构体.md)
