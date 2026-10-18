---
id: learning.zephyr-docs.api-source-architecture-reference.page-7
title: fdtable.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_fdtable.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html)。

## 7.1\_原始可见代码（Source Code）

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
<a id="foldopen00082"></a>
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
<a id="l00111"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="foldopen00152"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="foldopen00243"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="foldopen00260"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="foldopen00265"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="foldopen00273"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
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
<a id="l00316"></a>
<a id="l00318"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="afdtable_8h_html_a0248f37e9b8cfc0a76ced956b75a3ed2"></a>
<a id="afdtable_8h_html_a029809dfde96846d9e7871e252d74546"></a>
<a id="afdtable_8h_html_a0805f751464ff9a51a463841ce35ff5f"></a>
<a id="afdtable_8h_html_a0b8c1eeb3ff253e45d45752b77679e17"></a>
<a id="afdtable_8h_html_a0bb7c530d69c9e5b1cfc61e7a11441af"></a>
<a id="afdtable_8h_html_a1a758fb84d99d0390b6a8d51ec7cda34"></a>
<a id="afdtable_8h_html_a23e688ef88dd22d2350e790b44dbf28f"></a>
<a id="afdtable_8h_html_a24bf5bb71435e4921e051d115bf7b7db"></a>
<a id="afdtable_8h_html_a2ae009f516139ac12492a15bb1a31f97"></a>
<a id="afdtable_8h_html_a382577239f3941d357d313b38464c954"></a>
<a id="afdtable_8h_html_a448172e130af96c11af2fe6511e6b262"></a>
<a id="afdtable_8h_html_a4696b5a4cecb531946d2f5b2ecd8b8ff"></a>
<a id="afdtable_8h_html_a46ae4a3ac3d192de02fb1b6c4a4e95ac"></a>
<a id="afdtable_8h_html_a54e1f1cbd983631903757a93997c3fab"></a>
<a id="afdtable_8h_html_a5cedc4a2f8375d103238d611f6ed3422"></a>
<a id="afdtable_8h_html_a72815fac0eac70fa60d2a25a4aa4908d"></a>
<a id="afdtable_8h_html_a75c63fae34489b6297615de253c87d44"></a>
<a id="afdtable_8h_html_a78c25e35ddacd2d4287cc24acf4126cc"></a>
<a id="afdtable_8h_html_a84f63f19ea89e5711725f4d753b5484c"></a>
<a id="afdtable_8h_html_a8655ab5d3b0776f27eb67d53ef8a431b"></a>
<a id="afdtable_8h_html_a8a5a70692eb13de80858e976c4ae5004"></a>
<a id="afdtable_8h_html_a8ced1fc0adbdf35b71ec486a8ec68665"></a>
<a id="afdtable_8h_html_aac8cb8bde69d227a7a8e9edf2980bd20a1e88b6e9ca6cf0db43029f485af43ccb"></a>
<a id="afdtable_8h_html_aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62"></a>
<a id="afdtable_8h_html_aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683"></a>
<a id="afdtable_8h_html_aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e"></a>
<a id="afdtable_8h_html_aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4"></a>
<a id="afdtable_8h_html_aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072"></a>
<a id="afdtable_8h_html_aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530"></a>
<a id="afdtable_8h_html_aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe"></a>
<a id="afdtable_8h_html_aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa"></a>
<a id="afdtable_8h_html_aac8cb8bde69d227a7a8e9edf2980bd20aaccc19cb18dff80fd30127ff14a296e5"></a>
<a id="afdtable_8h_html_aac8cb8bde69d227a7a8e9edf2980bd20ac43f1468ea5c3e2124c415aae4f7402c"></a>
<a id="afdtable_8h_html_aac8cb8bde69d227a7a8e9edf2980bd20ad0d133771395d2ed7d1d6adcf203376f"></a>
<a id="afdtable_8h_html_afa48d92e5f545412139f567a19e01f71"></a>
<a id="afs_8h_html"></a>
<a id="agroup__sys-util_html_gae664e7492e37d324831caf2321ddda37"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructfd__op__vtable_html"></a>
<a id="astructfd__op__vtable_html_a139c24a21d141ccfdc7b00cf821f9a5e"></a>
<a id="astructfd__op__vtable_html_a48338a129571b7c76abc4a1b5a6372af"></a>
<a id="astructfd__op__vtable_html_a6748a61747f3ffd0c16174e5ad6d9829"></a>
<a id="astructfd__op__vtable_html_a80704417dfe01e8289d1f7fca819f5f1"></a>
<a id="astructfd__op__vtable_html_a8caad0c1e96cdb67ef02f918ab8aff17"></a>
<a id="astructfd__op__vtable_html_ac59ee326ff54a6a2324bf3425f4a3d5a"></a>
<a id="astructfd__op__vtable_html_aff079f05422413a0df3394ddfecc0298"></a>
<a id="astructk__condvar_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructtimespec_html"></a>
<a id="astructzvfs__fd__set_html"></a>
<a id="astructzvfs__fd__set_html_aa057869d6cee9109890d42f74c84fe19"></a>
<a id="astructzvfs__pollfd_html"></a>
<a id="astructzvfs__pollfd_html_a1e2a42fca725be5059d51817b2caaeb9"></a>
<a id="astructzvfs__pollfd_html_ab13e3da1e537937e487c99aa385c3265"></a>
<a id="astructzvfs__pollfd_html_af249cde934b4e7f620d0724c89ac7000"></a>
<a id="astructzvfs__stat_html"></a>
<a id="astructzvfs__stat_html_a24a28a774b55ce0a335ca58539a94877"></a>
<a id="astructzvfs__stat_html_a2e1288c3dd903b7200d9d8dba07454f4"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2018 Linaro Limited
 * Copyright (c) 2025 Antmicro
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_SYS_FDTABLE_H_
#define ZEPHYR_INCLUDE_SYS_FDTABLE_H_

