---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-29
title: Xen Dom0 系统控制（sysctl）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_Xen Dom0 系统控制（sysctl）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

发起仅供 Dom0 使用的 Xen sysctl 操作。

<a id="details"></a>

发起仅供 Dom0 使用的 Xen sysctl 操作。

<a id="header-files"></a>
<a id="files"></a>

## 29.1\_文件（Files）

<a id="r_sysctl_2Eh"></a>

```c
file sysctl.h
```

相关声明：[sysctl.h](../api_file_service_reference/P056_zephyr__xen__dom0__sysctl.h_文件参考.md)。

Xen Dom0的系统控制操作（System Control Operations）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 29.2\_函数（Functions）

<a id="r_ga4241e03d02285724a6b47a9c5338ad8f"></a>

```c
int xen_sysctl_physinfo (struct xen_sysctl_physinfo *info)
```

相关声明：[xen_sysctl_physinfo](#ga4241e03d02285724a6b47a9c5338ad8f)。

从 Xen 查询物理主机信息（Physical Host Information）。

<a id="r_gaaf1c2e7bdef408008b3cee7fd380e2eb"></a>

```c
int xen_sysctl_tbuf_op (struct xen_sysctl_tbuf_op *tbuf_op)
```

相关声明：[xen_sysctl_tbuf_op](#gaaf1c2e7bdef408008b3cee7fd380e2eb)。

执行 Xen 跟踪缓冲区系统控制操作（Trace Buffer `sysctl` Operation）。

<a id="r_gabae81727f21c359faa8325d094606fcc"></a>

```c
int xen_sysctl_getdomaininfo (struct xen_domctl_getdomaininfo *domaininfo, uint16_t first, uint16_t num)
```

相关声明：[xen_sysctl_getdomaininfo](#gabae81727f21c359faa8325d094606fcc)、[xen_domctl_getdomaininfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga4848541359c3e13358dc39b42b3c142f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取 Xen 域信息（Domain Information）。

<a id="r_gabf15e75ba751c107f3ba9e86b67820c7"></a>

```c
int xen_sysctl_cpu_hotplug (uint32_t cpu, bool enable)
```

相关声明：[xen_sysctl_cpu_hotplug](#gabf15e75ba751c107f3ba9e86b67820c7)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用物理 CPU（Physical CPUs）。

## 29.3\_详细说明（Detailed Documentation）

<a id="gabf15e75ba751c107f3ba9e86b67820c7"></a>

### `xen_sysctl_cpu_hotplug()`

```c
int xen_sysctl_cpu_hotplug ( uint32_t cpu, bool enable )
```

```c
#include <zephyr/xen/dom0/sysctl.h>
```

启用／禁用物理 CPU（Physical CPUs）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cpu` | 正在开启或关闭的 CPU 标识。 |
| `enable` | 指示应开启还是关闭 CPU 的标志（Flag）。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gabae81727f21c359faa8325d094606fcc"></a>

### `xen_sysctl_getdomaininfo()`

```c
int xen_sysctl_getdomaininfo ( struct xen_domctl_getdomaininfo * domaininfo, uint16_t first, uint16_t num )
```

```c
#include <zephyr/xen/dom0/sysctl.h>
```

获取 Xen 域信息（Domain Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] domaininfo` | 指向 `xen_domctl_getdomaininfo` 结构体的指针，用于保存取得的域信息（Domain Information）。 |
| ` first` | 要获取信息的第一个域标识（Domain ID）。 |
| ` num` | 要获取信息的最大域数量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `domaininfo` 为 `NULL`，或 `num` 为 0。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

**返回（Returns）**：**返回值（Returns）：**成功返回写入 `domaininfo` 的条目数，失败返回负的 `errno` 值。

<a id="ga4241e03d02285724a6b47a9c5338ad8f"></a>

### `xen_sysctl_physinfo()`

```c
int xen_sysctl_physinfo ( struct xen_sysctl_physinfo * info)
```

```c
#include <zephyr/xen/dom0/sysctl.h>
```

从 Xen 查询物理主机信息（Physical Host Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] info` | 接收 Xen 物理宿主机信息（Physical Host Information）的缓冲区。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `info` 为 `NULL`。 |

**注意（Attention）**：**注意（Attention）：**仅在启用 `CONFIG_XEN_DOM0` Kconfig 选项时可用。

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaaf1c2e7bdef408008b3cee7fd380e2eb"></a>

### `xen_sysctl_tbuf_op()`

```c
int xen_sysctl_tbuf_op ( struct xen_sysctl_tbuf_op * tbuf_op)
```

```c
#include <zephyr/xen/dom0/sysctl.h>
```

执行 Xen 跟踪缓冲区系统控制操作（Trace Buffer `sysctl` Operation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] tbuf_op` | 指向 `struct xen_sysctl_tbuf_op` 对象的指针，该对象定义跟踪缓冲区操作（Trace Buffer Operation），并接收 Xen 返回的各项输出值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-errno` | 失败。 |


## 29.4\_原页交叉引用（Cross References）

- [sysctl.h](../api_file_service_reference/P056_zephyr__xen__dom0__sysctl.h_文件参考.md)
- [xen_domctl_getdomaininfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga4848541359c3e13358dc39b42b3c142f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [CONFIG_XEN_DOM0](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN_DOM0)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P028_Wireguard 虚拟专用网络（VPN）服务.md) · [返回大纲](大纲.md)
