---
id: learning.zephyr-docs.portability.page-15
title: POSIX选项与选项组
kind: reference
status: maintained
domains: [zephyr, portability, cmsis]
source_url: https://docs.zephyrproject.org/latest/services/portability/posix/option_groups/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_POSIX选项与选项组

原文：[官方页面](https://docs.zephyrproject.org/latest/services/portability/posix/option_groups/index.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

译注：以下逐项翻译原页的选项与选项组说明，保留所有接口行和空白支持状态。表中“支持（yes）”后若有 †，还必须阅读相关限制；符号可链接不等于功能可用。† 的定义见[符合性说明](P012_POSIX符合性.md#posix-undefined-behaviour)。


## 15.1\_POSIX 选项组（Option Groups）

### 15.1.1\_同步屏障（Barriers） · `POSIX_BARRIERS`

通过 [`CONFIG_POSIX_BARRIERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_BARRIERS) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pthread_barrier_destroy() | 支持（yes） |
| pthread_barrier_init() | 支持（yes） |
| pthread_barrier_wait() | 支持（yes） |
| pthread_barrierattr_destroy() | 支持（yes） |
| pthread_barrierattr_init() | 支持（yes） |

### 15.1.2\_C 语言非局部跳转（Non-Local Jump） · `POSIX_C_LANG_JUMP`

`POSIX_C_LANG_JUMP` 选项组包含在 ISO C 标准中。

注意（Note）：

使用 Newlib、Picolibc 或其他符合 ISO C 标准的 C 库时，认为 `POSIX_C_LANG_JUMP` 选项组受到支持。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| setjmp() | 支持（yes） |
| longjmp() | 支持（yes） |

### 15.1.3\_C 语言数学功能（Math） · `POSIX_C_LANG_MATH`

`POSIX_C_LANG_MATH` 选项组包含在 ISO C 标准中。

注意（Note）：

使用 Newlib、Picolibc 或其他符合 ISO C 标准的 C 库时，认为 `POSIX_C_LANG_MATH` 选项组受到支持。

`POSIX_C_LANG_MATH` 选项组详情见 [子规范划分注意事项（Subprofiling Considerations）](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

### 15.1.4\_C 语言支持（C Language Support） · `POSIX_C_LANG_SUPPORT`

`POSIX_C_LANG_SUPPORT` 选项组包含通用 ISO C 库。

注意（Note）：

使用 Newlib、Picolibc 或其他符合 ISO C 标准的 C 库时，认为整个 `POSIX_C_LANG_SUPPORT` 选项组受到支持。

`POSIX_C_LANG_SUPPORT` 选项组详情见 [子规范划分注意事项（Subprofiling Considerations）](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

使用 C 语言开发 Zephyr 应用的更多信息，见 [C 语言支持说明](../languages/P001_语言支持入口.md#language-support)。

### 15.1.5\_C 库可重入接口（Reentrant Functions） · `POSIX_C_LANG_SUPPORT_R`

通过 [`CONFIG_POSIX_C_LANG_SUPPORT_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_C_LANG_SUPPORT_R) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| asctime_r() | 支持（yes） |
| ctime_r() | 支持（yes） |
| gmtime_r() | 支持（yes） |
| localtime_r() | 支持（yes） |
| rand_r() | 支持（yes） |
| strerror_r() | 支持（yes） |
| strtok_r() | 支持（yes） |

### 15.1.6\_C 库扩展（C Library Extensions） · `POSIX_C_LIB_EXT`

通过 [`CONFIG_POSIX_C_LIB_EXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_C_LIB_EXT) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| fnmatch() | 支持（yes） |
| getopt() | 支持（yes） |
| getsubopt() |  |
| optarg | 支持（yes） |
| opterr | 支持（yes） |
| optind | 支持（yes） |
| optopt | 支持（yes） |
| stpcpy() |  |
| stpncpy() |  |
| strcasecmp() |  |
| strdup() |  |
| strfmon() |  |
| strncasecmp() | 支持（yes） |
| strndup() |  |
| strnlen() | 支持（yes） |

### 15.1.7\_时钟选择（Clock Selection） · `POSIX_CLOCK_SELECTION`

通过 [`CONFIG_POSIX_CLOCK_SELECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_CLOCK_SELECTION) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pthread_condattr_getclock() | 支持（yes） |
| pthread_condattr_setclock() | 支持（yes） |
| clock_nanosleep() | 支持（yes） |

### 15.1.8\_设备输入输出（Device I/O） · `POSIX_DEVICE_IO`

通过 [`CONFIG_POSIX_DEVICE_IO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_DEVICE_IO) 启用此选项组。

注意（Note）：

使用 Newlib、Picolibc 或其他符合 ISO C 标准的 C 库时，认为 `POSIX_DEVICE_IO` 选项组中的 C89 部分受到支持。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| FD_CLR() | 支持（yes） |
| FD_ISSET() | 支持（yes） |
| FD_SET() | 支持（yes） |
| FD_ZERO() | 支持（yes） |
| clearerr() | 支持（yes） |
| close() | 支持（yes） |
| fclose() | 支持（yes） |
| fdopen() | 支持（yes） |
| feof() | 支持（yes） |
| ferror() | 支持（yes） |
| fflush() | 支持（yes） |
| fgetc() | 支持（yes） |
| fgets() | 支持（yes） |
| fileno() | 支持（yes） |
| fopen() | 支持（yes） |
| fprintf() | 支持（yes） |
| fputc() | 支持（yes） |
| fputs() | 支持（yes） |
| fread() | 支持（yes） |
| freopen() | 支持（yes） |
| fscanf() | 支持（yes） |
| fwrite() | 支持（yes） |
| getc() | 支持（yes） |
| getchar() | 支持（yes） |
| gets() | 支持（yes） |
| open() | 支持（yes） |
| perror() | 支持（yes） |
| poll() | 支持（yes） |
| printf() | 支持（yes） |
| pread() | 支持（yes） |
| pselect() | 支持（yes） |
| putc() | 支持（yes） |
| putchar() | 支持（yes） |
| puts() | 支持（yes） |
| pwrite() | 支持（yes） |
| read() | 支持（yes） |
| scanf() | 支持（yes） |
| select() | 支持（yes） |
| setbuf() | 支持（yes） |
| setvbuf() | 支持（yes） |
| stderr | 支持（yes） |
| stdin | 支持（yes） |
| stdout | 支持（yes） |
| ungetc() | 支持（yes） |
| vfprintf() | 支持（yes） |
| vfscanf() | 支持（yes） |
| vprintf() | 支持（yes） |
| vscanf() | 支持（yes） |
| write() | 支持（yes） |

### 15.1.9\_文件描述符管理（File Descriptor Management） · `POSIX_FD_MGMT`

通过 [`CONFIG_POSIX_FD_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_FD_MGMT) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| dup() |  |
| dup2() |  |
| fcntl() |  |
| fgetpos() |  |
| fseek() |  |
| fseeko() |  |
| fsetpos() |  |
| ftell() |  |
| ftello() |  |
| ftruncate() | 支持（yes） |
| lseek() |  |
| rewind() |  |

### 15.1.10\_文件锁定（File Locking） · `POSIX_FILE_LOCKING`

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| flockfile() |  |
| ftrylockfile() |  |
| funlockfile() |  |
| getc_unlocked() |  |
| getchar_unlocked() |  |
| putc_unlocked() |  |
| putchar_unlocked() |  |

### 15.1.11\_文件系统（File System） · `POSIX_FILE_SYSTEM`

通过 [`CONFIG_POSIX_FILE_SYSTEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_FILE_SYSTEM) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| access() |  |
| chdir() |  |
| closedir() | 支持（yes） |
| creat() |  |
| fchdir() |  |
| fpathconf() |  |
| fstat() | 支持（yes） |
| fstatvfs() |  |
| getcwd() |  |
| link() |  |
| mkdir() | 支持（yes） |
| mkstemp() |  |
| opendir() | 支持（yes） |
| pathconf() |  |
| readdir() | 支持（yes） |
| remove() | 支持（yes） |
| rename() | 支持（yes） |
| rewinddir() |  |
| rmdir() | 支持（yes） |
| stat() | 支持（yes） |
| statvfs() |  |
| tmpfile() |  |
| tmpnam() |  |
| truncate() |  |
| unlink() | 支持（yes） |
| utime() |  |

### 15.1.12\_文件系统可重入接口（Reentrant File-System Functions） · `POSIX_FILE_SYSTEM_R`

通过 [`CONFIG_POSIX_FILE_SYSTEM_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_FILE_SYSTEM_R) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| readdir_r() | 支持（yes） |

### 15.1.13\_文件映射（Mapped Files） · `POSIX_MAPPED_FILES`

通过 [`CONFIG_POSIX_MAPPED_FILES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MAPPED_FILES) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| mmap() | 支持（yes） |
| msync() | 支持（yes） |
| munmap() | 支持（yes） |

### 15.1.14\_内存保护（Memory Protection） · `POSIX_MEMORY_PROTECTION`

通过 [`CONFIG_POSIX_MEMORY_PROTECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MEMORY_PROTECTION) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| mprotect() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |

### 15.1.15\_多进程（Multiple Processes） · `POSIX_MULTI_PROCESS`

通过 [`CONFIG_POSIX_MULTI_PROCESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MULTI_PROCESS) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| _Exit() | 支持（yes） |
| _exit() | 支持（yes） |
| assert() | 支持（yes） |
| atexit() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| clock() |  |
| execl() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| execle() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| execlp() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| execv() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| execve() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| execvp() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| exit() | 支持（yes） |
| fork() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| getpgrp() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| getpgid() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| getpid() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| getppid() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| getsid() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| setsid() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| sleep() | 支持（yes） |
| times() |  |
| wait() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| waitid() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| waitpid() | [†](P012_POSIX符合性.md#posix-undefined-behaviour) |

### 15.1.16\_网络（Networking） · `POSIX_NETWORKING`

`sockatmark()` 尚不受支持，预期调用失败并将 `errno` 设为 `ENOSYS` †。

通过 [`CONFIG_POSIX_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_NETWORKING) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| accept() | 支持（yes） |
| bind() | 支持（yes） |
| connect() | 支持（yes） |
| endhostent() | 支持（yes） |
| endnetent() | 支持（yes） |
| endprotoent() | 支持（yes） |
| endservent() | 支持（yes） |
| freeaddrinfo() | 支持（yes） |
| gai_strerror() | 支持（yes） |
| getaddrinfo() | 支持（yes） |
| gethostent() | 支持（yes） |
| gethostname() | 支持（yes） |
| getnameinfo() | 支持（yes） |
| getnetbyaddr() | 支持（yes） |
| getnetbyname() | 支持（yes） |
| getnetent() | 支持（yes） |
| getpeername() | 支持（yes） |
| getprotobyname() | 支持（yes） |
| getprotobynumber() | 支持（yes） |
| getprotoent() | 支持（yes） |
| getservbyname() | 支持（yes） |
| getservbyport() | 支持（yes） |
| getservent() | 支持（yes） |
| getsockname() | 支持（yes） |
| getsockopt() | 支持（yes） |
| htonl() | 支持（yes） |
| htons() | 支持（yes） |
| if_freenameindex() | 支持（yes） |
| if_indextoname() | 支持（yes） |
| if_nameindex() | 支持（yes） |
| if_nametoindex() | 支持（yes） |
| inet_addr() | 支持（yes） |
| inet_ntoa() | 支持（yes） |
| inet_ntop() | 支持（yes） |
| inet_pton() | 支持（yes） |
| listen() | 支持（yes） |
| ntohl() | 支持（yes） |
| ntohs() | 支持（yes） |
| recv() | 支持（yes） |
| recvfrom() | 支持（yes） |
| recvmsg() | 支持（yes） |
| send() | 支持（yes） |
| sendmsg() | 支持（yes） |
| sendto() | 支持（yes） |
| sethostent() | 支持（yes） |
| setnetent() | 支持（yes） |
| setprotoent() | 支持（yes） |
| setservent() | 支持（yes） |
| setsockopt() | 支持（yes） |
| shutdown() | 支持（yes） |
| socket() | 支持（yes） |
| sockatmark() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| socketpair() | 支持（yes） |

### 15.1.17\_管道（Pipe） · `POSIX_PIPE`

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pipe() |  |

### 15.1.18\_实时信号（Realtime Signals） · `POSIX_REALTIME_SIGNALS`

通过 [`CONFIG_POSIX_REALTIME_SIGNALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_REALTIME_SIGNALS) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| sigqueue() |  |
| sigtimedwait() |  |
| sigwaitinfo() |  |

### 15.1.19\_读写锁（Read-Write Locks） · `POSIX_RW_LOCKS`

通过 [`CONFIG_POSIX_RW_LOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_RW_LOCKS) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pthread_rwlock_destroy() | 支持（yes） |
| pthread_rwlock_init() | 支持（yes） |
| pthread_rwlock_rdlock() | 支持（yes） |
| pthread_rwlock_tryrdlock() | 支持（yes） |
| pthread_rwlock_trywrlock() | 支持（yes） |
| pthread_rwlock_unlock() | 支持（yes） |
| pthread_rwlock_wrlock() | 支持（yes） |
| pthread_rwlockattr_destroy() | 支持（yes） |
| pthread_rwlockattr_getpshared() | 支持（yes） |
| pthread_rwlockattr_init() | 支持（yes） |
| pthread_rwlockattr_setpshared() | 支持（yes） |

### 15.1.20\_信号量（Semaphores） · `POSIX_SEMAPHORES`

通过 [`CONFIG_POSIX_SEMAPHORES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SEMAPHORES) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| sem_close() | 支持（yes） |
| sem_destroy() | 支持（yes） |
| sem_getvalue() | 支持（yes） |
| sem_init() | 支持（yes） |
| sem_open() | 支持（yes） |
| sem_post() | 支持（yes） |
| sem_trywait() | 支持（yes） |
| sem_unlink() | 支持（yes） |
| sem_wait() | 支持（yes） |

### 15.1.21\_信号环境跳转（Signal Jump） · `POSIX_SIGNAL_JUMP`

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| siglongjmp() |  |
| sigsetjmp() |  |

### 15.1.22\_信号（Signals） · `POSIX_SIGNALS`

通过 [`CONFIG_POSIX_SIGNALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SIGNALS) 启用此选项组。

注意（Note）：

由于 Zephyr 尚不支持进程，ISO C 函数 `abort()`、`signal()`、`raise()` 以及下面列出的其他 POSIX 函数可能表现出未定义行为（Undefined Behaviour）。POSIX 函数 `kill()`、`pause()`、`sigaction()`、`sigpending()`、`sigsuspend()` 和 `sigwait()` 的实现用于确保符合标准的应用能够链接，但预期调用会失败，并将 `errno` 设为 `ENOSYS` †。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| abort() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| alarm() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| kill() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| pause() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| raise() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| sigaction() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| sigaddset() | 支持（yes） |
| sigdelset() | 支持（yes） |
| sigemptyset() | 支持（yes） |
| sigfillset() | 支持（yes） |
| sigismember() | 支持（yes） |
| signal() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| sigpending() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| sigprocmask() | 支持（yes） |
| sigsuspend() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| sigwait() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| strsignal() | 支持（yes） |

### 15.1.23\_单进程（Single Process） · `POSIX_SINGLE_PROCESS`

`POSIX_SINGLE_PROCESS` 选项组包含面向单进程应用的服务。

通过 [`CONFIG_POSIX_SINGLE_PROCESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SINGLE_PROCESS) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| confstr() | 支持（yes） |
| environ | 支持（yes） |
| errno | 支持（yes） |
| getenv() | 支持（yes） |
| setenv() | 支持（yes） |
| sysconf() | 支持（yes） |
| uname() | 支持（yes） |
| unsetenv() | 支持（yes） |

### 15.1.24\_自旋锁（Spin Locks） · `POSIX_SPIN_LOCKS`

通过 [`CONFIG_POSIX_SPIN_LOCKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SPIN_LOCKS) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pthread_spin_destroy() | 支持（yes） |
| pthread_spin_init() | 支持（yes） |
| pthread_spin_lock() | 支持（yes） |
| pthread_spin_trylock() | 支持（yes） |
| pthread_spin_unlock() | 支持（yes） |

### 15.1.25\_基础线程服务（Base Thread Services） · `POSIX_THREADS_BASE`

此规范的基本假设是：系统由一个隐含的进程及多个线程组成。因此，标准要求提供全部基础线程服务，但不包括与多个进程相关的服务。

通过 [`CONFIG_POSIX_THREADS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pthread_atfork() | 支持（yes） |
| pthread_attr_destroy() | 支持（yes） |
| pthread_attr_getdetachstate() | 支持（yes） |
| pthread_attr_getschedparam() | 支持（yes） |
| pthread_attr_init() | 支持（yes） |
| pthread_attr_setdetachstate() | 支持（yes） |
| pthread_attr_setschedparam() | 支持（yes） |
| pthread_barrier_destroy() | 支持（yes） |
| pthread_barrier_init() | 支持（yes） |
| pthread_barrier_wait() | 支持（yes） |
| pthread_barrierattr_destroy() | 支持（yes） |
| pthread_barrierattr_getpshared() | 支持（yes） |
| pthread_barrierattr_init() | 支持（yes） |
| pthread_barrierattr_setpshared() | 支持（yes） |
| pthread_cancel() | 支持（yes） |
| pthread_cleanup_pop() | 支持（yes） |
| pthread_cleanup_push() | 支持（yes） |
| pthread_cond_broadcast() | 支持（yes） |
| pthread_cond_destroy() | 支持（yes） |
| pthread_cond_init() | 支持（yes） |
| pthread_cond_signal() | 支持（yes） |
| pthread_cond_timedwait() | 支持（yes） |
| pthread_cond_wait() | 支持（yes） |
| pthread_condattr_destroy() | 支持（yes） |
| pthread_condattr_init() | 支持（yes） |
| pthread_create() | 支持（yes） |
| pthread_detach() | 支持（yes） |
| pthread_equal() | 支持（yes） |
| pthread_exit() | 支持（yes） |
| pthread_getspecific() | 支持（yes） |
| pthread_join() | 支持（yes） |
| pthread_key_create() | 支持（yes） |
| pthread_key_delete() | 支持（yes） |
| pthread_kill() |  |
| pthread_mutex_destroy() | 支持（yes） |
| pthread_mutex_init() | 支持（yes） |
| pthread_mutex_lock() | 支持（yes） |
| pthread_mutex_trylock() | 支持（yes） |
| pthread_mutex_unlock() | 支持（yes） |
| pthread_mutexattr_destroy() | 支持（yes） |
| pthread_mutexattr_init() | 支持（yes） |
| pthread_once() | 支持（yes） |
| pthread_self() | 支持（yes） |
| pthread_setcancelstate() | 支持（yes） |
| pthread_setcanceltype() | 支持（yes） |
| pthread_setspecific() | 支持（yes） |
| pthread_sigmask() | 支持（yes） |
| pthread_testcancel() | 支持（yes） |
| sched_yield() | 支持（yes） |

### 15.1.26\_线程扩展（Thread Extensions） · `POSIX_THREADS_EXT`

通过 [`CONFIG_POSIX_THREADS_EXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREADS_EXT) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pthread_attr_getguardsize() | 支持（yes） |
| pthread_attr_setguardsize() | 支持（yes） |
| pthread_mutexattr_gettype() | 支持（yes） |
| pthread_mutexattr_settype() | 支持（yes） |

### 15.1.27\_定时器（Timers） · `POSIX_TIMERS`

通过 [`CONFIG_POSIX_TIMERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMERS) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| clock_getres() | 支持（yes） |
| clock_gettime() | 支持（yes） |
| clock_settime() | 支持（yes） |
| nanosleep() | 支持（yes） |
| timer_create() | 支持（yes） |
| timer_delete() | 支持（yes） |
| timer_gettime() | 支持（yes） |
| timer_getoverrun() | 支持（yes） |
| timer_settime() | 支持（yes） |

### 15.1.28\_XSI 实时扩展（Realtime Extensions） · `XSI_REALTIME`

`XSI_REALTIME` 选项组表示已启用 [`_POSIX_FSYNC`](#posix-option-fsync)、[`_POSIX_MEMLOCK`](#posix-option-memlock)、[`_POSIX_MEMLOCK_RANGE`](#posix-option-memlock-range)、[`_POSIX_MESSAGE_PASSING`](#posix-option-message-passing)、[`_POSIX_PRIORITY_SCHEDULING`](#posix-option-priority-scheduling)、[`_POSIX_SHARED_MEMORY_OBJECTS`](#posix-option-shared-memory-objects) 和 [`_POSIX_SYNCHRONIZED_IO`](#posix-option-synchronized-io) 选项。

通过 [`CONFIG_XSI_REALTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XSI_REALTIME) 启用此选项组。

启用此选项组后，特性测试宏（Feature Test Macro）`_XOPEN_REALTIME` 将定义为非 `-1` 的值。

### 15.1.29\_XSI 单进程扩展（Single-Process Extensions） · `XSI_SINGLE_PROCESS`

通过 [`CONFIG_XSI_SINGLE_PROCESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XSI_SINGLE_PROCESS) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| gethostid() | 支持（yes） |
| gettimeofday() | 支持（yes） |
| putenv() | 支持（yes） |

### 15.1.30\_XSI 系统日志（System Logging） · `XSI_SYSTEM_LOGGING`

通过 [`CONFIG_XSI_SYSTEM_LOGGING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XSI_SYSTEM_LOGGING) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| closelog() | 支持（yes） |
| openlog() | 支持（yes） |
| setlogmask() | 支持（yes） |
| syslog() | 支持（yes） |

### 15.1.31\_XSI 线程扩展（Thread Extensions） · `XSI_THREADS_EXT`

需要 `XSI_THREADS_EXT` 选项组，是因为它提供控制线程栈的函数；这种能力对任何实时应用都有用。

通过 [`CONFIG_XSI_THREADS_EXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XSI_THREADS_EXT) 启用此选项组。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pthread_attr_getstack() | 支持（yes） |
| pthread_attr_setstack() | 支持（yes） |
| pthread_getconcurrency() | 支持（yes） |
| pthread_setconcurrency() | 支持（yes） |

## 15.2\_POSIX 选项（Options）

### 15.2.1\_异步输入输出（Asynchronous I/O） · `_POSIX_ASYNCHRONOUS_IO`

Zephyr 没有实现 `_POSIX_ASYNCHRONOUS_IO` 选项中的功能，但仍提供相应函数，使符合标准的应用能够链接。这些函数将调用失败，并把 `errno` 设为 `ENOSYS` †。

通过 [`CONFIG_POSIX_ASYNCHRONOUS_IO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_ASYNCHRONOUS_IO) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| aio_cancel() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| aio_error() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| aio_fsync() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| aio_read() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| aio_return() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| aio_suspend() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| aio_write() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| lio_listio() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |

### 15.2.2\_CPU 时间（CPU Time） · `_POSIX_CPUTIME`

通过 [`CONFIG_POSIX_CPUTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_CPUTIME) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| CLOCK_PROCESS_CPUTIME_ID | 支持（yes） |

### 15.2.3\_文件同步（File Synchronization） · [`_POSIX_FSYNC`](#posix-option-fsync)

通过 [`CONFIG_POSIX_FSYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_FSYNC) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| fsync() | 支持（yes） |

### 15.2.4\_互联网协议第 6 版（Internet Protocol Version 6） · `_POSIX_IPV6`

支持互联网协议第 6 版（Internet Protocol Version 6，IPv6）。

更多信息见 [网络文档](../networking/P001_网络文档入口.md#networking)。

通过 [`CONFIG_POSIX_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_IPV6) 启用此选项。

### 15.2.5\_内存锁定（Memory Locking） · [`_POSIX_MEMLOCK`](#posix-option-memlock)

Zephyr 的按需分页 API（Demand Paging API）尚不支持固定或解除固定全部虚拟内存区域。下列函数预期会失败，并将 `errno` 设为 `ENOSYS` †。

通过 [`CONFIG_POSIX_MEMLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MEMLOCK) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| mlockall() | 支持（yes） |
| munlockall() | 支持（yes） |

### 15.2.6\_区域内存锁定（Range Memory Locking） · [`_POSIX_MEMLOCK_RANGE`](#posix-option-memlock-range)

通过 [`CONFIG_POSIX_MEMLOCK_RANGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MEMLOCK_RANGE) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| mlock() | 支持（yes） |
| munlock() | 支持（yes） |

### 15.2.7\_消息传递（Message Passing） · [`_POSIX_MESSAGE_PASSING`](#posix-option-message-passing)

通过 [`CONFIG_POSIX_MESSAGE_PASSING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MESSAGE_PASSING) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| mq_close() | 支持（yes） |
| mq_getattr() | 支持（yes） |
| mq_notify() | 支持（yes） |
| mq_open() | 支持（yes） |
| mq_receive() | 支持（yes） |
| mq_send() | 支持（yes） |
| mq_setattr() | 支持（yes） |
| mq_unlink() | 支持（yes） |

### 15.2.8\_单调时钟（Monotonic Clock） · `_POSIX_MONOTONIC_CLOCK`

通过 [`CONFIG_POSIX_MONOTONIC_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_MONOTONIC_CLOCK) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| CLOCK_MONOTONIC | 支持（yes） |

### 15.2.9\_优先级调度（Priority Scheduling） · [`_POSIX_PRIORITY_SCHEDULING`](#posix-option-priority-scheduling)

由于 Zephyr 尚不支持进程，`sched_rr_get_interval()`、`sched_setparam()` 和 `sched_setscheduler()` 预期会失败，并将 `errno` 设为 `ENOSYS` †。

通过 [`CONFIG_POSIX_PRIORITY_SCHEDULING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_PRIORITY_SCHEDULING) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| sched_get_priority_max() | 支持（yes） |
| sched_get_priority_min() | 支持（yes） |
| sched_getparam() | 支持（yes） |
| sched_getscheduler() | 支持（yes） |
| sched_rr_get_interval() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| sched_setparam() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| sched_setscheduler() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |

### 15.2.10\_原始套接字（Raw Sockets） · `_POSIX_RAW_SOCKETS`

支持原始套接字（Raw Sockets）。

更多信息见 [`CONFIG_NET_SOCKETS_PACKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_PACKET)。

通过 [`CONFIG_POSIX_RAW_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_RAW_SOCKETS) 启用此选项。

### 15.2.11\_共享内存对象（Shared Memory Objects） · [`_POSIX_SHARED_MEMORY_OBJECTS`](#posix-option-shared-memory-objects)

通过 [`CONFIG_POSIX_SHARED_MEMORY_OBJECTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SHARED_MEMORY_OBJECTS) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| mmap() | 支持（yes） |
| munmap() | 支持（yes） |
| shm_open() | 支持（yes） |
| shm_unlink() | 支持（yes） |

### 15.2.12\_同步输入输出（Synchronized I/O） · [`_POSIX_SYNCHRONIZED_IO`](#posix-option-synchronized-io)

通过 [`CONFIG_POSIX_SYNCHRONIZED_IO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYNCHRONIZED_IO) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| fdatasync() | 支持（yes） |
| fsync() | 支持（yes） |
| msync() | 支持（yes） |

### 15.2.13\_线程栈地址属性（Thread Stack Address） · `_POSIX_THREAD_ATTR_STACKADDR`

通过 [`CONFIG_POSIX_THREAD_ATTR_STACKADDR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_ATTR_STACKADDR) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pthread_attr_getstackaddr() | 支持（yes） |
| pthread_attr_setstackaddr() | 支持（yes） |

### 15.2.14\_线程栈大小属性（Thread Stack Size） · `_POSIX_THREAD_ATTR_STACKSIZE`

通过 [`CONFIG_POSIX_THREAD_ATTR_STACKSIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_ATTR_STACKSIZE) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pthread_attr_getstacksize() | 支持（yes） |
| pthread_attr_setstacksize() | 支持（yes） |

### 15.2.15\_线程 CPU 时间（Thread CPU Time） · `_POSIX_THREAD_CPUTIME`

通过 [`CONFIG_POSIX_THREAD_CPUTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_CPUTIME) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| CLOCK_THREAD_CPUTIME_ID | 支持（yes） |
| pthread_getcpuclockid() | 支持（yes） |

### 15.2.16\_线程优先级继承（Priority Inheritance） · `_POSIX_THREAD_PRIO_INHERIT`

通过 [`CONFIG_POSIX_THREAD_PRIO_INHERIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_PRIO_INHERIT) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pthread_mutexattr_getprotocol() | 支持（yes） |
| pthread_mutexattr_setprotocol() | 支持（yes） |

### 15.2.17\_线程优先级保护（Priority Protection） · `_POSIX_THREAD_PRIO_PROTECT`

通过 [`CONFIG_POSIX_THREAD_PRIO_PROTECT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_PRIO_PROTECT) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pthread_mutex_getprioceiling() | 支持（yes） |
| pthread_mutex_setprioceiling() | 支持（yes） |
| pthread_mutexattr_getprioceiling() | 支持（yes） |
| pthread_mutexattr_getprotocol() | 支持（yes） |
| pthread_mutexattr_setprioceiling() | 支持（yes） |
| pthread_mutexattr_setprotocol() | 支持（yes） |

### 15.2.18\_线程优先级调度（Thread Priority Scheduling） · `_POSIX_THREAD_PRIORITY_SCHEDULING`

通过 [`CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| pthread_attr_getinheritsched() | 支持（yes） |
| pthread_attr_getschedpolicy() | 支持（yes） |
| pthread_attr_getscope() | 支持（yes） |
| pthread_attr_setinheritsched() | 支持（yes） |
| pthread_attr_setschedpolicy() | 支持（yes） |
| pthread_attr_setscope() | 支持（yes） |
| pthread_getschedparam() | 支持（yes） |
| pthread_setschedparam() | 支持（yes） |
| pthread_setschedprio() | 支持（yes） |

### 15.2.19\_线程安全函数（Thread-Safe Functions） · `_POSIX_THREAD_SAFE_FUNCTIONS`

通过 [`CONFIG_POSIX_THREAD_SAFE_FUNCTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_THREAD_SAFE_FUNCTIONS) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| asctime_r() | 支持（yes） |
| ctime_r() | 支持（yes） （仅 UTC 时区） |
| flockfile() |  |
| ftrylockfile() |  |
| funlockfile() |  |
| getc_unlocked() |  |
| getchar_unlocked() |  |
| getgrgid_r() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| getgrnam_r() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| getpwnam_r() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| getpwuid_r() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| gmtime_r() | 支持（yes） |
| localtime_r() | 支持（yes） （仅 UTC 时区） |
| putc_unlocked() |  |
| putchar_unlocked() |  |
| rand_r() | 支持（yes） |
| readdir_r() | 支持（yes） |
| strerror_r() | 支持（yes） |
| strtok_r() | 支持（yes） |

### 15.2.20\_超时（Timeouts） · `_POSIX_TIMEOUTS`

通过 [`CONFIG_POSIX_TIMEOUTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMEOUTS) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| mq_timedreceive() | 支持（yes） |
| mq_timedsend() | 支持（yes） |
| pthread_mutex_timedlock() | 支持（yes） |
| pthread_rwlock_timedrdlock() | 支持（yes） |
| pthread_rwlock_timedwrlock() | 支持（yes） |
| sem_timedwait() | 支持（yes） |
| posix_trace_timedgetnext_event() |  |

### 15.2.21\_X/Open 流接口（STREAMS） · `_XOPEN_STREAMS`

除 `ioctl()` 外，Zephyr 没有实现 `_XOPEN_STREAMS` 选项组中的功能，但仍提供相应函数，使符合标准的应用能够链接。该组选项中未实现的函数将失败，并将 `errno` 设为 `ENOSYS` †。

通过 [`CONFIG_XSI_STREAMS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XSI_STREAMS) 启用此选项。

| 接口（API） | 支持状态（Supported） |
| --- | --- |
| fattach() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| fdetach() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| getmsg() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| getpmsg() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| ioctl() | 支持（yes） |
| isastream() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| putmsg() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |
| putpmsg() | 支持（yes） [†](P012_POSIX符合性.md#posix-undefined-behaviour) |

译注——源码对照：当前 `aio.c` 中的异步 I/O 函数仍有返回 `-1` 并设置 `errno=ENOSYS` 的占位实现；`sched.c` 的 `sched_getparam()` 和 `sched_getscheduler()` 也如此，而原页调度段落仅显式点名三个设置／查询接口。请逐函数检查实现，不能把表格中的“支持（yes）”理解为相关算法或进程行为均已实现。本章保留原页表格，不以译注中的检查结果改写官方支持矩阵。


译注核对来源：[subsys/portability/posix/options/aio.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/aio.c)、[subsys/portability/posix/options/signal.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/signal.c)、[subsys/portability/posix/options/sched.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/sched.c)、[subsys/portability/posix/options/stropts.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/stropts.c)。

本仓库的[对应源码](../../../subsys/portability/posix/options/aio.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="posix-option-and-option-group-details"></a>
<a id="posix-option-groups"></a>
<a id="id1"></a>
<a id="posix-barriers"></a>
<a id="posix-option-group-barriers"></a>
<a id="id4"></a>
<a id="posix-c-lang-jump"></a>
<a id="posix-option-group-c-lang-jump"></a>
<a id="id5"></a>
<a id="posix-c-lang-math"></a>
<a id="posix-option-group-c-lang-math"></a>
<a id="posix-c-lang-support"></a>
<a id="posix-option-group-c-lang-support"></a>
<a id="posix-c-lang-support-r"></a>
<a id="posix-option-group-c-lang-support-r"></a>
<a id="id6"></a>
<a id="posix-c-lib-ext"></a>
<a id="posix-option-group-c-lib-ext"></a>
<a id="id7"></a>
<a id="posix-clock-selection"></a>
<a id="posix-option-group-clock-selection"></a>
<a id="id8"></a>
<a id="posix-device-io"></a>
<a id="posix-option-group-device-io"></a>
<a id="id9"></a>
<a id="posix-fd-mgmt"></a>
<a id="posix-option-group-fd-mgmt"></a>
<a id="id10"></a>
<a id="posix-file-locking"></a>
<a id="posix-option-group-file-locking"></a>
<a id="id11"></a>
<a id="posix-file-system"></a>
<a id="posix-option-group-file-system"></a>
<a id="id12"></a>
<a id="posix-file-system-r"></a>
<a id="posix-option-group-file-system-r"></a>
<a id="id13"></a>
<a id="posix-mapped-files"></a>
<a id="posix-option-group-mapped-files"></a>
<a id="id14"></a>
<a id="posix-memory-protection"></a>
<a id="posix-option-group-memory-protection"></a>
<a id="id15"></a>
<a id="posix-multi-process"></a>
<a id="posix-option-group-multi-process"></a>
<a id="id16"></a>
<a id="posix-networking"></a>
<a id="posix-option-group-networking"></a>
<a id="id17"></a>
<a id="posix-pipe"></a>
<a id="posix-option-group-pipe"></a>
<a id="id18"></a>
<a id="posix-realtime-signals"></a>
<a id="posix-option-group-realtime-signals"></a>
<a id="id19"></a>
<a id="posix-rw-locks"></a>
<a id="posix-option-group-rw-locks"></a>
<a id="posix-option-reader-writer-locks"></a>
<a id="id20"></a>
<a id="posix-semaphores"></a>
<a id="posix-option-group-semaphores"></a>
<a id="id21"></a>
<a id="posix-signal-jump"></a>
<a id="posix-option-group-signal-jump"></a>
<a id="id22"></a>
<a id="posix-signals"></a>
<a id="posix-option-group-signals"></a>
<a id="id23"></a>
<a id="posix-single-process"></a>
<a id="posix-option-group-single-process"></a>
<a id="id24"></a>
<a id="posix-spin-locks"></a>
<a id="posix-option-group-spin-locks"></a>
<a id="id25"></a>
<a id="posix-threads-base"></a>
<a id="posix-option-group-threads-base"></a>
<a id="id26"></a>
<a id="posix-threads-ext"></a>
<a id="posix-option-group-posix-threads-ext"></a>
<a id="id27"></a>
<a id="posix-timers"></a>
<a id="posix-option-group-timers"></a>
<a id="id28"></a>
<a id="xsi-realtime"></a>
<a id="posix-option-group-xsi-realtime"></a>
<a id="xsi-single-process"></a>
<a id="posix-option-group-xsi-single-process"></a>
<a id="id29"></a>
<a id="xsi-system-logging"></a>
<a id="posix-option-group-xsi-system-logging"></a>
<a id="id30"></a>
<a id="xsi-threads-ext"></a>
<a id="posix-option-group-xsi-threads-ext"></a>
<a id="id31"></a>
<a id="posix-options"></a>
<a id="id2"></a>
<a id="posix-asynchronous-io"></a>
<a id="posix-option-asynchronous-io"></a>
<a id="id32"></a>
<a id="posix-cputime"></a>
<a id="posix-option-cputime"></a>
<a id="id33"></a>
<a id="posix-fsync"></a>
<a id="posix-option-fsync"></a>
<a id="id34"></a>
<a id="posix-ipv6"></a>
<a id="posix-option-ipv6"></a>
<a id="posix-memlock"></a>
<a id="posix-option-memlock"></a>
<a id="id35"></a>
<a id="posix-memlock-range"></a>
<a id="posix-option-memlock-range"></a>
<a id="id36"></a>
<a id="posix-message-passing"></a>
<a id="posix-option-message-passing"></a>
<a id="id37"></a>
<a id="posix-monotonic-clock"></a>
<a id="posix-option-monotonic-clock"></a>
<a id="id38"></a>
<a id="posix-priority-scheduling"></a>
<a id="posix-option-priority-scheduling"></a>
<a id="id39"></a>
<a id="posix-raw-sockets"></a>
<a id="posix-option-raw-sockets"></a>
<a id="posix-option-shared-memory-objects"></a>
<a id="posix-shared-memory-objects"></a>
<a id="id3"></a>
<a id="id40"></a>
<a id="posix-synchronized-io"></a>
<a id="posix-option-synchronized-io"></a>
<a id="id41"></a>
<a id="posix-thread-attr-stackaddr"></a>
<a id="posix-option-thread-attr-stackaddr"></a>
<a id="id42"></a>
<a id="posix-thread-attr-stacksize"></a>
<a id="posix-option-thread-attr-stacksize"></a>
<a id="id43"></a>
<a id="posix-thread-cputime"></a>
<a id="posix-option-thread-cputime"></a>
<a id="id44"></a>
<a id="posix-thread-prio-inherit"></a>
<a id="posix-option-thread-prio-inherit"></a>
<a id="id45"></a>
<a id="posix-thread-prio-protect"></a>
<a id="posix-option-thread-prio-protect"></a>
<a id="id46"></a>
<a id="posix-thread-priority-scheduling"></a>
<a id="posix-option-thread-priority-scheduling"></a>
<a id="id47"></a>
<a id="posix-thread-safe-functions"></a>
<a id="posix-option-thread-safe-functions"></a>
<a id="id48"></a>
<a id="posix-timeouts"></a>
<a id="posix-option-timeouts"></a>
<a id="id49"></a>
<a id="xopen-streams"></a>
<a id="posix-option-xopen-streams"></a>
<a id="id50"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：POSIX实现设计](P014_POSIX实现设计.md) · [本模块主线目录](../reading/portability.md) · [全部主线](../reading/README.md) · [下一篇：POSIX附加配置选项](P016_POSIX附加配置选项.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P014_POSIX实现设计.md) · [返回大纲](大纲.md) · [下一章](P016_POSIX附加配置选项.md)

</details>

<!-- reading-navigation:end -->
