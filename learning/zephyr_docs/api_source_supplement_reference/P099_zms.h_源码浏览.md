---
id: learning.zephyr-docs.api-source-supplement-reference.page-99
title: zms.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kvss_2zms_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_zms.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/kvss_2zms_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../storage/P075_Zephyr内存存储头文件.md)。

## 99.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
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
<a id="l00036"></a>
<a id="l00042"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="foldopen00146"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="foldopen00164"></a>
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
<a id="foldopen00182"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00206"></a>
<a id="l00212"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="adevice_8h_html"></a>
<a id="aflash_8h_html"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__zms__data__structures_html_ga0509b3dce3030a56ecff866d693944f9"></a>
<a id="agroup__zms__data__structures_html_ga5f9a7529c95876c29b6a0fd7a230fc92"></a>
<a id="agroup__zms__data__structures_html_ga73c4c209bc4fbb8125781088b15eef64"></a>
<a id="agroup__zms__data__structures_html_gga5f9a7529c95876c29b6a0fd7a230fc92a0b00eefe2f9cc169d285ad8255521c87"></a>
<a id="agroup__zms__high__level__api_html_ga02be33c18632687133f53557b5ee8bc2"></a>
<a id="agroup__zms__high__level__api_html_ga218132ef5cb0f2157721cb62886de842"></a>
<a id="agroup__zms__high__level__api_html_ga2c839e3cceb3fd4931a2ffc26726ca34"></a>
<a id="agroup__zms__high__level__api_html_ga31b8d970e70fd7cbb94a0dc068dbdcfc"></a>
<a id="agroup__zms__high__level__api_html_ga4aa193a3c357335a6d403139371803ab"></a>
<a id="agroup__zms__high__level__api_html_ga60ad1d79cd4f3ada1cf726d422c120c3"></a>
<a id="agroup__zms__high__level__api_html_ga6cedc2fe5bfe8aa6183d41273897f0e7"></a>
<a id="agroup__zms__high__level__api_html_ga76e06261e54f9d2ee65f7d31328e3bcc"></a>
<a id="agroup__zms__high__level__api_html_ga7ca762e1b37186a2a2bf1dce5333272d"></a>
<a id="agroup__zms__high__level__api_html_ga8871cfa165587b259a8043d22bf669a4"></a>
<a id="agroup__zms__high__level__api_html_ga8d61da1f5c0727bfa543fa9d5da7558f"></a>
<a id="agroup__zms__high__level__api_html_ga90a6f8c47f02641ca33ee42a7c709750"></a>
<a id="agroup__zms__high__level__api_html_ga962625b12f21cf030a35c944a2de380e"></a>
<a id="agroup__zms__high__level__api_html_gaa37ba625bd4835acf772b0cdb38a3348"></a>
<a id="agroup__zms__high__level__api_html_gab5a3adcdc5eecbb8a1bcb9d1c7709837"></a>
<a id="agroup__zms__high__level__api_html_gaba4e19c06a27a5287e9f8507a4fa11c3"></a>
<a id="agroup__zms__high__level__api_html_gafe06d28af34fbecf2bd666ef11095ed1"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructzms__fs_html"></a>
<a id="astructzms__fs_html_a19baa487b73542d4075eeb4ea24c303f"></a>
<a id="astructzms__fs_html_a25f2b002e4189ee29432198991061b7a"></a>
<a id="astructzms__fs_html_a2628eaff292518933e037b871179b8ea"></a>
<a id="astructzms__fs_html_a352dad2283b804c1318748bd05efaf75"></a>
<a id="astructzms__fs_html_a41063275f2211115abf00c4dbceb45cc"></a>
<a id="astructzms__fs_html_a6c28786531454a050f81981d32ca3640"></a>
<a id="astructzms__fs_html_a939f1c9100dc9d2efdc163aea61e38a3"></a>
<a id="astructzms__fs_html_aae1ffd5eebd0bfb4c898719c221a239f"></a>
<a id="astructzms__fs_html_ab3b4551a3007e4b36bfd8a2fc209b543"></a>
<a id="astructzms__fs_html_ad8960c2cee8e03446aca96697c0c9e4a"></a>
<a id="astructzms__fs_html_af2dfcc5d0e8eabc5f116e2964668b05f"></a>
<a id="astructzms__fs_html_af46a398f15fbb933d46c0b16283dae16"></a>
<a id="astructzms__fs_html_af524e7a105749a3dbff41a229c20443b"></a>
<a id="astructzms__iter__config_html"></a>
<a id="astructzms__iter__config_html_a4a23feb82c0e0456839bcea5d6296e23"></a>
<a id="astructzms__iter__config_html_a65b7fbc563c7222f0ae9549b84932ae8"></a>
<a id="astructzms__iter__config_html_a829f0fa76965955a302be4ccc0206150"></a>
<a id="astructzms__iter__config_html_a966d6318cf92a10c0d0df092badc8d9a"></a>
<a id="astructzms__iter__config_html_aaa2fad64dd01813dfee027dac55fd43e"></a>
<a id="astructzms__iter__config_html_adb97ffe9fa5dda172aaf4cde2be82a8a"></a>
<a id="astructzms__iter__config_html_ae97b3ae143582a23288a914e011b42e1"></a>
<a id="astructzms__iter_html"></a>
<a id="astructzms__iter_html_a14cf09843ce4046d541d4a5f7990685e"></a>
<a id="astructzms__iter_html_a1d2a58a6567d7143466372367e5cf73a"></a>
<a id="astructzms__iter_html_a2bbec3cf7aede64963a2bd2c5f03805a"></a>
<a id="astructzms__iter_html_a8a55a1e4aad54e9afed4da41813a2bd2"></a>
<a id="astructzms__iter_html_a958cec07dd78062c93c9db7f2ccb2370"></a>
<a id="astructzms__iter_html_a998147073d23464bf69077e47269f0de"></a>
<a id="astructzms__iter_html_aac50c79d889b0954df0cbb781747ef8d"></a>
<a id="astructzms__iter_html_ac7192fda17eabc58698615936691b89d"></a>
<a id="astructzms__iter_html_afaabf24d2be5a633c3370d9949abaacd"></a>
<a id="atoolchain_8h_html"></a>

