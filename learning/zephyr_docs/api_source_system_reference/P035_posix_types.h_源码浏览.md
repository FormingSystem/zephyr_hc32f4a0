---
id: learning.zephyr-docs.api-source-system-reference.page-35
title: posix_types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_posix\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md)。

## 35.1\_原始可见代码（Source Code）

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
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
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
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="foldopen00112"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00136"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="aposix__signal_8h_html_a114f9c2461df851d2ad00aad8dcfa3f7"></a>
<a id="aposix__signal_8h_html_ab3f45e72c67ecc7866d14ab09b3367e7"></a>
<a id="aposix__signal_8h_html_afc544433253791fc5f87b8203c9b6e63"></a>
<a id="aposix__time_8h_html_a6bb3206700910111f26e946bfbf0f2af"></a>
<a id="aposix__time_8h_html_aa37fa84abebf94371f0c8426c2fc614d"></a>
<a id="aposix__types_8h_html_a0f89a9a6420c24efc5254e10170009e9"></a>
<a id="aposix__types_8h_html_a1b893f49dfdf497be09c04a0e40f425e"></a>
<a id="aposix__types_8h_html_a1cf3c794977f92f3ccf2e041a68f3342"></a>
<a id="aposix__types_8h_html_a1d9c308dd59bf38ff0a7a45020d0aefa"></a>
<a id="aposix__types_8h_html_a2489174ff5737a33443b0959f4278765"></a>
<a id="aposix__types_8h_html_a24d58850626c8022bf4bbd5d2628615b"></a>
<a id="aposix__types_8h_html_a2603a6fda916554839174bc7d8849297"></a>
<a id="aposix__types_8h_html_a3a7834be1a79bb0c5a65d3546c2e3bd8"></a>
<a id="aposix__types_8h_html_a3b55f88f25d2c571de53a365ad658426"></a>
<a id="aposix__types_8h_html_a465eb2b962de164efdc8ce957025de7e"></a>
<a id="aposix__types_8h_html_a4e92e3fbb4be682babbb6796af90b50f"></a>
<a id="aposix__types_8h_html_a50c0d048e63387089a42aaf054a6d05b"></a>
<a id="aposix__types_8h_html_a779f87527fcb00a46d12056b753cf22c"></a>
<a id="aposix__types_8h_html_a8fd226393057ab7a8b17ac1c8b061911"></a>
<a id="aposix__types_8h_html_a952c84a825bb4f319cf55c9afb99ee0e"></a>
<a id="aposix__types_8h_html_a9f62774a7a4e1634e60fb611765251f1"></a>
<a id="aposix__types_8h_html_aa9a628992e7bcdc59d4fb606baada347"></a>
<a id="aposix__types_8h_html_acd12f65541fede33b6226f646e900ea6"></a>
<a id="aposix__types_8h_html_aeb637552f63e4c249e7aaeb2905f3db2"></a>
<a id="aposix__types_8h_html_afb4edc6a51d66a7a352424942b631a1e"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructk__sem_html"></a>
<a id="astructpthread__attr__t_html"></a>
<a id="astructpthread__barrierattr_html"></a>
<a id="astructpthread__barrierattr_html_a50ef34671e6743cc59c895dd878c4a86"></a>
<a id="astructpthread__condattr_html"></a>
<a id="astructpthread__condattr_html_ac8f29de493f72c650ea59c71305c3e96"></a>
<a id="astructpthread__mutexattr_html"></a>
<a id="astructpthread__mutexattr_html_a2d6345d486a409d7e9942f102e7f0b59"></a>
<a id="astructpthread__mutexattr_html_afa55f47ff86cf3931d7bbb65de6697c6"></a>
<a id="astructpthread__once_html"></a>
<a id="astructpthread__once_html_a9b9825a6d106c358fc4f2e399418de46"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_POSIX_POSIX_TYPES_H_
#define ZEPHYR_INCLUDE_POSIX_POSIX_TYPES_H_

#if !(defined(CONFIG_NATIVE_LIBC))
#include <sys/types.h>
#endif

#if !defined(_CLOCK_T_DECLARED) && !defined(__clock_t_defined)
typedef unsigned long clock_t;
#define _CLOCK_T_DECLARED
#define __clock_t_defined
#endif

