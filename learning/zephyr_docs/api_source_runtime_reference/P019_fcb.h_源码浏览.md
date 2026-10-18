---
id: learning.zephyr-docs.api-source-runtime-reference.page-19
title: fcb.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fcb_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_fcb.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fcb_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../storage/P071_闪存循环缓冲区头文件.md)。

## 19.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="l00040"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00156"></a>
<a id="l00163"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00316"></a>
<a id="l00323"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="aflash__map_8h_html"></a>
<a id="agroup__fcb__api_html_ga22b2bab8af3004c93e5d40659ccfec29"></a>
<a id="agroup__fcb__api_html_ga7908a252a09ebbb98b60a505220072bc"></a>
<a id="agroup__fcb__api_html_gaa9beaa3f5a6cc52b7e460d5670fdaabf"></a>
<a id="agroup__fcb__api_html_gaab78da410b7e709854e29219eb02a0c9"></a>
<a id="agroup__fcb__api_html_gaae445e8376db192ce45fff9dcf95c954"></a>
<a id="agroup__fcb__api_html_gab304f3e9e28f6229d7ddbe638eda2f70"></a>
<a id="agroup__fcb__api_html_gac15df95c0d9bed45c9da39802411598d"></a>
<a id="agroup__fcb__api_html_gad2fb288645e678dd6ea05b0871d5e774"></a>
<a id="agroup__fcb__api_html_gad50e579ec9430a23ef5525e74ceb21b2"></a>
<a id="agroup__fcb__api_html_gad567d124d8b0fe181ed54cfbe33b315c"></a>
<a id="agroup__fcb__api_html_gade8af12645d769ce3b27848976ada32a"></a>
<a id="agroup__fcb__api_html_gaeed5144438ee00d83c9b3d3b4b7490ea"></a>
<a id="agroup__fcb__internal_html_ga0b921b509dab767661058d164e80f55e"></a>
<a id="agroup__fcb__internal_html_gafcfb9b6d4b5c0e593c0a9e512a0ec309"></a>
<a id="ainttypes_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="alimits_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructfcb__entry__ctx_html"></a>
<a id="astructfcb__entry__ctx_html_a0da5217647b82c8799a6cde221253680"></a>
<a id="astructfcb__entry__ctx_html_a8b491cd670e609c2b4d897d15e37eb2b"></a>
<a id="astructfcb__entry_html"></a>
<a id="astructfcb__entry_html_a6d01cb2107949bf4f0a2779c9781261f"></a>
<a id="astructfcb__entry_html_a82cba5933875498c804f31722a6e90f9"></a>
<a id="astructfcb__entry_html_aa207d21d51bc2c7aa838ca9dc3b52be7"></a>
<a id="astructfcb__entry_html_aa564f9f79012beb20265bc5e85816fea"></a>
<a id="astructfcb_html"></a>
<a id="astructfcb_html_a030b96abd6c857295f154197278cca69"></a>
<a id="astructfcb_html_a16cfc82afc8abe70291f4b462e617f2f"></a>
<a id="astructfcb_html_a1f30c78d7e02748fbf0bf5033d4bdadf"></a>
<a id="astructfcb_html_a1f7922dc1e8076bcfffca117260d5e02"></a>
<a id="astructfcb_html_a4206faa9ed633ba2315163c52e557397"></a>
<a id="astructfcb_html_a614c6441395637c6c0a17a4fd6107db3"></a>
<a id="astructfcb_html_a6e66e3657ff946da9b87594b819de075"></a>
<a id="astructfcb_html_a8da1d0b4bef7d9ddcd5922d9bbef0cef"></a>
<a id="astructfcb_html_aa745e88d4477408b40a759dd1baea637"></a>
<a id="astructfcb_html_aab748de6989e30de6571fc94d66ee365"></a>
<a id="astructfcb_html_ac6dc6236f8b03e4b03f691c55b4d3327"></a>
<a id="astructfcb_html_afc96f045d541c8d141d3427884f1fb44"></a>
<a id="astructflash__area_html"></a>
<a id="astructflash__sector_html"></a>
<a id="astructk__mutex_html"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2017-2023 Nordic Semiconductor ASA
 * Copyright (c) 2015 Runtime Inc
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_FS_FCB_H_
#define ZEPHYR_INCLUDE_FS_FCB_H_

/*
 * Flash circular buffer.
 */
#include <inttypes.h>
#include <limits.h>

#include <zephyr/storage/flash_map.h>
#include <zephyr/sys/util_macro.h>

#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif



#define FCB_MAX_LEN     (0x3fffu)

struct fcb_entry {
        struct flash_sector *fe_sector;

        uint32_t fe_elem_off;

