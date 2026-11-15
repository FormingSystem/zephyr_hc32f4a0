---
id: learning.zephyr-docs.api-file-media-sensor-reference.page-3
title: zephyr__sys__fdtable.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_sys\_\_fdtable.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdarg.h>
#include <time.h>
#include <sys/types.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/util.h>
#include <zephyr/fs/fs.h>
#include <zephyr/syscalls/fdtable.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_fd_5Fop_5Fvtable"></a>

```c
struct fd_op_vtable
```

相关声明：[fd_op_vtable](../posix_system_model_reference/P002_fd_op_vtable_结构体.md)。

文件描述符（File Descriptor）的虚方法表。

<a id="r_zvfs_5Fstat"></a>

```c
struct zvfs_stat
```

相关声明：[zvfs_stat](../posix_system_model_reference/P034_zvfs_stat_结构体.md)。

ZFD_IOCTL_STAT ioctl调用结果的结构。

<a id="r_zvfs_5Fpollfd"></a>

```c
struct zvfs_pollfd
```

相关声明：[zvfs_pollfd](../posix_system_model_reference/P033_zvfs_pollfd_结构体.md)。

<a id="r_zvfs_5Ffd_5Fset"></a>

```c
struct zvfs_fd_set
```

相关声明：[zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_afa29fb3c7ff76f1e6cf2d69947865163"></a>

```c
#define ZVFS_O_APPEND 0x0008
```

相关声明：[ZVFS_O_APPEND](#afa29fb3c7ff76f1e6cf2d69947865163)。

<a id="r_aff3387bcd512c9bea99c94aa3c459214"></a>

```c
#define ZVFS_O_CREAT 0x0200
```

相关声明：[ZVFS_O_CREAT](#aff3387bcd512c9bea99c94aa3c459214)。

<a id="r_aecd7cfa3a9afdf22aac7b90911f4f459"></a>

```c
#define ZVFS_O_TRUNC 0x0400
```

相关声明：[ZVFS_O_TRUNC](#aecd7cfa3a9afdf22aac7b90911f4f459)。

<a id="r_a1aeb8126a4c817bdd2740a93f191de16"></a>

```c
#define ZVFS_O_RDONLY 00
```

相关声明：[ZVFS_O_RDONLY](#a1aeb8126a4c817bdd2740a93f191de16)。

<a id="r_abf07c70a006713aaed00a82ed87fb2be"></a>

```c
#define ZVFS_O_WRONLY 01
```

相关声明：[ZVFS_O_WRONLY](#abf07c70a006713aaed00a82ed87fb2be)。

<a id="r_a82be0ad3089fdd844137845fa50d6e21"></a>

```c
#define ZVFS_O_RDWR 02
```

相关声明：[ZVFS_O_RDWR](#a82be0ad3089fdd844137845fa50d6e21)。

<a id="r_a2cb7a8f1c86ab67839458f0bc4198515"></a>

```c
#define ZVFS_O_EXCL 0x0800
```

相关声明：[ZVFS_O_EXCL](#a2cb7a8f1c86ab67839458f0bc4198515)。

<a id="r_a122add73257644aab0689853c57c53f3"></a>

```c
#define ZVFS_O_NONBLOCK 0x4000
```

相关声明：[ZVFS_O_NONBLOCK](#a122add73257644aab0689853c57c53f3)。

<a id="r_ac72b82ab9384b25f52acb061f96779b2"></a>

```c
#define ZVFS_F_DUPFD 0
```

相关声明：[ZVFS_F_DUPFD](#ac72b82ab9384b25f52acb061f96779b2)。

<a id="r_a02737faaf00631600b940982d1c9d0e5"></a>

```c
#define ZVFS_F_GETFL 3
```

相关声明：[ZVFS_F_GETFL](#a02737faaf00631600b940982d1c9d0e5)。

<a id="r_a9f090c1504183cc5a023908dea28940b"></a>

```c
#define ZVFS_F_SETFL 4
```

相关声明：[ZVFS_F_SETFL](#a9f090c1504183cc5a023908dea28940b)。

<a id="r_a1a7eb223a64cc8df1d236ad9d4373c04"></a>

```c
#define ZVFS_MODE_IFMT 0170000
```

相关声明：[ZVFS_MODE_IFMT](#a1a7eb223a64cc8df1d236ad9d4373c04)。

<a id="r_a4696b5a4cecb531946d2f5b2ecd8b8ff"></a>

```c
#define ZVFS_MODE_UNSPEC 0000000
```

相关声明：[ZVFS_MODE_UNSPEC](#a4696b5a4cecb531946d2f5b2ecd8b8ff)。

<a id="r_a6af8ed654a6cc5e0b21b2374ab56d4ae"></a>

```c
#define ZVFS_MODE_IFIFO 0010000
```

相关声明：[ZVFS_MODE_IFIFO](#a6af8ed654a6cc5e0b21b2374ab56d4ae)。

<a id="r_a02b35555e5ea7d2a577daa2b14ca7c6b"></a>

```c
#define ZVFS_MODE_IFCHR 0020000
```

相关声明：[ZVFS_MODE_IFCHR](#a02b35555e5ea7d2a577daa2b14ca7c6b)。

<a id="r_a2bdc08321b707a710c4fc3f755638954"></a>

```c
#define ZVFS_MODE_IMSGQ 0030000
```

相关声明：[ZVFS_MODE_IMSGQ](#a2bdc08321b707a710c4fc3f755638954)。

<a id="r_a44cd1a7ec98550ba895b0906ffbcb52d"></a>

```c
#define ZVFS_MODE_IFDIR 0040000
```

相关声明：[ZVFS_MODE_IFDIR](#a44cd1a7ec98550ba895b0906ffbcb52d)。

<a id="r_a22ed252f154ab0a11edfedd2c1468647"></a>

```c
#define ZVFS_MODE_IFSEM 0050000
```

相关声明：[ZVFS_MODE_IFSEM](#a22ed252f154ab0a11edfedd2c1468647)。

<a id="r_a0da8fae58fe76c88d5701e5c0683da91"></a>

```c
#define ZVFS_MODE_IFBLK 0060000
```

相关声明：[ZVFS_MODE_IFBLK](#a0da8fae58fe76c88d5701e5c0683da91)。

<a id="r_aa6c681e545a9ab1644c47d83d375697c"></a>

```c
#define ZVFS_MODE_IFSHM 0070000
```

相关声明：[ZVFS_MODE_IFSHM](#aa6c681e545a9ab1644c47d83d375697c)。

<a id="r_ad0bb04c7688eb917fa06939f277cc8c0"></a>

```c
#define ZVFS_MODE_IFREG 0100000
```

相关声明：[ZVFS_MODE_IFREG](#ad0bb04c7688eb917fa06939f277cc8c0)。

<a id="r_a66443b8d46b4f32cf1a17a3d0a0a1486"></a>

```c
#define ZVFS_MODE_IFLNK 0120000
```

相关声明：[ZVFS_MODE_IFLNK](#a66443b8d46b4f32cf1a17a3d0a0a1486)。

<a id="r_a2b0c1987c6ab087dd6cd91e7af2fb883"></a>

```c
#define ZVFS_MODE_IFSOCK 0140000
```

相关声明：[ZVFS_MODE_IFSOCK](#a2b0c1987c6ab087dd6cd91e7af2fb883)。

<a id="r_abacd664acb7f265a70011864e7ba9b0f"></a>

```c
#define ZVFS_POLLIN BIT(0)
```

相关声明：[ZVFS_POLLIN](#abacd664acb7f265a70011864e7ba9b0f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_adf798c33fb9da067a17ffd68514791af"></a>

```c
#define ZVFS_POLLPRI BIT(1)
```

相关声明：[ZVFS_POLLPRI](#adf798c33fb9da067a17ffd68514791af)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ac1938ed509009a549d0eee1c8a9ffe80"></a>

```c
#define ZVFS_POLLOUT BIT(2)
```

相关声明：[ZVFS_POLLOUT](#ac1938ed509009a549d0eee1c8a9ffe80)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_acddab9e57408c2b5800c60be120f1101"></a>

```c
#define ZVFS_POLLERR BIT(3)
```

相关声明：[ZVFS_POLLERR](#acddab9e57408c2b5800c60be120f1101)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a510aeed3c8541e8f48db1c3241c85aab"></a>

```c
#define ZVFS_POLLHUP BIT(4)
```

相关声明：[ZVFS_POLLHUP](#a510aeed3c8541e8f48db1c3241c85aab)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a25568088715f7eacbd673a896f38caf2"></a>

```c
#define ZVFS_POLLNVAL BIT(5)
```

相关声明：[ZVFS_POLLNVAL](#a25568088715f7eacbd673a896f38caf2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ae8d10dc8bd02e619f8c384c493f53709"></a>

```c
#define ZVFS_FD_SETSIZE (sizeof(((struct zvfs_fd_set *)0)->bitset) * 8)
```

相关声明：[ZVFS_FD_SETSIZE](#ae8d10dc8bd02e619f8c384c493f53709)、[zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)。

可添加到 `zvfs_fd_set` 中的文件描述符数量（Number of File Descriptors）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.3\_枚举（Enumerations）

<a id="r_aac8cb8bde69d227a7a8e9edf2980bd20"></a>

```c
enum { ZFD_IOCTL_FSYNC = 0x100 , ZFD_IOCTL_LSEEK , ZFD_IOCTL_POLL_PREPARE , ZFD_IOCTL_POLL_UPDATE , ZFD_IOCTL_POLL_OFFLOAD , ZFD_IOCTL_SET_LOCK , ZFD_IOCTL_STAT , ZFD_IOCTL_TRUNCATE , ZFD_IOCTL_MMAP , ZFD_IOCTL_FIONREAD = 0x541B , ZFD_IOCTL_FIONBIO = 0x5421 , ZFD_IOCTL_FIONWRITE = 0x5411 }
```

相关声明：[ZFD_IOCTL_FSYNC](#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4)、[ZFD_IOCTL_LSEEK](#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072)、[ZFD_IOCTL_POLL_PREPARE](#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e)、[ZFD_IOCTL_POLL_UPDATE](#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa)、[ZFD_IOCTL_POLL_OFFLOAD](#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe)、[ZFD_IOCTL_SET_LOCK](#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62)、[ZFD_IOCTL_STAT](#aac8cb8bde69d227a7a8e9edf2980bd20ac43f1468ea5c3e2124c415aae4f7402c)、[ZFD_IOCTL_TRUNCATE](#aac8cb8bde69d227a7a8e9edf2980bd20aaccc19cb18dff80fd30127ff14a296e5)、[ZFD_IOCTL_MMAP](#aac8cb8bde69d227a7a8e9edf2980bd20ad0d133771395d2ed7d1d6adcf203376f)、[ZFD_IOCTL_FIONREAD](#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683)、[ZFD_IOCTL_FIONBIO](#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530)、[ZFD_IOCTL_FIONWRITE](#aac8cb8bde69d227a7a8e9edf2980bd20a1e88b6e9ca6cf0db43029f485af43ccb)。

`fd_op_vtable.ioctl()` 的请求代码（Request Codes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_a0805f751464ff9a51a463841ce35ff5f"></a>

```c
int zvfs_reserve_fd (void)
```

相关声明：[zvfs_reserve_fd](#a0805f751464ff9a51a463841ce35ff5f)。

预留文件描述符（Reserve File Descriptor）。

<a id="r_a448172e130af96c11af2fe6511e6b262"></a>

```c
void zvfs_finalize_typed_fd (int fd, void *obj, const struct fd_op_vtable *vtable, uint32_t mode)
```

相关声明：[zvfs_finalize_typed_fd](#a448172e130af96c11af2fe6511e6b262)、[fd_op_vtable](../posix_system_model_reference/P002_fd_op_vtable_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

完成文件描述符（File Descriptor）的创建，并传递类型信息。

<a id="r_a0bb7c530d69c9e5b1cfc61e7a11441af"></a>

```c
static void zvfs_finalize_fd (int fd, void *obj, const struct fd_op_vtable *vtable)
```

相关声明：[zvfs_finalize_fd](#a0bb7c530d69c9e5b1cfc61e7a11441af)、[fd_op_vtable](../posix_system_model_reference/P002_fd_op_vtable_结构体.md)。

完成文件描述符（File Descriptor）的创建。

<a id="r_a0248f37e9b8cfc0a76ced956b75a3ed2"></a>

```c
int zvfs_alloc_fd (void *obj, const struct fd_op_vtable *vtable)
```

相关声明：[zvfs_alloc_fd](#a0248f37e9b8cfc0a76ced956b75a3ed2)、[fd_op_vtable](../posix_system_model_reference/P002_fd_op_vtable_结构体.md)。

为底层输入／输出对象（I/O Object）分配文件描述符（File Descriptor）。

<a id="r_a5cedc4a2f8375d103238d611f6ed3422"></a>

```c
void zvfs_free_fd (int fd)
```

相关声明：[zvfs_free_fd](#a5cedc4a2f8375d103238d611f6ed3422)。

释放预留的文件描述符（Reserved File Descriptor）。

<a id="r_a8655ab5d3b0776f27eb67d53ef8a431b"></a>

```c
void * zvfs_get_fd_obj (int fd, const struct fd_op_vtable *vtable, int err)
```

相关声明：[zvfs_get_fd_obj](#a8655ab5d3b0776f27eb67d53ef8a431b)、[fd_op_vtable](../posix_system_model_reference/P002_fd_op_vtable_结构体.md)。

根据文件描述符（File Descriptor）获取底层对象指针（Underlying Object Pointer）。

<a id="r_a0b8c1eeb3ff253e45d45752b77679e17"></a>

```c
void * zvfs_get_fd_obj_and_vtable (int fd, const struct fd_op_vtable **vtable, struct k_mutex **lock)
```

相关声明：[zvfs_get_fd_obj_and_vtable](#a0b8c1eeb3ff253e45d45752b77679e17)、[fd_op_vtable](../posix_system_model_reference/P002_fd_op_vtable_结构体.md)、[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)。

根据文件描述符（File Descriptor）获取底层对象指针和虚函数表指针（Vtable Pointer）。

<a id="r_a54e1f1cbd983631903757a93997c3fab"></a>

```c
bool zvfs_get_obj_lock_and_cond (void *obj, const struct fd_op_vtable *vtable, struct k_mutex **lock, struct k_condvar **cond)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[zvfs_get_obj_lock_and_cond](#a54e1f1cbd983631903757a93997c3fab)、[fd_op_vtable](../posix_system_model_reference/P002_fd_op_vtable_结构体.md)、[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[k_condvar](../synchronization_reference/P011_内核条件变量结构.md)。

获取与给定对象及虚函数表（Vtable）关联的互斥量（Mutex）和条件变量（Condition Variable）。

<a id="r_a78c25e35ddacd2d4287cc24acf4126cc"></a>

```c
static int zvfs_fdtable_call_ioctl (const struct fd_op_vtable *vtable, void *obj, unsigned long request,...)
```

相关声明：[zvfs_fdtable_call_ioctl](#a78c25e35ddacd2d4287cc24acf4126cc)、[fd_op_vtable](../posix_system_model_reference/P002_fd_op_vtable_结构体.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

使用可变参数（Varargs）调用对象的 `ioctl` 虚方法（Virtual Method）。

<a id="r_a1a758fb84d99d0390b6a8d51ec7cda34"></a>

```c
int zvfs_poll (struct zvfs_pollfd *fds, int nfds, int poll_timeout)
```

相关声明：[zvfs_poll](#a1a758fb84d99d0390b6a8d51ec7cda34)、[zvfs_pollfd](../posix_system_model_reference/P033_zvfs_pollfd_结构体.md)。

<a id="r_a029809dfde96846d9e7871e252d74546"></a>

```c
void ZVFS_FD_CLR (int fd, struct zvfs_fd_set *fdset)
```

相关声明：[ZVFS_FD_CLR](#a029809dfde96846d9e7871e252d74546)、[zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)。

<a id="r_a84f63f19ea89e5711725f4d753b5484c"></a>

```c
int ZVFS_FD_ISSET (int fd, struct zvfs_fd_set *fdset)
```

相关声明：[ZVFS_FD_ISSET](#a84f63f19ea89e5711725f4d753b5484c)、[zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)。

<a id="r_afa48d92e5f545412139f567a19e01f71"></a>

```c
void ZVFS_FD_SET (int fd, struct zvfs_fd_set *fdset)
```

相关声明：[ZVFS_FD_SET](#afa48d92e5f545412139f567a19e01f71)、[zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)。

<a id="r_a46ae4a3ac3d192de02fb1b6c4a4e95ac"></a>

```c
void ZVFS_FD_ZERO (struct zvfs_fd_set *fdset)
```

相关声明：[ZVFS_FD_ZERO](#a46ae4a3ac3d192de02fb1b6c4a4e95ac)、[zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)。

<a id="r_a8ced1fc0adbdf35b71ec486a8ec68665"></a>

```c
int zvfs_select (int nfds, struct zvfs_fd_set *ZRESTRICT readfds, struct zvfs_fd_set *ZRESTRICT writefds, struct zvfs_fd_set *ZRESTRICT errorfds, const struct timespec *ZRESTRICT timeout, const void *ZRESTRICT sigmask)
```

相关声明：[zvfs_select](#a8ced1fc0adbdf35b71ec486a8ec68665)、[zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)、[zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)、[zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_a382577239f3941d357d313b38464c954"></a>

```c
int zvfs_open (const char *name, int flags, struct fd_op_vtable *vtable)
```

相关声明：[zvfs_open](#a382577239f3941d357d313b38464c954)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[fd_op_vtable](../posix_system_model_reference/P002_fd_op_vtable_结构体.md)。

打开指定名称的文件（File）。

<a id="r_a2ae009f516139ac12492a15bb1a31f97"></a>

```c
int zvfs_fstat (int fd, struct zvfs_stat *buf)
```

相关声明：[zvfs_fstat](#a2ae009f516139ac12492a15bb1a31f97)、[zvfs_stat](../posix_system_model_reference/P034_zvfs_stat_结构体.md)。

获取文件信息（File Information）。

<a id="r_a24bf5bb71435e4921e051d115bf7b7db"></a>

```c
int zvfs_close (int fd)
```

相关声明：[zvfs_close](#a24bf5bb71435e4921e051d115bf7b7db)。

关闭文件（File）。

<a id="r_a8a5a70692eb13de80858e976c4ae5004"></a>

```c
ssize_t zvfs_read (int fd, void *buf, size_t sz, const size_t *from_offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zvfs_read](#a8a5a70692eb13de80858e976c4ae5004)。

从文件（File）读取字节。

<a id="r_a23e688ef88dd22d2350e790b44dbf28f"></a>

```c
ssize_t zvfs_write (int fd, const void *buf, size_t sz, const size_t *from_offset)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[zvfs_write](#a23e688ef88dd22d2350e790b44dbf28f)。

向文件（File）写入字节。

<a id="r_a72815fac0eac70fa60d2a25a4aa4908d"></a>

```c
int zvfs_unlink (const char *path)
```

相关声明：[zvfs_unlink](#a72815fac0eac70fa60d2a25a4aa4908d)。

删除文件或目录（File or Directory）。

<a id="r_a75c63fae34489b6297615de253c87d44"></a>

```c
int zvfs_rename (const char *old, const char *newp)
```

相关声明：[zvfs_rename](#a75c63fae34489b6297615de253c87d44)。

重命名文件或目录（File or Directory），必要时进行移动。

## 3.5\_详细说明（Detailed Documentation）

<a id="ac72b82ab9384b25f52acb061f96779b2"></a>

### `ZVFS_F_DUPFD`

```c
#define ZVFS_F_DUPFD 0
```

<a id="a02737faaf00631600b940982d1c9d0e5"></a>

### `ZVFS_F_GETFL`

```c
#define ZVFS_F_GETFL 3
```

<a id="a9f090c1504183cc5a023908dea28940b"></a>

### `ZVFS_F_SETFL`

```c
#define ZVFS_F_SETFL 4
```

<a id="ae8d10dc8bd02e619f8c384c493f53709"></a>

### `ZVFS_FD_SETSIZE`

```c
#define ZVFS_FD_SETSIZE (sizeof(((struct zvfs_fd_set *)0)->bitset) * 8)
```

可添加到 `zvfs_fd_set` 中的文件描述符数量（Number of File Descriptors）。

<a id="a0da8fae58fe76c88d5701e5c0683da91"></a>

### `ZVFS_MODE_IFBLK`

```c
#define ZVFS_MODE_IFBLK 0060000
```

<a id="a02b35555e5ea7d2a577daa2b14ca7c6b"></a>

### `ZVFS_MODE_IFCHR`

```c
#define ZVFS_MODE_IFCHR 0020000
```

<a id="a44cd1a7ec98550ba895b0906ffbcb52d"></a>

### `ZVFS_MODE_IFDIR`

```c
#define ZVFS_MODE_IFDIR 0040000
```

<a id="a6af8ed654a6cc5e0b21b2374ab56d4ae"></a>

### `ZVFS_MODE_IFIFO`

```c
#define ZVFS_MODE_IFIFO 0010000
```

<a id="a66443b8d46b4f32cf1a17a3d0a0a1486"></a>

### `ZVFS_MODE_IFLNK`

```c
#define ZVFS_MODE_IFLNK 0120000
```

<a id="a1a7eb223a64cc8df1d236ad9d4373c04"></a>

### `ZVFS_MODE_IFMT`

```c
#define ZVFS_MODE_IFMT 0170000
```

<a id="ad0bb04c7688eb917fa06939f277cc8c0"></a>

### `ZVFS_MODE_IFREG`

```c
#define ZVFS_MODE_IFREG 0100000
```

<a id="a22ed252f154ab0a11edfedd2c1468647"></a>

### `ZVFS_MODE_IFSEM`

```c
#define ZVFS_MODE_IFSEM 0050000
```

<a id="aa6c681e545a9ab1644c47d83d375697c"></a>

### `ZVFS_MODE_IFSHM`

```c
#define ZVFS_MODE_IFSHM 0070000
```

<a id="a2b0c1987c6ab087dd6cd91e7af2fb883"></a>

### `ZVFS_MODE_IFSOCK`

```c
#define ZVFS_MODE_IFSOCK 0140000
```

<a id="a2bdc08321b707a710c4fc3f755638954"></a>

### `ZVFS_MODE_IMSGQ`

```c
#define ZVFS_MODE_IMSGQ 0030000
```

<a id="a4696b5a4cecb531946d2f5b2ecd8b8ff"></a>

### `ZVFS_MODE_UNSPEC`

```c
#define ZVFS_MODE_UNSPEC 0000000
```

<a id="afa29fb3c7ff76f1e6cf2d69947865163"></a>

### `ZVFS_O_APPEND`

```c
#define ZVFS_O_APPEND 0x0008
```

<a id="aff3387bcd512c9bea99c94aa3c459214"></a>

### `ZVFS_O_CREAT`

```c
#define ZVFS_O_CREAT 0x0200
```

<a id="a2cb7a8f1c86ab67839458f0bc4198515"></a>

### `ZVFS_O_EXCL`

```c
#define ZVFS_O_EXCL 0x0800
```

<a id="a122add73257644aab0689853c57c53f3"></a>

### `ZVFS_O_NONBLOCK`

```c
#define ZVFS_O_NONBLOCK 0x4000
```

<a id="a1aeb8126a4c817bdd2740a93f191de16"></a>

### `ZVFS_O_RDONLY`

```c
#define ZVFS_O_RDONLY 00
```

<a id="a82be0ad3089fdd844137845fa50d6e21"></a>

### `ZVFS_O_RDWR`

```c
#define ZVFS_O_RDWR 02
```

<a id="aecd7cfa3a9afdf22aac7b90911f4f459"></a>

### `ZVFS_O_TRUNC`

```c
#define ZVFS_O_TRUNC 0x0400
```

<a id="abf07c70a006713aaed00a82ed87fb2be"></a>

### `ZVFS_O_WRONLY`

```c
#define ZVFS_O_WRONLY 01
```

<a id="acddab9e57408c2b5800c60be120f1101"></a>

### `ZVFS_POLLERR`

```c
#define ZVFS_POLLERR BIT(3)
```

<a id="a510aeed3c8541e8f48db1c3241c85aab"></a>

### `ZVFS_POLLHUP`

```c
#define ZVFS_POLLHUP BIT(4)
```

<a id="abacd664acb7f265a70011864e7ba9b0f"></a>

### `ZVFS_POLLIN`

```c
#define ZVFS_POLLIN BIT(0)
```

<a id="a25568088715f7eacbd673a896f38caf2"></a>

### `ZVFS_POLLNVAL`

```c
#define ZVFS_POLLNVAL BIT(5)
```

<a id="ac1938ed509009a549d0eee1c8a9ffe80"></a>

### `ZVFS_POLLOUT`

```c
#define ZVFS_POLLOUT BIT(2)
```

<a id="adf798c33fb9da067a17ffd68514791af"></a>

### `ZVFS_POLLPRI`

```c
#define ZVFS_POLLPRI BIT(1)
```

<a id="aac8cb8bde69d227a7a8e9edf2980bd20"></a>

### `anonymous enum`

```c
anonymous enum
```

`fd_op_vtable.ioctl()` 的请求代码（Request Codes）。

注意，这些代码是 Zephyr 内部编号，用于 Zephyr 内部操作，可能在不通知的情况下改变，不属于稳定应用二进制接口（Stable ABI）。但它们应能与通用的 POSIX/Linux `ioctl` 编号共存，且不发生冲突。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ZFD_IOCTL_FSYNC` |  |
| `ZFD_IOCTL_LSEEK` |  |
| `ZFD_IOCTL_POLL_PREPARE` |  |
| `ZFD_IOCTL_POLL_UPDATE` |  |
| `ZFD_IOCTL_POLL_OFFLOAD` |  |
| `ZFD_IOCTL_SET_LOCK` |  |
| `ZFD_IOCTL_STAT` |  |
| `ZFD_IOCTL_TRUNCATE` |  |
| `ZFD_IOCTL_MMAP` |  |
| `ZFD_IOCTL_FIONREAD` | 获取可供读取的字节数（Number of Bytes Available to Read）。 |
| `ZFD_IOCTL_FIONBIO` | 设置非阻塞模式（Non-Blocking Mode）。 |
| `ZFD_IOCTL_FIONWRITE` | 获取已排队等待 TCP 发送、但尚未收到确认的字节数（Unacknowledged TCP TX Bytes）。 |

<a id="a0248f37e9b8cfc0a76ced956b75a3ed2"></a>

### `zvfs_alloc_fd()`

```c
int zvfs_alloc_fd ( void * obj, const struct fd_op_vtable * vtable )
```

为底层输入／输出对象（I/O Object）分配文件描述符（File Descriptor）。

本函数将 `zvfs_reserve_fd()` 和 `zvfs_finalize_fd()` 的操作合并为一步，以方便使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obj` | 指向输入／输出对象结构体（I/O Object Structure）的指针。 |
| `vtable` | 指向该对象输入／输出操作实现（I/O Operation Implementations）的指针。 |

**返回（Returns）**：返回值（Returns）：分配得到的文件描述符（File Descriptor）；出错时为 -1，并设置 `errno`。

<a id="a24bf5bb71435e4921e051d115bf7b7db"></a>

### `zvfs_close()`

```c
int zvfs_close ( int fd)
```

关闭文件（File）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 文件描述符索引（File Descriptor Index）。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；出错时为 -1，并设置 `errno`。

<a id="a029809dfde96846d9e7871e252d74546"></a>

### `ZVFS_FD_CLR()`

```c
void ZVFS_FD_CLR ( int fd, struct zvfs_fd_set * fdset )
```

<a id="a84f63f19ea89e5711725f4d753b5484c"></a>

### `ZVFS_FD_ISSET()`

```c
int ZVFS_FD_ISSET ( int fd, struct zvfs_fd_set * fdset )
```

<a id="afa48d92e5f545412139f567a19e01f71"></a>

### `ZVFS_FD_SET()`

```c
void ZVFS_FD_SET ( int fd, struct zvfs_fd_set * fdset )
```

<a id="a46ae4a3ac3d192de02fb1b6c4a4e95ac"></a>

### `ZVFS_FD_ZERO()`

```c
void ZVFS_FD_ZERO ( struct zvfs_fd_set * fdset)
```

<a id="a78c25e35ddacd2d4287cc24acf4126cc"></a>

### `zvfs_fdtable_call_ioctl()`

```c
int zvfs_fdtable_call_ioctl ( const struct fd_op_vtable * vtable, void * obj, unsigned long request, ... )
```

声明属性：`inline`、`static`。

使用可变参数（Varargs）调用对象的 `ioctl` 虚方法（Virtual Method）。

需要此辅助函数，是因为 `ioctl` 虚方法（Virtual Method）声明为接收 `va_list`，而构造 `va_list` 的唯一可移植方式是使用函数的 `...` 参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `vtable` | 包含 `ioctl` 函数指针的虚函数表（Vtable）。 |
| `obj` | 要在其上调用 `ioctl` 的对象（Object）。 |
| `request` | `ioctl` 请求编号（Request Number）。 |
| `...` | 传给 `ioctl` 的可变参数（Variadic Arguments）。 |

<a id="a0bb7c530d69c9e5b1cfc61e7a11441af"></a>

### `zvfs_finalize_fd()`

```c
void zvfs_finalize_fd ( int fd, void * obj, const struct fd_op_vtable * vtable )
```

声明属性：`inline`、`static`。

完成文件描述符（File Descriptor）的创建。

本函数应在 `zvfs_reserve_fd()` 之后恰好调用一次，不应在其他情况下调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 先前由 `zvfs_reserve_fd()` 返回的文件描述符（File Descriptor）。 |
| `obj` | 指向输入／输出对象结构体（I/O Object Structure）的指针。 |
| `vtable` | 指向该对象输入／输出操作实现（I/O Operation Implementations）的指针。 |

<a id="a448172e130af96c11af2fe6511e6b262"></a>

### `zvfs_finalize_typed_fd()`

```c
void zvfs_finalize_typed_fd ( int fd, void * obj, const struct fd_op_vtable * vtable, uint32_t mode )
```

完成文件描述符（File Descriptor）的创建，并传递类型信息。

本函数应在 `zvfs_reserve_fd()` 之后恰好调用一次，不应在其他情况下调用。

本函数与 `zvfs_finalize_fd` 的区别是，后者不传递所创建文件描述符（File Descriptor）的类型信息。

`mode` 允许的取值为 `ZVFS_MODE_...` 之一。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 先前由 `zvfs_reserve_fd()` 返回的文件描述符（File Descriptor）。 |
| `obj` | 指向输入／输出对象结构体（I/O Object Structure）的指针。 |
| `vtable` | 指向该对象输入／输出操作实现（I/O Operation Implementations）的指针。 |
| `mode` | 如上所述的文件类型（File Type）。 |

<a id="a5cedc4a2f8375d103238d611f6ed3422"></a>

### `zvfs_free_fd()`

```c
void zvfs_free_fd ( int fd)
```

释放预留的文件描述符（Reserved File Descriptor）。

本函数可在 `zvfs_reserve_fd()` 之后调用一次，不应在其他情况下调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 先前由 `zvfs_reserve_fd()` 返回的文件描述符（File Descriptor）。 |

<a id="a2ae009f516139ac12492a15bb1a31f97"></a>

### `zvfs_fstat()`

```c
int zvfs_fstat ( int fd, struct zvfs_stat * buf )
```

获取文件信息（File Information）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 文件描述符索引（File Descriptor Index）。 |
| `buf` | 指向结果结构体（Result Structure）的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；出错时为 -1，并设置 `errno`。

<a id="a8655ab5d3b0776f27eb67d53ef8a431b"></a>

### `zvfs_get_fd_obj()`

```c
void * zvfs_get_fd_obj ( int fd, const struct fd_op_vtable * vtable, int err )
```

根据文件描述符（File Descriptor）获取底层对象指针（Underlying Object Pointer）。

本函数供 `read`／`write`／`ioctl` 以外的函数根据 `fd` 查找底层输入／输出对象（I/O Object），并可选择利用虚函数表引用（Vtable Reference）检查其类型。如果 `fd` 指向无效条目，则返回 `NULL` 并将 `errno` 设为 `EBADF`。如果 `fd` 有效，但 `vtable` 参数非 `NULL` 且与对象的虚函数表不匹配，则返回 `NULL` 并将 `errno` 设为 `err` 参数的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 先前由 `zvfs_reserve_fd()` 返回的文件描述符（File Descriptor）。 |
| `vtable` | 预期的对象虚函数表（Object Vtable），或 `NULL`。 |
| `err` | 对象虚函数表（Object Vtable）不匹配时要设置的 `errno` 值。 |

**返回（Returns）**：返回值（Returns）：对象指针（Object Pointer），或 `NULL`，并设置 `errno`。

<a id="a0b8c1eeb3ff253e45d45752b77679e17"></a>

### `zvfs_get_fd_obj_and_vtable()`

```c
void * zvfs_get_fd_obj_and_vtable ( int fd, const struct fd_op_vtable ** vtable, struct k_mutex ** lock )
```

根据文件描述符（File Descriptor）获取底层对象指针和虚函数表指针（Vtable Pointer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 先前由 `zvfs_reserve_fd()` 返回的文件描述符（File Descriptor）。 |
| `vtable` | 指向指针变量的指针，用于存储虚函数表（Vtable）。 |
| `lock` | 可选的指针，指向用于存储互斥量（Mutex）的指针变量。该互斥量用于防止并发访问描述符。本函数不会获取锁，只将锁返回，以便调用者按需使用。调用者不需要锁时传入 `NULL`。 |

**返回（Returns）**：返回值（Returns）：对象指针（Object Pointer），或 `NULL`，并设置 `errno`。

<a id="a54e1f1cbd983631903757a93997c3fab"></a>

### `zvfs_get_obj_lock_and_cond()`

```c
bool zvfs_get_obj_lock_and_cond ( void * obj, const struct fd_op_vtable * vtable, struct k_mutex ** lock, struct k_condvar ** cond )
```

获取与给定对象及虚函数表（Vtable）关联的互斥量（Mutex）和条件变量（Condition Variable）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `obj` | 先前由 `zvfs_get_fd_obj` 等调用返回的对象（Object）。 |
| `vtable` | 指向与 `obj` 关联的虚函数表（Vtable）的指针。 |
| `lock` | 可选的指针，指向用于存储互斥量（Mutex）的指针变量。该互斥量用于防止并发访问描述符。本函数不会获取锁，只将锁返回，以便调用者按需使用。调用者不需要锁时传入 `NULL`。 |
| `cond` | 可选的指针，指向用于存储条件变量（Condition Variable）的指针变量。该条件变量用于在并发访问描述符时通知等待线程。调用者不需要条件变量时传入 `NULL`。 |

**返回（Returns）**：返回值（Returns）：成功时为 `true`，否则为 `false`。

<a id="a382577239f3941d357d313b38464c954"></a>

### `zvfs_open()`

```c
int zvfs_open ( const char * name, int flags, struct fd_op_vtable * vtable )
```

打开指定名称的文件（File）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 文件名称（File Name）。 |
| `flags` | `fs_open` 的访问模式（Access Modes）。 |
| `vtable` | 指向具有相应输入／输出函数（I/O Functions）的结构体的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为新创建的文件描述符索引（File Descriptor Index）；出错时为 -1，并设置 `errno`。

<a id="a1a758fb84d99d0390b6a8d51ec7cda34"></a>

### `zvfs_poll()`

```c
int zvfs_poll ( struct zvfs_pollfd * fds, int nfds, int poll_timeout )
```

<a id="a8a5a70692eb13de80858e976c4ae5004"></a>

### `zvfs_read()`

```c
ssize_t zvfs_read ( int fd, void * buf, size_t sz, const size_t * from_offset )
```

从文件（File）读取字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 文件描述符索引（File Descriptor Index）。 |
| `buf` | 目标缓冲区。 |
| `sz` | 要读取的字节数。 |
| `from_offset` | 指向指定起始位置（Starting Position）的变量的指针；为 `NULL` 时使用当前偏移量（Current Offset）。 |

**返回（Returns）**：返回值（Returns）：成功读取的字节数；失败时为 -1，并设置 `errno`。

<a id="a75c63fae34489b6297615de253c87d44"></a>

### `zvfs_rename()`

```c
int zvfs_rename ( const char * old, const char * newp )
```

重命名文件或目录（File or Directory），必要时进行移动。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `old` | 当前名称（Current Name）。 |
| `newp` | 目标名称（Target Name）。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；出错时为 -1，并设置 `errno`。

<a id="a0805f751464ff9a51a463841ce35ff5f"></a>

### `zvfs_reserve_fd()`

```c
int zvfs_reserve_fd ( void )
```

预留文件描述符（Reserve File Descriptor）。

本函数在底层表中为文件描述符条目（File Descriptor Entry）预留空间，因此没有空闲描述符时，调用者能够尽早失败。如果本函数成功，必须调用 `zvfs_finalize_fd()` 或 `zvfs_free_fd()`。

**返回（Returns）**：返回值（Returns）：分配得到的文件描述符（File Descriptor）；出错时为 -1，并设置 `errno`。

<a id="a8ced1fc0adbdf35b71ec486a8ec68665"></a>

### `zvfs_select()`

```c
int zvfs_select ( int nfds, struct zvfs_fd_set *ZRESTRICT readfds, struct zvfs_fd_set *ZRESTRICT writefds, struct zvfs_fd_set *ZRESTRICT errorfds, const struct timespec *ZRESTRICT timeout, const void *ZRESTRICT sigmask )
```

<a id="a72815fac0eac70fa60d2a25a4aa4908d"></a>

### `zvfs_unlink()`

```c
int zvfs_unlink ( const char * path)
```

删除文件或目录（File or Directory）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `path` | 要移除文件的路径或名称（Path or Name）。 |

**返回（Returns）**：返回值（Returns）：成功时为 0；出错时为 -1，并设置 `errno`。

<a id="a23e688ef88dd22d2350e790b44dbf28f"></a>

### `zvfs_write()`

```c
ssize_t zvfs_write ( int fd, const void * buf, size_t sz, const size_t * from_offset )
```

向文件（File）写入字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 文件描述符索引（File Descriptor Index）。 |
| `buf` | 源缓冲区。 |
| `sz` | 要写入的字节数。 |
| `from_offset` | 指向指定起始位置（Starting Position）的变量的指针；为 `NULL` 时使用当前偏移量（Current Offset）。 |

**返回（Returns）**：返回值（Returns）：成功写入的字节数；失败时为 -1，并设置 `errno`。


## 3.6\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/fs/fs.h](../api_source_supplement_reference/P074_fs.h_源码浏览.md)
- [查看此文件的源码。](../api_source_architecture_reference/P007_fdtable.h_源码浏览.md)
- [fd_op_vtable](../posix_system_model_reference/P002_fd_op_vtable_结构体.md)
- [zvfs_stat](../posix_system_model_reference/P034_zvfs_stat_结构体.md)
- [zvfs_pollfd](../posix_system_model_reference/P033_zvfs_pollfd_结构体.md)
- [zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [fd_op_vtable.ioctl()](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#aff079f05422413a0df3394ddfecc0298)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [k_condvar](../synchronization_reference/P011_内核条件变量结构.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [fs_open](https://docs.zephyrproject.org/latest/doxygen/html/group__file__system__api.html#ga9c90031ba3e5a10da8e00e81d53ef63b)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4"></a>
<a id="aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072"></a>
<a id="aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e"></a>
<a id="aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa"></a>
<a id="aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe"></a>
<a id="aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62"></a>
<a id="aac8cb8bde69d227a7a8e9edf2980bd20ac43f1468ea5c3e2124c415aae4f7402c"></a>
<a id="aac8cb8bde69d227a7a8e9edf2980bd20aaccc19cb18dff80fd30127ff14a296e5"></a>
<a id="aac8cb8bde69d227a7a8e9edf2980bd20ad0d133771395d2ed7d1d6adcf203376f"></a>
<a id="aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683"></a>
<a id="aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530"></a>
<a id="aac8cb8bde69d227a7a8e9edf2980bd20a1e88b6e9ca6cf0db43029f485af43ccb"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_zephyr__bluetooth__classic__map.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__video__formats.h_文件参考.md)
