---
id: learning.zephyr-docs.api-source-runtime-reference.page-47
title: parser_state.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_parser\_state.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html)。

## 47.1\_原始可见代码（Source Code）

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
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
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
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a08e05eb8bc0a42e6e84fa22dd75bdc95"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a0d0a86b054a404f46184e4e7e41e0d26"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a0eeafcb1a1e4409ffd8c034be9af860d"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a159666494992773deef3d091d61efa64"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a16494186a1ec7a1e140af1b4eaa09d20"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a17f7885ac699f68b5179b74e264605d8"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a1ae8a6fc8117d6baa6a0812d077f5b73"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a1dfa1c7e958daff320dcca379e1891f2"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a1e52abf531e01c40b73cb9e8b3fdd9f4"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a209e6e32f0783f5d76fad26c46013390"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a246c6aaa49d61e24a43dbb1e4d601b2a"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a2a4dde0eafd4f5bcb5284744ccafe86a"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a2dc9752e25cc2a00c3c89bbdf9b0f23b"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a3159d98e8c993680b7640db1e6eed22c"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a3353eed9aa8e2fd854b9f82d3ac1bff1"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a36add21fb73304295cc924d6014c11ef"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a3c7bfb6f21eb5f914d33e49bd3ca4809"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a4581640a88dc9931031916da00dc9bc6"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a48289d7f47c2a74a9b9c498e5c8070c8"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a484786609cb1b307e43c55b5b3078435"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a490988d398dd839f49be96a79f1dcffe"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a49cdf111588eeedd1593e549fdb2b4b7"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a4aa98ee464114fd4b6a00b02d5a83a69"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a5a871b16732400896f13a0b4bf4d2d2e"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a5dd2f6b19fd4e3cb6b428e094ab7e443"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a63c8547a6c351def0a6d1d1529c90aad"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a641d4adec0c7f121153854eae440c2c3"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a64272a20486c8d0694704832aea24872"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a68c1b3800638f03d6ad0e3cb6da31acf"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a6c9131528d4f92c9b42361fcd943744a"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a726ed5570859dca67883ae410c1b9f5b"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a758a72c507e51909cd1ab0f84148ac3c"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a76ed9bbc2d835b88cb30299abcdd67e8"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a77eeb3ce03bff5e0a71d81e6689715ea"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a7c3dea78ecb0ee88212988ed0b90a5e7"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a80fae8bf0e824df045b912278ad0316d"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a85e4e4637f2bc962302e1ba3a3f5f769"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a8a068d6a93bae075f7ba5694c46d2de6"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90a94807fb310f4104dd03e2ddb1ab4ae9b"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90aa99f675903d976e1912fb54c5a71baa0"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90aac9df6a576e6b66610d1c78e0a0fce85"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90aad6b279013498df4ef81557cec965fe6"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90ab837338881e7c475bbaff41b146fc57d"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90abb02b342bbb8d22a763b55386db8c0fb"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90abe81888b100852a3ff950be05d2650fe"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90ac379ae76d71944b4daf9519e3b22a1a1"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90ac76a17504862a273d8cb490d612f9759"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90ad55e2affc1684fca9fc2d2dfa0ef02be"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90ae2c4dfd6dc9680c009c6e2554af4341d"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90ae4f0cd1ac4cbbc85edd6073bc27b85b7"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90ae58f59a3755eed3117db8930dc78c6ec"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90ae830ce7380ef6c61643a332ab63f6774"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90ae928e87617dbca34f86693408ffb8b08"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90aeadb7f8e79fd094e250279f8afec062f"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90aee2b77d4458cf570e1a7bab584ba5907"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90aef104c331e8e270e735d1aed0430d32e"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90aef8541c5f33f59dfbed9e429ecd92d21"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90aefa1bc8b7519ce8b995dc7e71e551f15"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90af5876995d7ba04281d118e845db8110d"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90af9d6a67a8cad297aa880c91180699409"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90afe0af478bf5e6e82c2d36dc6209fa72c"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90aff85ea02669f8cf3bae62121928668c0"></a>

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
#ifndef ZEPHYR_INCLUDE_NET_HTTP_PARSER_STATE_H_
#define ZEPHYR_INCLUDE_NET_HTTP_PARSER_STATE_H_
#ifdef __cplusplus
extern "C" {
#endif

enum state {
        s_dead = 1, /* important that this is > 0 */
        s_start_req_or_res,
        s_res_or_resp_H,
        s_start_res,
        s_res_H,
        s_res_HT,
        s_res_HTT,
        s_res_HTTP,
        s_res_first_http_major,
        s_res_http_major,
        s_res_first_http_minor,
        s_res_http_minor,
        s_res_first_status_code,
        s_res_status_code,
        s_res_status_start,
        s_res_status,
        s_res_line_almost_done,
        s_start_req,
        s_req_method,
        s_req_spaces_before_url,
        s_req_schema,
        s_req_schema_slash,
        s_req_schema_slash_slash,
        s_req_server_start,
        s_req_server,
        s_req_server_with_at,
        s_req_path,
        s_req_query_string_start,
        s_req_query_string,
        s_req_fragment_start,
        s_req_fragment,
        s_req_http_start,
        s_req_http_H,
        s_req_http_HT,
        s_req_http_HTT,
        s_req_http_HTTP,
        s_req_first_http_major,
        s_req_http_major,
        s_req_first_http_minor,
        s_req_http_minor,
        s_req_line_almost_done,
        s_header_field_start,
        s_header_field,
        s_header_value_discard_ws,
        s_header_value_discard_ws_almost_done,
        s_header_value_discard_lws,
        s_header_value_start,
        s_header_value,
        s_header_value_lws,
        s_header_almost_done,
        s_chunk_size_start,
        s_chunk_size,
        s_chunk_parameters,
        s_chunk_size_almost_done,
        s_headers_almost_done,
        s_headers_done,
        /* Important: 's_headers_done' must be the last 'header' state. All
         * states beyond this must be 'body' states. It is used for overflow
         * checking. See the PARSING_HEADER() macro.
         */
        s_chunk_data,
        s_chunk_data_almost_done,
        s_chunk_data_done,
        s_body_identity,
        s_body_identity_eof,
        s_message_done
};

#ifdef __cplusplus
}
#endif
#endif
```

## 47.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`MIT`。

### 注释 2：原第 3 行

版权（Copyright）归 Joyent, Inc. 及其他 Node 贡献者所有。保留所有权利（All rights reserved）。

特此免费授予任何获得本软件及相关文档文件（以下称“软件”）副本的人不受限制地处理本软件的许可，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售本软件副本的权利，以及允许获提供本软件的人实施上述行为的权利，但须符合以下条件：

上述版权声明和本许可声明必须包含在本软件的所有副本或实质性部分中。

本软件按“原样”（AS IS）提供，不附带任何形式的明示或默示担保，包括但不限于适销性、特定用途适用性以及不侵权的担保。无论是基于合同、侵权或其他诉讼事由，作者或版权持有人均不对因本软件、使用本软件或对本软件进行其他处理而产生、引起或相关的任何索赔、损害或其他责任承担责任。

### 注释 3：原第 30 行

此值必须大于 0，这一点很重要。

### 注释 4：原第 86 行

重要：`s_headers_done` 必须是最后一个头部状态（Header state）。其后的所有状态必须是正文状态（Body state）。此顺序用于溢出检查，参见 `PARSING_HEADER()` 宏。

## 47.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [s_dead](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90ae928e87617dbca34f86693408ffb8b08)
- [s_start_req_or_res](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a5a871b16732400896f13a0b4bf4d2d2e)
- [s_res_or_resp_H](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90ad55e2affc1684fca9fc2d2dfa0ef02be)
- [s_start_res](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a17f7885ac699f68b5179b74e264605d8)
- [s_res_H](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a1e52abf531e01c40b73cb9e8b3fdd9f4)
- [s_res_HT](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90aef104c331e8e270e735d1aed0430d32e)
- [s_res_HTT](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90aac9df6a576e6b66610d1c78e0a0fce85)
- [s_res_HTTP](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a49cdf111588eeedd1593e549fdb2b4b7)
- [s_res_first_http_major](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a758a72c507e51909cd1ab0f84148ac3c)
- [s_res_http_major](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a4581640a88dc9931031916da00dc9bc6)
- [s_res_first_http_minor](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a2a4dde0eafd4f5bcb5284744ccafe86a)
- [s_res_http_minor](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a76ed9bbc2d835b88cb30299abcdd67e8)
- [s_res_first_status_code](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a246c6aaa49d61e24a43dbb1e4d601b2a)
- [s_res_status_code](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90aefa1bc8b7519ce8b995dc7e71e551f15)
- [s_res_status_start](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90aef8541c5f33f59dfbed9e429ecd92d21)
- [s_res_status](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a3159d98e8c993680b7640db1e6eed22c)
- [s_res_line_almost_done](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a94807fb310f4104dd03e2ddb1ab4ae9b)
- [s_start_req](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a726ed5570859dca67883ae410c1b9f5b)
- [s_req_method](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a5dd2f6b19fd4e3cb6b428e094ab7e443)
- [s_req_spaces_before_url](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a48289d7f47c2a74a9b9c498e5c8070c8)
- [s_req_schema](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a77eeb3ce03bff5e0a71d81e6689715ea)
- [s_req_schema_slash](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90ac76a17504862a273d8cb490d612f9759)
- [s_req_schema_slash_slash](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a80fae8bf0e824df045b912278ad0316d)
- [s_req_server_start](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90afe0af478bf5e6e82c2d36dc6209fa72c)
- [s_req_server](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a68c1b3800638f03d6ad0e3cb6da31acf)
- [s_req_server_with_at](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a0d0a86b054a404f46184e4e7e41e0d26)
- [s_req_path](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a490988d398dd839f49be96a79f1dcffe)
- [s_req_query_string_start](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a3c7bfb6f21eb5f914d33e49bd3ca4809)
- [s_req_query_string](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a36add21fb73304295cc924d6014c11ef)
- [s_req_fragment_start](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90ae2c4dfd6dc9680c009c6e2554af4341d)
- [s_req_fragment](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90ac379ae76d71944b4daf9519e3b22a1a1)
- [s_req_http_start](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90aeadb7f8e79fd094e250279f8afec062f)
- [s_req_http_H](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a7c3dea78ecb0ee88212988ed0b90a5e7)
- [s_req_http_HT](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90ae4f0cd1ac4cbbc85edd6073bc27b85b7)
- [s_req_http_HTT](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90aee2b77d4458cf570e1a7bab584ba5907)
- [s_req_http_HTTP](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a641d4adec0c7f121153854eae440c2c3)
- [s_req_first_http_major](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a8a068d6a93bae075f7ba5694c46d2de6)
- [s_req_http_major](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90aad6b279013498df4ef81557cec965fe6)
- [s_req_first_http_minor](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90af5876995d7ba04281d118e845db8110d)
- [s_req_http_minor](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a64272a20486c8d0694704832aea24872)
- [s_req_line_almost_done](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90abb02b342bbb8d22a763b55386db8c0fb)
- [s_header_field_start](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a85e4e4637f2bc962302e1ba3a3f5f769)
- [s_header_field](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a3353eed9aa8e2fd854b9f82d3ac1bff1)
- [s_header_value_discard_ws](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90ae58f59a3755eed3117db8930dc78c6ec)
- [s_header_value_discard_ws_almost_done](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a0eeafcb1a1e4409ffd8c034be9af860d)
- [s_header_value_discard_lws](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a2dc9752e25cc2a00c3c89bbdf9b0f23b)
- [s_header_value_start](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90aa99f675903d976e1912fb54c5a71baa0)
- [s_header_value](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a4aa98ee464114fd4b6a00b02d5a83a69)
- [s_header_value_lws](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90ab837338881e7c475bbaff41b146fc57d)
- [s_header_almost_done](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a484786609cb1b307e43c55b5b3078435)
- [s_chunk_size_start](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90af9d6a67a8cad297aa880c91180699409)
- [s_chunk_size](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a63c8547a6c351def0a6d1d1529c90aad)
- [s_chunk_parameters](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a6c9131528d4f92c9b42361fcd943744a)
- [s_chunk_size_almost_done](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a16494186a1ec7a1e140af1b4eaa09d20)
- [s_headers_almost_done](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90abe81888b100852a3ff950be05d2650fe)
- [s_headers_done](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a209e6e32f0783f5d76fad26c46013390)
- [s_chunk_data](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a1dfa1c7e958daff320dcca379e1891f2)
- [s_chunk_data_almost_done](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90aff85ea02669f8cf3bae62121928668c0)
- [s_chunk_data_done](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a159666494992773deef3d091d61efa64)
- [s_body_identity](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a08e05eb8bc0a42e6e84fa22dd75bdc95)
- [s_body_identity_eof](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90a1ae8a6fc8117d6baa6a0812d077f5b73)
- [s_message_done](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90ae830ce7380ef6c61643a332ab63f6774)

---

[上一章](P046_nxp-fmeas.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P048_pinctrl_bcm2712_common.h_源码浏览.md)
