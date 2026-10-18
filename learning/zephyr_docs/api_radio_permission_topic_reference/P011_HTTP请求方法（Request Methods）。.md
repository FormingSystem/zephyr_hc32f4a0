---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-11
title: HTTP请求方法（Request Methods）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_HTTP请求方法（Request Methods）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP请求方法（Request Methods）。

<a id="details"></a>

HTTP 请求方法（Request Methods）。引入版本（Since）：3.3；API 版本（Version）：0.8.0。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.1\_枚举（Enumerations）

<a id="r_gaacd5f203e33ac338ca5cb8f02a3ff3b8"></a>

```c
enum http_method { HTTP_DELETE = 0 , HTTP_GET = 1 , HTTP_HEAD = 2 , HTTP_POST = 3 , HTTP_PUT = 4 , HTTP_CONNECT = 5 , HTTP_OPTIONS = 6 , HTTP_TRACE = 7 , HTTP_COPY = 8 , HTTP_LOCK = 9 , HTTP_MKCOL = 10 , HTTP_MOVE = 11 , HTTP_PROPFIND = 12 , HTTP_PROPPATCH = 13 , HTTP_SEARCH = 14 , HTTP_UNLOCK = 15 , HTTP_BIND = 16 , HTTP_REBIND = 17 , HTTP_UNBIND = 18 , HTTP_ACL = 19 , HTTP_REPORT = 20 , HTTP_MKACTIVITY = 21 , HTTP_CHECKOUT = 22 , HTTP_MERGE = 23 , HTTP_MSEARCH = 24 , HTTP_NOTIFY = 25 , HTTP_SUBSCRIBE = 26 , HTTP_UNSUBSCRIBE = 27 , HTTP_PATCH = 28 , HTTP_PURGE = 29 , HTTP_MKCALENDAR = 30 , HTTP_LINK = 31 , HTTP_UNLINK = 32 }
```

