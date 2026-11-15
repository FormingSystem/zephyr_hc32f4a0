---
id: learning.zephyr-docs.api-source-interrupt-modem-reference.page-11
title: sw_isr_table.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sw__isr__table_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_sw\_isr\_table.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sw__isr__table_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sw__isr__table_8h.html)。

## 11.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00084"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00129"></a>
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
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
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
<a id="l00169"></a>
<a id="l00171"></a>
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
<a id="adevice_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2014, Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SW_ISR_TABLE_H_
#define ZEPHYR_INCLUDE_SW_ISR_TABLE_H_

#if !defined(_ASMLANGUAGE)
#include <zephyr/device.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/types.h>
#include <zephyr/toolchain.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Default vector for the IRQ vector table */
void _isr_wrapper(void);

/* Spurious interrupt handler. Throws an error if called */
void z_irq_spurious(const void *unused);

/*
 * Note the order: arg first, then ISR. This allows a table entry to be
 * loaded arg -> r0, isr -> r3 in _isr_wrapper with one ldmia instruction,
 * on ARM Cortex-M (Thumb2).
 */
struct _isr_table_entry {
        const void *arg;
        void (*isr)(const void *);
};

#if defined(CONFIG_GEN_SW_ISR_TABLE_ARRAY)
/* The software ISR table itself, an array of these structures indexed by the
 * irq line
 */
extern
#ifndef CONFIG_DYNAMIC_INTERRUPTS
        const
#endif /* CONFIG_DYNAMIC_INTERRUPTS */
        struct _isr_table_entry _sw_isr_table[];
#elif defined(CONFIG_GEN_SW_ISR_TABLE_SWITCH)
extern void __sw_isr_table get_isr_entry(int irq_number, struct _isr_table_entry *entry);
#endif /* CONFIG_GEN_SW_ISR_TABLE_ARRAY */

struct _irq_parent_entry {
        const struct device *dev;
        unsigned int level;
        unsigned int irq;
        unsigned int offset;
};


/* Mapping between aggregator level to order */
#define Z_STR_L2 2ND
#define Z_STR_L3 3RD
#define Z_SW_ISR_TBL_KCONFIG_BY_ALVL(l) CONCAT(CONFIG_, CONCAT(Z_STR_L, l), _LVL_ISR_TBL_OFFSET)


#define INTC_BASE_ISR_TBL_OFFSET(node_id)                                                          \
        Z_SW_ISR_TBL_KCONFIG_BY_ALVL(DT_INTC_GET_AGGREGATOR_LEVEL(node_id))

#define INTC_INST_ISR_TBL_OFFSET(inst)                                                             \
        (INTC_BASE_ISR_TBL_OFFSET(DT_DRV_INST(inst)) + (inst * CONFIG_MAX_IRQ_PER_AGGREGATOR))

#define INTC_CHILD_ISR_TBL_OFFSET(node_id)                                                         \
        (INTC_BASE_ISR_TBL_OFFSET(node_id) +                                                       \
         (DT_NODE_CHILD_IDX(node_id) * CONFIG_MAX_IRQ_PER_AGGREGATOR))

#define IRQ_PARENT_ENTRY_DEFINE(_name, _dev, _irq, _offset, _level)                                \
        static const STRUCT_SECTION_ITERABLE_ALTERNATE(intc_table, _irq_parent_entry, _name) = {   \
                .dev = _dev,                                                                       \
                .level = _level,                                                                   \
                .irq = _irq,                                                                       \
                .offset = _offset,                                                                 \
        }

/*
 * Data structure created in a special binary .intlist section for each
 * configured interrupt. gen_irq_tables.py pulls this out of the binary and
 * uses it to create the IRQ vector table and the _sw_isr_table.
 *
 * More discussion in include/linker/intlist.ld
 *
 * This is a version used when CONFIG_ISR_TABLES_LOCAL_DECLARATION is disabled.
 * See _isr_list_sname used otherwise.
 */
struct _isr_list {
        int32_t irq;
        int32_t flags;
        void *func;
        const void *param;
};

