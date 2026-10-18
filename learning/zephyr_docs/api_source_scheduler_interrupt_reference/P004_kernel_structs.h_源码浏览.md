---
id: learning.zephyr-docs.api-source-scheduler-interrupt-reference.page-4
title: kernel_structs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kernel__structs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_kernel\_structs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/kernel__structs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P180_zephyr__kernel_structs.h_文件参考.md)。

## 4.1\_原始可见代码（Source Code）

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
<a id="l00242"></a>
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
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
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
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
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
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="aatomic_8h_html"></a>
<a id="adlist_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__doubly-linked-list__apis_html_ga57fdb936802a617d16c00ab08cd2ad98"></a>
<a id="agroup__doubly-linked-list__apis_html_gaa03f9557215b486fee1039dd4c07e683"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_2stats_8h_html"></a>
<a id="akernel__structs_8h_html_a3fcfea2426c3da024f627c8ab9e754ad"></a>
<a id="akernel__structs_8h_html_a44c6f88a879877ad8da28706e274064f"></a>
<a id="akernel__structs_8h_html_ae861b4805a52e8bd99d5481d3943dc5c"></a>
<a id="amin__heap__ref_8h_html"></a>
<a id="aobj__core_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="arb_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructk__cycle__stats_html"></a>
<a id="astructk__obj__core_html"></a>
<a id="astructk__thread_html"></a>
<a id="astructrbnode_html"></a>
<a id="astructrbtree_html"></a>
<a id="astructs_8h_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="asys__heap_8h_html"></a>

