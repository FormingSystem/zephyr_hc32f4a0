---
id: learning.zephyr-docs.api-file-configuration-reference.page-12
title: zephyr__net__coap_link_format.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap__link__format_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_net\_\_coap\_link\_format.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/coap__link__format_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Zephyr的受限应用协议（CoAP）实现。

查看此文件的源码。

<a id="details"></a>

Zephyr的受限应用协议（CoAP）实现。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_coap_5Fcore_5Fmetadata"></a>

```c
struct coap_core_metadata
```

相关声明：[coap_core_metadata](../network_application_model_reference/P008_coap_core_metadata_结构体.md)。

如果需要为“well-known/core”虚拟资源包含的资源添加属性，应让metadata字段指向有效的coap_core_metadata结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="r_ga09d2c727fc6fc76aa9d908b759a3f40b"></a>

```c
#define COAP_WELL_KNOWN_CORE_PATH ((const char * const[]) { ".well-known", "core", NULL })
```

相关声明：[COAP_WELL_KNOWN_CORE_PATH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga09d2c727fc6fc76aa9d908b759a3f40b)。

若要将此资源（Resource）与 `coap_well_known_core_get` 配合使用，必须在添加所有应包含在 `.well-known/core` 资源响应中的其他资源之前，先添加此资源。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.3\_函数（Functions）

<a id="r_ga3f2eded87dbeb7408ff6f07e04afb30b"></a>

```c
int coap_well_known_core_get (struct coap_resource *resource, const struct coap_packet *request, struct coap_packet *response, uint8_t *data, uint16_t data_len)
```

相关声明：[coap_well_known_core_get](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3f2eded87dbeb7408ff6f07e04afb30b)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

为 `.well-known/core` CoAP 请求（Request）构造 CoAP 响应（Response）。

<a id="r_ga49d63f12b593d7509690a504b05da730"></a>

```c
int coap_well_known_core_get_len (struct coap_resource *resources, size_t resources_len, const struct coap_packet *request, struct coap_packet *response, uint8_t *data, uint16_t data_len)
```

相关声明：[coap_well_known_core_get_len](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga49d63f12b593d7509690a504b05da730)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

为 `.well-known/core` CoAP 请求（Request）构造 CoAP 响应（Response）。


## 12.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P107_coap_link_format.h_源码浏览.md)
- [coap_core_metadata](../network_application_model_reference/P008_coap_core_metadata_结构体.md)
- [COAP_WELL_KNOWN_CORE_PATH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga09d2c727fc6fc76aa9d908b759a3f40b)
- [coap_well_known_core_get](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3f2eded87dbeb7408ff6f07e04afb30b)
- [coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)
- [coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [coap_well_known_core_get_len](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga49d63f12b593d7509690a504b05da730)

<a id="header-details"></a>

---

[上一章](P011_zephyr__drivers__sensor__bmm350.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__drivers__haptics__cs40l26.h_文件参考.md)