```c
/* Copyright (c) 2018 Laczen
 * Copyright (c) 2024 BayLibre SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * ZMS: Zephyr Memory Storage
 */


#ifndef ZEPHYR_INCLUDE_KVSS_ZMS_H_
#define ZEPHYR_INCLUDE_KVSS_ZMS_H_

#include <sys/types.h>
#include <zephyr/drivers/flash.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif



enum zms_mount_flags {
        ZMS_MOUNT_FLAG_NO_FORMAT = BIT(0),
};

#if CONFIG_ZMS_ID_64BIT
typedef uint64_t zms_id_t;
#else
typedef uint32_t zms_id_t;
#endif

#if CONFIG_ZMS_ID_64BIT
#define ZMS_DATA_IN_ATE_SIZE 4
#else
#define ZMS_DATA_IN_ATE_SIZE 8
#endif

#define ZMS_ITER_ID_MIN ((zms_id_t)0)

#define ZMS_ITER_ID_MAX ((zms_id_t)~(zms_id_t)0)

#define ZMS_ITER_MASK_ALL ZMS_ITER_ID_MAX

typedef bool (*zms_iter_predicate_t)(zms_id_t id);

struct zms_fs {
        off_t offset;
        uint64_t ate_wra;
        uint64_t data_wra;
        uint32_t sector_size;
        uint32_t sector_count;
        uint32_t mount_flags;
        uint8_t sector_cycle;
        bool ready;
        bool lock_initialized;
        struct k_mutex zms_lock;
        const struct device *flash_device;
        const struct flash_parameters *flash_parameters;
        size_t ate_size;
#if CONFIG_ZMS_LOOKUP_CACHE
#if CONFIG_ZMS_LOOKUP_CACHE_MANUAL
        uint64_t *lookup_cache;
        size_t lookup_cache_size;
#else
        uint64_t lookup_cache[CONFIG_ZMS_LOOKUP_CACHE_SIZE];
#endif
#endif
};

struct zms_iter_config {
        zms_id_t mask_id;
        zms_id_t min_id;
        zms_id_t max_id;
        bool use_mask;
        bool use_range;
        bool use_predicate;
        zms_iter_predicate_t predicate_func;
};

#define ZMS_ITER_CONFIG_DEFAULT \
        { \
                .mask_id = ZMS_ITER_MASK_ALL, \
                .min_id = ZMS_ITER_ID_MIN, \
                .max_id = ZMS_ITER_ID_MAX, \
                .use_mask = false, \
                .use_range = false, \
                .use_predicate = false, \
                .predicate_func = NULL, \
        }

struct zms_iter {
        uint64_t walk_addr;
        uint64_t end_addr;
        zms_id_t mask_id;
        zms_id_t min_id;
        zms_id_t max_id;
        zms_iter_predicate_t predicate_func;
        bool exhausted;
        int previous_sector_num;
        uint8_t current_cycle;
};



int zms_mount(struct zms_fs *fs);

int zms_mount_force(struct zms_fs *fs);

int zms_clear(struct zms_fs *fs);

ssize_t zms_write(struct zms_fs *fs, zms_id_t id, const void *data, size_t len);

int zms_delete(struct zms_fs *fs, zms_id_t id);

ssize_t zms_read(struct zms_fs *fs, zms_id_t id, void *data, size_t len);

ssize_t zms_read_hist(struct zms_fs *fs, zms_id_t id, void *data, size_t len, uint32_t cnt);

ssize_t zms_get_data_length(struct zms_fs *fs, zms_id_t id);

ssize_t zms_calc_free_space(struct zms_fs *fs);

ssize_t zms_active_sector_free_space(struct zms_fs *fs);

int zms_sector_use_next(struct zms_fs *fs);

#if CONFIG_ZMS_LOOKUP_CACHE_MANUAL
int zms_set_lookup_cache(struct zms_fs *fs, uint64_t *buffer, size_t size);
#endif

int zms_get_num_cycles(struct zms_fs *fs, uint32_t *cycles);

int zms_get_sector_num_cycles(struct zms_fs *fs, uint32_t sector, uint32_t *cycles);

int zms_iter_init_with_config(const struct zms_fs *fs, struct zms_iter *iter,
                              const struct zms_iter_config *config);

int zms_iter_init(const struct zms_fs *fs, struct zms_iter *iter);

int zms_iter_next(struct zms_fs *fs, struct zms_iter *iter, zms_id_t *id, size_t *len, void *data,
                  size_t data_len);

int zms_iter_next_all(struct zms_fs *fs, struct zms_iter *iter, zms_id_t *id, size_t *len,
                      void *data, size_t data_len);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_KVSS_ZMS_H_ */
```

