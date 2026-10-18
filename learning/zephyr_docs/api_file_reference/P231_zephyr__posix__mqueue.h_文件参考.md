---
id: learning.zephyr-docs.api-file-reference.page-231
title: zephyr__posix__mqueue.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第231章\_zephyr\_\_posix\_\_mqueue.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mqueue_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <time.h>
#include <signal.h>
#include <zephyr/kernel.h>
#include <zephyr/posix/fcntl.h>
#include <zephyr/posix/sys/stat.h>
#include <zephyr/posix/posix_types.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 231.1\_数据结构（Data Structures）

<a id="r_mq_5Fattr"></a>

```c
struct mq_attr
```

相关声明：[mq_attr](../posix_system_model_reference/P007_mq_attr_结构体.md)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 231.2\_类型定义（Typedefs）

<a id="r_aa03ac56b19aba70879b7e2934da6a507"></a>

```c
typedef void * mqd_t
```

相关声明：[mqd_t](#aa03ac56b19aba70879b7e2934da6a507)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 231.3\_函数（Functions）

<a id="r_a6e6c4881ac0fd3ad18d733b96d088b8b"></a>

```c
mqd_t mq_open (const char *name, int oflags,...)
```

相关声明：[mqd_t](#aa03ac56b19aba70879b7e2934da6a507)、[mq_open](#a6e6c4881ac0fd3ad18d733b96d088b8b)。

<a id="r_a3fbd3906296be63451c64d69be2bc371"></a>

```c
int mq_close (mqd_t mqdes)
```

相关声明：[mq_close](#a3fbd3906296be63451c64d69be2bc371)、[mqd_t](#aa03ac56b19aba70879b7e2934da6a507)。

<a id="r_accd8c5ee36e60d990963e1d544ef4140"></a>

```c
int mq_unlink (const char *name)
```

相关声明：[mq_unlink](#accd8c5ee36e60d990963e1d544ef4140)。

<a id="r_a5a55ce03d8466a53a36601aaca9ee328"></a>

```c
int mq_getattr (mqd_t mqdes, struct mq_attr *mqstat)
```

相关声明：[mq_getattr](#a5a55ce03d8466a53a36601aaca9ee328)、[mqd_t](#aa03ac56b19aba70879b7e2934da6a507)、[mq_attr](../posix_system_model_reference/P007_mq_attr_结构体.md)。

<a id="r_ae0ff0175064ab31858eff0669b7e745b"></a>

```c
int mq_receive (mqd_t mqdes, char *msg_ptr, size_t msg_len, unsigned int *msg_prio)
```

相关声明：[mq_receive](#ae0ff0175064ab31858eff0669b7e745b)、[mqd_t](#aa03ac56b19aba70879b7e2934da6a507)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_af13b6f0b3b15e14624b0c50050d062a4"></a>

```c
int mq_send (mqd_t mqdes, const char *msg_ptr, size_t msg_len, unsigned int msg_prio)
```

相关声明：[mq_send](#af13b6f0b3b15e14624b0c50050d062a4)、[mqd_t](#aa03ac56b19aba70879b7e2934da6a507)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

<a id="r_a83b7aa93cb6f1f5a4fd938baea5579a6"></a>

```c
int mq_setattr (mqd_t mqdes, const struct mq_attr *mqstat, struct mq_attr *omqstat)
```

相关声明：[mq_setattr](#a83b7aa93cb6f1f5a4fd938baea5579a6)、[mqd_t](#aa03ac56b19aba70879b7e2934da6a507)、[mq_attr](../posix_system_model_reference/P007_mq_attr_结构体.md)、[mq_attr](../posix_system_model_reference/P007_mq_attr_结构体.md)。

<a id="r_aaf2e88ac75eac32eb5a3672fd56759b7"></a>

```c
int mq_timedreceive (mqd_t mqdes, char *msg_ptr, size_t msg_len, unsigned int *msg_prio, const struct timespec *abstime)
```

相关声明：[mq_timedreceive](#aaf2e88ac75eac32eb5a3672fd56759b7)、[mqd_t](#aa03ac56b19aba70879b7e2934da6a507)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_ac19939c8157d7ef9033a5be97a7ca6a1"></a>

```c
int mq_timedsend (mqd_t mqdes, const char *msg_ptr, size_t msg_len, unsigned int msg_prio, const struct timespec *abstime)
```

相关声明：[mq_timedsend](#ac19939c8157d7ef9033a5be97a7ca6a1)、[mqd_t](#aa03ac56b19aba70879b7e2934da6a507)、[unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_a5eadbb82e0b9702d77f384a27827b334"></a>

```c
int mq_notify (mqd_t mqdes, const struct sigevent *notification)
```

相关声明：[mq_notify](#a5eadbb82e0b9702d77f384a27827b334)、[mqd_t](#aa03ac56b19aba70879b7e2934da6a507)、[sigevent](../posix_system_model_reference/P018_sigevent_结构体.md)。

## 231.4\_详细说明（Detailed Documentation）

<a id="aa03ac56b19aba70879b7e2934da6a507"></a>

### `mqd_t`

```c
typedef void* mqd_t
```

<a id="a3fbd3906296be63451c64d69be2bc371"></a>

### `mq_close()`

```c
int mq_close ( mqd_t mqdes)
```

<a id="a5a55ce03d8466a53a36601aaca9ee328"></a>

### `mq_getattr()`

```c
int mq_getattr ( mqd_t mqdes, struct mq_attr * mqstat )
```

<a id="a5eadbb82e0b9702d77f384a27827b334"></a>

### `mq_notify()`

```c
int mq_notify ( mqd_t mqdes, const struct sigevent * notification )
```

<a id="a6e6c4881ac0fd3ad18d733b96d088b8b"></a>

### `mq_open()`

```c
mqd_t mq_open ( const char * name, int oflags, ... )
```

<a id="ae0ff0175064ab31858eff0669b7e745b"></a>

### `mq_receive()`

```c
int mq_receive ( mqd_t mqdes, char * msg_ptr, size_t msg_len, unsigned int * msg_prio )
```

<a id="af13b6f0b3b15e14624b0c50050d062a4"></a>

### `mq_send()`

```c
int mq_send ( mqd_t mqdes, const char * msg_ptr, size_t msg_len, unsigned int msg_prio )
```

<a id="a83b7aa93cb6f1f5a4fd938baea5579a6"></a>

### `mq_setattr()`

```c
int mq_setattr ( mqd_t mqdes, const struct mq_attr * mqstat, struct mq_attr * omqstat )
```

<a id="aaf2e88ac75eac32eb5a3672fd56759b7"></a>

### `mq_timedreceive()`

```c
int mq_timedreceive ( mqd_t mqdes, char * msg_ptr, size_t msg_len, unsigned int * msg_prio, const struct timespec * abstime )
```

<a id="ac19939c8157d7ef9033a5be97a7ca6a1"></a>

### `mq_timedsend()`

```c
int mq_timedsend ( mqd_t mqdes, const char * msg_ptr, size_t msg_len, unsigned int msg_prio, const struct timespec * abstime )
```

<a id="accd8c5ee36e60d990963e1d544ef4140"></a>

### `mq_unlink()`

```c
int mq_unlink ( const char * name)
```


## 231.5\_原页交叉引用（Cross References）

- [signal.h](../api_source_reference/P784_signal.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/posix/fcntl.h](../api_source_reference/P255_fcntl.h_源码浏览.md)
- [zephyr/posix/sys/stat.h](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h_source.html)
- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P119_mqueue.h_源码浏览.md)
- [mq_attr](../posix_system_model_reference/P007_mq_attr_结构体.md)
- [unsigned](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [sigevent](../posix_system_model_reference/P018_sigevent_结构体.md)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P230_zephyr__mpipe__base__mpipe_base.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P232_zephyr__usb__msos_desc.h_文件参考.md)
