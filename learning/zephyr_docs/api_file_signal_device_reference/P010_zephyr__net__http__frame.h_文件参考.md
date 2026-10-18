---
id: learning.zephyr-docs.api-file-signal-device-reference.page-10
title: zephyr__net__http__frame.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_net\_\_http\_\_frame.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/frame_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP/2帧信息（Frame Information）。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

HTTP/2帧信息（Frame Information）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_http2_5Fsettings_5Ffield"></a>

```c
struct http2_settings_field
```

相关声明：[http2_settings_field](../network_service_model_reference/P024_http2_settings_field_结构体.md)。

HTTP/2设置字段（Settings Field）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.2\_枚举（Enumerations）

<a id="r_a3017b7bf771b2502f76e1d8bb672bb2f"></a>

```c
enum http2_frame_type { HTTP2_DATA_FRAME = 0x00 , HTTP2_HEADERS_FRAME = 0x01 , HTTP2_PRIORITY_FRAME = 0x02 , HTTP2_RST_STREAM_FRAME = 0x03 , HTTP2_SETTINGS_FRAME = 0x04 , HTTP2_PUSH_PROMISE_FRAME = 0x05 , HTTP2_PING_FRAME = 0x06 , HTTP2_GOAWAY_FRAME = 0x07 , HTTP2_WINDOW_UPDATE_FRAME = 0x08 , HTTP2_CONTINUATION_FRAME = 0x09 }
```

