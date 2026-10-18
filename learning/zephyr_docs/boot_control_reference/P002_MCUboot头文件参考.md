---
id: learning.zephyr-docs.boot-control-reference.page-2
title: MCUboot头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcuboot_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_MCUboot头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mcuboot_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入MCUboot镜像控制、系统重启、内核版本和启动模式参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

用于控制镜像启动过程（Image Boot Process）的 MCUboot 公共 API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
#include <sys/types.h>
#include <zephyr/types.h>
```

查看此文件的源码。

用于控制镜像启动过程的 MCUboot 公共 API。此头文件声明的 API 函数可用于获取应用镜像信息，并选择用于启动的应用镜像。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_mcuboot_5Fimg_5Fsem_5Fver"></a>

```c
struct mcuboot_img_sem_ver
```

相关声明：[mcuboot_img_sem_ver](P004_MCUboot语义版本结构.md)。

MCUboot 镜像头中的镜像版本表示。

<a id="r_mcuboot_5Fimg_5Fheader_5Fv1"></a>

```c
struct mcuboot_img_header_v1
```

相关声明：[mcuboot_img_header_v1](P005_MCUboot版本一镜像头结构.md)。

版本 1 的 MCUboot 镜像头模型（Image Header Model）。

<a id="r_mcuboot_5Fimg_5Fheader"></a>

```c
struct mcuboot_img_header
```

相关声明：[mcuboot_img_header](P006_MCUboot镜像头结构.md)。

MCUboot 镜像头模型。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_gabb6482b898e8307074d8aef01b1102b7"></a>

```c
#define BOOT_SWAP_TYPE_NONE 1
```

相关声明：[BOOT_SWAP_TYPE_NONE](P001_MCUboot镜像控制接口.md#gabb6482b898e8307074d8aef01b1102b7)。

尝试启动槽位 0（Slot 0）中的内容。

<a id="r_ga3aa4415c47231a120c4cab455ea0beef"></a>

```c
#define BOOT_SWAP_TYPE_TEST 2
```

相关声明：[BOOT_SWAP_TYPE_TEST](P001_MCUboot镜像控制接口.md#ga3aa4415c47231a120c4cab455ea0beef)。

交换到槽位 1（Slot 1）。

<a id="r_ga09ebc9ba28e294e71388480bb9e4f677"></a>

```c
#define BOOT_SWAP_TYPE_PERM 3
```

相关声明：[BOOT_SWAP_TYPE_PERM](P001_MCUboot镜像控制接口.md#ga09ebc9ba28e294e71388480bb9e4f677)。

交换到槽位 1，并永久改为启动该槽位中的内容。

<a id="r_ga8ca7bd765c6ab669db0774c0b0122494"></a>

```c
#define BOOT_SWAP_TYPE_REVERT 4
```

相关声明：[BOOT_SWAP_TYPE_REVERT](P001_MCUboot镜像控制接口.md#ga8ca7bd765c6ab669db0774c0b0122494)。

交换回另一槽位（Alternate Slot）。

<a id="r_ga28cb43e6bfacdd285d95751cda80de13"></a>

```c
#define BOOT_SWAP_TYPE_FAIL 5
```

相关声明：[BOOT_SWAP_TYPE_FAIL](P001_MCUboot镜像控制接口.md#ga28cb43e6bfacdd285d95751cda80de13)。

因待运行的镜像无效而交换失败。

<a id="r_ga1e697351ff503f9a53b17916e63cce06"></a>

```c
#define BOOT_IMG_VER_STRLEN_MAX 25 /* 255.255.65535.4294967295\0 */
```

相关声明：[BOOT_IMG_VER_STRLEN_MAX](P001_MCUboot镜像控制接口.md#ga1e697351ff503f9a53b17916e63cce06)。

<a id="r_gadd593dccf6b631e3cd909a3d6e0ae8f0"></a>

```c
#define BOOT_INVALID_SLOT_ID 255
```

相关声明：[BOOT_INVALID_SLOT_ID](P001_MCUboot镜像控制接口.md#gadd593dccf6b631e3cd909a3d6e0ae8f0)。

保留值，用于表示槽位无效或无法确定槽位编号。

<a id="r_ga68aeea51973f08c06dc664f02b935ff7"></a>

```c
#define SWAP_USING_OFFSET_SECTOR_UPDATE_BEGIN 1
```

相关声明：[SWAP_USING_OFFSET_SECTOR_UPDATE_BEGIN](P001_MCUboot镜像控制接口.md#ga68aeea51973f08c06dc664f02b935ff7)。

采用偏移交换模式（Swap Using Offset Mode）时，应用应放置固件更新的扇区（Sector）。

<a id="r_ga9ed69fcd1ebf57cc356ce2bb835853f7"></a>

```c
#define BOOT_UPGRADE_TEST 0
```

相关声明：[BOOT_UPGRADE_TEST](P001_MCUboot镜像控制接口.md#ga9ed69fcd1ebf57cc356ce2bb835853f7)。

启动升级请求模式（Boot Upgrade Request Modes）。

<a id="r_gab48b79d246df6ebc712040c5ee00aa73"></a>

```c
#define BOOT_UPGRADE_PERMANENT 1
```

相关声明：[BOOT_UPGRADE_PERMANENT](P001_MCUboot镜像控制接口.md#gab48b79d246df6ebc712040c5ee00aa73)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_ga652ffad55e2917c62a62f6463935fe59"></a>

```c
int boot_read_bank_header (uint8_t area_id, struct mcuboot_img_header *header, size_t header_size)
```

相关声明：[boot_read_bank_header](P001_MCUboot镜像控制接口.md#ga652ffad55e2917c62a62f6463935fe59)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mcuboot_img_header](P006_MCUboot镜像头结构.md)。

从镜像存储区（Image Bank）读取 MCUboot 镜像头信息。

<a id="r_ga4ce6857cd516204fba5f7fb5c1c6272c"></a>

```c
uint8_t boot_fetch_active_slot (void)
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[boot_fetch_active_slot](P001_MCUboot镜像控制接口.md#ga4ce6857cd516204fba5f7fb5c1c6272c)。

取得活动镜像槽位的 Flash 区域标识（Flash Area ID）。

<a id="r_ga2eadd700521a8b94dea3d3d04c9f5bd8"></a>

```c
bool boot_is_img_confirmed (void)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[boot_is_img_confirmed](P001_MCUboot镜像控制接口.md#ga2eadd700521a8b94dea3d3d04c9f5bd8)。

检查当前运行的镜像是否已确认为正常（Confirmed as OK）。

<a id="r_ga95ccc9e1c7460fec16b9ce9ac8ad7a72"></a>

```c
int boot_write_img_confirmed (void)
```

相关声明：[boot_write_img_confirmed](P001_MCUboot镜像控制接口.md#ga95ccc9e1c7460fec16b9ce9ac8ad7a72)。

将当前运行的镜像标记为已确认（Confirmed）。

<a id="r_gaa0f2410f520ef57e6d793c169639a6f8"></a>

```c
int boot_write_img_confirmed_multi (int image_index)
```

相关声明：[boot_write_img_confirmed_multi](P001_MCUboot镜像控制接口.md#gaa0f2410f520ef57e6d793c169639a6f8)。

将主槽位（Primary Slot）中指定索引的镜像标记为已确认。

<a id="r_gaa0ce517ba1c0b21c4898762fab959b12"></a>

```c
int mcuboot_swap_type (void)
```

相关声明：[mcuboot_swap_type](P001_MCUboot镜像控制接口.md#gaa0ce517ba1c0b21c4898762fab959b12)。

确定 MCUboot 在下次重启时将执行的操作（如果有）。

<a id="r_ga1e679c6fefe7deaaed9a2265ce69cf1e"></a>

```c
int mcuboot_swap_type_multi (int image_index)
```

相关声明：[mcuboot_swap_type_multi](P001_MCUboot镜像控制接口.md#ga1e679c6fefe7deaaed9a2265ce69cf1e)。

确定 MCUboot 在下次重启时将执行的操作（如果有）。

<a id="r_gad47f2356938a7b5acf8e0bbe4d9e4494"></a>

```c
int boot_request_upgrade (int permanent)
```

相关声明：[boot_request_upgrade](P001_MCUboot镜像控制接口.md#gad47f2356938a7b5acf8e0bbe4d9e4494)。

将槽位 1 中的镜像标记为待处理（Pending）。

<a id="r_gae9e0e43663c3671aa4b4df6d30511d39"></a>

```c
int boot_request_upgrade_multi (int image_index, int permanent)
```

相关声明：[boot_request_upgrade_multi](P001_MCUboot镜像控制接口.md#gae9e0e43663c3671aa4b4df6d30511d39)。

将次槽位（Secondary Slot）中指定索引的镜像标记为待处理。

<a id="r_ga03b691762d00e4cab6a5bd91979d8d80"></a>

```c
int boot_erase_img_bank (uint8_t area_id)
```

相关声明：[boot_erase_img_bank](P001_MCUboot镜像控制接口.md#ga03b691762d00e4cab6a5bd91979d8d80)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

擦除镜像存储区。

<a id="r_ga6fa12d4058bbb78b7d8f35b436f0009c"></a>

```c
ssize_t boot_get_area_trailer_status_offset (uint8_t area_id)
```

相关声明：[ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)、[boot_get_area_trailer_status_offset](P001_MCUboot镜像控制接口.md#ga6fa12d4058bbb78b7d8f35b436f0009c)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

取得状态信息在镜像存储区中的偏移量（Offset）。

<a id="r_ga7b4443f339f2935895f01dfb80c6b460"></a>

```c
ssize_t boot_get_trailer_status_offset (size_t area_size)
```

相关声明：[ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)、[boot_get_trailer_status_offset](P001_MCUboot镜像控制接口.md#ga7b4443f339f2935895f01dfb80c6b460)。

根据镜像存储区大小取得状态信息的偏移量。

<a id="r_ga85c68e5758724d541586f8a6d61869d0"></a>

```c
size_t boot_get_image_start_offset (uint8_t area_id)
```

相关声明：[boot_get_image_start_offset](P001_MCUboot镜像控制接口.md#ga85c68e5758724d541586f8a6d61869d0)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

取得镜像头的偏移量。在偏移交换模式下应使用此接口，因为次槽位数据会根据当前状态从第一个或第二个扇区开始。

## 2.4\_源码定位与版本边界

相对源码定位：[include/zephyr/dfu/mcuboot.h](../../../include/zephyr/dfu/mcuboot.h)、[subsys/dfu/boot/mcuboot.c](../../../subsys/dfu/boot/mcuboot.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中保存摘要的官方main文件。源码定位采用相对链接；本地版本如有差异，应核对来源摘要与实际实现，不把文档核对视为固件升级或重启实测。

> 译注——源码核对：请求升级（Request Upgrade）、确认镜像（Confirm Image）与系统重启（System Reboot）是不同动作。boot_request_upgrade设置下次启动的待处理状态，没有复制固件、下载镜像或调用sys_reboot；boot_write_img_confirmed确认当前镜像，不能代替应用自身的启动健康检查。

> 译注——源码核对：area_id是Flash区域标识（Flash Area ID），image_index是镜像对索引（Image Pair Index），槽位编号（Slot Number）又是另一层标识。boot_fetch_active_slot返回映射后的Flash区域ID；RAM加载模式会查询引导加载程序提供的槽位信息，查询失败或不能映射时返回BOOT_INVALID_SLOT_ID。不得把这些整数参数直接互换。

> 译注——源码核对：本次boot_request_upgrade在没有FLASH_AREA_IMAGE_SECONDARY时也会返回0，此分支并没有登记待升级镜像。因此函数返回成功不能单独证明工程已配置次槽位或升级流程已经可用。应核对分区、启动模式和所选MCUboot配置。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h_source.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h_source.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码](P003_MCUboot头文件源码.md)
- [mcuboot_img_sem_ver](P004_MCUboot语义版本结构.md)
- [mcuboot_img_header_v1](P005_MCUboot版本一镜像头结构.md)
- [mcuboot_img_header](P006_MCUboot镜像头结构.md)
- [BOOT_SWAP_TYPE_NONE](P001_MCUboot镜像控制接口.md#gabb6482b898e8307074d8aef01b1102b7)
- [BOOT_SWAP_TYPE_TEST](P001_MCUboot镜像控制接口.md#ga3aa4415c47231a120c4cab455ea0beef)
- [BOOT_SWAP_TYPE_PERM](P001_MCUboot镜像控制接口.md#ga09ebc9ba28e294e71388480bb9e4f677)
- [BOOT_SWAP_TYPE_REVERT](P001_MCUboot镜像控制接口.md#ga8ca7bd765c6ab669db0774c0b0122494)
- [BOOT_SWAP_TYPE_FAIL](P001_MCUboot镜像控制接口.md#ga28cb43e6bfacdd285d95751cda80de13)
- [BOOT_IMG_VER_STRLEN_MAX](P001_MCUboot镜像控制接口.md#ga1e697351ff503f9a53b17916e63cce06)
- [BOOT_INVALID_SLOT_ID](P001_MCUboot镜像控制接口.md#gadd593dccf6b631e3cd909a3d6e0ae8f0)
- [SWAP_USING_OFFSET_SECTOR_UPDATE_BEGIN](P001_MCUboot镜像控制接口.md#ga68aeea51973f08c06dc664f02b935ff7)
- [BOOT_UPGRADE_TEST](P001_MCUboot镜像控制接口.md#ga9ed69fcd1ebf57cc356ce2bb835853f7)
- [BOOT_UPGRADE_PERMANENT](P001_MCUboot镜像控制接口.md#gab48b79d246df6ebc712040c5ee00aa73)
- [boot_read_bank_header](P001_MCUboot镜像控制接口.md#ga652ffad55e2917c62a62f6463935fe59)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [boot_fetch_active_slot](P001_MCUboot镜像控制接口.md#ga4ce6857cd516204fba5f7fb5c1c6272c)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [boot_is_img_confirmed](P001_MCUboot镜像控制接口.md#ga2eadd700521a8b94dea3d3d04c9f5bd8)
- [boot_write_img_confirmed](P001_MCUboot镜像控制接口.md#ga95ccc9e1c7460fec16b9ce9ac8ad7a72)
- [boot_write_img_confirmed_multi](P001_MCUboot镜像控制接口.md#gaa0f2410f520ef57e6d793c169639a6f8)
- [mcuboot_swap_type](P001_MCUboot镜像控制接口.md#gaa0ce517ba1c0b21c4898762fab959b12)
- [mcuboot_swap_type_multi](P001_MCUboot镜像控制接口.md#ga1e679c6fefe7deaaed9a2265ce69cf1e)
- [boot_request_upgrade](P001_MCUboot镜像控制接口.md#gad47f2356938a7b5acf8e0bbe4d9e4494)
- [boot_request_upgrade_multi](P001_MCUboot镜像控制接口.md#gae9e0e43663c3671aa4b4df6d30511d39)
- [boot_erase_img_bank](P001_MCUboot镜像控制接口.md#ga03b691762d00e4cab6a5bd91979d8d80)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [boot_get_area_trailer_status_offset](P001_MCUboot镜像控制接口.md#ga6fa12d4058bbb78b7d8f35b436f0009c)
- [boot_get_trailer_status_offset](P001_MCUboot镜像控制接口.md#ga7b4443f339f2935895f01dfb80c6b460)
- [boot_get_image_start_offset](P001_MCUboot镜像控制接口.md#ga85c68e5758724d541586f8a6d61869d0)

<a id="header-details"></a>

---

[上一章](P001_MCUboot镜像控制接口.md) · [返回大纲](大纲.md) · [下一章](P003_MCUboot头文件源码.md)