#include <stdarg.h>
#include <time.h>

/* FIXME: For native_posix ssize_t, off_t. */
#include <sys/types.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/util.h>

#ifdef CONFIG_PICOLIBC
#define ZVFS_O_APPEND 0x0400
#define ZVFS_O_CREAT  0x0040
#define ZVFS_O_TRUNC  0x0200
#else
#define ZVFS_O_APPEND 0x0008
#define ZVFS_O_CREAT  0x0200
#define ZVFS_O_TRUNC  0x0400
#endif

#define ZVFS_O_RDONLY 00
#define ZVFS_O_WRONLY 01
#define ZVFS_O_RDWR   02

#define ZVFS_O_EXCL     0x0800
#define ZVFS_O_NONBLOCK 0x4000

#define ZVFS_F_DUPFD 0
#define ZVFS_F_GETFL 3
#define ZVFS_F_SETFL 4

/* File mode bits */
#define ZVFS_MODE_IFMT   0170000
#define ZVFS_MODE_UNSPEC 0000000
#define ZVFS_MODE_IFIFO  0010000
#define ZVFS_MODE_IFCHR  0020000
#define ZVFS_MODE_IMSGQ  0030000
#define ZVFS_MODE_IFDIR  0040000
#define ZVFS_MODE_IFSEM  0050000
#define ZVFS_MODE_IFBLK  0060000
#define ZVFS_MODE_IFSHM  0070000
#define ZVFS_MODE_IFREG  0100000
#define ZVFS_MODE_IFLNK  0120000
#define ZVFS_MODE_IFSOCK 0140000

#define ZVFS_POLLIN   BIT(0)
#define ZVFS_POLLPRI  BIT(1)
#define ZVFS_POLLOUT  BIT(2)
#define ZVFS_POLLERR  BIT(3)
#define ZVFS_POLLHUP  BIT(4)
#define ZVFS_POLLNVAL BIT(5)

/* FIXME: use k_off_t and k_ssize_t to avoid the POSIX->Zephyr->POSIX dependency cycle */
#ifdef CONFIG_NEWLIB_LIBC
#ifndef _OFF_T_DECLARED
typedef __off_t off_t;
#define _OFF_T_DECLARED
#endif
#ifndef _SSIZE_T_DECLARED
typedef _ssize_t ssize_t;
#define _SSIZE_T_DECLARED
#endif
#endif

#include <zephyr/fs/fs.h>

