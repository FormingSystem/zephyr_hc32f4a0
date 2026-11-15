---
id: learning.zephyr-docs.api-source-reference.page-696
title: rat.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rat_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第696章\_rat.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html)。

## 696.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="foldopen00020"></a>
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
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
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
<a id="arat_8h_html_a2a544044af8a5d05fa562ac93f707c05"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881e"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea040a8134c953aecc21244a345df155df"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea04dbfa2d52dfefb293092f9e11a23113"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea051f8ca6c90e483782a79baa69c24d5a"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea072693f3fe262f442ff8036fe9d762d8"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea11b12b2dc0d87f01571a85e4d4d2b925"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea175247673aabe51988328e3baf4d7f2c"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea1a5c0ad9be70669316c2f3b0bf5f2b12"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea1b125b2f8bab78b4d2a504cebed559c2"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea279d93a8260daf631aa0199469af0b53"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea32eb15028196cf30411c597e8815e3f0"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea4b17e36f5f39f920c78e684df121abef"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea564588b427d38b1137e73a47748f2c8a"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea5700badf7a90fb967dd354ac0fc11164"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea5807a3fe19aba5a9ecfe472200a3fe79"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea602aefd08974ed3b66687205f32cc2af"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea7b851d6026a73d2ed29ae928a858a054"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea81426462fbe9681a39a6e3d172ab6f22"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea83dd8600901fe070cab760e1b16c9252"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea8950584e532d0e7d5dfe84d9df9df555"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea8f58d582cd0c756345d5006804405df3"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ea8f7389ecd49b7263e9c33613b32ff6a5"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881eaa1fb7f23f29fa23f03435cecdcce95c2"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881eab293b5d29ef308e02c7920235c7f848c"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881eabb0fb07483fd4c7da7a7a93484aebb55"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881eac4940c1e11068d9c74878b209a09acaa"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881eac866cbba7ad7848f22a6b023e983188f"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ead08d9d6124c8069651e7fa624fa9271a"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ead2486648f0256c8fafffc92d8d9008ae"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881ead7490f34d6aa5b45f1704ce985645fc1"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881eadcdcbcc90bfdd2f718bacf063d5efbf1"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881eadd5defe08d296c7236eb9651a79b82a4"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881eae6615e1cd2c34edb18b09d84cd8f2d63"></a>
<a id="arat_8h_html_add39d351d9d3b5e5e0b1ed6a7dd0881eaf97a04aae5b62d1bf686dadf7fe5323b"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructaddress__trans__region__config_html"></a>
<a id="astructaddress__trans__region__config_html_a0cae76338ca84e5de894f2def9272ddd"></a>
<a id="astructaddress__trans__region__config_html_ab5ad2baec37c5949f099ff9e32016cc5"></a>
<a id="astructaddress__trans__region__config_html_ae58869e0b4be0e52d9a39d4a29733843"></a>

```c
/*
 * Copyright (c) 2023 Texas Instruments Incorporated
 * Copyright (c) 2023 L Lakshmanan
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_MM_RAT_H_
#define ZEPHYR_INCLUDE_DRIVERS_MM_RAT_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

enum address_trans_region_size {
        address_trans_region_size_1 = 0x0,
        address_trans_region_size_2,
        address_trans_region_size_4,
        address_trans_region_size_8,
        address_trans_region_size_16,
        address_trans_region_size_32,
        address_trans_region_size_64,
        address_trans_region_size_128,
        address_trans_region_size_256,
        address_trans_region_size_512,
        address_trans_region_size_1K,
        address_trans_region_size_2K,
        address_trans_region_size_4K,
        address_trans_region_size_8K,
        address_trans_region_size_16K,
        address_trans_region_size_32K,
        address_trans_region_size_64K,
        address_trans_region_size_128K,
        address_trans_region_size_256K,
        address_trans_region_size_512K,
        address_trans_region_size_1M,
        address_trans_region_size_2M,
        address_trans_region_size_4M,
        address_trans_region_size_8M,
        address_trans_region_size_16M,
        address_trans_region_size_32M,
        address_trans_region_size_64M,
        address_trans_region_size_128M,
        address_trans_region_size_256M,
        address_trans_region_size_512M,
        address_trans_region_size_1G,
        address_trans_region_size_2G,
        address_trans_region_size_4G
};

struct address_trans_region_config {
        uint64_t system_addr;
        uint32_t local_addr;
        uint32_t size;
};

void sys_mm_drv_ti_rat_init(struct address_trans_region_config *region_config,
                            uint64_t rat_base_addr, uint8_t translate_regions);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MM_RAT_H_ */
```

## 696.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Texas Instruments Incorporated。

