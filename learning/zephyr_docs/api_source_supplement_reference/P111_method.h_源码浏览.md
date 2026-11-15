---
id: learning.zephyr-docs.api-source-supplement-reference.page-111
title: method.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/method_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第111章\_method.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/method_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/method_8h.html)。

## 111.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
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
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="agroup__http__methods_html_gaacd5f203e33ac338ca5cb8f02a3ff3b8"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a12eca1105638a830128e9dc989318f92"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a20ba2a33b5833d9a16cca5a1ba9de8e3"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2415577115dd0cd5d5a5aa62d52e1512"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2bf319204b9298444ae66023a78ba9b4"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2cc45c2a2e2dcce009d34ac124a0c80f"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a327dcf61f2241a23b809ffda50af1e9b"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a36428da6d444779444f9944ee50ff2a5"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a39f145838eada9b10c689e4a2b154ccf"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a3d253975870f94c93f049575afaff83d"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a427575ab776ed70f0aa76667affc3942"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4851e8dca997a9b41099f2d8f14be069"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4ad23c3d2f21f7502ba058ef89518166"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a544d35cc7e95e6a0be97122ab744f2bd"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a59dcf849dc60543ed33bdb9ccd476daf"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a658daa8d3d7dbc917e2473eeb9a8590a"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a73feb27a5ac46d923d5c636f797b3e76"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a81202ae84a8fc30e687bc5059958c477"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a850ffd3aeeb1d55b124aa6d1f990b3a6"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86aa5540a666a38528d28bd7591cb251"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86af7b9dfab558c6d7e77788b0bf9c29"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a930cc3d0451fc715afb07adb2267198f"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8a9a8d347e6e7127432058b90466f6a2fd"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa7119ecfb8aece4bbfb7a261331abddf"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa763023b51da2b3618f24cbf994b34bf"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab547cb50f6792b41c3e7d52ee0f8e442"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab5d284c93074084b1782b6b4f0c84cac"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab7485b3ada0c697c057054e785b443d4"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab76b7cdc0a589106ab2be8e068ae9e8c"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8abcc115ec0192f6a56fd7ca8564c9e30e"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8ad284635f2909fb5b9640928cb0e705c7"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8adb9611ac2f3fbaa16b21eddc40791b7c"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8ae1345469c9ff83a10676dd96e7acf0dc"></a>
<a id="agroup__http__methods_html_ggaacd5f203e33ac338ca5cb8f02a3ff3b8aeb1f77f6a1e09403704128086deecf6c"></a>

```c


/*
 * Copyright (c) 2022 Meta
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_HTTP_METHOD_H_
#define ZEPHYR_INCLUDE_NET_HTTP_METHOD_H_


#ifdef __cplusplus
extern "C" {
#endif

enum http_method {
        HTTP_DELETE = 0,
        HTTP_GET = 1,
        HTTP_HEAD = 2,
        HTTP_POST = 3,
        HTTP_PUT = 4,
        HTTP_CONNECT = 5,
        HTTP_OPTIONS = 6,
        HTTP_TRACE = 7,
        HTTP_COPY = 8,
        HTTP_LOCK = 9,
        HTTP_MKCOL = 10,
        HTTP_MOVE = 11,
        HTTP_PROPFIND = 12,
        HTTP_PROPPATCH = 13,
        HTTP_SEARCH = 14,
        HTTP_UNLOCK = 15,
        HTTP_BIND = 16,
        HTTP_REBIND = 17,
        HTTP_UNBIND = 18,
        HTTP_ACL = 19,
        HTTP_REPORT = 20,
        HTTP_MKACTIVITY = 21,
        HTTP_CHECKOUT = 22,
        HTTP_MERGE = 23,
        HTTP_MSEARCH = 24,
        HTTP_NOTIFY = 25,
        HTTP_SUBSCRIBE = 26,
        HTTP_UNSUBSCRIBE = 27,
        HTTP_PATCH = 28,
        HTTP_PURGE = 29,
        HTTP_MKCALENDAR = 30,
        HTTP_LINK = 31,
        HTTP_UNLINK = 32,

        HTTP_METHOD_END_VALUE /* keep this the last value */
};

#ifdef __cplusplus
}
#endif


#endif
```

## 111.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2022 Meta。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 64 行

将此项保持为最后一个值。

## 111.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/method_8h.html)
- [http_method](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#gaacd5f203e33ac338ca5cb8f02a3ff3b8)
- [HTTP_DELETE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a427575ab776ed70f0aa76667affc3942)
- [HTTP_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4ad23c3d2f21f7502ba058ef89518166)
- [HTTP_HEAD](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab547cb50f6792b41c3e7d52ee0f8e442)
- [HTTP_POST](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa763023b51da2b3618f24cbf994b34bf)
- [HTTP_PUT](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2415577115dd0cd5d5a5aa62d52e1512)
- [HTTP_CONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a73feb27a5ac46d923d5c636f797b3e76)
- [HTTP_OPTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86aa5540a666a38528d28bd7591cb251)
- [HTTP_TRACE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aeb1f77f6a1e09403704128086deecf6c)
- [HTTP_COPY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8adb9611ac2f3fbaa16b21eddc40791b7c)
- [HTTP_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8aa7119ecfb8aece4bbfb7a261331abddf)
- [HTTP_MKCOL](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a850ffd3aeeb1d55b124aa6d1f990b3a6)
- [HTTP_MOVE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ad284635f2909fb5b9640928cb0e705c7)
- [HTTP_PROPFIND](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a3d253975870f94c93f049575afaff83d)
- [HTTP_PROPPATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a12eca1105638a830128e9dc989318f92)
- [HTTP_SEARCH](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab5d284c93074084b1782b6b4f0c84cac)
- [HTTP_UNLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a81202ae84a8fc30e687bc5059958c477)
- [HTTP_BIND](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a327dcf61f2241a23b809ffda50af1e9b)
- [HTTP_REBIND](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a9a8d347e6e7127432058b90466f6a2fd)
- [HTTP_UNBIND](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a658daa8d3d7dbc917e2473eeb9a8590a)
- [HTTP_ACL](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab76b7cdc0a589106ab2be8e068ae9e8c)
- [HTTP_REPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a544d35cc7e95e6a0be97122ab744f2bd)
- [HTTP_MKACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2bf319204b9298444ae66023a78ba9b4)
- [HTTP_CHECKOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8abcc115ec0192f6a56fd7ca8564c9e30e)
- [HTTP_MERGE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a4851e8dca997a9b41099f2d8f14be069)
- [HTTP_MSEARCH](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a20ba2a33b5833d9a16cca5a1ba9de8e3)
- [HTTP_NOTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a39f145838eada9b10c689e4a2b154ccf)
- [HTTP_SUBSCRIBE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a59dcf849dc60543ed33bdb9ccd476daf)
- [HTTP_UNSUBSCRIBE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a930cc3d0451fc715afb07adb2267198f)
- [HTTP_PATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ae1345469c9ff83a10676dd96e7acf0dc)
- [HTTP_PURGE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a36428da6d444779444f9944ee50ff2a5)
- [HTTP_MKCALENDAR](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a2cc45c2a2e2dcce009d34ac124a0c80f)
- [HTTP_LINK](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8a86af7b9dfab558c6d7e77788b0bf9c29)
- [HTTP_UNLINK](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#ggaacd5f203e33ac338ca5cb8f02a3ff3b8ab7485b3ada0c697c057054e785b443d4)

---

[上一章](P110_mem_manage.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P112_metric.h_源码浏览.md)
