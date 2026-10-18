---
id: learning.zephyr-docs.api-source-scheduler-interrupt-reference.page-10
title: stat.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stat_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_stat.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md)。

## 10.1\_原始可见代码（Source Code）

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
<a id="foldopen00057"></a>
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
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
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
<a id="l00160"></a>
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
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
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
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="a__timespec_8h_html_aa17c461cd5eca7fc12a66daa803c7fd7"></a>
<a id="acdefs_8h_html"></a>
<a id="ainclude_2zephyr_2posix_2sys_2time_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_adb8322e115035a284aab704909e63d00"></a>
<a id="aposix__signal_8h_html_afc544433253791fc5f87b8203c9b6e63"></a>
<a id="aposix__types_8h_html"></a>
<a id="aposix__types_8h_html_a0f89a9a6420c24efc5254e10170009e9"></a>
<a id="aposix__types_8h_html_a3a7834be1a79bb0c5a65d3546c2e3bd8"></a>
<a id="aposix__types_8h_html_a50c0d048e63387089a42aaf054a6d05b"></a>
<a id="aposix__types_8h_html_a779f87527fcb00a46d12056b753cf22c"></a>
<a id="aposix__types_8h_html_a952c84a825bb4f319cf55c9afb99ee0e"></a>
<a id="aposix__types_8h_html_aa9a628992e7bcdc59d4fb606baada347"></a>
<a id="astat_8h_html_a0f949e7f97dc8e3e4ea1142cda8be155"></a>
<a id="astat_8h_html_a276d3b2ba668bdc06f78fccc16b956fe"></a>
<a id="astat_8h_html_a2dd9b364b84aee095dc6208ff18de4f5"></a>
<a id="astat_8h_html_a4ce306737c3153a7e2e99272c0a92ec5"></a>
<a id="astat_8h_html_a6a5c46cd35365436fb3bb5e034be78e2"></a>
<a id="astat_8h_html_a90e6dc0189b82ecf0e2da52d74d2a149"></a>
<a id="astat_8h_html_aa0a896031839c30189c42617ebc5aaeb"></a>
<a id="astat_8h_html_acce8c726e07337e0581d74699e2324fe"></a>
<a id="astat_8h_html_aecd62777ab7c6c1d6d23e4967632c5ef"></a>
<a id="astat_8h_html_afa4a4f346213cdc5ae4cfc9aedf7ef2e"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructstat_html"></a>
<a id="astructstat_html_a040e19c8b9766f841fde8786ce9297bf"></a>
<a id="astructstat_html_a0ed9092fa6c77a3251b9b9a4738ef84f"></a>
<a id="astructstat_html_a3715a60e75816e25a52d150e1893af76"></a>
<a id="astructstat_html_a38d474e1ae3cf6fbdde89ac3c3e308f1"></a>
<a id="astructstat_html_a42dd716b2f9234f961d949fc9500eefb"></a>
<a id="astructstat_html_a4a8708a3d18be60ee7b2f06c4cab0c70"></a>
<a id="astructstat_html_a5cbdd829011af82ba61e83773bbcbc7d"></a>
<a id="astructstat_html_a78eca07da5a8a88b1c3dd8be5a32821e"></a>
<a id="astructstat_html_a8447c545451bec2b95f9d67787404934"></a>
<a id="astructstat_html_a8fcf65727b775d92b773776ed1210c8b"></a>
<a id="astructstat_html_a9769ed8f0d4c5a9f329c32bc92479d56"></a>
<a id="astructstat_html_aa61e6c1a8a91c69f1d26f6700a0546cb"></a>
<a id="astructstat_html_ab864f16f436cec370f0ced585d897698"></a>
<a id="astructstat_html_ac5b90090ae323741ae4c9e4f3683a29f"></a>
<a id="astructtimespec_html"></a>

