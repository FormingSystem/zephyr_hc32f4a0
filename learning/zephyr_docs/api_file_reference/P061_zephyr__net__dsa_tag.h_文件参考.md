---
id: learning.zephyr-docs.api-file-reference.page-61
title: zephyr__net__dsa_tag.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dsa__tag_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_zephyr\_\_net\_\_dsa\_tag.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dsa__tag_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

分布式交换架构（DSA）标签协议（Tag Protocol）的定义。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/ethernet/dsa_tag_proto.h>
```

查看此文件的源码。

分布式交换架构（DSA）标签协议（Tag Protocol）的定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 61.1\_数据结构（Data Structures）

<a id="r_dsa_5Ftag_5Fregister"></a>

```c
struct dsa_tag_register
```

相关声明：[dsa_tag_register](../network_service_model_reference/P005_dsa_tag_register_结构体.md)。

DSA标签协议（Tag Protocol）的注册信息。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 61.2\_宏定义（Macros）

<a id="r_ga7521cd5f21d007217c03a250922aa7b3"></a>

```c
#define DSA_TAG_REGISTER(_proto, _recv, _xmit)
```

相关声明：[DSA_TAG_REGISTER](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__tag.html#ga7521cd5f21d007217c03a250922aa7b3)。


## 61.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/ethernet/dsa_tag_proto.h](../api_source_configuration_reference/P020_dsa_tag_proto.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P015_dsa_tag.h_源码浏览.md)
- [dsa_tag_register](../network_service_model_reference/P005_dsa_tag_register_结构体.md)
- [DSA_TAG_REGISTER](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__tag.html#ga7521cd5f21d007217c03a250922aa7b3)

<a id="header-details"></a>

---

[上一章](P060_zephyr__drivers__sensor__mtch9010.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P062_zephyr__dt-bindings__ethernet__dsa_tag_proto.h_文件参考.md)
