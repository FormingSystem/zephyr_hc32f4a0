---
id: learning.zephyr-docs.api-source-configuration-reference.page-106
title: stats.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第106章\_stats.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h.html)。

## 106.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00118"></a>
<a id="foldopen00125"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="foldopen00139"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00157"></a>
<a id="foldopen00163"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00216"></a>
<a id="l00220"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00227"></a>
<a id="l00232"></a>
<a id="foldopen00243"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="foldopen00255"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="foldopen00268"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="foldopen00280"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00284"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00295"></a>
<a id="foldopen00311"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00388"></a>
<a id="l00393"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00488"></a>
<a id="l00490"></a>
<a id="l00501"></a>
<a id="foldopen00510"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="foldopen00519"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="foldopen00538"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="agroup__stats__apis_html_ga0a26d63646d1157509afcc370738b9d8"></a>
<a id="agroup__stats__apis_html_ga11402b3eb75529d1ebf7b7b87c9e20f8"></a>
<a id="agroup__stats__apis_html_ga3b431d3e69b3978bfd81268b70eda6e0"></a>
<a id="agroup__stats__apis_html_ga454c4c833e25fcb8808c4b85db4f0291"></a>
<a id="agroup__stats__apis_html_ga5e2c74f2c77a8cf1d2a43eb7190a9b93"></a>
<a id="agroup__stats__apis_html_ga687b3da8d0e3e0f55e8ea8d5e47eaf2a"></a>
<a id="agroup__stats__apis_html_ga8cb611a313ede400835eb56a4d209c7a"></a>
<a id="agroup__stats__apis_html_gaa4f75157451e12d76e5cc0fbc65063da"></a>
<a id="agroup__stats__apis_html_gaca8e338b464a6c317232d7029c80f206"></a>
<a id="agroup__stats__apis_html_gae6aeebd4e8f57b0b82c6dcf69bddcc64"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructstats__hdr_html"></a>
<a id="astructstats__name__map_html"></a>