#ifdef __cplusplus
extern "C" {
#endif

struct fd_op_vtable {
        union {
                ssize_t (*read)(void *obj, void *buf, size_t sz);
                ssize_t (*read_offs)(void *obj, void *buf, size_t sz, size_t offset);
        };
        union {
                ssize_t (*write)(void *obj, const void *buf, size_t sz);
                ssize_t (*write_offs)(void *obj, const void *buf, size_t sz, size_t offset);
        };
        union {
                int (*close)(void *obj);
                int (*close2)(void *obj, int fd);
        };
        int (*ioctl)(void *obj, unsigned int request, va_list args);
};


/* Called by zvfs_close() for every ZVFS_MODE_IFSOCK descriptor, implemented by the socket layer. */
#if defined(CONFIG_NET_SOCKETS)
void zvfs_socket_close_hook(int fd);
#else
static inline void zvfs_socket_close_hook(int fd)
{
        ARG_UNUSED(fd);
}
#endif /* CONFIG_NET_SOCKETS */


int zvfs_reserve_fd(void);

void zvfs_finalize_typed_fd(int fd, void *obj, const struct fd_op_vtable *vtable, uint32_t mode);

static inline void zvfs_finalize_fd(int fd, void *obj, const struct fd_op_vtable *vtable)
{
        zvfs_finalize_typed_fd(fd, obj, vtable, ZVFS_MODE_UNSPEC);
}

int zvfs_alloc_fd(void *obj, const struct fd_op_vtable *vtable);

void zvfs_free_fd(int fd);

void *zvfs_get_fd_obj(int fd, const struct fd_op_vtable *vtable, int err);

void *zvfs_get_fd_obj_and_vtable(int fd, const struct fd_op_vtable **vtable,
                              struct k_mutex **lock);

bool zvfs_get_obj_lock_and_cond(void *obj, const struct fd_op_vtable *vtable, struct k_mutex **lock,
                             struct k_condvar **cond);

static inline int zvfs_fdtable_call_ioctl(const struct fd_op_vtable *vtable, void *obj,
                                       unsigned long request, ...)
{
        va_list args;
        int res;

        va_start(args, request);
        res = vtable->ioctl(obj, request, args);
        va_end(args);

        return res;
}

struct zvfs_stat {
        off_t size;
        uint32_t mode;
};

struct zvfs_pollfd {
        int fd;
        short events;
        short revents;
};

__syscall int zvfs_poll(struct zvfs_pollfd *fds, int nfds, int poll_timeout);

struct zvfs_fd_set {
#ifdef ZVFS_OPEN_SIZE
        uint32_t bitset[DIV_ROUND_UP(ZVFS_OPEN_SIZE, 32)];
#else
        uint32_t bitset[1];
#endif
};

#define ZVFS_FD_SETSIZE (sizeof(((struct zvfs_fd_set *)0)->bitset) * 8)

void ZVFS_FD_CLR(int fd, struct zvfs_fd_set *fdset);
int ZVFS_FD_ISSET(int fd, struct zvfs_fd_set *fdset);
void ZVFS_FD_SET(int fd, struct zvfs_fd_set *fdset);
void ZVFS_FD_ZERO(struct zvfs_fd_set *fdset);

__syscall int zvfs_select(int nfds, struct zvfs_fd_set *ZRESTRICT readfds,
                          struct zvfs_fd_set *ZRESTRICT writefds,
                          struct zvfs_fd_set *ZRESTRICT errorfds,
                          const struct timespec *ZRESTRICT timeout, const void *ZRESTRICT sigmask);

enum {
        /* Codes below 0x100 are reserved for fcntl() codes. */
        ZFD_IOCTL_FSYNC = 0x100,
        ZFD_IOCTL_LSEEK,
        ZFD_IOCTL_POLL_PREPARE,
        ZFD_IOCTL_POLL_UPDATE,
        ZFD_IOCTL_POLL_OFFLOAD,
        ZFD_IOCTL_SET_LOCK,
        ZFD_IOCTL_STAT,
        ZFD_IOCTL_TRUNCATE,
        ZFD_IOCTL_MMAP,

        /* Codes above 0x5400 and below 0x5500 are reserved for termios, FIO, etc */
        ZFD_IOCTL_FIONREAD = 0x541B,
        ZFD_IOCTL_FIONBIO = 0x5421,
        ZFD_IOCTL_FIONWRITE = 0x5411,
};

int zvfs_open(const char *name, int flags, struct fd_op_vtable *vtable);

int zvfs_fstat(int fd, struct zvfs_stat *buf);

int zvfs_close(int fd);

ssize_t zvfs_read(int fd, void *buf, size_t sz, const size_t *from_offset);

ssize_t zvfs_write(int fd, const void *buf, size_t sz, const size_t *from_offset);

#ifdef CONFIG_ZVFS_DEFAULT_FILE_VMETHODS
int zvfs_ioctl_vmeth(void *obj, unsigned int request, va_list args);
int zvfs_close_vmeth(void *obj);
ssize_t zvfs_write_vmeth(void *obj, const void *buffer, size_t count);
ssize_t zvfs_read_vmeth(void *obj, void *buffer, size_t count);
#endif

int zvfs_unlink(const char *path);

int zvfs_rename(const char *old, const char *newp);

#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/fdtable.h>

#endif /* ZEPHYR_INCLUDE_SYS_FDTABLE_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Linaro Limited。

版权（Copyright）：© 2025 Antmicro。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 13 行

待修复（FIXME）：用于 native_posix 的 `ssize_t`、`off_t`。

### 注释 3：原第 39 行

文件模式位（File Mode Bits）。

### 注释 4：原第 60 行

待修复（FIXME）：使用 `k_off_t` 和 `k_ssize_t`，避免 POSIX → Zephyr → POSIX 的循环依赖（Dependency Cycle）。

### 注释 5：原第 100 行

`zvfs_close()` 会针对每个 `ZVFS_MODE_IFSOCK` 描述符（Descriptor）调用此函数，其实现位于套接字层（Socket Layer）。

### 注释 6：原第 108 行

条件编译配置（Configuration）标记：`CONFIG_NET_SOCKETS`。

### 注释 7：原第 303 行

小于 `0x100` 的代码值保留给 `fcntl()`。

### 注释 8：原第 314 行

大于 `0x5400` 且小于 `0x5500` 的代码值保留给 termios、FIO 等。

### 注释 9：原第 411 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SYS_FDTABLE_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html)
- [sys/types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [zephyr/fs/fs.h](../storage/P077_文件系统公共头文件.md)
- [fd_op_vtable](../posix_system_model_reference/P002_fd_op_vtable_结构体.md)
- [read](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#a8caad0c1e96cdb67ef02f918ab8aff17)
- [read_offs](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#a6748a61747f3ffd0c16174e5ad6d9829)
- [write](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#ac59ee326ff54a6a2324bf3425f4a3d5a)
- [write_offs](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#a48338a129571b7c76abc4a1b5a6372af)
- [close](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#a80704417dfe01e8289d1f7fca819f5f1)
- [close2](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#a139c24a21d141ccfdc7b00cf821f9a5e)
- [ioctl](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#aff079f05422413a0df3394ddfecc0298)
- [zvfs_reserve_fd](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a0805f751464ff9a51a463841ce35ff5f)
- [zvfs_finalize_typed_fd](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a448172e130af96c11af2fe6511e6b262)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zvfs_finalize_fd](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a0bb7c530d69c9e5b1cfc61e7a11441af)
- [ZVFS_MODE_UNSPEC](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a4696b5a4cecb531946d2f5b2ecd8b8ff)
- [zvfs_alloc_fd](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a0248f37e9b8cfc0a76ced956b75a3ed2)
- [zvfs_free_fd](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a5cedc4a2f8375d103238d611f6ed3422)
- [zvfs_get_fd_obj](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a8655ab5d3b0776f27eb67d53ef8a431b)
- [zvfs_get_fd_obj_and_vtable](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a0b8c1eeb3ff253e45d45752b77679e17)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [zvfs_get_obj_lock_and_cond](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a54e1f1cbd983631903757a93997c3fab)
- [k_condvar](../synchronization_reference/P011_内核条件变量结构.md)
- [zvfs_fdtable_call_ioctl](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a78c25e35ddacd2d4287cc24acf4126cc)
- [zvfs_stat](../posix_system_model_reference/P034_zvfs_stat_结构体.md)
- [size](../posix_system_model_reference/P034_zvfs_stat_结构体.md#a2e1288c3dd903b7200d9d8dba07454f4)
- [mode](../posix_system_model_reference/P034_zvfs_stat_结构体.md#a24a28a774b55ce0a335ca58539a94877)
- [zvfs_pollfd](../posix_system_model_reference/P033_zvfs_pollfd_结构体.md)
- [fd](../posix_system_model_reference/P033_zvfs_pollfd_结构体.md#af249cde934b4e7f620d0724c89ac7000)
- [events](../posix_system_model_reference/P033_zvfs_pollfd_结构体.md#a1e2a42fca725be5059d51817b2caaeb9)
- [revents](../posix_system_model_reference/P033_zvfs_pollfd_结构体.md#ab13e3da1e537937e487c99aa385c3265)
- [zvfs_poll](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a1a758fb84d99d0390b6a8d51ec7cda34)
- [zvfs_fd_set](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md)
- [bitset](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md#aa057869d6cee9109890d42f74c84fe19)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [ZVFS_FD_CLR](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a029809dfde96846d9e7871e252d74546)
- [ZVFS_FD_ISSET](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a84f63f19ea89e5711725f4d753b5484c)
- [ZVFS_FD_SET](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#afa48d92e5f545412139f567a19e01f71)
- [ZVFS_FD_ZERO](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a46ae4a3ac3d192de02fb1b6c4a4e95ac)
- [zvfs_select](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a8ced1fc0adbdf35b71ec486a8ec68665)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [ZFD_IOCTL_FSYNC](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4)
- [ZFD_IOCTL_LSEEK](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072)
- [ZFD_IOCTL_POLL_PREPARE](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e)
- [ZFD_IOCTL_POLL_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa)
- [ZFD_IOCTL_POLL_OFFLOAD](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe)
- [ZFD_IOCTL_SET_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62)
- [ZFD_IOCTL_STAT](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20ac43f1468ea5c3e2124c415aae4f7402c)
- [ZFD_IOCTL_TRUNCATE](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20aaccc19cb18dff80fd30127ff14a296e5)
- [ZFD_IOCTL_MMAP](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20ad0d133771395d2ed7d1d6adcf203376f)
- [ZFD_IOCTL_FIONREAD](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683)
- [ZFD_IOCTL_FIONBIO](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530)
- [ZFD_IOCTL_FIONWRITE](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a1e88b6e9ca6cf0db43029f485af43ccb)
- [zvfs_open](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a382577239f3941d357d313b38464c954)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zvfs_fstat](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a2ae009f516139ac12492a15bb1a31f97)
- [zvfs_close](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a24bf5bb71435e4921e051d115bf7b7db)
- [zvfs_read](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a8a5a70692eb13de80858e976c4ae5004)
- [zvfs_write](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a23e688ef88dd22d2350e790b44dbf28f)
- [zvfs_unlink](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a72815fac0eac70fa60d2a25a4aa4908d)
- [zvfs_rename](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#a75c63fae34489b6297615de253c87d44)
- [fs.h](../storage/P077_文件系统公共头文件.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [types.h](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md)
- [fd_op_vtable::close2](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#a139c24a21d141ccfdc7b00cf821f9a5e)
- [fd_op_vtable::write_offs](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#a48338a129571b7c76abc4a1b5a6372af)
- [fd_op_vtable::read_offs](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#a6748a61747f3ffd0c16174e5ad6d9829)
- [fd_op_vtable::close](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#a80704417dfe01e8289d1f7fca819f5f1)
- [fd_op_vtable::read](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#a8caad0c1e96cdb67ef02f918ab8aff17)
- [fd_op_vtable::write](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#ac59ee326ff54a6a2324bf3425f4a3d5a)
- [fd_op_vtable::ioctl](../posix_system_model_reference/P002_fd_op_vtable_结构体.md#aff079f05422413a0df3394ddfecc0298)
- [zvfs_fd_set::bitset](../posix_system_model_reference/P032_zvfs_fd_set_结构体.md#aa057869d6cee9109890d42f74c84fe19)
- [zvfs_pollfd::events](../posix_system_model_reference/P033_zvfs_pollfd_结构体.md#a1e2a42fca725be5059d51817b2caaeb9)
- [zvfs_pollfd::revents](../posix_system_model_reference/P033_zvfs_pollfd_结构体.md#ab13e3da1e537937e487c99aa385c3265)
- [zvfs_pollfd::fd](../posix_system_model_reference/P033_zvfs_pollfd_结构体.md#af249cde934b4e7f620d0724c89ac7000)
- [zvfs_stat::mode](../posix_system_model_reference/P034_zvfs_stat_结构体.md#a24a28a774b55ce0a335ca58539a94877)
- [zvfs_stat::size](../posix_system_model_reference/P034_zvfs_stat_结构体.md#a2e1288c3dd903b7200d9d8dba07454f4)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P006_mtch9010.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_ft8xx.h_源码浏览.md)
