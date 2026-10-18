---
id: learning.zephyr-docs.api-source-packet-gnss-reference.page-7
title: posix_features.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix__features_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_posix\_features.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/posix__features_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P309_zephyr__posix__posix_features.h_文件参考.md)。

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
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2024 BayLibre SAS
 * Copyright (c) 2024 Tenstorrent AI ULC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_POSIX_POSIX_FEATURES_H_
#define ZEPHYR_INCLUDE_POSIX_POSIX_FEATURES_H_

#include <zephyr/autoconf.h>       /* CONFIG_* */
#include <zephyr/sys/util_macro.h> /* COND_CODE_1() */

/*
 * POSIX Application Environment Profiles (AEP - IEEE Std 1003.13-2003)
 */

#ifdef CONFIG_POSIX_AEP_REALTIME_MINIMAL
#define _POSIX_AEP_REALTIME_MINIMAL 200312L
#endif

#ifdef CONFIG_POSIX_AEP_REALTIME_CONTROLLER
#define _POSIX_AEP_REALTIME_CONTROLLER 200312L
#endif

#ifdef CONFIG_POSIX_AEP_REALTIME_DEDICATED
#define _POSIX_AEP_REALTIME_DEDICATED 200312L
#endif

/*
 * Subprofiling Considerations
 */
#define _POSIX_SUBPROFILE 1

/*
 * POSIX System Interfaces
 */

#define _POSIX_VERSION 200809L

#define _POSIX_CHOWN_RESTRICTED (0)
#define _POSIX_NO_TRUNC         (0)
#define _POSIX_VDISABLE         ('\0')

/* _POSIX_ADVISORY_INFO: not supported */

#ifdef CONFIG_POSIX_ASYNCHRONOUS_IO
#define _POSIX_ASYNCHRONOUS_IO _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_BARRIERS
#define _POSIX_BARRIERS _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_FSYNC
#define _POSIX_FSYNC _POSIX_VERSION
#endif

#ifdef CONFIG_NET_IPV6
#define _POSIX_IPV6 _POSIX_VERSION
#endif

/* _POSIX_JOB_CONTROL: not supported */

#ifdef CONFIG_POSIX_MAPPED_FILES
#define _POSIX_MAPPED_FILES _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_MEMLOCK
#define _POSIX_MEMLOCK _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_MEMLOCK_RANGE
#define _POSIX_MEMLOCK_RANGE _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_MEMORY_PROTECTION
#define _POSIX_MEMORY_PROTECTION _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_MESSAGE_PASSING
#define _POSIX_MESSAGE_PASSING _POSIX_VERSION
#endif

/* _POSIX_PRIORITIZED_IO: not supported */

#ifdef CONFIG_POSIX_PRIORITY_SCHEDULING
#define _POSIX_PRIORITY_SCHEDULING _POSIX_VERSION
#endif

#ifdef CONFIG_NET_SOCKETS_PACKET
#define _POSIX_RAW_SOCKETS _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_RW_LOCKS
#define _POSIX_READER_WRITER_LOCKS _POSIX_VERSION
#endif

/* _POSIX_REGEXP: not supported */
/* _POSIX_SAVED_IDS: not supported */

#ifdef CONFIG_POSIX_SEMAPHORES
#define _POSIX_SEMAPHORES _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_SHARED_MEMORY_OBJECTS
#define _POSIX_SHARED_MEMORY_OBJECTS _POSIX_VERSION
#endif

/* _POSIX_SHELL: not supported */
/* _POSIX_SPAWN: not supported */

#ifdef CONFIG_POSIX_SPIN_LOCKS
#define _POSIX_SPIN_LOCKS _POSIX_VERSION
#endif

/* _POSIX_SPORADIC_SERVER: not supported */

#ifdef CONFIG_POSIX_SYNCHRONIZED_IO
#define _POSIX_SYNCHRONIZED_IO _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_THREAD_ATTR_STACKADDR
#define _POSIX_THREAD_ATTR_STACKADDR _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_THREAD_ATTR_STACKSIZE
#define _POSIX_THREAD_ATTR_STACKSIZE _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_THREAD_CPUTIME
#define _POSIX_THREAD_CPUTIME _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_THREAD_PRIO_INHERIT
#define _POSIX_THREAD_PRIO_INHERIT _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_THREAD_PRIO_PROTECT
#define _POSIX_THREAD_PRIO_PROTECT _POSIX_VERSION
#endif

#ifdef CONFIG_POSIX_THREAD_PRIORITY_SCHEDULING
#define _POSIX_THREAD_PRIORITY_SCHEDULING _POSIX_VERSION
#endif

/* _POSIX_THREAD_PROCESS_SHARED: not supported */
/* _POSIX_THREAD_ROBUST_PRIO_INHERIT: not supported */
/* _POSIX_THREAD_ROBUST_PRIO_PROTECT: not supported */

