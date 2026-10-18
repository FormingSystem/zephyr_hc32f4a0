---
id: learning.zephyr-docs.api-platform-topic-reference.page-14
title: 分布式交换架构标签协议（DSA tag protocol）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__tag.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_分布式交换架构标签协议（DSA tag protocol）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__tag.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分布式交换架构（DSA）标签协议（Tag Protocol）的定义。

<a id="details"></a>

分布式交换架构标签协议（DSA Tag Protocol）的定义。

自 4.4 版提供（Since 4.4）；接口版本（Version）0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_dsa_5Ftag_5Fregister"></a>

```c
struct dsa_tag_register
```

相关声明：[dsa_tag_register](../network_service_model_reference/P005_dsa_tag_register_结构体.md)。

DSA标签协议（Tag Protocol）的注册信息。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="r_ga7521cd5f21d007217c03a250922aa7b3"></a>

```c
#define DSA_TAG_REGISTER(_proto, _recv, _xmit)
```

相关声明：[DSA_TAG_REGISTER](#ga7521cd5f21d007217c03a250922aa7b3)。

## 14.3\_详细说明（Detailed Documentation）

<a id="ga7521cd5f21d007217c03a250922aa7b3"></a>

### `DSA_TAG_REGISTER`

```c
#define DSA_TAG_REGISTER ( _proto, _recv, _xmit )
```

```c
#include <zephyr/net/dsa_tag.h>
```

展开值（Value）：

```c
static const STRUCT_SECTION_ITERABLE(dsa_tag_register, __dsa_tag_register_##_proto) = {    \
        .proto = _proto,                                                                   \
        .recv = _recv,                                                                     \
        .xmit = _xmit,                                                                     \
}
```


## 14.4\_原页交叉引用（Cross References）

- [dsa_tag_register](../network_service_model_reference/P005_dsa_tag_register_结构体.md)
- [zephyr/net/dsa_tag.h](../api_file_reference/P061_zephyr__net__dsa_tag.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructdsa__tag__register_html"></a>

---

[上一章](P013_DAI 驱动后端 API（Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P015_Espressif ESP32 中断分配器（Interrupt allocator）.md)