相关声明：[http_method](#gaacd5f203e33ac338ca5cb8f02a3ff3b8)、[HTTP_DELETE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a427575ab776ed70f0aa76667affc3942)、[HTTP_GET](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4ad23c3d2f21f7502ba058ef89518166)、[HTTP_HEAD](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab547cb50f6792b41c3e7d52ee0f8e442)、[HTTP_POST](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa763023b51da2b3618f24cbf994b34bf)、[HTTP_PUT](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2415577115dd0cd5d5a5aa62d52e1512)、[HTTP_CONNECT](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a73feb27a5ac46d923d5c636f797b3e76)、[HTTP_OPTIONS](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86aa5540a666a38528d28bd7591cb251)、[HTTP_TRACE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aeb1f77f6a1e09403704128086deecf6c)、[HTTP_COPY](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8adb9611ac2f3fbaa16b21eddc40791b7c)、[HTTP_LOCK](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa7119ecfb8aece4bbfb7a261331abddf)、[HTTP_MKCOL](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a850ffd3aeeb1d55b124aa6d1f990b3a6)、[HTTP_MOVE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ad284635f2909fb5b9640928cb0e705c7)、[HTTP_PROPFIND](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a3d253975870f94c93f049575afaff83d)、[HTTP_PROPPATCH](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a12eca1105638a830128e9dc989318f92)、[HTTP_SEARCH](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab5d284c93074084b1782b6b4f0c84cac)、[HTTP_UNLOCK](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a81202ae84a8fc30e687bc5059958c477)、[HTTP_BIND](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a327dcf61f2241a23b809ffda50af1e9b)、[HTTP_REBIND](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a9a8d347e6e7127432058b90466f6a2fd)、[HTTP_UNBIND](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a658daa8d3d7dbc917e2473eeb9a8590a)、[HTTP_ACL](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab76b7cdc0a589106ab2be8e068ae9e8c)、[HTTP_REPORT](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a544d35cc7e95e6a0be97122ab744f2bd)、[HTTP_MKACTIVITY](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2bf319204b9298444ae66023a78ba9b4)、[HTTP_CHECKOUT](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8abcc115ec0192f6a56fd7ca8564c9e30e)、[HTTP_MERGE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4851e8dca997a9b41099f2d8f14be069)、[HTTP_MSEARCH](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a20ba2a33b5833d9a16cca5a1ba9de8e3)、[HTTP_NOTIFY](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a39f145838eada9b10c689e4a2b154ccf)、[HTTP_SUBSCRIBE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a59dcf849dc60543ed33bdb9ccd476daf)、[HTTP_UNSUBSCRIBE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a930cc3d0451fc715afb07adb2267198f)、[HTTP_PATCH](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ae1345469c9ff83a10676dd96e7acf0dc)、[HTTP_PURGE](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a36428da6d444779444f9944ee50ff2a5)、[HTTP_MKCALENDAR](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2cc45c2a2e2dcce009d34ac124a0c80f)、[HTTP_LINK](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86af7b9dfab558c6d7e77788b0bf9c29)、[HTTP_UNLINK](#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab7485b3ada0c697c057054e785b443d4)。

HTTP 请求方法（HTTP Request Methods）。

## 11.2\_详细说明（Detailed Documentation）

<a id="gaacd5f203e33ac338ca5cb8f02a3ff3b8"></a>

### `http_method`

```c
enum http_method
```

```c
#include <zephyr/net/http/method.h>
```

HTTP 请求方法（HTTP Request Methods）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HTTP_DELETE` | DELETE（删除）。 |
| `HTTP_GET` | GET（获取）。 |
| `HTTP_HEAD` | HEAD（获取头部）。 |
| `HTTP_POST` | POST（提交）。 |
| `HTTP_PUT` | PUT（写入）。 |
| `HTTP_CONNECT` | CONNECT（建立隧道连接）。 |
| `HTTP_OPTIONS` | OPTIONS（查询选项）。 |
| `HTTP_TRACE` | TRACE（回显跟踪）。 |
| `HTTP_COPY` | COPY（复制）。 |
| `HTTP_LOCK` | LOCK（加锁）。 |
| `HTTP_MKCOL` | MKCOL（创建集合）。 |
| `HTTP_MOVE` | MOVE（移动）。 |
| `HTTP_PROPFIND` | PROPFIND（查找属性）。 |
| `HTTP_PROPPATCH` | PROPPATCH（修改属性）。 |
| `HTTP_SEARCH` | SEARCH（搜索）。 |
| `HTTP_UNLOCK` | UNLOCK（解锁）。 |
| `HTTP_BIND` | BIND（绑定）。 |
| `HTTP_REBIND` | REBIND（重新绑定）。 |
| `HTTP_UNBIND` | UNBIND（解除绑定）。 |
| `HTTP_ACL` | ACL（访问控制列表）。 |
| `HTTP_REPORT` | REPORT（报告）。 |
| `HTTP_MKACTIVITY` | MKACTIVITY（创建活动）。 |
| `HTTP_CHECKOUT` | CHECKOUT（检出）。 |
| `HTTP_MERGE` | MERGE（合并）。 |
| `HTTP_MSEARCH` | MSEARCH（多播搜索）。 |
| `HTTP_NOTIFY` | NOTIFY（通知）。 |
| `HTTP_SUBSCRIBE` | SUBSCRIBE（订阅）。 |
| `HTTP_UNSUBSCRIBE` | UNSUBSCRIBE（取消订阅）。 |
| `HTTP_PATCH` | PATCH（部分修改）。 |
| `HTTP_PURGE` | PURGE（清除）。 |
| `HTTP_MKCALENDAR` | MKCALENDAR（创建日历）。 |
| `HTTP_LINK` | LINK（建立链接）。 |
| `HTTP_UNLINK` | UNLINK（解除链接）。 |


## 11.3\_原页交叉引用（Cross References）

- [zephyr/net/http/method.h](../api_file_supplement_reference/P065_zephyr__net__http__method.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a427575ab776ed70f0aa76667affc3942"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4ad23c3d2f21f7502ba058ef89518166"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab547cb50f6792b41c3e7d52ee0f8e442"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa763023b51da2b3618f24cbf994b34bf"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2415577115dd0cd5d5a5aa62d52e1512"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a73feb27a5ac46d923d5c636f797b3e76"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86aa5540a666a38528d28bd7591cb251"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8aeb1f77f6a1e09403704128086deecf6c"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8adb9611ac2f3fbaa16b21eddc40791b7c"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa7119ecfb8aece4bbfb7a261331abddf"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a850ffd3aeeb1d55b124aa6d1f990b3a6"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8ad284635f2909fb5b9640928cb0e705c7"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a3d253975870f94c93f049575afaff83d"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a12eca1105638a830128e9dc989318f92"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab5d284c93074084b1782b6b4f0c84cac"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a81202ae84a8fc30e687bc5059958c477"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a327dcf61f2241a23b809ffda50af1e9b"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a9a8d347e6e7127432058b90466f6a2fd"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a658daa8d3d7dbc917e2473eeb9a8590a"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab76b7cdc0a589106ab2be8e068ae9e8c"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a544d35cc7e95e6a0be97122ab744f2bd"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2bf319204b9298444ae66023a78ba9b4"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8abcc115ec0192f6a56fd7ca8564c9e30e"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4851e8dca997a9b41099f2d8f14be069"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a20ba2a33b5833d9a16cca5a1ba9de8e3"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a39f145838eada9b10c689e4a2b154ccf"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a59dcf849dc60543ed33bdb9ccd476daf"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a930cc3d0451fc715afb07adb2267198f"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8ae1345469c9ff83a10676dd96e7acf0dc"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a36428da6d444779444f9944ee50ff2a5"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2cc45c2a2e2dcce009d34ac124a0c80f"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86af7b9dfab558c6d7e77788b0bf9c29"></a>
<a id="ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab7485b3ada0c697c057054e785b443d4"></a>

---

[上一章](P010_eSPI SAF API主题.md) · [返回大纲](大纲.md) · [下一章](P012_IIS3DWB API主题.md)
