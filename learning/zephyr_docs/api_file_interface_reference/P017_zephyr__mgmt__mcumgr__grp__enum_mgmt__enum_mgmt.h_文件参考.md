---
id: learning.zephyr-docs.api-file-interface-reference.page-17
title: zephyr__mgmt__mcumgr__grp__enum_mgmt__enum_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/enum__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_enum\_mgmt\_\_enum\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/enum__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr枚举管理组（Enumeration Management Group）API的头文件。

查看此文件的源码。

<a id="details"></a>

MCUmgr枚举管理组（Enumeration Management Group）API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 枚举管理组命令标识符（Command IDs for enumeration management group）

<a id="r_gab16f2823b9bb4140a2fc336af5d16d2b"></a>

```c
#define ENUM_MGMT_ID_COUNT 0
```

相关声明：[ENUM_MGMT_ID_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#gab16f2823b9bb4140a2fc336af5d16d2b)。

所支持组（groups）的数量。

<a id="r_ga9b6c5a3021a30f8f6a83694ff9a07bf4"></a>

```c
#define ENUM_MGMT_ID_LIST 1
```

相关声明：[ENUM_MGMT_ID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ga9b6c5a3021a30f8f6a83694ff9a07bf4)。

列出所支持的组。

<a id="r_ga5b08e51b1e32c27da5597fab4f68f94e"></a>

```c
#define ENUM_MGMT_ID_SINGLE 2
```

相关声明：[ENUM_MGMT_ID_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ga5b08e51b1e32c27da5597fab4f68f94e)。

获取单个组标识符（group ID）。

<a id="r_ga03edf25ed33ccdf00b0a21ee574e1b4d"></a>

```c
#define ENUM_MGMT_ID_DETAILS 3
```

相关声明：[ENUM_MGMT_ID_DETAILS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ga03edf25ed33ccdf00b0a21ee574e1b4d)。

所支持组的详细信息。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.2\_枚举（Enumerations）

<a id="r_gaceaae2d8284b4a64b1303513e6aa3099"></a>

```c
enum enum_mgmt_err_code_t { ENUM_MGMT_ERR_OK = 0 , ENUM_MGMT_ERR_UNKNOWN , ENUM_MGMT_ERR_TOO_MANY_GROUP_ENTRIES , ENUM_MGMT_ERR_INSUFFICIENT_HEAP_FOR_ENTRIES , ENUM_MGMT_ERR_INDEX_TOO_LARGE }
```

相关声明：[enum_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#gaceaae2d8284b4a64b1303513e6aa3099)、[ENUM_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ggaceaae2d8284b4a64b1303513e6aa3099aab31067e337c3220232e8eb3b3d885c0)、[ENUM_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ggaceaae2d8284b4a64b1303513e6aa3099a7f535a752e4c789024e4fecb5cdd7c7f)、[ENUM_MGMT_ERR_TOO_MANY_GROUP_ENTRIES](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ggaceaae2d8284b4a64b1303513e6aa3099a7866b895eac198fe6eb021ef385a185e)、[ENUM_MGMT_ERR_INSUFFICIENT_HEAP_FOR_ENTRIES](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ggaceaae2d8284b4a64b1303513e6aa3099ac056ab2ae764f50715d9ee478bc0c153)、[ENUM_MGMT_ERR_INDEX_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ggaceaae2d8284b4a64b1303513e6aa3099af2dff8560e72db54fea41a6345aa5f72)。

枚举管理组（enumeration management group）的命令结果码。


## 17.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P230_enum_mgmt.h_源码浏览.md)
- [ENUM_MGMT_ID_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#gab16f2823b9bb4140a2fc336af5d16d2b)
- [ENUM_MGMT_ID_LIST](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ga9b6c5a3021a30f8f6a83694ff9a07bf4)
- [ENUM_MGMT_ID_SINGLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ga5b08e51b1e32c27da5597fab4f68f94e)
- [ENUM_MGMT_ID_DETAILS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ga03edf25ed33ccdf00b0a21ee574e1b4d)
- [enum_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#gaceaae2d8284b4a64b1303513e6aa3099)
- [ENUM_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ggaceaae2d8284b4a64b1303513e6aa3099aab31067e337c3220232e8eb3b3d885c0)
- [ENUM_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ggaceaae2d8284b4a64b1303513e6aa3099a7f535a752e4c789024e4fecb5cdd7c7f)
- [ENUM_MGMT_ERR_TOO_MANY_GROUP_ENTRIES](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ggaceaae2d8284b4a64b1303513e6aa3099a7866b895eac198fe6eb021ef385a185e)
- [ENUM_MGMT_ERR_INSUFFICIENT_HEAP_FOR_ENTRIES](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ggaceaae2d8284b4a64b1303513e6aa3099ac056ab2ae764f50715d9ee478bc0c153)
- [ENUM_MGMT_ERR_INDEX_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html#ggaceaae2d8284b4a64b1303513e6aa3099af2dff8560e72db54fea41a6345aa5f72)

<a id="header-details"></a>

---

[上一章](P016_zephyr__drivers__emul_sensor.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__drivers__clock_control__esp32_clock_control.h_文件参考.md)
