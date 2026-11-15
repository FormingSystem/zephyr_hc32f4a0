---
id: learning.zephyr-docs.api-connection-topic-reference.page-24
title: Xen 安全模块 FLASK（Xen XSM FLASK）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xen__xsm__flask.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_Xen 安全模块 FLASK（Xen XSM FLASK）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__xsm__flask.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

加载 Xen 安全策略，管理 FLASK 强制执行模式，将上下文转换为安全标识符（SID），管理对象上下文（ocontexts），以及执行其他 FLASK 相关任务。

<a id="details"></a>

加载 Xen 安全策略，管理 FLASK 强制执行模式，将上下文转换为安全标识符（SID），管理对象上下文（ocontexts），以及执行其他 FLASK 相关任务。

<a id="header-files"></a>
<a id="files"></a>

## 24.1\_文件（Files）

<a id="r_flask_2Eh"></a>

```c
file flask.h
```

相关声明：[flask.h](../api_file_configuration_reference/P028_zephyr__xen__flask.h_文件参考.md)。

Xen XSM FLASK的操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.2\_函数（Functions）

<a id="r_gafedcdbff09ea3a91952aa011954bcae3"></a>

```c
int flask_context_to_sid (char *buf, uint32_t size, uint32_t *sid)
```

相关声明：[flask_context_to_sid](#gafedcdbff09ea3a91952aa011954bcae3)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将上下文字符串（Context String）转换为数值形式的安全标识（SID）。

<a id="r_gaf7c884e01c7a9bb55c248c53d9b848eb"></a>

```c
int flask_getenforce (void)
```

相关声明：[flask_getenforce](#gaf7c884e01c7a9bb55c248c53d9b848eb)。

获取当前 FLASK 强制模式（Enforcing Mode）。

## 24.3\_详细说明（Detailed Documentation）

<a id="gafedcdbff09ea3a91952aa011954bcae3"></a>

### `flask_context_to_sid()`

```c
int flask_context_to_sid ( char * buf, uint32_t size, uint32_t * sid )
```

```c
#include <zephyr/xen/flask.h>
```

将上下文字符串（Context String）转换为数值形式的安全标识（SID）。

此函数发出 `FLASK_CONTEXT_TO_SID` 超级调用（hypercall），获取已加载策略中与给定安全上下文（security context）对应的安全标识符（Security ID，SID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 上下文字符串（context string）。 |
| `size` | 上下文字符串的长度。 |
| `sid` | 用于接收对应 SID 的输出指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败时返回负 `errno` 错误码。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_FLASK` 时可用。

<a id="gaf7c884e01c7a9bb55c248c53d9b848eb"></a>

### `flask_getenforce()`

```c
int flask_getenforce ( void )
```

```c
#include <zephyr/xen/flask.h>
```

获取当前 FLASK 强制模式（Enforcing Mode）。

此函数发出 `FLASK_GETENFORCE` 超级调用（hypercall），获取当前强制执行模式（enforcing mode）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 宽容模式（Permissive Mode）。 |
| `1` | 强制模式（Enforcing Mode）。 |
| `-errno` | 失败时返回负 `errno` 错误码。 |

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_XEN_FLASK` 时可用。


## 24.4\_原页交叉引用（Cross References）

- [flask.h](../api_file_configuration_reference/P028_zephyr__xen__flask.h_文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [CONFIG_XEN_FLASK](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN_FLASK)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P023_WUC 驱动后端 API.md) · [返回大纲](大纲.md)