#if !defined(_CLOCKID_T_DECLARED) && !defined(__clockid_t_defined)
typedef unsigned long clockid_t;
#define _CLOCKID_T_DECLARED
#define __clockid_t_defined
#endif

#ifdef CONFIG_NEWLIB_LIBC
#include <sys/_pthreadtypes.h>
#endif

#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif

#if !defined(_DEV_T_DECLARED) && !defined(__dev_t_defined)
typedef int dev_t;
#define _DEV_T_DECLARED
#define __dev_t_defined
#endif

#if !defined(_INO_T_DECLARED) && !defined(__ino_t_defined)
typedef int ino_t;
#define _INO_T_DECLARED
#define __ino_t_defined
#endif

#if !defined(_NLINK_T_DECLARED) && !defined(__nlink_t_defined)
typedef unsigned short nlink_t;
#define _NLINK_T_DECLARED
#define __nlink_t_defined
#endif

#if !defined(_UID_T_DECLARED) && !defined(__uid_t_defined)
typedef unsigned short uid_t;
#define _UID_T_DECLARED
#define __uid_t_defined
#endif

#if !defined(_GID_T_DECLARED) && !defined(__gid_t_defined)
typedef unsigned short gid_t;
#define _GID_T_DECLARED
#define __gid_t_defined
#endif

#if !defined(_BLKSIZE_T_DECLARED) && !defined(__blksize_t_defined)
typedef unsigned long blksize_t;
#define _BLKSIZE_T_DECLARED
#define __blksize_t_defined
#endif

#if !defined(_BLKCNT_T_DECLARED) && !defined(__blkcnt_t_defined)
typedef unsigned long blkcnt_t;
#define _BLKCNT_T_DECLARED
#define __blkcnt_t_defined
#endif

#if !defined(CONFIG_ARCMWDT_LIBC)
typedef int pid_t;
#endif

#if !defined(_USECONDS_T_DECLARED) && !defined(__useconds_t_defined)
typedef unsigned long useconds_t;
#endif

/* time related attributes */
#if !defined(__timer_t_defined) && !defined(_TIMER_T_DECLARED)
typedef unsigned long timer_t;
#endif

/* Thread attributes */
#if !defined(CONFIG_NEWLIB_LIBC)
#if !defined(_PTHREAD_ATTR_T_DECLARED) && !defined(__pthread_attr_t_defined)
typedef struct {
        void *stack;
        unsigned int details[2];
} pthread_attr_t;
#define _PTHREAD_ATTR_T_DECLARED
#define __pthread_attr_t_defined
#endif
#endif

typedef uint32_t pthread_t;
typedef uint32_t pthread_spinlock_t;

/* Semaphore */
typedef struct k_sem sem_t;

/* Mutex */
typedef uint32_t pthread_mutex_t;

struct pthread_mutexattr {
        unsigned char type: 2;
        bool initialized: 1;
};
#if !defined(CONFIG_NEWLIB_LIBC)
typedef struct pthread_mutexattr pthread_mutexattr_t;
BUILD_ASSERT(sizeof(pthread_mutexattr_t) >= sizeof(struct pthread_mutexattr));
#endif

/* Condition variables */
typedef uint32_t pthread_cond_t;

struct pthread_condattr {
        clockid_t clock;
};

#if !defined(CONFIG_NEWLIB_LIBC)
typedef struct pthread_condattr pthread_condattr_t;
BUILD_ASSERT(sizeof(pthread_condattr_t) >= sizeof(struct pthread_condattr));
#endif

/* Barrier */
typedef uint32_t pthread_barrier_t;

typedef struct pthread_barrierattr {
        int pshared;
} pthread_barrierattr_t;

typedef uint32_t pthread_rwlockattr_t;

typedef uint32_t pthread_rwlock_t;

struct pthread_once {
        bool flag;
};

#if !defined(CONFIG_NEWLIB_LIBC)
typedef uint32_t pthread_key_t;
typedef struct pthread_once pthread_once_t;
/* Newlib typedefs pthread_once_t as a struct with two ints */
BUILD_ASSERT(sizeof(pthread_once_t) >= sizeof(struct pthread_once));
#endif

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_POSIX_TYPES_H_ */
```

## 35.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 86 行

时间相关属性（Time-Related Attributes）。

### 注释 3：原第 91 行

线程属性（Thread Attributes）。

### 注释 4：原第 106 行

信号量（Semaphore）

### 注释 5：原第 109 行

互斥锁（Mutex）

### 注释 6：原第 121 行

条件变量（Condition Variables）。

### 注释 7：原第 133 行

屏障（Barrier）。

### 注释 8：原第 151 行

Newlib 将 `pthread_once_t` 定义为含两个 `int` 成员的结构体（Struct）。

### 注释 9：原第 159 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_POSIX_TYPES_H_`。

