---
id: learning.zephyr-docs.api-source-runtime-reference.page-36
title: kobject.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kobject_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_kobject.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/kobject_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/kobject_8h.html)。

## 36.1\_原始可见代码（Source Code）

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
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00039"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="agroup__usermode__apis_html_ga2c25103810b5e06fdde8355134bed46c"></a>
<a id="agroup__usermode__apis_html_ga3cb1a024c0178918def2dd0186e565b3"></a>
<a id="agroup__usermode__apis_html_ga5bba3a354fbc63673c76c9815db40812"></a>
<a id="agroup__usermode__apis_html_ga94087bedf96fe2a2bea437d3d585ca22"></a>
<a id="agroup__usermode__apis_html_ga9cc15e8fd7df9cb81c3d7b6c79917aab"></a>
<a id="agroup__usermode__apis_html_gaacd9b4b517db99b3b027dd717e6746b4"></a>
<a id="agroup__usermode__apis_html_gab70fe65497da1347cc4b7bf7ca2daf22"></a>
<a id="agroup__usermode__apis_html_gab99a640325f14a6505a85218dcba5446"></a>
<a id="agroup__usermode__apis_html_gababc731e98a6378323c0d633b2abaa6a"></a>
<a id="agroup__usermode__apis_html_gac1dcfff520e5a2c86ecf9e483900a655"></a>
<a id="akobject_8h_html_af3a248c0e3b05c84b1dd38642f7cf2a1"></a>
<a id="akobject_8h_html_af3a248c0e3b05c84b1dd38642f7cf2a1a51b9ec845f71832ad8fbb35d0cb3e5f6"></a>
<a id="akobject_8h_html_af3a248c0e3b05c84b1dd38642f7cf2a1a7aecd777175f519ce8240e337e1cf430"></a>
<a id="akobject_8h_html_af3a248c0e3b05c84b1dd38642f7cf2a1ab03fc9b624b9a942815d5fb334436fd6"></a>
<a id="akobject__internal_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructk__thread_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2020 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_SYS_KOBJECT_H
#define ZEPHYR_INCLUDE_SYS_KOBJECT_H

#include <stdint.h>
#include <stddef.h>

#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/internal/kobject_internal.h>

