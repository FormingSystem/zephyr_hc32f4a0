---
id: learning.zephyr-docs.api-source-transport-clock-reference.page-18
title: kobject_internal.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kobject__internal_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_kobject\_internal.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/kobject__internal_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_supplement_reference/P055_zephyr__sys__internal__kobject_internal.h_文件参考.md)。

## 18.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00066"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="foldopen00152"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="agroup__usermode__internal__apis_html_ga3879ef0db97f968d82938da87698e359"></a>
<a id="agroup__usermode__internal__apis_html_ga50528134a693d656cd60c001f50645ba"></a>
<a id="agroup__usermode__internal__apis_html_gafc261408a120975732788b1bd9223036"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__mutex_html"></a>
<a id="astructk__object__assignment_html"></a>
<a id="astructk__object__assignment_html_aca82e8f65cfdcfb7497a4b9f3df4eb8d"></a>
<a id="astructk__object__assignment_html_ad034fa126915ad604f1edc3b0a177d5a"></a>
<a id="astructk__object_html"></a>
<a id="astructk__object_html_a351cbe565fef17ea75966085be3142c9"></a>
<a id="astructk__object_html_a9c8686d9552cb48c24aef939c8a80057"></a>
<a id="astructk__object_html_a9e32404b2259979e52b65983ad77ec58"></a>
<a id="astructk__object_html_ad676d4edce580d351104fe09f174c323"></a>
<a id="astructk__object_html_aea0ad6871d88e2756ba0cbd482fa3aa7"></a>
<a id="astructk__thread_html"></a>
<a id="aunionk__object__data_html"></a>
<a id="aunionk__object__data_html_a2f95fd75c72a619e8c5224e64d1aacc0"></a>
<a id="aunionk__object__data_html_ab285ad5a6119657341be525276837fda"></a>
<a id="aunionk__object__data_html_ac8fdffd51c0b32ea262fa98a827a5bd4"></a>
<a id="aunionk__object__data_html_ada581c427efa9e48b441b1a323bd57e6"></a>

```c
/*
 * Copyright (c) 2020 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_SYS_INTERNAL_KOBJECT_INTERNAL_H
#define ZEPHYR_INCLUDE_SYS_INTERNAL_KOBJECT_INTERNAL_H

#ifdef __cplusplus
extern "C" {
#endif


#if defined(CONFIG_USERSPACE) || defined(__DOXYGEN__)
#if defined(CONFIG_GEN_PRIV_STACKS) || defined(__DOXYGEN__)
/* Metadata struct for K_OBJ_THREAD_STACK_ELEMENT */
struct z_stack_data {
        /* Size of the entire stack object, including reserved areas */
        size_t size;

        /* Stack buffer for privilege mode elevations */
        uint8_t *priv;
};
#endif /* CONFIG_GEN_PRIV_STACKS */

/* Object extra data. Only some objects use this, determined by object type */
union k_object_data {
        /* Backing mutex for K_OBJ_SYS_MUTEX */
        struct k_mutex *mutex;

        /* Numerical thread ID for K_OBJ_THREAD */
        unsigned int thread_id;

#if defined(CONFIG_GEN_PRIV_STACKS) || defined(__DOXYGEN__)
        /* Metadata for K_OBJ_THREAD_STACK_ELEMENT */
        const struct z_stack_data *stack_data;
#else
        /* Stack buffer size for K_OBJ_THREAD_STACK_ELEMENT */
        size_t stack_size;
#endif /* CONFIG_GEN_PRIV_STACKS */

        /* All other objects */
        int unused;
};

struct k_object {
        void *name;
        uint8_t perms[CONFIG_MAX_THREAD_BYTES];
        uint8_t type;
        uint8_t flags;
        union k_object_data data;
} __packed __aligned(4);

struct k_object_assignment {
        struct k_thread *thread;
        void * const *objects;
};


void k_object_init(const void *obj);


#else
/* LCOV_EXCL_START */
static inline void k_object_init(const void *obj)
{
        ARG_UNUSED(obj);
}
/* LCOV_EXCL_STOP */
#endif /* !CONFIG_USERSPACE */

#ifdef CONFIG_DYNAMIC_OBJECTS
struct k_object *k_object_create_dynamic_aligned(size_t align, size_t size);

static inline struct k_object *k_object_create_dynamic(size_t size)
{
        return k_object_create_dynamic_aligned(0, size);
}

#else

/* LCOV_EXCL_START */
static inline struct k_object *k_object_create_dynamic_aligned(size_t align,
                                                               size_t size)
{
        ARG_UNUSED(align);
        ARG_UNUSED(size);

        return NULL;
}

static inline struct k_object *k_object_create_dynamic(size_t size)
{
        ARG_UNUSED(size);

        return NULL;
}

/* LCOV_EXCL_STOP */
#endif /* CONFIG_DYNAMIC_OBJECTS */


#ifdef __cplusplus
}
#endif

#endif
```

## 18.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 21 行

`K_OBJ_THREAD_STACK_ELEMENT` 的元数据结构体（metadata struct）。

### 注释 3：原第 23 行

整个栈对象（stack object）的大小，包括保留区域。

### 注释 4：原第 26 行

用于提升到特权模式（privilege mode elevations）的栈缓冲区。

### 注释 5：原第 29 行

条件编译配置（Configuration）标记：`CONFIG_GEN_PRIV_STACKS`。

### 注释 6：原第 31 行

对象附加数据（object extra data）。只有部分对象使用，由对象类型决定。

### 注释 7：原第 33 行

支撑 `K_OBJ_SYS_MUTEX` 的互斥锁（backing mutex）。

