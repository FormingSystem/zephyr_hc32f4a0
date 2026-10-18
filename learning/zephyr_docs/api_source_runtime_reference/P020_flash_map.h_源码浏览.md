---
id: learning.zephyr-docs.api-source-runtime-reference.page-20
title: flash_map.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/flash__map_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_flash\_map.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/flash__map_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/flash__map_8h.html)。

## 20.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
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
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="foldopen00141"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="foldopen00162"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="foldopen00337"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="foldopen00349"></a>
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
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="foldopen00393"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="foldopen00437"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="foldopen00459"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="foldopen00500"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="foldopen00526"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="foldopen00555"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00563"></a>
<a id="l00564"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="foldopen00584"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00590"></a>
<a id="l00591"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00604"></a>
<a id="l00605"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="l00614"></a>
<a id="l00615"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00619"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00634"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="l00638"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00646"></a>
<a id="l00647"></a>
<a id="adevice_8h_html"></a>
<a id="adevicetree_2partitions_8h_html"></a>
<a id="adevicetree_8h_html"></a>
<a id="afixed-partitions_8h_html"></a>
<a id="agroup__device__model_html_gaa4944bd850e90cbd52b0489f9b12edfb"></a>
<a id="agroup__devicetree-generic-foreach_html_ga52b34316d269cc8d8ef2244d3ca460b8"></a>
<a id="agroup__flash__area__api_html_ga12064d388369a504b571e9776201f688"></a>
<a id="agroup__flash__area__api_html_ga13b7294e84544373e97b8c0274859f6e"></a>
<a id="agroup__flash__area__api_html_ga1f16d59cecb25c5143c6a923b3b2f466"></a>
<a id="agroup__flash__area__api_html_ga34e74955153f8576acdbff1a524f2d37"></a>
<a id="agroup__flash__area__api_html_ga557d5fd981b0d52d0eb483ab218c497c"></a>
<a id="agroup__flash__area__api_html_ga5c89e0be6c41058beb1c3f87a0c9c94f"></a>
<a id="agroup__flash__area__api_html_ga6fe2593210688eb85e03bea5f96ea2f7"></a>
<a id="agroup__flash__area__api_html_ga7adf79769378ed468df6d3ffef5e02a9"></a>
<a id="agroup__flash__area__api_html_ga7c55704b0c0061a4715470676114b127"></a>
<a id="agroup__flash__area__api_html_ga826350cb9176f58fecead9998b79756f"></a>
<a id="agroup__flash__area__api_html_ga868a47161b33c99629df600c1d7d9d43"></a>
<a id="agroup__flash__area__api_html_ga91e8c75b636b6f300207128df8b0ca9a"></a>
<a id="agroup__flash__area__api_html_gaa50bb1b455a9004f9c24e4af9fd74cd7"></a>
<a id="agroup__flash__area__api_html_gaa56052f8d6bf4f6966752bc21f5cceb8"></a>
<a id="agroup__flash__area__api_html_gab9d0b43faefa1f25805e7def82819f2c"></a>
<a id="agroup__flash__area__api_html_gacc5cbff19d23773115f3334f862814d2"></a>
<a id="agroup__flash__area__api_html_gafd097d05f5bfe91695bc7793e82cabcd"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="amapped-partition_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructflash__area_html"></a>
<a id="astructflash__area_html_a3a362ad9aa44725a0b0188042a2ee257"></a>
<a id="astructflash__area_html_a6c3c23c4c628f48c92505dddf4b24edf"></a>
<a id="astructflash__area_html_a941637492ab4e321e3b08de19cd769d2"></a>
<a id="astructflash__area_html_acfe73a1f4f00fdf58129b21e5b71f5d4"></a>
<a id="astructflash__area_html_af98b8f20c0219bfcdd2fc20037845a99"></a>
<a id="astructflash__sector_html"></a>
<a id="astructflash__sector_html_a7d3d01c03efcddd6deb757e64e3db865"></a>
<a id="astructflash__sector_html_ab1fef4b1b6978d25b5f809d778888f75"></a>