```c
/*
 * Copyright (c) 2016 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/*
 * The purpose of this file is to provide essential/minimal kernel structure
 * definitions, so that they can be used without including kernel.h.
 *
 * The following rules must be observed:
 *  1. kernel_structs.h shall not depend on kernel.h both directly and
 *    indirectly (i.e. it shall not include any header files that include
 *    kernel.h in their dependency chain).
 *  2. kernel.h shall imply kernel_structs.h, such that it shall not be
 *    necessary to include kernel_structs.h explicitly when kernel.h is
 *    included.
 */

#ifndef ZEPHYR_INCLUDE_KERNEL_STRUCTS_H_
#define ZEPHYR_INCLUDE_KERNEL_STRUCTS_H_

#if !defined(_ASMLANGUAGE)
#include <zephyr/sys/atomic.h>
#include <zephyr/types.h>
#include <zephyr/sys/dlist.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/sys_heap.h>
#include <zephyr/arch/structs.h>
#include <zephyr/kernel/stats.h>
#include <zephyr/kernel/obj_core.h>
#include <zephyr/sys/rb.h>
#if defined(CONFIG_TIMEOUT_BACKEND_MINHEAP)
#include <zephyr/sys/min_heap_ref.h>
#endif
#endif

#define K_NUM_THREAD_PRIO (CONFIG_NUM_PREEMPT_PRIORITIES + CONFIG_NUM_COOP_PRIORITIES + 1)
#define PRIQ_BITMAP_SIZE  (DIV_ROUND_UP(K_NUM_THREAD_PRIO, BITS_PER_LONG))

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Bitmask definitions for the struct k_thread.thread_state field.
 *
 * Must be before kernel_arch_data.h because it might need them to be already
 * defined.
 */

/* states: common uses low bits, arch-specific use high bits */

/* Not a real thread */
#define _THREAD_DUMMY (BIT(0))

/* Thread is waiting on an object */
#define _THREAD_PENDING (BIT(1))

/* Thread is sleeping */
#define _THREAD_SLEEPING (BIT(2))

/* Thread has terminated */
#define _THREAD_DEAD (BIT(3))

/* Thread is suspended */
#define _THREAD_SUSPENDED (BIT(4))

/* Thread is in the process of aborting */
#define _THREAD_ABORTING (BIT(5))

/* Thread is in the process of suspending */
#define _THREAD_SUSPENDING (BIT(6))

/* Thread is present in the ready queue */
#define _THREAD_QUEUED (BIT(7))

/* end - states */

#ifdef CONFIG_STACK_SENTINEL
/* Magic value in lowest bytes of the stack */
#define STACK_SENTINEL 0xF0F0F0F0
#endif

/* lowest value of _thread_base.preempt at which a thread is non-preemptible */
#define _NON_PREEMPT_THRESHOLD 0x0080U

/* highest value of _thread_base.preempt at which a thread is preemptible */
#define _PREEMPT_THRESHOLD (_NON_PREEMPT_THRESHOLD - 1U)

#if !defined(_ASMLANGUAGE)

/* There are three abstractions defined for "thread priority queues".
 *
 * The first is a simple doubly linked list (sys_dlist_t) appropriate for
 * systems with small numbers of threads and sensitive to code size. It is
 * stored in sorted order, taking an O(N) cost every time a thread is added
 * to the list. This corresponds to the way the original _wait_q_t abstraction
 * worked and is very fast as long as the number of threads is small.
 *
 * The second is a scalable balanced tree. It has a rather larger code size
 * (due to the data structure itself, the code here is just stubs) and higher
 * constant-factor performance overhead, with O(logN) scaling in the presence
 * of large number of threads.
 *
 * The third is a traditional/textbook "multi-queue". It has separate lists
 * for each priority. This corresponds to the original Zephyr scheduler. RAM
 * requirements are comparatively high, but performance is very fast. It won't
 * work with features like deadline scheduling which need large priority spaces
 * to represent their requirements.
 *
 * Either the simple or balanced tree abstractions may be used for the wait_q.
 * Any of the three may be used for the system ready queue. The choices are
 * configurable at build time.
 */

struct _priq_rb {
        struct rbtree tree;
        int next_order_key;
};

struct _priq_mq {
        sys_dlist_t queues[K_NUM_THREAD_PRIO];
        unsigned long bitmask[PRIQ_BITMAP_SIZE];
#ifndef CONFIG_SMP
        unsigned int cached_queue_index;
#endif
};

struct _ready_q {
#ifndef CONFIG_SMP
        /* always contains next thread to run: cannot be NULL */
        struct k_thread *cache;
#endif

#if defined(CONFIG_SCHED_SIMPLE)
        sys_dlist_t runq;
#elif defined(CONFIG_SCHED_SCALABLE)
        struct _priq_rb runq;
#elif defined(CONFIG_SCHED_MULTIQ)
        struct _priq_mq runq;
#endif
};

typedef struct _ready_q _ready_q_t;

/* CPU records in coherent memory do not need padding to avoid false sharing. */
#ifndef CONFIG_KERNEL_COHERENCE
#define Z_DCACHE_ALIGN_SMP_CPU Z_DCACHE_ALIGN_SMP
#else
#define Z_DCACHE_ALIGN_SMP_CPU
#endif

struct _cpu {
        /* nested interrupt count */
        uint32_t nested;

        /* interrupt stack pointer base */
        char *irq_stack;

        /* currently scheduled thread */
        struct k_thread *current;

        /* one assigned idle thread per CPU */
        struct k_thread *idle_thread;

#ifdef CONFIG_SCHED_CPU_MASK_PIN_ONLY
        struct _ready_q ready_q;
#endif

#if (CONFIG_NUM_METAIRQ_PRIORITIES > 0)
        /* Coop thread preempted by current metairq, or NULL */
        struct k_thread *metairq_preempted;
#endif

        uint8_t id;

#if defined(CONFIG_FPU_SHARING)
        void *fp_ctx;
#endif

#ifdef CONFIG_SMP
        /* True when _current is allowed to context switch */
        uint8_t swap_ok;
#endif

#ifdef CONFIG_SCHED_THREAD_USAGE
        /*
         * [usage0] is used as a timestamp to mark the beginning of an
         * execution window. [0] is a special value indicating that it
         * has been stopped (but not disabled).
         */

        uint32_t usage0;

#ifdef CONFIG_SCHED_THREAD_USAGE_ALL
        struct k_cycle_stats *usage;
#endif
#endif

#ifdef CONFIG_OBJ_CORE_SYSTEM
        struct k_obj_core  obj_core;
#endif

#ifdef CONFIG_SCHED_IPI_SUPPORTED
        sys_dlist_t ipi_workq;
#endif

        /* Per CPU architecture specifics */
        struct _cpu_arch arch;
} Z_DCACHE_ALIGN_SMP_CPU;

typedef struct _cpu _cpu_t;

struct z_kernel {
        struct _cpu cpus[CONFIG_MP_MAX_NUM_CPUS];

#ifdef CONFIG_PM
        int32_t idle; /* Number of ticks for kernel idling */
#endif

        /*
         * ready queue: can be big, keep after small fields, since some
         * assembly (e.g. ARC) are limited in the encoding of the offset
         */
#ifndef CONFIG_SCHED_CPU_MASK_PIN_ONLY
        struct _ready_q ready_q;
#endif

#if defined(CONFIG_THREAD_MONITOR)
        struct k_thread *threads; /* singly linked list of ALL threads */
#endif
#ifdef CONFIG_SCHED_THREAD_USAGE_ALL
        struct k_cycle_stats usage[CONFIG_MP_MAX_NUM_CPUS];
#endif

#ifdef CONFIG_OBJ_CORE_SYSTEM
        struct k_obj_core  obj_core;
#endif

#if defined(CONFIG_SMP) && defined(CONFIG_SCHED_IPI_SUPPORTED)
        /* Identify CPUs to send IPIs to at the next scheduling point */
        atomic_t pending_ipi;
#endif

#if defined(CONFIG_IPI_OPTIMIZE_IDLE)
        /* Idle CPU reservations. sched_ipi_reserved marks valid entries in
         * sched_ipi_target. Each entry represents logical coverage by an
         * outstanding IPI, not a binding between that CPU and thread.
         * Protected by _sched_spinlock.
         */
        uint32_t sched_ipi_reserved;
        struct k_thread *sched_ipi_target[CONFIG_MP_MAX_NUM_CPUS];
#endif
};

typedef struct z_kernel _kernel_t;

extern struct z_kernel _kernel;

extern atomic_t _cpus_active;

#ifdef CONFIG_SMP

/* True if the current context can be preempted and migrated to
 * another SMP CPU.
 */
bool z_smp_cpu_mobile(void);
#define _current_cpu ({ __ASSERT_NO_MSG(!z_smp_cpu_mobile()); \
                        arch_curr_cpu(); })
#else
#define _current_cpu (&_kernel.cpus[0])
#endif

/* The current thread, in the per-CPU structure where the kernel records it.
 *
 * This is the definitive location: z_current_thread_set() always writes here
 * and nothing caches it, so it reports the incoming thread as soon as that
 * call has been made.  Reading it requires a context that cannot migrate,
 * which is what _current_cpu asserts: an ISR, or interrupts locked.
 *
 * Use _current instead unless the value must be up to date and the caller
 * already meets that requirement.
 */
#define _raw_current (_current_cpu->current)

#ifdef CONFIG_SMP
__attribute_const__ struct k_thread *z_smp_current_get(void);
#define _current z_smp_current_get()
#else
#define _current _raw_current
#endif

#define CPU_ID ((CONFIG_MP_MAX_NUM_CPUS == 1) ? 0 : _current_cpu->id)

/* This is always invoked from a context where preemption is disabled.
 *
 * Callers must not assume that _current reflects the new thread before the
 * switch actually happens.  An architecture may cache the current thread in
 * a register (CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL), and the compiler is then
 * free to reuse a value it read earlier in the same function.  Code running
 * between this call and the switch must therefore use the new thread pointer
 * it already has, or _raw_current where it has none.
 */
#define z_current_thread_set(thread) ({ _raw_current = (thread); })

#ifdef CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL
#undef _current
#define _current arch_current_thread()
#undef z_current_thread_set
#define z_current_thread_set(thread) \
        arch_current_thread_set(({ _raw_current = (thread); }))
#endif

/* kernel wait queue record */
#ifdef CONFIG_WAITQ_SCALABLE

typedef struct {
        struct _priq_rb waitq;
} _wait_q_t;

/* defined in kernel/priority_queues.c */
bool z_priq_rb_lessthan(struct rbnode *a, struct rbnode *b);

#define Z_WAIT_Q_INIT(wait_q) { { { .lessthan_fn = z_priq_rb_lessthan } } }

#else

typedef struct {
        sys_dlist_t waitq;
} _wait_q_t;

#define Z_WAIT_Q_INIT(wait_q) { SYS_DLIST_STATIC_INIT(&(wait_q)->waitq) }

#endif /* CONFIG_WAITQ_SCALABLE */

/* kernel timeout record */
struct _timeout;
typedef void (*_timeout_func_t)(struct _timeout *t);

struct _timeout {
        /*
         * Backend-specific queue representation. The handler pointer (fn) is
         * common to all backends and kept as the trailing member; everything
         * above it is owned by the selected timeout backend (see
         * kernel/include/timeout_q.h).
         */
#if defined(CONFIG_TIMEOUT_BACKEND_MINHEAP)
        /*
         * Min-heap backend: absolute expiry tick plus the heap position
         * handle. heap_handle.idx == 0 means the timeout is not queued
         * (idle, popped for announcing, or aborted).
         */
        int64_t abs_ticks;
        struct min_heap_handle heap_handle;
#elif defined(CONFIG_TIMEOUT_BACKEND_SKIPLIST)
        /*
         * Skip-list backend: absolute expiry tick plus a geometric-height
         * tower of forward pointers. height == 0 means the timeout is not
         * queued (idle, popped for announcing, or aborted).
         */
        int64_t abs_ticks;
        uint8_t height;
        struct _timeout *forward[CONFIG_TIMEOUT_SKIPLIST_MAX_LEVEL];
#else
        /*
         * Delta-list, bucket, and timer-wheel backends: a list node plus
         * dticks (a delta to the predecessor for the delta list; an encoded
         * slot position for the wheel or bucket). The wheel adds a flags
         * field recording which wheel tier the timeout currently occupies.
         */
        sys_dnode_t node;
#if defined(CONFIG_TIMEOUT_BACKEND_WHEEL)
        uint32_t flags;
#endif
#ifdef CONFIG_TIMEOUT_64BIT
        /* Can't use k_ticks_t for header dependency reasons */
        int64_t dticks;
#else
        int32_t dticks;
#endif
#endif /* CONFIG_TIMEOUT_BACKEND_MINHEAP */
        _timeout_func_t fn;
};

typedef void (*k_thread_timeslice_fn_t)(struct k_thread *thread, void *data);

#ifdef __cplusplus
}
#endif

#endif /* _ASMLANGUAGE */

#endif /* ZEPHYR_INCLUDE_KERNEL_STRUCTS_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 7 行

本文件提供必要且最小化的内核结构体定义（Kernel Structure Definitions），以便在不包含 `kernel.h` 的情况下使用。必须遵守以下规则：

1. `kernel_structs.h` 不得直接或间接依赖 `kernel.h`，即不得包含依赖链中含有 `kernel.h` 的任何头文件。
2. `kernel.h` 必须隐含包含 `kernel_structs.h`，因此已包含 `kernel.h` 时不必再显式包含 `kernel_structs.h`。

### 注释 3：原第 45 行

`struct k_thread.thread_state` 字段的位掩码定义（Bitmask Definitions）。必须放在 `kernel_arch_data.h` 之前，因为后者可能要求这些内容已定义。

### 注释 4：原第 52 行

状态（States）：通用状态使用低位，体系结构专用状态使用高位。

### 注释 5：原第 54 行

不是真正的线程（Not a Real Thread）。

### 注释 6：原第 57 行

线程正在等待对象（Waiting on an Object）。

### 注释 7：原第 60 行

线程处于睡眠状态（Sleeping）。

### 注释 8：原第 63 行

线程已终止（Terminated）。

### 注释 9：原第 66 行

线程已挂起（Suspended）。

### 注释 10：原第 69 行

线程正在中止（Aborting）。

### 注释 11：原第 72 行

线程正在挂起（Suspending）。

### 注释 12：原第 75 行

线程位于就绪队列（Ready Queue）中。

### 注释 13：原第 78 行

状态定义结束（End of States）。

### 注释 14：原第 81 行

栈最低字节中的魔数（Magic Value）。

### 注释 15：原第 85 行

使线程不可抢占（Non-preemptible）的 `_thread_base.preempt` 最小值。

### 注释 16：原第 88 行

使线程可抢占（Preemptible）的 `_thread_base.preempt` 最大值。

### 注释 17：原第 93 行

“线程优先级队列”（Thread Priority Queues）定义了三种抽象。

第一种是简单的双向链表（Doubly Linked List，`sys_dlist_t`），适用于线程较少、对代码大小敏感的系统。链表保持排序，每次加入线程的开销为 `O(N)`。这与最初 `_wait_q_t` 抽象的方式一致，只要线程数量较少，速度就很快。

第二种是可扩展的平衡树（Balanced Tree）。其代码大小明显更大，这是由数据结构本身造成的，此处代码只是桩函数；固定的性能开销也更高，但在线程数量较多时可按 `O(logN)` 扩展。

第三种是传统、教科书式的多队列（Multi-queue）：每个优先级都有单独的列表。这对应最初的 Zephyr 调度器，RAM 需求相对较高，但性能很快。它无法支持截止时间调度（Deadline Scheduling）这类需要很大优先级空间表达需求的功能。

等待队列（`wait_q`）可以使用简单链表或平衡树；系统就绪队列（Ready Queue）可以使用三者中的任意一种。具体选择在构建时配置。

### 注释 18：原第 132 行

始终包含下一个要运行的线程，不能为 `NULL`。

### 注释 19：原第 147 行

一致性内存（Coherent Memory）中的 CPU 记录不需要通过填充（Padding）来避免伪共享（False Sharing）。

### 注释 20：原第 155 行

嵌套中断计数（Nested Interrupt Count）。

### 注释 21：原第 158 行

中断栈指针基址（Interrupt Stack Pointer Base）。

### 注释 22：原第 161 行

当前被调度的线程（Currently Scheduled Thread）。

### 注释 23：原第 164 行

每个 CPU 分配一个空闲线程（Idle Thread）。

### 注释 24：原第 172 行

被当前元中断（Meta-IRQ）抢占的协作式线程（Cooperative Thread），或 `NULL`。

### 注释 25：原第 183 行

允许 `_current` 进行上下文切换（Context Switch）时为 `true`。

### 注释 26：原第 188 行

`[usage0]` 用作时间戳（Timestamp），标记执行窗口（Execution Window）的开始。`[0]` 是特殊值，表示已经停止，但未禁用。

### 注释 27：原第 209 行

各 CPU 架构专用内容（Per CPU architecture specifics）。

### 注释 28：原第 219 行

内核空闲（Kernel Idling）的节拍数（Ticks）。

### 注释 29：原第 222 行

就绪队列（Ready Queue）可能较大，因此放在较小字段之后；某些体系结构的汇编指令，例如 ARC，对偏移量编码有限制。

### 注释 30：原第 231 行

包含所有线程的单向链表（Singly Linked List）。

### 注释 31：原第 242 行

标识在下一个调度点（Scheduling Point）需要接收处理器间中断（IPI）的 CPU。

### 注释 32：原第 247 行

空闲 CPU 预留（Idle CPU Reservations）。`sched_ipi_reserved` 标记 `sched_ipi_target` 中的有效条目。每项表示一个尚未完成的处理器间中断（IPI）在逻辑上覆盖该 CPU，并不绑定该 CPU 与线程。由 `_sched_spinlock` 保护。

### 注释 33：原第 265 行

当前上下文可以被抢占并迁移到另一个对称多处理（SMP）CPU 时为 `true`。

### 注释 34：原第 275 行

当前线程，存放在内核用于记录它的每 CPU 结构体（Per-CPU Structure）中。

这是权威存储位置：`z_current_thread_set()` 总是写入这里，且没有缓存副本，因此该调用一执行完，这里就反映即将切入的线程。读取时要求当前上下文不能迁移，这正是 `_current_cpu` 断言的条件，即处于中断服务程序（ISR）中或已锁定中断。

除非必须获取最新值且调用者已满足上述要求，否则应使用 `_current`。

### 注释 35：原第 296 行

此调用始终发生在禁止抢占（Preemption Disabled）的上下文。

调用者不能假设实际切换之前，`_current` 已反映新线程。某些体系结构会将当前线程缓存在寄存器中（`CONFIG_ARCH_HAS_CUSTOM_CURRENT_IMPL`），编译器可能重用同一函数内之前读取的值。因此，在此调用与实际切换之间运行的代码，必须使用手中已有的新线程指针；若没有该指针，则使用 `_raw_current`。

### 注释 36：原第 315 行

内核等待队列记录（Kernel Wait Queue Record）。

### 注释 37：原第 322 行

定义在 `kernel/priority_queues.c` 中。

### 注释 38：原第 335 行

条件编译配置（Configuration）标记：`CONFIG_WAITQ_SCALABLE`。

### 注释 39：原第 337 行

内核超时记录（Kernel Timeout Record）。

### 注释 40：原第 342 行

后端专用的队列表示（Backend-specific Queue Representation）。处理函数指针 `fn` 由所有后端共用，并保持为末尾成员；之前的所有内容由所选超时后端拥有，参见 `kernel/include/timeout_q.h`。

### 注释 41：原第 349 行

最小堆后端（Min-heap Backend）：绝对到期节拍值和堆位置句柄（Heap Position Handle）。`heap_handle.idx == 0` 表示该超时项不在队列中，可能为空闲、已弹出以通知到期，或已中止。

### 注释 42：原第 357 行

跳表后端（Skip-list Backend）：绝对到期节拍值，以及高度服从几何分布的前向指针塔（Tower of Forward Pointers）。`height == 0` 表示该超时项不在队列中，可能为空闲、已弹出以通知到期，或已中止。

### 注释 43：原第 366 行

差值链表、桶和时间轮后端（Delta-list, Bucket, and Timer-wheel Backends）：列表节点加 `dticks`。对于差值链表，`dticks` 表示相对前驱的差值；对于时间轮或桶，则为编码后的槽位置。时间轮还增加一个标志字段，用于记录超时项当前所处的轮层级（Wheel Tier）。

### 注释 44：原第 377 行

因头文件依赖关系，不能使用 `k_ticks_t`。

### 注释 45：原第 382 行

条件编译配置（Configuration）标记：`CONFIG_TIMEOUT_BACKEND_MINHEAP`。

### 注释 46：原第 392 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 47：原第 394 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_KERNEL_STRUCTS_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P180_zephyr__kernel_structs.h_文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/sys/dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/sys_heap.h](../lowheap_reference/P011_底层堆头文件参考.md)
- [zephyr/arch/structs.h](../api_file_reference/P475_zephyr__arch__structs.h_文件参考.md)
- [zephyr/kernel/stats.h](../api_file_reference/P178_zephyr__kernel__stats.h_文件参考.md)
- [zephyr/kernel/obj_core.h](../object_core_reference/P003_对象核心头文件参考.md)
- [zephyr/sys/rb.h](../rbtree_reference/P004_红黑树头文件参考.md)
- [zephyr/sys/min_heap_ref.h](../minheap_reference/P008_引用最小堆头文件参考.md)
- [rbtree](../rbtree_reference/P003_红黑树结构.md)
- [sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)
- [K_NUM_THREAD_PRIO](../api_file_reference/P180_zephyr__kernel_structs.h_文件参考.md#ae861b4805a52e8bd99d5481d3943dc5c)
- [PRIQ_BITMAP_SIZE](../api_file_reference/P180_zephyr__kernel_structs.h_文件参考.md#a3fcfea2426c3da024f627c8ab9e754ad)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [k_cycle_stats](../kernel_runtime_model_reference/P001_k_cycle_stats_结构体.md)
- [k_obj_core](../object_core_reference/P005_对象核心结构.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [rbnode](../rbtree_reference/P002_红黑树节点.md)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [k_thread_timeslice_fn_t](../api_file_reference/P180_zephyr__kernel_structs.h_文件参考.md#a44c6f88a879877ad8da28706e274064f)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [stats.h](../api_file_reference/P178_zephyr__kernel__stats.h_文件参考.md)
- [min_heap_ref.h](../minheap_reference/P008_引用最小堆头文件参考.md)
- [obj_core.h](../object_core_reference/P003_对象核心头文件参考.md)
- [rb.h](../rbtree_reference/P004_红黑树头文件参考.md)
- [structs.h](../api_file_reference/P475_zephyr__arch__structs.h_文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [sys_heap.h](../lowheap_reference/P011_底层堆头文件参考.md)

---

[上一章](P003_gic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_loapic.h_源码浏览.md)
