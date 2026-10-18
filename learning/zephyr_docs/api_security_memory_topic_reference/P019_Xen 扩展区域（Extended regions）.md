---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-19
title: Xen 扩展区域（Extended regions）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_Xen 扩展区域（Extended regions）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

从 Xen 扩展内存区域分配、释放和映射缓冲区。

<a id="details"></a>

从 Xen 扩展内存区域分配、释放和映射缓冲区。

<a id="header-files"></a>
<a id="files"></a>

## 19.1\_文件（Files）

<a id="r_regions_2Eh"></a>

```c
file regions.h
```

相关声明：[regions.h](../api_file_interface_reference/P047_zephyr__xen__regions.h_文件参考.md)。

Xen扩展区域管理（Extended Region Management）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.2\_函数（Functions）

<a id="r_gabe293a88ca167b9a52709c7e94af73b3"></a>

```c
bool xen_region_is_addr_extreg (void *ptr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[xen_region_is_addr_extreg](#gabe293a88ca167b9a52709c7e94af73b3)。

检查地址是否属于已配置的扩展区域（extended region）。

<a id="r_ga4853ade09ca37b66ad484ad1cbab6cf3"></a>

```c
void * xen_region_get_pages (size_t nr_pages)
```

相关声明：[xen_region_get_pages](#ga4853ade09ca37b66ad484ad1cbab6cf3)。

从扩展区域分配一个或多个连续内存页（contiguous pages）。

<a id="r_gaa82b399b305dc279da8fb8206da77d3b"></a>

```c
int xen_region_put_pages (void *ptr, size_t nr_pages)
```

相关声明：[xen_region_put_pages](#gaa82b399b305dc279da8fb8206da77d3b)。

释放先前从扩展区域分配的内存页。

<a id="r_ga65b8fda79f7b6e4db26cccc818c69c79"></a>

```c
int xen_region_map (void *ptr, size_t nr_pages)
```

相关声明：[xen_region_map](#ga65b8fda79f7b6e4db26cccc818c69c79)。

将扩展区域的缓冲区映射到内核地址空间（kernel address space）。

<a id="r_gaf576c75a5b01b1a8b6f2be3b48a25886"></a>

```c
int xen_region_unmap (void *ptr, size_t nr_pages)
```

相关声明：[xen_region_unmap](#gaf576c75a5b01b1a8b6f2be3b48a25886)。

从内核地址空间解除扩展区域缓冲区的映射。

## 19.3\_详细说明（Detailed Documentation）

<a id="ga4853ade09ca37b66ad484ad1cbab6cf3"></a>

### `xen_region_get_pages()`

```c
void * xen_region_get_pages ( size_t nr_pages)
```

```c
#include <zephyr/xen/regions.h>
```

从扩展区域分配一个或多个连续内存页（contiguous pages）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nr_pages` | 要分配的 Xen 页面数量（Number of Xen Pages）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_REGIONS` Kconfig 选项时可用。

**返回（Returns）**：**返回值（Returns）：**已分配范围的基地址（Base Address）；若没有区域能满足请求，则为 `NULL`。

<a id="gabe293a88ca167b9a52709c7e94af73b3"></a>

### `xen_region_is_addr_extreg()`

```c
bool xen_region_is_addr_extreg ( void * ptr)
```

```c
#include <zephyr/xen/regions.h>
```

检查地址是否属于已配置的扩展区域（extended region）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ptr` | 要测试的地址（Address）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | `ptr` 位于某个已配置的扩展区域（Extended Region）内。 |
| `false` | `ptr` 为 `NULL`，或位于所有已配置扩展区域之外。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_REGIONS` Kconfig 选项时可用。

<a id="ga65b8fda79f7b6e4db26cccc818c69c79"></a>

### `xen_region_map()`

```c
int xen_region_map ( void * ptr, size_t nr_pages )
```

```c
#include <zephyr/xen/regions.h>
```

将扩展区域的缓冲区映射到内核地址空间（kernel address space）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ptr` | 扩展区域缓冲区（Extended-region Buffer）的基地址。 |
| `nr_pages` | 要映射的页面数量（Number of Pages）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EFAULT` | `ptr` 不属于扩展区域（Extended Region）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_REGIONS` Kconfig 选项时可用。

<a id="gaa82b399b305dc279da8fb8206da77d3b"></a>

### `xen_region_put_pages()`

```c
int xen_region_put_pages ( void * ptr, size_t nr_pages )
```

```c
#include <zephyr/xen/regions.h>
```

释放先前从扩展区域分配的内存页。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ptr` | `xen_region_get_pages()` 返回的基地址（Base Address）。 |
| `nr_pages` | 要释放的页面数量（Number of Pages）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EIO` | `ptr` 不属于已知的扩展区域（Extended Region）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_REGIONS` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaf576c75a5b01b1a8b6f2be3b48a25886"></a>

### `xen_region_unmap()`

```c
int xen_region_unmap ( void * ptr, size_t nr_pages )
```

```c
#include <zephyr/xen/regions.h>
```

从内核地址空间解除扩展区域缓冲区的映射。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ptr` | 扩展区域缓冲区（Extended-region Buffer）的基地址。 |
| `nr_pages` | 要取消映射的页面数量（Number of Pages）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EFAULT` | `ptr` 不属于扩展区域（Extended Region）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_REGIONS` Kconfig 选项时可用。


## 19.4\_原页交叉引用（Cross References）

- [regions.h](../api_file_interface_reference/P047_zephyr__xen__regions.h_文件参考.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [CONFIG_XEN_REGIONS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN_REGIONS)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_Wi-Fi 网络管理器 API（Network Manager API）.md) · [返回大纲](大纲.md)