## 35.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md)
- [sys/types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [clock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a3b55f88f25d2c571de53a365ad658426)
- [clockid_t](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a6bb3206700910111f26e946bfbf0f2af)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [dev_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a0f89a9a6420c24efc5254e10170009e9)
- [ino_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a779f87527fcb00a46d12056b753cf22c)
- [nlink_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a952c84a825bb4f319cf55c9afb99ee0e)
- [uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)
- [gid_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a3a7834be1a79bb0c5a65d3546c2e3bd8)
- [blksize_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a50c0d048e63387089a42aaf054a6d05b)
- [blkcnt_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#aa9a628992e7bcdc59d4fb606baada347)
- [pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)
- [useconds_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a1cf3c794977f92f3ccf2e041a68f3342)
- [timer_t](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#aa37fa84abebf94371f0c8426c2fc614d)
- [pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)
- [pthread_spinlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a1d9c308dd59bf38ff0a7a45020d0aefa)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [sem_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#afb4edc6a51d66a7a352424942b631a1e)
- [pthread_mutex_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a465eb2b962de164efdc8ce957025de7e)
- [pthread_mutexattr](../posix_system_model_reference/P014_pthread_mutexattr_结构体.md)
- [type](../posix_system_model_reference/P014_pthread_mutexattr_结构体.md#a2d6345d486a409d7e9942f102e7f0b59)
- [initialized](../posix_system_model_reference/P014_pthread_mutexattr_结构体.md#afa55f47ff86cf3931d7bbb65de6697c6)
- [pthread_mutexattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a2489174ff5737a33443b0959f4278765)
- [pthread_cond_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a1b893f49dfdf497be09c04a0e40f425e)
- [pthread_condattr](../posix_system_model_reference/P013_pthread_condattr_结构体.md)
- [clock](../posix_system_model_reference/P013_pthread_condattr_结构体.md#ac8f29de493f72c650ea59c71305c3e96)
- [pthread_condattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a9f62774a7a4e1634e60fb611765251f1)
- [pthread_barrier_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#aeb637552f63e4c249e7aaeb2905f3db2)
- [pthread_barrierattr](../posix_system_model_reference/P012_pthread_barrierattr_结构体.md)
- [pshared](../posix_system_model_reference/P012_pthread_barrierattr_结构体.md#a50ef34671e6743cc59c895dd878c4a86)
- [pthread_barrierattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a24d58850626c8022bf4bbd5d2628615b)
- [pthread_rwlockattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a4e92e3fbb4be682babbb6796af90b50f)
- [pthread_rwlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#acd12f65541fede33b6226f646e900ea6)
- [pthread_once](../posix_system_model_reference/P015_pthread_once_结构体.md)
- [flag](../posix_system_model_reference/P015_pthread_once_结构体.md#a9b9825a6d106c358fc4f2e399418de46)
- [pthread_key_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a8fd226393057ab7a8b17ac1c8b061911)
- [pthread_once_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a2603a6fda916554839174bc7d8849297)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [pthread_barrierattr::pshared](../posix_system_model_reference/P012_pthread_barrierattr_结构体.md#a50ef34671e6743cc59c895dd878c4a86)
- [pthread_condattr::clock](../posix_system_model_reference/P013_pthread_condattr_结构体.md#ac8f29de493f72c650ea59c71305c3e96)
- [pthread_mutexattr::type](../posix_system_model_reference/P014_pthread_mutexattr_结构体.md#a2d6345d486a409d7e9942f102e7f0b59)
- [pthread_mutexattr::initialized](../posix_system_model_reference/P014_pthread_mutexattr_结构体.md#afa55f47ff86cf3931d7bbb65de6697c6)
- [pthread_once::flag](../posix_system_model_reference/P015_pthread_once_结构体.md#a9b9825a6d106c358fc4f2e399418de46)

---

[上一章](P034_posix_limits.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P036_r8a7795_cpg_mssr.h_源码浏览.md)
