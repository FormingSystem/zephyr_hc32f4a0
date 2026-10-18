---
id: learning.zephyr-docs.modem-wireless-model-reference.page-6
title: cellular_evt_registration_status_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcellular__evt__registration__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_cellular\_evt\_registration\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcellular__evt__registration__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CELLULAR_EVENT_REGISTRATION_STATUS_CHANGED事件的载荷（Payload）。

```c
#include <zephyr/drivers/cellular.h>
```

<a id="details"></a>

CELLULAR_EVENT_REGISTRATION_STATUS_CHANGED事件的载荷（Payload）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_a24432c0d1d942d08e4d7daa55c3fce51"></a>

```c
enum cellular_registration_status status
```

相关声明：[cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)、[status](#a24432c0d1d942d08e4d7daa55c3fce51)。

新的注册状态。

## 6.2\_详细说明（Detailed Documentation）

<a id="a24432c0d1d942d08e4d7daa55c3fce51"></a>

### `status`

```c
enum cellular_registration_status cellular_evt_registration_status::status
```

新的注册状态。

本数据类型文档由以下文件生成：

- `zephyr/drivers/cellular.h`

## 6.3\_原页交叉引用（Cross References）

- [CELLULAR_EVENT_REGISTRATION_STATUS_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411abef0b770a0cab6c6efd2ccf58345f27a)
- [zephyr/drivers/cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h_source.html)
- [cellular_registration_status](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga7309390ed507748fdb72cf078b8e08a4)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_cellular_evt_network_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_cellular_network_结构体.md)
