---
id: learning.zephyr-docs.api-file-supplement-reference.page-98
title: zephyr__drivers__mm__rat.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第98章\_zephyr\_\_drivers\_\_mm\_\_rat.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rat_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 98.1\_数据结构（Data Structures）

<a id="r_address_5Ftrans_5Fregion_5Fconfig"></a>

```c
struct address_trans_region_config
```

相关声明：[address_trans_region_config](../driver_model_reference/P006_地址转换区域配置.md)。

区域配置结构体（Region Configuration Structure）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 98.2\_枚举（Enumerations）

<a id="r_add39d351d9d3b5e5e0b1ed6a7dd0881e"></a>

```c
enum address_trans_region_size { address_trans_region_size_1 = 0x0 , address_trans_region_size_2 , address_trans_region_size_4 , address_trans_region_size_8 , address_trans_region_size_16 , address_trans_region_size_32 , address_trans_region_size_64 , address_trans_region_size_128 , address_trans_region_size_256 , address_trans_region_size_512 , address_trans_region_size_1K , address_trans_region_size_2K , address_trans_region_size_4K , address_trans_region_size_8K , address_trans_region_size_16K , address_trans_region_size_32K , address_trans_region_size_64K , address_trans_region_size_128K , address_trans_region_size_256K , address_trans_region_size_512K , address_trans_region_size_1M , address_trans_region_size_2M , address_trans_region_size_4M , address_trans_region_size_8M , address_trans_region_size_16M , address_trans_region_size_32M , address_trans_region_size_64M , address_trans_region_size_128M , address_trans_region_size_256M , address_trans_region_size_512M , address_trans_region_size_1G , address_trans_region_size_2G , address_trans_region_size_4G }
```