相关声明：[http2_frame_type](#a3017b7bf771b2502f76e1d8bb672bb2f)、[HTTP2_DATA_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fa02d444bc7da5f9342c8490051494a561)、[HTTP2_HEADERS_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fabb919f746f9cb550e3d3ed3fbd0aa0fb)、[HTTP2_PRIORITY_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fab09f251d80dd5475808473a190349d15)、[HTTP2_RST_STREAM_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2faea35662abfea3d425ca626be3a042e49)、[HTTP2_SETTINGS_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fa87d56ac6afcb9d85c8774b190b4f9123)、[HTTP2_PUSH_PROMISE_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fad82d652aee8fd35ce6e2ca0eec717442)、[HTTP2_PING_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fa12949c06e095e808f65bd4fb3cfa69ff)、[HTTP2_GOAWAY_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fa9439fea062e3e2d61d8bfadd66e421c8)、[HTTP2_WINDOW_UPDATE_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fa619d7150ec1e5eff0f7b98a0a228b6b4)、[HTTP2_CONTINUATION_FRAME](#a3017b7bf771b2502f76e1d8bb672bb2fa2baf23cf1cb79f34306edb76f768e822)。

HTTP/2 帧类型（Frame Types）。

<a id="r_ac0e63ce922141d8043318ed40da4b559"></a>

```c
enum http2_settings { HTTP2_SETTINGS_HEADER_TABLE_SIZE = 1 , HTTP2_SETTINGS_ENABLE_PUSH = 2 , HTTP2_SETTINGS_MAX_CONCURRENT_STREAMS = 3 , HTTP2_SETTINGS_INITIAL_WINDOW_SIZE = 4 , HTTP2_SETTINGS_MAX_FRAME_SIZE = 5 , HTTP2_SETTINGS_MAX_HEADER_LIST_SIZE = 6 }
```

相关声明：[http2_settings](#ac0e63ce922141d8043318ed40da4b559)、[HTTP2_SETTINGS_HEADER_TABLE_SIZE](#ac0e63ce922141d8043318ed40da4b559a0dcdd60d4c429d558c4cebc9c1527e06)、[HTTP2_SETTINGS_ENABLE_PUSH](#ac0e63ce922141d8043318ed40da4b559ad1c9118f459a93bce47b0ad1546b50b4)、[HTTP2_SETTINGS_MAX_CONCURRENT_STREAMS](#ac0e63ce922141d8043318ed40da4b559a844c0af59b8b254301d47b0888886304)、[HTTP2_SETTINGS_INITIAL_WINDOW_SIZE](#ac0e63ce922141d8043318ed40da4b559a1152ff63cb965c24f05419e92112d6f0)、[HTTP2_SETTINGS_MAX_FRAME_SIZE](#ac0e63ce922141d8043318ed40da4b559af09a348b42a97e9d8ae57bff5e252a9e)、[HTTP2_SETTINGS_MAX_HEADER_LIST_SIZE](#ac0e63ce922141d8043318ed40da4b559a763095cc59fc3a905a4612e9a2843705)。

HTTP/2 设置（Settings）。

## 10.3\_详细说明（Detailed Documentation）

<a id="a3017b7bf771b2502f76e1d8bb672bb2f"></a>

### `http2_frame_type`

```c
enum http2_frame_type
```

HTTP/2 帧类型（Frame Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HTTP2_DATA_FRAME` | 数据帧（Data Frame）。 |
| `HTTP2_HEADERS_FRAME` | 头部帧（HEADERS Frame）。 |
| `HTTP2_PRIORITY_FRAME` | 优先级帧（PRIORITY Frame）。 |
| `HTTP2_RST_STREAM_FRAME` | 流复位帧（RST_STREAM Frame）。 |
| `HTTP2_SETTINGS_FRAME` | 设置帧（SETTINGS Frame）。 |
| `HTTP2_PUSH_PROMISE_FRAME` | 推送承诺帧（PUSH_PROMISE Frame）。 |
| `HTTP2_PING_FRAME` | Ping 帧（PING Frame）。 |
| `HTTP2_GOAWAY_FRAME` | 关闭通知帧（GOAWAY Frame）。 |
| `HTTP2_WINDOW_UPDATE_FRAME` | 窗口更新帧（WINDOW_UPDATE Frame）。 |
| `HTTP2_CONTINUATION_FRAME` | 延续帧（CONTINUATION Frame）。 |

<a id="ac0e63ce922141d8043318ed40da4b559"></a>

### `http2_settings`

```c
enum http2_settings
```

HTTP/2 设置（Settings）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HTTP2_SETTINGS_HEADER_TABLE_SIZE` | 头部表大小（Header Table Size）。 |
| `HTTP2_SETTINGS_ENABLE_PUSH` | 启用推送（Enable Push）。 |
| `HTTP2_SETTINGS_MAX_CONCURRENT_STREAMS` | 最大并发流数量（Maximum Concurrent Streams）。 |
| `HTTP2_SETTINGS_INITIAL_WINDOW_SIZE` | 初始窗口大小（Initial Window Size）。 |
| `HTTP2_SETTINGS_MAX_FRAME_SIZE` | 最大帧大小（Max Frame Size）。 |
| `HTTP2_SETTINGS_MAX_HEADER_LIST_SIZE` | 最大头部列表大小（Max Header List Size）。 |


## 10.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P270_frame.h_源码浏览.md)
- [http2_settings_field](../network_service_model_reference/P024_http2_settings_field_结构体.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a3017b7bf771b2502f76e1d8bb672bb2fa02d444bc7da5f9342c8490051494a561"></a>
<a id="a3017b7bf771b2502f76e1d8bb672bb2fabb919f746f9cb550e3d3ed3fbd0aa0fb"></a>
<a id="a3017b7bf771b2502f76e1d8bb672bb2fab09f251d80dd5475808473a190349d15"></a>
<a id="a3017b7bf771b2502f76e1d8bb672bb2faea35662abfea3d425ca626be3a042e49"></a>
<a id="a3017b7bf771b2502f76e1d8bb672bb2fa87d56ac6afcb9d85c8774b190b4f9123"></a>
<a id="a3017b7bf771b2502f76e1d8bb672bb2fad82d652aee8fd35ce6e2ca0eec717442"></a>
<a id="a3017b7bf771b2502f76e1d8bb672bb2fa12949c06e095e808f65bd4fb3cfa69ff"></a>
<a id="a3017b7bf771b2502f76e1d8bb672bb2fa9439fea062e3e2d61d8bfadd66e421c8"></a>
<a id="a3017b7bf771b2502f76e1d8bb672bb2fa619d7150ec1e5eff0f7b98a0a228b6b4"></a>
<a id="a3017b7bf771b2502f76e1d8bb672bb2fa2baf23cf1cb79f34306edb76f768e822"></a>
<a id="ac0e63ce922141d8043318ed40da4b559a0dcdd60d4c429d558c4cebc9c1527e06"></a>
<a id="ac0e63ce922141d8043318ed40da4b559ad1c9118f459a93bce47b0ad1546b50b4"></a>
<a id="ac0e63ce922141d8043318ed40da4b559a844c0af59b8b254301d47b0888886304"></a>
<a id="ac0e63ce922141d8043318ed40da4b559a1152ff63cb965c24f05419e92112d6f0"></a>
<a id="ac0e63ce922141d8043318ed40da4b559af09a348b42a97e9d8ae57bff5e252a9e"></a>
<a id="ac0e63ce922141d8043318ed40da4b559a763095cc59fc3a905a4612e9a2843705"></a>

---

[上一章](P009_zephyr__drivers__regulator__fake.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt_hash_checksum.h_文件参考.md)
