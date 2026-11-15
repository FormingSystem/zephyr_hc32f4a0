---
id: learning.zephyr-docs.api-source-supplement-reference.page-98
title: nvs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kvss_2nvs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第98章\_nvs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/kvss_2nvs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../storage/P073_非易失性存储头文件.md)。

## 98.1\_原始可见代码（Source Code）

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
<a id="l00035"></a>
<a id="l00042"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00077"></a>
<a id="l00084"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__nvs__high__level__api_html_ga341fd2ad029709cbb6eafde1ae88603f"></a>
<a id="agroup__nvs__high__level__api_html_ga34d40e9f63ba514d7915b72c4fef0b82"></a>
<a id="agroup__nvs__high__level__api_html_ga37e5a55f0b9209c7c0c95db9e1e84715"></a>
<a id="agroup__nvs__high__level__api_html_ga42ee9fd0d98f89dcabc5888f8b4600f0"></a>
<a id="agroup__nvs__high__level__api_html_ga52db47389e9aa2b0de77497f0e60ed5b"></a>
<a id="agroup__nvs__high__level__api_html_ga5fd4175a4976e6d3ee8621ed95e0ee9e"></a>
<a id="agroup__nvs__high__level__api_html_ga7ce6065cf3ac68544f51d26cabd983b2"></a>
<a id="agroup__nvs__high__level__api_html_ga8e525038e353045ad6cd90607e887b0d"></a>
<a id="agroup__nvs__high__level__api_html_gab932ea2d6e933825c2378bef8c30b065"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructnvs__fs_html"></a>
<a id="astructnvs__fs_html_a02381974223dfbd22fe50b2cfecb7da2"></a>
<a id="astructnvs__fs_html_a2a167bd6a1698d2070dbe65b669ba0f4"></a>
<a id="astructnvs__fs_html_a34f769be6fed7c81254501af207147df"></a>
<a id="astructnvs__fs_html_a6f49bb17819e3b78e0b3c1a1bc578f09"></a>
<a id="astructnvs__fs_html_a793b43b069d5e7a42963d84423ab5717"></a>
<a id="astructnvs__fs_html_aba5caa7709d58fa018cbb91db085f140"></a>
<a id="astructnvs__fs_html_abf8ffaea29e3357ca6e897902fd49a63"></a>
<a id="astructnvs__fs_html_ac6bc3719e803f27fc20de5ebc63d7707"></a>
<a id="astructnvs__fs_html_aeec2d70881591f9b85ae5bb39a064476"></a>
<a id="atoolchain_8h_html"></a>

```c
/*  NVS: non volatile storage in flash
 *
 * Copyright (c) 2018 Laczen
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_KVSS_NVS_H_
#define ZEPHYR_INCLUDE_KVSS_NVS_H_

#include <sys/types.h>
#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif



struct nvs_fs {
        off_t offset;
        uint32_t ate_wra;
        uint32_t data_wra;
        uint32_t sector_size;
        uint16_t sector_count;
        bool ready;
        struct k_mutex nvs_lock;
        const struct device *flash_device;
        const struct flash_parameters *flash_parameters;
#if CONFIG_NVS_LOOKUP_CACHE
        uint32_t lookup_cache[CONFIG_NVS_LOOKUP_CACHE_SIZE];
#endif
};



int nvs_mount(struct nvs_fs *fs);

int nvs_clear(struct nvs_fs *fs);

ssize_t nvs_write(struct nvs_fs *fs, uint16_t id, const void *data, size_t len);

int nvs_delete(struct nvs_fs *fs, uint16_t id);

ssize_t nvs_read(struct nvs_fs *fs, uint16_t id, void *data, size_t len);

ssize_t nvs_read_hist(struct nvs_fs *fs, uint16_t id, void *data, size_t len, uint16_t cnt);

ssize_t nvs_calc_free_space(struct nvs_fs *fs);

size_t nvs_sector_max_data_size(struct nvs_fs *fs);

int nvs_sector_use_next(struct nvs_fs *fs);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_KVSS_NVS_H_ */
```

## 98.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

NVS：闪存中的非易失性存储（Non-volatile storage）。

版权（Copyright）：© 2018 Laczen。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 206 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_KVSS_NVS_H_`。

## 98.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../storage/P073_非易失性存储头文件.md)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [nvs_fs](../storage/P056_非易失性存储实例结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [offset](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#a793b43b069d5e7a42963d84423ab5717)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [ate_wra](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#aba5caa7709d58fa018cbb91db085f140)
- [data_wra](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#ac6bc3719e803f27fc20de5ebc63d7707)
- [sector_size](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#aeec2d70881591f9b85ae5bb39a064476)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [sector_count](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#abf8ffaea29e3357ca6e897902fd49a63)
- [ready](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#a2a167bd6a1698d2070dbe65b669ba0f4)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [nvs_lock](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#a6f49bb17819e3b78e0b3c1a1bc578f09)
- [device](../device_reference/P002_设备对象结构.md)
- [flash_device](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#a02381974223dfbd22fe50b2cfecb7da2)
- [flash_parameters](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#a34f769be6fed7c81254501af207147df)
- [nvs_mount](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs__high__level__api.html#gab932ea2d6e933825c2378bef8c30b065)
- [nvs_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs__high__level__api.html#ga42ee9fd0d98f89dcabc5888f8b4600f0)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [nvs_write](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs__high__level__api.html#ga34d40e9f63ba514d7915b72c4fef0b82)
- [nvs_delete](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs__high__level__api.html#ga5fd4175a4976e6d3ee8621ed95e0ee9e)
- [nvs_read](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs__high__level__api.html#ga341fd2ad029709cbb6eafde1ae88603f)
- [nvs_read_hist](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs__high__level__api.html#ga8e525038e353045ad6cd90607e887b0d)
- [nvs_calc_free_space](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs__high__level__api.html#ga37e5a55f0b9209c7c0c95db9e1e84715)
- [nvs_sector_max_data_size](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs__high__level__api.html#ga7ce6065cf3ac68544f51d26cabd983b2)
- [nvs_sector_use_next](https://docs.zephyrproject.org/latest/doxygen/html/group__nvs__high__level__api.html#ga52db47389e9aa2b0de77497f0e60ed5b)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [nvs_fs::flash_device](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#a02381974223dfbd22fe50b2cfecb7da2)
- [nvs_fs::ready](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#a2a167bd6a1698d2070dbe65b669ba0f4)
- [nvs_fs::flash_parameters](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#a34f769be6fed7c81254501af207147df)
- [nvs_fs::nvs_lock](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#a6f49bb17819e3b78e0b3c1a1bc578f09)
- [nvs_fs::offset](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#a793b43b069d5e7a42963d84423ab5717)
- [nvs_fs::ate_wra](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#aba5caa7709d58fa018cbb91db085f140)
- [nvs_fs::sector_count](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#abf8ffaea29e3357ca6e897902fd49a63)
- [nvs_fs::data_wra](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#ac6bc3719e803f27fc20de5ebc63d7707)
- [nvs_fs::sector_size](https://docs.zephyrproject.org/latest/doxygen/html/structnvs__fs.html#aeec2d70881591f9b85ae5bb39a064476)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P097_it51xxx-i2c.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P099_zms.h_源码浏览.md)
