---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-3
title: zephyr__drivers__disk.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/disk_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr__drivers__disk.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/disk_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P003_zephyr__drivers__disk.h_头文件参考.md)。

## 3.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00063"></a>
<a id="l00075"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="foldopen00100"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="foldopen00116"></a>
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
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="adlist_8h_html"></a>
<a id="agroup__disk__driver__interface_html_gaa11586a0b8ae6f2f0c142cec0df0c5fa"></a>
<a id="agroup__disk__driver__interface_html_gada802c6be65186009162a25f391dfb71"></a>
<a id="agroup__doubly-linked-list__apis_html_ga57fdb936802a617d16c00ab08cd2ad98"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdisk__info_html"></a>
<a id="astructdisk__info_html_a329a571f988718fd4737b8974d4f7ada"></a>
<a id="astructdisk__info_html_ab3413d8809d5181c671e1890a4662ba2"></a>
<a id="astructdisk__info_html_ac8ce763ca2514e4c4f4f8e0e04547ed3"></a>
<a id="astructdisk__info_html_accc0a618e4d939543f6ffc553b45e3b2"></a>
<a id="astructdisk__info_html_ae316915bd577f22dc9d353fc4b2f04bb"></a>
<a id="astructdisk__operations_html"></a>
<a id="astructdisk__operations_html_a2899499e982a861f41d02fa2e856b753"></a>
<a id="astructdisk__operations_html_a890f3f9e912b7e0b56fa105f82608f97"></a>
<a id="astructdisk__operations_html_a9fd72e76cd9bd31103a7a3d180710132"></a>
<a id="astructdisk__operations_html_acd7d82f4d65ae8badd5005ae3a21bf44"></a>
<a id="astructdisk__operations_html_ad74bec53a1ef7dc159b1ca90dd3c5a91"></a>
<a id="astructdisk__operations_html_ad944962a397c3427b4b6331518d6eb8b"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation.
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_DISK_H_
#define ZEPHYR_INCLUDE_DRIVERS_DISK_H_


#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/sys/dlist.h>

#ifdef __cplusplus
extern "C" {
#endif


#define DISK_IOCTL_GET_SECTOR_COUNT             1
#define DISK_IOCTL_GET_SECTOR_SIZE              2
#define DISK_IOCTL_RESERVED                     3
#define DISK_IOCTL_GET_ERASE_BLOCK_SZ           4
#define DISK_IOCTL_CTRL_SYNC                    5
#define DISK_IOCTL_CTRL_INIT                    6
#define DISK_IOCTL_CTRL_DEINIT                  7
#define DISK_IOCTL_GET_CARD_CID                 8


#define DISK_STATUS_OK                  0x00
#define DISK_STATUS_UNINIT              0x01
#define DISK_STATUS_NOMEDIA             0x02
#define DISK_STATUS_WR_PROTECT          0x04

struct disk_operations;

struct disk_info {
        sys_dnode_t node;
        const char *name;
        const struct disk_operations *ops;
        const struct device *dev;
        uint16_t refcnt;
};

struct disk_operations {
        int (*init)(struct disk_info *disk);
        int (*status)(struct disk_info *disk);
        int (*read)(struct disk_info *disk, uint8_t *data_buf,
                    uint32_t start_sector, uint32_t num_sector);
        int (*write)(struct disk_info *disk, const uint8_t *data_buf,
                     uint32_t start_sector, uint32_t num_sector);
        int (*erase)(struct disk_info *disk, uint32_t start_sector, uint32_t num_sector);
        int (*ioctl)(struct disk_info *disk, uint8_t cmd, void *buff);
};

int disk_access_register(struct disk_info *disk);

int disk_access_unregister(struct disk_info *disk);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_DISK_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation.。

版权（Copyright）：© 2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 153 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_DISK_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P003_zephyr__drivers__disk.h_头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/sys/dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [disk_operations](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md)
- [disk_info](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md)
- [sys_dnode_t](../dlist_reference/P001_双向链表公共接口.md#ga57fdb936802a617d16c00ab08cd2ad98)
- [node](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md#ab3413d8809d5181c671e1890a4662ba2)
- [name](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md#ac8ce763ca2514e4c4f4f8e0e04547ed3)
- [ops](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md#a329a571f988718fd4737b8974d4f7ada)
- [device](../device_reference/P002_设备对象结构.md)
- [dev](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md#ae316915bd577f22dc9d353fc4b2f04bb)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [refcnt](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md#accc0a618e4d939543f6ffc553b45e3b2)
- [init](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md#ad944962a397c3427b4b6331518d6eb8b)
- [status](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md#acd7d82f4d65ae8badd5005ae3a21bf44)
- [read](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md#a2899499e982a861f41d02fa2e856b753)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [write](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md#ad74bec53a1ef7dc159b1ca90dd3c5a91)
- [erase](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md#a9fd72e76cd9bd31103a7a3d180710132)
- [ioctl](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md#a890f3f9e912b7e0b56fa105f82608f97)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [disk_access_register](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#gaa11586a0b8ae6f2f0c142cec0df0c5fa)
- [disk_access_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__driver__interface.html#gada802c6be65186009162a25f391dfb71)
- [dlist.h](../dlist_reference/P002_双向链表头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [disk_info::ops](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md#a329a571f988718fd4737b8974d4f7ada)
- [disk_info::node](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md#ab3413d8809d5181c671e1890a4662ba2)
- [disk_info::name](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md#ac8ce763ca2514e4c4f4f8e0e04547ed3)
- [disk_info::refcnt](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md#accc0a618e4d939543f6ffc553b45e3b2)
- [disk_info::dev](../peripheral_bus_storage_model_reference/P004_disk_info_结构体.md#ae316915bd577f22dc9d353fc4b2f04bb)
- [disk_operations::read](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md#a2899499e982a861f41d02fa2e856b753)
- [disk_operations::ioctl](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md#a890f3f9e912b7e0b56fa105f82608f97)
- [disk_operations::erase](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md#a9fd72e76cd9bd31103a7a3d180710132)
- [disk_operations::status](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md#acd7d82f4d65ae8badd5005ae3a21bf44)
- [disk_operations::write](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md#ad74bec53a1ef7dc159b1ca90dd3c5a91)
- [disk_operations::init](../peripheral_bus_storage_model_reference/P005_disk_operations_结构体.md#ad944962a397c3427b4b6331518d6eb8b)

---

[上一章](P002_zephyr__drivers__misc__devmux__devmux.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__drivers__espi.h_头文件源码.md)