```c
/* SPDX-License-Identifier: BSD-3-Clause */
/*
 * Copyright (c) 1982, 1986, 1993
 * The Regents of the University of California.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the University nor the names of its contributors
 * may be used to endorse or promote products derived from this software
 * without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */
#ifndef ZEPHYR_INCLUDE_POSIX_SYS_STAT_H_
#define ZEPHYR_INCLUDE_POSIX_SYS_STAT_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <time.h>
#include <sys/cdefs.h>

#include <zephyr/posix/posix_types.h>

/* dj's stat defines _STAT_H_ */
#ifndef _STAT_H_

/*
 * It is intended that the layout of this structure not change when the
 * sizes of any of the basic types change (short, int, long) [via a compile
 * time option].
 */

#ifdef __CYGWIN__
#include <cygwin/stat.h>
#ifdef _LIBC
#define stat64 stat
#endif
#else
struct stat {
        dev_t st_dev;
        ino_t st_ino;
        mode_t st_mode;
        nlink_t st_nlink;
        uid_t st_uid;
        gid_t st_gid;
#if defined(__linux) && defined(__x86_64__)
        int __pad0;
#endif
        dev_t st_rdev;
#if defined(__linux) && !defined(__x86_64__)
        unsigned short int __pad2;
#endif
        off_t st_size;
#if defined(__linux)
        blksize_t st_blksize;
        blkcnt_t st_blocks;
        struct timespec st_atim;
        struct timespec st_mtim;
        struct timespec st_ctim;
#define st_atime st_atim.tv_sec /* Backward compatibility */
#define st_mtime st_mtim.tv_sec
#define st_ctime st_ctim.tv_sec
#if defined(__linux) && defined(__x86_64__)
        uint64_t __glibc_reserved[3];
#endif
#else
#if defined(__rtems__)
        struct timespec st_atim;
        struct timespec st_mtim;
        struct timespec st_ctim;
        blksize_t st_blksize;
        blkcnt_t st_blocks;
#else
        /* SysV/sco doesn't have the rest... But Solaris, eabi does.  */
#if defined(__svr4__) && !defined(__PPC__) && !defined(__sun__)
        time_t st_atime;
        time_t st_mtime;
        time_t st_ctime;
#else
        struct timespec st_atim;
        struct timespec st_mtim;
        struct timespec st_ctim;
        blksize_t st_blksize;
        blkcnt_t st_blocks;
#if !defined(__rtems__)
        long st_spare4[2];
#endif
#endif
#endif
#endif
};

#if !(defined(__svr4__) && !defined(__PPC__) && !defined(__sun__))
#define st_atime st_atim.tv_sec
#define st_ctime st_ctim.tv_sec
#define st_mtime st_mtim.tv_sec
#endif

#endif

#define _IFMT   0170000 /* type of file */
#define _IFDIR  0040000 /* directory */
#define _IFCHR  0020000 /* character special */
#define _IFBLK  0060000 /* block special */
#define _IFREG  0100000 /* regular */
#define _IFLNK  0120000 /* symbolic link */
#define _IFSOCK 0140000 /* socket */
#define _IFIFO  0010000 /* fifo */

#define S_BLKSIZE 1024 /* size of a block */

#define S_ISUID 0004000 /* set user id on execution */
#define S_ISGID 0002000 /* set group id on execution */
#define S_ISVTX 0001000 /* save swapped text even after use */
#if __BSD_VISIBLE
#define S_IREAD  0000400 /* read permission, owner */
#define S_IWRITE 0000200 /* write permission, owner */
#define S_IEXEC  0000100 /* execute/search permission, owner */
#define S_ENFMT  0002000 /* enforcement-mode locking */
#endif                   /* !_BSD_VISIBLE */

#define S_IFMT   _IFMT
#define S_IFDIR  _IFDIR
#define S_IFCHR  _IFCHR
#define S_IFBLK  _IFBLK
#define S_IFREG  _IFREG
#define S_IFLNK  _IFLNK
#define S_IFSOCK _IFSOCK
#define S_IFIFO  _IFIFO

#ifdef _WIN32
/*
 * The Windows header files define _S_ forms of these, so we do too
 * for easier portability.
 */
#define _S_IFMT   _IFMT
#define _S_IFDIR  _IFDIR
#define _S_IFCHR  _IFCHR
#define _S_IFIFO  _IFIFO
#define _S_IFREG  _IFREG
#define _S_IREAD  0000400
#define _S_IWRITE 0000200
#define _S_IEXEC  0000100
#endif

#define S_IRWXU (S_IRUSR | S_IWUSR | S_IXUSR)
#define S_IRUSR 0000400 /* read permission, owner */
#define S_IWUSR 0000200 /* write permission, owner */
#define S_IXUSR 0000100 /* execute/search permission, owner */
#define S_IRWXG (S_IRGRP | S_IWGRP | S_IXGRP)
#define S_IRGRP 0000040 /* read permission, group */
#define S_IWGRP 0000020 /* write permission, grougroup */
#define S_IXGRP 0000010 /* execute/search permission, group */
#define S_IRWXO (S_IROTH | S_IWOTH | S_IXOTH)
#define S_IROTH 0000004 /* read permission, other */
#define S_IWOTH 0000002 /* write permission, other */
#define S_IXOTH 0000001 /* execute/search permission, other */

#if __BSD_VISIBLE
#define ACCESSPERMS (S_IRWXU | S_IRWXG | S_IRWXO)                               /* 0777 */
#define ALLPERMS    (S_ISUID | S_ISGID | S_ISVTX | S_IRWXU | S_IRWXG | S_IRWXO) /* 07777 */
#define DEFFILEMODE (S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH) /* 0666 */
#endif

#define S_ISBLK(m)  (((m)&_IFMT) == _IFBLK)
#define S_ISCHR(m)  (((m)&_IFMT) == _IFCHR)
#define S_ISDIR(m)  (((m)&_IFMT) == _IFDIR)
#define S_ISFIFO(m) (((m)&_IFMT) == _IFIFO)
#define S_ISREG(m)  (((m)&_IFMT) == _IFREG)
#define S_ISLNK(m)  (((m)&_IFMT) == _IFLNK)
#define S_ISSOCK(m) (((m)&_IFMT) == _IFSOCK)

#if defined(__CYGWIN__) || defined(__rtems__)
/* Special tv_nsec values for futimens(2) and utimensat(2). */
#define UTIME_NOW  -2L
#define UTIME_OMIT -1L
#endif

int chmod(const char *__path, mode_t __mode);
int fchmod(int __fd, mode_t __mode);
int fstat(int __fd, struct stat *__sbuf);
int mkdir(const char *_path, mode_t __mode);
int mkfifo(const char *__path, mode_t __mode);
int stat(const char *__restrict __path, struct stat *__restrict __sbuf);
mode_t umask(mode_t __mask);

#if defined(__SPU__) || defined(__rtems__) || defined(__CYGWIN__) && !defined(__INSIDE_CYGWIN__)
int lstat(const char *__restrict __path, struct stat *__restrict __buf);
int mknod(const char *__path, mode_t __mode, dev_t __dev);
#endif

#if __ATFILE_VISIBLE && !defined(__INSIDE_CYGWIN__)
int fchmodat(int __fd, const char *__path, mode_t __mode, int __flag);
int fstatat(int __fd, const char *__restrict __path, struct stat *__restrict __buf, int __flag);
int mkdirat(int __fd, const char *__path, mode_t __mode);
int mkfifoat(int __fd, const char *__path, mode_t __mode);
int mknodat(int __fd, const char *__path, mode_t __mode, dev_t __dev);
int utimensat(int __fd, const char *__path, const struct timespec __times[2], int __flag);
#endif
#if __POSIX_VISIBLE >= 200809 && !defined(__INSIDE_CYGWIN__)
int futimens(int __fd, const struct timespec __times[2]);
#endif

/*
 * Provide prototypes for most of the _<systemcall> names that are
 * provided in newlib for some compilers.
 */
#ifdef _LIBC
int _fstat(int __fd, struct stat *__sbuf);
int _stat(const char *__restrict __path, struct stat *__restrict __sbuf);
int _mkdir(const char *_path, mode_t __mode);
#ifdef __LARGE64_FILES
struct stat64;
int _stat64(const char *__restrict __path, struct stat64 *__restrict __sbuf);
int _fstat64(int __fd, struct stat64 *__sbuf);
#endif
#endif

#endif /* !_STAT_H_ */
#ifdef __cplusplus
}
#endif
#endif /* ZEPHYR_INCLUDE_POSIX_SYS_STAT_H_ */
```