/*
 * Data structure created in a special binary .intlist section for each
 * configured interrupt. gen_isr_tables.py pulls this out of the binary and
 * uses it to create linker script chunks that would place interrupt table entries
 * in the right place in the memory.
 *
 * This is a version used when CONFIG_ISR_TABLES_LOCAL_DECLARATION is enabled.
 * See _isr_list used otherwise.
 */
struct _isr_list_sname {
        int32_t irq;
        int32_t flags;
        const char sname[];
};

#ifdef CONFIG_SHARED_INTERRUPTS
struct z_shared_isr_table_entry {
        struct _isr_table_entry clients[CONFIG_SHARED_IRQ_MAX_NUM_CLIENTS];
        size_t client_num;
};

void z_shared_isr(const void *data);

extern
#ifndef CONFIG_DYNAMIC_INTERRUPTS
const
#endif
struct z_shared_isr_table_entry z_shared_sw_isr_table[];
#endif /* CONFIG_SHARED_INTERRUPTS */

#define ISR_FLAG_DIRECT BIT(0)

#define _MK_ISR_NAME(x, y) __MK_ISR_NAME(x, y)
#define __MK_ISR_NAME(x, y) __isr_ ## x ## _irq_ ## y


#if defined(CONFIG_ISR_TABLES_LOCAL_DECLARATION)

#define _MK_ISR_ELEMENT_NAME(func, id) __MK_ISR_ELEMENT_NAME(func, id)
#define __MK_ISR_ELEMENT_NAME(func, id) __isr_table_entry_ ## func ## _irq_ ## id

#define _MK_IRQ_ELEMENT_NAME(func, id) __MK_ISR_ELEMENT_NAME(func, id)
#define __MK_IRQ_ELEMENT_NAME(func, id) __irq_table_entry_ ## func ## _irq_ ## id

#define _MK_ISR_SECTION_NAME(prefix, file, counter)                                                \
        "." Z_STRINGIFY(prefix) "." file "." Z_STRINGIFY(counter)

#define _MK_ISR_ELEMENT_SECTION(counter) _MK_ISR_SECTION_NAME(irq, __FILE__, counter)
#define _MK_IRQ_ELEMENT_SECTION(counter) _MK_ISR_SECTION_NAME(isr, __FILE__, counter)

/* Separated macro to create ISR table entry only.
 * Used by Z_ISR_DECLARE and ISR tables generation script.
 */
#define _Z_ISR_TABLE_ENTRY(func, param, sect) \
        static Z_DECL_ALIGN(struct _isr_table_entry)                                      \
                __attribute__((section(sect)))                                            \
                __used _MK_ISR_ELEMENT_NAME(func, __COUNTER__) = {                        \
                        .arg = (const void *)(param),                                     \
                        .isr = (void (*)(const void *))(void *)(func)                     \
        }

#define Z_ISR_DECLARE_C(irq, flags, func, param, counter) \
        _Z_ISR_DECLARE_C(irq, flags, func, param, counter)

#define _Z_ISR_DECLARE_C(irq, flags, func, param, counter)                                         \
        _Z_ISR_TABLE_ENTRY(func, param, _MK_ISR_ELEMENT_SECTION(counter));                         \
        static Z_DECL_ALIGN(struct _isr_list_sname) Z_GENERIC_SECTION(.intList) __used             \
        _MK_ISR_NAME(func, counter) = {irq, flags, {_MK_ISR_ELEMENT_SECTION(counter)}}

/* Create an entry for _isr_table to be then placed by the linker.
 * An instance of struct _isr_list which gets put in the .intList
 * section is created with the name of the section where _isr_table entry is placed to be then
 * used by isr generation script to create linker script chunk.
 */
#define Z_ISR_DECLARE(irq, flags, func, param)                                            \
        BUILD_ASSERT(((flags) & ISR_FLAG_DIRECT) == 0, "Use Z_ISR_DECLARE_DIRECT macro"); \
        Z_ISR_DECLARE_C(irq, flags, func, param, __COUNTER__)


