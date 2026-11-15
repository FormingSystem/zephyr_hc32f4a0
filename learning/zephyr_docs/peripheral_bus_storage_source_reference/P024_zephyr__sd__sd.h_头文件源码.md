---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-24
title: zephyr__sd__sd.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sd_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr__sd__sd.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sd_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md)。

## 24.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="foldopen00026"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00063"></a>
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
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__sdhc__interface_html_ga34041edf280f125b8500809226b3de5d"></a>
<a id="agroup__sys-util_html_gafa99ec4acc4ecb2dc3c2d05da15d0e3f"></a>
<a id="akernel_8h_html"></a>
<a id="asd_8h_html_a52167aac735d93085a5eebc6f50e1bba"></a>
<a id="asd_8h_html_a52167aac735d93085a5eebc6f50e1bbaa5458e6fab05f8c1afbe7d191eb489e5e"></a>
<a id="asd_8h_html_a52167aac735d93085a5eebc6f50e1bbaa839d17bb0bee41a125a617683bce17c9"></a>
<a id="asd_8h_html_a52167aac735d93085a5eebc6f50e1bbaaa059e919850b36b85ebe33a07050e453"></a>
<a id="asd_8h_html_ac02b6fe46112b8b891e9713ef24bd131"></a>
<a id="asd_8h_html_aed46c9c492c5c6434a6ae4d6151ac7d3"></a>
<a id="asd_8h_html_aee707e2ff5691dbdefd9341a18de7b14"></a>
<a id="asd_8h_html_aee707e2ff5691dbdefd9341a18de7b14a5afc0338b5a0541bb34f1a5b67139b6b"></a>
<a id="asd_8h_html_aee707e2ff5691dbdefd9341a18de7b14a868625c31f4384780de3992d78b93345"></a>
<a id="asd_8h_html_aee707e2ff5691dbdefd9341a18de7b14a8b26749346e26d9257cd53c48a68eda4"></a>
<a id="asd_8h_html_aee707e2ff5691dbdefd9341a18de7b14ad527710e81e76e0938689015c2013090"></a>
<a id="asd__spec_8h_html_a3a542344967c5c1912bde216559e7cd6"></a>
<a id="asdhc_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructsd__card_html"></a>
<a id="astructsd__card_html_a03d7be3154dcd881df60921681a4f308"></a>
<a id="astructsd__card_html_a03eac55046f7222c97d60fa919e3cae9"></a>
<a id="astructsd__card_html_a17a021db8aa3a8ad224e422f3854eafc"></a>
<a id="astructsd__card_html_a1db9545598f0eb6b6440e63d4941d2ab"></a>
<a id="astructsd__card_html_a38383b8f5c1f9bff1537f407fbec9faf"></a>
<a id="astructsd__card_html_a3d29b73f029af5182475c2a2d365173b"></a>
<a id="astructsd__card_html_a5a9a627df5daf23b468ce705bf5f5f81"></a>
<a id="astructsd__card_html_a798acb1bb9495d1009a23f139d269108"></a>
<a id="astructsd__card_html_a81c9ec36c79e77599c10163455c86e7c"></a>
<a id="astructsd__card_html_a856e7ea75577c62be17dc5d8c99908f4"></a>
<a id="astructsd__card_html_a875b7081a3e647b782cdb835372f5029"></a>
<a id="astructsd__card_html_a8beccfe60fc714c159528fbd2c122b16"></a>
<a id="astructsd__card_html_a93986ee5db729d9931b4ababe41c303a"></a>
<a id="astructsd__card_html_a9f597007072d3af5b70ea5cc2a4cbd29"></a>
<a id="astructsd__card_html_ab122e442ab3ba5078c99a98a861ec908"></a>
<a id="astructsd__card_html_aba2501397066d0930691c40778405aa7"></a>
<a id="astructsd__card_html_acdcfdaab67d284ef3a8ee3202fd7a538"></a>
<a id="astructsd__card_html_ad5d6e798ae8b04d829fb8131f6cb1ccf"></a>
<a id="astructsd__card_html_ae8e85d2fc44a97b42247d87a5c2aafdf"></a>
<a id="astructsd__card_html_afabeaa207f2f5caaec8cfedac6b35661"></a>
<a id="astructsd__switch__caps_html"></a>
<a id="astructsdhc__host__props_html"></a>
<a id="astructsdhc__io_html"></a>
<a id="astructsdio__cis_html"></a>
<a id="astructsdio__func_html"></a>
<a id="astructsdio__func_html_a3bc320f1ca7268344b848a998ace615c"></a>
<a id="astructsdio__func_html_a7387979362ba892c013a7a69e004d96b"></a>
<a id="astructsdio__func_html_aa4ad13eb77f656020b38f6cf165e2965"></a>
<a id="astructsdio__func_html_af83e71e628841b8acf70130261a97060"></a>