        uint32_t fe_data_off;

        uint16_t fe_data_len;
};

#define FCB_ENTRY_FA_DATA_OFF(entry) (entry.fe_sector->fs_off +\
                                      entry.fe_data_off)

struct fcb_entry_ctx {
        struct fcb_entry loc;
        const struct flash_area *fap;
};

#define FCB_FLAGS_CRC_DISABLED BIT(0)

struct fcb {
        /* Caller of fcb_init fills this in */
        uint32_t f_magic;

        uint8_t f_version;
        uint16_t f_sector_cnt;
        uint8_t f_scratch_cnt;

        struct flash_sector *f_sectors;

        /* Flash circular buffer internal state */
        struct k_mutex f_mtx;

        struct flash_sector *f_oldest;

        struct fcb_entry f_active;
        uint16_t f_active_id;

        uint8_t f_align;

        const struct flash_area *fap;

        uint8_t f_erase_value;
#ifdef CONFIG_FCB_ALLOW_FIXED_ENDMARKER
        const uint8_t f_flags;
#endif
};



int fcb_init(int f_area_id, struct fcb *fcbp);

int fcb_append(struct fcb *fcbp, uint16_t len, struct fcb_entry *loc);

int fcb_append_finish(struct fcb *fcbp, struct fcb_entry *append_loc);

typedef int (*fcb_walk_cb)(struct fcb_entry_ctx *loc_ctx, void *arg);

int fcb_walk(struct fcb *fcbp, struct flash_sector *sector, fcb_walk_cb cb, void *cb_arg);

int fcb_getnext(struct fcb *fcbp, struct fcb_entry *loc);

int fcb_rotate(struct fcb *fcbp);

int fcb_append_to_scratch(struct fcb *fcbp);

int fcb_free_sector_cnt(struct fcb *fcbp);

int fcb_is_empty(struct fcb *fcbp);

int fcb_offset_last_n(struct fcb *fcbp, uint8_t entries, struct fcb_entry *last_n_entry);

int fcb_clear(struct fcb *fcbp);



int fcb_flash_read(const struct fcb *fcbp, const struct flash_sector *sector, off_t off,
                   void *dst, size_t len);

int fcb_flash_write(const struct fcb *fcbp, const struct flash_sector *sector, off_t off,
                    const void *src, size_t len);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_FS_FCB_H_ */
```

## 19.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017-2023 Nordic Semiconductor ASA。

版权（Copyright）：© 2015 Runtime Inc。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 17 行

闪存循环缓冲区（Flash circular buffer）。

### 注释 3：原第 102 行

由 `fcb_init` 的调用者填写。

### 注释 4：原第 122 行

闪存循环缓冲区内部状态（Internal state）。

### 注释 5：原第 360 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_FS_FCB_H_`。