```c
/*
 * Copyright (c) 2017-2024 Nordic Semiconductor ASA
 * Copyright (c) 2015 Runtime Inc
 * Copyright (c) 2023 Sensorfy B.V.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_STORAGE_FLASH_MAP_H_
#define ZEPHYR_INCLUDE_STORAGE_FLASH_MAP_H_


/*
 * This API makes it possible to operate on flash areas easily and
 * effectively.
 *
 * The system contains global data about flash areas. Every area
 * contains an ID number, offset, and length.
 */

#include <zephyr/types.h>
#include <stddef.h>
#include <sys/types.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/devicetree/fixed-partitions.h>
#include <zephyr/devicetree/mapped-partition.h>
#include <zephyr/devicetree/partitions.h>

#ifdef __cplusplus
extern "C" {
#endif

struct flash_area {
        uint8_t fa_id;
        uint16_t pad16;
        off_t fa_off;
        size_t fa_size;
        const struct device *fa_dev;
#if defined(CONFIG_FLASH_MAP_LABELS)
        const char *fa_label;
#endif
};

struct flash_sector {
        ptrdiff_t fs_off;
        size_t fs_size;
};

#if defined(CONFIG_FLASH_AREA_CHECK_INTEGRITY)
struct flash_area_check {
        const uint8_t *match;
        size_t clen;
        size_t off;
        uint8_t *rbuf;
        size_t rblen;
};

int flash_area_check_int_sha256(const struct flash_area *fa,
                                const struct flash_area_check *fac);
#endif

int flash_area_open(uint8_t id, const struct flash_area **fa);

static inline void flash_area_close(__unused const struct flash_area *fa)
{
        /* nothing to do for now */
}

static ALWAYS_INLINE bool flash_area_device_is_ready(const struct flash_area *fa)
{
        return (fa != NULL && device_is_ready(fa->fa_dev));
}

int flash_area_read(const struct flash_area *fa, off_t off, void *dst,
                    size_t len);

int flash_area_write(const struct flash_area *fa, off_t off, const void *src,
                     size_t len);

int flash_area_copy(const struct flash_area *src_fa, off_t src_off,
                    const struct flash_area *dst_fa, off_t dst_off,
                    off_t len, uint8_t *buf, size_t buf_size);

int flash_area_erase(const struct flash_area *fa, off_t off, size_t len);

int flash_area_flatten(const struct flash_area *fa, off_t off, size_t len);

uint32_t flash_area_align(const struct flash_area *fa);

int flash_area_get_sectors(int fa_id, uint32_t *count,
                           struct flash_sector *sectors);

int flash_area_sectors(const struct flash_area *fa, uint32_t *count, struct flash_sector *sectors);

typedef void (*flash_area_cb_t)(const struct flash_area *fa,
                                void *user_data);

void flash_area_foreach(flash_area_cb_t user_cb, void *user_data);

int flash_area_has_driver(const struct flash_area *fa);

static inline const struct device *flash_area_get_device(const struct flash_area *fa)
{
        return fa->fa_dev;
}

static inline const char *flash_area_label(const struct flash_area *fa)
{
#if defined(CONFIG_FLASH_MAP_LABELS)
        return fa->fa_label;
#else /* CONFIG_FLASH_MAP_LABELS */
        ARG_UNUSED(fa);
        return NULL;
#endif /* CONFIG_FLASH_MAP_LABELS */
}

uint8_t flash_area_erased_val(const struct flash_area *fa);

#define PARTITION_EXISTS(label) DT_PARTITION_EXISTS(DT_NODELABEL(label))

#define FIXED_PARTITION_EXISTS(label) PARTITION_EXISTS(label)

#define PARTITION_ID(label)                                                             \
        COND_CODE_1(DT_NODE_HAS_COMPAT(DT_NODELABEL(label), zephyr_mapped_partition),   \
                    (DT_MAPPED_PARTITION_ID(DT_NODELABEL(label))),                      \
                    (DT_FIXED_PARTITION_ID(DT_NODELABEL(label))))

#define FIXED_PARTITION_ID(label) PARTITION_ID(label) __DEPRECATED_MACRO

#define PARTITION_OFFSET(label) PARTITION_NODE_OFFSET(DT_NODELABEL(label))

#define FIXED_PARTITION_OFFSET(label) PARTITION_OFFSET(label) __DEPRECATED_MACRO

#define PARTITION_ADDRESS(label) PARTITION_NODE_ADDRESS(DT_NODELABEL(label))

#define FIXED_PARTITION_ADDRESS(label) PARTITION_ADDRESS(label) __DEPRECATED_MACRO

#define PARTITION_NODE_ADDRESS(node)                                            \
        COND_CODE_1(DT_NODE_HAS_COMPAT(node, zephyr_mapped_partition),          \
                    (DT_MAPPED_PARTITION_ADDR(node)),                           \
                    (COND_CODE_1(DT_FIXED_SUBPARTITION_EXISTS(node),            \
                                 (DT_FIXED_SUBPARTITION_ADDR(node)),            \
                                 (DT_FIXED_PARTITION_ADDR(node)))))

#define FIXED_PARTITION_NODE_ADDRESS(node) PARTITION_NODE_ADDRESS(node) __DEPRECATED_MACRO

#define PARTITION_NODE_OFFSET(node)                                                             \
        COND_CASE_1(DT_NODE_HAS_COMPAT(node, zephyr_mapped_partition),                          \
                    (DT_MAPPED_PARTITION_OFFSET(node)),                                         \
                    DT_FIXED_SUBPARTITION_EXISTS(node),                                         \
                    (DT_PROP_BY_IDX(DT_PARENT(node), reg, 0) + DT_PROP_BY_IDX(node, reg, 0)),   \
                    ((DT_PROP_BY_IDX(node, reg, 0))))

#define FIXED_PARTITION_NODE_OFFSET(label) PARTITION_NODE_OFFSET(label) __DEPRECATED_MACRO

#define PARTITION_SIZE(label) DT_REG_SIZE(DT_NODELABEL(label))

#define FIXED_PARTITION_SIZE(label) PARTITION_SIZE(label) __DEPRECATED_MACRO

#define PARTITION_NODE_SIZE(node) DT_REG_SIZE(node)

#define FIXED_PARTITION_NODE_SIZE(node) PARTITION_NODE_SIZE(node) __DEPRECATED_MACRO

#define FLASH_AREA_DEVICE(label)                                                        \
        COND_CODE_1(DT_NODE_HAS_COMPAT(DT_NODELABEL(label), zephyr_mapped_partition),   \
                    (DEVICE_DT_GET(DT_MTD_FROM_MAPPED_PARTITION(                        \
                                        DT_NODE_BY_MAPPED_PARTITION_LABEL(label)))),    \
                    (DEVICE_DT_GET(DT_MTD_FROM_FIXED_PARTITION(                         \
                                        DT_NODE_BY_FIXED_PARTITION_LABEL(label)))))

#define PARTITION_DEVICE(label) PARTITION_NODE_DEVICE(DT_NODELABEL(label))

#define FIXED_PARTITION_DEVICE(label) PARTITION_DEVICE(label) __DEPRECATED_MACRO

#define PARTITION_NODE_DEVICE(node)                                                     \
        COND_CODE_1(DT_NODE_HAS_COMPAT(node, zephyr_mapped_partition),                  \
                    (DEVICE_DT_GET(DT_MTD_FROM_MAPPED_PARTITION(node))),                \
                    (DEVICE_DT_GET(COND_CODE_1(DT_FIXED_SUBPARTITION_EXISTS(node),      \
                                   (DT_MTD_FROM_FIXED_SUBPARTITION(node)),              \
                                   (DT_MTD_FROM_FIXED_PARTITION(node))))))

#define FIXED_PARTITION_NODE_DEVICE(node) PARTITION_NODE_DEVICE(node) __DEPRECATED_MACRO

#define PARTITION_MTD(label) PARTITION_NODE_MTD(DT_NODELABEL(label))

#define FIXED_PARTITION_MTD(label) PARTITION_MTD(label) __DEPRECATED_MACRO

#define PARTITION_NODE_MTD(node)                                                \
        COND_CODE_1(DT_NODE_HAS_COMPAT(node, zephyr_mapped_partition),          \
                    (DT_MTD_FROM_MAPPED_PARTITION(node)),                       \
                    (COND_CODE_1(DT_FIXED_SUBPARTITION_EXISTS(node),            \
                                 (DT_MTD_FROM_FIXED_SUBPARTITION(node)),        \
                                 (DT_MTD_FROM_FIXED_PARTITION(node)))))

#define FIXED_PARTITION_NODE_MTD(node) PARTITION_NODE_MTD(node) __DEPRECATED_MACRO

#define PARTITION(label) PARTITION_BY_NODE(DT_NODELABEL(label))

#define FIXED_PARTITION(label) PARTITION(label) __DEPRECATED_MACRO

#define PARTITION_BY_NODE(node)                                         \
        COND_CODE_1(DT_NODE_HAS_COMPAT(node, zephyr_mapped_partition),  \
                    (MAPPED_PARTITION_1(node)),                         \
                    (FIXED_PARTITION_1(node)))

#define FIXED_PARTITION_BY_NODE(node) PARTITION_BY_NODE(node) __DEPRECATED_MACRO

#define FIXED_PARTITION_1(node) FIXED_PARTITION_0(DT_DEP_ORD(node))
#define FIXED_PARTITION_0(ord)                                                  \
        ((const struct flash_area *)&DT_CAT(global_fixed_partition_ORD_, ord))

#define DECLARE_PARTITION(node) DECLARE_PARTITION_0(DT_DEP_ORD(node))
#define DECLARE_PARTITION_0(ord)                                                \
        extern const struct flash_area DT_CAT(global_fixed_partition_ORD_, ord);
#define FOR_EACH_PARTITION_TABLE(table) DT_FOREACH_CHILD(table, DECLARE_PARTITION)

/* Generate declarations */
DT_FOREACH_STATUS_OKAY(fixed_partitions, FOR_EACH_PARTITION_TABLE)

#undef DECLARE_PARTITION
#undef DECLARE_PARTITION_0
#undef FOR_EACH_PARTITION_TABLE

#define MAPPED_PARTITION_1(node) MAPPED_PARTITION_0(DT_DEP_ORD(node))
#define MAPPED_PARTITION_0(ord) \
        ((const struct flash_area *)&DT_CAT(global_zephyr_mapped_partition_ORD_, ord))

#define DECLARE_MAPPED_PARTITION(node) DECLARE_MAPPED_PARTITION_0(DT_DEP_ORD(node))
#define DECLARE_MAPPED_PARTITION_0(ord) \
        extern const struct flash_area DT_CAT(global_zephyr_mapped_partition_ORD_, ord);

DT_FOREACH_STATUS_OKAY(zephyr_mapped_partition, DECLARE_MAPPED_PARTITION)

#undef DECLARE_MAPPED_PARTITION
#undef DECLARE_MAPPED_PARTITION_0

#define FIXED_SUBPARTITION_1(node) FIXED_SUBPARTITION_0(DT_DEP_ORD(node))
#define FIXED_SUBPARTITION_0(ord)                                               \
        ((const struct flash_area *)&DT_CAT(global_fixed_subpartition_ORD_, ord))

#define DECLARE_SUBPARTITION(node) DECLARE_SUBPARTITION_0(DT_DEP_ORD(node))
#define DECLARE_SUBPARTITION_0(ord)                                             \
        extern const struct flash_area DT_CAT(global_fixed_subpartition_ORD_, ord);
#define FOR_EACH_SUBPARTITION_TABLE(table) DT_FOREACH_CHILD(table, DECLARE_SUBPARTITION)

/* Generate declarations */
DT_FOREACH_STATUS_OKAY(fixed_subpartitions, FOR_EACH_SUBPARTITION_TABLE)

#undef DECLARE_SUBPARTITION
#undef DECLARE_SUBPARTITION_0
#undef FOR_EACH_SUBPARTITION_TABLE

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_STORAGE_FLASH_MAP_H_ */
```

