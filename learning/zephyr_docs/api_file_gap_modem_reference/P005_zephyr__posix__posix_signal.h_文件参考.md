---
id: learning.zephyr-docs.api-file-gap-modem-reference.page-5
title: zephyr__posix__posix_signal.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_posix\_\_posix\_signal.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/toolchain.h>
#include <zephyr/sys/util.h>
#include <stddef.h>
#include <time.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_timespec"></a>

```c
struct timespec
```

相关声明：[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_sigset_5Ft"></a>

```c
struct sigset_t
```

相关声明：[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)。

<a id="r_pthread_5Fattr_5Ft"></a>

```c
struct pthread_attr_t
```

相关声明：[pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)。

<a id="r_sigval"></a>

```c
union sigval
```

相关声明：[sigval](../posix_system_model_reference/P035_sigval_联合体.md)。

<a id="r_sigevent"></a>

```c
struct sigevent
```

相关声明：[sigevent](../posix_system_model_reference/P018_sigevent_结构体.md)。

<a id="r_siginfo_5Ft"></a>

```c
struct siginfo_t
```

相关声明：[siginfo_t](../posix_system_model_reference/P019_siginfo_t_结构体.md)。

<a id="r_sigaction"></a>

```c
struct sigaction
```

相关声明：[sigaction](../posix_system_model_reference/P017_sigaction_结构体.md)。

<a id="r_mcontext_5Ft"></a>

```c
struct mcontext_t
```

相关声明：[mcontext_t](../platform_security_model_reference/P017_mcontext_t_结构体.md)。

<a id="r_stack_5Ft"></a>

```c
struct stack_t
```

相关声明：[stack_t](../posix_system_model_reference/P021_stack_t_结构体.md)。

<a id="r_ucontext_5Ft"></a>

```c
struct ucontext_t
```

相关声明：[ucontext_t](../posix_system_model_reference/P027_ucontext_t_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_a0fa971487344a463a7f0545c9c9ef2bf"></a>

```c
#define SIG_HOLD ((void *)-2)
```

相关声明：[SIG_HOLD](#a0fa971487344a463a7f0545c9c9ef2bf)。

<a id="r_ae89f9a1282bd2d1b2a2b310c12ea16a5"></a>

```c
#define SIGRTMIN 32
```

相关声明：[SIGRTMIN](#ae89f9a1282bd2d1b2a2b310c12ea16a5)。

<a id="r_a5336d2c76af22b10373e3dd28fb3b0f0"></a>

```c
#define SIGRTMAX (SIGRTMIN + CONFIG_POSIX_RTSIG_MAX)
```

相关声明：[SIGRTMAX](#a5336d2c76af22b10373e3dd28fb3b0f0)、[SIGRTMIN](#ae89f9a1282bd2d1b2a2b310c12ea16a5)。

<a id="r_aced9a66610d9d61756999ce4f103740e"></a>

```c
#define SIGEV_NONE 1
```

相关声明：[SIGEV_NONE](#aced9a66610d9d61756999ce4f103740e)。

<a id="r_a06d5881eeb84e6ac35f5b801c380dbb6"></a>

```c
#define SIGEV_SIGNAL 2
```

相关声明：[SIGEV_SIGNAL](#a06d5881eeb84e6ac35f5b801c380dbb6)。

<a id="r_a29ccb6a17fa90a1357b478f62af7fca0"></a>

```c
#define SIGEV_THREAD 3
```

相关声明：[SIGEV_THREAD](#a29ccb6a17fa90a1357b478f62af7fca0)。

<a id="r_a927f6ae16379576d638006c7498ac5d7"></a>

```c
#define SIG_BLOCK 1
```

相关声明：[SIG_BLOCK](#a927f6ae16379576d638006c7498ac5d7)。

<a id="r_a5fcd73313a63dac2cc7eb3b654215250"></a>

```c
#define SIG_UNBLOCK 2
```

相关声明：[SIG_UNBLOCK](#a5fcd73313a63dac2cc7eb3b654215250)。

<a id="r_a37750b78b7ae75fe02ad26e70f6cc845"></a>

```c
#define SIG_SETMASK 0
```

相关声明：[SIG_SETMASK](#a37750b78b7ae75fe02ad26e70f6cc845)。

<a id="r_af6a71c97263725437f59ceb16241fd32"></a>

```c
#define SA_NOCLDSTOP 0x00000001
```

相关声明：[SA_NOCLDSTOP](#af6a71c97263725437f59ceb16241fd32)。

<a id="r_a322c220e296393958ab4238145a0d273"></a>

```c
#define SA_ONSTACK 0x00000002
```

相关声明：[SA_ONSTACK](#a322c220e296393958ab4238145a0d273)。

<a id="r_a8d5fb4f35858d31035e7354c1d4048ea"></a>

```c
#define SA_RESETHAND 0x00000004
```

相关声明：[SA_RESETHAND](#a8d5fb4f35858d31035e7354c1d4048ea)。

<a id="r_a74ef0a27afcf55b6cd6d35cf0fa5d427"></a>

```c
#define SA_RESTART 0x00000008
```

相关声明：[SA_RESTART](#a74ef0a27afcf55b6cd6d35cf0fa5d427)。

<a id="r_a59b4c0774aace526b10b6d737075a790"></a>

```c
#define SA_SIGINFO 0x00000010
```

相关声明：[SA_SIGINFO](#a59b4c0774aace526b10b6d737075a790)。

<a id="r_ae4c1aad864ef72e4a2cce74b1b8a5a0b"></a>

```c
#define SA_NOCLDWAIT 0x00000020
```

相关声明：[SA_NOCLDWAIT](#ae4c1aad864ef72e4a2cce74b1b8a5a0b)。

<a id="r_abec4abd80d73397fc2f78f57f178565f"></a>

```c
#define SA_NODEFER 0x00000040
```

相关声明：[SA_NODEFER](#abec4abd80d73397fc2f78f57f178565f)。

<a id="r_a17bcfefa3c6fafd5d3277d867bd723fb"></a>

```c
#define SS_ONSTACK 0x00000001
```

相关声明：[SS_ONSTACK](#a17bcfefa3c6fafd5d3277d867bd723fb)。

<a id="r_ac515f2efc91c54803f65de08d14d4566"></a>

```c
#define SS_DISABLE 0x00000002
```

相关声明：[SS_DISABLE](#ac515f2efc91c54803f65de08d14d4566)。

<a id="r_aae6a742a8c5acf12caba1d148dd03f10"></a>

```c
#define MINSIGSTKSZ 4096
```

相关声明：[MINSIGSTKSZ](#aae6a742a8c5acf12caba1d148dd03f10)。

<a id="r_a8a433a10420a0c51355da26cfcab2131"></a>

```c
#define SIGSTKSZ 4096
```

相关声明：[SIGSTKSZ](#a8a433a10420a0c51355da26cfcab2131)。

<a id="r_a136c64ec2d1306de745e39d6aee362ca"></a>

```c
#define SIGHUP 1
```

相关声明：[SIGHUP](#a136c64ec2d1306de745e39d6aee362ca)。

挂断（Hangup）。

<a id="r_a487309e3e9e0527535644115204a639a"></a>

```c
#define SIGINT 2
```

相关声明：[SIGINT](#a487309e3e9e0527535644115204a639a)。

中断（Interrupt）。

<a id="r_a62045b465be11891160d53c10861b16c"></a>

```c
#define SIGQUIT 3
```

相关声明：[SIGQUIT](#a62045b465be11891160d53c10861b16c)。

退出（Quit）。

<a id="r_a4c9c5284f8c8d146bd7a93d25017fc62"></a>

```c
#define SIGILL 4
```

相关声明：[SIGILL](#a4c9c5284f8c8d146bd7a93d25017fc62)。

非法指令（Illegal Instruction）。

<a id="r_aa2beb906ab1b46676e63823f4e773c38"></a>

```c
#define SIGTRAP 5
```

相关声明：[SIGTRAP](#aa2beb906ab1b46676e63823f4e773c38)。

跟踪／断点陷阱（Trace/Breakpoint Trap）。

<a id="r_aa86c630133e5b5174ac970227b273446"></a>

```c
#define SIGABRT 6
```

相关声明：[SIGABRT](#aa86c630133e5b5174ac970227b273446)。

已中止（Aborted）。

<a id="r_aead3d488474201acf18c4b63d91edc3c"></a>

```c
#define SIGBUS 7
```

相关声明：[SIGBUS](#aead3d488474201acf18c4b63d91edc3c)。

总线错误（Bus Error）。

<a id="r_a7fbba29aec3e4a8daae12935299df92d"></a>

```c
#define SIGFPE 8
```

相关声明：[SIGFPE](#a7fbba29aec3e4a8daae12935299df92d)。

算术异常（Arithmetic Exception）。

<a id="r_addd8dcd406ce514ab3b4f576a5343d42"></a>

```c
#define SIGKILL 9
```

相关声明：[SIGKILL](#addd8dcd406ce514ab3b4f576a5343d42)。

被强制终止（Killed）。

<a id="r_a944a8250e34bfd7991123abd3436d8c0"></a>

```c
#define SIGUSR1 10
```

相关声明：[SIGUSR1](#a944a8250e34bfd7991123abd3436d8c0)。

用户定义信号 1（User-Defined Signal 1）。

<a id="r_ae20b4f7171a09516ea73c9d2745bd596"></a>

```c
#define SIGSEGV 11
```

相关声明：[SIGSEGV](#ae20b4f7171a09516ea73c9d2745bd596)。

无效内存引用（Invalid Memory Reference）。

<a id="r_abaaa61abe503c43481e35e21b0b5a031"></a>

```c
#define SIGUSR2 12
```

相关声明：[SIGUSR2](#abaaa61abe503c43481e35e21b0b5a031)。

用户定义信号 2（User-Defined Signal 2）。

<a id="r_a57e9c8c5fa13bf86bc779a9f6f408b7c"></a>

```c
#define SIGPIPE 13
```

相关声明：[SIGPIPE](#a57e9c8c5fa13bf86bc779a9f6f408b7c)。

管道断开（Broken Pipe）。

<a id="r_aa6946723c6b7a86ec3c33caaf832840b"></a>

```c
#define SIGALRM 14
```

相关声明：[SIGALRM](#aa6946723c6b7a86ec3c33caaf832840b)。

闹钟（Alarm Clock）。

<a id="r_a682182a5e5f38fd61f4311501e9dac5d"></a>

```c
#define SIGTERM 15
```

相关声明：[SIGTERM](#a682182a5e5f38fd61f4311501e9dac5d)。

已终止（Terminated）。

<a id="r_a0e63521a64cc8bc2b91d36a87d32c9f8"></a>

```c
#define SIGCHLD 17
```

相关声明：[SIGCHLD](#a0e63521a64cc8bc2b91d36a87d32c9f8)。

子进程状态已改变（Child Status Changed）。

<a id="r_a024f43063003e753afc6cca1acd6e104"></a>

```c
#define SIGCONT 18
```

相关声明：[SIGCONT](#a024f43063003e753afc6cca1acd6e104)。

已继续（Continued）。

<a id="r_a069e358bc9a864b7dc4fed2440eda14c"></a>

```c
#define SIGSTOP 19
```

相关声明：[SIGSTOP](#a069e358bc9a864b7dc4fed2440eda14c)。

停止执行（Stop Executing）。

<a id="r_abe65c086e01f0d286b7a785a7e3cdd1a"></a>

```c
#define SIGTSTP 20
```

相关声明：[SIGTSTP](#abe65c086e01f0d286b7a785a7e3cdd1a)。

已停止（Stopped）。

<a id="r_a2c146e34a6b5a78dfba41cded3331181"></a>

```c
#define SIGTTIN 21
```

相关声明：[SIGTTIN](#a2c146e34a6b5a78dfba41cded3331181)。

因读取而停止（Stopped，Read）。

<a id="r_a782864287613e2c5c030411fa9c5e9b1"></a>

```c
#define SIGTTOU 22
```

相关声明：[SIGTTOU](#a782864287613e2c5c030411fa9c5e9b1)。

因写入而停止（Stopped，Write）。

<a id="r_ad9ff13149e36144a4ea28788948c34dd"></a>

```c
#define SIGURG 23
```

相关声明：[SIGURG](#ad9ff13149e36144a4ea28788948c34dd)。

紧急 I/O 状态（Urgent I/O Condition）。

<a id="r_a7265cbba4972503c1c30a2e52a929874"></a>

```c
#define SIGXCPU 24
```

相关声明：[SIGXCPU](#a7265cbba4972503c1c30a2e52a929874)。

超出 CPU 时间限制（CPU Time Limit）。

<a id="r_a75440a7aa885a1052dfd3b4393fd9baa"></a>

```c
#define SIGXFSZ 25
```

相关声明：[SIGXFSZ](#a75440a7aa885a1052dfd3b4393fd9baa)。

超出文件大小限制（File Size Limit）。

<a id="r_a71403d2f5240e409e213060ea3301851"></a>

```c
#define SIGVTALRM 26
```

相关声明：[SIGVTALRM](#a71403d2f5240e409e213060ea3301851)。

虚拟定时器到期（Virtual Timer Expired）。

<a id="r_ab6bd2a2ff7e58d45965ef257f96dfe65"></a>

```c
#define SIGPROF 27
```

相关声明：[SIGPROF](#ab6bd2a2ff7e58d45965ef257f96dfe65)。

性能分析定时器到期（Profiling Timer Expired）。

<a id="r_a1614264a836d6a5642554775ef0134d0"></a>

```c
#define SIGPOLL 29
```

相关声明：[SIGPOLL](#a1614264a836d6a5642554775ef0134d0)。

发生了可轮询事件（Pollable Event）。

<a id="r_a8bacf9eb18fd539099c1bb4666c45d60"></a>

```c
#define SIGSYS 31
```

相关声明：[SIGSYS](#a8bacf9eb18fd539099c1bb4666c45d60)。

错误的系统调用（Bad System Call）。

<a id="r_a41705eedb4a32e5b0b9a3ef98f98599c"></a>

```c
#define ILL_ILLOPC 1
```

相关声明：[ILL_ILLOPC](#a41705eedb4a32e5b0b9a3ef98f98599c)。

非法操作码（Illegal Opcode）。

<a id="r_af5f5854f70f082160b7e0656907a4ced"></a>

```c
#define ILL_ILLOPN 2
```

相关声明：[ILL_ILLOPN](#af5f5854f70f082160b7e0656907a4ced)。

非法操作数（Illegal Operand）。

<a id="r_ab225825a0696d9341ea4569abdc954f0"></a>

```c
#define ILL_ILLADR 3
```

相关声明：[ILL_ILLADR](#ab225825a0696d9341ea4569abdc954f0)。

非法寻址模式（Illegal Addressing Mode）。

<a id="r_adb1378440989b1b20f7ff358a91e3cb2"></a>

```c
#define ILL_ILLTRP 4
```

相关声明：[ILL_ILLTRP](#adb1378440989b1b20f7ff358a91e3cb2)。

非法陷阱（Illegal Trap）。

<a id="r_af7d4b4283e951ed0cb3cc33b2b451fd2"></a>

```c
#define ILL_PRVOPC 5
```

相关声明：[ILL_PRVOPC](#af7d4b4283e951ed0cb3cc33b2b451fd2)。

特权操作码（Privileged Opcode）。

<a id="r_aa3bff56a3faabe1a3755fd77cda127b1"></a>

```c
#define ILL_PRVREG 6
```

相关声明：[ILL_PRVREG](#aa3bff56a3faabe1a3755fd77cda127b1)。

特权寄存器（Privileged Register）。

<a id="r_ae8aca6f3472a885fb6d3948f8e1a5fa9"></a>

```c
#define ILL_COPROC 7
```

相关声明：[ILL_COPROC](#ae8aca6f3472a885fb6d3948f8e1a5fa9)。

协处理器错误（Coprocessor Error）。

<a id="r_ad16edcc255b0df2dd3572fc9256ef180"></a>

```c
#define ILL_BADSTK 8
```

相关声明：[ILL_BADSTK](#ad16edcc255b0df2dd3572fc9256ef180)。

内部栈错误（Internal Stack Error）。

<a id="r_abc24569f7a193eff6381dd2212464a0a"></a>

```c
#define FPE_INTDIV 9
```

相关声明：[FPE_INTDIV](#abc24569f7a193eff6381dd2212464a0a)。

整数除以零（Integer Divide by Zero）。

<a id="r_aa85ab73a55a64cf580afa3596c0d5a03"></a>

```c
#define FPE_INTOVF 10
```

相关声明：[FPE_INTOVF](#aa85ab73a55a64cf580afa3596c0d5a03)。

整数溢出（Integer Overflow）。

<a id="r_af9bde83d81419c42660d5963159e3b12"></a>

```c
#define FPE_FLTDIV 11
```

相关声明：[FPE_FLTDIV](#af9bde83d81419c42660d5963159e3b12)。

浮点除以零（Floating-Point Divide by Zero）。

<a id="r_adb3c2df5b8d0979b8b26f89096a513b9"></a>

```c
#define FPE_FLTOVF 12
```

相关声明：[FPE_FLTOVF](#adb3c2df5b8d0979b8b26f89096a513b9)。

浮点上溢（Floating-Point Overflow）。

<a id="r_aa48a81252484098176287529607bd275"></a>

```c
#define FPE_FLTUND 13
```

相关声明：[FPE_FLTUND](#aa48a81252484098176287529607bd275)。

浮点下溢（Floating-Point Underflow）。

<a id="r_add5139f33bb657877bb88e2c2b2084ab"></a>

```c
#define FPE_FLTRES 15
```

相关声明：[FPE_FLTRES](#add5139f33bb657877bb88e2c2b2084ab)。

浮点结果不精确（Floating-Point Inexact Result）。

<a id="r_a4616f880b63120a93c1e4ac6a7aa3dae"></a>

```c
#define FPE_FLTINV 16
```

相关声明：[FPE_FLTINV](#a4616f880b63120a93c1e4ac6a7aa3dae)。

无效浮点运算（Invalid Floating-Point Operation）。

<a id="r_a72463f25ca7c74964873c79b4fc3009d"></a>

```c
#define FPE_FLTSUB 17
```

相关声明：[FPE_FLTSUB](#a72463f25ca7c74964873c79b4fc3009d)。

下标超出范围（Subscript out of Range）。

<a id="r_a289e4151377c06f31fd4295061de78d9"></a>

```c
#define SEGV_MAPERR 18
```

相关声明：[SEGV_MAPERR](#a289e4151377c06f31fd4295061de78d9)。

地址未映射到对象（Address Not Mapped to Object）。

<a id="r_aba23f74fc8d8b7f8826f6275422a5648"></a>

```c
#define SEGV_ACCERR 19
```

相关声明：[SEGV_ACCERR](#aba23f74fc8d8b7f8826f6275422a5648)。

映射对象的访问权限无效（Invalid Permissions for Mapped Object）。

<a id="r_a6ea334f3e9a67fbe0cce4c9738cc842a"></a>

```c
#define BUS_ADRALN 20
```

相关声明：[BUS_ADRALN](#a6ea334f3e9a67fbe0cce4c9738cc842a)。

地址对齐无效（Invalid Address Alignment）。

<a id="r_a2343c7bb80913e6f8d69ae3cd7bd6273"></a>

```c
#define BUS_ADRERR 21
```

相关声明：[BUS_ADRERR](#a2343c7bb80913e6f8d69ae3cd7bd6273)。

物理地址不存在（Nonexistent Physical Address）。

<a id="r_a1b507e6736ff85de98cc1b0151f61d44"></a>

```c
#define BUS_OBJERR 22
```

相关声明：[BUS_OBJERR](#a1b507e6736ff85de98cc1b0151f61d44)。

对象特有的硬件错误（Object-Specific Hardware Error）。

<a id="r_a79fcb87a23520cade78f77a4dd3142c6"></a>

```c
#define TRAP_BRKPT 23
```

相关声明：[TRAP_BRKPT](#a79fcb87a23520cade78f77a4dd3142c6)。

进程断点（Process Breakpoint）。

<a id="r_a16042a25974d31a1aff6f09bb6a7358a"></a>

```c
#define TRAP_TRACE 24
```

相关声明：[TRAP_TRACE](#a16042a25974d31a1aff6f09bb6a7358a)。

进程跟踪陷阱（Process Trace Trap）。

<a id="r_a3e6df4a3087d9aa8ba11c61c38c9218c"></a>

```c
#define CLD_EXITED 25
```

相关声明：[CLD_EXITED](#a3e6df4a3087d9aa8ba11c61c38c9218c)。

子进程已退出（Child Has Exited）。

<a id="r_a2d5941afd29bca8b8f74461cb97fe982"></a>

```c
#define CLD_KILLED 26
```

相关声明：[CLD_KILLED](#a2d5941afd29bca8b8f74461cb97fe982)。

子进程已异常终止，且未创建核心转储文件（Core File）。

<a id="r_afe6e9bccf7df675f022a3e484a73461f"></a>

```c
#define CLD_DUMPED 27
```

相关声明：[CLD_DUMPED](#afe6e9bccf7df675f022a3e484a73461f)。

子进程已异常终止，并已创建核心转储文件（Core File）。

<a id="r_aa679c19d95672068f1e4a4673a15ff1c"></a>

```c
#define CLD_TRAPPED 28
```

相关声明：[CLD_TRAPPED](#aa679c19d95672068f1e4a4673a15ff1c)。

被跟踪的子进程触发了陷阱（Trap）。

<a id="r_a1844847a22da24371fa347b959283916"></a>

```c
#define CLD_STOPPED 29
```

相关声明：[CLD_STOPPED](#a1844847a22da24371fa347b959283916)。

子进程已停止（Stopped）。

<a id="r_afad5fd60fd725025f0682ec2697d1b45"></a>

```c
#define CLD_CONTINUED 30
```

相关声明：[CLD_CONTINUED](#afad5fd60fd725025f0682ec2697d1b45)。

已停止的子进程已继续执行（Continued）。

<a id="r_ad78b4cee7029b93a9b7e7b3a92df77eb"></a>

```c
#define POLL_IN 31
```

相关声明：[POLL_IN](#ad78b4cee7029b93a9b7e7b3a92df77eb)。

有数据可供输入（Data Input Available）。

<a id="r_aa29f1b123e70df2a75508eb8e3e7c32b"></a>

```c
#define POLL_OUT 32
```

相关声明：[POLL_OUT](#aa29f1b123e70df2a75508eb8e3e7c32b)。

有可用输出缓冲区（Output Buffers Available）。

<a id="r_a4fb3eb4526e54e7cd3ba550021fdd91d"></a>

```c
#define POLL_MSG 33
```

相关声明：[POLL_MSG](#a4fb3eb4526e54e7cd3ba550021fdd91d)。

有可用输入消息（Input Message Available）。

<a id="r_ab23ba62b3171d1c93c7fd9bd588c1b08"></a>

```c
#define POLL_ERR 34
```

相关声明：[POLL_ERR](#ab23ba62b3171d1c93c7fd9bd588c1b08)。

输入／输出错误（I/O Error）。

<a id="r_a62827cb6f0ae13e8df4d310c4a089c07"></a>

```c
#define POLL_PRI 35
```

相关声明：[POLL_PRI](#a62827cb6f0ae13e8df4d310c4a089c07)。

有可用高优先级输入（High Priority Input Available）。

<a id="r_a0d20a75cd180ea52abb636e90c4b15b4"></a>

```c
#define POLL_HUP 36
```

相关声明：[POLL_HUP](#a0d20a75cd180ea52abb636e90c4b15b4)。

设备已断开连接（Device Disconnected）。

<a id="r_af9e4986b4f6bb9bd932b2fc8166301b9"></a>

```c
#define SI_USER 37
```

相关声明：[SI_USER](#af9e4986b4f6bb9bd932b2fc8166301b9)。

由 `kill()` 发送的信号（Signal）。

<a id="r_a4f23f53a46f88a96a0f28e23f7a9bad6"></a>

```c
#define SI_QUEUE 38
```

相关声明：[SI_QUEUE](#a4f23f53a46f88a96a0f28e23f7a9bad6)。

由 `sigqueue()` 发送的信号（Signal）。

<a id="r_ab57ec52e57fbb49071f96f255bc7c31b"></a>

```c
#define SI_TIMER 39
```

相关声明：[SI_TIMER](#ab57ec52e57fbb49071f96f255bc7c31b)。

由 `timer_settime()` 设置的定时器到期时生成的信号（Signal）。

<a id="r_aa8ff6c6d4af21cf9380de1e8fef9db4c"></a>

```c
#define SI_ASYNCIO 40
```

相关声明：[SI_ASYNCIO](#aa8ff6c6d4af21cf9380de1e8fef9db4c)。

异步 I/O 请求（Asynchronous I/O Request）完成时生成的信号。

<a id="r_afdf808efb3ebd166f67910156146c8fc"></a>

```c
#define SI_MESGQ 41
```

相关声明：[SI_MESGQ](#afdf808efb3ebd166f67910156146c8fc)。

消息到达空消息队列（Message Queue）时生成的信号。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 5.3\_类型定义（Typedefs）

<a id="r_ab3f45e72c67ecc7866d14ab09b3367e7"></a>

```c
typedef unsigned int pthread_t
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[pthread_t](#ab3f45e72c67ecc7866d14ab09b3367e7)。

<a id="r_afc544433253791fc5f87b8203c9b6e63"></a>

```c
typedef int uid_t
```

相关声明：[uid_t](#afc544433253791fc5f87b8203c9b6e63)。

<a id="r_a114f9c2461df851d2ad00aad8dcfa3f7"></a>

```c
typedef long pid_t
```

相关声明：[pid_t](#a114f9c2461df851d2ad00aad8dcfa3f7)。

<a id="r_a87cd503247b3afbb79788256ac093ad5"></a>

```c
typedef void(* sighandler_t) (int sig)
```

相关声明：[sighandler_t](#a87cd503247b3afbb79788256ac093ad5)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.4\_函数（Functions）

<a id="r_a4539db972bcf3dd8c8b429af0dc3789d"></a>

```c
int kill (pid_t pid, int sig)
```

相关声明：[kill](#a4539db972bcf3dd8c8b429af0dc3789d)、[pid_t](#a114f9c2461df851d2ad00aad8dcfa3f7)。

<a id="r_a4ba25c1b785eb5c68e93ee2a73fd7a34"></a>

```c
int killpg (pid_t pgrp, int sig)
```

相关声明：[killpg](#a4ba25c1b785eb5c68e93ee2a73fd7a34)、[pid_t](#a114f9c2461df851d2ad00aad8dcfa3f7)。

<a id="r_aa9255939ddcf0bdcd925f1fca741238c"></a>

```c
void psiginfo (const siginfo_t *info, const char *message)
```

相关声明：[psiginfo](#aa9255939ddcf0bdcd925f1fca741238c)、[siginfo_t](../posix_system_model_reference/P019_siginfo_t_结构体.md)。

<a id="r_afa550831803d7395d8ac098d6be59242"></a>

```c
void psignal (int sig, const char *message)
```

相关声明：[psignal](#afa550831803d7395d8ac098d6be59242)。

<a id="r_a5aafacc071cdfafd0eb992004dee3e62"></a>

```c
int pthread_kill (pthread_t thread, int sig)
```

相关声明：[pthread_kill](#a5aafacc071cdfafd0eb992004dee3e62)、[pthread_t](#ab3f45e72c67ecc7866d14ab09b3367e7)。

<a id="r_a16972ede9065cb2709fcfc6a84272116"></a>

```c
int pthread_sigmask (int how, const sigset_t *ZRESTRICT set, sigset_t *ZRESTRICT oset)
```

相关声明：[pthread_sigmask](#a16972ede9065cb2709fcfc6a84272116)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)。

<a id="r_a36954d8c880465d4396c26ca38a69dc0"></a>

```c
TOOLCHAIN_DISABLE_WARNING (TOOLCHAIN_WARNING_SHADOW)
```

相关声明：[TOOLCHAIN_DISABLE_WARNING](#a36954d8c880465d4396c26ca38a69dc0)、[TOOLCHAIN_WARNING_SHADOW](../api_memory_network_topic_reference/P020_工具链抽象（Toolchain abstraction）.md#gae917ae1adad468956fa5d28a50d10670)。

<a id="r_a5dabd0b7783afd0e4cab78446436e25c"></a>

```c
int sigaction (int sig, const struct sigaction *ZRESTRICT act, struct sigaction *ZRESTRICT oact)
```

相关声明：[sigaction](#a5dabd0b7783afd0e4cab78446436e25c)。

<a id="r_a18706c8aebf5582117b552c12925e54d"></a>

```c
TOOLCHAIN_ENABLE_WARNING (TOOLCHAIN_WARNING_SHADOW)
```

相关声明：[TOOLCHAIN_ENABLE_WARNING](#a18706c8aebf5582117b552c12925e54d)、[TOOLCHAIN_WARNING_SHADOW](../api_memory_network_topic_reference/P020_工具链抽象（Toolchain abstraction）.md#gae917ae1adad468956fa5d28a50d10670)。

<a id="r_aba080a9ab72ac6d079ff0bf8ac9b23f4"></a>

```c
int sigaddset (sigset_t *set, int sig)
```

相关声明：[sigaddset](#aba080a9ab72ac6d079ff0bf8ac9b23f4)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)。

<a id="r_af2a9e8d53e783f7ad3343ac36ecc74b0"></a>

```c
int sigaltstack (const stack_t *ZRESTRICT ss, stack_t *ZRESTRICT oss)
```

相关声明：[sigaltstack](#af2a9e8d53e783f7ad3343ac36ecc74b0)、[stack_t](../posix_system_model_reference/P021_stack_t_结构体.md)、[stack_t](../posix_system_model_reference/P021_stack_t_结构体.md)。

<a id="r_a16efce9e80266d0db1ed9a3ef281ad2b"></a>

```c
int sigdelset (sigset_t *set, int sig)
```

相关声明：[sigdelset](#a16efce9e80266d0db1ed9a3ef281ad2b)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)。

<a id="r_a5925352f90eb589393274fa0376d7def"></a>

```c
int sigemptyset (sigset_t *set)
```

相关声明：[sigemptyset](#a5925352f90eb589393274fa0376d7def)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)。

<a id="r_a88d7bbc77ea1569ee21c90db549ea023"></a>

```c
int sigfillset (sigset_t *set)
```

相关声明：[sigfillset](#a88d7bbc77ea1569ee21c90db549ea023)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)。

<a id="r_a8f2faa6ea120d4cb0cc916f46d3731a7"></a>

```c
int sighold (int sig)
```

相关声明：[sighold](#a8f2faa6ea120d4cb0cc916f46d3731a7)。

<a id="r_a1034c4dceaeebeee401fbf7c5e4396ed"></a>

```c
int sigignore (int sig)
```

相关声明：[sigignore](#a1034c4dceaeebeee401fbf7c5e4396ed)。

<a id="r_a5d5adc4eb4b54c2ce456db2c36905322"></a>

```c
int siginterrupt (int sig, int flag)
```

相关声明：[siginterrupt](#a5d5adc4eb4b54c2ce456db2c36905322)。

<a id="r_a5eaaad0671fbdba01a60ab5b1c8649be"></a>

```c
int sigismember (const sigset_t *set, int sig)
```

相关声明：[sigismember](#a5eaaad0671fbdba01a60ab5b1c8649be)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)。

<a id="r_aa11e3a8419c84b5af84dad8e7663a670"></a>

```c
int sigpause (int sig)
```

相关声明：[sigpause](#aa11e3a8419c84b5af84dad8e7663a670)。

<a id="r_a7b91eecad5998acd6162fde3ab530d7a"></a>

```c
int sigpending (sigset_t *set)
```

相关声明：[sigpending](#a7b91eecad5998acd6162fde3ab530d7a)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)。

<a id="r_a6e6b04897703c43b2ad10013041ad152"></a>

```c
int sigprocmask (int how, const sigset_t *ZRESTRICT set, sigset_t *ZRESTRICT oset)
```

相关声明：[sigprocmask](#a6e6b04897703c43b2ad10013041ad152)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)。

<a id="r_a4949c54b6d058d6fd166c59b7e7aac24"></a>

```c
int sigqueue (pid_t pid, int sig, union sigval value)
```

相关声明：[sigqueue](#a4949c54b6d058d6fd166c59b7e7aac24)、[pid_t](#a114f9c2461df851d2ad00aad8dcfa3f7)、[sigval](../posix_system_model_reference/P035_sigval_联合体.md)。

<a id="r_a8a0e594afe61149ff3f4e48c722c46b1"></a>

```c
int sigrelse (int sig)
```

相关声明：[sigrelse](#a8a0e594afe61149ff3f4e48c722c46b1)。

<a id="r_af1e91276412ec4c5ed1d4ae71fc0bdb4"></a>

```c
sighandler_t sigset (int sig, sighandler_t disp)
```

相关声明：[sighandler_t](#a87cd503247b3afbb79788256ac093ad5)、[sigset](#af1e91276412ec4c5ed1d4ae71fc0bdb4)、[sighandler_t](#a87cd503247b3afbb79788256ac093ad5)。

<a id="r_a651e913fac32255355993a3d7ca193c8"></a>

```c
int sigsuspend (const sigset_t *set)
```

相关声明：[sigsuspend](#a651e913fac32255355993a3d7ca193c8)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)。

<a id="r_a5858057ae172789da253b6b281d49875"></a>

```c
int sigtimedwait (const sigset_t *ZRESTRICT set, siginfo_t *ZRESTRICT info, const struct timespec *ZRESTRICT timeout)
```

相关声明：[sigtimedwait](#a5858057ae172789da253b6b281d49875)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)、[siginfo_t](../posix_system_model_reference/P019_siginfo_t_结构体.md)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

<a id="r_a8f5732f547a8cd36485e3e08490757f2"></a>

```c
int sigwait (const sigset_t *ZRESTRICT set, int *ZRESTRICT sig)
```

相关声明：[sigwait](#a8f5732f547a8cd36485e3e08490757f2)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)。

<a id="r_ae29ee6133f77ce4ef463a7bb9734716f"></a>

```c
int sigwaitinfo (const sigset_t *ZRESTRICT set, siginfo_t *ZRESTRICT info)
```

相关声明：[sigwaitinfo](#ae29ee6133f77ce4ef463a7bb9734716f)、[sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)、[siginfo_t](../posix_system_model_reference/P019_siginfo_t_结构体.md)。

## 5.5\_详细说明（Detailed Documentation）

<a id="a6ea334f3e9a67fbe0cce4c9738cc842a"></a>

### `BUS_ADRALN`

```c
#define BUS_ADRALN 20
```

地址对齐无效（Invalid Address Alignment）。

<a id="a2343c7bb80913e6f8d69ae3cd7bd6273"></a>

### `BUS_ADRERR`

```c
#define BUS_ADRERR 21
```

物理地址不存在（Nonexistent Physical Address）。

<a id="a1b507e6736ff85de98cc1b0151f61d44"></a>

### `BUS_OBJERR`

```c
#define BUS_OBJERR 22
```

对象特有的硬件错误（Object-Specific Hardware Error）。

<a id="afad5fd60fd725025f0682ec2697d1b45"></a>

### `CLD_CONTINUED`

```c
#define CLD_CONTINUED 30
```

已停止的子进程已继续执行（Continued）。

<a id="afe6e9bccf7df675f022a3e484a73461f"></a>

### `CLD_DUMPED`

```c
#define CLD_DUMPED 27
```

子进程已异常终止，并已创建核心转储文件（Core File）。

<a id="a3e6df4a3087d9aa8ba11c61c38c9218c"></a>

### `CLD_EXITED`

```c
#define CLD_EXITED 25
```

子进程已退出（Child Has Exited）。

<a id="a2d5941afd29bca8b8f74461cb97fe982"></a>

### `CLD_KILLED`

```c
#define CLD_KILLED 26
```

子进程已异常终止，且未创建核心转储文件（Core File）。

<a id="a1844847a22da24371fa347b959283916"></a>

### `CLD_STOPPED`

```c
#define CLD_STOPPED 29
```

子进程已停止（Stopped）。

<a id="aa679c19d95672068f1e4a4673a15ff1c"></a>

### `CLD_TRAPPED`

```c
#define CLD_TRAPPED 28
```

被跟踪的子进程触发了陷阱（Trap）。

<a id="af9bde83d81419c42660d5963159e3b12"></a>

### `FPE_FLTDIV`

```c
#define FPE_FLTDIV 11
```

浮点除以零（Floating-Point Divide by Zero）。

<a id="a4616f880b63120a93c1e4ac6a7aa3dae"></a>

### `FPE_FLTINV`

```c
#define FPE_FLTINV 16
```

无效浮点运算（Invalid Floating-Point Operation）。

<a id="adb3c2df5b8d0979b8b26f89096a513b9"></a>

### `FPE_FLTOVF`

```c
#define FPE_FLTOVF 12
```

浮点上溢（Floating-Point Overflow）。

<a id="add5139f33bb657877bb88e2c2b2084ab"></a>

### `FPE_FLTRES`

```c
#define FPE_FLTRES 15
```

浮点结果不精确（Floating-Point Inexact Result）。

<a id="a72463f25ca7c74964873c79b4fc3009d"></a>

### `FPE_FLTSUB`

```c
#define FPE_FLTSUB 17
```

下标超出范围（Subscript out of Range）。

<a id="aa48a81252484098176287529607bd275"></a>

### `FPE_FLTUND`

```c
#define FPE_FLTUND 13
```

浮点下溢（Floating-Point Underflow）。

<a id="abc24569f7a193eff6381dd2212464a0a"></a>

### `FPE_INTDIV`

```c
#define FPE_INTDIV 9
```

整数除以零（Integer Divide by Zero）。

<a id="aa85ab73a55a64cf580afa3596c0d5a03"></a>

### `FPE_INTOVF`

```c
#define FPE_INTOVF 10
```

整数溢出（Integer Overflow）。

<a id="ad16edcc255b0df2dd3572fc9256ef180"></a>

### `ILL_BADSTK`

```c
#define ILL_BADSTK 8
```

内部栈错误（Internal Stack Error）。

<a id="ae8aca6f3472a885fb6d3948f8e1a5fa9"></a>

### `ILL_COPROC`

```c
#define ILL_COPROC 7
```

协处理器错误（Coprocessor Error）。

<a id="ab225825a0696d9341ea4569abdc954f0"></a>

### `ILL_ILLADR`

```c
#define ILL_ILLADR 3
```

非法寻址模式（Illegal Addressing Mode）。

<a id="a41705eedb4a32e5b0b9a3ef98f98599c"></a>

### `ILL_ILLOPC`

```c
#define ILL_ILLOPC 1
```

非法操作码（Illegal Opcode）。

<a id="af5f5854f70f082160b7e0656907a4ced"></a>

### `ILL_ILLOPN`

```c
#define ILL_ILLOPN 2
```

非法操作数（Illegal Operand）。

<a id="adb1378440989b1b20f7ff358a91e3cb2"></a>

### `ILL_ILLTRP`

```c
#define ILL_ILLTRP 4
```

非法陷阱（Illegal Trap）。

<a id="af7d4b4283e951ed0cb3cc33b2b451fd2"></a>

### `ILL_PRVOPC`

```c
#define ILL_PRVOPC 5
```

特权操作码（Privileged Opcode）。

<a id="aa3bff56a3faabe1a3755fd77cda127b1"></a>

### `ILL_PRVREG`

```c
#define ILL_PRVREG 6
```

特权寄存器（Privileged Register）。

<a id="aae6a742a8c5acf12caba1d148dd03f10"></a>

### `MINSIGSTKSZ`

```c
#define MINSIGSTKSZ 4096
```

<a id="ab23ba62b3171d1c93c7fd9bd588c1b08"></a>

### `POLL_ERR`

```c
#define POLL_ERR 34
```

输入／输出错误（I/O Error）。

<a id="a0d20a75cd180ea52abb636e90c4b15b4"></a>

### `POLL_HUP`

```c
#define POLL_HUP 36
```

设备已断开连接（Device Disconnected）。

<a id="ad78b4cee7029b93a9b7e7b3a92df77eb"></a>

### `POLL_IN`

```c
#define POLL_IN 31
```

有数据可供输入（Data Input Available）。

<a id="a4fb3eb4526e54e7cd3ba550021fdd91d"></a>

### `POLL_MSG`

```c
#define POLL_MSG 33
```

有可用输入消息（Input Message Available）。

<a id="aa29f1b123e70df2a75508eb8e3e7c32b"></a>

### `POLL_OUT`

```c
#define POLL_OUT 32
```

有可用输出缓冲区（Output Buffers Available）。

<a id="a62827cb6f0ae13e8df4d310c4a089c07"></a>

### `POLL_PRI`

```c
#define POLL_PRI 35
```

有可用高优先级输入（High Priority Input Available）。

<a id="af6a71c97263725437f59ceb16241fd32"></a>

### `SA_NOCLDSTOP`

```c
#define SA_NOCLDSTOP 0x00000001
```

<a id="ae4c1aad864ef72e4a2cce74b1b8a5a0b"></a>

### `SA_NOCLDWAIT`

```c
#define SA_NOCLDWAIT 0x00000020
```

<a id="abec4abd80d73397fc2f78f57f178565f"></a>

### `SA_NODEFER`

```c
#define SA_NODEFER 0x00000040
```

<a id="a322c220e296393958ab4238145a0d273"></a>

### `SA_ONSTACK`

```c
#define SA_ONSTACK 0x00000002
```

<a id="a8d5fb4f35858d31035e7354c1d4048ea"></a>

### `SA_RESETHAND`

```c
#define SA_RESETHAND 0x00000004
```

<a id="a74ef0a27afcf55b6cd6d35cf0fa5d427"></a>

### `SA_RESTART`

```c
#define SA_RESTART 0x00000008
```

<a id="a59b4c0774aace526b10b6d737075a790"></a>

### `SA_SIGINFO`

```c
#define SA_SIGINFO 0x00000010
```

<a id="aba23f74fc8d8b7f8826f6275422a5648"></a>

### `SEGV_ACCERR`

```c
#define SEGV_ACCERR 19
```

映射对象的访问权限无效（Invalid Permissions for Mapped Object）。

<a id="a289e4151377c06f31fd4295061de78d9"></a>

### `SEGV_MAPERR`

```c
#define SEGV_MAPERR 18
```

地址未映射到对象（Address Not Mapped to Object）。

<a id="aa8ff6c6d4af21cf9380de1e8fef9db4c"></a>

### `SI_ASYNCIO`

```c
#define SI_ASYNCIO 40
```

异步 I/O 请求（Asynchronous I/O Request）完成时生成的信号。

<a id="afdf808efb3ebd166f67910156146c8fc"></a>

### `SI_MESGQ`

```c
#define SI_MESGQ 41
```

消息到达空消息队列（Message Queue）时生成的信号。

<a id="a4f23f53a46f88a96a0f28e23f7a9bad6"></a>

### `SI_QUEUE`

```c
#define SI_QUEUE 38
```

由 `sigqueue()` 发送的信号（Signal）。

<a id="ab57ec52e57fbb49071f96f255bc7c31b"></a>

### `SI_TIMER`

```c
#define SI_TIMER 39
```

由 `timer_settime()` 设置的定时器到期时生成的信号（Signal）。

<a id="af9e4986b4f6bb9bd932b2fc8166301b9"></a>

### `SI_USER`

```c
#define SI_USER 37
```

由 `kill()` 发送的信号（Signal）。

<a id="a927f6ae16379576d638006c7498ac5d7"></a>

### `SIG_BLOCK`

```c
#define SIG_BLOCK 1
```

<a id="a0fa971487344a463a7f0545c9c9ef2bf"></a>

### `SIG_HOLD`

```c
#define SIG_HOLD ((void *)-2)
```

<a id="a37750b78b7ae75fe02ad26e70f6cc845"></a>

### `SIG_SETMASK`

```c
#define SIG_SETMASK 0
```

<a id="a5fcd73313a63dac2cc7eb3b654215250"></a>

### `SIG_UNBLOCK`

```c
#define SIG_UNBLOCK 2
```

<a id="aa86c630133e5b5174ac970227b273446"></a>

### `SIGABRT`

```c
#define SIGABRT 6
```

已中止（Aborted）。

<a id="aa6946723c6b7a86ec3c33caaf832840b"></a>

### `SIGALRM`

```c
#define SIGALRM 14
```

闹钟（Alarm Clock）。

<a id="aead3d488474201acf18c4b63d91edc3c"></a>

### `SIGBUS`

```c
#define SIGBUS 7
```

总线错误（Bus Error）。

<a id="a0e63521a64cc8bc2b91d36a87d32c9f8"></a>

### `SIGCHLD`

```c
#define SIGCHLD 17
```

子进程状态已改变（Child Status Changed）。

<a id="a024f43063003e753afc6cca1acd6e104"></a>

### `SIGCONT`

```c
#define SIGCONT 18
```

已继续（Continued）。

<a id="aced9a66610d9d61756999ce4f103740e"></a>

### `SIGEV_NONE`

```c
#define SIGEV_NONE 1
```

<a id="a06d5881eeb84e6ac35f5b801c380dbb6"></a>

### `SIGEV_SIGNAL`

```c
#define SIGEV_SIGNAL 2
```

<a id="a29ccb6a17fa90a1357b478f62af7fca0"></a>

### `SIGEV_THREAD`

```c
#define SIGEV_THREAD 3
```

<a id="a7fbba29aec3e4a8daae12935299df92d"></a>

### `SIGFPE`

```c
#define SIGFPE 8
```

算术异常（Arithmetic Exception）。

<a id="a136c64ec2d1306de745e39d6aee362ca"></a>

### `SIGHUP`

```c
#define SIGHUP 1
```

挂断（Hangup）。

<a id="a4c9c5284f8c8d146bd7a93d25017fc62"></a>

### `SIGILL`

```c
#define SIGILL 4
```

非法指令（Illegal Instruction）。

<a id="a487309e3e9e0527535644115204a639a"></a>

### `SIGINT`

```c
#define SIGINT 2
```

中断（Interrupt）。

<a id="addd8dcd406ce514ab3b4f576a5343d42"></a>

### `SIGKILL`

```c
#define SIGKILL 9
```

被强制终止（Killed）。

<a id="a57e9c8c5fa13bf86bc779a9f6f408b7c"></a>

### `SIGPIPE`

```c
#define SIGPIPE 13
```

管道断开（Broken Pipe）。

<a id="a1614264a836d6a5642554775ef0134d0"></a>

### `SIGPOLL`

```c
#define SIGPOLL 29
```

发生了可轮询事件（Pollable Event）。

<a id="ab6bd2a2ff7e58d45965ef257f96dfe65"></a>

### `SIGPROF`

```c
#define SIGPROF 27
```

性能分析定时器到期（Profiling Timer Expired）。

<a id="a62045b465be11891160d53c10861b16c"></a>

### `SIGQUIT`

```c
#define SIGQUIT 3
```

退出（Quit）。

<a id="a5336d2c76af22b10373e3dd28fb3b0f0"></a>

### `SIGRTMAX`

```c
#define SIGRTMAX (SIGRTMIN + CONFIG_POSIX_RTSIG_MAX)
```

<a id="ae89f9a1282bd2d1b2a2b310c12ea16a5"></a>

### `SIGRTMIN`

```c
#define SIGRTMIN 32
```

<a id="ae20b4f7171a09516ea73c9d2745bd596"></a>

### `SIGSEGV`

```c
#define SIGSEGV 11
```

无效内存引用（Invalid Memory Reference）。

<a id="a8a433a10420a0c51355da26cfcab2131"></a>

### `SIGSTKSZ`

```c
#define SIGSTKSZ 4096
```

<a id="a069e358bc9a864b7dc4fed2440eda14c"></a>

### `SIGSTOP`

```c
#define SIGSTOP 19
```

停止执行（Stop Executing）。

<a id="a8bacf9eb18fd539099c1bb4666c45d60"></a>

### `SIGSYS`

```c
#define SIGSYS 31
```

错误的系统调用（Bad System Call）。

<a id="a682182a5e5f38fd61f4311501e9dac5d"></a>

### `SIGTERM`

```c
#define SIGTERM 15
```

已终止（Terminated）。

<a id="aa2beb906ab1b46676e63823f4e773c38"></a>

### `SIGTRAP`

```c
#define SIGTRAP 5
```

跟踪／断点陷阱（Trace/Breakpoint Trap）。

<a id="abe65c086e01f0d286b7a785a7e3cdd1a"></a>

### `SIGTSTP`

```c
#define SIGTSTP 20
```

已停止（Stopped）。

<a id="a2c146e34a6b5a78dfba41cded3331181"></a>

### `SIGTTIN`

```c
#define SIGTTIN 21
```

因读取而停止（Stopped，Read）。

<a id="a782864287613e2c5c030411fa9c5e9b1"></a>

### `SIGTTOU`

```c
#define SIGTTOU 22
```

因写入而停止（Stopped，Write）。

<a id="ad9ff13149e36144a4ea28788948c34dd"></a>

### `SIGURG`

```c
#define SIGURG 23
```

紧急 I/O 状态（Urgent I/O Condition）。

<a id="a944a8250e34bfd7991123abd3436d8c0"></a>

### `SIGUSR1`

```c
#define SIGUSR1 10
```

用户定义信号 1（User-Defined Signal 1）。

<a id="abaaa61abe503c43481e35e21b0b5a031"></a>

### `SIGUSR2`

```c
#define SIGUSR2 12
```

用户定义信号 2（User-Defined Signal 2）。

<a id="a71403d2f5240e409e213060ea3301851"></a>

### `SIGVTALRM`

```c
#define SIGVTALRM 26
```

虚拟定时器到期（Virtual Timer Expired）。

<a id="a7265cbba4972503c1c30a2e52a929874"></a>

### `SIGXCPU`

```c
#define SIGXCPU 24
```

超出 CPU 时间限制（CPU Time Limit）。

<a id="a75440a7aa885a1052dfd3b4393fd9baa"></a>

### `SIGXFSZ`

```c
#define SIGXFSZ 25
```

超出文件大小限制（File Size Limit）。

<a id="ac515f2efc91c54803f65de08d14d4566"></a>

### `SS_DISABLE`

```c
#define SS_DISABLE 0x00000002
```

<a id="a17bcfefa3c6fafd5d3277d867bd723fb"></a>

### `SS_ONSTACK`

```c
#define SS_ONSTACK 0x00000001
```

<a id="a79fcb87a23520cade78f77a4dd3142c6"></a>

### `TRAP_BRKPT`

```c
#define TRAP_BRKPT 23
```

进程断点（Process Breakpoint）。

<a id="a16042a25974d31a1aff6f09bb6a7358a"></a>

### `TRAP_TRACE`

```c
#define TRAP_TRACE 24
```

进程跟踪陷阱（Process Trace Trap）。

<a id="a114f9c2461df851d2ad00aad8dcfa3f7"></a>

### `pid_t`

```c
typedef long pid_t
```

<a id="ab3f45e72c67ecc7866d14ab09b3367e7"></a>

### `pthread_t`

```c
typedef unsigned int pthread_t
```

<a id="a87cd503247b3afbb79788256ac093ad5"></a>

### `sighandler_t`

```c
typedef void(* sighandler_t) (int sig)
```

<a id="afc544433253791fc5f87b8203c9b6e63"></a>

### `uid_t`

```c
typedef int uid_t
```

<a id="a4539db972bcf3dd8c8b429af0dc3789d"></a>

### `kill()`

```c
int kill ( pid_t pid, int sig )
```

<a id="a4ba25c1b785eb5c68e93ee2a73fd7a34"></a>

### `killpg()`

```c
int killpg ( pid_t pgrp, int sig )
```

<a id="aa9255939ddcf0bdcd925f1fca741238c"></a>

### `psiginfo()`

```c
void psiginfo ( const siginfo_t * info, const char * message )
```

<a id="afa550831803d7395d8ac098d6be59242"></a>

### `psignal()`

```c
void psignal ( int sig, const char * message )
```

<a id="a5aafacc071cdfafd0eb992004dee3e62"></a>

### `pthread_kill()`

```c
int pthread_kill ( pthread_t thread, int sig )
```

<a id="a16972ede9065cb2709fcfc6a84272116"></a>

### `pthread_sigmask()`

```c
int pthread_sigmask ( int how, const sigset_t *ZRESTRICT set, sigset_t *ZRESTRICT oset )
```

<a id="a5dabd0b7783afd0e4cab78446436e25c"></a>

### `sigaction()`

```c
int sigaction ( int sig, const struct sigaction *ZRESTRICT act, struct sigaction *ZRESTRICT oact )
```

<a id="aba080a9ab72ac6d079ff0bf8ac9b23f4"></a>

### `sigaddset()`

```c
int sigaddset ( sigset_t * set, int sig )
```

<a id="af2a9e8d53e783f7ad3343ac36ecc74b0"></a>

### `sigaltstack()`

```c
int sigaltstack ( const stack_t *ZRESTRICT ss, stack_t *ZRESTRICT oss )
```

<a id="a16efce9e80266d0db1ed9a3ef281ad2b"></a>

### `sigdelset()`

```c
int sigdelset ( sigset_t * set, int sig )
```

<a id="a5925352f90eb589393274fa0376d7def"></a>

### `sigemptyset()`

```c
int sigemptyset ( sigset_t * set)
```

<a id="a88d7bbc77ea1569ee21c90db549ea023"></a>

### `sigfillset()`

```c
int sigfillset ( sigset_t * set)
```

<a id="a8f2faa6ea120d4cb0cc916f46d3731a7"></a>

### `sighold()`

```c
int sighold ( int sig)
```

<a id="a1034c4dceaeebeee401fbf7c5e4396ed"></a>

### `sigignore()`

```c
int sigignore ( int sig)
```

<a id="a5d5adc4eb4b54c2ce456db2c36905322"></a>

### `siginterrupt()`

```c
int siginterrupt ( int sig, int flag )
```

<a id="a5eaaad0671fbdba01a60ab5b1c8649be"></a>

### `sigismember()`

```c
int sigismember ( const sigset_t * set, int sig )
```

<a id="aa11e3a8419c84b5af84dad8e7663a670"></a>

### `sigpause()`

```c
int sigpause ( int sig)
```

<a id="a7b91eecad5998acd6162fde3ab530d7a"></a>

### `sigpending()`

```c
int sigpending ( sigset_t * set)
```

<a id="a6e6b04897703c43b2ad10013041ad152"></a>

### `sigprocmask()`

```c
int sigprocmask ( int how, const sigset_t *ZRESTRICT set, sigset_t *ZRESTRICT oset )
```

<a id="a4949c54b6d058d6fd166c59b7e7aac24"></a>

### `sigqueue()`

```c
int sigqueue ( pid_t pid, int sig, union sigval value )
```

<a id="a8a0e594afe61149ff3f4e48c722c46b1"></a>

### `sigrelse()`

```c
int sigrelse ( int sig)
```

<a id="af1e91276412ec4c5ed1d4ae71fc0bdb4"></a>

### `sigset()`

```c
sighandler_t sigset ( int sig, sighandler_t disp )
```

<a id="a651e913fac32255355993a3d7ca193c8"></a>

### `sigsuspend()`

```c
int sigsuspend ( const sigset_t * set)
```

<a id="a5858057ae172789da253b6b281d49875"></a>

### `sigtimedwait()`

```c
int sigtimedwait ( const sigset_t *ZRESTRICT set, siginfo_t *ZRESTRICT info, const struct timespec *ZRESTRICT timeout )
```

<a id="a8f5732f547a8cd36485e3e08490757f2"></a>

### `sigwait()`

```c
int sigwait ( const sigset_t *ZRESTRICT set, int *ZRESTRICT sig )
```

<a id="ae29ee6133f77ce4ef463a7bb9734716f"></a>

### `sigwaitinfo()`

```c
int sigwaitinfo ( const sigset_t *ZRESTRICT set, siginfo_t *ZRESTRICT info )
```

<a id="a36954d8c880465d4396c26ca38a69dc0"></a>

### `TOOLCHAIN_DISABLE_WARNING()`

```c
TOOLCHAIN_DISABLE_WARNING ( TOOLCHAIN_WARNING_SHADOW )
```

<a id="a18706c8aebf5582117b552c12925e54d"></a>

### `TOOLCHAIN_ENABLE_WARNING()`

```c
TOOLCHAIN_ENABLE_WARNING ( TOOLCHAIN_WARNING_SHADOW )
```


## 5.6\_原页交叉引用（Cross References）

- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_http_wifi_reference/P008_posix_signal.h_源码浏览.md)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [sigset_t](../posix_system_model_reference/P020_sigset_t_结构体.md)
- [pthread_attr_t](../posix_system_model_reference/P011_pthread_attr_t_结构体.md)
- [sigval](../posix_system_model_reference/P035_sigval_联合体.md)
- [sigevent](../posix_system_model_reference/P018_sigevent_结构体.md)
- [siginfo_t](../posix_system_model_reference/P019_siginfo_t_结构体.md)
- [sigaction](../posix_system_model_reference/P017_sigaction_结构体.md)
- [mcontext_t](../platform_security_model_reference/P017_mcontext_t_结构体.md)
- [stack_t](../posix_system_model_reference/P021_stack_t_结构体.md)
- [ucontext_t](../posix_system_model_reference/P027_ucontext_t_结构体.md)
- [timer_settime()](../api_file_reference/P311_zephyr__posix__posix_time.h_文件参考.md#a32207b51f2effa8441f4c728fd8519c0)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [TOOLCHAIN_WARNING_SHADOW](../api_memory_network_topic_reference/P020_工具链抽象（Toolchain abstraction）.md#gae917ae1adad468956fa5d28a50d10670)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_zephyr__net__net_event.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__dt-bindings__pinctrl__stm32f1-afio.h_文件参考.md)
