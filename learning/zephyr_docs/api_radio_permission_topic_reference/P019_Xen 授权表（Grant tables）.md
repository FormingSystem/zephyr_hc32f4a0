---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-19
title: Xen 授权表（Grant tables）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_Xen 授权表（Grant tables）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

与其他域共享内存，并映射其他域的内存授权（Foreign grants）。

<a id="details"></a>

与其他域共享内存，并映射其他域的内存授权（Foreign grants）。

<a id="header-files"></a>
<a id="files"></a>

## 19.1\_文件（Files）

<a id="r_gnttab_2Eh"></a>

```c
file gnttab.h
```

相关声明：[gnttab.h](../api_file_network_device_reference/P013_zephyr__xen__gnttab.h_文件参考.md)。

Xen授权表（Grant Table）的辅助接口。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.2\_函数（Functions）

<a id="r_gaa36d64f2cd70dedabc2c7a67ddb497a9"></a>

```c
grant_ref_t gnttab_grant_access (domid_t domid, unsigned long gfn, bool readonly)
```

相关声明：[gnttab_grant_access](#gaa36d64f2cd70dedabc2c7a67ddb497a9)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

授予另一个域（Domain）访问客户机页帧（Guest Frame）的权限。

<a id="r_ga16013267f3a28da2b672e9d8961b0d9d"></a>

```c
int gnttab_end_access (grant_ref_t gref)
```

相关声明：[gnttab_end_access](#ga16013267f3a28da2b672e9d8961b0d9d)。

释放由 `gnttab_grant_access()` 创建的授权引用（Grant Reference）。

<a id="r_gafedf9bc092852f2fd9f7461b89482634"></a>

```c
int32_t gnttab_alloc_and_grant (void **map, bool readonly)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[gnttab_alloc_and_grant](#gafedf9bc092852f2fd9f7461b89482634)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

分配页面并立即授予其访问权限（Grant Access）。

<a id="r_ga423310c4f8f0ff8f9758e33ab004365e"></a>

```c
void * gnttab_get_pages (unsigned int npages)
```

相关声明：[gnttab_get_pages](#ga423310c4f8f0ff8f9758e33ab004365e)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

分配可承载授权映射（Grant Mappings）的页面。

<a id="r_ga4c9b81e0148848d14d1517fcbba4d8e7"></a>

```c
int gnttab_put_pages (void *start_addr, unsigned int npages)
```

相关声明：[gnttab_put_pages](#ga4c9b81e0148848d14d1517fcbba4d8e7)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

释放由 `gnttab_get_pages()` 分配的页面。

<a id="r_ga64d478848b93048af3e7de5474cc3c0b"></a>

```c
int gnttab_map_refs (struct gnttab_map_grant_ref *map_ops, unsigned int count)
```

相关声明：[gnttab_map_refs](#ga64d478848b93048af3e7de5474cc3c0b)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

映射一个或多个其他域的授权引用（Foreign Grant References）。

<a id="r_gadc5dee1df1b16011a6bb4e6975136092"></a>

```c
int gnttab_unmap_refs (struct gnttab_unmap_grant_ref *unmap_ops, unsigned int count)
```

相关声明：[gnttab_unmap_refs](#gadc5dee1df1b16011a6bb4e6975136092)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

取消一个或多个其他域授权引用（Foreign Grant References）的映射。

<a id="r_ga39c9410cefe90e66b08c297e32e0282c"></a>

```c
int gnttab_query_size (domid_t dom, uint32_t *nr_frames, uint32_t *max_nr_frames, int16_t *status)
```

相关声明：[gnttab_query_size](#ga39c9410cefe90e66b08c297e32e0282c)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

查询某个域（Domain）的当前和最大授权表大小（Grant Table Size）。

<a id="r_gafe3ff541ac6015e39922f34940154724"></a>

```c
const char * gnttabop_error (int16_t status)
```

相关声明：[gnttabop_error](#gafe3ff541ac6015e39922f34940154724)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

将 Xen 授权表状态（Grant-table Status）转换为可读文本。

## 19.3\_详细说明（Detailed Documentation）

<a id="gafedf9bc092852f2fd9f7461b89482634"></a>

### `gnttab_alloc_and_grant()`

```c
int32_t gnttab_alloc_and_grant ( void ** map, bool readonly )
```

```c
#include <zephyr/xen/gnttab.h>
```

分配页面并立即授予其访问权限（Grant Access）。

不再需要时，调用方必须先释放授权（Grant），再对 map 返回的缓冲区调用 k_free()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] map` | 用于接收页基地址（Page Base Address）的缓冲区。 |
| ` readonly` | 设为 true 表示授予只读访问（Read-only Access）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOMEM` | 页面分配（Page Allocation）失败。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_XEN_GRANT_TABLE 时可用。

**返回（Returns）**：返回值（Returns）：成功返回授权引用（Grant Reference），失败返回负 errno。

<a id="ga16013267f3a28da2b672e9d8961b0d9d"></a>

### `gnttab_end_access()`

```c
int gnttab_end_access ( grant_ref_t gref)
```

```c
#include <zephyr/xen/gnttab.h>
```

释放由 `gnttab_grant_access()` 创建的授权引用（Grant Reference）。

这不会释放先前由 gnttab_alloc_and_grant() 分配的内存。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `gref` | 待释放的授权引用（Grant Reference）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_XEN_GRANT_TABLE 时可用。

<a id="ga423310c4f8f0ff8f9758e33ab004365e"></a>

### `gnttab_get_pages()`

```c
void * gnttab_get_pages ( unsigned int npages)
```

```c
#include <zephyr/xen/gnttab.h>
```

分配可承载授权映射（Grant Mappings）的页面。

返回的范围适合用作 struct gnttab_map_grant_ref 条目中的 host_addr；使用后调用 gnttab_put_pages() 释放。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `npages` | 要分配的页数（Number of Pages）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_XEN_GRANT_TABLE 时可用。

**返回（Returns）**：返回值（Returns）：已分配范围的基地址（Base Address），失败返回 NULL。

<a id="gaa36d64f2cd70dedabc2c7a67ddb497a9"></a>

### `gnttab_grant_access()`

```c
grant_ref_t gnttab_grant_access ( domid_t domid, unsigned long gfn, bool readonly )
```

```c
#include <zephyr/xen/gnttab.h>
```

授予另一个域（Domain）访问客户机页帧（Guest Frame）的权限。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `domid` | 获得该页框访问权限的外部域（Foreign Domain）。 |
| `gfn` | 要公开的客户机页框号（Guest Frame Number）。 |
| `readonly` | 设为 true 表示授予只读访问（Read-only Access）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_XEN_GRANT_TABLE 时可用。

**返回（Returns）**：返回值（Returns）：标识新条目的授权引用（Grant Reference）。

<a id="ga64d478848b93048af3e7de5474cc3c0b"></a>

### `gnttab_map_refs()`

```c
int gnttab_map_refs ( struct gnttab_map_grant_ref * map_ops, unsigned int count )
```

```c
#include <zephyr/xen/gnttab.h>
```

映射一个或多个其他域的授权引用（Foreign Grant References）。

map_ops 引用的 host_addr 页面必须按 4K 对齐，且应通过 gnttab_get_pages() 获取。

Xen 还会在每个 map_ops[i].status 字段中存放对应条目的状态码（Status Code）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] map_ops` | 已准备好的映射操作数组（Map Operations）。 |
| ` count` | map_ops 中的条目数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EFAULT` | 已启用 Xen 扩展区域（Extended Regions），且某个主机地址位于这些区域之外。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_XEN_GRANT_TABLE 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga4c9b81e0148848d14d1517fcbba4d8e7"></a>

### `gnttab_put_pages()`

```c
int gnttab_put_pages ( void * start_addr, unsigned int npages )
```

```c
#include <zephyr/xen/gnttab.h>
```

释放由 `gnttab_get_pages()` 分配的页面。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `start_addr` | gnttab_get_pages() 返回的基地址（Base Address）。 |
| `npages` | 要释放的页面数量（Number of Pages）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_XEN_GRANT_TABLE 时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga39c9410cefe90e66b08c297e32e0282c"></a>

### `gnttab_query_size()`

```c
int gnttab_query_size ( domid_t dom, uint32_t * nr_frames, uint32_t * max_nr_frames, int16_t * status )
```

```c
#include <zephyr/xen/gnttab.h>
```

查询某个域（Domain）的当前和最大授权表大小（Grant Table Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dom` | 要查询授权表大小（Grant Table Size）的域；查询调用域自身时使用 DOMID_SELF。 |
| `nr_frames` | 供 Xen 写入当前页框数量（Current Frame Count）的存储位置。 |
| `max_nr_frames` | 供 Xen 写入最大页框数量（Maximum Frame Count）的存储位置。 |
| `status` | 供 Xen 写入 GNTST_* 操作状态（Operation Status）的存储位置。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_XEN_GRANT_TABLE 时可用。

**返回（Returns）**：返回值（Returns）：超级调用（Hypercall）成功返回 0，失败返回负 errno。

<a id="gadc5dee1df1b16011a6bb4e6975136092"></a>

### `gnttab_unmap_refs()`

```c
int gnttab_unmap_refs ( struct gnttab_unmap_grant_ref * unmap_ops, unsigned int count )
```

```c
#include <zephyr/xen/gnttab.h>
```

取消一个或多个其他域授权引用（Foreign Grant References）的映射。

随后对成功解除映射的页面调用 gnttab_put_pages()。

Xen 还会在每个 unmap_ops[i].status 字段中存放对应条目的状态码（Status Code）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] unmap_ops` | 已准备好的解除映射操作数组（Unmap Operations）。 |
| ` count` | unmap_ops 中的条目数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EFAULT` | 已启用 Xen 扩展区域（Extended Regions），且某个主机地址位于这些区域之外。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_XEN_GRANT_TABLE 时可用。

**返回（Returns）**：返回值（Returns）：GNTTABOP_unmap_grant_ref 超级调用（Hypercall）的返回值，成功为 0；失败返回负 errno。

<a id="gafe3ff541ac6015e39922f34940154724"></a>

### `gnttabop_error()`

```c
const char * gnttabop_error ( int16_t status)
```

```c
#include <zephyr/xen/gnttab.h>
```

将 Xen 授权表状态（Grant-table Status）转换为可读文本。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `status` | 负的 GNTST_* 状态码（Status Code）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_XEN_GRANT_TABLE 时可用。

**返回（Returns）**：返回值（Returns）：指向常量错误字符串（Constant Error String）的指针。


## 19.4\_原页交叉引用（Cross References）

- [gnttab.h](../api_file_network_device_reference/P013_zephyr__xen__gnttab.h_文件参考.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [k_free()](../heap_reference/P001_内核堆公共接口.md#ga79b63cc93b3358cf82d74f40e73b69d5)
- [CONFIG_XEN_GRANT_TABLE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN_GRANT_TABLE)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_1-Wire 网络层（Network layer）.md) · [返回大纲](大纲.md) · [下一章](P020_Xen 内存管理（Memory management）.md)
