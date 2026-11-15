---
id: learning.zephyr-docs.api-file-display-management-reference.page-10
title: zephyr__sys__kobject.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kobject_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_sys\_\_kobject.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/kobject_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <stddef.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/internal/kobject_internal.h>
#include <zephyr/syscalls/kobject.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="r_ga6a2dae4c6dc6959d8785ff1924b1b424"></a>

```c
#define K_THREAD_ACCESS_GRANT(name_, ...)
```

相关声明：[K_THREAD_ACCESS_GRANT](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga6a2dae4c6dc6959d8785ff1924b1b424)。

授予静态线程（Static Thread）对一组内核对象（Kernel Objects）的访问权限。

<a id="r_ga1418482d67c7964855570fd0ac79628d"></a>

```c
#define K_OBJ_FLAG_INITIALIZED BIT(0)
```

相关声明：[K_OBJ_FLAG_INITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga1418482d67c7964855570fd0ac79628d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对象已初始化（Initialized）。

<a id="r_ga8892f9343266ec24abf25e29f3f6bc9b"></a>

```c
#define K_OBJ_FLAG_PUBLIC BIT(1)
```

相关声明：[K_OBJ_FLAG_PUBLIC](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga8892f9343266ec24abf25e29f3f6bc9b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对象为公共对象（Public）。

<a id="r_ga1bf7c8c1d5fe0a7358dd70c4663a5a7a"></a>

```c
#define K_OBJ_FLAG_ALLOC BIT(2)
```

相关声明：[K_OBJ_FLAG_ALLOC](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga1bf7c8c1d5fe0a7358dd70c4663a5a7a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对象已分配（Allocated）。

<a id="r_ga82d3a7242074db70130415201d3d0fd6"></a>

```c
#define K_OBJ_FLAG_DRIVER BIT(3)
```

相关声明：[K_OBJ_FLAG_DRIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga82d3a7242074db70130415201d3d0fd6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

驱动对象（Driver Object）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.2\_枚举（Enumerations）

<a id="r_af3a248c0e3b05c84b1dd38642f7cf2a1"></a>

```c
enum k_objects { K_OBJ_ANY , K_OBJ_DRIVER_ANY , K_OBJ_LAST }
```

相关声明：[k_objects](#af3a248c0e3b05c84b1dd38642f7cf2a1)、[K_OBJ_ANY](#af3a248c0e3b05c84b1dd38642f7cf2a1a51b9ec845f71832ad8fbb35d0cb3e5f6)、[K_OBJ_DRIVER_ANY](#af3a248c0e3b05c84b1dd38642f7cf2a1ab03fc9b624b9a942815d5fb334436fd6)、[K_OBJ_LAST](#af3a248c0e3b05c84b1dd38642f7cf2a1a7aecd777175f519ce8240e337e1cf430)。

内核对象类型（Kernel Object Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.3\_函数（Functions）

<a id="r_ga94087bedf96fe2a2bea437d3d585ca22"></a>

```c
void k_object_access_grant (const void *object, struct k_thread *thread)
```

相关声明：[k_object_access_grant](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga94087bedf96fe2a2bea437d3d585ca22)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

授予线程访问内核对象（Kernel Object）的权限。

<a id="r_gab70fe65497da1347cc4b7bf7ca2daf22"></a>

```c
void k_object_access_revoke (const void *object, struct k_thread *thread)
```

相关声明：[k_object_access_revoke](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gab70fe65497da1347cc4b7bf7ca2daf22)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

撤销线程访问内核对象（Kernel Object）的权限。

<a id="r_gac1dcfff520e5a2c86ecf9e483900a655"></a>

```c
void k_object_access_revoke_others (const void *object)
```

相关声明：[k_object_access_revoke_others](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gac1dcfff520e5a2c86ecf9e483900a655)。

撤销所有其他线程访问某内核对象（Kernel Object）的权限。

<a id="r_ga3cb1a024c0178918def2dd0186e565b3"></a>

```c
void k_object_release (const void *object)
```

相关声明：[k_object_release](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga3cb1a024c0178918def2dd0186e565b3)。

释放对象（Release an Object）。

<a id="r_gababc731e98a6378323c0d633b2abaa6a"></a>

```c
void k_object_access_all_grant (const void *object)
```

相关声明：[k_object_access_all_grant](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gababc731e98a6378323c0d633b2abaa6a)。

授予所有当前及将来线程对某对象的访问权限（Access）。

<a id="r_gaacd9b4b517db99b3b027dd717e6746b4"></a>

```c
bool k_object_is_valid (const void *obj, enum k_objects otype)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_object_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gaacd9b4b517db99b3b027dd717e6746b4)、[k_objects](#af3a248c0e3b05c84b1dd38642f7cf2a1)。

检查内核对象（Kernel Object）是否为指定类型且有效。

<a id="r_ga2c25103810b5e06fdde8355134bed46c"></a>

```c
int k_object_access_check (const void *object)
```

相关声明：[k_object_access_check](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga2c25103810b5e06fdde8355134bed46c)。

检查当前线程是否有权访问某对象（Object Access）。

<a id="r_ga5bba3a354fbc63673c76c9815db40812"></a>

```c
void * k_object_alloc (enum k_objects otype)
```

相关声明：[k_object_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga5bba3a354fbc63673c76c9815db40812)、[k_objects](#af3a248c0e3b05c84b1dd38642f7cf2a1)。

分配指定类型的内核对象（Kernel Object）。

<a id="r_gab99a640325f14a6505a85218dcba5446"></a>

```c
void * k_object_alloc_size (enum k_objects otype, size_t size)
```

相关声明：[k_object_alloc_size](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gab99a640325f14a6505a85218dcba5446)、[k_objects](#af3a248c0e3b05c84b1dd38642f7cf2a1)。

分配指定类型及给定大小的内核对象（Kernel Object）。

<a id="r_ga9cc15e8fd7df9cb81c3d7b6c79917aab"></a>

```c
void k_object_free (void *obj)
```

相关声明：[k_object_free](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga9cc15e8fd7df9cb81c3d7b6c79917aab)。

释放先前使用 `k_object_alloc()` 分配的内核对象（Kernel Object）。

## 10.4\_详细说明（Detailed Documentation）

<a id="af3a248c0e3b05c84b1dd38642f7cf2a1"></a>

### `k_objects`

```c
enum k_objects
```

内核对象类型（Kernel Object Types）。

此枚举必须与 `scripts/build/gen_kobject_list.py` 中的内核对象和子系统列表，以及 `kernel/userspace/userspace.c` 中的 `otype_to_str()` 函数保持同步。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `K_OBJ_ANY` | 用于匹配任意对象类型（Object Type）。 |
| `K_OBJ_DRIVER_ANY` | 用于匹配任意驱动对象类型（Driver Object Type）。 |
| `K_OBJ_LAST` |  |


## 10.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/internal/kobject_internal.h](../api_source_transport_clock_reference/P018_kobject_internal.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P036_kobject.h_源码浏览.md)
- [K_THREAD_ACCESS_GRANT](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga6a2dae4c6dc6959d8785ff1924b1b424)
- [K_OBJ_FLAG_INITIALIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga1418482d67c7964855570fd0ac79628d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [K_OBJ_FLAG_PUBLIC](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga8892f9343266ec24abf25e29f3f6bc9b)
- [K_OBJ_FLAG_ALLOC](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga1bf7c8c1d5fe0a7358dd70c4663a5a7a)
- [K_OBJ_FLAG_DRIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga82d3a7242074db70130415201d3d0fd6)
- [k_object_access_grant](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga94087bedf96fe2a2bea437d3d585ca22)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_object_access_revoke](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gab70fe65497da1347cc4b7bf7ca2daf22)
- [k_object_access_revoke_others](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gac1dcfff520e5a2c86ecf9e483900a655)
- [k_object_release](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga3cb1a024c0178918def2dd0186e565b3)
- [k_object_access_all_grant](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gababc731e98a6378323c0d633b2abaa6a)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [k_object_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gaacd9b4b517db99b3b027dd717e6746b4)
- [k_object_access_check](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga2c25103810b5e06fdde8355134bed46c)
- [k_object_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga5bba3a354fbc63673c76c9815db40812)
- [k_object_alloc_size](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gab99a640325f14a6505a85218dcba5446)
- [k_object_free](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga9cc15e8fd7df9cb81c3d7b6c79917aab)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="af3a248c0e3b05c84b1dd38642f7cf2a1a51b9ec845f71832ad8fbb35d0cb3e5f6"></a>
<a id="af3a248c0e3b05c84b1dd38642f7cf2a1ab03fc9b624b9a942815d5fb334436fd6"></a>
<a id="af3a248c0e3b05c84b1dd38642f7cf2a1a7aecd777175f519ce8240e337e1cf430"></a>

---

[上一章](P009_zephyr__drivers__misc__ft8xx__ft8xx_dl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__mgmt__mcumgr__smp__smp.h_文件参考.md)
