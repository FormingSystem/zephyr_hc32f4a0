---
id: learning.zephyr-docs.api-file-service-reference.page-56
title: zephyr__xen__dom0__sysctl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sysctl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第56章\_zephyr\_\_xen\_\_dom0\_\_sysctl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sysctl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen Dom0的系统控制操作（System Control Operations）。

<a id="details"></a>

```c
#include <xen/public/xen.h>
#include <xen/public/sysctl.h>
#include <zephyr/xen/generic.h>
```

查看此文件的源码。

Xen Dom0的系统控制操作（System Control Operations）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 56.1\_函数（Functions）

<a id="r_ga4241e03d02285724a6b47a9c5338ad8f"></a>

```c
int xen_sysctl_physinfo (struct xen_sysctl_physinfo *info)
```

相关声明：[xen_sysctl_physinfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html#ga4241e03d02285724a6b47a9c5338ad8f)。

从 Xen 查询物理主机信息（Physical Host Information）。

<a id="r_gaaf1c2e7bdef408008b3cee7fd380e2eb"></a>

```c
int xen_sysctl_tbuf_op (struct xen_sysctl_tbuf_op *tbuf_op)
```

相关声明：[xen_sysctl_tbuf_op](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html#gaaf1c2e7bdef408008b3cee7fd380e2eb)。

执行 Xen 跟踪缓冲区系统控制操作（Trace Buffer `sysctl` Operation）。

<a id="r_gabae81727f21c359faa8325d094606fcc"></a>

```c
int xen_sysctl_getdomaininfo (struct xen_domctl_getdomaininfo *domaininfo, uint16_t first, uint16_t num)
```

相关声明：[xen_sysctl_getdomaininfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html#gabae81727f21c359faa8325d094606fcc)、[xen_domctl_getdomaininfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga4848541359c3e13358dc39b42b3c142f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取 Xen 域信息（Domain Information）。

<a id="r_gabf15e75ba751c107f3ba9e86b67820c7"></a>

```c
int xen_sysctl_cpu_hotplug (uint32_t cpu, bool enable)
```

相关声明：[xen_sysctl_cpu_hotplug](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html#gabf15e75ba751c107f3ba9e86b67820c7)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用／禁用物理 CPU（Physical CPUs）。


## 56.2\_原页交叉引用（Cross References）

- [zephyr/xen/generic.h](../api_source_supplement_reference/P078_generic.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P852_sysctl.h_源码浏览.md)
- [xen_sysctl_physinfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html#ga4241e03d02285724a6b47a9c5338ad8f)
- [xen_sysctl_tbuf_op](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html#gaaf1c2e7bdef408008b3cee7fd380e2eb)
- [xen_sysctl_getdomaininfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html#gabae81727f21c359faa8325d094606fcc)
- [xen_domctl_getdomaininfo](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__domain__control.html#ga4848541359c3e13358dc39b42b3c142f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [xen_sysctl_cpu_hotplug](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__dom0__sysctl.html#gabf15e75ba751c107f3ba9e86b67820c7)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>

---

[上一章](P055_zephyr__dt-bindings__power__stm32n6_iocell.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P057_zephyr__drivers__clock_control__tisci_clock_control.h_文件参考.md)
