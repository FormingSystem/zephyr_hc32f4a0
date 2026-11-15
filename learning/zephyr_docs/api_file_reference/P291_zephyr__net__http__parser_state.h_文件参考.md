---
id: learning.zephyr-docs.api-file-reference.page-291
title: zephyr__net__http__parser_state.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第291章\_zephyr\_\_net\_\_http\_\_parser\_state.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 291.1\_枚举（Enumerations）

<a id="r_adc6e5733fc3c22f0a7b2914188c49c90"></a>

```c
enum state { s_dead = 1 , s_start_req_or_res , s_res_or_resp_H , s_start_res , s_res_H , s_res_HT , s_res_HTT , s_res_HTTP , s_res_first_http_major , s_res_http_major , s_res_first_http_minor , s_res_http_minor , s_res_first_status_code , s_res_status_code , s_res_status_start , s_res_status , s_res_line_almost_done , s_start_req , s_req_method , s_req_spaces_before_url , s_req_schema , s_req_schema_slash , s_req_schema_slash_slash , s_req_server_start , s_req_server , s_req_server_with_at , s_req_path , s_req_query_string_start , s_req_query_string , s_req_fragment_start , s_req_fragment , s_req_http_start , s_req_http_H , s_req_http_HT , s_req_http_HTT , s_req_http_HTTP , s_req_first_http_major , s_req_http_major , s_req_first_http_minor , s_req_http_minor , s_req_line_almost_done , s_header_field_start , s_header_field , s_header_value_discard_ws , s_header_value_discard_ws_almost_done , s_header_value_discard_lws , s_header_value_start , s_header_value , s_header_value_lws , s_header_almost_done , s_chunk_size_start , s_chunk_size , s_chunk_parameters , s_chunk_size_almost_done , s_headers_almost_done , s_headers_done , s_chunk_data , s_chunk_data_almost_done , s_chunk_data_done , s_body_identity , s_body_identity_eof , s_message_done }
```

