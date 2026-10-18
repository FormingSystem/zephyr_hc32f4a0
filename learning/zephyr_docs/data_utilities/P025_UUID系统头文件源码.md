---
id: learning.zephyr-docs.data-utilities.api-25
title: UUID系统头文件源码
kind: reference
status: maintained
domains: [zephyr, data, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sys_2uuid_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_UUID系统头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sys_2uuid_8h_source.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 25.1\_阅读说明与来源

译注：本组是 `<zephyr/sys/uuid.h>` 的通用唯一标识符（Universally Unique Identifier，UUID）接口。先读[UUID 指南](P014_UUID通用唯一标识符.md)和[生成示例](P015_UUID生成示例.md)，再查询生成、比较、解析及编码转换。蓝牙专用 UUID 类型和接口另有官方页面，不与这里的 `struct uuid` 混用。

本组：[UUID生成与转换接口](P023_UUID生成与转换接口.md) · [UUID系统头文件](P024_UUID系统头文件.md) · [UUID系统头文件源码](P025_UUID系统头文件源码.md) · [UUID二进制结构](P026_UUID二进制结构.md)。

下方保留官方 Doxygen 源码浏览页展示的全部代码、标识符和版权／许可注释。仅移除网页行号，将展示用不换行空格还原为空格，并清除行尾空白。原页面已省略用于生成 API 文档的部分注释，行号原本存在跳跃；本展示不能替代完整原始头文件。接口、参数和结构体注释均在本组参考页翻译。

## 25.2\_原始源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="agroup__uuid_html_ga1ae245a3ed4e1780a7b4d0346ede1188"></a>
<a id="agroup__uuid_html_ga1d71eb34412c3e04f9f85bb8320548d6"></a>
<a id="agroup__uuid_html_ga1e1e2f008f5ac3366bf474de27d42b66"></a>
<a id="agroup__uuid_html_ga1fd6f837800e0bd9bd0e4c4e5891568e"></a>
<a id="agroup__uuid_html_ga2562309a55cbd49b70e1c60a761fb08f"></a>
<a id="agroup__uuid_html_ga2c73bd8b52693f1c28dbbc10e145e098"></a>
<a id="agroup__uuid_html_ga5db91c4b658dc322b42959cb5c851020"></a>
<a id="agroup__uuid_html_ga68dcce718b9e98d4873fe7c40d99ad4c"></a>
<a id="agroup__uuid_html_ga6d37dd9ad8391595db1b71ca2103a228"></a>
<a id="agroup__uuid_html_ga6f692b733f600e0346317f3d25d84409"></a>
<a id="agroup__uuid_html_ga91f227c01e8b6bc7b8df8f37a1632b36"></a>
<a id="agroup__uuid_html_gaac4b9f9b243c9ecbeac94f0b4947ede1"></a>
<a id="agroup__uuid_html_gacf4a46349ed1a7a6a44b3cc84c687bc1"></a>
<a id="agroup__uuid_html_gadf6084420d0ee8cc41a522ebb2c71e7d"></a>
<a id="agroup__uuid_html_gae28fa917e2f1ad587da4cf901f0de94a"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructuuid_html"></a>

```c
/*
 * Copyright (c) 2025, SECO Mind Srl
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SYS_UUID_H_
#define ZEPHYR_INCLUDE_SYS_UUID_H_


#include <zephyr/kernel.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif


#define UUID_SIZE 16U

#define UUID_STR_LEN 37U

#define UUID_BASE64_LEN 25U

#define UUID_BASE64URL_LEN 23U

struct uuid {
        uint8_t val[UUID_SIZE];
};

int uuid_generate_v4(struct uuid *out);

int uuid_generate_v5(const struct uuid *ns, const void *data, size_t data_size,
                     struct uuid *out);

int uuid_cmp(const struct uuid *a, const struct uuid *b);

bool uuid_is_nil(const struct uuid *data);

int uuid_copy(const struct uuid *data, struct uuid *out);

int uuid_from_buffer(const uint8_t data[UUID_SIZE], struct uuid *out);

int uuid_from_string(const char data[UUID_STR_LEN], struct uuid *out);

int uuid_to_buffer(const struct uuid *data, uint8_t out[UUID_SIZE]);

int uuid_to_string(const struct uuid *data, char out[UUID_STR_LEN]);

int uuid_to_base64(const struct uuid *data, char out[UUID_BASE64_LEN]);

int uuid_to_base64url(const struct uuid *data, char out[UUID_BASE64URL_LEN]);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SYS_UUID_H_ */
```

## 25.3\_源码注释译文

版权：2025 年 SECO Mind Srl；许可证标识为 `Apache-2.0`，原始署名保持不变。`ZEPHYR_INCLUDE_SYS_UUID_H_` 为头文件包含保护（Header Include Guard），`extern "C"` 为 C++ 调用方提供 C 链接约定。源码浏览页省略的生成、解析和转换注释已在[接口参考](P023_UUID生成与转换接口.md)中翻译；`INTERNAL_HIDDEN` 隐藏成员的含义见[二进制结构](P026_UUID二进制结构.md)。

## 25.4\_相关源码与使用边界

声明来自 `<zephyr/sys/uuid.h>`。可通过本仓库[对应头文件](../../../include/zephyr/sys/uuid.h)追踪源码；本仓库版本可能与官网 `latest` 不同。译注核对依据为保存的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/uuid.h)、[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/uuid/uuid.c)和[Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/uuid/Kconfig)，摘要见[来源记录](../SOURCES.md)。

[上一章](P024_UUID系统头文件.md) · [返回大纲](大纲.md) · [下一章](P026_UUID二进制结构.md)
