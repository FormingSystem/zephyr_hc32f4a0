---
id: learning.zephyr-docs.boot-control-reference.page-3
title: MCUboot头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcuboot_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_MCUboot头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mcuboot_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P002_MCUboot头文件参考.md)和[公共API](P001_MCUboot镜像控制接口.md)。

## 3.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00097"></a>
<a id="foldopen00113"></a>
<a id="foldopen00131"></a>
<a id="agroup__mcuboot__api_html_ga03b691762d00e4cab6a5bd91979d8d80"></a>
<a id="agroup__mcuboot__api_html_ga1e679c6fefe7deaaed9a2265ce69cf1e"></a>
<a id="agroup__mcuboot__api_html_ga2eadd700521a8b94dea3d3d04c9f5bd8"></a>
<a id="agroup__mcuboot__api_html_ga4ce6857cd516204fba5f7fb5c1c6272c"></a>
<a id="agroup__mcuboot__api_html_ga652ffad55e2917c62a62f6463935fe59"></a>
<a id="agroup__mcuboot__api_html_ga6fa12d4058bbb78b7d8f35b436f0009c"></a>
<a id="agroup__mcuboot__api_html_ga7b4443f339f2935895f01dfb80c6b460"></a>
<a id="agroup__mcuboot__api_html_ga85c68e5758724d541586f8a6d61869d0"></a>
<a id="agroup__mcuboot__api_html_ga95ccc9e1c7460fec16b9ce9ac8ad7a72"></a>
<a id="agroup__mcuboot__api_html_gaa0ce517ba1c0b21c4898762fab959b12"></a>
<a id="agroup__mcuboot__api_html_gaa0f2410f520ef57e6d793c169639a6f8"></a>
<a id="agroup__mcuboot__api_html_gad47f2356938a7b5acf8e0bbe4d9e4494"></a>
<a id="agroup__mcuboot__api_html_gae9e0e43663c3671aa4b4df6d30511d39"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructmcuboot__img__header__v1_html"></a>
<a id="astructmcuboot__img__header__v1_html_a01dd3b50bb00accf4108b08c01df4e2b"></a>
<a id="astructmcuboot__img__header__v1_html_a83a042079d850f383eef7a46cad14fa4"></a>
<a id="astructmcuboot__img__header_html"></a>
<a id="astructmcuboot__img__header_html_a34f5595bbd5b974c04386b568c88e39f"></a>
<a id="astructmcuboot__img__header_html_ab5147e9586062d4dd5b381af13f1e82d"></a>
<a id="astructmcuboot__img__header_html_aff12aff412ea774f96948e7db0b25009"></a>
<a id="astructmcuboot__img__sem__ver_html"></a>
<a id="astructmcuboot__img__sem__ver_html_a3ab711b800ab894e201d175b491a9552"></a>
<a id="astructmcuboot__img__sem__ver_html_aabecc9fffb8ec7a7f02f2894f8d6e0f0"></a>
<a id="astructmcuboot__img__sem__ver_html_abf2e489560daefaa0c5d33e9c7535dab"></a>
<a id="astructmcuboot__img__sem__ver_html_ae6fa8e6cc51e57e24a2d99670e543998"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2017 Nordic Semiconductor ASA
<a id="l00003"></a> * Copyright (c) 2016 Linaro Limited
<a id="l00004"></a> *
<a id="l00005"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00006"></a> */
<a id="l00007"></a>
<a id="l00015"></a>
<a id="l00016"></a>#ifndef ZEPHYR_INCLUDE_DFU_MCUBOOT_H_
<a id="l00017"></a>#define ZEPHYR_INCLUDE_DFU_MCUBOOT_H_
<a id="l00018"></a>
<a id="l00019"></a>#include &lt;stdbool.h&gt;
<a id="l00020"></a>#include &lt;stddef.h&gt;
<a id="l00021"></a>#include &lt;sys/types.h&gt;
<a id="l00022"></a>
<a id="l00023"></a>#include &lt;zephyr/types.h&gt;
<a id="l00024"></a>
<a id="l00032"></a>
<a id="l00033"></a>#ifdef __cplusplus
<a id="l00034"></a>extern "C" {
<a id="l00035"></a>#endif
<a id="l00036"></a>
<a id="l00037"></a>#ifdef BOOT_SWAP_TYPE_NONE
<a id="l00038"></a>#if BOOT_SWAP_TYPE_NONE != 1 /*ensure the same definition in MCUboot */
<a id="l00039"></a>#error "definition incompatible"
<a id="l00040"></a>#endif
<a id="l00041"></a>#else
<a id="l00043"></a>#define BOOT_SWAP_TYPE_NONE     1
<a id="l00044"></a>#endif
<a id="l00045"></a>
<a id="l00046"></a>#ifdef BOOT_SWAP_TYPE_TEST
<a id="l00047"></a>#if BOOT_SWAP_TYPE_TEST != 2  /*ensure the same definition in MCUboot */
<a id="l00048"></a>#error "definition incompatible"
<a id="l00049"></a>#endif
<a id="l00050"></a>#else
<a id="l00052"></a>#define BOOT_SWAP_TYPE_TEST     2
<a id="l00053"></a>#endif
<a id="l00054"></a>
<a id="l00055"></a>#ifdef BOOT_SWAP_TYPE_PERM
<a id="l00056"></a>#if BOOT_SWAP_TYPE_PERM != 3  /*ensure the same definition in MCUboot */
<a id="l00057"></a>#error "definition incompatible"
<a id="l00058"></a>#endif
<a id="l00059"></a>#else
<a id="l00061"></a>#define BOOT_SWAP_TYPE_PERM     3
<a id="l00062"></a>#endif
<a id="l00063"></a>
<a id="l00064"></a>#ifdef BOOT_SWAP_TYPE_REVERT
<a id="l00065"></a>#if BOOT_SWAP_TYPE_REVERT != 4  /*ensure the same definition in MCUboot */
<a id="l00066"></a>#error "definition incompatible"
<a id="l00067"></a>#endif
<a id="l00068"></a>#else
<a id="l00070"></a>#define BOOT_SWAP_TYPE_REVERT   4
<a id="l00071"></a>#endif
<a id="l00072"></a>
<a id="l00073"></a>#ifdef BOOT_SWAP_TYPE_FAIL
<a id="l00074"></a>#if BOOT_SWAP_TYPE_FAIL != 5  /*ensure the same definition in MCUboot */
<a id="l00075"></a>#error "definition incompatible"
<a id="l00076"></a>#endif
<a id="l00077"></a>#else
<a id="l00079"></a>#define BOOT_SWAP_TYPE_FAIL     5
<a id="l00080"></a>#endif
<a id="l00081"></a>
<a id="l00082"></a>#define BOOT_IMG_VER_STRLEN_MAX 25  /* 255.255.65535.4294967295\0 */
<a id="l00083"></a>
<a id="l00085"></a>#define BOOT_INVALID_SLOT_ID 255
<a id="l00086"></a>
<a id="l00088"></a>#define SWAP_USING_OFFSET_SECTOR_UPDATE_BEGIN 1
<a id="l00089"></a>
<a id="l00097"></a>struct mcuboot_img_sem_ver {
<a id="l00098"></a>        uint8_t major;
<a id="l00099"></a>        uint8_t minor;
<a id="l00100"></a>        uint16_t revision;
<a id="l00101"></a>        uint32_t build_num;
<a id="l00102"></a>};
<a id="l00103"></a>
<a id="l00113"></a>struct mcuboot_img_header_v1 {
<a id="l00115"></a>        uint32_t image_size;
<a id="l00117"></a>        struct mcuboot_img_sem_ver sem_ver;
<a id="l00118"></a>};
<a id="l00119"></a>
<a id="l00131"></a>struct mcuboot_img_header {
<a id="l00137"></a>        uint32_t mcuboot_version;
<a id="l00143"></a>        union {
<a id="l00145"></a>                struct mcuboot_img_header_v1 v1;
<a id="l00146"></a>        } h;
<a id="l00147"></a>};
<a id="l00148"></a>
<a id="l00163"></a>int boot_read_bank_header(uint8_t area_id,
<a id="l00164"></a>                          struct mcuboot_img_header *header,
<a id="l00165"></a>                          size_t header_size);
<a id="l00166"></a>
<a id="l00172"></a>uint8_t boot_fetch_active_slot(void);
<a id="l00173"></a>
<a id="l00188"></a>bool boot_is_img_confirmed(void);
<a id="l00189"></a>
<a id="l00202"></a>int boot_write_img_confirmed(void);
<a id="l00203"></a>
<a id="l00218"></a>int boot_write_img_confirmed_multi(int image_index);
<a id="l00219"></a>
<a id="l00226"></a>int mcuboot_swap_type(void);
<a id="l00227"></a>
<a id="l00237"></a>int mcuboot_swap_type_multi(int image_index);
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00241"></a>#define BOOT_UPGRADE_TEST       0
<a id="l00242"></a>#define BOOT_UPGRADE_PERMANENT  1
<a id="l00243"></a>
<a id="l00254"></a>int boot_request_upgrade(int permanent);
<a id="l00255"></a>
<a id="l00268"></a>int boot_request_upgrade_multi(int image_index, int permanent);
<a id="l00269"></a>
<a id="l00276"></a>int boot_erase_img_bank(uint8_t area_id);
<a id="l00277"></a>
<a id="l00284"></a>ssize_t boot_get_area_trailer_status_offset(uint8_t area_id);
<a id="l00285"></a>
<a id="l00293"></a>ssize_t boot_get_trailer_status_offset(size_t area_size);
<a id="l00294"></a>
<a id="l00295"></a>#if defined(CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET) || defined(__DOXYGEN__)
<a id="l00304"></a>size_t boot_get_image_start_offset(uint8_t area_id);
<a id="l00305"></a>#else
<a id="l00306"></a>#define boot_get_image_start_offset(...) 0
<a id="l00307"></a>#endif
<a id="l00308"></a>
<a id="l00309"></a>#ifdef __cplusplus
<a id="l00310"></a>}
<a id="l00311"></a>#endif
<a id="l00312"></a>
<a id="l00316"></a>
<a id="l00317"></a>#endif  /* ZEPHYR_INCLUDE_DFU_MCUBOOT_H_ */
</code></pre>

