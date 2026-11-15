---
id: learning.zephyr-docs.api-file-runtime-reference.page-51
title: zephyr__sys__printk-hooks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/printk-hooks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_zephyr\_\_sys\_\_printk-hooks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/printk-hooks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可重定向printk()字符输出的钩子（Hooks）的头文件。

查看此文件的源码。

<a id="details"></a>

可重定向printk()字符输出的钩子（Hooks）的头文件。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 51.1\_类型定义（Typedefs）

<a id="r_a17d0c01ee515cc6f962dbd56a4c9b36f"></a>

```c
typedef int(* printk_hook_fn_t) (int c)
```

相关声明：[printk_hook_fn_t](#a17d0c01ee515cc6f962dbd56a4c9b36f)。

`printk` 函数处理器（Function Handler）。

## 51.2\_详细说明（Detailed Documentation）

<a id="a17d0c01ee515cc6f962dbd56a4c9b36f"></a>

### `printk_hook_fn_t`

```c
typedef int(* printk_hook_fn_t) (int c)
```

`printk` 函数处理器（Function Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `c` | 要输出的字符（Character）。 |

返回（Returns）：作为输入传入的字符（Character）。


## 51.3\_原页交叉引用（Cross References）

- [printk()](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a1bce54a738ce2d9dd6d95ee842ec237c)
- [查看此文件的源码。](../api_source_reference/P671_printk-hooks.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P050_zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt_client.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P052_zephyr__net__ptp_time.h_文件参考.md)