## 10.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`BSD-3-Clause`。

### 注释 2：原第 2 行

版权（Copyright）© 1982、1986、1993，加利福尼亚大学董事会（The Regents of the University of California）。保留所有权利。

在满足以下条件的前提下，允许以源码形式或二进制形式再分发和使用本软件，无论是否经过修改：

1. 以源码形式再分发时，必须保留上述版权声明、此条件列表和下述免责声明。
2. 以二进制形式再分发时，必须在随发行版提供的文档和／或其他材料中重现上述版权声明、此条件列表和下述免责声明。
3. 未经事先明确的书面许可，不得使用大学名称或其贡献者姓名，为本软件衍生产品背书或推广。

本软件由董事会及贡献者按“原样”（AS IS）提供，不提供任何明示或默示保证，包括但不限于适销性（Merchantability）和特定用途适用性（Fitness for a Particular Purpose）的默示保证。无论损害如何产生，也无论基于何种责任理论，包括合同、严格责任或侵权行为（含疏忽或其他情形），董事会及贡献者在任何情况下均不对因使用本软件而以任何方式产生的直接、间接、附带、特殊、惩戒性或后果性损害承担责任；这些损害包括但不限于采购替代商品或服务、使用损失、数据或利润损失，以及业务中断，即使已被告知可能发生此类损害，亦不承担责任。