```c
/*
 * Copyright 2022 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SD_SD_H_
#define ZEPHYR_INCLUDE_SD_SD_H_

#include <zephyr/device.h>
#include <zephyr/drivers/sdhc.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif

enum card_status {
        CARD_UNINITIALIZED = 0,
        CARD_ERROR = 1,
        CARD_INITIALIZED = 2,
};

enum card_type {
        CARD_SDMMC = 0,
        CARD_SDIO = 1,
        CARD_COMBO = 2,
        CARD_MMC = 3,
};

struct sdio_func {
        enum sdio_func_num num;
        struct sd_card *card;
        struct sdio_cis cis;
        uint16_t block_size;
};


struct sd_card {
        const struct device *sdhc;
        struct sdhc_io bus_io;
        enum sd_voltage card_voltage;
        struct k_mutex lock;
        struct sdhc_host_props host_props;
        uint32_t ocr;
        struct sd_switch_caps switch_caps;
        unsigned int num_io: 3;
        uint16_t relative_addr;
        uint32_t block_count;
        uint16_t block_size;
        uint8_t sd_version;
        uint8_t card_speed;
        enum card_status status;
        enum card_type type;
        uint16_t flags;
        uint8_t bus_width;
        uint32_t cccr_flags;
        struct sdio_func func0;

        /* NOTE: The buffer is accessed as a uint32_t* by the SD subsystem, so must be
         * aligned to 4 bytes for platforms that don't support unaligned access...
         * Systems where the buffer is accessed by DMA may require wider alignment, in
         * which case, use CONFIG_SDHC_BUFFER_ALIGNMENT.
         */
        uint8_t card_buffer[CONFIG_SD_BUFFER_SIZE]
                __aligned(MAX(4, CONFIG_SDHC_BUFFER_ALIGNMENT)); /* Card internal buffer */
};

int sd_init(const struct device *sdhc_dev, struct sd_card *card);

bool sd_is_card_present(const struct device *sdhc_dev);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SD_SD_H_ */
```

## 24.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 84 行

注意：SD 子系统通过 `uint32_t*` 访问此缓冲区，因此，对于不支持非对齐访问（Unaligned access）的平台，缓冲区必须按 4 字节对齐。通过 DMA 访问缓冲区的系统可能需要更大的对齐边界；此时应使用 `CONFIG_SDHC_BUFFER_ALIGNMENT`。

### 注释 3：原第 90 行

卡内部缓冲区（Card internal buffer）。

### 注释 4：原第 121 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SD_SD_H_`。