/* _POSIX_THREAD_SPORADIC_SERVER: not supported */

#ifdef CONFIG_POSIX_THREADS
#ifndef _POSIX_THREADS
#define _POSIX_THREADS _POSIX_VERSION
#endif
#endif

#ifdef CONFIG_POSIX_TIMEOUTS
#define _POSIX_TIMEOUTS _POSIX_VERSION
#endif

/* _POSIX_TRACE: not supported */
/* _POSIX_TRACE_EVENT_FILTER: not supported */
/* _POSIX_TRACE_INHERIT: not supported */
/* _POSIX_TRACE_LOG: not supported */
/* _POSIX_TYPED_MEMORY_OBJECTS: not supported */

/*
 * POSIX v6 Options
 */
/* _POSIX_V6_ILP32_OFF32: not supported */
/* _POSIX_V6_ILP32_OFFBIG: not supported */
/* _POSIX_V6_LP64_OFF64: not supported */
/* _POSIX_V6_LPBIG_OFFBIG: not supported */

/*
 * POSIX v7 Options
 */
/* _POSIX_V7_ILP32_OFF32: not supported */
/* _POSIX_V7_ILP32_OFFBIG: not supported */
/* _POSIX_V7_LP64_OFF64: not supported */
/* _POSIX_V7_LPBIG_OFFBIG: not supported */

/*
 * POSIX2 Options
 */
/* _POSIX2_VERSION: not supported */
#define _POSIX2_C_BIND _POSIX_VERSION
/* _POSIX2_C_DEV: not supported */
/* _POSIX2_CHAR_TERM: not supported */
/* _POSIX2_FORT_DEV: not supported */
/* _POSIX2_FORT_RUN: not supported */
/* _POSIX2_LOCALEDEF: not supported */
/* _POSIX2_PBS: not supported */
/* _POSIX2_PBS_ACCOUNTING: not supported */
/* _POSIX2_PBS_CHECKPOINT: not supported */
/* _POSIX2_PBS_LOCATE: not supported */
/* _POSIX2_PBS_MESSAGE: not supported */
/* _POSIX2_PBS_TRACK: not supported */
/* _POSIX2_SW_DEV: not supported */
/* _POSIX2_UPE: not supported */

/*
 * X/Open System Interfaces
 */
#define _XOPEN_VERSION 700
/* _XOPEN_CRYPT: not supported */
/* _XOPEN_ENH_I18N: not supported */
#if defined(CONFIG_XSI_REALTIME) ||                                                                \
        (defined(CONFIG_POSIX_FSYNC) && defined(CONFIG_POSIX_MEMLOCK) &&                           \
         defined(CONFIG_POSIX_MEMLOCK_RANGE) && defined(CONFIG_POSIX_MESSAGE_PASSING) &&           \
         defined(CONFIG_POSIX_PRIORITY_SCHEDULING) &&                                              \
         defined(CONFIG_POSIX_SHARED_MEMORY_OBJECTS) && defined(CONFIG_POSIX_SYNCHRONIZED_IO))
#define _XOPEN_REALTIME _XOPEN_VERSION
#endif
/* _XOPEN_REALTIME_THREADS: not supported */
/* _XOPEN_SHM: not supported */

#ifdef CONFIG_XOPEN_STREAMS
#define _XOPEN_STREAMS _XOPEN_VERSION
#endif

/* _XOPEN_UNIX: not supported */
/* _XOPEN_UUCP: not supported */

#endif /* ZEPHYR_INCLUDE_POSIX_POSIX_FEATURES_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 BayLibre SAS。

版权（Copyright）：© 2024 Tenstorrent AI ULC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

配置符号模式（Configuration Symbol Pattern）：`CONFIG_*`。

### 注释 3：原第 12 行

条件展开宏 `COND_CODE_1()`。

### 注释 4：原第 14 行

POSIX 应用程序环境配置文件（Application Environment Profiles，AEP），依据 IEEE Std 1003.13-2003。

### 注释 5：原第 30 行

子配置文件设计考虑（Subprofiling Considerations）。

### 注释 6：原第 35 行

POSIX 系统接口（System Interfaces）。

### 注释 7：原第 45 行

不支持（Not Supported）`_POSIX_ADVISORY_INFO`。

### 注释 8：原第 63 行

不支持（Not Supported）`_POSIX_JOB_CONTROL`。

### 注释 9：原第 85 行

不支持（Not Supported）`_POSIX_PRIORITIZED_IO`。

### 注释 10：原第 99 行

不支持（Not Supported）`_POSIX_REGEXP`。

### 注释 11：原第 100 行

不支持（Not Supported）`_POSIX_SAVED_IDS`。

### 注释 12：原第 110 行

不支持（Not Supported）`_POSIX_SHELL`。

### 注释 13：原第 111 行