相关声明：[address_trans_region_size](#add39d351d9d3b5e5e0b1ed6a7dd0881e)、[address_trans_region_size_1](#add39d351d9d3b5e5e0b1ed6a7dd0881ea8f58d582cd0c756345d5006804405df3)、[address_trans_region_size_2](#add39d351d9d3b5e5e0b1ed6a7dd0881ea04dbfa2d52dfefb293092f9e11a23113)、[address_trans_region_size_4](#add39d351d9d3b5e5e0b1ed6a7dd0881ead08d9d6124c8069651e7fa624fa9271a)、[address_trans_region_size_8](#add39d351d9d3b5e5e0b1ed6a7dd0881ead2486648f0256c8fafffc92d8d9008ae)、[address_trans_region_size_16](#add39d351d9d3b5e5e0b1ed6a7dd0881ea5700badf7a90fb967dd354ac0fc11164)、[address_trans_region_size_32](#add39d351d9d3b5e5e0b1ed6a7dd0881ea175247673aabe51988328e3baf4d7f2c)、[address_trans_region_size_64](#add39d351d9d3b5e5e0b1ed6a7dd0881ea8f7389ecd49b7263e9c33613b32ff6a5)、[address_trans_region_size_128](#add39d351d9d3b5e5e0b1ed6a7dd0881ea4b17e36f5f39f920c78e684df121abef)、[address_trans_region_size_256](#add39d351d9d3b5e5e0b1ed6a7dd0881eaf97a04aae5b62d1bf686dadf7fe5323b)、[address_trans_region_size_512](#add39d351d9d3b5e5e0b1ed6a7dd0881ea32eb15028196cf30411c597e8815e3f0)、[address_trans_region_size_1K](#add39d351d9d3b5e5e0b1ed6a7dd0881ea040a8134c953aecc21244a345df155df)、[address_trans_region_size_2K](#add39d351d9d3b5e5e0b1ed6a7dd0881eae6615e1cd2c34edb18b09d84cd8f2d63)、[address_trans_region_size_4K](#add39d351d9d3b5e5e0b1ed6a7dd0881ea83dd8600901fe070cab760e1b16c9252)、[address_trans_region_size_8K](#add39d351d9d3b5e5e0b1ed6a7dd0881ea1a5c0ad9be70669316c2f3b0bf5f2b12)、[address_trans_region_size_16K](#add39d351d9d3b5e5e0b1ed6a7dd0881ea072693f3fe262f442ff8036fe9d762d8)、[address_trans_region_size_32K](#add39d351d9d3b5e5e0b1ed6a7dd0881eadd5defe08d296c7236eb9651a79b82a4)、[address_trans_region_size_64K](#add39d351d9d3b5e5e0b1ed6a7dd0881eac866cbba7ad7848f22a6b023e983188f)、[address_trans_region_size_128K](#add39d351d9d3b5e5e0b1ed6a7dd0881ea8950584e532d0e7d5dfe84d9df9df555)、[address_trans_region_size_256K](#add39d351d9d3b5e5e0b1ed6a7dd0881ea564588b427d38b1137e73a47748f2c8a)、[address_trans_region_size_512K](#add39d351d9d3b5e5e0b1ed6a7dd0881eac4940c1e11068d9c74878b209a09acaa)、[address_trans_region_size_1M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea051f8ca6c90e483782a79baa69c24d5a)、[address_trans_region_size_2M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea5807a3fe19aba5a9ecfe472200a3fe79)、[address_trans_region_size_4M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea602aefd08974ed3b66687205f32cc2af)、[address_trans_region_size_8M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea81426462fbe9681a39a6e3d172ab6f22)、[address_trans_region_size_16M](#add39d351d9d3b5e5e0b1ed6a7dd0881eadcdcbcc90bfdd2f718bacf063d5efbf1)、[address_trans_region_size_32M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea7b851d6026a73d2ed29ae928a858a054)、[address_trans_region_size_64M](#add39d351d9d3b5e5e0b1ed6a7dd0881eabb0fb07483fd4c7da7a7a93484aebb55)、[address_trans_region_size_128M](#add39d351d9d3b5e5e0b1ed6a7dd0881eaa1fb7f23f29fa23f03435cecdcce95c2)、[address_trans_region_size_256M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea11b12b2dc0d87f01571a85e4d4d2b925)、[address_trans_region_size_512M](#add39d351d9d3b5e5e0b1ed6a7dd0881ea279d93a8260daf631aa0199469af0b53)、[address_trans_region_size_1G](#add39d351d9d3b5e5e0b1ed6a7dd0881eab293b5d29ef308e02c7920235c7f848c)、[address_trans_region_size_2G](#add39d351d9d3b5e5e0b1ed6a7dd0881ead7490f34d6aa5b45f1704ce985645fc1)、[address_trans_region_size_4G](#add39d351d9d3b5e5e0b1ed6a7dd0881ea1b125b2f8bab78b4d2a504cebed559c2)。

用于表示地址转换模块（Address Translate Module）可选区域大小（Region Sizes）的枚举（Enums）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 98.3\_函数（Functions）

<a id="r_a2a544044af8a5d05fa562ac93f707c05"></a>

```c
void sys_mm_drv_ti_rat_init (struct address_trans_region_config *region_config, uint64_t rat_base_addr, uint8_t translate_regions)
```

相关声明：[sys_mm_drv_ti_rat_init](#a2a544044af8a5d05fa562ac93f707c05)、[address_trans_region_config](../driver_model_reference/P006_地址转换区域配置.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

## 98.4\_详细说明（Detailed Documentation）

<a id="add39d351d9d3b5e5e0b1ed6a7dd0881e"></a>

### `address_trans_region_size`

```c
enum address_trans_region_size
```

用于表示地址转换模块（Address Translate Module）可选区域大小（Region Sizes）的枚举（Enums）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `address_trans_region_size_1` |  |
| `address_trans_region_size_2` |  |
| `address_trans_region_size_4` |  |
| `address_trans_region_size_8` |  |
| `address_trans_region_size_16` |  |
| `address_trans_region_size_32` |  |
| `address_trans_region_size_64` |  |
| `address_trans_region_size_128` |  |
| `address_trans_region_size_256` |  |
| `address_trans_region_size_512` |  |
| `address_trans_region_size_1K` |  |
| `address_trans_region_size_2K` |  |
| `address_trans_region_size_4K` |  |
| `address_trans_region_size_8K` |  |
| `address_trans_region_size_16K` |  |
| `address_trans_region_size_32K` |  |
| `address_trans_region_size_64K` |  |
| `address_trans_region_size_128K` |  |
| `address_trans_region_size_256K` |  |
| `address_trans_region_size_512K` |  |
| `address_trans_region_size_1M` |  |
| `address_trans_region_size_2M` |  |
| `address_trans_region_size_4M` |  |
| `address_trans_region_size_8M` |  |
| `address_trans_region_size_16M` |  |
| `address_trans_region_size_32M` |  |
| `address_trans_region_size_64M` |  |
| `address_trans_region_size_128M` |  |
| `address_trans_region_size_256M` |  |
| `address_trans_region_size_512M` |  |
| `address_trans_region_size_1G` |  |
| `address_trans_region_size_2G` |  |
| `address_trans_region_size_4G` |  |

<a id="a2a544044af8a5d05fa562ac93f707c05"></a>

### `sys_mm_drv_ti_rat_init()`

```c
void sys_mm_drv_ti_rat_init ( struct address_trans_region_config * region_config, uint64_t rat_base_addr, uint8_t translate_regions )
```


## 98.5\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P696_rat.h_源码浏览.md)
- [address_trans_region_config](../driver_model_reference/P006_地址转换区域配置.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea8f58d582cd0c756345d5006804405df3"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea04dbfa2d52dfefb293092f9e11a23113"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ead08d9d6124c8069651e7fa624fa9271a"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ead2486648f0256c8fafffc92d8d9008ae"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea5700badf7a90fb967dd354ac0fc11164"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea175247673aabe51988328e3baf4d7f2c"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea8f7389ecd49b7263e9c33613b32ff6a5"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea4b17e36f5f39f920c78e684df121abef"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881eaf97a04aae5b62d1bf686dadf7fe5323b"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea32eb15028196cf30411c597e8815e3f0"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea040a8134c953aecc21244a345df155df"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881eae6615e1cd2c34edb18b09d84cd8f2d63"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea83dd8600901fe070cab760e1b16c9252"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea1a5c0ad9be70669316c2f3b0bf5f2b12"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea072693f3fe262f442ff8036fe9d762d8"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881eadd5defe08d296c7236eb9651a79b82a4"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881eac866cbba7ad7848f22a6b023e983188f"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea8950584e532d0e7d5dfe84d9df9df555"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea564588b427d38b1137e73a47748f2c8a"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881eac4940c1e11068d9c74878b209a09acaa"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea051f8ca6c90e483782a79baa69c24d5a"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea5807a3fe19aba5a9ecfe472200a3fe79"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea602aefd08974ed3b66687205f32cc2af"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea81426462fbe9681a39a6e3d172ab6f22"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881eadcdcbcc90bfdd2f718bacf063d5efbf1"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea7b851d6026a73d2ed29ae928a858a054"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881eabb0fb07483fd4c7da7a7a93484aebb55"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881eaa1fb7f23f29fa23f03435cecdcce95c2"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea11b12b2dc0d87f01571a85e4d4d2b925"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea279d93a8260daf631aa0199469af0b53"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881eab293b5d29ef308e02c7920235c7f848c"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ead7490f34d6aa5b45f1704ce985645fc1"></a>
<a id="add39d351d9d3b5e5e0b1ed6a7dd0881ea1b125b2f8bab78b4d2a504cebed559c2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P097_zephyr__drivers__flash__ra_flash_api_extensions.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P099_zephyr__dt-bindings__clock__renesas_rza2m_clock.h_文件参考.md)
