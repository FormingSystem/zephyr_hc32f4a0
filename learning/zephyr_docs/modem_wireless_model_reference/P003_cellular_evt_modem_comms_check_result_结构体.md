---
id: learning.zephyr-docs.modem-wireless-model-reference.page-3
title: cellular_evt_modem_comms_check_result_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcellular__evt__modem__comms__check__result.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_cellular\_evt\_modem\_comms\_check\_result\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcellular__evt__modem__comms__check__result.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT事件的载荷（Payload）。

```c
#include <zephyr/drivers/cellular.h>
```

<a id="details"></a>

CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT事件的载荷（Payload）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a86871d448e51af8535fffa445606f9a7"></a>

```c
bool success
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[success](#a86871d448e51af8535fffa445606f9a7)。

已成功检查与调制解调器的通信。

## 3.2\_详细说明（Detailed Documentation）

<a id="a86871d448e51af8535fffa445606f9a7"></a>

### `success`

```c
bool cellular_evt_modem_comms_check_result::success
```

已成功检查与调制解调器的通信。

本数据类型文档由以下文件生成：

- `zephyr/drivers/cellular.h`

## 3.3\_原页交叉引用（Cross References）

- [CELLULAR_EVENT_MODEM_COMMS_CHECK_RESULT](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#gga27c0b71128c782a7f42832b82eb94411a272d43454fa064bc4794d8fa64402910)
- [zephyr/drivers/cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_cellular_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_cellular_evt_modem_info_结构体.md)