/* Separated macro to create ISR Direct table entry only.
 * Used by Z_ISR_DECLARE_DIRECT and ISR tables generation script.
 */
#define _Z_ISR_DIRECT_TABLE_ENTRY(func, sect)                                                      \
        COND_CODE_1(CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_ADDRESS, (                                     \
                        static Z_DECL_ALIGN(uintptr_t)                                             \
                        __attribute__((section(sect)))                                             \
                        __used _MK_IRQ_ELEMENT_NAME(func, __COUNTER__) = ((uintptr_t)(func));      \
                ), (                                                                               \
                        void __attribute__((section(sect))) __attribute__((naked))                 \
                        /* clang-format off */                                                     \
                        __used _MK_IRQ_ELEMENT_NAME(func, __COUNTER__) (void) {                    \
                                __asm(ARCH_IRQ_VECTOR_JUMP_CODE(func));                            \
                        }                                                                          \
                        /* clang-format on */                                                      \
                ))

#define Z_ISR_DECLARE_DIRECT_C(irq, flags, func, counter) \
        _Z_ISR_DECLARE_DIRECT_C(irq, flags, func, counter)

#define _Z_ISR_DECLARE_DIRECT_C(irq, flags, func, counter)                                         \
        _Z_ISR_DIRECT_TABLE_ENTRY(func, _MK_IRQ_ELEMENT_SECTION(counter));                         \
        static Z_DECL_ALIGN(struct _isr_list_sname) Z_GENERIC_SECTION(.intList)                    \
                __used _MK_ISR_NAME(func, counter) = {                                             \
                        irq,                                                                       \
                        ISR_FLAG_DIRECT | (flags),                                                 \
                        _MK_IRQ_ELEMENT_SECTION(counter)}

/* Create an entry to irq table and place it in specific section which name is then placed
 * in an instance of struct _isr_list to be then used by the isr generation script to create
 * the linker script chunks.
 */
#define Z_ISR_DECLARE_DIRECT(irq, flags, func)                                                     \
        BUILD_ASSERT(IS_ENABLED(CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_ADDRESS) ||                        \
                IS_ENABLED(CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_CODE),                                  \
                "CONFIG_IRQ_VECTOR_TABLE_JUMP_BY_{ADDRESS,CODE} not set");                         \
        Z_ISR_DECLARE_DIRECT_C(irq, flags, func, __COUNTER__)


#else /* defined(CONFIG_ISR_TABLES_LOCAL_DECLARATION) */

/* Create an instance of struct _isr_list which gets put in the .intList
 * section. This gets consumed by gen_isr_tables.py which creates the vector
 * and/or SW ISR tables.
 */
#define Z_ISR_DECLARE(irq, flags, func, param) \
        static Z_DECL_ALIGN(struct _isr_list) Z_GENERIC_SECTION(.intList) \
                __used _MK_ISR_NAME(func, __COUNTER__) = \
                        {irq, flags, (void *)&func, (const void *)param}

/* The version of the Z_ISR_DECLARE that should be used for direct ISR declaration.
 * It is here for the API match the version with CONFIG_ISR_TABLES_LOCAL_DECLARATION enabled.
 */
#define Z_ISR_DECLARE_DIRECT(irq, flags, func) \
        Z_ISR_DECLARE(irq, ISR_FLAG_DIRECT | (flags), func, NULL)

#endif

#define IRQ_TABLE_SIZE (CONFIG_NUM_IRQS - CONFIG_GEN_IRQ_START_VECTOR)

#ifdef CONFIG_DYNAMIC_INTERRUPTS
void z_isr_install(unsigned int irq, void (*routine)(const void *parameter),
                   const void *param);

#ifdef CONFIG_SHARED_INTERRUPTS
int z_isr_uninstall(unsigned int irq, void (*routine)(const void *parameter),
                    const void *param);
#endif /* CONFIG_SHARED_INTERRUPTS */
#endif

#ifdef __cplusplus
}
#endif

#endif /* _ASMLANGUAGE */

