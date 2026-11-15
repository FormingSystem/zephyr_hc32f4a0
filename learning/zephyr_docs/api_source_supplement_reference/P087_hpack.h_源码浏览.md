---
id: learning.zephyr-docs.api-source-supplement-reference.page-87
title: hpack.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hpack_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第87章\_hpack.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hpack_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hpack_8h.html)。

## 87.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00017"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructhttp__hpack__header__buf_html"></a>
<a id="astructhttp__hpack__header__buf_html_a48291a396efc761d85ffb5f46ddddf07"></a>
<a id="astructhttp__hpack__header__buf_html_a6d1d09942d85f148e3979cf88f1cb87a"></a>
<a id="astructhttp__hpack__header__buf_html_a957db215f89359b64a76e98e878e8c83"></a>
<a id="astructhttp__hpack__header__buf_html_a9d1c7d2daaf55f201c03e7438b033abf"></a>
<a id="astructhttp__hpack__header__buf_html_ac0b781b733a16dc0c9e99753a4d2b25d"></a>
<a id="astructhttp__hpack__header__buf_html_ad6079192782eec8e4a0c1d89018c6d7b"></a>

```c


/*
 * Copyright (c) 2023 Emna Rekik
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_HTTP_HPACK_H_
#define ZEPHYR_INCLUDE_NET_HTTP_HPACK_H_

#include <stddef.h>
#include <stdint.h>


#ifdef __cplusplus
extern "C" {
#endif


enum http_hpack_static_key {
        HTTP_SERVER_HPACK_INVALID = 0,
        HTTP_SERVER_HPACK_AUTHORITY = 1,
        HTTP_SERVER_HPACK_METHOD_GET = 2,
        HTTP_SERVER_HPACK_METHOD_POST = 3,
        HTTP_SERVER_HPACK_PATH_ROOT = 4,
        HTTP_SERVER_HPACK_PATH_INDEX = 5,
        HTTP_SERVER_HPACK_SCHEME_HTTP = 6,
        HTTP_SERVER_HPACK_SCHEME_HTTPS = 7,
        HTTP_SERVER_HPACK_STATUS_200 = 8,
        HTTP_SERVER_HPACK_STATUS_204 = 9,
        HTTP_SERVER_HPACK_STATUS_206 = 10,
        HTTP_SERVER_HPACK_STATUS_304 = 11,
        HTTP_SERVER_HPACK_STATUS_400 = 12,
        HTTP_SERVER_HPACK_STATUS_404 = 13,
        HTTP_SERVER_HPACK_STATUS_500 = 14,
        HTTP_SERVER_HPACK_ACCEPT_CHARSET = 15,
        HTTP_SERVER_HPACK_ACCEPT_ENCODING = 16,
        HTTP_SERVER_HPACK_ACCEPT_LANGUAGE = 17,
        HTTP_SERVER_HPACK_ACCEPT_RANGES = 18,
        HTTP_SERVER_HPACK_ACCEPT = 19,
        HTTP_SERVER_HPACK_ACCESS_CONTROL_ALLOW_ORIGIN = 20,
        HTTP_SERVER_HPACK_AGE = 21,
        HTTP_SERVER_HPACK_ALLOW = 22,
        HTTP_SERVER_HPACK_AUTHORIZATION = 23,
        HTTP_SERVER_HPACK_CACHE_CONTROL = 24,
        HTTP_SERVER_HPACK_CONTENT_DISPOSITION = 25,
        HTTP_SERVER_HPACK_CONTENT_ENCODING = 26,
        HTTP_SERVER_HPACK_CONTENT_LANGUAGE = 27,
        HTTP_SERVER_HPACK_CONTENT_LENGTH = 28,
        HTTP_SERVER_HPACK_CONTENT_LOCATION = 29,
        HTTP_SERVER_HPACK_CONTENT_RANGE = 30,
        HTTP_SERVER_HPACK_CONTENT_TYPE = 31,
        HTTP_SERVER_HPACK_COOKIE = 32,
        HTTP_SERVER_HPACK_DATE = 33,
        HTTP_SERVER_HPACK_ETAG = 34,
        HTTP_SERVER_HPACK_EXPECT = 35,
        HTTP_SERVER_HPACK_EXPIRES = 36,
        HTTP_SERVER_HPACK_FROM = 37,
        HTTP_SERVER_HPACK_HOST = 38,
        HTTP_SERVER_HPACK_IF_MATCH = 39,
        HTTP_SERVER_HPACK_IF_MODIFIED_SINCE = 40,
        HTTP_SERVER_HPACK_IF_NONE_MATCH = 41,
        HTTP_SERVER_HPACK_IF_RANGE = 42,
        HTTP_SERVER_HPACK_IF_UNMODIFIED_SINCE = 43,
        HTTP_SERVER_HPACK_LAST_MODIFIED = 44,
        HTTP_SERVER_HPACK_LINK = 45,
        HTTP_SERVER_HPACK_LOCATION = 46,
        HTTP_SERVER_HPACK_MAX_FORWARDS = 47,
        HTTP_SERVER_HPACK_PROXY_AUTHENTICATE = 48,
        HTTP_SERVER_HPACK_PROXY_AUTHORIZATION = 49,
        HTTP_SERVER_HPACK_RANGE = 50,
        HTTP_SERVER_HPACK_REFERER = 51,
        HTTP_SERVER_HPACK_REFRESH = 52,
        HTTP_SERVER_HPACK_RETRY_AFTER = 53,
        HTTP_SERVER_HPACK_SERVER = 54,
        HTTP_SERVER_HPACK_SET_COOKIE = 55,
        HTTP_SERVER_HPACK_STRICT_TRANSPORT_SECURITY = 56,
        HTTP_SERVER_HPACK_TRANSFER_ENCODING = 57,
        HTTP_SERVER_HPACK_USER_AGENT = 58,
        HTTP_SERVER_HPACK_VARY = 59,
        HTTP_SERVER_HPACK_VIA = 60,
        HTTP_SERVER_HPACK_WWW_AUTHENTICATE = 61,
};

/* TODO Kconfig */
#define HTTP2_HEADER_FIELD_MAX_LEN 256

#if defined(CONFIG_HTTP_SERVER)
#define HTTP_SERVER_HUFFMAN_DECODE_BUFFER_SIZE CONFIG_HTTP_SERVER_HUFFMAN_DECODE_BUFFER_SIZE
#else
#define HTTP_SERVER_HUFFMAN_DECODE_BUFFER_SIZE 0
#endif


struct http_hpack_header_buf {
        const char *name;

        const char *value;

        size_t name_len;

        size_t value_len;

        uint8_t buf[HTTP_SERVER_HUFFMAN_DECODE_BUFFER_SIZE];

        size_t datalen;
};


int http_hpack_huffman_decode(const uint8_t *encoded_buf, size_t encoded_len,
                              uint8_t *buf, size_t buflen);
int http_hpack_huffman_encode(const uint8_t *str, size_t str_len,
                              uint8_t *buf, size_t buflen);
int http_hpack_decode_header(const uint8_t *buf, size_t datalen,
                             struct http_hpack_header_buf *header);
int http_hpack_encode_header(uint8_t *buf, size_t buflen,
                             struct http_hpack_header_buf *header);


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_HTTP_HPACK_H_ */
```

