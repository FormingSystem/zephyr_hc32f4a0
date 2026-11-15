---
id: learning.zephyr-docs.crypto.api-32
title: JWT头文件源码
kind: reference
status: maintained
domains: [zephyr, crypto, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/jwt_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_JWT头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/jwt_8h_source.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 32.1\_阅读说明与来源

译注：配合[JSON Web Token 指南](P029_JSONWebToken指南.md)阅读。这里的构建器（Builder）生成包含固定声明（Claims）并经过签名的 JWT，接口没有提供任意声明编辑、令牌解析或验证功能。

本组：[JWT构建与签名接口](P030_JWT构建与签名接口.md) · [JWT头文件](P031_JWT头文件.md) · [JWT头文件源码](P032_JWT头文件源码.md) · [JWT构建器结构](P033_JWT构建器结构.md)。

下方保留官方 Doxygen 源码浏览页展示的全部代码、标识符和版权／许可注释。仅移除网页行号，将展示用不换行空格还原为空格，并清除行尾空白。原页面已省略用于生成 API 文档的部分注释，行号原本存在跳跃；本展示不能替代完整原始头文件。接口、参数和结构体注释均在本组参考页翻译。

## 32.2\_原始源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00023"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="agroup__jwt_html_ga209dc2bdbaf72b4c9d11be02e0ffe479"></a>
<a id="agroup__jwt_html_gaa000189c83e9b9113f401cd7d523cefe"></a>
<a id="agroup__jwt_html_gab10ee40ee3c0b3eea98051c2acbb8a75"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astructjwt__builder_html"></a>
<a id="astructjwt__builder_html_a23a0aa512e5bc66722b6d7a8cf20aa95"></a>
<a id="astructjwt__builder_html_a4bd0376eef7f162e9e9e1e1399388fed"></a>
<a id="astructjwt__builder_html_a74a3d3e645f8b438bcdf12abdf0aabf7"></a>
<a id="astructjwt__builder_html_a7e4880c8fc8136083bad0ef2559c67e4"></a>
<a id="astructjwt__builder_html_a8fcc85d6704b63cd773397a5a4d9774d"></a>
<a id="astructjwt__builder_html_af53cb40609f623b95ff68d3c66a387ce"></a>

```c
/*
 * Copyright (c) 2018 Linaro Ltd
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DATA_JWT_H_
#define ZEPHYR_INCLUDE_DATA_JWT_H_

#include <zephyr/types.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif


struct jwt_builder {
        char *base;

        char *buf;

        size_t len;

        bool overflowed;

        /* Pending bytes yet to be converted to base64. */
        unsigned char wip[3];

        /* Number of pending bytes. */
        int pending;
};

int jwt_init_builder(struct jwt_builder *builder,
                     char *buffer,
                     size_t buffer_size);

int jwt_add_payload(struct jwt_builder *builder,
                    int32_t exp,
                    int32_t iat,
                    const char *aud);

int jwt_sign(struct jwt_builder *builder,
             const char *der_key,
             size_t der_key_len);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DATA_JWT_H_ */
```

## 32.3\_源码注释译文

版权：2018 年 Linaro Ltd；许可证标识为 `Apache-2.0`，原始署名保持不变。`ZEPHYR_INCLUDE_DATA_JWT_H_` 是头文件包含保护（Header Include Guard），`extern "C"` 提供 C++ 调用的 C 链接约定。源码中 `Pending bytes yet to be converted to base64` 指尚待转换为 Base64 的字节；`Number of pending bytes` 指待处理字节数。API 注释见本组接口与结构参考。

## 32.4\_相关源码与使用边界

本仓库的[JWT 头文件](../../../include/zephyr/data/jwt.h)与[构建实现](../../../subsys/jwt/jwt.c)可用于源码追踪，版本可能与官网 `latest` 不同。译注核对依据为保存的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/data/jwt.h)、[官方构建实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/jwt.c)与[PSA 签名后端](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/jwt/jwt_psa.c)，摘要见[来源记录](../SOURCES.md)。

[上一章](P031_JWT头文件.md) · [返回大纲](大纲.md) · [下一章](P033_JWT构建器结构.md)
