---
id: learning.zephyr-docs.kconfig-reference.page-414
title: "`subsys/portability`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第414章\_`subsys/portability`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `subsys/portability` 的 26 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_POSIX_THREADS_EXT"></a>

## 414.1 `CONFIG_POSIX_THREADS_EXT`

**提示（Prompt）**：扩展 POSIX 线程支持（Extended thread support）

**说明（Help）**

启用后可使用 `pthread_attr_getguardsize()`、`pthread_attr_setguardsize()`、`pthread_mutexattr_gettype()` 或 `pthread_mutexattr_settype()`。更多信息参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_THREAD_ATTR_STACKADDR"></a>

## 414.2 `CONFIG_POSIX_THREAD_ATTR_STACKADDR`

**提示（Prompt）**：支持获取与设置 POSIX 线程栈地址（Thread stack address）

**说明（Help）**

启用后可使用 `pthread_attr_getstackaddr()` 和 `pthread_attr_setstackaddr()`。IEEE 1003.1-2017 已移除此选项，改用 `pthread_attr_getstack()` 和 `pthread_attr_setstack()`。更多信息参见 [旧版栈地址接口](https://pubs.opengroup.org/onlinepubs/009696799/functions/pthread_attr_getstackaddr.html)、[POSIX 系统接口说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_xsh_chap03.html) 和 [线程栈相关说明](https://pubs.opengroup.org/onlinepubs/9699919799/functions/V2_chap02.html#tag_15_09_08)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)。

<a id="CONFIG_POSIX_THREAD_ATTR_STACKSIZE"></a>

## 414.3 `CONFIG_POSIX_THREAD_ATTR_STACKSIZE`

**提示（Prompt）**：支持获取与设置 POSIX 线程栈大小（Thread stack size）

**说明（Help）**

启用后可使用 `pthread_attr_getstacksize()` 或 `pthread_attr_setstacksize()`。更多信息参见 [POSIX 线程栈大小接口](https://pubs.opengroup.org/onlinepubs/009696699/functions/pthread_attr_getstacksize.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)。

<a id="CONFIG_POSIX_THREAD_CPUTIME"></a>

## 414.4 `CONFIG_POSIX_THREAD_CPUTIME`

**提示（Prompt）**：POSIX 每线程 CPU 时间时钟（Per-thread CPU-time clock）

**说明（Help）**

启用 `CLOCK_THREAD_CPUTIME_ID`。更多信息参见 [POSIX 可移植性说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html)、[CPU 时间定义](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html#tag_03_118) 和 [CPU 时间时钟相关接口说明](https://pubs.opengroup.org/onlinepubs/9699919799/functions/V2_chap02.html#tag_15_08_05_04)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_TIMERS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.timer:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.timer#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_TIMERS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_TIMERS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)。

<a id="CONFIG_POSIX_THREAD_KEYS_MAX"></a>

## 414.5 `CONFIG_POSIX_THREAD_KEYS_MAX`

**提示（Prompt）**：POSIX 线程专用存储键（Thread-specific-storage key）的最大数量

**说明（Help）**

POSIX 应用中可同时处于活动状态的线程专用存储键（Thread-specific-storage key）最大数量。更多信息参见 [POSIX limits.h](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/limits.h.html)。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING"></a>

## 414.6 `CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING`

**提示（Prompt）**：使用不同优先级和调度器（Scheduler）运行 POSIX 线程

**说明（Help）**

启用后，应用可通过 `pthread_setschedparam()`、`pthread_setschedprio()` 等函数，为不同线程配置不同优先级和调度算法（Scheduling algorithm）。实时线程（Realtime Threads）和高级实时线程（Advanced Realtime Threads）需要此功能。更多信息参见 [POSIX 实时要求](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap02.html#tag_02_01_06) 和 [posixoptions(7)](https://man7.org/linux/man-pages/man7/posixoptions.7.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)。

<a id="CONFIG_POSIX_THREAD_PRIO_INHERIT"></a>

## 414.7 `CONFIG_POSIX_THREAD_PRIO_INHERIT`

**提示（Prompt）**：POSIX 互斥锁优先级继承（Mutex priority inheritance）

**说明（Help）**

选择 `y` 以启用 POSIX 互斥锁优先级继承（Priority inheritance）。更多信息参见 [互斥锁协议属性接口](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_getprotocol.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)。

<a id="CONFIG_POSIX_THREAD_PRIO_PROTECT"></a>

## 414.8 `CONFIG_POSIX_THREAD_PRIO_PROTECT`

**提示（Prompt）**：POSIX 互斥锁优先级保护（Mutex priority protection）

**说明（Help）**

选择 `y` 以启用 POSIX 互斥锁优先级保护（Priority protection）。更多信息参见 [互斥锁协议属性接口](https://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_mutexattr_getprotocol.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)。

<a id="CONFIG_POSIX_THREAD_SAFE_FUNCTIONS"></a>

## 414.9 `CONFIG_POSIX_THREAD_SAFE_FUNCTIONS`

**提示（Prompt）**：POSIX 线程安全函数（Thread-safe functions）

**说明（Help）**

选择 `y` 以启用 POSIX 线程安全函数（Thread-safe function），包括 `asctime_r()`、`ctime_r()`、`flockfile()`、`ftrylockfile()`、`funlockfile()`、`getc_unlocked()`、`getchar_unlocked()`、`getgrgid_r()`、`getgrnam_r()`、`getpwnam_r()`、`getpwuid_r()`、`gmtime_r()`、`localtime_r()`、`putc_unlocked()`、`putchar_unlocked()`、`rand_r()`、`readdir_r()`、`strerror_r()` 和 `strtok_r()`。更多信息参见 [POSIX 线程安全相关说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_xsh_chap02.html#tag_22_02_09_07)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_POSIX_FILE_SYSTEM_R
CONFIG_POSIX_C_LANG_SUPPORT_R
```

**被选择（Selected by）**

```text
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_FILE_SYSTEM_R`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_FILE_SYSTEM_R)、[`CONFIG_POSIX_C_LANG_SUPPORT_R`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_C_LANG_SUPPORT_R)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<a id="CONFIG_POSIX_THREAD_THREADS_MAX"></a>

## 414.10 `CONFIG_POSIX_THREAD_THREADS_MAX`

**提示（Prompt）**：POSIX 线程（Thread）的最大数量

**说明（Help）**

POSIX 应用中可同时处于活动状态的线程（Thread）的最大数量。更多信息参见 [POSIX limits.h](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/limits.h.html)。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_TIMEOUTS"></a>

## 414.11 `CONFIG_POSIX_TIMEOUTS`

**提示（Prompt）**：为部分阻塞 POSIX 服务支持超时（Timeout）

**说明（Help）**

为部分阻塞操作（Blocking operation）启用必需的超时支持。更多信息参见 [POSIX 可移植性说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_port.html) 和 [基本定义相关说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_xbd_chap02.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_TIMERS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.timer:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.timer#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_TIMERS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_TIMERS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<a id="CONFIG_POSIX_TIMERS"></a>

## 414.12 `CONFIG_POSIX_TIMERS`

**提示（Prompt）**：POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `clock_getres()`、`clock_gettime()`、`clock_settime()`、`nanosleep()`、`timer_create()`、`timer_delete()`、`timer_getoverrun()`、`timer_settime()` 和 `timer_gettime()` 的实现。更多信息参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_SIMPLELINK_HOST_DRIVER
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_NXP_WIFI_SIGMA_AGENT
CONFIG_POSIX_BASE_DEFINITIONS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.timer:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.timer#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_SIMPLELINK_HOST_DRIVER`](P211_modules_Kconfig.simplelink_配置项参考.md#CONFIG_SIMPLELINK_HOST_DRIVER)、[`CONFIG_NXP_WIFI_SIGMA_AGENT`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SIGMA_AGENT)、[`CONFIG_POSIX_BASE_DEFINITIONS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BASE_DEFINITIONS)。

<a id="CONFIG_POSIX_TIMER_MAX"></a>

## 414.13 `CONFIG_POSIX_TIMER_MAX`

**提示（Prompt）**：每个进程的 POSIX 定时器（Timer）最大数量

**说明（Help）**

POSIX 应用中可同时处于活动状态的 `timer_t` 的最大数量。更多信息参见 [POSIX limits.h](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/limits.h.html)。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_TIMERS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.timer:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.timer#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_TIMERS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_TIMERS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_POSIX_UNAME_NODENAME_LEN"></a>

## 414.14 `CONFIG_POSIX_UNAME_NODENAME_LEN`

**提示（Prompt）**：`uname` 的节点名（Nodename）字符串长度

**说明（Help）**

定义 `nodename` 字符串的最大长度。原文将其称为“nodename version”。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SINGLE_PROCESS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
6 if !CONFIG_NET_HOSTNAME_UNIQUE
22 if CONFIG_NET_HOSTNAME_UNIQUE
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.proc1:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.proc1#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 单进程（Single process）支持

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SINGLE_PROCESS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SINGLE_PROCESS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NET_HOSTNAME_UNIQUE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_HOSTNAME_UNIQUE)。

<a id="CONFIG_POSIX_UNAME_SHELL"></a>

## 414.15 `CONFIG_POSIX_UNAME_SHELL`

**提示（Prompt）**：`uname` 命令支持

**说明（Help）**

支持在终端（Terminal）中使用 `uname` 命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SINGLE_PROCESS && CONFIG_SHELL && CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_SHELL_GETOPT
CONFIG_POSIX_SHELL
```

**定义位置（Location）**：[`subsys/portability/posix/shell/Kconfig.uname:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/shell/Kconfig.uname#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 命令行工具（Shell Utilities）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SINGLE_PROCESS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SINGLE_PROCESS)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_SHELL_GETOPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_GETOPT)、[`CONFIG_POSIX_SHELL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SHELL)。

<a id="CONFIG_POSIX_UNAME_VERSION_LEN"></a>

## 414.16 `CONFIG_POSIX_UNAME_VERSION_LEN`

**提示（Prompt）**：`uname` 的版本（Version）字符串长度

**说明（Help）**

定义 `uname` 版本（Version）字符串的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SINGLE_PROCESS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
70
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.proc1:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.proc1#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 单进程（Single process）支持

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SINGLE_PROCESS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SINGLE_PROCESS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_PTHREAD_CREATE_BARRIER"></a>

## 414.17 `CONFIG_PTHREAD_CREATE_BARRIER`

**提示（Prompt）**：使用 POSIX 屏障（Barrier）串行化 `pthread_create()`

**说明（Help）**

例如通过 Twister 在多个并行 QEMU 实例中运行对称多处理（SMP）应用，并发创建和联结（Join）大量 POSIX 线程时，可能需要在 `pthread_create()` 与 `zephyr_thread_wrapper()` 之间显式串行化（Serialization）。此类系统可选择 `Y`，通过 `pthread_barrier_wait()` 引入显式串行化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_BARRIERS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_NXP_WIFI_SIGMA_AGENT
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.barrier:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.barrier#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 屏障（barriers）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_BARRIERS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_BARRIERS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_NXP_WIFI_SIGMA_AGENT`](P191_drivers_wifi_配置项参考_4.md#CONFIG_NXP_WIFI_SIGMA_AGENT)。

<a id="CONFIG_PTHREAD_RECYCLER_DELAY_MS"></a>

## 414.18 `CONFIG_PTHREAD_RECYCLER_DELAY_MS`

**提示（Prompt）**：回收动态 POSIX 线程栈（Dynamic pthread stack）的延迟（毫秒）

**说明（Help）**

POSIX 线程通过 `k_thread_abort()` 终止前，会向系统工作队列（System Workqueue，SWQ）添加延迟执行的工作，以便将该线程分配的资源，例如来自内存池或堆的线程栈，归还系统。调用 `pthread_create()` 时也会释放资源，因此无需担心资源饥饿（Resource starvation）。本选项设置该工作延后执行的毫秒数。注意，此选项应视为临时方案；有了更加同步的解决方案后，很可能被移除。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_THREADS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.pthread:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.pthread#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 线程支持（thread support）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_THREADS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_THREADS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_TIMER_CREATE_WAIT"></a>

## 414.19 `CONFIG_TIMER_CREATE_WAIT`

**提示（Prompt）**：POSIX 应用等待定时器可用的时间（毫秒）

**说明（Help）**

控制符合 POSIX 的应用在创建新定时器（Timer）时，等待资源可用的时长。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_TIMERS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[0, 1000]
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.timer:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.timer#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_TIMERS`](P414_subsys_portability_配置项参考_2.md#CONFIG_POSIX_TIMERS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_XOPEN_STREAMS"></a>

## 414.20 `CONFIG_XOPEN_STREAMS`

**提示（Prompt）**：X/Open 流（Streams）［已弃用，Deprecated］

**说明（Help）**

此选项已弃用，请改用 `XSI_STREAMS`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_XSI_STREAMS
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.xsi_streams:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.xsi_streams#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_XSI_STREAMS`](P414_subsys_portability_配置项参考_2.md#CONFIG_XSI_STREAMS)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_XSI_REALTIME"></a>

## 414.21 `CONFIG_XSI_REALTIME`

**提示（Prompt）**：X/Open 实时功能（Realtime）

**说明（Help）**

选择 `y` 后，提供以下函数：

`fsync()`、`mlockall()`、`munlockall()`、`mlock()`、`munlock()`、`mq_close()`、`mq_getattr()`、`mq_notify()`、`mq_open()`、`mq_receive()`、`mq_send()`、`mq_setattr()`、`mq_unlink()`、`sched_get_priority_max()`、`sched_get_priority_min()`、`sched_getparam()`、`sched_getscheduler()`、`sched_rr_get_interval()`、`sched_setparam()`、`sched_setscheduler()`、`sched_yield()`、`mmap()`、`munmap()`、`shm_open()` 和 `shm_unlink()`。

`fsync()`、`fdatasync()` 和 `open()` 将提供同步 I/O（Synchronized I/O）能力。更多信息参见 [POSIX 符合性说明](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap02.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_POSIX_FSYNC
CONFIG_POSIX_MEMLOCK
CONFIG_POSIX_MEMLOCK_RANGE
CONFIG_POSIX_MESSAGE_PASSING
CONFIG_POSIX_PRIORITY_SCHEDULING
CONFIG_POSIX_SHARED_MEMORY_OBJECTS
CONFIG_POSIX_SYNCHRONIZED_IO
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.xsi_realtime:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.xsi_realtime#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_FSYNC`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_FSYNC)、[`CONFIG_POSIX_MEMLOCK`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MEMLOCK)、[`CONFIG_POSIX_MEMLOCK_RANGE`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MEMLOCK_RANGE)、[`CONFIG_POSIX_MESSAGE_PASSING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_MESSAGE_PASSING)、[`CONFIG_POSIX_PRIORITY_SCHEDULING`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_PRIORITY_SCHEDULING)、[`CONFIG_POSIX_SHARED_MEMORY_OBJECTS`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SHARED_MEMORY_OBJECTS)、[`CONFIG_POSIX_SYNCHRONIZED_IO`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYNCHRONIZED_IO)。

<a id="CONFIG_XSI_SINGLE_PROCESS"></a>

## 414.22 `CONFIG_XSI_SINGLE_PROCESS`

**提示（Prompt）**：X/Open 单进程（Single process）

**说明（Help）**

选择 `y` 后，Zephyr 提供 `gethostid()`、`gettimeofday()` 和 `putenv()` 的实现。更多信息参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**主动选择（Selects）**

```text
CONFIG_HWINFO
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**被弱选择（Implied by）**

```text
CONFIG_POSIX_API
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.xsi_single_process:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.xsi_single_process#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_POSIX_API`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_API)。

<a id="CONFIG_XSI_STREAMS"></a>

## 414.23 `CONFIG_XSI_STREAMS`

**提示（Prompt）**：X/Open 流（Streams）

**说明（Help）**

支持 X/Open 流接口（Streams interface），包括 `fattach()`、`fdetach()`、`getmsg()`、`getpmsg()`、`putmsg()` 和 `putpmsg()` 等函数。更多信息参见 [X/Open Streams 相关说明](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap02.html#tag_02_01_05_09)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_XOPEN_STREAMS
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.xsi_streams:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.xsi_streams#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_XOPEN_STREAMS`](P414_subsys_portability_配置项参考_2.md#CONFIG_XOPEN_STREAMS)。

<a id="CONFIG_XSI_SYSTEM_LOGGING"></a>

## 414.24 `CONFIG_XSI_SYSTEM_LOGGING`

**提示（Prompt）**：X/Open 系统日志（System logging）

**说明（Help）**

支持 `closelog()`、`openlog()`、`syslog()`、`setlogmask()` 和 `vsyslog()`。更多信息参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.xsi_system_logging:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.xsi_system_logging#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<a id="CONFIG_XSI_THREADS_EXT"></a>

## 414.25 `CONFIG_XSI_THREADS_EXT`

**提示（Prompt）**：X/Open 线程扩展（Threads extensions）

**说明（Help）**

支持 `pthread_attr_getstack()`、`pthread_attr_setstack()`、`pthread_getconcurrency()` 和 `pthread_setconcurrency()`。更多信息参见 [POSIX 子配置文件说明](https://pubs.opengroup.org/onlinepubs/9699919799/xrat/V4_subprofiles.html)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**被选择（Selected by）**

```text
CONFIG_POSIX_AEP_REALTIME_MINIMAL
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.xsi_threads_ext:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.xsi_threads_ext#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_POSIX_AEP_REALTIME_MINIMAL`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_AEP_REALTIME_MINIMAL)。

<a id="CONFIG_ZVFS_OPEN_ADD_SIZE_POSIX"></a>

## 414.26 `CONFIG_ZVFS_OPEN_ADD_SIZE_POSIX`

**提示（Prompt）**：POSIX 使用的文件描述符（File descriptor）数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/portability/posix/options/Kconfig.device_io:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/portability/posix/options/Kconfig.device_io#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 设备 I/O（Device I/O）

**配置项引用（Symbol References）**：[`CONFIG_POSIX_SYSTEM_INTERFACES`](P413_subsys_portability_配置项参考_1.md#CONFIG_POSIX_SYSTEM_INTERFACES)。

<!-- kconfig-navigation -->

[上一章](P413_subsys_portability_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P415_subsys_precision_timing_配置项参考.md)