## 87.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2023 Emna Rekik。

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 98 行

待办（TODO）：Kconfig。

### 注释 3：原第 151 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_HTTP_HPACK_H_`。

## 87.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hpack_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [http_hpack_header_buf](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md)
- [name](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md#ac0b781b733a16dc0c9e99753a4d2b25d)
- [value](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md#a957db215f89359b64a76e98e878e8c83)
- [name_len](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md#ad6079192782eec8e4a0c1d89018c6d7b)
- [value_len](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md#a48291a396efc761d85ffb5f46ddddf07)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [buf](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md#a6d1d09942d85f148e3979cf88f1cb87a)
- [datalen](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md#a9d1c7d2daaf55f201c03e7438b033abf)
- [http_hpack_header_buf::value_len](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md#a48291a396efc761d85ffb5f46ddddf07)
- [http_hpack_header_buf::buf](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md#a6d1d09942d85f148e3979cf88f1cb87a)
- [http_hpack_header_buf::value](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md#a957db215f89359b64a76e98e878e8c83)
- [http_hpack_header_buf::datalen](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md#a9d1c7d2daaf55f201c03e7438b033abf)
- [http_hpack_header_buf::name](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md#ac0b781b733a16dc0c9e99753a4d2b25d)
- [http_hpack_header_buf::name_len](../network_application_model_reference/P031_http_hpack_header_buf_结构体.md#ad6079192782eec8e4a0c1d89018c6d7b)

---

[上一章](P086_hdlc_rcp_if.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P088_client.h_源码浏览.md)