## 3.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2017 Nordic Semiconductor ASA；Copyright (c) 2016 Linaro Limited；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. 确保与MCUboot中的同名定义一致。

3. 确保与MCUboot中的同名定义一致。

4. 确保与MCUboot中的同名定义一致。

5. 确保与MCUboot中的同名定义一致。

6. 确保与MCUboot中的同名定义一致。

7. 版本字符串容量示例：255.255.65535.4294967295及结尾空字符\0。

8. ZEPHYR_INCLUDE_DFU_MCUBOOT_H_头文件包含保护结束。

## 3.3\_原页符号提示（Symbol Descriptions）

### `boot_erase_img_bank`

```c
int boot_erase_img_bank(uint8_t area_id)
```

擦除镜像存储区。

符号定位：[boot_erase_img_bank](P001_MCUboot镜像控制接口.md#ga03b691762d00e4cab6a5bd91979d8d80)。

### `mcuboot_swap_type_multi`

```c
int mcuboot_swap_type_multi(int image_index)
```

确定 MCUboot 在下次重启时将执行的操作（如果有）。

符号定位：[mcuboot_swap_type_multi](P001_MCUboot镜像控制接口.md#ga1e679c6fefe7deaaed9a2265ce69cf1e)。

### `boot_is_img_confirmed`

```c
bool boot_is_img_confirmed(void)
```

检查当前运行的镜像是否已确认为正常（Confirmed as OK）。

符号定位：[boot_is_img_confirmed](P001_MCUboot镜像控制接口.md#ga2eadd700521a8b94dea3d3d04c9f5bd8)。

### `boot_fetch_active_slot`

```c
uint8_t boot_fetch_active_slot(void)
```

取得活动镜像槽位的 Flash 区域标识（Flash Area ID）。

符号定位：[boot_fetch_active_slot](P001_MCUboot镜像控制接口.md#ga4ce6857cd516204fba5f7fb5c1c6272c)。

### `boot_read_bank_header`

```c
int boot_read_bank_header(uint8_t area_id, struct mcuboot_img_header *header, size_t header_size)
```

从镜像存储区（Image Bank）读取 MCUboot 镜像头信息。

符号定位：[boot_read_bank_header](P001_MCUboot镜像控制接口.md#ga652ffad55e2917c62a62f6463935fe59)。

### `boot_get_area_trailer_status_offset`

```c
ssize_t boot_get_area_trailer_status_offset(uint8_t area_id)
```

取得状态信息在镜像存储区中的偏移量（Offset）。

符号定位：[boot_get_area_trailer_status_offset](P001_MCUboot镜像控制接口.md#ga6fa12d4058bbb78b7d8f35b436f0009c)。

### `boot_get_trailer_status_offset`

```c
ssize_t boot_get_trailer_status_offset(size_t area_size)
```

根据镜像存储区大小取得状态信息的偏移量。

符号定位：[boot_get_trailer_status_offset](P001_MCUboot镜像控制接口.md#ga7b4443f339f2935895f01dfb80c6b460)。

### `boot_get_image_start_offset`

```c
size_t boot_get_image_start_offset(uint8_t area_id)
```

取得镜像头偏移量；在偏移交换模式下应使用此接口，以考虑……（原符号提示在此截断）

符号定位：[boot_get_image_start_offset](P001_MCUboot镜像控制接口.md#ga85c68e5758724d541586f8a6d61869d0)。

### `boot_write_img_confirmed`

```c
int boot_write_img_confirmed(void)
```

将当前运行的镜像标记为已确认（Confirmed）。

符号定位：[boot_write_img_confirmed](P001_MCUboot镜像控制接口.md#ga95ccc9e1c7460fec16b9ce9ac8ad7a72)。

### `mcuboot_swap_type`

```c
int mcuboot_swap_type(void)
```

确定 MCUboot 在下次重启时将执行的操作（如果有）。

符号定位：[mcuboot_swap_type](P001_MCUboot镜像控制接口.md#gaa0ce517ba1c0b21c4898762fab959b12)。

### `boot_write_img_confirmed_multi`

```c
int boot_write_img_confirmed_multi(int image_index)
```

将主槽位（Primary Slot）中指定索引的镜像标记为已确认。

符号定位：[boot_write_img_confirmed_multi](P001_MCUboot镜像控制接口.md#gaa0f2410f520ef57e6d793c169639a6f8)。

### `boot_request_upgrade`

```c
int boot_request_upgrade(int permanent)
```

将槽位 1 中的镜像标记为待处理（Pending）。

符号定位：[boot_request_upgrade](P001_MCUboot镜像控制接口.md#gad47f2356938a7b5acf8e0bbe4d9e4494)。

### `boot_request_upgrade_multi`

```c
int boot_request_upgrade_multi(int image_index, int permanent)
```

将次槽位（Secondary Slot）中指定索引的镜像标记为待处理。

符号定位：[boot_request_upgrade_multi](P001_MCUboot镜像控制接口.md#gae9e0e43663c3671aa4b4df6d30511d39)。

### `types.h`

符号定位：[types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)。

### `types.h`

符号定位：[types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)。

### `ssize_t`

```c
__SIZE_TYPE__ ssize_t
```

定义位置（Definition）：types.h:28。

符号定位：[ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)。

### `stdbool.h`

符号定位：[stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `mcuboot_img_header_v1`

版本 1 的 MCUboot 镜像头模型（Image Header Model）。

定义位置（Definition）：mcuboot.h:113。

符号定位：[mcuboot_img_header_v1](P005_MCUboot版本一镜像头结构.md)。

### `mcuboot_img_header_v1::sem_ver`

```c
struct mcuboot_img_sem_ver sem_ver
```

镜像版本（Image Version）。

定义位置（Definition）：mcuboot.h:117。

符号定位：[mcuboot_img_header_v1::sem_ver](P005_MCUboot版本一镜像头结构.md#a01dd3b50bb00accf4108b08c01df4e2b)。

### `mcuboot_img_header_v1::image_size`

```c
uint32_t image_size
```

镜像大小，单位为字节（Bytes）。

定义位置（Definition）：mcuboot.h:115。

符号定位：[mcuboot_img_header_v1::image_size](P005_MCUboot版本一镜像头结构.md#a83a042079d850f383eef7a46cad14fa4)。

### `mcuboot_img_header`

MCUboot 镜像头模型。

定义位置（Definition）：mcuboot.h:131。

符号定位：[mcuboot_img_header](P006_MCUboot镜像头结构.md)。

### `mcuboot_img_header::h`

```c
union mcuboot_img_header::@205062151061022111344000230326144127133004125136 h
```

镜像头信息。

符号定位：[mcuboot_img_header::h](P006_MCUboot镜像头结构.md#a34f5595bbd5b974c04386b568c88e39f)。

### `mcuboot_img_header::mcuboot_version`

```c
uint32_t mcuboot_version
```

此镜像头面向的 MCUboot 版本。

定义位置（Definition）：mcuboot.h:137。

符号定位：[mcuboot_img_header::mcuboot_version](P006_MCUboot镜像头结构.md#ab5147e9586062d4dd5b381af13f1e82d)。

### `mcuboot_img_header::v1`

```c
struct mcuboot_img_header_v1 v1
```

MCUboot 版本 1 的镜像头信息。

定义位置（Definition）：mcuboot.h:145。

符号定位：[mcuboot_img_header::v1](P006_MCUboot镜像头结构.md#aff12aff412ea774f96948e7db0b25009)。

### `mcuboot_img_sem_ver`

MCUboot 镜像头中的镜像版本表示。

定义位置（Definition）：mcuboot.h:97。

符号定位：[mcuboot_img_sem_ver](P004_MCUboot语义版本结构.md)。

### `mcuboot_img_sem_ver::minor`

```c
uint8_t minor
```

定义位置（Definition）：mcuboot.h:99。

符号定位：[mcuboot_img_sem_ver::minor](P004_MCUboot语义版本结构.md#a3ab711b800ab894e201d175b491a9552)。

### `mcuboot_img_sem_ver::revision`

```c
uint16_t revision
```

定义位置（Definition）：mcuboot.h:100。

符号定位：[mcuboot_img_sem_ver::revision](P004_MCUboot语义版本结构.md#aabecc9fffb8ec7a7f02f2894f8d6e0f0)。

### `mcuboot_img_sem_ver::build_num`

```c
uint32_t build_num
```

定义位置（Definition）：mcuboot.h:101。

符号定位：[mcuboot_img_sem_ver::build_num](P004_MCUboot语义版本结构.md#abf2e489560daefaa0c5d33e9c7535dab)。

### `mcuboot_img_sem_ver::major`

```c
uint8_t major
```

定义位置（Definition）：mcuboot.h:98。

符号定位：[mcuboot_img_sem_ver::major](P004_MCUboot语义版本结构.md#ae6fa8e6cc51e57e24a2d99670e543998)。

## 3.4\_源码跟踪译注

> 译注——请求升级（Request Upgrade）、确认镜像（Confirm Image）与系统重启（System Reboot）是不同动作。boot_request_upgrade设置下次启动的待处理状态，没有复制固件、下载镜像或调用sys_reboot；boot_write_img_confirmed确认当前镜像，不能代替应用自身的启动健康检查。

> 译注——area_id是Flash区域标识（Flash Area ID），image_index是镜像对索引（Image Pair Index），槽位编号（Slot Number）又是另一层标识。boot_fetch_active_slot返回映射后的Flash区域ID；RAM加载模式会查询引导加载程序提供的槽位信息，查询失败或不能映射时返回BOOT_INVALID_SLOT_ID。不得把这些整数参数直接互换。

> 译注——本次boot_request_upgrade在没有FLASH_AREA_IMAGE_SECONDARY时也会返回0，此分支并没有登记待升级镜像。因此函数返回成功不能单独证明工程已配置次槽位或升级流程已经可用。应核对分区、启动模式和所选MCUboot配置。

> 译注——boot_is_img_confirmed返回布尔值；当前实现打开区域或读取状态失败也会返回false，不能仅凭false区分“尚未确认”和读取错误。没有交换魔数的初始／预烧录镜像会被视为已确认，以与确认函数保持一致。

> 译注——boot_read_bank_header解码镜像头并检查魔数、头部最小长度及调用方结构大小，当前实现仅支持版本1模型。这不是镜像签名验证，也不证明完整镜像可启动。公开结构省略了原始头中的部分字段，不能把结构内存直接当作Flash中的原始头部布局。

> 译注——偏移交换（Swap Using Offset）模式下，次槽位镜像头可能位于首个或第二个扇区。本次实现结合交换状态和扇区大小求偏移；其他模式下头文件把boot_get_image_start_offset展开为0。该接口返回size_t，当前错误分支也可能返回0，因此0不是独立的错误码。

> 译注——boot_erase_img_bank对所给Flash区域的整个fa_size调用flash_area_flatten，不只是清除镜像头。尾部状态（Trailer Status）偏移接口返回相对于镜像区域的偏移，而非CPU地址；负数结果须先处理，不能无条件转换为无符号地址。

头文件相对定位：[include/zephyr/dfu/mcuboot.h](../../../include/zephyr/dfu/mcuboot.h)，关联实现／接口：[subsys/dfu/boot/mcuboot.c](../../../subsys/dfu/boot/mcuboot.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dfu/mcuboot.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/dfu/boot/mcuboot.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P002_MCUboot头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [mcuboot_img_sem_ver](P004_MCUboot语义版本结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [major](P004_MCUboot语义版本结构.md#ae6fa8e6cc51e57e24a2d99670e543998)
- [minor](P004_MCUboot语义版本结构.md#a3ab711b800ab894e201d175b491a9552)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [revision](P004_MCUboot语义版本结构.md#aabecc9fffb8ec7a7f02f2894f8d6e0f0)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [build_num](P004_MCUboot语义版本结构.md#abf2e489560daefaa0c5d33e9c7535dab)
- [mcuboot_img_header_v1](P005_MCUboot版本一镜像头结构.md)
- [image_size](P005_MCUboot版本一镜像头结构.md#a83a042079d850f383eef7a46cad14fa4)
- [sem_ver](P005_MCUboot版本一镜像头结构.md#a01dd3b50bb00accf4108b08c01df4e2b)
- [mcuboot_img_header](P006_MCUboot镜像头结构.md)
- [mcuboot_version](P006_MCUboot镜像头结构.md#ab5147e9586062d4dd5b381af13f1e82d)
- [v1](P006_MCUboot镜像头结构.md#aff12aff412ea774f96948e7db0b25009)
- [h](P006_MCUboot镜像头结构.md#a34f5595bbd5b974c04386b568c88e39f)
- [boot_read_bank_header](P001_MCUboot镜像控制接口.md#ga652ffad55e2917c62a62f6463935fe59)
- [boot_fetch_active_slot](P001_MCUboot镜像控制接口.md#ga4ce6857cd516204fba5f7fb5c1c6272c)
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

---

[上一章](P002_MCUboot头文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_MCUboot语义版本结构.md)
