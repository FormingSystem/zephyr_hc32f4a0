---
id: learning.zephyr-docs.api-file-reference.page-312
title: zephyr__posix__posix_types.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第312章\_zephyr\_\_posix\_\_posix\_types.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <sys/types.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 312.1\_数据结构（Data Structures）

<a id="r_pthread_5Fattr_5Ft"></a>

```c
struct pthread_attr_t
```

相关声明：[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_pthread_5Fmutexattr"></a>

```c
struct pthread_mutexattr
```

相关声明：[pthread_mutexattr](../posix_system_model_reference/P014_pthread_mutexattr_结构体.md)。

<a id="r_pthread_5Fcondattr"></a>

```c
struct pthread_condattr
```

相关声明：[pthread_condattr](../posix_system_model_reference/P013_pthread_condattr_结构体.md)。

<a id="r_pthread_5Fbarrierattr"></a>

```c
struct pthread_barrierattr
```

相关声明：[pthread_barrierattr](../posix_system_model_reference/P012_pthread_barrierattr_结构体.md)。

<a id="r_pthread_5Fonce"></a>

```c
struct pthread_once
```

相关声明：[pthread_once](../posix_system_model_reference/P015_pthread_once_结构体.md)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 312.2\_类型定义（Typedefs）

<a id="r_a3b55f88f25d2c571de53a365ad658426"></a>

```c
typedef unsigned long clock_t
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[clock_t](#a3b55f88f25d2c571de53a365ad658426)。

<a id="r_a0f89a9a6420c24efc5254e10170009e9"></a>

```c
typedef int dev_t
```

相关声明：[dev_t](#a0f89a9a6420c24efc5254e10170009e9)。

<a id="r_a779f87527fcb00a46d12056b753cf22c"></a>

```c
typedef int ino_t
```

相关声明：[ino_t](#a779f87527fcb00a46d12056b753cf22c)。

<a id="r_a952c84a825bb4f319cf55c9afb99ee0e"></a>

```c
typedef unsigned short nlink_t
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[nlink_t](#a952c84a825bb4f319cf55c9afb99ee0e)。

<a id="r_a75bb141dc55bc89a8ddc565fd374e3d9"></a>

```c
typedef unsigned short uid_t
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uid_t](#a75bb141dc55bc89a8ddc565fd374e3d9)。

<a id="r_a3a7834be1a79bb0c5a65d3546c2e3bd8"></a>

```c
typedef unsigned short gid_t
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[gid_t](#a3a7834be1a79bb0c5a65d3546c2e3bd8)。

<a id="r_a50c0d048e63387089a42aaf054a6d05b"></a>

```c
typedef unsigned long blksize_t
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[blksize_t](#a50c0d048e63387089a42aaf054a6d05b)。

<a id="r_aa9a628992e7bcdc59d4fb606baada347"></a>

```c
typedef unsigned long blkcnt_t
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[blkcnt_t](#aa9a628992e7bcdc59d4fb606baada347)。

<a id="r_a1cf3c794977f92f3ccf2e041a68f3342"></a>

```c
typedef unsigned long useconds_t
```

相关声明：[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[useconds_t](#a1cf3c794977f92f3ccf2e041a68f3342)。

<a id="r_a405938c67e9c568fde9993c7e14d58ec"></a>

```c
typedef uint32_t pthread_t
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pthread_t](#a405938c67e9c568fde9993c7e14d58ec)。

<a id="r_a1d9c308dd59bf38ff0a7a45020d0aefa"></a>

```c
typedef uint32_t pthread_spinlock_t
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pthread_spinlock_t](#a1d9c308dd59bf38ff0a7a45020d0aefa)。

<a id="r_afb4edc6a51d66a7a352424942b631a1e"></a>

```c
typedef struct k_sem sem_t
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[sem_t](#afb4edc6a51d66a7a352424942b631a1e)。

<a id="r_a465eb2b962de164efdc8ce957025de7e"></a>

```c
typedef uint32_t pthread_mutex_t
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pthread_mutex_t](#a465eb2b962de164efdc8ce957025de7e)。

<a id="r_a2489174ff5737a33443b0959f4278765"></a>

```c
typedef struct pthread_mutexattr pthread_mutexattr_t
```

相关声明：[pthread_mutexattr](../posix_system_model_reference/P014_pthread_mutexattr_结构体.md)、[pthread_mutexattr_t](#a2489174ff5737a33443b0959f4278765)。

<a id="r_a1b893f49dfdf497be09c04a0e40f425e"></a>

```c
typedef uint32_t pthread_cond_t = sizeof(struct pthread_mutexattr))
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pthread_cond_t](#a1b893f49dfdf497be09c04a0e40f425e)、[pthread_mutexattr](../posix_system_model_reference/P014_pthread_mutexattr_结构体.md)。

<a id="r_a9f62774a7a4e1634e60fb611765251f1"></a>

```c
typedef struct pthread_condattr pthread_condattr_t
```

相关声明：[pthread_condattr](../posix_system_model_reference/P013_pthread_condattr_结构体.md)、[pthread_condattr_t](#a9f62774a7a4e1634e60fb611765251f1)。

<a id="r_aeb637552f63e4c249e7aaeb2905f3db2"></a>

```c
typedef uint32_t pthread_barrier_t = sizeof(struct pthread_condattr))
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pthread_barrier_t](#aeb637552f63e4c249e7aaeb2905f3db2)、[pthread_condattr](../posix_system_model_reference/P013_pthread_condattr_结构体.md)。

<a id="r_a24d58850626c8022bf4bbd5d2628615b"></a>

```c
typedef struct pthread_barrierattr pthread_barrierattr_t
```

相关声明：[pthread_barrierattr](../posix_system_model_reference/P012_pthread_barrierattr_结构体.md)、[pthread_barrierattr_t](#a24d58850626c8022bf4bbd5d2628615b)。

<a id="r_a4e92e3fbb4be682babbb6796af90b50f"></a>

```c
typedef uint32_t pthread_rwlockattr_t
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pthread_rwlockattr_t](#a4e92e3fbb4be682babbb6796af90b50f)。

<a id="r_acd12f65541fede33b6226f646e900ea6"></a>

```c
typedef uint32_t pthread_rwlock_t
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pthread_rwlock_t](#acd12f65541fede33b6226f646e900ea6)。

<a id="r_a8fd226393057ab7a8b17ac1c8b061911"></a>

```c
typedef uint32_t pthread_key_t
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pthread_key_t](#a8fd226393057ab7a8b17ac1c8b061911)。

<a id="r_a2603a6fda916554839174bc7d8849297"></a>

```c
typedef struct pthread_once pthread_once_t
```

相关声明：[pthread_once](../posix_system_model_reference/P015_pthread_once_结构体.md)、[pthread_once_t](#a2603a6fda916554839174bc7d8849297)。

## 312.3\_详细说明（Detailed Documentation）

<a id="aa9a628992e7bcdc59d4fb606baada347"></a>

### `blkcnt_t`

```c
typedef unsigned long blkcnt_t
```

<a id="a50c0d048e63387089a42aaf054a6d05b"></a>

### `blksize_t`

```c
typedef unsigned long blksize_t
```

<a id="a3b55f88f25d2c571de53a365ad658426"></a>

### `clock_t`

```c
typedef unsigned long clock_t
```

<a id="a0f89a9a6420c24efc5254e10170009e9"></a>

### `dev_t`

```c
typedef int dev_t
```

<a id="a3a7834be1a79bb0c5a65d3546c2e3bd8"></a>

### `gid_t`

```c
typedef unsigned short gid_t
```

<a id="a779f87527fcb00a46d12056b753cf22c"></a>

### `ino_t`

```c
typedef int ino_t
```

<a id="a952c84a825bb4f319cf55c9afb99ee0e"></a>

### `nlink_t`

```c
typedef unsigned short nlink_t
```

<a id="aeb637552f63e4c249e7aaeb2905f3db2"></a>

### `pthread_barrier_t`

```c
typedef uint32_t pthread_barrier_t = sizeof(struct pthread_condattr))
```

<a id="a24d58850626c8022bf4bbd5d2628615b"></a>

### `pthread_barrierattr_t`

```c
typedef struct pthread_barrierattr pthread_barrierattr_t
```

<a id="a1b893f49dfdf497be09c04a0e40f425e"></a>

### `pthread_cond_t`

```c
typedef uint32_t pthread_cond_t = sizeof(struct pthread_mutexattr))
```

<a id="a9f62774a7a4e1634e60fb611765251f1"></a>

### `pthread_condattr_t`

```c
typedef struct pthread_condattr pthread_condattr_t
```

<a id="a8fd226393057ab7a8b17ac1c8b061911"></a>

### `pthread_key_t`

```c
typedef uint32_t pthread_key_t
```

<a id="a465eb2b962de164efdc8ce957025de7e"></a>

### `pthread_mutex_t`

```c
typedef uint32_t pthread_mutex_t
```

<a id="a2489174ff5737a33443b0959f4278765"></a>

### `pthread_mutexattr_t`

```c
typedef struct pthread_mutexattr pthread_mutexattr_t
```

<a id="a2603a6fda916554839174bc7d8849297"></a>

### `pthread_once_t`

```c
typedef struct pthread_once pthread_once_t
```

<a id="acd12f65541fede33b6226f646e900ea6"></a>

### `pthread_rwlock_t`

```c
typedef uint32_t pthread_rwlock_t
```

<a id="a4e92e3fbb4be682babbb6796af90b50f"></a>

### `pthread_rwlockattr_t`

```c
typedef uint32_t pthread_rwlockattr_t
```

<a id="a1d9c308dd59bf38ff0a7a45020d0aefa"></a>

### `pthread_spinlock_t`

```c
typedef uint32_t pthread_spinlock_t
```

<a id="a405938c67e9c568fde9993c7e14d58ec"></a>

### `pthread_t`

```c
typedef uint32_t pthread_t
```

<a id="afb4edc6a51d66a7a352424942b631a1e"></a>

### `sem_t`

```c
typedef struct k_sem sem_t
```

<a id="a75bb141dc55bc89a8ddc565fd374e3d9"></a>

### `uid_t`

```c
typedef unsigned short uid_t
```

<a id="a1cf3c794977f92f3ccf2e041a68f3342"></a>

### `useconds_t`

```c
typedef unsigned long useconds_t
```


## 312.4\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h_source.html)
- [pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)
- [pthread_mutexattr](../posix_system_model_reference/P014_pthread_mutexattr_结构体.md)
- [pthread_condattr](../posix_system_model_reference/P013_pthread_condattr_结构体.md)
- [pthread_barrierattr](../posix_system_model_reference/P012_pthread_barrierattr_结构体.md)
- [pthread_once](../posix_system_model_reference/P015_pthread_once_结构体.md)
- [unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [pthread_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#ab3f45e72c67ecc7866d14ab09b3367e7)
- [uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P311_zephyr__posix__posix_time.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P313_zephyr__posix__pwd.h_文件参考.md)