### 注释 3：原第 42 行

dj 的 `stat` 定义了 `_STAT_H_`。

### 注释 4：原第 45 行

设计目标是：即使通过编译时选项改变任何基本类型（`short`、`int`、`long`）的大小，此结构体布局（Structure Layout）也保持不变。

### 注释 5：原第 78 行

向后兼容（Backward Compatibility）。

### 注释 6：原第 92 行

SysV/sco 没有余下这些内容，但 Solaris 和 eabi 有。

### 注释 7：原第 119 行

文件类型（File Type）。

### 注释 8：原第 120 行

目录（Directory）。

### 注释 9：原第 121 行

字符特殊文件（Character Special File）。

### 注释 10：原第 122 行

块特殊文件（Block Special File）。

### 注释 11：原第 123 行

普通文件（Regular File）。

### 注释 12：原第 124 行

符号链接（Symbolic Link）。

### 注释 13：原第 125 行

套接字（Socket）。

### 注释 14：原第 126 行

先进先出管道（FIFO）。

### 注释 15：原第 128 行

块大小（Block Size）。

### 注释 16：原第 130 行

执行时设置用户标识（Set User ID on Execution）。

### 注释 17：原第 131 行

执行时设置组标识（Set Group ID on Execution）。

### 注释 18：原第 132 行

使用结束后仍保留换出的正文段（Save Swapped Text Even After Use）。

### 注释 19：原第 134 行

所有者读取权限（Owner Read Permission）。

### 注释 20：原第 135 行

所有者写入权限（Owner Write Permission）。

### 注释 21：原第 136 行

所有者执行／搜索权限（Owner Execute/Search Permission）。

### 注释 22：原第 137 行

强制模式锁定（Enforcement-mode Locking）。

