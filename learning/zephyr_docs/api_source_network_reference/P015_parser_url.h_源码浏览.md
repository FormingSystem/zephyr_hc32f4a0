---
id: learning.zephyr-docs.api-source-network-reference.page-15
title: parser_url.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/parser__url_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_parser\_url.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/parser__url_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md)。

## 15.1\_原始可见代码（Source Code）

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
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00035"></a>
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
<a id="foldopen00053"></a>
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
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="aparser__state_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aparser__url_8h_html_a64e907d36fbcc883033c6bbe5a78b1b3"></a>
<a id="aparser__url_8h_html_a9ca1f91c2958091e2ac9e9b2f903d4eb"></a>
<a id="aparser__url_8h_html_a9ca1f91c2958091e2ac9e9b2f903d4eba32fb35461b96b6872f1427b2d51d1c30"></a>
<a id="aparser__url_8h_html_a9ca1f91c2958091e2ac9e9b2f903d4eba357b6dc1326ed55be377b0d839e8ca0f"></a>
<a id="aparser__url_8h_html_a9ca1f91c2958091e2ac9e9b2f903d4eba4b40c88291e4fa018de04553e7e1adfd"></a>
<a id="aparser__url_8h_html_a9ca1f91c2958091e2ac9e9b2f903d4eba86b9abfa220db7b834490d8b36e915af"></a>
<a id="aparser__url_8h_html_a9ca1f91c2958091e2ac9e9b2f903d4ebab2b8b31b30d6bc897dde653f6cc9f06c"></a>
<a id="aparser__url_8h_html_a9ca1f91c2958091e2ac9e9b2f903d4ebabc8500a49ccad1cd91d66d1eefb503cc"></a>
<a id="aparser__url_8h_html_a9ca1f91c2958091e2ac9e9b2f903d4ebacb4a85c6a7d6cd0b64ec6e91e7ba8689"></a>
<a id="aparser__url_8h_html_a9ca1f91c2958091e2ac9e9b2f903d4ebaf2aeb0b896645bd8100ca0f1e263a12f"></a>
<a id="aparser__url_8h_html_a9f477f452dcabd0d22f4a96ce0bfda57"></a>
<a id="aparser__url_8h_html_aeb269310a348fd68fd001b30b690fc83"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructhttp__parser__url_html"></a>
<a id="astructhttp__parser__url_html_a60fb784a989dd5a95e5bd19d468d22c7"></a>
<a id="astructhttp__parser__url_html_a6510826f3aa9a1100ac5f714323edeb1"></a>
<a id="astructhttp__parser__url_html_a77af61a480f11c41938810dd76ca49eb"></a>
<a id="astructhttp__parser__url_html_a875fb8faf3ee45707078eda5435fa563"></a>
<a id="astructhttp__parser__url_html_a911c18d1fc54309a7665d942c55cfae9"></a>

```c
/* SPDX-License-Identifier: MIT */

/* Copyright Joyent, Inc. and other Node contributors. All rights reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */
#ifndef ZEPHYR_INCLUDE_NET_HTTP_PARSER_URL_H_
#define ZEPHYR_INCLUDE_NET_HTTP_PARSER_URL_H_

#include <sys/types.h>
#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/net/http/parser_state.h>

#ifdef __cplusplus
extern "C" {
#endif

enum http_parser_url_fields {
          UF_SCHEMA           = 0
        , UF_HOST             = 1
        , UF_PORT             = 2
        , UF_PATH             = 3
        , UF_QUERY            = 4
        , UF_FRAGMENT         = 5
        , UF_USERINFO         = 6
        , UF_MAX              = 7
};

/* Result structure for http_parser_url_fields().
 *
 * Callers should index into field_data[] with UF_* values iff field_set
 * has the relevant (1 << UF_*) bit set. As a courtesy to clients (and
 * because we probably have padding left over), we convert any port to
 * a uint16_t.
 */
struct http_parser_url {
        uint16_t field_set;           /* Bitmask of (1 << UF_*) values */
        uint16_t port;                /* Converted UF_PORT string */

        struct {
                uint16_t off;               /* Offset into buffer in which field
                                          * starts
                                          */
                uint16_t len;               /* Length of run in buffer */
        } field_data[UF_MAX];
};

enum state parse_url_char(enum state s, const char ch);

/* Initialize all http_parser_url members to 0 */
void http_parser_url_init(struct http_parser_url *u);

/* Parse a URL; return nonzero on failure */
int http_parser_parse_url(const char *buf, size_t buflen,
                          int is_connect, struct http_parser_url *u);

#ifdef __cplusplus
}
#endif
#endif
```

## 15.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`MIT`。

### 注释 2：原第 3 行

版权（Copyright）归 Joyent, Inc. 及其他 Node 贡献者所有。保留所有权利（All rights reserved）。

特此免费授予任何获得本软件及相关文档文件（以下称“软件”）副本的人不受限制地处理本软件的许可，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售本软件副本的权利，以及允许获提供本软件的人实施上述行为的权利，但须符合以下条件：