### 注释 8：原第 36 行

`K_OBJ_THREAD` 的数值线程标识符（numerical thread ID）。

### 注释 9：原第 40 行

`K_OBJ_THREAD_STACK_ELEMENT` 的元数据（metadata）。

### 注释 10：原第 43 行

`K_OBJ_THREAD_STACK_ELEMENT` 的栈缓冲区大小。

### 注释 11：原第 45 行

条件编译配置（Configuration）标记：`CONFIG_GEN_PRIV_STACKS`。

### 注释 12：原第 47 行

所有其他对象（objects）。

### 注释 13：原第 88 行

代码覆盖率统计排除区域的起始标记：`LCOV_EXCL_START`。

### 注释 14：原第 93 行

代码覆盖率统计排除区域的结束标记：`LCOV_EXCL_STOP`。

### 注释 15：原第 94 行

条件编译表达式：`!CONFIG_USERSPACE`。

### 注释 16：原第 151 行

代码覆盖率统计排除区域的起始标记：`LCOV_EXCL_START`。

### 注释 17：原第 168 行

代码覆盖率统计排除区域的结束标记：`LCOV_EXCL_STOP`。

### 注释 18：原第 169 行

条件编译配置（Configuration）标记：`CONFIG_DYNAMIC_OBJECTS`。

## 18.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_supplement_reference/P055_zephyr__sys__internal__kobject_internal.h_文件参考.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [k_object_data](../kernel_runtime_model_reference/P020_k_object_data_联合体.md)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [mutex](../kernel_runtime_model_reference/P020_k_object_data_联合体.md#ab285ad5a6119657341be525276837fda)
- [thread_id](../kernel_runtime_model_reference/P020_k_object_data_联合体.md#ada581c427efa9e48b441b1a323bd57e6)
- [stack_data](../kernel_runtime_model_reference/P020_k_object_data_联合体.md#ac8fdffd51c0b32ea262fa98a827a5bd4)
- [unused](../kernel_runtime_model_reference/P020_k_object_data_联合体.md#a2f95fd75c72a619e8c5224e64d1aacc0)
- [k_object](../kernel_runtime_model_reference/P005_k_object_结构体.md)
- [name](../kernel_runtime_model_reference/P005_k_object_结构体.md#ad676d4edce580d351104fe09f174c323)
- [perms](../kernel_runtime_model_reference/P005_k_object_结构体.md#a9e32404b2259979e52b65983ad77ec58)
- [type](../kernel_runtime_model_reference/P005_k_object_结构体.md#a9c8686d9552cb48c24aef939c8a80057)
- [flags](../kernel_runtime_model_reference/P005_k_object_结构体.md#a351cbe565fef17ea75966085be3142c9)
- [data](../kernel_runtime_model_reference/P005_k_object_结构体.md#aea0ad6871d88e2756ba0cbd482fa3aa7)
- [k_object_assignment](../kernel_runtime_model_reference/P006_k_object_assignment_结构体.md)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [thread](../kernel_runtime_model_reference/P006_k_object_assignment_结构体.md#aca82e8f65cfdcfb7497a4b9f3df4eb8d)
- [objects](../kernel_runtime_model_reference/P006_k_object_assignment_结构体.md#ad034fa126915ad604f1edc3b0a177d5a)
- [k_object_init](../api_platform_topic_reference/P126_用户模式内部 API（User Mode Internal APIs）.md#ga50528134a693d656cd60c001f50645ba)
- [k_object_create_dynamic_aligned](../api_platform_topic_reference/P126_用户模式内部 API（User Mode Internal APIs）.md#gafc261408a120975732788b1bd9223036)
- [k_object_create_dynamic](../api_platform_topic_reference/P126_用户模式内部 API（User Mode Internal APIs）.md#ga3879ef0db97f968d82938da87698e359)
- [k_object_assignment::thread](../kernel_runtime_model_reference/P006_k_object_assignment_结构体.md#aca82e8f65cfdcfb7497a4b9f3df4eb8d)
- [k_object_assignment::objects](../kernel_runtime_model_reference/P006_k_object_assignment_结构体.md#ad034fa126915ad604f1edc3b0a177d5a)
- [k_object::flags](../kernel_runtime_model_reference/P005_k_object_结构体.md#a351cbe565fef17ea75966085be3142c9)
- [k_object::type](../kernel_runtime_model_reference/P005_k_object_结构体.md#a9c8686d9552cb48c24aef939c8a80057)
- [k_object::perms](../kernel_runtime_model_reference/P005_k_object_结构体.md#a9e32404b2259979e52b65983ad77ec58)
- [k_object::name](../kernel_runtime_model_reference/P005_k_object_结构体.md#ad676d4edce580d351104fe09f174c323)
- [k_object::data](../kernel_runtime_model_reference/P005_k_object_结构体.md#aea0ad6871d88e2756ba0cbd482fa3aa7)
- [k_object_data::unused](../kernel_runtime_model_reference/P020_k_object_data_联合体.md#a2f95fd75c72a619e8c5224e64d1aacc0)
- [k_object_data::mutex](../kernel_runtime_model_reference/P020_k_object_data_联合体.md#ab285ad5a6119657341be525276837fda)
- [k_object_data::stack_data](../kernel_runtime_model_reference/P020_k_object_data_联合体.md#ac8fdffd51c0b32ea262fa98a827a5bd4)
- [k_object_data::thread_id](../kernel_runtime_model_reference/P020_k_object_data_联合体.md#ada581c427efa9e48b441b1a323bd57e6)

---

[上一章](P017_hfp_hf.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P019_mchp_pic32cm_jh_clock.h_源码浏览.md)