版权（Copyright）：© 2023 L Lakshmanan。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 72 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MM_RAT_H_`。

## 696.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [address_trans_region_size](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881e)
- [address_trans_region_size_1](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea8f58d582cd0c756345d5006804405df3)
- [address_trans_region_size_2](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea04dbfa2d52dfefb293092f9e11a23113)
- [address_trans_region_size_4](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ead08d9d6124c8069651e7fa624fa9271a)
- [address_trans_region_size_8](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ead2486648f0256c8fafffc92d8d9008ae)
- [address_trans_region_size_16](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea5700badf7a90fb967dd354ac0fc11164)
- [address_trans_region_size_32](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea175247673aabe51988328e3baf4d7f2c)
- [address_trans_region_size_64](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea8f7389ecd49b7263e9c33613b32ff6a5)
- [address_trans_region_size_128](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea4b17e36f5f39f920c78e684df121abef)
- [address_trans_region_size_256](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881eaf97a04aae5b62d1bf686dadf7fe5323b)
- [address_trans_region_size_512](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea32eb15028196cf30411c597e8815e3f0)
- [address_trans_region_size_1K](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea040a8134c953aecc21244a345df155df)
- [address_trans_region_size_2K](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881eae6615e1cd2c34edb18b09d84cd8f2d63)
- [address_trans_region_size_4K](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea83dd8600901fe070cab760e1b16c9252)
- [address_trans_region_size_8K](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea1a5c0ad9be70669316c2f3b0bf5f2b12)
- [address_trans_region_size_16K](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea072693f3fe262f442ff8036fe9d762d8)
- [address_trans_region_size_32K](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881eadd5defe08d296c7236eb9651a79b82a4)
- [address_trans_region_size_64K](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881eac866cbba7ad7848f22a6b023e983188f)
- [address_trans_region_size_128K](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea8950584e532d0e7d5dfe84d9df9df555)
- [address_trans_region_size_256K](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea564588b427d38b1137e73a47748f2c8a)
- [address_trans_region_size_512K](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881eac4940c1e11068d9c74878b209a09acaa)
- [address_trans_region_size_1M](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea051f8ca6c90e483782a79baa69c24d5a)
- [address_trans_region_size_2M](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea5807a3fe19aba5a9ecfe472200a3fe79)
- [address_trans_region_size_4M](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea602aefd08974ed3b66687205f32cc2af)
- [address_trans_region_size_8M](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea81426462fbe9681a39a6e3d172ab6f22)
- [address_trans_region_size_16M](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881eadcdcbcc90bfdd2f718bacf063d5efbf1)
- [address_trans_region_size_32M](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea7b851d6026a73d2ed29ae928a858a054)
- [address_trans_region_size_64M](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881eabb0fb07483fd4c7da7a7a93484aebb55)
- [address_trans_region_size_128M](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881eaa1fb7f23f29fa23f03435cecdcce95c2)
- [address_trans_region_size_256M](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea11b12b2dc0d87f01571a85e4d4d2b925)
- [address_trans_region_size_512M](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea279d93a8260daf631aa0199469af0b53)
- [address_trans_region_size_1G](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881eab293b5d29ef308e02c7920235c7f848c)
- [address_trans_region_size_2G](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ead7490f34d6aa5b45f1704ce985645fc1)
- [address_trans_region_size_4G](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#add39d351d9d3b5e5e0b1ed6a7dd0881ea1b125b2f8bab78b4d2a504cebed559c2)
- [address_trans_region_config](../driver_model_reference/P006_地址转换区域配置.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [system_addr](../driver_model_reference/P006_地址转换区域配置.md#ab5ad2baec37c5949f099ff9e32016cc5)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [local_addr](../driver_model_reference/P006_地址转换区域配置.md#ae58869e0b4be0e52d9a39d4a29733843)
- [size](../driver_model_reference/P006_地址转换区域配置.md#a0cae76338ca84e5de894f2def9272ddd)
- [sys_mm_drv_ti_rat_init](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html#a2a544044af8a5d05fa562ac93f707c05)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [address_trans_region_config::size](../driver_model_reference/P006_地址转换区域配置.md#a0cae76338ca84e5de894f2def9272ddd)
- [address_trans_region_config::system_addr](../driver_model_reference/P006_地址转换区域配置.md#ab5ad2baec37c5949f099ff9e32016cc5)
- [address_trans_region_config::local_addr](../driver_model_reference/P006_地址转换区域配置.md#ae58869e0b4be0e52d9a39d4a29733843)

---

[上一章](P695_raspberrypi-csi-connector.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P697_realtek-bee-gpio.h_源码浏览.md)