上述版权声明和本许可声明必须包含在本软件的所有副本或实质性部分中。

本软件按“原样”（AS IS）提供，不附带任何形式的明示或默示担保，包括但不限于适销性、特定用途适用性以及不侵权的担保。无论是基于合同、侵权或其他诉讼事由，作者或版权持有人均不对因本软件、使用本软件或对本软件进行其他处理而产生、引起或相关的任何索赔、损害或其他责任承担责任。

### 注释 3：原第 46 行

`http_parser_url_fields()` 的结果结构体（result structure）。

当且仅当 `field_set` 中相应的 `(1 << UF_*)` 位已置位时，调用方才应使用 `UF_*` 值索引 `field_data[]`。为了方便调用方（而且结构体中可能还有剩余的填充空间），端口号会转换为 `uint16_t`。

### 注释 4：原第 54 行

由 `(1 << UF_*)` 值组成的位掩码（bitmask）。

### 注释 5：原第 55 行

由 `UF_PORT` 字符串转换得到的值。

### 注释 6：原第 58 行

字段起始位置相对于缓冲区（buffer）的偏移量。

### 注释 7：原第 61 行

缓冲区内这段数据的长度。

### 注释 8：原第 67 行

将 `http_parser_url` 的所有成员初始化为 0。

### 注释 9：原第 70 行

解析 URL；失败时返回非零值。

## 15.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md)
- [sys/types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/net/http/parser_state.h](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md)
- [http_parser_url_fields](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md#a9ca1f91c2958091e2ac9e9b2f903d4eb)
- [UF_SCHEMA](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md#a9ca1f91c2958091e2ac9e9b2f903d4ebab2b8b31b30d6bc897dde653f6cc9f06c)
- [UF_HOST](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md#a9ca1f91c2958091e2ac9e9b2f903d4ebaf2aeb0b896645bd8100ca0f1e263a12f)
- [UF_PORT](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md#a9ca1f91c2958091e2ac9e9b2f903d4eba357b6dc1326ed55be377b0d839e8ca0f)
- [UF_PATH](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md#a9ca1f91c2958091e2ac9e9b2f903d4eba86b9abfa220db7b834490d8b36e915af)
- [UF_QUERY](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md#a9ca1f91c2958091e2ac9e9b2f903d4ebabc8500a49ccad1cd91d66d1eefb503cc)
- [UF_FRAGMENT](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md#a9ca1f91c2958091e2ac9e9b2f903d4eba32fb35461b96b6872f1427b2d51d1c30)
- [UF_USERINFO](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md#a9ca1f91c2958091e2ac9e9b2f903d4ebacb4a85c6a7d6cd0b64ec6e91e7ba8689)
- [UF_MAX](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md#a9ca1f91c2958091e2ac9e9b2f903d4eba4b40c88291e4fa018de04553e7e1adfd)
- [http_parser_url](../network_application_model_reference/P034_http_parser_url_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [field_set](../network_application_model_reference/P034_http_parser_url_结构体.md#a77af61a480f11c41938810dd76ca49eb)
- [port](../network_application_model_reference/P034_http_parser_url_结构体.md#a875fb8faf3ee45707078eda5435fa563)
- [off](../network_application_model_reference/P034_http_parser_url_结构体.md#a6510826f3aa9a1100ac5f714323edeb1)
- [len](../network_application_model_reference/P034_http_parser_url_结构体.md#a60fb784a989dd5a95e5bd19d468d22c7)
- [field_data](../network_application_model_reference/P034_http_parser_url_结构体.md#a911c18d1fc54309a7665d942c55cfae9)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [parse_url_char](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md#a9f477f452dcabd0d22f4a96ce0bfda57)
- [http_parser_url_init](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md#a64e907d36fbcc883033c6bbe5a78b1b3)
- [http_parser_parse_url](../api_file_reference/P292_zephyr__net__http__parser_url.h_文件参考.md#aeb269310a348fd68fd001b30b690fc83)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [parser_state.h](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md)
- [http_parser_url::len](../network_application_model_reference/P034_http_parser_url_结构体.md#a60fb784a989dd5a95e5bd19d468d22c7)
- [http_parser_url::off](../network_application_model_reference/P034_http_parser_url_结构体.md#a6510826f3aa9a1100ac5f714323edeb1)
- [http_parser_url::field_set](../network_application_model_reference/P034_http_parser_url_结构体.md#a77af61a480f11c41938810dd76ca49eb)
- [http_parser_url::port](../network_application_model_reference/P034_http_parser_url_结构体.md#a875fb8faf3ee45707078eda5435fa563)
- [http_parser_url::field_data](../network_application_model_reference/P034_http_parser_url_结构体.md#a911c18d1fc54309a7665d942c55cfae9)

---

[上一章](P014_nxp_pint.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P016_pinctrl-rza2m.h_源码浏览.md)
