---
id: learning.zephyr-docs.api-file-secure-value-reference.page-11
title: zephyr__posix__pthread.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_posix\_\_pthread.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pthread_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <zephyr/kernel.h>
#include <zephyr/posix/unistd.h>
#include <zephyr/posix/sched.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_a391c5eb0f6b5febc48710d0be3f62394"></a>

```c
#define PTHREAD_CREATE_DETACHED 1
```

相关声明：[PTHREAD_CREATE_DETACHED](#a391c5eb0f6b5febc48710d0be3f62394)。

<a id="r_afb10d234d831c7b57768d62786748bc7"></a>

```c
#define PTHREAD_CREATE_JOINABLE 0
```

相关声明：[PTHREAD_CREATE_JOINABLE](#afb10d234d831c7b57768d62786748bc7)。

<a id="r_a443f2f512de9324bf77625041ecb04f4"></a>

```c
#define PTHREAD_PROCESS_PRIVATE 0
```

相关声明：[PTHREAD_PROCESS_PRIVATE](#a443f2f512de9324bf77625041ecb04f4)。

<a id="r_a07f3670a510cdb93233e84e1a0b50e89"></a>

```c
#define PTHREAD_PROCESS_SHARED 1
```

相关声明：[PTHREAD_PROCESS_SHARED](#a07f3670a510cdb93233e84e1a0b50e89)。

<a id="r_a17ddda04a6c1ee32116c49c85e2ac4ae"></a>

```c
#define PTHREAD_CANCELED ((void *)-1)
```

相关声明：[PTHREAD_CANCELED](#a17ddda04a6c1ee32116c49c85e2ac4ae)。

<a id="r_aaf18882a8a6b82c7b7849a645f4445ef"></a>

```c
#define PTHREAD_CANCEL_ENABLE 0
```

相关声明：[PTHREAD_CANCEL_ENABLE](#aaf18882a8a6b82c7b7849a645f4445ef)。

<a id="r_a6c661332f782dcebc87b878990424b4c"></a>

```c
#define PTHREAD_CANCEL_DISABLE 1
```

相关声明：[PTHREAD_CANCEL_DISABLE](#a6c661332f782dcebc87b878990424b4c)。

<a id="r_a7559901d88e4d3b8100b407e164cd75e"></a>

```c
#define PTHREAD_CANCEL_DEFERRED 0
```

相关声明：[PTHREAD_CANCEL_DEFERRED](#a7559901d88e4d3b8100b407e164cd75e)。

<a id="r_aae774738da39ed214c9b01f342222686"></a>

```c
#define PTHREAD_CANCEL_ASYNCHRONOUS 1
```

相关声明：[PTHREAD_CANCEL_ASYNCHRONOUS](#aae774738da39ed214c9b01f342222686)。

<a id="r_aeab18be4f4ee13db4b0b65c6768fb539"></a>

```c
#define PTHREAD_SCOPE_PROCESS 1
```

相关声明：[PTHREAD_SCOPE_PROCESS](#aeab18be4f4ee13db4b0b65c6768fb539)。

<a id="r_ab754f4339f76c46b8f57413c03e8ec65"></a>

```c
#define PTHREAD_SCOPE_SYSTEM 0
```

相关声明：[PTHREAD_SCOPE_SYSTEM](#ab754f4339f76c46b8f57413c03e8ec65)。

<a id="r_a470fccc57c4d7c3846e446a17cd23573"></a>

```c
#define PTHREAD_INHERIT_SCHED 0
```

相关声明：[PTHREAD_INHERIT_SCHED](#a470fccc57c4d7c3846e446a17cd23573)。

<a id="r_ad45abe03c8232518b6995e73172fe053"></a>

```c
#define PTHREAD_EXPLICIT_SCHED 1
```

相关声明：[PTHREAD_EXPLICIT_SCHED](#ad45abe03c8232518b6995e73172fe053)。

<a id="r_a59e22497b65fc305ddb5cea8b4990b51"></a>

```c
#define PTHREAD_ONCE_INIT {0}
```

相关声明：[PTHREAD_ONCE_INIT](#a59e22497b65fc305ddb5cea8b4990b51)。

<a id="r_a8b3dc1c5c1a165d6143b1dce950e8266"></a>

```c
#define PTHREAD_STACK_MIN K_KERNEL_STACK_LEN(0)
```

相关声明：[PTHREAD_STACK_MIN](#a8b3dc1c5c1a165d6143b1dce950e8266)、[K_KERNEL_STACK_LEN](../thread_stack_reference/P002_线程栈头文件参考.md#a12f78cb2d5b9bf83068e810bf1e31937)。

<a id="r_aa7b867fe46f3660283fcb356c4fcbbf0"></a>

```c
#define PTHREAD_COND_INITIALIZER (-1)
```

相关声明：[PTHREAD_COND_INITIALIZER](#aa7b867fe46f3660283fcb356c4fcbbf0)。

将条件变量（Condition Variable）声明为已初始化。

<a id="r_a84e55100366a6a8338a2af3b3f279686"></a>

```c
#define PTHREAD_MUTEX_INITIALIZER (-1)
```

相关声明：[PTHREAD_MUTEX_INITIALIZER](#a84e55100366a6a8338a2af3b3f279686)。

将互斥锁（Mutex）声明为已初始化。

<a id="r_aa92fd7b492a8a5b31b2f8b3b6039c622"></a>

```c
#define PTHREAD_RWLOCK_INITIALIZER (-1)
```

相关声明：[PTHREAD_RWLOCK_INITIALIZER](#aa92fd7b492a8a5b31b2f8b3b6039c622)。

将读写锁（Read-write Lock）声明为已初始化。

<a id="r_aae4b650085c2599674938f503d6253cf"></a>

```c
#define PTHREAD_MUTEX_NORMAL 0
```

相关声明：[PTHREAD_MUTEX_NORMAL](#aae4b650085c2599674938f503d6253cf)。

<a id="r_a715e9644a7183d98cb2c9dd41cb89645"></a>

```c
#define PTHREAD_MUTEX_RECURSIVE 1
```

相关声明：[PTHREAD_MUTEX_RECURSIVE](#a715e9644a7183d98cb2c9dd41cb89645)。

<a id="r_aaf502496651f95b06be861af7902cb23"></a>

```c
#define PTHREAD_MUTEX_ERRORCHECK 2
```

相关声明：[PTHREAD_MUTEX_ERRORCHECK](#aaf502496651f95b06be861af7902cb23)。

<a id="r_a2a9b96c0491ae490c17d0b400bc427b0"></a>

```c
#define PTHREAD_MUTEX_DEFAULT PTHREAD_MUTEX_NORMAL
```

相关声明：[PTHREAD_MUTEX_DEFAULT](#a2a9b96c0491ae490c17d0b400bc427b0)、[PTHREAD_MUTEX_NORMAL](#aae4b650085c2599674938f503d6253cf)。

<a id="r_a8c1426a72025b27d9726580ac0e8404f"></a>

```c
#define PTHREAD_PRIO_NONE 0
```

相关声明：[PTHREAD_PRIO_NONE](#a8c1426a72025b27d9726580ac0e8404f)。

<a id="r_a0087e0ca82fd36e6c15f4c8ad443dbfc"></a>

```c
#define PTHREAD_PRIO_INHERIT 1
```

相关声明：[PTHREAD_PRIO_INHERIT](#a0087e0ca82fd36e6c15f4c8ad443dbfc)。

<a id="r_a65da4c842cd4287f43d2f69ad5a5470b"></a>

```c
#define PTHREAD_PRIO_PROTECT 2
```

相关声明：[PTHREAD_PRIO_PROTECT](#a65da4c842cd4287f43d2f69ad5a5470b)。

<a id="r_a822c63bc662ad86cfb2dcec50edbb42b"></a>

```c
#define PTHREAD_BARRIER_SERIAL_THREAD 1
```

相关声明：[PTHREAD_BARRIER_SERIAL_THREAD](#a822c63bc662ad86cfb2dcec50edbb42b)。

<a id="r_a7c56b94733c97109259266d9c1f60338"></a>

```c
#define PTHREAD_PROCESS_PRIVATE 0
```

相关声明：[PTHREAD_PROCESS_PRIVATE](#a7c56b94733c97109259266d9c1f60338)。

<a id="r_afff2f9c2b019a07298f341cf70ee829d"></a>

```c
#define PTHREAD_PROCESS_PUBLIC 1
```

相关声明：[PTHREAD_PROCESS_PUBLIC](#afff2f9c2b019a07298f341cf70ee829d)。

<a id="r_a265bda35a73d502fe8b710dc34f421cc"></a>

```c
#define pthread_cleanup_push(_rtn, _arg)
```

相关声明：[pthread_cleanup_push](#a265bda35a73d502fe8b710dc34f421cc)。

<a id="r_a234ffab9eecdb6ae28198aeeedb4f10c"></a>

```c
#define pthread_cleanup_pop(_ex)
```

相关声明：[pthread_cleanup_pop](#a234ffab9eecdb6ae28198aeeedb4f10c)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.2\_函数（Functions）

<a id="r_a319a61cdb25d069c9d4504e8225fd0c3"></a>

```c
int pthread_cond_init (pthread_cond_t *cv, const pthread_condattr_t *att)
```

相关声明：[pthread_cond_init](#a319a61cdb25d069c9d4504e8225fd0c3)、[pthread_cond_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a1b893f49dfdf497be09c04a0e40f425e)、[pthread_condattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a9f62774a7a4e1634e60fb611765251f1)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a8d44e4eae235f675bbab1b9163a3bc1d"></a>

```c
int pthread_cond_destroy (pthread_cond_t *cv)
```

相关声明：[pthread_cond_destroy](#a8d44e4eae235f675bbab1b9163a3bc1d)、[pthread_cond_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a1b893f49dfdf497be09c04a0e40f425e)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_add1fea97e50755b5dbf4bd9a83b710dd"></a>

```c
int pthread_cond_signal (pthread_cond_t *cv)
```

相关声明：[pthread_cond_signal](#add1fea97e50755b5dbf4bd9a83b710dd)、[pthread_cond_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a1b893f49dfdf497be09c04a0e40f425e)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a91ff7fff67462ce9216d299c89683119"></a>

```c
int pthread_cond_broadcast (pthread_cond_t *cv)
```

相关声明：[pthread_cond_broadcast](#a91ff7fff67462ce9216d299c89683119)、[pthread_cond_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a1b893f49dfdf497be09c04a0e40f425e)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a61a1bf88d32de361e82ef4ea99b47322"></a>

```c
int pthread_cond_wait (pthread_cond_t *cv, pthread_mutex_t *mut)
```

相关声明：[pthread_cond_wait](#a61a1bf88d32de361e82ef4ea99b47322)、[pthread_cond_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a1b893f49dfdf497be09c04a0e40f425e)、[pthread_mutex_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a465eb2b962de164efdc8ce957025de7e)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_aecea498fbd2df02942790e5ccd7d78b2"></a>

```c
int pthread_cond_timedwait (pthread_cond_t *cv, pthread_mutex_t *mut, const struct timespec *abstime)
```

相关声明：[pthread_cond_timedwait](#aecea498fbd2df02942790e5ccd7d78b2)、[pthread_cond_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a1b893f49dfdf497be09c04a0e40f425e)、[pthread_mutex_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a465eb2b962de164efdc8ce957025de7e)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a01159da320b2317ee286a7e92d713f16"></a>

```c
int pthread_condattr_init (pthread_condattr_t *att)
```

相关声明：[pthread_condattr_init](#a01159da320b2317ee286a7e92d713f16)、[pthread_condattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a9f62774a7a4e1634e60fb611765251f1)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_af37eaf73f0d83989d8efc06e676909f1"></a>

```c
int pthread_condattr_destroy (pthread_condattr_t *att)
```

相关声明：[pthread_condattr_destroy](#af37eaf73f0d83989d8efc06e676909f1)、[pthread_condattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a9f62774a7a4e1634e60fb611765251f1)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a77376b018eec6db2986939b847915a3c"></a>

```c
int pthread_condattr_getclock (const pthread_condattr_t *ZRESTRICT att, clockid_t *ZRESTRICT clock_id)
```

相关声明：[pthread_condattr_getclock](#a77376b018eec6db2986939b847915a3c)、[pthread_condattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a9f62774a7a4e1634e60fb611765251f1)、[clockid_t](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a6bb3206700910111f26e946bfbf0f2af)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_ac0b4f6d49deeab0ddb269a23ee303156"></a>

```c
int pthread_condattr_setclock (pthread_condattr_t *att, clockid_t clock_id)
```

相关声明：[pthread_condattr_setclock](#ac0b4f6d49deeab0ddb269a23ee303156)、[pthread_condattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a9f62774a7a4e1634e60fb611765251f1)、[clockid_t](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a6bb3206700910111f26e946bfbf0f2af)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_af89d9cfa300f33b46720a96eac83d175"></a>

```c
int pthread_mutex_destroy (pthread_mutex_t *m)
```

相关声明：[pthread_mutex_destroy](#af89d9cfa300f33b46720a96eac83d175)、[pthread_mutex_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a465eb2b962de164efdc8ce957025de7e)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_afd70d6f2c50e22b996c926fb9d6ad291"></a>

```c
int pthread_mutex_lock (pthread_mutex_t *m)
```

相关声明：[pthread_mutex_lock](#afd70d6f2c50e22b996c926fb9d6ad291)、[pthread_mutex_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a465eb2b962de164efdc8ce957025de7e)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a02a3c64dac70730e226c31c0e7dbb45c"></a>

```c
int pthread_mutex_unlock (pthread_mutex_t *m)
```

相关声明：[pthread_mutex_unlock](#a02a3c64dac70730e226c31c0e7dbb45c)、[pthread_mutex_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a465eb2b962de164efdc8ce957025de7e)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_abbec44a62531009629601fbb34f1027c"></a>

```c
int pthread_mutex_timedlock (pthread_mutex_t *m, const struct timespec *abstime)
```

相关声明：[pthread_mutex_timedlock](#abbec44a62531009629601fbb34f1027c)、[pthread_mutex_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a465eb2b962de164efdc8ce957025de7e)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_acc1ccbaf3d76572da85a8030bba1ede4"></a>

```c
int pthread_mutex_trylock (pthread_mutex_t *m)
```

相关声明：[pthread_mutex_trylock](#acc1ccbaf3d76572da85a8030bba1ede4)、[pthread_mutex_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a465eb2b962de164efdc8ce957025de7e)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a7948bc0ea8a33439aece34d0fb3daf8b"></a>

```c
int pthread_mutex_init (pthread_mutex_t *m, const pthread_mutexattr_t *att)
```

相关声明：[pthread_mutex_init](#a7948bc0ea8a33439aece34d0fb3daf8b)、[pthread_mutex_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a465eb2b962de164efdc8ce957025de7e)、[pthread_mutexattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a2489174ff5737a33443b0959f4278765)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_ae7e6584c2b2cf9b9ff061115d2342bb5"></a>

```c
int pthread_mutexattr_setprotocol (pthread_mutexattr_t *attr, int protocol)
```

相关声明：[pthread_mutexattr_setprotocol](#ae7e6584c2b2cf9b9ff061115d2342bb5)、[pthread_mutexattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a2489174ff5737a33443b0959f4278765)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a8387c80e660e9426f801ac0217ecfae5"></a>

```c
int pthread_mutexattr_settype (pthread_mutexattr_t *attr, int type)
```

相关声明：[pthread_mutexattr_settype](#a8387c80e660e9426f801ac0217ecfae5)、[pthread_mutexattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a2489174ff5737a33443b0959f4278765)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a200fcbc9157e6183376f83bc0e5937dd"></a>

```c
int pthread_mutexattr_getprotocol (const pthread_mutexattr_t *attr, int *protocol)
```

相关声明：[pthread_mutexattr_getprotocol](#a200fcbc9157e6183376f83bc0e5937dd)、[pthread_mutexattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a2489174ff5737a33443b0959f4278765)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a7f064a4db96a009a5a9a7c7e5cc03599"></a>

```c
int pthread_mutexattr_gettype (const pthread_mutexattr_t *attr, int *type)
```

相关声明：[pthread_mutexattr_gettype](#a7f064a4db96a009a5a9a7c7e5cc03599)、[pthread_mutexattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a2489174ff5737a33443b0959f4278765)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_af98f6b6c483077a39d1400b1de1577b8"></a>

```c
int pthread_mutexattr_init (pthread_mutexattr_t *attr)
```

相关声明：[pthread_mutexattr_init](#af98f6b6c483077a39d1400b1de1577b8)、[pthread_mutexattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a2489174ff5737a33443b0959f4278765)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a2321aabf58224b06021185708d0f9658"></a>

```c
int pthread_mutexattr_destroy (pthread_mutexattr_t *attr)
```

相关声明：[pthread_mutexattr_destroy](#a2321aabf58224b06021185708d0f9658)、[pthread_mutexattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a2489174ff5737a33443b0959f4278765)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_af786372165ba080986ae4143928c5436"></a>

```c
int pthread_barrier_wait (pthread_barrier_t *b)
```

相关声明：[pthread_barrier_wait](#af786372165ba080986ae4143928c5436)、[pthread_barrier_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#aeb637552f63e4c249e7aaeb2905f3db2)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_aecc6c99901aac517072970e153863296"></a>

```c
int pthread_barrier_init (pthread_barrier_t *b, const pthread_barrierattr_t *attr, unsigned int count)
```

相关声明：[pthread_barrier_init](#aecc6c99901aac517072970e153863296)、[pthread_barrier_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#aeb637552f63e4c249e7aaeb2905f3db2)、[pthread_barrierattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a24d58850626c8022bf4bbd5d2628615b)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_ab05ae13769e61dea9c53ca7894743c8f"></a>

```c
int pthread_barrier_destroy (pthread_barrier_t *b)
```

相关声明：[pthread_barrier_destroy](#ab05ae13769e61dea9c53ca7894743c8f)、[pthread_barrier_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#aeb637552f63e4c249e7aaeb2905f3db2)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_ad540451ab679ace869b51c7cbb7b8486"></a>

```c
int pthread_barrierattr_init (pthread_barrierattr_t *b)
```

相关声明：[pthread_barrierattr_init](#ad540451ab679ace869b51c7cbb7b8486)、[pthread_barrierattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a24d58850626c8022bf4bbd5d2628615b)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a5e27d4773f3d0552e36f2ff3b922a988"></a>

```c
int pthread_barrierattr_destroy (pthread_barrierattr_t *b)
```

相关声明：[pthread_barrierattr_destroy](#a5e27d4773f3d0552e36f2ff3b922a988)、[pthread_barrierattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a24d58850626c8022bf4bbd5d2628615b)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_aa9c3c335f5bcf702fe85a1c12dcdc70e"></a>

```c
int pthread_barrierattr_setpshared (pthread_barrierattr_t *attr, int pshared)
```

相关声明：[pthread_barrierattr_setpshared](#aa9c3c335f5bcf702fe85a1c12dcdc70e)、[pthread_barrierattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a24d58850626c8022bf4bbd5d2628615b)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a54e367403c0524680115b780ccfbc586"></a>

```c
int pthread_barrierattr_getpshared (const pthread_barrierattr_t *ZRESTRICT attr, int *ZRESTRICT pshared)
```

相关声明：[pthread_barrierattr_getpshared](#a54e367403c0524680115b780ccfbc586)、[pthread_barrierattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a24d58850626c8022bf4bbd5d2628615b)。

可移植操作系统接口（POSIX）线程兼容 API。

<a id="r_a4c4f5f3b4f8f45d9d897847d53b11aaa"></a>

```c
pthread_t pthread_self (void)
```

相关声明：[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)、[pthread_self](#a4c4f5f3b4f8f45d9d897847d53b11aaa)。

获取调用线程的 ID（Thread ID）。

<a id="r_a2a460fe3d4e4518057366f6ead455f4a"></a>

```c
int pthread_equal (pthread_t pt1, pthread_t pt2)
```

相关声明：[pthread_equal](#a2a460fe3d4e4518057366f6ead455f4a)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)。

比较线程 ID（Thread IDs）。

<a id="r_a78a54e67f0afe2601dbda0a904fa0bdf"></a>

```c
int pthread_rwlockattr_destroy (pthread_rwlockattr_t *attr)
```

相关声明：[pthread_rwlockattr_destroy](#a78a54e67f0afe2601dbda0a904fa0bdf)、[pthread_rwlockattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a4e92e3fbb4be682babbb6796af90b50f)。

销毁读写锁属性对象（Read-write Lock Attributes Object）。

<a id="r_a9d831af0179ed16d1b6cbeba0304810b"></a>

```c
int pthread_rwlockattr_init (pthread_rwlockattr_t *attr)
```

相关声明：[pthread_rwlockattr_init](#a9d831af0179ed16d1b6cbeba0304810b)、[pthread_rwlockattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a4e92e3fbb4be682babbb6796af90b50f)。

初始化读写锁属性对象（Read-write Lock Attributes Object）。

<a id="r_a5ca1dea9ea7d3cfb34a9c8561e47cf02"></a>

```c
int pthread_rwlockattr_getpshared (const pthread_rwlockattr_t *ZRESTRICT attr, int *ZRESTRICT pshared)
```

相关声明：[pthread_rwlockattr_getpshared](#a5ca1dea9ea7d3cfb34a9c8561e47cf02)、[pthread_rwlockattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a4e92e3fbb4be682babbb6796af90b50f)。

<a id="r_ae6550aa6aede71f618bb7457f3e50524"></a>

```c
int pthread_rwlockattr_setpshared (pthread_rwlockattr_t *attr, int pshared)
```

相关声明：[pthread_rwlockattr_setpshared](#ae6550aa6aede71f618bb7457f3e50524)、[pthread_rwlockattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a4e92e3fbb4be682babbb6796af90b50f)。

<a id="r_abee3ae43d1f00b597111f6f82b0416a1"></a>

```c
int pthread_attr_getguardsize (const pthread_attr_t *ZRESTRICT attr, size_t *ZRESTRICT guardsize)
```

相关声明：[pthread_attr_getguardsize](#abee3ae43d1f00b597111f6f82b0416a1)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_ae23600d4670359ab12bfba20db2c9a37"></a>

```c
int pthread_attr_getstacksize (const pthread_attr_t *attr, size_t *stacksize)
```

相关声明：[pthread_attr_getstacksize](#ae23600d4670359ab12bfba20db2c9a37)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_a532b31c11a9d87663053c5342400758c"></a>

```c
int pthread_attr_setguardsize (pthread_attr_t *attr, size_t guardsize)
```

相关声明：[pthread_attr_setguardsize](#a532b31c11a9d87663053c5342400758c)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_a812a9a455ae2ef2bb0dca4fff201a281"></a>

```c
int pthread_attr_setstacksize (pthread_attr_t *attr, size_t stacksize)
```

相关声明：[pthread_attr_setstacksize](#a812a9a455ae2ef2bb0dca4fff201a281)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_a79b4c9e71486a87ef3014f1c660b33eb"></a>

```c
int pthread_attr_setschedpolicy (pthread_attr_t *attr, int policy)
```

相关声明：[pthread_attr_setschedpolicy](#a79b4c9e71486a87ef3014f1c660b33eb)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_af032906f326f3c209c7eed6bb248ebee"></a>

```c
int pthread_attr_getschedpolicy (const pthread_attr_t *attr, int *policy)
```

相关声明：[pthread_attr_getschedpolicy](#af032906f326f3c209c7eed6bb248ebee)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_ae6ee78c307d8467b34a9b0c330993a54"></a>

```c
int pthread_attr_setdetachstate (pthread_attr_t *attr, int detachstate)
```

相关声明：[pthread_attr_setdetachstate](#ae6ee78c307d8467b34a9b0c330993a54)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_a391c34da42e68ddd24f5ee0c070d5c4f"></a>

```c
int pthread_attr_getdetachstate (const pthread_attr_t *attr, int *detachstate)
```

相关声明：[pthread_attr_getdetachstate](#a391c34da42e68ddd24f5ee0c070d5c4f)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_a0b85ebb1e3aac081a4c0a5e85ae3cbe9"></a>

```c
int pthread_attr_init (pthread_attr_t *attr)
```

相关声明：[pthread_attr_init](#a0b85ebb1e3aac081a4c0a5e85ae3cbe9)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_a4bcdbf47c17c7dcc51e9f05f5cb56d81"></a>

```c
int pthread_attr_destroy (pthread_attr_t *attr)
```

相关声明：[pthread_attr_destroy](#a4bcdbf47c17c7dcc51e9f05f5cb56d81)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_abcd67baa86ff65d7ce65985d8b50d579"></a>

```c
int pthread_attr_getschedparam (const pthread_attr_t *attr, struct sched_param *schedparam)
```

相关声明：[pthread_attr_getschedparam](#abcd67baa86ff65d7ce65985d8b50d579)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_ac60393667965dbd06670d3d280b65757"></a>

```c
int pthread_getschedparam (pthread_t pthread, int *policy, struct sched_param *param)
```

相关声明：[pthread_getschedparam](#ac60393667965dbd06670d3d280b65757)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)。

<a id="r_aec19ad460995a9fe8aeb4eaf2bb1ed1d"></a>

```c
int pthread_attr_getstack (const pthread_attr_t *attr, void **stackaddr, size_t *stacksize)
```

相关声明：[pthread_attr_getstack](#aec19ad460995a9fe8aeb4eaf2bb1ed1d)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_a94ede89b99a3a4fa17e516d30aaf3409"></a>

```c
int pthread_attr_setstack (pthread_attr_t *attr, void *stackaddr, size_t stacksize)
```

相关声明：[pthread_attr_setstack](#a94ede89b99a3a4fa17e516d30aaf3409)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_ad3fe01698c4fad85bb5cc3f9a2e82ea3"></a>

```c
int pthread_attr_getscope (const pthread_attr_t *attr, int *contentionscope)
```

相关声明：[pthread_attr_getscope](#ad3fe01698c4fad85bb5cc3f9a2e82ea3)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_a6d8d320a882ba044a064975dddcf9ced"></a>

```c
int pthread_attr_setscope (pthread_attr_t *attr, int contentionscope)
```

相关声明：[pthread_attr_setscope](#a6d8d320a882ba044a064975dddcf9ced)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_a79a77b688c30213e5e52e6be178cde4e"></a>

```c
int pthread_attr_getinheritsched (const pthread_attr_t *attr, int *inheritsched)
```

相关声明：[pthread_attr_getinheritsched](#a79a77b688c30213e5e52e6be178cde4e)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_ad437fe8caa3ef9f0cb7d69f6f6479df9"></a>

```c
int pthread_attr_setinheritsched (pthread_attr_t *attr, int inheritsched)
```

相关声明：[pthread_attr_setinheritsched](#ad437fe8caa3ef9f0cb7d69f6f6479df9)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_ab9a027122b38833e8c2e1c0e733da3e6"></a>

```c
FUNC_NORETURN void pthread_exit (void *retval)
```

相关声明：[pthread_exit](#ab9a027122b38833e8c2e1c0e733da3e6)。

<a id="r_a742eefdf61f97bf1607d15a4fa2a3173"></a>

```c
int pthread_timedjoin_np (pthread_t thread, void **status, const struct timespec *abstime)
```

相关声明：[pthread_timedjoin_np](#a742eefdf61f97bf1607d15a4fa2a3173)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_a32dd5d2994c5ca7dd33294ce8cbd13bf"></a>

```c
int pthread_tryjoin_np (pthread_t thread, void **status)
```

相关声明：[pthread_tryjoin_np](#a32dd5d2994c5ca7dd33294ce8cbd13bf)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)。

<a id="r_a6e4d503c2b358be5c98330f9006b3417"></a>

```c
int pthread_join (pthread_t thread, void **status)
```

相关声明：[pthread_join](#a6e4d503c2b358be5c98330f9006b3417)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)。

<a id="r_a66a8f4bac5afe05538794218ff7c85ea"></a>

```c
int pthread_cancel (pthread_t pthread)
```

相关声明：[pthread_cancel](#a66a8f4bac5afe05538794218ff7c85ea)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)。

<a id="r_a7c275c509c26566b6dd95a2de1668a2f"></a>

```c
int pthread_detach (pthread_t thread)
```

相关声明：[pthread_detach](#a7c275c509c26566b6dd95a2de1668a2f)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)。

<a id="r_adcf534f63e3c1e209befc503d5a3db74"></a>

```c
int pthread_create (pthread_t *newthread, const pthread_attr_t *attr, void *(*threadroutine)(void *arg), void *arg)
```

相关声明：[pthread_create](#adcf534f63e3c1e209befc503d5a3db74)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_a37075410fbbaad7ee93c95375fc86e0e"></a>

```c
int pthread_setcancelstate (int state, int *oldstate)
```

相关声明：[pthread_setcancelstate](#a37075410fbbaad7ee93c95375fc86e0e)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

<a id="r_aab579bcfcf0662a0c1e35fd82162e61d"></a>

```c
int pthread_setcanceltype (int type, int *oldtype)
```

相关声明：[pthread_setcanceltype](#aab579bcfcf0662a0c1e35fd82162e61d)。

<a id="r_af1c95282ab2bea25f0888a19652cd41f"></a>

```c
void pthread_testcancel (void)
```

相关声明：[pthread_testcancel](#af1c95282ab2bea25f0888a19652cd41f)。

<a id="r_a18b9aa91fe20481a25650df20c567ff5"></a>

```c
int pthread_attr_setschedparam (pthread_attr_t *attr, const struct sched_param *schedparam)
```

相关声明：[pthread_attr_setschedparam](#a18b9aa91fe20481a25650df20c567ff5)、[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_ad8e89d31b56c88d632ba9aeb956fa043"></a>

```c
int pthread_setschedparam (pthread_t pthread, int policy, const struct sched_param *param)
```

相关声明：[pthread_setschedparam](#ad8e89d31b56c88d632ba9aeb956fa043)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)。

<a id="r_a7a23cbcfc21a4e3edf531ed65f022370"></a>

```c
int pthread_setschedprio (pthread_t thread, int prio)
```

相关声明：[pthread_setschedprio](#a7a23cbcfc21a4e3edf531ed65f022370)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)。

<a id="r_a79839f0f4f4a768bf6d218faf377c209"></a>

```c
int pthread_rwlock_destroy (pthread_rwlock_t *rwlock)
```

相关声明：[pthread_rwlock_destroy](#a79839f0f4f4a768bf6d218faf377c209)、[pthread_rwlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#acd12f65541fede33b6226f646e900ea6)。

<a id="r_a1596a13569ec35ee66cc867586fd643d"></a>

```c
int pthread_rwlock_init (pthread_rwlock_t *rwlock, const pthread_rwlockattr_t *attr)
```

相关声明：[pthread_rwlock_init](#a1596a13569ec35ee66cc867586fd643d)、[pthread_rwlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#acd12f65541fede33b6226f646e900ea6)、[pthread_rwlockattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a4e92e3fbb4be682babbb6796af90b50f)。

<a id="r_acc16fb32464b480d31bc69cce4e206c9"></a>

```c
int pthread_rwlock_rdlock (pthread_rwlock_t *rwlock)
```

相关声明：[pthread_rwlock_rdlock](#acc16fb32464b480d31bc69cce4e206c9)、[pthread_rwlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#acd12f65541fede33b6226f646e900ea6)。

<a id="r_ad791558625e69852e4a435b7c1580468"></a>

```c
int pthread_rwlock_timedrdlock (pthread_rwlock_t *rwlock, const struct timespec *abstime)
```

相关声明：[pthread_rwlock_timedrdlock](#ad791558625e69852e4a435b7c1580468)、[pthread_rwlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#acd12f65541fede33b6226f646e900ea6)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_a16c935f2f6146a95f9adbca71e0455e7"></a>

```c
int pthread_rwlock_timedwrlock (pthread_rwlock_t *rwlock, const struct timespec *abstime)
```

相关声明：[pthread_rwlock_timedwrlock](#a16c935f2f6146a95f9adbca71e0455e7)、[pthread_rwlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#acd12f65541fede33b6226f646e900ea6)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_aae52fb1d3e6d03b18fa5731d0b49d197"></a>

```c
int pthread_rwlock_tryrdlock (pthread_rwlock_t *rwlock)
```

相关声明：[pthread_rwlock_tryrdlock](#aae52fb1d3e6d03b18fa5731d0b49d197)、[pthread_rwlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#acd12f65541fede33b6226f646e900ea6)。

<a id="r_a065b618f7b786ed9bc7dddef4490cefb"></a>

```c
int pthread_rwlock_trywrlock (pthread_rwlock_t *rwlock)
```

相关声明：[pthread_rwlock_trywrlock](#a065b618f7b786ed9bc7dddef4490cefb)、[pthread_rwlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#acd12f65541fede33b6226f646e900ea6)。

<a id="r_a7d3b987d99117fc10c4ef97230011983"></a>

```c
int pthread_rwlock_unlock (pthread_rwlock_t *rwlock)
```

相关声明：[pthread_rwlock_unlock](#a7d3b987d99117fc10c4ef97230011983)、[pthread_rwlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#acd12f65541fede33b6226f646e900ea6)。

<a id="r_a5ddd4cc028257f9baa9e23c2337abe3b"></a>

```c
int pthread_rwlock_wrlock (pthread_rwlock_t *rwlock)
```

相关声明：[pthread_rwlock_wrlock](#a5ddd4cc028257f9baa9e23c2337abe3b)、[pthread_rwlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#acd12f65541fede33b6226f646e900ea6)。

<a id="r_a4a15369dee1898e5bb06c538c66aca7a"></a>

```c
int pthread_key_create (pthread_key_t *key, void(*destructor)(void *value))
```

相关声明：[pthread_key_create](#a4a15369dee1898e5bb06c538c66aca7a)、[pthread_key_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a8fd226393057ab7a8b17ac1c8b061911)。

<a id="r_aee96306dc79294927ee840bb4de2244b"></a>

```c
int pthread_key_delete (pthread_key_t key)
```

相关声明：[pthread_key_delete](#aee96306dc79294927ee840bb4de2244b)、[pthread_key_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a8fd226393057ab7a8b17ac1c8b061911)。

<a id="r_a2187333dd46ce08d9d2e044f79fad705"></a>

```c
int pthread_setspecific (pthread_key_t key, const void *value)
```

相关声明：[pthread_setspecific](#a2187333dd46ce08d9d2e044f79fad705)、[pthread_key_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a8fd226393057ab7a8b17ac1c8b061911)。

<a id="r_acdf9f73a16ea40eba1bc174d38e76ca5"></a>

```c
void * pthread_getspecific (pthread_key_t key)
```

相关声明：[pthread_getspecific](#acdf9f73a16ea40eba1bc174d38e76ca5)、[pthread_key_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a8fd226393057ab7a8b17ac1c8b061911)。

<a id="r_a80008474c3d68e9880da960a53d2f430"></a>

```c
int pthread_atfork (void(*prepare)(void), void(*parent)(void), void(*child)(void))
```

相关声明：[pthread_atfork](#a80008474c3d68e9880da960a53d2f430)。

<a id="r_afb4344ea91774ba279ea5df3cb656ebc"></a>

```c
int pthread_getconcurrency (void)
```

相关声明：[pthread_getconcurrency](#afb4344ea91774ba279ea5df3cb656ebc)。

<a id="r_a46064892e8c4622e0a3ebe22d9792b92"></a>

```c
int pthread_setconcurrency (int new_level)
```

相关声明：[pthread_setconcurrency](#a46064892e8c4622e0a3ebe22d9792b92)。

<a id="r_aa21465e084e7185bfbb94bb50d60cd08"></a>

```c
int pthread_setname_np (pthread_t thread, const char *name)
```

相关声明：[pthread_setname_np](#aa21465e084e7185bfbb94bb50d60cd08)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)。

设置 POSIX 线程名称（Thread Name）。

<a id="r_a8d55a60492c979991dc1a361b5453813"></a>

```c
int pthread_getname_np (pthread_t thread, char *name, size_t len)
```

相关声明：[pthread_getname_np](#a8d55a60492c979991dc1a361b5453813)、[pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)。

获取 POSIX 线程名称，并将其存入大小为 `len` 的 `name` 缓冲区。

## 11.3\_详细说明（Detailed Documentation）

<a id="a822c63bc662ad86cfb2dcec50edbb42b"></a>

### `PTHREAD_BARRIER_SERIAL_THREAD`

```c
#define PTHREAD_BARRIER_SERIAL_THREAD 1
```

<a id="aae774738da39ed214c9b01f342222686"></a>

### `PTHREAD_CANCEL_ASYNCHRONOUS`

```c
#define PTHREAD_CANCEL_ASYNCHRONOUS 1
```

<a id="a7559901d88e4d3b8100b407e164cd75e"></a>

### `PTHREAD_CANCEL_DEFERRED`

```c
#define PTHREAD_CANCEL_DEFERRED 0
```

<a id="a6c661332f782dcebc87b878990424b4c"></a>

### `PTHREAD_CANCEL_DISABLE`

```c
#define PTHREAD_CANCEL_DISABLE 1
```

<a id="aaf18882a8a6b82c7b7849a645f4445ef"></a>

### `PTHREAD_CANCEL_ENABLE`

```c
#define PTHREAD_CANCEL_ENABLE 0
```

<a id="a17ddda04a6c1ee32116c49c85e2ac4ae"></a>

### `PTHREAD_CANCELED`

```c
#define PTHREAD_CANCELED ((void *)-1)
```

<a id="a234ffab9eecdb6ae28198aeeedb4f10c"></a>

### `pthread_cleanup_pop`

```c
#define pthread_cleanup_pop ( _ex)
```

展开值（Value）：

```c
        __z_pthread_cleanup_pop(_ex);                                                      \
} /* enforce '}'-like behaviour */ while (0)
```

<a id="a265bda35a73d502fe8b710dc34f421cc"></a>

### `pthread_cleanup_push`

```c
#define pthread_cleanup_push ( _rtn, _arg )
```

展开值（Value）：

```c
do /* enforce '{'-like behaviour */ {                                                      \
        void *_z_pthread_cleanup[3];                                                       \
        __z_pthread_cleanup_push(_z_pthread_cleanup, _rtn, _arg)
```

<a id="aa7b867fe46f3660283fcb356c4fcbbf0"></a>

### `PTHREAD_COND_INITIALIZER`

```c
#define PTHREAD_COND_INITIALIZER (-1)
```

将条件变量（Condition Variable）声明为已初始化。

使用默认条件变量属性（Condition Variable Attributes）初始化条件变量。

<a id="a391c5eb0f6b5febc48710d0be3f62394"></a>

### `PTHREAD_CREATE_DETACHED`

```c
#define PTHREAD_CREATE_DETACHED 1
```

<a id="afb10d234d831c7b57768d62786748bc7"></a>

### `PTHREAD_CREATE_JOINABLE`

```c
#define PTHREAD_CREATE_JOINABLE 0
```

<a id="ad45abe03c8232518b6995e73172fe053"></a>

### `PTHREAD_EXPLICIT_SCHED`

```c
#define PTHREAD_EXPLICIT_SCHED 1
```

<a id="a470fccc57c4d7c3846e446a17cd23573"></a>

### `PTHREAD_INHERIT_SCHED`

```c
#define PTHREAD_INHERIT_SCHED 0
```

<a id="a2a9b96c0491ae490c17d0b400bc427b0"></a>

### `PTHREAD_MUTEX_DEFAULT`

```c
#define PTHREAD_MUTEX_DEFAULT PTHREAD_MUTEX_NORMAL
```

<a id="aaf502496651f95b06be861af7902cb23"></a>

### `PTHREAD_MUTEX_ERRORCHECK`

```c
#define PTHREAD_MUTEX_ERRORCHECK 2
```

<a id="a84e55100366a6a8338a2af3b3f279686"></a>

### `PTHREAD_MUTEX_INITIALIZER`

```c
#define PTHREAD_MUTEX_INITIALIZER (-1)
```

将互斥锁（Mutex）声明为已初始化。

使用默认互斥锁属性（Mutex Attributes）初始化互斥锁。

<a id="aae4b650085c2599674938f503d6253cf"></a>

### `PTHREAD_MUTEX_NORMAL`

```c
#define PTHREAD_MUTEX_NORMAL 0
```

<a id="a715e9644a7183d98cb2c9dd41cb89645"></a>

### `PTHREAD_MUTEX_RECURSIVE`

```c
#define PTHREAD_MUTEX_RECURSIVE 1
```

<a id="a59e22497b65fc305ddb5cea8b4990b51"></a>

### `PTHREAD_ONCE_INIT`

```c
#define PTHREAD_ONCE_INIT {0}
```

<a id="a0087e0ca82fd36e6c15f4c8ad443dbfc"></a>

### `PTHREAD_PRIO_INHERIT`

```c
#define PTHREAD_PRIO_INHERIT 1
```

<a id="a8c1426a72025b27d9726580ac0e8404f"></a>

### `PTHREAD_PRIO_NONE`

```c
#define PTHREAD_PRIO_NONE 0
```

<a id="a65da4c842cd4287f43d2f69ad5a5470b"></a>

### `PTHREAD_PRIO_PROTECT`

```c
#define PTHREAD_PRIO_PROTECT 2
```

<a id="a7c56b94733c97109259266d9c1f60338"></a>

### `PTHREAD_PROCESS_PRIVATE [1/2]`

```c
#define PTHREAD_PROCESS_PRIVATE 0
```

<a id="a443f2f512de9324bf77625041ecb04f4"></a>

### `PTHREAD_PROCESS_PRIVATE [2/2]`

```c
#define PTHREAD_PROCESS_PRIVATE 0
```

<a id="afff2f9c2b019a07298f341cf70ee829d"></a>

### `PTHREAD_PROCESS_PUBLIC`

```c
#define PTHREAD_PROCESS_PUBLIC 1
```

<a id="a07f3670a510cdb93233e84e1a0b50e89"></a>

### `PTHREAD_PROCESS_SHARED`

```c
#define PTHREAD_PROCESS_SHARED 1
```

<a id="aa92fd7b492a8a5b31b2f8b3b6039c622"></a>

### `PTHREAD_RWLOCK_INITIALIZER`

```c
#define PTHREAD_RWLOCK_INITIALIZER (-1)
```

将读写锁（Read-write Lock）声明为已初始化。

使用默认读写锁属性（Read-write Lock Attributes）初始化读写锁。

<a id="aeab18be4f4ee13db4b0b65c6768fb539"></a>

### `PTHREAD_SCOPE_PROCESS`

```c
#define PTHREAD_SCOPE_PROCESS 1
```

<a id="ab754f4339f76c46b8f57413c03e8ec65"></a>

### `PTHREAD_SCOPE_SYSTEM`

```c
#define PTHREAD_SCOPE_SYSTEM 0
```

<a id="a8b3dc1c5c1a165d6143b1dce950e8266"></a>

### `PTHREAD_STACK_MIN`

```c
#define PTHREAD_STACK_MIN K_KERNEL_STACK_LEN(0)
```

<a id="a80008474c3d68e9880da960a53d2f430"></a>

### `pthread_atfork()`

```c
int pthread_atfork ( void(* prepare )(void), void(* parent )(void), void(* child )(void) )
```

<a id="a4bcdbf47c17c7dcc51e9f05f5cb56d81"></a>

### `pthread_attr_destroy()`

```c
int pthread_attr_destroy ( pthread_attr_t * attr)
```

<a id="a391c34da42e68ddd24f5ee0c070d5c4f"></a>

### `pthread_attr_getdetachstate()`

```c
int pthread_attr_getdetachstate ( const pthread_attr_t * attr, int * detachstate )
```

<a id="abee3ae43d1f00b597111f6f82b0416a1"></a>

### `pthread_attr_getguardsize()`

```c
int pthread_attr_getguardsize ( const pthread_attr_t *ZRESTRICT attr, size_t *ZRESTRICT guardsize )
```

<a id="a79a77b688c30213e5e52e6be178cde4e"></a>

### `pthread_attr_getinheritsched()`

```c
int pthread_attr_getinheritsched ( const pthread_attr_t * attr, int * inheritsched )
```

<a id="abcd67baa86ff65d7ce65985d8b50d579"></a>

### `pthread_attr_getschedparam()`

```c
int pthread_attr_getschedparam ( const pthread_attr_t * attr, struct sched_param * schedparam )
```

<a id="af032906f326f3c209c7eed6bb248ebee"></a>

### `pthread_attr_getschedpolicy()`

```c
int pthread_attr_getschedpolicy ( const pthread_attr_t * attr, int * policy )
```

<a id="ad3fe01698c4fad85bb5cc3f9a2e82ea3"></a>

### `pthread_attr_getscope()`

```c
int pthread_attr_getscope ( const pthread_attr_t * attr, int * contentionscope )
```

<a id="aec19ad460995a9fe8aeb4eaf2bb1ed1d"></a>

### `pthread_attr_getstack()`

```c
int pthread_attr_getstack ( const pthread_attr_t * attr, void ** stackaddr, size_t * stacksize )
```

<a id="ae23600d4670359ab12bfba20db2c9a37"></a>

### `pthread_attr_getstacksize()`

```c
int pthread_attr_getstacksize ( const pthread_attr_t * attr, size_t * stacksize )
```

<a id="a0b85ebb1e3aac081a4c0a5e85ae3cbe9"></a>

### `pthread_attr_init()`

```c
int pthread_attr_init ( pthread_attr_t * attr)
```

<a id="ae6ee78c307d8467b34a9b0c330993a54"></a>

### `pthread_attr_setdetachstate()`

```c
int pthread_attr_setdetachstate ( pthread_attr_t * attr, int detachstate )
```

<a id="a532b31c11a9d87663053c5342400758c"></a>

### `pthread_attr_setguardsize()`

```c
int pthread_attr_setguardsize ( pthread_attr_t * attr, size_t guardsize )
```

<a id="ad437fe8caa3ef9f0cb7d69f6f6479df9"></a>

### `pthread_attr_setinheritsched()`

```c
int pthread_attr_setinheritsched ( pthread_attr_t * attr, int inheritsched )
```

<a id="a18b9aa91fe20481a25650df20c567ff5"></a>

### `pthread_attr_setschedparam()`

```c
int pthread_attr_setschedparam ( pthread_attr_t * attr, const struct sched_param * schedparam )
```

<a id="a79b4c9e71486a87ef3014f1c660b33eb"></a>

### `pthread_attr_setschedpolicy()`

```c
int pthread_attr_setschedpolicy ( pthread_attr_t * attr, int policy )
```

<a id="a6d8d320a882ba044a064975dddcf9ced"></a>

### `pthread_attr_setscope()`

```c
int pthread_attr_setscope ( pthread_attr_t * attr, int contentionscope )
```

<a id="a94ede89b99a3a4fa17e516d30aaf3409"></a>

### `pthread_attr_setstack()`

```c
int pthread_attr_setstack ( pthread_attr_t * attr, void * stackaddr, size_t stacksize )
```

<a id="a812a9a455ae2ef2bb0dca4fff201a281"></a>

### `pthread_attr_setstacksize()`

```c
int pthread_attr_setstacksize ( pthread_attr_t * attr, size_t stacksize )
```

<a id="ab05ae13769e61dea9c53ca7894743c8f"></a>

### `pthread_barrier_destroy()`

```c
int pthread_barrier_destroy ( pthread_barrier_t * b)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="aecc6c99901aac517072970e153863296"></a>

### `pthread_barrier_init()`

```c
int pthread_barrier_init ( pthread_barrier_t * b, const pthread_barrierattr_t * attr, unsigned int count )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="af786372165ba080986ae4143928c5436"></a>

### `pthread_barrier_wait()`

```c
int pthread_barrier_wait ( pthread_barrier_t * b)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a5e27d4773f3d0552e36f2ff3b922a988"></a>

### `pthread_barrierattr_destroy()`

```c
int pthread_barrierattr_destroy ( pthread_barrierattr_t * b)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a54e367403c0524680115b780ccfbc586"></a>

### `pthread_barrierattr_getpshared()`

```c
int pthread_barrierattr_getpshared ( const pthread_barrierattr_t *ZRESTRICT attr, int *ZRESTRICT pshared )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="ad540451ab679ace869b51c7cbb7b8486"></a>

### `pthread_barrierattr_init()`

```c
int pthread_barrierattr_init ( pthread_barrierattr_t * b)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="aa9c3c335f5bcf702fe85a1c12dcdc70e"></a>

### `pthread_barrierattr_setpshared()`

```c
int pthread_barrierattr_setpshared ( pthread_barrierattr_t * attr, int pshared )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a66a8f4bac5afe05538794218ff7c85ea"></a>

### `pthread_cancel()`

```c
int pthread_cancel ( pthread_t pthread)
```

<a id="a91ff7fff67462ce9216d299c89683119"></a>

### `pthread_cond_broadcast()`

```c
int pthread_cond_broadcast ( pthread_cond_t * cv)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a8d44e4eae235f675bbab1b9163a3bc1d"></a>

### `pthread_cond_destroy()`

```c
int pthread_cond_destroy ( pthread_cond_t * cv)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a319a61cdb25d069c9d4504e8225fd0c3"></a>

### `pthread_cond_init()`

```c
int pthread_cond_init ( pthread_cond_t * cv, const pthread_condattr_t * att )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="add1fea97e50755b5dbf4bd9a83b710dd"></a>

### `pthread_cond_signal()`

```c
int pthread_cond_signal ( pthread_cond_t * cv)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="aecea498fbd2df02942790e5ccd7d78b2"></a>

### `pthread_cond_timedwait()`

```c
int pthread_cond_timedwait ( pthread_cond_t * cv, pthread_mutex_t * mut, const struct timespec * abstime )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a61a1bf88d32de361e82ef4ea99b47322"></a>

### `pthread_cond_wait()`

```c
int pthread_cond_wait ( pthread_cond_t * cv, pthread_mutex_t * mut )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="af37eaf73f0d83989d8efc06e676909f1"></a>

### `pthread_condattr_destroy()`

```c
int pthread_condattr_destroy ( pthread_condattr_t * att)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a77376b018eec6db2986939b847915a3c"></a>

### `pthread_condattr_getclock()`

```c
int pthread_condattr_getclock ( const pthread_condattr_t *ZRESTRICT att, clockid_t *ZRESTRICT clock_id )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a01159da320b2317ee286a7e92d713f16"></a>

### `pthread_condattr_init()`

```c
int pthread_condattr_init ( pthread_condattr_t * att)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="ac0b4f6d49deeab0ddb269a23ee303156"></a>

### `pthread_condattr_setclock()`

```c
int pthread_condattr_setclock ( pthread_condattr_t * att, clockid_t clock_id )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="adcf534f63e3c1e209befc503d5a3db74"></a>

### `pthread_create()`

```c
int pthread_create ( pthread_t * newthread, const pthread_attr_t * attr, void *(* threadroutine )(void *arg), void * arg )
```

<a id="a7c275c509c26566b6dd95a2de1668a2f"></a>

### `pthread_detach()`

```c
int pthread_detach ( pthread_t thread)
```

<a id="a2a460fe3d4e4518057366f6ead455f4a"></a>

### `pthread_equal()`

```c
int pthread_equal ( pthread_t pt1, pthread_t pt2 )
```

比较线程 ID（Thread IDs）。

参见 IEEE 1003.1。

<a id="ab9a027122b38833e8c2e1c0e733da3e6"></a>

### `pthread_exit()`

```c
FUNC_NORETURN void pthread_exit ( void * retval)
```

<a id="afb4344ea91774ba279ea5df3cb656ebc"></a>

### `pthread_getconcurrency()`

```c
int pthread_getconcurrency ( void )
```

<a id="a8d55a60492c979991dc1a361b5453813"></a>

### `pthread_getname_np()`

```c
int pthread_getname_np ( pthread_t thread, char * name, size_t len )
```

获取 POSIX 线程名称，并将其存入大小为 `len` 的 `name` 缓冲区。

不可移植的扩展函数（Non-portable Extension Function），与此函数在大多数其他实现中的定义一致。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `thread` | 要获取名称信息的 POSIX 线程（Thread）。 |
| `name` | 目标缓冲区。 |
| `len` | 目标缓冲区大小。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `ESRCH` | 线程不存在（Thread Does Not Exist）。 |
| `EINVAL` | 名称缓冲区（Name Buffer）为 `NULL`。 |
| `<0` | 内核函数出错时返回负值。 |

<a id="ac60393667965dbd06670d3d280b65757"></a>

### `pthread_getschedparam()`

```c
int pthread_getschedparam ( pthread_t pthread, int * policy, struct sched_param * param )
```

<a id="acdf9f73a16ea40eba1bc174d38e76ca5"></a>

### `pthread_getspecific()`

```c
void * pthread_getspecific ( pthread_key_t key)
```

<a id="a6e4d503c2b358be5c98330f9006b3417"></a>

### `pthread_join()`

```c
int pthread_join ( pthread_t thread, void ** status )
```

<a id="a4a15369dee1898e5bb06c538c66aca7a"></a>

### `pthread_key_create()`

```c
int pthread_key_create ( pthread_key_t * key, void(* destructor )(void *value) )
```

<a id="aee96306dc79294927ee840bb4de2244b"></a>

### `pthread_key_delete()`

```c
int pthread_key_delete ( pthread_key_t key)
```

<a id="af89d9cfa300f33b46720a96eac83d175"></a>

### `pthread_mutex_destroy()`

```c
int pthread_mutex_destroy ( pthread_mutex_t * m)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a7948bc0ea8a33439aece34d0fb3daf8b"></a>

### `pthread_mutex_init()`

```c
int pthread_mutex_init ( pthread_mutex_t * m, const pthread_mutexattr_t * att )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="afd70d6f2c50e22b996c926fb9d6ad291"></a>

### `pthread_mutex_lock()`

```c
int pthread_mutex_lock ( pthread_mutex_t * m)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="abbec44a62531009629601fbb34f1027c"></a>

### `pthread_mutex_timedlock()`

```c
int pthread_mutex_timedlock ( pthread_mutex_t * m, const struct timespec * abstime )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="acc1ccbaf3d76572da85a8030bba1ede4"></a>

### `pthread_mutex_trylock()`

```c
int pthread_mutex_trylock ( pthread_mutex_t * m)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a02a3c64dac70730e226c31c0e7dbb45c"></a>

### `pthread_mutex_unlock()`

```c
int pthread_mutex_unlock ( pthread_mutex_t * m)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a2321aabf58224b06021185708d0f9658"></a>

### `pthread_mutexattr_destroy()`

```c
int pthread_mutexattr_destroy ( pthread_mutexattr_t * attr)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

注意：Zephyr 中的 pthread 属性结构体（Attribute Structs）目前不产生实际效果，即 no-op。

<a id="a200fcbc9157e6183376f83bc0e5937dd"></a>

### `pthread_mutexattr_getprotocol()`

```c
int pthread_mutexattr_getprotocol ( const pthread_mutexattr_t * attr, int * protocol )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a7f064a4db96a009a5a9a7c7e5cc03599"></a>

### `pthread_mutexattr_gettype()`

```c
int pthread_mutexattr_gettype ( const pthread_mutexattr_t * attr, int * type )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="af98f6b6c483077a39d1400b1de1577b8"></a>

### `pthread_mutexattr_init()`

```c
int pthread_mutexattr_init ( pthread_mutexattr_t * attr)
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

注意：Zephyr 中的 pthread 属性结构体（Attribute Structs）目前不产生实际效果，即 no-op。

<a id="ae7e6584c2b2cf9b9ff061115d2342bb5"></a>

### `pthread_mutexattr_setprotocol()`

```c
int pthread_mutexattr_setprotocol ( pthread_mutexattr_t * attr, int protocol )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a8387c80e660e9426f801ac0217ecfae5"></a>

### `pthread_mutexattr_settype()`

```c
int pthread_mutexattr_settype ( pthread_mutexattr_t * attr, int type )
```

可移植操作系统接口（POSIX）线程兼容 API。

参见 IEEE 1003.1。

<a id="a79839f0f4f4a768bf6d218faf377c209"></a>

### `pthread_rwlock_destroy()`

```c
int pthread_rwlock_destroy ( pthread_rwlock_t * rwlock)
```

<a id="a1596a13569ec35ee66cc867586fd643d"></a>

### `pthread_rwlock_init()`

```c
int pthread_rwlock_init ( pthread_rwlock_t * rwlock, const pthread_rwlockattr_t * attr )
```

<a id="acc16fb32464b480d31bc69cce4e206c9"></a>

### `pthread_rwlock_rdlock()`

```c
int pthread_rwlock_rdlock ( pthread_rwlock_t * rwlock)
```

<a id="ad791558625e69852e4a435b7c1580468"></a>

### `pthread_rwlock_timedrdlock()`

```c
int pthread_rwlock_timedrdlock ( pthread_rwlock_t * rwlock, const struct timespec * abstime )
```

<a id="a16c935f2f6146a95f9adbca71e0455e7"></a>

### `pthread_rwlock_timedwrlock()`

```c
int pthread_rwlock_timedwrlock ( pthread_rwlock_t * rwlock, const struct timespec * abstime )
```

<a id="aae52fb1d3e6d03b18fa5731d0b49d197"></a>

### `pthread_rwlock_tryrdlock()`

```c
int pthread_rwlock_tryrdlock ( pthread_rwlock_t * rwlock)
```

<a id="a065b618f7b786ed9bc7dddef4490cefb"></a>

### `pthread_rwlock_trywrlock()`

```c
int pthread_rwlock_trywrlock ( pthread_rwlock_t * rwlock)
```

<a id="a7d3b987d99117fc10c4ef97230011983"></a>

### `pthread_rwlock_unlock()`

```c
int pthread_rwlock_unlock ( pthread_rwlock_t * rwlock)
```

<a id="a5ddd4cc028257f9baa9e23c2337abe3b"></a>

### `pthread_rwlock_wrlock()`

```c
int pthread_rwlock_wrlock ( pthread_rwlock_t * rwlock)
```

<a id="a78a54e67f0afe2601dbda0a904fa0bdf"></a>

### `pthread_rwlockattr_destroy()`

```c
int pthread_rwlockattr_destroy ( pthread_rwlockattr_t * attr)
```

销毁读写锁属性对象（Read-write Lock Attributes Object）。

参见 IEEE 1003.1。

<a id="a5ca1dea9ea7d3cfb34a9c8561e47cf02"></a>

### `pthread_rwlockattr_getpshared()`

```c
int pthread_rwlockattr_getpshared ( const pthread_rwlockattr_t *ZRESTRICT attr, int *ZRESTRICT pshared )
```

<a id="a9d831af0179ed16d1b6cbeba0304810b"></a>

### `pthread_rwlockattr_init()`

```c
int pthread_rwlockattr_init ( pthread_rwlockattr_t * attr)
```

初始化读写锁属性对象（Read-write Lock Attributes Object）。

参见 IEEE 1003.1。

<a id="ae6550aa6aede71f618bb7457f3e50524"></a>

### `pthread_rwlockattr_setpshared()`

```c
int pthread_rwlockattr_setpshared ( pthread_rwlockattr_t * attr, int pshared )
```

<a id="a4c4f5f3b4f8f45d9d897847d53b11aaa"></a>

### `pthread_self()`

```c
pthread_t pthread_self ( void )
```

获取调用线程的 ID（Thread ID）。

从不是通过 `pthread_create()` 创建的线程调用此 API，结果未定义（Undefined）。

参见 IEEE 1003.1。

<a id="a37075410fbbaad7ee93c95375fc86e0e"></a>

### `pthread_setcancelstate()`

```c
int pthread_setcancelstate ( int state, int * oldstate )
```

<a id="aab579bcfcf0662a0c1e35fd82162e61d"></a>

### `pthread_setcanceltype()`

```c
int pthread_setcanceltype ( int type, int * oldtype )
```

<a id="a46064892e8c4622e0a3ebe22d9792b92"></a>

### `pthread_setconcurrency()`

```c
int pthread_setconcurrency ( int new_level)
```

<a id="aa21465e084e7185bfbb94bb50d60cd08"></a>

### `pthread_setname_np()`

```c
int pthread_setname_np ( pthread_t thread, const char * name )
```

设置 POSIX 线程名称（Thread Name）。

不可移植的扩展函数（Non-portable Extension Function），与此函数在大多数其他实现中的定义一致。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `thread` | 要设置名称的 POSIX 线程（Thread）。 |
| `name` | 名称字符串。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `ESRCH` | 线程不存在（Thread Does Not Exist）。 |
| `EINVAL` | 名称缓冲区（Name Buffer）为 `NULL`。 |
| `<0` | 内核函数出错时返回负值。 |

<a id="ad8e89d31b56c88d632ba9aeb956fa043"></a>

### `pthread_setschedparam()`

```c
int pthread_setschedparam ( pthread_t pthread, int policy, const struct sched_param * param )
```

<a id="a7a23cbcfc21a4e3edf531ed65f022370"></a>

### `pthread_setschedprio()`

```c
int pthread_setschedprio ( pthread_t thread, int prio )
```

<a id="a2187333dd46ce08d9d2e044f79fad705"></a>

### `pthread_setspecific()`

```c
int pthread_setspecific ( pthread_key_t key, const void * value )
```

<a id="af1c95282ab2bea25f0888a19652cd41f"></a>

### `pthread_testcancel()`

```c
void pthread_testcancel ( void )
```

<a id="a742eefdf61f97bf1607d15a4fa2a3173"></a>

### `pthread_timedjoin_np()`

```c
int pthread_timedjoin_np ( pthread_t thread, void ** status, const struct timespec * abstime )
```

<a id="a32dd5d2994c5ca7dd33294ce8cbd13bf"></a>

### `pthread_tryjoin_np()`

```c
int pthread_tryjoin_np ( pthread_t thread, void ** status )
```


## 11.4\_原页交叉引用（Cross References）

- [stdlib.h](../api_source_configuration_reference/P107_stdlib.h_源码浏览.md)
- [string.h](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/posix/unistd.h](../api_source_configuration_reference/P116_unistd.h_源码浏览.md)
- [zephyr/posix/sched.h](../api_source_runtime_reference/P050_sched.h_源码浏览.md)
- [查看此文件的源码。](../api_source_interrupt_modem_reference/P009_pthread.h_源码浏览.md)
- [K_KERNEL_STACK_LEN](../thread_stack_reference/P002_线程栈头文件参考.md#a12f78cb2d5b9bf83068e810bf1e31937)
- [pthread_cond_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a1b893f49dfdf497be09c04a0e40f425e)
- [pthread_condattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a9f62774a7a4e1634e60fb611765251f1)
- [pthread_mutex_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a465eb2b962de164efdc8ce957025de7e)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [clockid_t](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a6bb3206700910111f26e946bfbf0f2af)
- [pthread_mutexattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a2489174ff5737a33443b0959f4278765)
- [pthread_barrier_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#aeb637552f63e4c249e7aaeb2905f3db2)
- [pthread_barrierattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a24d58850626c8022bf4bbd5d2628615b)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)
- [pthread_rwlockattr_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a4e92e3fbb4be682babbb6796af90b50f)
- [pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [pthread_rwlock_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#acd12f65541fede33b6226f646e900ea6)
- [pthread_key_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a8fd226393057ab7a8b17ac1c8b061911)
- [ESRCH](../error_reference/P003_系统错误号公共接口.md#ga462e47a8af6288232a5df548221ada4c)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_zephyr__net__net_pkt_filter.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__drivers__i2c__target__regset_target_lib.h_文件参考.md)