## 19.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../storage/P071_闪存循环缓冲区头文件.md)
- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h.html)
- [limits.h](https://docs.zephyrproject.org/latest/doxygen/html/limits_8h.html)
- [zephyr/storage/flash_map.h](https://docs.zephyrproject.org/latest/doxygen/html/flash__map_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [fcb_entry](../storage/P051_闪存循环缓冲区条目结构.md)
- [flash_sector](../system_service_model_reference/P033_flash_sector_结构体.md)
- [fe_sector](https://docs.zephyrproject.org/latest/doxygen/html/structfcb__entry.html#aa564f9f79012beb20265bc5e85816fea)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [fe_elem_off](https://docs.zephyrproject.org/latest/doxygen/html/structfcb__entry.html#a6d01cb2107949bf4f0a2779c9781261f)
- [fe_data_off](https://docs.zephyrproject.org/latest/doxygen/html/structfcb__entry.html#a82cba5933875498c804f31722a6e90f9)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [fe_data_len](https://docs.zephyrproject.org/latest/doxygen/html/structfcb__entry.html#aa207d21d51bc2c7aa838ca9dc3b52be7)
- [fcb_entry_ctx](../storage/P052_闪存循环缓冲区条目上下文.md)
- [loc](https://docs.zephyrproject.org/latest/doxygen/html/structfcb__entry__ctx.html#a0da5217647b82c8799a6cde221253680)
- [flash_area](../system_service_model_reference/P027_flash_area_结构体.md)
- [fap](https://docs.zephyrproject.org/latest/doxygen/html/structfcb__entry__ctx.html#a8b491cd670e609c2b4d897d15e37eb2b)
- [fcb](../storage/P050_闪存循环缓冲区实例结构.md)
- [f_magic](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a4206faa9ed633ba2315163c52e557397)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [f_version](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a030b96abd6c857295f154197278cca69)
- [f_sector_cnt](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a6e66e3657ff946da9b87594b819de075)
- [f_scratch_cnt](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#aab748de6989e30de6571fc94d66ee365)
- [f_sectors](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#afc96f045d541c8d141d3427884f1fb44)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [f_mtx](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a1f30c78d7e02748fbf0bf5033d4bdadf)
- [f_oldest](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#ac6dc6236f8b03e4b03f691c55b4d3327)
- [f_active](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a1f7922dc1e8076bcfffca117260d5e02)
- [f_active_id](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a8da1d0b4bef7d9ddcd5922d9bbef0cef)
- [f_align](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#aa745e88d4477408b40a759dd1baea637)
- [fap](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a16cfc82afc8abe70291f4b462e617f2f)
- [f_erase_value](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a614c6441395637c6c0a17a4fd6107db3)
- [fcb_init](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html#gab304f3e9e28f6229d7ddbe638eda2f70)
- [fcb_append](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html#gad567d124d8b0fe181ed54cfbe33b315c)
- [fcb_append_finish](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html#gaae445e8376db192ce45fff9dcf95c954)
- [fcb_walk_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html#gaeed5144438ee00d83c9b3d3b4b7490ea)
- [fcb_walk](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html#gad50e579ec9430a23ef5525e74ceb21b2)
- [fcb_getnext](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html#ga7908a252a09ebbb98b60a505220072bc)
- [fcb_rotate](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html#gad2fb288645e678dd6ea05b0871d5e774)
- [fcb_append_to_scratch](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html#ga22b2bab8af3004c93e5d40659ccfec29)
- [fcb_free_sector_cnt](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html#gaa9beaa3f5a6cc52b7e460d5670fdaabf)
- [fcb_is_empty](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html#gade8af12645d769ce3b27848976ada32a)
- [fcb_offset_last_n](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html#gac15df95c0d9bed45c9da39802411598d)
- [fcb_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__api.html#gaab78da410b7e709854e29219eb02a0c9)
- [fcb_flash_read](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__internal.html#ga0b921b509dab767661058d164e80f55e)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [fcb_flash_write](https://docs.zephyrproject.org/latest/doxygen/html/group__fcb__internal.html#gafcfb9b6d4b5c0e593c0a9e512a0ec309)
- [flash_map.h](https://docs.zephyrproject.org/latest/doxygen/html/flash__map_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [fcb_entry_ctx::loc](https://docs.zephyrproject.org/latest/doxygen/html/structfcb__entry__ctx.html#a0da5217647b82c8799a6cde221253680)
- [fcb_entry_ctx::fap](https://docs.zephyrproject.org/latest/doxygen/html/structfcb__entry__ctx.html#a8b491cd670e609c2b4d897d15e37eb2b)
- [fcb_entry::fe_elem_off](https://docs.zephyrproject.org/latest/doxygen/html/structfcb__entry.html#a6d01cb2107949bf4f0a2779c9781261f)
- [fcb_entry::fe_data_off](https://docs.zephyrproject.org/latest/doxygen/html/structfcb__entry.html#a82cba5933875498c804f31722a6e90f9)
- [fcb_entry::fe_data_len](https://docs.zephyrproject.org/latest/doxygen/html/structfcb__entry.html#aa207d21d51bc2c7aa838ca9dc3b52be7)
- [fcb_entry::fe_sector](https://docs.zephyrproject.org/latest/doxygen/html/structfcb__entry.html#aa564f9f79012beb20265bc5e85816fea)
- [fcb::f_version](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a030b96abd6c857295f154197278cca69)
- [fcb::fap](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a16cfc82afc8abe70291f4b462e617f2f)
- [fcb::f_mtx](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a1f30c78d7e02748fbf0bf5033d4bdadf)
- [fcb::f_active](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a1f7922dc1e8076bcfffca117260d5e02)
- [fcb::f_magic](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a4206faa9ed633ba2315163c52e557397)
- [fcb::f_erase_value](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a614c6441395637c6c0a17a4fd6107db3)
- [fcb::f_sector_cnt](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a6e66e3657ff946da9b87594b819de075)
- [fcb::f_active_id](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#a8da1d0b4bef7d9ddcd5922d9bbef0cef)
- [fcb::f_align](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#aa745e88d4477408b40a759dd1baea637)
- [fcb::f_scratch_cnt](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#aab748de6989e30de6571fc94d66ee365)
- [fcb::f_oldest](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#ac6dc6236f8b03e4b03f691c55b4d3327)
- [fcb::f_sectors](https://docs.zephyrproject.org/latest/doxygen/html/structfcb.html#afc96f045d541c8d141d3427884f1fb44)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P018_eth_nxp_enet_qos.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P020_flash_map.h_源码浏览.md)
