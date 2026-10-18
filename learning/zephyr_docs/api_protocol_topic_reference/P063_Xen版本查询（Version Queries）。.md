---
id: learning.zephyr-docs.api-protocol-topic-reference.page-63
title: Xen版本查询（Version Queries）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xen__version__queries.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_Xen版本查询（Version Queries）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__version__queries.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查询向当前域公开的 Xen 虚拟机监控器版本。

<a id="details"></a>

查询向当前域公开的 Xen 虚拟机监控器版本。

<a id="header-files"></a>
<a id="files"></a>

## 63.1\_文件（Files）

<a id="r_version_2Eh"></a>

```c
file version.h
```

相关声明：[version.h](../api_file_configuration_reference/P079_zephyr__xen__version.h_文件参考.md)。

Xen版本查询（Version Queries）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 63.2\_函数（Functions）

<a id="r_ga1a790f668be1f721823419393a62201b"></a>

```c
int xen_version (void)
```

相关声明：[xen_version](#ga1a790f668be1f721823419393a62201b)。

获取按主版本号和次版本号（Major and Minor Numbers）编码的 Xen 版本（Version）。

<a id="r_ga9ed44decd02728419b557c1db7d86635"></a>

```c
int xen_version_extraversion (char *extra, int len)
```

相关声明：[xen_version_extraversion](#ga9ed44decd02728419b557c1db7d86635)。

获取 Xen 附加版本字符串（Extra Version String）。

## 63.3\_详细说明（Detailed Documentation）

<a id="ga1a790f668be1f721823419393a62201b"></a>

### `xen_version()`

```c
int xen_version ( void )
```

```c
#include <zephyr/xen/version.h>
```

获取按主版本号和次版本号（Major and Minor Numbers）编码的 Xen 版本（Version）。

返回的整数使用 `XENVER_version` 定义的 Xen 主版本号：次版本号（major:minor）编码。

**返回（Returns）**：返回值：成功时返回编码后的 Xen 版本，失败时返回负 `errno` 值。

<a id="ga9ed44decd02728419b557c1db7d86635"></a>

### `xen_version_extraversion()`

```c
int xen_version_extraversion ( char * extra, int len )
```

```c
#include <zephyr/xen/version.h>
```

获取 Xen 附加版本字符串（Extra Version String）。

执行超级调用（hypercall）之前会清空目标缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] extra` | 用于保存附加版本字符串（extra version string）的目标缓冲区。 |
| ` len` | `extra` 的大小，单位为字节，必须至少为 `XEN_EXTRAVERSION_LEN`。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `extra` 为 `NULL`，或 `len` 过小。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 63.4\_原页交叉引用（Cross References）

- [version.h](../api_file_configuration_reference/P079_zephyr__xen__version.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P062_单总线（1-Wire）.md) · [返回大纲](大纲.md)