## 99.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Laczen；© 2024 BayLibre SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

ZMS：Zephyr 存储系统（Zephyr Memory Storage）。

### 注释 2：原第 596 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_KVSS_ZMS_H_`。

## 99.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../storage/P075_Zephyr内存存储头文件.md)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/drivers/flash.h](../flash_reference/P009_Flash公共头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zms_mount_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga5f9a7529c95876c29b6a0fd7a230fc92)
- [ZMS_MOUNT_FLAG_NO_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#gga5f9a7529c95876c29b6a0fd7a230fc92a0b00eefe2f9cc169d285ad8255521c87)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [zms_id_t](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga0509b3dce3030a56ecff866d693944f9)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [zms_iter_predicate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__data__structures.html#ga73c4c209bc4fbb8125781088b15eef64)
- [zms_fs](../storage/P060_Zephyr内存存储实例结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [offset](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#af2dfcc5d0e8eabc5f116e2964668b05f)
- [ate_wra](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a6c28786531454a050f81981d32ca3640)
- [data_wra](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a25f2b002e4189ee29432198991061b7a)
- [sector_size](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#aae1ffd5eebd0bfb4c898719c221a239f)
- [sector_count](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#ad8960c2cee8e03446aca96697c0c9e4a)
- [mount_flags](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a41063275f2211115abf00c4dbceb45cc)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sector_cycle](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#ab3b4551a3007e4b36bfd8a2fc209b543)
- [ready](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#af46a398f15fbb933d46c0b16283dae16)
- [lock_initialized](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a352dad2283b804c1318748bd05efaf75)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [zms_lock](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#af524e7a105749a3dbff41a229c20443b)
- [device](../device_reference/P002_设备对象结构.md)
- [flash_device](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a2628eaff292518933e037b871179b8ea)
- [flash_parameters](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a19baa487b73542d4075eeb4ea24c303f)
- [ate_size](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a939f1c9100dc9d2efdc163aea61e38a3)
- [zms_iter_config](../storage/P062_Zephyr内存存储迭代配置.md)
- [mask_id](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#ae97b3ae143582a23288a914e011b42e1)
- [min_id](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a966d6318cf92a10c0d0df092badc8d9a)
- [max_id](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#adb97ffe9fa5dda172aaf4cde2be82a8a)
- [use_mask](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#aaa2fad64dd01813dfee027dac55fd43e)
- [use_range](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a4a23feb82c0e0456839bcea5d6296e23)
- [use_predicate](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a829f0fa76965955a302be4ccc0206150)
- [predicate_func](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a65b7fbc563c7222f0ae9549b84932ae8)
- [zms_iter](../storage/P061_Zephyr内存存储迭代器结构.md)
- [walk_addr](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#ac7192fda17eabc58698615936691b89d)
- [end_addr](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a998147073d23464bf69077e47269f0de)
- [mask_id](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a8a55a1e4aad54e9afed4da41813a2bd2)
- [min_id](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#aac50c79d889b0954df0cbb781747ef8d)
- [max_id](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a1d2a58a6567d7143466372367e5cf73a)
- [predicate_func](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a14cf09843ce4046d541d4a5f7990685e)
- [exhausted](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#afaabf24d2be5a633c3370d9949abaacd)
- [previous_sector_num](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a2bbec3cf7aede64963a2bd2c5f03805a)
- [current_cycle](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a958cec07dd78062c93c9db7f2ccb2370)
- [zms_mount](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga962625b12f21cf030a35c944a2de380e)
- [zms_mount_force](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gab5a3adcdc5eecbb8a1bcb9d1c7709837)
- [zms_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gafe06d28af34fbecf2bd666ef11095ed1)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [zms_write](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga218132ef5cb0f2157721cb62886de842)
- [zms_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga60ad1d79cd4f3ada1cf726d422c120c3)
- [zms_read](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga8d61da1f5c0727bfa543fa9d5da7558f)
- [zms_read_hist](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga6cedc2fe5bfe8aa6183d41273897f0e7)
- [zms_get_data_length](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga8871cfa165587b259a8043d22bf669a4)
- [zms_calc_free_space](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga02be33c18632687133f53557b5ee8bc2)
- [zms_active_sector_free_space](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga76e06261e54f9d2ee65f7d31328e3bcc)
- [zms_sector_use_next](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga90a6f8c47f02641ca33ee42a7c709750)
- [zms_get_num_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga31b8d970e70fd7cbb94a0dc068dbdcfc)
- [zms_get_sector_num_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga4aa193a3c357335a6d403139371803ab)
- [zms_iter_init_with_config](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga2c839e3cceb3fd4931a2ffc26726ca34)
- [zms_iter_init](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#ga7ca762e1b37186a2a2bf1dce5333272d)
- [zms_iter_next](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaba4e19c06a27a5287e9f8507a4fa11c3)
- [zms_iter_next_all](https://docs.zephyrproject.org/latest/doxygen/html/group__zms__high__level__api.html#gaa37ba625bd4835acf772b0cdb38a3348)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [flash.h](../flash_reference/P009_Flash公共头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zms_fs::flash_parameters](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a19baa487b73542d4075eeb4ea24c303f)
- [zms_fs::data_wra](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a25f2b002e4189ee29432198991061b7a)
- [zms_fs::flash_device](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a2628eaff292518933e037b871179b8ea)
- [zms_fs::lock_initialized](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a352dad2283b804c1318748bd05efaf75)
- [zms_fs::mount_flags](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a41063275f2211115abf00c4dbceb45cc)
- [zms_fs::ate_wra](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a6c28786531454a050f81981d32ca3640)
- [zms_fs::ate_size](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#a939f1c9100dc9d2efdc163aea61e38a3)
- [zms_fs::sector_size](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#aae1ffd5eebd0bfb4c898719c221a239f)
- [zms_fs::sector_cycle](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#ab3b4551a3007e4b36bfd8a2fc209b543)
- [zms_fs::sector_count](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#ad8960c2cee8e03446aca96697c0c9e4a)
- [zms_fs::offset](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#af2dfcc5d0e8eabc5f116e2964668b05f)
- [zms_fs::ready](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#af46a398f15fbb933d46c0b16283dae16)
- [zms_fs::zms_lock](https://docs.zephyrproject.org/latest/doxygen/html/structzms__fs.html#af524e7a105749a3dbff41a229c20443b)
- [zms_iter_config::use_range](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a4a23feb82c0e0456839bcea5d6296e23)
- [zms_iter_config::predicate_func](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a65b7fbc563c7222f0ae9549b84932ae8)
- [zms_iter_config::use_predicate](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a829f0fa76965955a302be4ccc0206150)
- [zms_iter_config::min_id](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#a966d6318cf92a10c0d0df092badc8d9a)
- [zms_iter_config::use_mask](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#aaa2fad64dd01813dfee027dac55fd43e)
- [zms_iter_config::max_id](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#adb97ffe9fa5dda172aaf4cde2be82a8a)
- [zms_iter_config::mask_id](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter__config.html#ae97b3ae143582a23288a914e011b42e1)
- [zms_iter::predicate_func](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a14cf09843ce4046d541d4a5f7990685e)
- [zms_iter::max_id](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a1d2a58a6567d7143466372367e5cf73a)
- [zms_iter::previous_sector_num](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a2bbec3cf7aede64963a2bd2c5f03805a)
- [zms_iter::mask_id](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a8a55a1e4aad54e9afed4da41813a2bd2)
- [zms_iter::current_cycle](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a958cec07dd78062c93c9db7f2ccb2370)
- [zms_iter::end_addr](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#a998147073d23464bf69077e47269f0de)
- [zms_iter::min_id](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#aac50c79d889b0954df0cbb781747ef8d)
- [zms_iter::walk_addr](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#ac7192fda17eabc58698615936691b89d)
- [zms_iter::exhausted](https://docs.zephyrproject.org/latest/doxygen/html/structzms__iter.html#afaabf24d2be5a633c3370d9949abaacd)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P098_nvs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P100_loader.h_源码浏览.md)
