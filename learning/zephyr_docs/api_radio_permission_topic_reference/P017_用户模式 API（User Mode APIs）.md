---
id: learning.zephyr-docs.api-radio-permission-topic-reference.page-17
title: 用户模式 API（User Mode APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_用户模式 API（User Mode APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-groups"></a>
<a id="groups"></a>

## 17.1\_主题（Topics）

<a id="r_user_5Fmutex_5Fapis"></a>

相关声明：[用户模式互斥锁 API](../userspace_sync_reference/P003_用户模式互斥量公共接口.md)。

<a id="r_user_5Fsemaphore_5Fapis"></a>

相关声明：[用户模式信号量 API](../userspace_sync_reference/P007_用户模式信号量公共接口.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.2\_宏定义（Macros）

<a id="r_ga6a2dae4c6dc6959d8785ff1924b1b424"></a>

```c
#define K_THREAD_ACCESS_GRANT(name_, ...)
```

相关声明：[K_THREAD_ACCESS_GRANT](#ga6a2dae4c6dc6959d8785ff1924b1b424)。

授予静态线程（Static Thread）对一组内核对象（Kernel Objects）的访问权限。

<a id="r_ga1418482d67c7964855570fd0ac79628d"></a>

```c
#define K_OBJ_FLAG_INITIALIZED BIT(0)
```

相关声明：[K_OBJ_FLAG_INITIALIZED](#ga1418482d67c7964855570fd0ac79628d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对象已初始化（Initialized）。

<a id="r_ga8892f9343266ec24abf25e29f3f6bc9b"></a>

```c
#define K_OBJ_FLAG_PUBLIC BIT(1)
```

相关声明：[K_OBJ_FLAG_PUBLIC](#ga8892f9343266ec24abf25e29f3f6bc9b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对象为公共对象（Public）。

<a id="r_ga1bf7c8c1d5fe0a7358dd70c4663a5a7a"></a>

```c
#define K_OBJ_FLAG_ALLOC BIT(2)
```

相关声明：[K_OBJ_FLAG_ALLOC](#ga1bf7c8c1d5fe0a7358dd70c4663a5a7a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对象已分配（Allocated）。

<a id="r_ga82d3a7242074db70130415201d3d0fd6"></a>

```c
#define K_OBJ_FLAG_DRIVER BIT(3)
```

相关声明：[K_OBJ_FLAG_DRIVER](#ga82d3a7242074db70130415201d3d0fd6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

驱动对象（Driver Object）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.3\_函数（Functions）

<a id="r_ga94087bedf96fe2a2bea437d3d585ca22"></a>

```c
void k_object_access_grant (const void *object, struct k_thread *thread)
```

相关声明：[k_object_access_grant](#ga94087bedf96fe2a2bea437d3d585ca22)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

授予线程访问内核对象（Kernel Object）的权限。

<a id="r_gab70fe65497da1347cc4b7bf7ca2daf22"></a>

```c
void k_object_access_revoke (const void *object, struct k_thread *thread)
```

相关声明：[k_object_access_revoke](#gab70fe65497da1347cc4b7bf7ca2daf22)、[k_thread](../thread_core_reference/P004_线程对象结构.md)。

撤销线程访问内核对象（Kernel Object）的权限。

<a id="r_gac1dcfff520e5a2c86ecf9e483900a655"></a>

```c
void k_object_access_revoke_others (const void *object)
```

相关声明：[k_object_access_revoke_others](#gac1dcfff520e5a2c86ecf9e483900a655)。

撤销所有其他线程访问某内核对象（Kernel Object）的权限。

<a id="r_ga3cb1a024c0178918def2dd0186e565b3"></a>

```c
void k_object_release (const void *object)
```

相关声明：[k_object_release](#ga3cb1a024c0178918def2dd0186e565b3)。

释放对象（Release an Object）。

<a id="r_gababc731e98a6378323c0d633b2abaa6a"></a>

```c
void k_object_access_all_grant (const void *object)
```

相关声明：[k_object_access_all_grant](#gababc731e98a6378323c0d633b2abaa6a)。

授予所有当前及将来线程对某对象的访问权限（Access）。

<a id="r_gaacd9b4b517db99b3b027dd717e6746b4"></a>

```c
bool k_object_is_valid (const void *obj, enum k_objects otype)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[k_object_is_valid](#gaacd9b4b517db99b3b027dd717e6746b4)、[k_objects](../api_file_display_management_reference/P010_zephyr__sys__kobject.h_文件参考.md#af3a248c0e3b05c84b1dd38642f7cf2a1)。

检查内核对象（Kernel Object）是否为指定类型且有效。

<a id="r_ga2c25103810b5e06fdde8355134bed46c"></a>

```c
int k_object_access_check (const void *object)
```

相关声明：[k_object_access_check](#ga2c25103810b5e06fdde8355134bed46c)。

检查当前线程是否有权访问某对象（Object Access）。

<a id="r_ga5bba3a354fbc63673c76c9815db40812"></a>

```c
void * k_object_alloc (enum k_objects otype)
```

相关声明：[k_object_alloc](#ga5bba3a354fbc63673c76c9815db40812)、[k_objects](../api_file_display_management_reference/P010_zephyr__sys__kobject.h_文件参考.md#af3a248c0e3b05c84b1dd38642f7cf2a1)。

分配指定类型的内核对象（Kernel Object）。

<a id="r_gab99a640325f14a6505a85218dcba5446"></a>

```c
void * k_object_alloc_size (enum k_objects otype, size_t size)
```

相关声明：[k_object_alloc_size](#gab99a640325f14a6505a85218dcba5446)、[k_objects](../api_file_display_management_reference/P010_zephyr__sys__kobject.h_文件参考.md#af3a248c0e3b05c84b1dd38642f7cf2a1)。

分配指定类型及给定大小的内核对象（Kernel Object）。

<a id="r_ga9cc15e8fd7df9cb81c3d7b6c79917aab"></a>

```c
void k_object_free (void *obj)
```

相关声明：[k_object_free](#ga9cc15e8fd7df9cb81c3d7b6c79917aab)。

释放先前使用 `k_object_alloc()` 分配的内核对象（Kernel Object）。

## 17.4\_详细说明（Detailed Documentation）

<a id="ga1bf7c8c1d5fe0a7358dd70c4663a5a7a"></a>

### `K_OBJ_FLAG_ALLOC`

```c
#define K_OBJ_FLAG_ALLOC BIT(2)
```

```c
#include <zephyr/sys/kobject.h>
```

对象已分配（Allocated）。

<a id="ga82d3a7242074db70130415201d3d0fd6"></a>

### `K_OBJ_FLAG_DRIVER`

```c
#define K_OBJ_FLAG_DRIVER BIT(3)
```

```c
#include <zephyr/sys/kobject.h>
```

驱动对象（Driver Object）。

<a id="ga1418482d67c7964855570fd0ac79628d"></a>

### `K_OBJ_FLAG_INITIALIZED`

```c
#define K_OBJ_FLAG_INITIALIZED BIT(0)
```

```c
#include <zephyr/sys/kobject.h>
```

对象已初始化（Initialized）。

<a id="ga8892f9343266ec24abf25e29f3f6bc9b"></a>

### `K_OBJ_FLAG_PUBLIC`

```c
#define K_OBJ_FLAG_PUBLIC BIT(1)
```

```c
#include <zephyr/sys/kobject.h>
```

对象为公共对象（Public）。

<a id="ga6a2dae4c6dc6959d8785ff1924b1b424"></a>

### `K_THREAD_ACCESS_GRANT`

```c
#define K_THREAD_ACCESS_GRANT ( name_, ... )
```

```c
#include <zephyr/sys/kobject.h>
```

展开值（Value）：

```c
static void * const _CONCAT(_object_list_, name_)[] = \
        { __VA_ARGS__, NULL }; \
static const STRUCT_SECTION_ITERABLE(k_object_assignment, \
                                _CONCAT(_object_access_, name_)) = \
                { (&_k_thread_obj_ ## name_), \
                  (_CONCAT(_object_list_, name_)) }
```

授予静态线程（Static Thread）对一组内核对象（Kernel Objects）的访问权限。

对通过 K_THREAD_DEFINE() 声明的线程，授予一组内核对象（Kernel Objects）的访问权限。这些对象无需已初始化；在线程于早期启动序列初始化时授予权限。

除第一个参数外，其余所有参数必须是指向内核对象（Kernel Objects）的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name_` | 传给 K_THREAD_DEFINE() 的线程名称（Thread Name） |

<a id="gababc731e98a6378323c0d633b2abaa6a"></a>

### `k_object_access_all_grant()`

```c
void k_object_access_all_grant ( const void * object)
```

```c
#include <zephyr/sys/kobject.h>
```

授予所有当前及将来线程对某对象的访问权限（Access）。

若调用方处于监督模式（Supervisor Mode），或处于用户模式（User Mode）且对此对象有足够权限，则为系统内所有当前及未来线程授予此对象的访问权限，使其成为公共内核对象（Public Kernel Object）。

运行不可信代码的系统应避免使用此 API，因为这些代码可能推导内核对象地址并执行不期望的操作。

无法撤销单个线程对公共对象（Public Objects）的权限；对象一旦公开，任何线程都可使用。可用 k_object_access_revoke_others() 取消对象的公共访问状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `object` | 内核对象地址（Address of Kernel Object） |

<a id="ga2c25103810b5e06fdde8355134bed46c"></a>

### `k_object_access_check()`

```c
int k_object_access_check ( const void * object)
```

```c
#include <zephyr/sys/kobject.h>
```

检查当前线程是否有权访问某对象（Object Access）。

允许用户线程（User Threads）在尝试操作前检查权限，以便无权限时妥善处理失败。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `object` | 待检查的对象（Object） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 对象有效，且当前线程有访问权限。 |
| `-EBADF` | 对象无效。 |
| `-EPERM` | 对象有效，但当前线程没有访问权限。 |

<a id="ga94087bedf96fe2a2bea437d3d585ca22"></a>

### `k_object_access_grant()`

```c
void k_object_access_grant ( const void * object, struct k_thread * thread )
```

```c
#include <zephyr/sys/kobject.h>
```

授予线程访问内核对象（Kernel Object）的权限。

调用方处于监督模式（Supervisor Mode），或处于用户模式且同时拥有对象和被授权线程的权限时，为目标线程授予对象访问权限。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `object` | 内核对象地址（Address of Kernel Object） |
| `thread` | 要授予对象访问权限的线程 |

<a id="gab70fe65497da1347cc4b7bf7ca2daf22"></a>

### `k_object_access_revoke()`

```c
void k_object_access_revoke ( const void * object, struct k_thread * thread )
```

```c
#include <zephyr/sys/kobject.h>
```

撤销线程访问内核对象（Kernel Object）的权限。

调用方处于监督模式（Supervisor Mode），或处于用户模式且同时拥有对象和被撤权线程的权限时，目标线程将失去对象访问权限。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `object` | 内核对象地址（Address of Kernel Object） |
| `thread` | 要移除对象访问权限的线程 |

<a id="gac1dcfff520e5a2c86ecf9e483900a655"></a>

### `k_object_access_revoke_others()`

```c
void k_object_access_revoke_others ( const void * object)
```

```c
#include <zephyr/sys/kobject.h>
```

撤销所有其他线程访问某内核对象（Kernel Object）的权限。

用户线程可以将自身有权限的对象授权给其他线程，包括自己创建的线程，因此在许多情况下只撤销指定线程的权限并不足够。此 API 撤销当前线程以外所有线程的访问权限，使不再有拥有权限的用户线程。

同时取消对象先前可能通过 k_object_access_all_grant() 获得的公共访问状态（Public Access Status）。

仅内核线程（Kernel Threads）可使用此函数。因此从权限角度看，保留调用线程的访问权限影响很小，但仍保留一个所有者，明确保证此函数绝不会释放动态对象；正常情况下，动态对象失去所有所有者时会被释放。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `object` | 内核对象地址（Address of Kernel Object） |

<a id="ga5bba3a354fbc63673c76c9815db40812"></a>

### `k_object_alloc()`

```c
void * k_object_alloc ( enum k_objects otype)
```

```c
#include <zephyr/sys/kobject.h>
```

分配指定类型的内核对象（Kernel Object）。

运行时实例化指定类型的内核对象（Kernel Object），并返回其指针。对象返回时尚未初始化，调用线程获得其访问权限。对象内存从调用线程的资源池（Resource Pool）分配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otype` | 所请求的内核对象类型（Kernel Object Type） |

**说明（Note）**：注意（Note）：仅选择 CONFIG_DYNAMIC_OBJECTS 时可用。线程栈对象（Thread Stack Object）必须使用 k_object_alloc_size()，因为栈大小可能不同。

**返回（Returns）**：返回值（Returns）：指向已分配内核对象的指针；没有可用内存时返回 NULL。

<a id="gab99a640325f14a6505a85218dcba5446"></a>

### `k_object_alloc_size()`

```c
void * k_object_alloc_size ( enum k_objects otype, size_t size )
```

```c
#include <zephyr/sys/kobject.h>
```

分配指定类型及给定大小的内核对象（Kernel Object）。

运行时实例化指定类型的内核对象（Kernel Object），并返回其指针。对象返回时尚未初始化，调用线程获得其访问权限。对象内存从调用线程的资源池（Resource Pool）分配。

此函数尤其适合大小可变的线程栈对象（Thread Stack Objects）；其他对象通常应考虑 k_object_alloc()。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `otype` | 所请求的内核对象类型（Kernel Object Type） |
| `size` | 所请求的内核对象大小（Kernel Object Size） |

**说明（Note）**：注意（Note）：仅选择 CONFIG_DYNAMIC_OBJECTS 时可用。

**返回（Returns）**：返回值（Returns）：指向已分配内核对象的指针；没有可用内存时返回 NULL。

<a id="ga9cc15e8fd7df9cb81c3d7b6c79917aab"></a>

### `k_object_free()`

```c
void k_object_free ( void * obj)
```

```c
#include <zephyr/sys/kobject.h>
```

释放先前使用 `k_object_alloc()` 分配的内核对象（Kernel Object）。

将内核对象内存归还到分配它的资源池（Resource Pool）。必须确保在调用期间及之后不再使用该对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obj` | 指向内核对象内存地址的指针。 |

**说明（Note）**：注意（Note）：仅选择 CONFIG_DYNAMIC_OBJECTS 时可用。

<a id="gaacd9b4b517db99b3b027dd717e6746b4"></a>

### `k_object_is_valid()`

```c
bool k_object_is_valid ( const void * obj, enum k_objects otype )
```

```c
#include <zephyr/sys/kobject.h>
```

检查内核对象（Kernel Object）是否为指定类型且有效。

检查内核对象是否存在、类型是否符合且是否已经初始化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obj` | 内核对象的地址。 |
| `otype` | 对象类型（Object Type）；使用 K_OBJ_ANY 可忽略类型检查。 |

**返回（Returns）**：返回值（Returns）：内核对象 obj 存在、类型符合且已初始化时返回 True，否则返回 False。

<a id="ga3cb1a024c0178918def2dd0186e565b3"></a>

### `k_object_release()`

```c
void k_object_release ( const void * object)
```

```c
#include <zephyr/sys/kobject.h>
```

释放对象（Release an Object）。

允许用户线程放弃自身对对象的权限；线程终止时，其权限会自动清除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `object` | 待释放访问权限的对象（Object）。 |


## 17.5\_原页交叉引用（Cross References）

- [用户模式互斥锁 API](../userspace_sync_reference/P003_用户模式互斥量公共接口.md)
- [用户模式信号量 API](../userspace_sync_reference/P007_用户模式信号量公共接口.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [k_objects](../api_file_display_management_reference/P010_zephyr__sys__kobject.h_文件参考.md#af3a248c0e3b05c84b1dd38642f7cf2a1)
- [zephyr/sys/kobject.h](../api_file_display_management_reference/P010_zephyr__sys__kobject.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [k_object_assignment](../kernel_runtime_model_reference/P006_k_object_assignment_结构体.md)
- [K_THREAD_DEFINE()](../thread_core_reference/P001_线程公共接口.md#gab3ced58648ca35788a40676e8478ecd2)
- [CONFIG_DYNAMIC_OBJECTS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DYNAMIC_OBJECTS)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructk__object__assignment_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_半主机 API（Semihosting APIs）.md) · [返回大纲](大纲.md) · [下一章](P018_1-Wire 网络层（Network layer）.md)