#ifdef __cplusplus
extern "C" {
#endif

struct k_thread;
struct k_mutex;

enum k_objects {
        K_OBJ_ANY,
        K_OBJ_DRIVER_ANY,

#include <zephyr/kobj-types-enum.h>

        K_OBJ_LAST
};


#ifdef CONFIG_USERSPACE

#define K_THREAD_ACCESS_GRANT(name_, ...) \
        static void * const _CONCAT(_object_list_, name_)[] = \
                { __VA_ARGS__, NULL }; \
        static const STRUCT_SECTION_ITERABLE(k_object_assignment, \
                                        _CONCAT(_object_access_, name_)) = \
                        { (&_k_thread_obj_ ## name_), \
                          (_CONCAT(_object_list_, name_)) }

#define K_OBJ_FLAG_INITIALIZED  BIT(0)
#define K_OBJ_FLAG_PUBLIC       BIT(1)
#define K_OBJ_FLAG_ALLOC        BIT(2)
#define K_OBJ_FLAG_DRIVER       BIT(3)

__syscall void k_object_access_grant(const void *object,
                                     struct k_thread *thread);

void k_object_access_revoke(const void *object, struct k_thread *thread);

void k_object_access_revoke_others(const void *object);

__syscall void k_object_release(const void *object);

void k_object_access_all_grant(const void *object);

bool k_object_is_valid(const void *obj, enum k_objects otype);

__syscall int k_object_access_check(const void *object);
#else
/* LCOV_EXCL_START */
#define K_THREAD_ACCESS_GRANT(thread, ...)

static inline void z_impl_k_object_access_grant(const void *object,
                                                struct k_thread *thread)
{
        ARG_UNUSED(object);
        ARG_UNUSED(thread);
}

static inline void k_object_access_revoke(const void *object,
                                          struct k_thread *thread)
{
        ARG_UNUSED(object);
        ARG_UNUSED(thread);
}

static inline void k_object_access_revoke_others(const void *object)
{
        ARG_UNUSED(object);
}

static inline void z_impl_k_object_release(const void *object)
{
        ARG_UNUSED(object);
}

static inline void k_object_access_all_grant(const void *object)
{
        ARG_UNUSED(object);
}

static inline bool k_object_is_valid(const void *obj, enum k_objects otype)
{
        ARG_UNUSED(obj);
        ARG_UNUSED(otype);

        return true;
}

static inline int z_impl_k_object_access_check(const void *object)
{
        ARG_UNUSED(object);

        return 0;
}

/* LCOV_EXCL_STOP */
#endif /* !CONFIG_USERSPACE */

#if defined(CONFIG_DYNAMIC_OBJECTS) || defined(__DOXYGEN__)
__syscall void *k_object_alloc(enum k_objects otype);

__syscall void *k_object_alloc_size(enum k_objects otype, size_t size);

void k_object_free(void *obj);
#else

/* LCOV_EXCL_START */
static inline void *z_impl_k_object_alloc(enum k_objects otype)
{
        ARG_UNUSED(otype);

        return NULL;
}

static inline void *z_impl_k_object_alloc_size(enum k_objects otype,
                                        size_t size)
{
        ARG_UNUSED(otype);
        ARG_UNUSED(size);

        return NULL;
}

static inline void k_object_free(void *obj)
{
        ARG_UNUSED(obj);
}
/* LCOV_EXCL_STOP */
#endif /* CONFIG_DYNAMIC_OBJECTS */


#include <zephyr/syscalls/kobject.h>
#ifdef __cplusplus
}
#endif

#endif
```

## 36.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 186 行

代码覆盖率统计排除区域的起始标记：`LCOV_EXCL_START`。

### 注释 3：原第 248 行

代码覆盖率统计排除区域的结束标记：`LCOV_EXCL_STOP`。

### 注释 4：原第 249 行

条件编译表达式：`!CONFIG_USERSPACE`。

### 注释 5：原第 308 行

代码覆盖率统计排除区域的起始标记：`LCOV_EXCL_START`。

### 注释 6：原第 334 行

代码覆盖率统计排除区域的结束标记：`LCOV_EXCL_STOP`。

### 注释 7：原第 335 行

条件编译配置（Configuration）标记：`CONFIG_DYNAMIC_OBJECTS`。

## 36.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/kobject_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/sys/internal/kobject_internal.h](https://docs.zephyrproject.org/latest/doxygen/html/kobject__internal_8h.html)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [k_objects](https://docs.zephyrproject.org/latest/doxygen/html/kobject_8h.html#af3a248c0e3b05c84b1dd38642f7cf2a1)
- [K_OBJ_ANY](https://docs.zephyrproject.org/latest/doxygen/html/kobject_8h.html#af3a248c0e3b05c84b1dd38642f7cf2a1a51b9ec845f71832ad8fbb35d0cb3e5f6)
- [K_OBJ_DRIVER_ANY](https://docs.zephyrproject.org/latest/doxygen/html/kobject_8h.html#af3a248c0e3b05c84b1dd38642f7cf2a1ab03fc9b624b9a942815d5fb334436fd6)
- [K_OBJ_LAST](https://docs.zephyrproject.org/latest/doxygen/html/kobject_8h.html#af3a248c0e3b05c84b1dd38642f7cf2a1a7aecd777175f519ce8240e337e1cf430)
- [k_object_access_grant](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga94087bedf96fe2a2bea437d3d585ca22)
- [k_object_access_revoke](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gab70fe65497da1347cc4b7bf7ca2daf22)
- [k_object_access_revoke_others](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gac1dcfff520e5a2c86ecf9e483900a655)
- [k_object_release](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga3cb1a024c0178918def2dd0186e565b3)
- [k_object_access_all_grant](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gababc731e98a6378323c0d633b2abaa6a)
- [k_object_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gaacd9b4b517db99b3b027dd717e6746b4)
- [k_object_access_check](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga2c25103810b5e06fdde8355134bed46c)
- [k_object_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga5bba3a354fbc63673c76c9815db40812)
- [k_object_alloc_size](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#gab99a640325f14a6505a85218dcba5446)
- [k_object_free](https://docs.zephyrproject.org/latest/doxygen/html/group__usermode__apis.html#ga9cc15e8fd7df9cb81c3d7b6c79917aab)
- [kobject_internal.h](https://docs.zephyrproject.org/latest/doxygen/html/kobject__internal_8h.html)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P035_it8xxx2_pwm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P037_led_strip.h_源码浏览.md)