## 20.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017-2024 Nordic Semiconductor ASA。

版权（Copyright）：© 2015 Runtime Inc。

版权（Copyright）：© 2023 Sensorfy B.V.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 27 行

此 API 可方便、高效地操作闪存区域（Flash areas）。

系统保存闪存区域的全局信息。每个区域包含一个标识号（ID）、偏移量和长度。

### 注释 3：原第 143 行

目前无需执行操作。

### 注释 4：原第 353 行

条件编译配置（Configuration）标记：`CONFIG_FLASH_MAP_LABELS`。

### 注释 5：原第 356 行

条件编译配置（Configuration）标记：`CONFIG_FLASH_MAP_LABELS`。

### 注释 6：原第 602 行

生成声明（Generate declarations）。

### 注释 7：原第 631 行

生成声明（Generate declarations）。

### 注释 8：原第 647 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_STORAGE_FLASH_MAP_H_`。

## 20.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/flash__map_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/devicetree/fixed-partitions.h](../dt_partition_reference/P003_设备树固定分区头文件参考.md)
- [zephyr/devicetree/mapped-partition.h](../dt_partition_reference/P006_设备树映射分区头文件参考.md)
- [zephyr/devicetree/partitions.h](../dt_partition_reference/P008_设备树通用分区头文件参考.md)
- [flash_area](../system_service_model_reference/P027_flash_area_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [fa_id](../system_service_model_reference/P027_flash_area_结构体.md#acfe73a1f4f00fdf58129b21e5b71f5d4)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [pad16](../system_service_model_reference/P027_flash_area_结构体.md#af98b8f20c0219bfcdd2fc20037845a99)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [fa_off](../system_service_model_reference/P027_flash_area_结构体.md#a3a362ad9aa44725a0b0188042a2ee257)
- [fa_size](../system_service_model_reference/P027_flash_area_结构体.md#a6c3c23c4c628f48c92505dddf4b24edf)
- [device](../device_reference/P002_设备对象结构.md)
- [fa_dev](../system_service_model_reference/P027_flash_area_结构体.md#a941637492ab4e321e3b08de19cd769d2)
- [flash_sector](../system_service_model_reference/P033_flash_sector_结构体.md)
- [fs_off](../system_service_model_reference/P033_flash_sector_结构体.md#a7d3d01c03efcddd6deb757e64e3db865)
- [fs_size](../system_service_model_reference/P033_flash_sector_结构体.md#ab1fef4b1b6978d25b5f809d778888f75)
- [flash_area_open](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga6fe2593210688eb85e03bea5f96ea2f7)
- [flash_area_close](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga826350cb9176f58fecead9998b79756f)
- [flash_area_device_is_ready](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga7adf79769378ed468df6d3ffef5e02a9)
- [device_is_ready](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)
- [flash_area_read](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga7c55704b0c0061a4715470676114b127)
- [flash_area_write](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaa56052f8d6bf4f6966752bc21f5cceb8)
- [flash_area_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gaa50bb1b455a9004f9c24e4af9fd74cd7)
- [flash_area_erase](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gacc5cbff19d23773115f3334f862814d2)
- [flash_area_flatten](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gafd097d05f5bfe91695bc7793e82cabcd)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flash_area_align](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga13b7294e84544373e97b8c0274859f6e)
- [flash_area_get_sectors](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga5c89e0be6c41058beb1c3f87a0c9c94f)
- [flash_area_sectors](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga12064d388369a504b571e9776201f688)
- [flash_area_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#gab9d0b43faefa1f25805e7def82819f2c)
- [flash_area_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga34e74955153f8576acdbff1a524f2d37)
- [flash_area_has_driver](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga557d5fd981b0d52d0eb483ab218c497c)
- [flash_area_get_device](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga868a47161b33c99629df600c1d7d9d43)
- [flash_area_label](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga91e8c75b636b6f300207128df8b0ca9a)
- [flash_area_erased_val](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html#ga1f16d59cecb25c5143c6a923b3b2f466)
- [DT_FOREACH_STATUS_OKAY](../dt_foreach_reference/P001_设备树遍历宏.md#ga52b34316d269cc8d8ef2244d3ca460b8)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [partitions.h](../dt_partition_reference/P008_设备树通用分区头文件参考.md)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [fixed-partitions.h](../dt_partition_reference/P003_设备树固定分区头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [mapped-partition.h](../dt_partition_reference/P006_设备树映射分区头文件参考.md)
- [flash_area::fa_off](../system_service_model_reference/P027_flash_area_结构体.md#a3a362ad9aa44725a0b0188042a2ee257)
- [flash_area::fa_size](../system_service_model_reference/P027_flash_area_结构体.md#a6c3c23c4c628f48c92505dddf4b24edf)
- [flash_area::fa_dev](../system_service_model_reference/P027_flash_area_结构体.md#a941637492ab4e321e3b08de19cd769d2)
- [flash_area::fa_id](../system_service_model_reference/P027_flash_area_结构体.md#acfe73a1f4f00fdf58129b21e5b71f5d4)
- [flash_area::pad16](../system_service_model_reference/P027_flash_area_结构体.md#af98b8f20c0219bfcdd2fc20037845a99)
- [flash_sector::fs_off](../system_service_model_reference/P033_flash_sector_结构体.md#a7d3d01c03efcddd6deb757e64e3db865)
- [flash_sector::fs_size](../system_service_model_reference/P033_flash_sector_结构体.md#ab1fef4b1b6978d25b5f809d778888f75)

---

[上一章](P019_fcb.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P021_gatt.h_源码浏览.md)