### 注释 23：原第 138 行

条件编译标记：`!_BSD_VISIBLE`。

### 注释 24：原第 150 行

Windows 头文件为这些标识定义了 `_S_` 形式，因此这里也这样定义，以便移植（Portability）。

### 注释 25：原第 165 行

所有者读取权限（Owner Read Permission）。

### 注释 26：原第 166 行

所有者写入权限（Owner Write Permission）。

### 注释 27：原第 167 行

所有者执行／搜索权限（Owner Execute/Search Permission）。

### 注释 28：原第 169 行

所属组读取权限（Group Read Permission）。

### 注释 29：原第 170 行

所属组写入权限（Group Write Permission）。

### 注释 30：原第 171 行

所属组执行／搜索权限（Group Execute/Search Permission）。

### 注释 31：原第 173 行

其他用户读取权限（Other Read Permission）。

### 注释 32：原第 174 行

其他用户写入权限（Other Write Permission）。

### 注释 33：原第 175 行

其他用户执行／搜索权限（Other Execute/Search Permission）。

### 注释 34：原第 178 行

八进制权限值 `0777`。

### 注释 35：原第 179 行

八进制权限值 `07777`。

### 注释 36：原第 180 行

八进制权限值 `0666`。

### 注释 37：原第 192 行

`futimens(2)` 和 `utimensat(2)` 使用的特殊 `tv_nsec` 值。

### 注释 38：原第 222 行

为多数 `_<systemcall>` 名称提供函数原型（Prototypes）；某些编译器使用的 newlib 提供这些名称。

### 注释 39：原第 237 行

条件编译标记：`!_STAT_H_`。

### 注释 40：原第 241 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_SYS_STAT_H_`。