```c
/*
 * Copyright Runtime.io 2018. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_STATS_STATS_H_
#define ZEPHYR_INCLUDE_STATS_STATS_H_

#include <stddef.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif


struct stats_name_map {
        uint16_t snm_off;
        const char *snm_name;
} __attribute__((packed));

struct stats_hdr {
        const char *s_name;
        uint8_t s_size;
        uint16_t s_cnt;
        uint8_t s_pad1;
#ifdef CONFIG_STATS_NAMES
        const struct stats_name_map *s_map;
        int s_map_cnt;
#endif
        struct stats_hdr *s_next;
};


#define STATS_SECT_DECL(group__) \
        struct stats_ ## group__

#define STATS_SECT_END }

/* The following macros depend on whether CONFIG_STATS is defined.  If it is
 * not defined, then invocations of these macros get compiled out.
 */
#if defined(CONFIG_STATS) || defined(__DOXYGEN__)

#define STATS_SECT_START(group__)  \
        STATS_SECT_DECL(group__) { \
                struct stats_hdr s_hdr;

#define STATS_SECT_ENTRY(var__) uint32_t var__;

#define STATS_SECT_ENTRY16(var__) uint16_t var__;

#define STATS_SECT_ENTRY32(var__) uint32_t var__;

#define STATS_SECT_ENTRY64(var__) uint64_t var__;

#define STATS_SIZE_16 (sizeof(uint16_t))
#define STATS_SIZE_32 (sizeof(uint32_t))
#define STATS_SIZE_64 (sizeof(uint64_t))



#define STATS_INCN(group__, var__, n__) \
        ((group__).var__ += (n__))

#define STATS_INC(group__, var__) \
        STATS_INCN(group__, var__, 1)

#define STATS_SET(group__, var__, n__)  \
        ((group__).var__ = (n__))

#define STATS_CLEAR(group__, var__) \
        ((group__).var__ = 0)


#define STATS_SIZE_INIT_PARMS(group__, size__) \
        (size__),                              \
        ((sizeof(group__)) - sizeof(struct stats_hdr)) / (size__)


#define STATS_INIT_AND_REG(group__, size__, name__)                      \
        stats_init_and_reg(                                              \
                &(group__).s_hdr,                                        \
                (size__),                                                \
                (sizeof(group__) - sizeof(struct stats_hdr)) / (size__), \
                STATS_NAME_INIT_PARMS(group__),                          \
                (name__))

void stats_init(struct stats_hdr *shdr, uint8_t size, uint16_t cnt,
                const struct stats_name_map *map, uint16_t map_cnt);

int stats_register(const char *name, struct stats_hdr *shdr);

int stats_init_and_reg(struct stats_hdr *hdr, uint8_t size, uint16_t cnt,
                       const struct stats_name_map *map, uint16_t map_cnt,
                       const char *name);

void stats_reset(struct stats_hdr *shdr);



typedef int stats_walk_fn(struct stats_hdr *hdr, void *arg,
                          const char *name, uint16_t off);

int stats_walk(struct stats_hdr *hdr, stats_walk_fn *walk_cb, void *arg);

typedef int stats_group_walk_fn(struct stats_hdr *hdr, void *arg);

int stats_group_walk(stats_group_walk_fn *walk_cb, void *arg);

struct stats_hdr *stats_group_get_next(const struct stats_hdr *cur);

struct stats_hdr *stats_group_find(const char *name);


#else /* CONFIG_STATS */

#define STATS_SECT_START(group__) \
        STATS_SECT_DECL(group__) {

#define STATS_SECT_ENTRY(var__)
#define STATS_SECT_ENTRY16(var__)
#define STATS_SECT_ENTRY32(var__)
#define STATS_SECT_ENTRY64(var__)
#define STATS_RESET(var__)
#define STATS_SIZE_INIT_PARMS(group__, size__)
#define STATS_INCN(group__, var__, n__)
#define STATS_INC(group__, var__)
#define STATS_SET(group__, var__, n__)
#define STATS_CLEAR(group__, var__)
#define STATS_INIT_AND_REG(group__, size__, name__) (0)

#endif /* CONFIG_STATS || __DOXYGEN__ */

#if defined(CONFIG_STATS_NAMES) || defined(__DOXYGEN__)

#define STATS_NAME_MAP_NAME(sectname__) stats_map_ ## sectname__


#define STATS_NAME_START(sectname__) \
        static const struct stats_name_map STATS_NAME_MAP_NAME(sectname__)[] = {

#define STATS_NAME(sectname__, entry__) \
        { offsetof(STATS_SECT_DECL(sectname__), entry__), #entry__ },

#define STATS_NAME_END(sectname__) }

#define STATS_NAME_INIT_PARMS(name__)       \
        &(STATS_NAME_MAP_NAME(name__)[0]), \
        (sizeof(STATS_NAME_MAP_NAME(name__)) / sizeof(struct stats_name_map))


#else /* CONFIG_STATS_NAMES */

#define STATS_NAME_START(name__)
#define STATS_NAME(name__, entry__)
#define STATS_NAME_END(name__)
#define STATS_NAME_INIT_PARMS(name__) NULL, 0

#endif /* CONFIG_STATS_NAMES */


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_STATS_STATS_H_ */
```

## 106.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：Runtime.io 2018. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 171 行

以下宏依赖是否定义了 `CONFIG_STATS`。如果没有定义，对这些宏的调用会在编译时被移除。

### 注释 3：原第 466 行

条件编译配置（Configuration）标记：`CONFIG_STATS`。

### 注释 4：原第 483 行

条件编译表达式：`CONFIG_STATS || __DOXYGEN__`。

### 注释 5：原第 544 行

条件编译配置（Configuration）标记：`CONFIG_STATS_NAMES`。

### 注释 6：原第 551 行

条件编译配置（Configuration）标记：`CONFIG_STATS_NAMES`。

### 注释 7：原第 561 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_STATS_STATS_H_`。

## 106.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [stats_name_map](../system_service_model_reference/P086_stats_name_map_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [stats_hdr](../system_service_model_reference/P085_stats_hdr_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [stats_init](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga5e2c74f2c77a8cf1d2a43eb7190a9b93)
- [stats_register](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga0a26d63646d1157509afcc370738b9d8)
- [stats_init_and_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga687b3da8d0e3e0f55e8ea8d5e47eaf2a)
- [stats_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gaca8e338b464a6c317232d7029c80f206)
- [stats_walk_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gaa4f75157451e12d76e5cc0fbc65063da)
- [stats_walk](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gae6aeebd4e8f57b0b82c6dcf69bddcc64)
- [stats_group_walk_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga454c4c833e25fcb8808c4b85db4f0291)
- [stats_group_walk](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga3b431d3e69b3978bfd81268b70eda6e0)
- [stats_group_get_next](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga11402b3eb75529d1ebf7b7b87c9e20f8)
- [stats_group_find](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga8cb611a313ede400835eb56a4d209c7a)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P105_socket_types.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P107_stdlib.h_源码浏览.md)