相关声明：[state](#adc6e5733fc3c22f0a7b2914188c49c90)、[s_dead](#adc6e5733fc3c22f0a7b2914188c49c90ae928e87617dbca34f86693408ffb8b08)、[s_start_req_or_res](#adc6e5733fc3c22f0a7b2914188c49c90a5a871b16732400896f13a0b4bf4d2d2e)、[s_res_or_resp_H](#adc6e5733fc3c22f0a7b2914188c49c90ad55e2affc1684fca9fc2d2dfa0ef02be)、[s_start_res](#adc6e5733fc3c22f0a7b2914188c49c90a17f7885ac699f68b5179b74e264605d8)、[s_res_H](#adc6e5733fc3c22f0a7b2914188c49c90a1e52abf531e01c40b73cb9e8b3fdd9f4)、[s_res_HT](#adc6e5733fc3c22f0a7b2914188c49c90aef104c331e8e270e735d1aed0430d32e)、[s_res_HTT](#adc6e5733fc3c22f0a7b2914188c49c90aac9df6a576e6b66610d1c78e0a0fce85)、[s_res_HTTP](#adc6e5733fc3c22f0a7b2914188c49c90a49cdf111588eeedd1593e549fdb2b4b7)、[s_res_first_http_major](#adc6e5733fc3c22f0a7b2914188c49c90a758a72c507e51909cd1ab0f84148ac3c)、[s_res_http_major](#adc6e5733fc3c22f0a7b2914188c49c90a4581640a88dc9931031916da00dc9bc6)、[s_res_first_http_minor](#adc6e5733fc3c22f0a7b2914188c49c90a2a4dde0eafd4f5bcb5284744ccafe86a)、[s_res_http_minor](#adc6e5733fc3c22f0a7b2914188c49c90a76ed9bbc2d835b88cb30299abcdd67e8)、[s_res_first_status_code](#adc6e5733fc3c22f0a7b2914188c49c90a246c6aaa49d61e24a43dbb1e4d601b2a)、[s_res_status_code](#adc6e5733fc3c22f0a7b2914188c49c90aefa1bc8b7519ce8b995dc7e71e551f15)、[s_res_status_start](#adc6e5733fc3c22f0a7b2914188c49c90aef8541c5f33f59dfbed9e429ecd92d21)、[s_res_status](#adc6e5733fc3c22f0a7b2914188c49c90a3159d98e8c993680b7640db1e6eed22c)、[s_res_line_almost_done](#adc6e5733fc3c22f0a7b2914188c49c90a94807fb310f4104dd03e2ddb1ab4ae9b)、[s_start_req](#adc6e5733fc3c22f0a7b2914188c49c90a726ed5570859dca67883ae410c1b9f5b)、[s_req_method](#adc6e5733fc3c22f0a7b2914188c49c90a5dd2f6b19fd4e3cb6b428e094ab7e443)、[s_req_spaces_before_url](#adc6e5733fc3c22f0a7b2914188c49c90a48289d7f47c2a74a9b9c498e5c8070c8)、[s_req_schema](#adc6e5733fc3c22f0a7b2914188c49c90a77eeb3ce03bff5e0a71d81e6689715ea)、[s_req_schema_slash](#adc6e5733fc3c22f0a7b2914188c49c90ac76a17504862a273d8cb490d612f9759)、[s_req_schema_slash_slash](#adc6e5733fc3c22f0a7b2914188c49c90a80fae8bf0e824df045b912278ad0316d)、[s_req_server_start](#adc6e5733fc3c22f0a7b2914188c49c90afe0af478bf5e6e82c2d36dc6209fa72c)、[s_req_server](#adc6e5733fc3c22f0a7b2914188c49c90a68c1b3800638f03d6ad0e3cb6da31acf)、[s_req_server_with_at](#adc6e5733fc3c22f0a7b2914188c49c90a0d0a86b054a404f46184e4e7e41e0d26)、[s_req_path](#adc6e5733fc3c22f0a7b2914188c49c90a490988d398dd839f49be96a79f1dcffe)、[s_req_query_string_start](#adc6e5733fc3c22f0a7b2914188c49c90a3c7bfb6f21eb5f914d33e49bd3ca4809)、[s_req_query_string](#adc6e5733fc3c22f0a7b2914188c49c90a36add21fb73304295cc924d6014c11ef)、[s_req_fragment_start](#adc6e5733fc3c22f0a7b2914188c49c90ae2c4dfd6dc9680c009c6e2554af4341d)、[s_req_fragment](#adc6e5733fc3c22f0a7b2914188c49c90ac379ae76d71944b4daf9519e3b22a1a1)、[s_req_http_start](#adc6e5733fc3c22f0a7b2914188c49c90aeadb7f8e79fd094e250279f8afec062f)、[s_req_http_H](#adc6e5733fc3c22f0a7b2914188c49c90a7c3dea78ecb0ee88212988ed0b90a5e7)、[s_req_http_HT](#adc6e5733fc3c22f0a7b2914188c49c90ae4f0cd1ac4cbbc85edd6073bc27b85b7)、[s_req_http_HTT](#adc6e5733fc3c22f0a7b2914188c49c90aee2b77d4458cf570e1a7bab584ba5907)、[s_req_http_HTTP](#adc6e5733fc3c22f0a7b2914188c49c90a641d4adec0c7f121153854eae440c2c3)、[s_req_first_http_major](#adc6e5733fc3c22f0a7b2914188c49c90a8a068d6a93bae075f7ba5694c46d2de6)、[s_req_http_major](#adc6e5733fc3c22f0a7b2914188c49c90aad6b279013498df4ef81557cec965fe6)、[s_req_first_http_minor](#adc6e5733fc3c22f0a7b2914188c49c90af5876995d7ba04281d118e845db8110d)、[s_req_http_minor](#adc6e5733fc3c22f0a7b2914188c49c90a64272a20486c8d0694704832aea24872)、[s_req_line_almost_done](#adc6e5733fc3c22f0a7b2914188c49c90abb02b342bbb8d22a763b55386db8c0fb)、[s_header_field_start](#adc6e5733fc3c22f0a7b2914188c49c90a85e4e4637f2bc962302e1ba3a3f5f769)、[s_header_field](#adc6e5733fc3c22f0a7b2914188c49c90a3353eed9aa8e2fd854b9f82d3ac1bff1)、[s_header_value_discard_ws](#adc6e5733fc3c22f0a7b2914188c49c90ae58f59a3755eed3117db8930dc78c6ec)、[s_header_value_discard_ws_almost_done](#adc6e5733fc3c22f0a7b2914188c49c90a0eeafcb1a1e4409ffd8c034be9af860d)、[s_header_value_discard_lws](#adc6e5733fc3c22f0a7b2914188c49c90a2dc9752e25cc2a00c3c89bbdf9b0f23b)、[s_header_value_start](#adc6e5733fc3c22f0a7b2914188c49c90aa99f675903d976e1912fb54c5a71baa0)、[s_header_value](#adc6e5733fc3c22f0a7b2914188c49c90a4aa98ee464114fd4b6a00b02d5a83a69)、[s_header_value_lws](#adc6e5733fc3c22f0a7b2914188c49c90ab837338881e7c475bbaff41b146fc57d)、[s_header_almost_done](#adc6e5733fc3c22f0a7b2914188c49c90a484786609cb1b307e43c55b5b3078435)、[s_chunk_size_start](#adc6e5733fc3c22f0a7b2914188c49c90af9d6a67a8cad297aa880c91180699409)、[s_chunk_size](#adc6e5733fc3c22f0a7b2914188c49c90a63c8547a6c351def0a6d1d1529c90aad)、[s_chunk_parameters](#adc6e5733fc3c22f0a7b2914188c49c90a6c9131528d4f92c9b42361fcd943744a)、[s_chunk_size_almost_done](#adc6e5733fc3c22f0a7b2914188c49c90a16494186a1ec7a1e140af1b4eaa09d20)、[s_headers_almost_done](#adc6e5733fc3c22f0a7b2914188c49c90abe81888b100852a3ff950be05d2650fe)、[s_headers_done](#adc6e5733fc3c22f0a7b2914188c49c90a209e6e32f0783f5d76fad26c46013390)、[s_chunk_data](#adc6e5733fc3c22f0a7b2914188c49c90a1dfa1c7e958daff320dcca379e1891f2)、[s_chunk_data_almost_done](#adc6e5733fc3c22f0a7b2914188c49c90aff85ea02669f8cf3bae62121928668c0)、[s_chunk_data_done](#adc6e5733fc3c22f0a7b2914188c49c90a159666494992773deef3d091d61efa64)、[s_body_identity](#adc6e5733fc3c22f0a7b2914188c49c90a08e05eb8bc0a42e6e84fa22dd75bdc95)、[s_body_identity_eof](#adc6e5733fc3c22f0a7b2914188c49c90a1ae8a6fc8117d6baa6a0812d077f5b73)、[s_message_done](#adc6e5733fc3c22f0a7b2914188c49c90ae830ce7380ef6c61643a332ab63f6774)。

## 291.2\_详细说明（Detailed Documentation）

<a id="adc6e5733fc3c22f0a7b2914188c49c90"></a>

### `state`

```c
enum state
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `s_dead` |  |
| `s_start_req_or_res` |  |
| `s_res_or_resp_H` |  |
| `s_start_res` |  |
| `s_res_H` |  |
| `s_res_HT` |  |
| `s_res_HTT` |  |
| `s_res_HTTP` |  |
| `s_res_first_http_major` |  |
| `s_res_http_major` |  |
| `s_res_first_http_minor` |  |
| `s_res_http_minor` |  |
| `s_res_first_status_code` |  |
| `s_res_status_code` |  |
| `s_res_status_start` |  |
| `s_res_status` |  |
| `s_res_line_almost_done` |  |
| `s_start_req` |  |
| `s_req_method` |  |
| `s_req_spaces_before_url` |  |
| `s_req_schema` |  |
| `s_req_schema_slash` |  |
| `s_req_schema_slash_slash` |  |
| `s_req_server_start` |  |
| `s_req_server` |  |
| `s_req_server_with_at` |  |
| `s_req_path` |  |
| `s_req_query_string_start` |  |
| `s_req_query_string` |  |
| `s_req_fragment_start` |  |
| `s_req_fragment` |  |
| `s_req_http_start` |  |
| `s_req_http_H` |  |
| `s_req_http_HT` |  |
| `s_req_http_HTT` |  |
| `s_req_http_HTTP` |  |
| `s_req_first_http_major` |  |
| `s_req_http_major` |  |
| `s_req_first_http_minor` |  |
| `s_req_http_minor` |  |
| `s_req_line_almost_done` |  |
| `s_header_field_start` |  |
| `s_header_field` |  |
| `s_header_value_discard_ws` |  |
| `s_header_value_discard_ws_almost_done` |  |
| `s_header_value_discard_lws` |  |
| `s_header_value_start` |  |
| `s_header_value` |  |
| `s_header_value_lws` |  |
| `s_header_almost_done` |  |
| `s_chunk_size_start` |  |
| `s_chunk_size` |  |
| `s_chunk_parameters` |  |
| `s_chunk_size_almost_done` |  |
| `s_headers_almost_done` |  |
| `s_headers_done` |  |
| `s_chunk_data` |  |
| `s_chunk_data_almost_done` |  |
| `s_chunk_data_done` |  |
| `s_body_identity` |  |
| `s_body_identity_eof` |  |
| `s_message_done` |  |


## 291.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_runtime_reference/P047_parser_state.h_源码浏览.md)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90ae928e87617dbca34f86693408ffb8b08"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a5a871b16732400896f13a0b4bf4d2d2e"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90ad55e2affc1684fca9fc2d2dfa0ef02be"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a17f7885ac699f68b5179b74e264605d8"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a1e52abf531e01c40b73cb9e8b3fdd9f4"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90aef104c331e8e270e735d1aed0430d32e"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90aac9df6a576e6b66610d1c78e0a0fce85"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a49cdf111588eeedd1593e549fdb2b4b7"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a758a72c507e51909cd1ab0f84148ac3c"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a4581640a88dc9931031916da00dc9bc6"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a2a4dde0eafd4f5bcb5284744ccafe86a"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a76ed9bbc2d835b88cb30299abcdd67e8"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a246c6aaa49d61e24a43dbb1e4d601b2a"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90aefa1bc8b7519ce8b995dc7e71e551f15"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90aef8541c5f33f59dfbed9e429ecd92d21"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a3159d98e8c993680b7640db1e6eed22c"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a94807fb310f4104dd03e2ddb1ab4ae9b"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a726ed5570859dca67883ae410c1b9f5b"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a5dd2f6b19fd4e3cb6b428e094ab7e443"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a48289d7f47c2a74a9b9c498e5c8070c8"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a77eeb3ce03bff5e0a71d81e6689715ea"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90ac76a17504862a273d8cb490d612f9759"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a80fae8bf0e824df045b912278ad0316d"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90afe0af478bf5e6e82c2d36dc6209fa72c"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a68c1b3800638f03d6ad0e3cb6da31acf"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a0d0a86b054a404f46184e4e7e41e0d26"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a490988d398dd839f49be96a79f1dcffe"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a3c7bfb6f21eb5f914d33e49bd3ca4809"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a36add21fb73304295cc924d6014c11ef"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90ae2c4dfd6dc9680c009c6e2554af4341d"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90ac379ae76d71944b4daf9519e3b22a1a1"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90aeadb7f8e79fd094e250279f8afec062f"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a7c3dea78ecb0ee88212988ed0b90a5e7"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90ae4f0cd1ac4cbbc85edd6073bc27b85b7"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90aee2b77d4458cf570e1a7bab584ba5907"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a641d4adec0c7f121153854eae440c2c3"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a8a068d6a93bae075f7ba5694c46d2de6"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90aad6b279013498df4ef81557cec965fe6"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90af5876995d7ba04281d118e845db8110d"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a64272a20486c8d0694704832aea24872"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90abb02b342bbb8d22a763b55386db8c0fb"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a85e4e4637f2bc962302e1ba3a3f5f769"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a3353eed9aa8e2fd854b9f82d3ac1bff1"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90ae58f59a3755eed3117db8930dc78c6ec"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a0eeafcb1a1e4409ffd8c034be9af860d"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a2dc9752e25cc2a00c3c89bbdf9b0f23b"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90aa99f675903d976e1912fb54c5a71baa0"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a4aa98ee464114fd4b6a00b02d5a83a69"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90ab837338881e7c475bbaff41b146fc57d"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a484786609cb1b307e43c55b5b3078435"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90af9d6a67a8cad297aa880c91180699409"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a63c8547a6c351def0a6d1d1529c90aad"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a6c9131528d4f92c9b42361fcd943744a"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a16494186a1ec7a1e140af1b4eaa09d20"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90abe81888b100852a3ff950be05d2650fe"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a209e6e32f0783f5d76fad26c46013390"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a1dfa1c7e958daff320dcca379e1891f2"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90aff85ea02669f8cf3bae62121928668c0"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a159666494992773deef3d091d61efa64"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a08e05eb8bc0a42e6e84fa22dd75bdc95"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90a1ae8a6fc8117d6baa6a0812d077f5b73"></a>
<a id="adc6e5733fc3c22f0a7b2914188c49c90ae830ce7380ef6c61643a332ab63f6774"></a>

---

[上一章](P290_zephyr__net__http__parser.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P292_zephyr__net__http__parser_url.h_文件参考.md)