## 10.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md)
- [time.h](../api_file_reference/P159_zephyr__posix__sys__time.h_文件参考.md)
- [sys/cdefs.h](../api_file_reference/P033_____w__zephyr__zephyr__lib__libc__minimal__include__sys__cdefs.h_文件参考.md)
- [zephyr/posix/posix_types.h](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md)
- [stat](../posix_system_model_reference/P022_stat_结构体.md)
- [dev_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a0f89a9a6420c24efc5254e10170009e9)
- [st_dev](../posix_system_model_reference/P022_stat_结构体.md#ac5b90090ae323741ae4c9e4f3683a29f)
- [ino_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a779f87527fcb00a46d12056b753cf22c)
- [st_ino](../posix_system_model_reference/P022_stat_结构体.md#a9769ed8f0d4c5a9f329c32bc92479d56)
- [mode_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#adb8322e115035a284aab704909e63d00)
- [st_mode](../posix_system_model_reference/P022_stat_结构体.md#a5cbdd829011af82ba61e83773bbcbc7d)
- [nlink_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a952c84a825bb4f319cf55c9afb99ee0e)
- [st_nlink](../posix_system_model_reference/P022_stat_结构体.md#a0ed9092fa6c77a3251b9b9a4738ef84f)
- [uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)
- [st_uid](../posix_system_model_reference/P022_stat_结构体.md#a4a8708a3d18be60ee7b2f06c4cab0c70)
- [gid_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a3a7834be1a79bb0c5a65d3546c2e3bd8)
- [st_gid](../posix_system_model_reference/P022_stat_结构体.md#ab864f16f436cec370f0ced585d897698)
- [st_rdev](../posix_system_model_reference/P022_stat_结构体.md#aa61e6c1a8a91c69f1d26f6700a0546cb)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [st_size](../posix_system_model_reference/P022_stat_结构体.md#a040e19c8b9766f841fde8786ce9297bf)
- [blksize_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a50c0d048e63387089a42aaf054a6d05b)
- [st_blksize](../posix_system_model_reference/P022_stat_结构体.md#a38d474e1ae3cf6fbdde89ac3c3e308f1)
- [blkcnt_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#aa9a628992e7bcdc59d4fb606baada347)
- [st_blocks](../posix_system_model_reference/P022_stat_结构体.md#a42dd716b2f9234f961d949fc9500eefb)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [st_atim](../posix_system_model_reference/P022_stat_结构体.md#a8447c545451bec2b95f9d67787404934)
- [st_mtim](../posix_system_model_reference/P022_stat_结构体.md#a78eca07da5a8a88b1c3dd8be5a32821e)
- [st_ctim](../posix_system_model_reference/P022_stat_结构体.md#a8fcf65727b775d92b773776ed1210c8b)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [st_atime](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md#a4ce306737c3153a7e2e99272c0a92ec5)
- [st_mtime](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md#aecd62777ab7c6c1d6d23e4967632c5ef)
- [st_ctime](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md#a2dd9b364b84aee095dc6208ff18de4f5)
- [st_spare4](../posix_system_model_reference/P022_stat_结构体.md#a3715a60e75816e25a52d150e1893af76)
- [chmod](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md#aa0a896031839c30189c42617ebc5aaeb)
- [fchmod](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md#a6a5c46cd35365436fb3bb5e034be78e2)
- [fstat](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md#a276d3b2ba668bdc06f78fccc16b956fe)
- [mkdir](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md#afa4a4f346213cdc5ae4cfc9aedf7ef2e)
- [mkfifo](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md#acce8c726e07337e0581d74699e2324fe)
- [stat](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md#a0f949e7f97dc8e3e4ea1142cda8be155)
- [umask](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md#a90e6dc0189b82ecf0e2da52d74d2a149)
- [cdefs.h](../api_file_reference/P033_____w__zephyr__zephyr__lib__libc__minimal__include__sys__cdefs.h_文件参考.md)
- [posix_types.h](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md)
- [stat::st_size](../posix_system_model_reference/P022_stat_结构体.md#a040e19c8b9766f841fde8786ce9297bf)
- [stat::st_nlink](../posix_system_model_reference/P022_stat_结构体.md#a0ed9092fa6c77a3251b9b9a4738ef84f)
- [stat::st_spare4](../posix_system_model_reference/P022_stat_结构体.md#a3715a60e75816e25a52d150e1893af76)
- [stat::st_blksize](../posix_system_model_reference/P022_stat_结构体.md#a38d474e1ae3cf6fbdde89ac3c3e308f1)
- [stat::st_blocks](../posix_system_model_reference/P022_stat_结构体.md#a42dd716b2f9234f961d949fc9500eefb)
- [stat::st_uid](../posix_system_model_reference/P022_stat_结构体.md#a4a8708a3d18be60ee7b2f06c4cab0c70)
- [stat::st_mode](../posix_system_model_reference/P022_stat_结构体.md#a5cbdd829011af82ba61e83773bbcbc7d)
- [stat::st_mtim](../posix_system_model_reference/P022_stat_结构体.md#a78eca07da5a8a88b1c3dd8be5a32821e)
- [stat::st_atim](../posix_system_model_reference/P022_stat_结构体.md#a8447c545451bec2b95f9d67787404934)
- [stat::st_ctim](../posix_system_model_reference/P022_stat_结构体.md#a8fcf65727b775d92b773776ed1210c8b)
- [stat::st_ino](../posix_system_model_reference/P022_stat_结构体.md#a9769ed8f0d4c5a9f329c32bc92479d56)
- [stat::st_rdev](../posix_system_model_reference/P022_stat_结构体.md#aa61e6c1a8a91c69f1d26f6700a0546cb)
- [stat::st_gid](../posix_system_model_reference/P022_stat_结构体.md#ab864f16f436cec370f0ced585d897698)
- [stat::st_dev](../posix_system_model_reference/P022_stat_结构体.md#ac5b90090ae323741ae4c9e4f3683a29f)

---

[上一章](P009_renesas_rzv_clock.h_源码浏览.md) · [返回大纲](大纲.md)
