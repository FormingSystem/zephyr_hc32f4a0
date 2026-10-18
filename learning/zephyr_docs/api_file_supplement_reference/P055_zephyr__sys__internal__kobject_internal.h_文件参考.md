---
id: learning.zephyr-docs.api-file-supplement-reference.page-55
title: zephyr__sys__internal__kobject_internal.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kobject__internal_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_zephyr\_\_sys\_\_internal\_\_kobject\_internal.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/kobject__internal_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 55.1\_数据结构（Data Structures）

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

## 55.2\_函数（Functions）

<a id="r_ga50528134a693d656cd60c001f50645ba"></a>

```c
void k_object_init (const void *obj)
```

相关声明：[k_object_init](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__internal__apis.html#ga50528134a693d656cd60c001f50645ba)。

查找内核对象（Kernel Object）；若对象存在，则初始化其元数据（Metadata）。

<a id="r_gafc261408a120975732788b1bd9223036"></a>

```c
static struct k_object * k_object_create_dynamic_aligned (size_t align, size_t size)
```

相关声明：[k_object](../kernel_runtime_model_reference/P005_k_object_结构体.md)、[k_object_create_dynamic_aligned](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__internal__apis.html#gafc261408a120975732788b1bd9223036)。

<a id="r_ga3879ef0db97f968d82938da87698e359"></a>

```c
static struct k_object * k_object_create_dynamic (size_t size)
```

相关声明：[k_object](../kernel_runtime_model_reference/P005_k_object_结构体.md)、[k_object_create_dynamic](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__internal__apis.html#ga3879ef0db97f968d82938da87698e359)。


## 55.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/kobject__internal_8h_source.html)
- [k_object_data](../kernel_runtime_model_reference/P020_k_object_data_联合体.md)
- [k_object](../kernel_runtime_model_reference/P005_k_object_结构体.md)
- [k_object_find()](../syscall_boot_reference/P001_系统调用接口.md#ga0d5a4ed3856e0e57c7953f2082ee6fca)
- [k_object_assignment](../kernel_runtime_model_reference/P006_k_object_assignment_结构体.md)
- [k_object_init](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__internal__apis.html#ga50528134a693d656cd60c001f50645ba)
- [k_object_create_dynamic_aligned](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__internal__apis.html#gafc261408a120975732788b1bd9223036)
- [k_object_create_dynamic](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__internal__apis.html#ga3879ef0db97f968d82938da87698e359)

---

[上一章](P054_zephyr__dt-bindings__interrupt-controller__ite-it51xxx-wuc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P056_zephyr__bluetooth__mesh__large_comp_data_srv.h_文件参考.md)
