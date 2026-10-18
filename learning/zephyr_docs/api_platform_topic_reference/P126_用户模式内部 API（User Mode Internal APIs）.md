---
id: learning.zephyr-docs.api-platform-topic-reference.page-126
title: 用户模式内部 API（User Mode Internal APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__internal__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第126章\_用户模式内部 API（User Mode Internal APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__internal__apis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 126.1\_数据结构（Data Structures）

<a id="r_k_5Fobject_5Fdata"></a>

```c
union k_object_data
```

相关声明：[k_object_data](../kernel_runtime_model_reference/P020_k_object_data_联合体.md)。

<a id="r_k_5Fobject"></a>

```c
struct k_object
```

相关声明：[k_object](../kernel_runtime_model_reference/P005_k_object_结构体.md)。

gperf生成的表；通过k_object_find()检索这些对象。

<a id="r_k_5Fobject_5Fassignment"></a>

```c
struct k_object_assignment
```

相关声明：[k_object_assignment](../kernel_runtime_model_reference/P006_k_object_assignment_结构体.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 126.2\_函数（Functions）

<a id="r_ga50528134a693d656cd60c001f50645ba"></a>

```c
void k_object_init (const void *obj)
```

相关声明：[k_object_init](#ga50528134a693d656cd60c001f50645ba)。

查找内核对象（Kernel Object）；若对象存在，则初始化其元数据（Metadata）。

<a id="r_gafc261408a120975732788b1bd9223036"></a>

```c
static struct k_object * k_object_create_dynamic_aligned (size_t align, size_t size)
```

相关声明：[k_object](../kernel_runtime_model_reference/P005_k_object_结构体.md)、[k_object_create_dynamic_aligned](#gafc261408a120975732788b1bd9223036)。

<a id="r_ga3879ef0db97f968d82938da87698e359"></a>

```c
static struct k_object * k_object_create_dynamic (size_t size)
```

相关声明：[k_object](../kernel_runtime_model_reference/P005_k_object_结构体.md)、[k_object_create_dynamic](#ga3879ef0db97f968d82938da87698e359)。

## 126.3\_详细说明（Detailed Documentation）

<a id="ga3879ef0db97f968d82938da87698e359"></a>

### `k_object_create_dynamic()`

```c
struct k_object * k_object_create_dynamic ( size_t size)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/internal/kobject_internal.h>
```

<a id="gafc261408a120975732788b1bd9223036"></a>

### `k_object_create_dynamic_aligned()`

```c
struct k_object * k_object_create_dynamic_aligned ( size_t align, size_t size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/internal/kobject_internal.h>
```

<a id="ga50528134a693d656cd60c001f50645ba"></a>

### `k_object_init()`

```c
void k_object_init ( const void * obj)
```

```c
#include <zephyr/sys/internal/kobject_internal.h>
```

查找内核对象（Kernel Object）；若对象存在，则初始化其元数据（Metadata）。

对对象（Object）调用本函数后，该对象即可从用户空间（Userspace）使用。它应作为内核对象初始化函数（Kernel Object Init Functions）的最后一条语句调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obj` | 内核对象的地址。 |

说明（Note）：这是内部 API。除非正在扩展 Zephyr 源码树中的功能，否则不要使用。


## 126.4\_原页交叉引用（Cross References）

- [k_object_data](../kernel_runtime_model_reference/P020_k_object_data_联合体.md)
- [k_object](../kernel_runtime_model_reference/P005_k_object_结构体.md)
- [k_object_find()](../syscall_boot_reference/P001_系统调用接口.md#ga0d5a4ed3856e0e57c7953f2082ee6fca)
- [k_object_assignment](../kernel_runtime_model_reference/P006_k_object_assignment_结构体.md)
- [zephyr/sys/internal/kobject_internal.h](../api_file_supplement_reference/P055_zephyr__sys__internal__kobject_internal.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P125_USB-C VBUS 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P127_实用工具（Utilities）.md)