#endif /* ZEPHYR_INCLUDE_SW_ISR_TABLE_H_ */
```

## 11.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2014, Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 28 行

IRQ 向量表（IRQ vector table）的默认向量。

### 注释 3：原第 31 行

伪中断处理函数（spurious interrupt handler），被调用时抛出错误。

### 注释 4：原第 34 行

注意顺序：先 `arg`，后 `ISR`。这样，在 ARM Cortex-M（Thumb2）上，`_isr_wrapper` 可以通过一条 `ldmia` 指令加载一个表项，将 `arg` 载入 `r0`，将 `isr` 载入 `r3`。

### 注释 5：原第 45 行

软件中断服务程序表（software ISR table）本身，是按 IRQ 线索引的此类结构体数组。

### 注释 6：原第 51 行

条件编译配置（Configuration）标记：`CONFIG_DYNAMIC_INTERRUPTS`。

### 注释 7：原第 55 行

条件编译配置（Configuration）标记：`CONFIG_GEN_SW_ISR_TABLE_ARRAY`。

### 注释 8：原第 68 行

聚合器级别（aggregator level）到顺序（order）的映射。

### 注释 9：原第 137 行

为每个已配置中断在特殊二进制节（section）`.intlist` 中创建的数据结构。`gen_irq_tables.py` 从二进制文件中提取它，用于创建 IRQ 向量表和 `_sw_isr_table`。更多说明见 `include/linker/intlist.ld`。

此版本用于禁用 `CONFIG_ISR_TABLES_LOCAL_DECLARATION` 的情况；其他情况下使用 `_isr_list_sname`。

### 注释 10：原第 158 行

为每个已配置中断在特殊二进制节（section）`.intlist` 中创建的数据结构。`gen_isr_tables.py` 从二进制文件中提取它，用于创建链接器脚本片段（linker script chunks），将中断表条目放到正确的内存位置。

此版本用于启用 `CONFIG_ISR_TABLES_LOCAL_DECLARATION` 的情况；其他情况下使用 `_isr_list`。

### 注释 11：原第 189 行

条件编译配置（Configuration）标记：`CONFIG_SHARED_INTERRUPTS`。

### 注释 12：原第 212 行

独立的宏，仅创建 ISR 表条目（table entry）。由 `Z_ISR_DECLARE` 及 ISR 表生成脚本使用。

### 注释 13：原第 231 行

创建随后由链接器放置的 `_isr_table` 条目。创建一个放入 `.intList` 节的 `struct _isr_list` 实例，其中记录 `_isr_table` 条目所在节的名称；ISR 生成脚本随后使用它创建链接器脚本片段。

### 注释 14：原第 241 行

独立的宏，仅创建直接中断服务程序表（ISR Direct table）条目。由 `Z_ISR_DECLARE_DIRECT` 及 ISR 表生成脚本使用。

### 注释 15：原第 251 行

关闭 clang-format 自动排版（clang-format off）。

### 注释 16：原第 255 行

开启 clang-format 自动排版（clang-format on）。

### 注释 17：原第 269 行

创建 IRQ 表条目并将其放入指定节，再将该节名称记录在 `struct _isr_list` 实例中；ISR 生成脚本随后使用该实例创建链接器脚本片段。

### 注释 18：原第 280 行

条件表达式：`defined(CONFIG_ISR_TABLES_LOCAL_DECLARATION)`。

### 注释 19：原第 282 行

创建一个放入 `.intList` 节的 `struct _isr_list` 实例。`gen_isr_tables.py` 使用它创建向量表和／或软件 ISR 表。

### 注释 20：原第 291 行

用于声明直接 ISR（direct ISR）的 `Z_ISR_DECLARE` 版本。此处提供它，以便 API 与启用 `CONFIG_ISR_TABLES_LOCAL_DECLARATION` 时的版本一致。

### 注释 21：原第 308 行

条件编译配置（Configuration）标记：`CONFIG_SHARED_INTERRUPTS`。

### 注释 22：原第 315 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 23：原第 317 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SW_ISR_TABLE_H_`。

## 11.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sw__isr__table_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P010_renesas_rztn_clock.h_源码浏览.md) · [返回大纲](大纲.md)