## 24.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/sdhc.h](../peripheral_bus_storage_header_reference/P025_zephyr__drivers__sdhc.h_头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [card_status](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md#a52167aac735d93085a5eebc6f50e1bba)
- [CARD_UNINITIALIZED](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md#a52167aac735d93085a5eebc6f50e1bbaaa059e919850b36b85ebe33a07050e453)
- [CARD_ERROR](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md#a52167aac735d93085a5eebc6f50e1bbaa5458e6fab05f8c1afbe7d191eb489e5e)
- [CARD_INITIALIZED](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md#a52167aac735d93085a5eebc6f50e1bbaa839d17bb0bee41a125a617683bce17c9)
- [card_type](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md#aee707e2ff5691dbdefd9341a18de7b14)
- [CARD_SDMMC](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md#aee707e2ff5691dbdefd9341a18de7b14a8b26749346e26d9257cd53c48a68eda4)
- [CARD_SDIO](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md#aee707e2ff5691dbdefd9341a18de7b14a5afc0338b5a0541bb34f1a5b67139b6b)
- [CARD_COMBO](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md#aee707e2ff5691dbdefd9341a18de7b14ad527710e81e76e0938689015c2013090)
- [CARD_MMC](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md#aee707e2ff5691dbdefd9341a18de7b14a868625c31f4384780de3992d78b93345)
- [sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)
- [sdio_func_num](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6)
- [num](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md#a3bc320f1ca7268344b848a998ace615c)
- [sd_card](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md)
- [card](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md#a7387979362ba892c013a7a69e004d96b)
- [sdio_cis](../peripheral_bus_storage_model_reference/P085_sdio_cis_结构体.md)
- [cis](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md#af83e71e628841b8acf70130261a97060)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [block_size](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md#aa4ad13eb77f656020b38f6cf165e2965)
- [device](../device_reference/P002_设备对象结构.md)
- [sdhc](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#afabeaa207f2f5caaec8cfedac6b35661)
- [sdhc_io](../peripheral_bus_storage_model_reference/P084_sdhc_io_结构体.md)
- [bus_io](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a875b7081a3e647b782cdb835372f5029)
- [sd_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga34041edf280f125b8500809226b3de5d)
- [card_voltage](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#ae8e85d2fc44a97b42247d87a5c2aafdf)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [lock](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#aba2501397066d0930691c40778405aa7)
- [sdhc_host_props](../peripheral_bus_storage_model_reference/P083_sdhc_host_props_结构体.md)
- [host_props](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a9f597007072d3af5b70ea5cc2a4cbd29)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [ocr](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a856e7ea75577c62be17dc5d8c99908f4)
- [sd_switch_caps](../peripheral_bus_storage_model_reference/P078_sd_switch_caps_结构体.md)
- [switch_caps](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a03eac55046f7222c97d60fa919e3cae9)
- [num_io](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a17a021db8aa3a8ad224e422f3854eafc)
- [relative_addr](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a1db9545598f0eb6b6440e63d4941d2ab)
- [block_count](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#acdcfdaab67d284ef3a8ee3202fd7a538)
- [block_size](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a3d29b73f029af5182475c2a2d365173b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sd_version](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a5a9a627df5daf23b468ce705bf5f5f81)
- [card_speed](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a8beccfe60fc714c159528fbd2c122b16)
- [status](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a03d7be3154dcd881df60921681a4f308)
- [type](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a798acb1bb9495d1009a23f139d269108)
- [flags](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#ad5d6e798ae8b04d829fb8131f6cb1ccf)
- [bus_width](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a38383b8f5c1f9bff1537f407fbec9faf)
- [cccr_flags](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#ab122e442ab3ba5078c99a98a861ec908)
- [func0](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a93986ee5db729d9931b4ababe41c303a)
- [card_buffer](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a81c9ec36c79e77599c10163455c86e7c)
- [MAX](../util_reference/P001_通用工具公共接口.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)
- [sd_init](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md#ac02b6fe46112b8b891e9713ef24bd131)
- [sd_is_card_present](../peripheral_bus_storage_header_reference/P024_zephyr__sd__sd.h_头文件参考.md#aed46c9c492c5c6434a6ae4d6151ac7d3)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [sdhc.h](../peripheral_bus_storage_header_reference/P025_zephyr__drivers__sdhc.h_头文件参考.md)
- [sd_card::status](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a03d7be3154dcd881df60921681a4f308)
- [sd_card::switch_caps](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a03eac55046f7222c97d60fa919e3cae9)
- [sd_card::num_io](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a17a021db8aa3a8ad224e422f3854eafc)
- [sd_card::relative_addr](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a1db9545598f0eb6b6440e63d4941d2ab)
- [sd_card::bus_width](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a38383b8f5c1f9bff1537f407fbec9faf)
- [sd_card::block_size](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a3d29b73f029af5182475c2a2d365173b)
- [sd_card::sd_version](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a5a9a627df5daf23b468ce705bf5f5f81)
- [sd_card::type](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a798acb1bb9495d1009a23f139d269108)
- [sd_card::card_buffer](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a81c9ec36c79e77599c10163455c86e7c)
- [sd_card::ocr](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a856e7ea75577c62be17dc5d8c99908f4)
- [sd_card::bus_io](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a875b7081a3e647b782cdb835372f5029)
- [sd_card::card_speed](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a8beccfe60fc714c159528fbd2c122b16)
- [sd_card::func0](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a93986ee5db729d9931b4ababe41c303a)
- [sd_card::host_props](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#a9f597007072d3af5b70ea5cc2a4cbd29)
- [sd_card::cccr_flags](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#ab122e442ab3ba5078c99a98a861ec908)
- [sd_card::lock](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#aba2501397066d0930691c40778405aa7)
- [sd_card::block_count](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#acdcfdaab67d284ef3a8ee3202fd7a538)
- [sd_card::flags](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#ad5d6e798ae8b04d829fb8131f6cb1ccf)
- [sd_card::card_voltage](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#ae8e85d2fc44a97b42247d87a5c2aafdf)
- [sd_card::sdhc](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md#afabeaa207f2f5caaec8cfedac6b35661)
- [sdio_func::num](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md#a3bc320f1ca7268344b848a998ace615c)
- [sdio_func::card](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md#a7387979362ba892c013a7a69e004d96b)
- [sdio_func::block_size](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md#aa4ad13eb77f656020b38f6cf165e2965)
- [sdio_func::cis](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md#af83e71e628841b8acf70130261a97060)

---

[上一章](P023_zephyr__drivers__psi5__psi5.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__drivers__sdhc.h_头文件源码.md)
