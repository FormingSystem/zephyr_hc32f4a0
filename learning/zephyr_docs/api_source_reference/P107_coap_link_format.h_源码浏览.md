---
id: learning.zephyr-docs.api-source-reference.page-107
title: coap_link_format.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap__link__format_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第107章\_coap\_link\_format.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/coap__link__format_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/coap__link__format_8h.html)。

## 107.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="foldopen00072"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="agroup__coap_html_ga3f2eded87dbeb7408ff6f07e04afb30b"></a>
<a id="agroup__coap_html_ga49d63f12b593d7509690a504b05da730"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructcoap__core__metadata_html"></a>
<a id="astructcoap__core__metadata_html_a74e8a533d7f8596498d5d0ce2afc102f"></a>
<a id="astructcoap__core__metadata_html_aeb04ef8b47ecc144dd036007cccd2e59"></a>
<a id="astructcoap__packet_html"></a>
<a id="astructcoap__resource_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_COAP_LINK_FORMAT_H_
#define ZEPHYR_INCLUDE_NET_COAP_LINK_FORMAT_H_


#ifdef __cplusplus
extern "C" {
#endif

#define COAP_WELL_KNOWN_CORE_PATH \
        ((const char * const[]) { ".well-known", "core", NULL })

int coap_well_known_core_get(struct coap_resource *resource,
                             const struct coap_packet *request,
                             struct coap_packet *response,
                             uint8_t *data, uint16_t data_len);

int coap_well_known_core_get_len(struct coap_resource *resources,
                                 size_t resources_len,
                                 const struct coap_packet *request,
                                 struct coap_packet *response,
                                 uint8_t *data, uint16_t data_len);

struct coap_core_metadata {
        const char * const *attributes;
        void *user_data;
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_COAP_LINK_FORMAT_H_ */
```

## 107.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 87 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_COAP_LINK_FORMAT_H_`。

## 107.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/coap__link__format_8h.html)
- [coap_well_known_core_get](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3f2eded87dbeb7408ff6f07e04afb30b)
- [coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)
- [coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [coap_well_known_core_get_len](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga49d63f12b593d7509690a504b05da730)
- [coap_core_metadata](../network_application_model_reference/P008_coap_core_metadata_结构体.md)
- [attributes](../network_application_model_reference/P008_coap_core_metadata_结构体.md#aeb04ef8b47ecc144dd036007cccd2e59)
- [user_data](../network_application_model_reference/P008_coap_core_metadata_结构体.md#a74e8a533d7f8596498d5d0ce2afc102f)
- [coap_core_metadata::user_data](../network_application_model_reference/P008_coap_core_metadata_结构体.md#a74e8a533d7f8596498d5d0ce2afc102f)
- [coap_core_metadata::attributes](../network_application_model_reference/P008_coap_core_metadata_结构体.md#aeb04ef8b47ecc144dd036007cccd2e59)

---

[上一章](P106_cmsis_types.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P108_coap_oscore.h_源码浏览.md)