不支持（Not Supported）`_POSIX_SPAWN`。

### 注释 14：原第 117 行

不支持（Not Supported）`_POSIX_SPORADIC_SERVER`。

### 注释 15：原第 147 行

不支持（Not Supported）`_POSIX_THREAD_PROCESS_SHARED`。

### 注释 16：原第 148 行

不支持（Not Supported）`_POSIX_THREAD_ROBUST_PRIO_INHERIT`。

### 注释 17：原第 149 行

不支持（Not Supported）`_POSIX_THREAD_ROBUST_PRIO_PROTECT`。

### 注释 18：原第 151 行

不支持（Not Supported）`_POSIX_THREAD_SPORADIC_SERVER`。

### 注释 19：原第 163 行

不支持（Not Supported）`_POSIX_TRACE`。

### 注释 20：原第 164 行

不支持（Not Supported）`_POSIX_TRACE_EVENT_FILTER`。

### 注释 21：原第 165 行

不支持（Not Supported）`_POSIX_TRACE_INHERIT`。

### 注释 22：原第 166 行

不支持（Not Supported）`_POSIX_TRACE_LOG`。

### 注释 23：原第 167 行

不支持（Not Supported）`_POSIX_TYPED_MEMORY_OBJECTS`。

### 注释 24：原第 169 行

POSIX v6 选项（Options）。

### 注释 25：原第 172 行

不支持（Not Supported）`_POSIX_V6_ILP32_OFF32`。

### 注释 26：原第 173 行

不支持（Not Supported）`_POSIX_V6_ILP32_OFFBIG`。

### 注释 27：原第 174 行

不支持（Not Supported）`_POSIX_V6_LP64_OFF64`。

### 注释 28：原第 175 行

不支持（Not Supported）`_POSIX_V6_LPBIG_OFFBIG`。

### 注释 29：原第 177 行

POSIX v7 选项（Options）。

### 注释 30：原第 180 行

不支持（Not Supported）`_POSIX_V7_ILP32_OFF32`。

### 注释 31：原第 181 行

不支持（Not Supported）`_POSIX_V7_ILP32_OFFBIG`。

### 注释 32：原第 182 行

不支持（Not Supported）`_POSIX_V7_LP64_OFF64`。

### 注释 33：原第 183 行

不支持（Not Supported）`_POSIX_V7_LPBIG_OFFBIG`。

### 注释 34：原第 185 行

POSIX2 选项（Options）。

### 注释 35：原第 188 行

不支持（Not Supported）`_POSIX2_VERSION`。

### 注释 36：原第 190 行

不支持（Not Supported）`_POSIX2_C_DEV`。

### 注释 37：原第 191 行

不支持（Not Supported）`_POSIX2_CHAR_TERM`。

### 注释 38：原第 192 行

不支持（Not Supported）`_POSIX2_FORT_DEV`。

### 注释 39：原第 193 行

不支持（Not Supported）`_POSIX2_FORT_RUN`。

### 注释 40：原第 194 行

不支持（Not Supported）`_POSIX2_LOCALEDEF`。

### 注释 41：原第 195 行

不支持（Not Supported）`_POSIX2_PBS`。

### 注释 42：原第 196 行

不支持（Not Supported）`_POSIX2_PBS_ACCOUNTING`。

### 注释 43：原第 197 行

不支持（Not Supported）`_POSIX2_PBS_CHECKPOINT`。

### 注释 44：原第 198 行

不支持（Not Supported）`_POSIX2_PBS_LOCATE`。

### 注释 45：原第 199 行

不支持（Not Supported）`_POSIX2_PBS_MESSAGE`。

### 注释 46：原第 200 行

不支持（Not Supported）`_POSIX2_PBS_TRACK`。

### 注释 47：原第 201 行

不支持（Not Supported）`_POSIX2_SW_DEV`。

### 注释 48：原第 202 行

不支持（Not Supported）`_POSIX2_UPE`。

### 注释 49：原第 204 行

X/Open 系统接口（System Interfaces）。

### 注释 50：原第 208 行

不支持（Not Supported）`_XOPEN_CRYPT`。

### 注释 51：原第 209 行

不支持（Not Supported）`_XOPEN_ENH_I18N`。

### 注释 52：原第 217 行

不支持（Not Supported）`_XOPEN_REALTIME_THREADS`。

### 注释 53：原第 218 行

不支持（Not Supported）`_XOPEN_SHM`。

### 注释 54：原第 224 行

不支持（Not Supported）`_XOPEN_UNIX`。

### 注释 55：原第 225 行

不支持（Not Supported）`_XOPEN_UUCP`。

### 注释 56：原第 227 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_POSIX_FEATURES_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P309_zephyr__posix__posix_features.h_文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P006_net_pkt.h_源码浏览.md) · [返回大纲](大纲.md)
