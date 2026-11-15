---
id: learning.zephyr-docs.api-file-service-interface-reference.page-50
title: zephyr__drivers__mfd__tla2528.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tla2528_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_zephyr\_\_drivers\_\_mfd\_\_tla2528.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tla2528_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TLA2528多功能设备（MFD）驱动的头文件。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/sys/mutex.h>
#include <zephyr/sys/util_macro.h>
#include <stdint.h>
```

查看此文件的源码。

TLA2528多功能设备（MFD）驱动的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 50.1\_枚举（Enumerations）

<a id="r_gae9ef53f1a7533dcce0125a0f81e3d2f9"></a>

```c
enum tla2528_reg { TLA2528_SYSTEM_STATUS = 0x0 , TLA2528_GENERAL_CFG = 0x1 , TLA2528_DATA_CFG = 0x2 , TLA2528_OSR_CFG = 0x3 , TLA2528_OPMODE_CFG = 0x4 , TLA2528_PIN_CFG = 0x5 , TLA2528_GPIO_CFG = 0x7 , TLA2528_GPO_DRIVE_CFG = 0x9 , TLA2528_GPO_VALUE = 0xb , TLA2528_GPI_VALUE = 0xd , TLA2528_SEQUENCE_CFG = 0x10 , TLA2528_CHANNEL_SEL = 0x11 , TLA2528_AUTO_SEQ_CH_SEL = 0x12 }
```

相关声明：[tla2528_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gae9ef53f1a7533dcce0125a0f81e3d2f9)、[TLA2528_SYSTEM_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a698cea620265b7a897caa24931da6d73)、[TLA2528_GENERAL_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a2822fdf57a7ae72ca67ce1bd038d7beb)、[TLA2528_DATA_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9aa3feb424e3b88176f9ec57c1e06891bc)、[TLA2528_OSR_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9ac07d4692c36eb4031122425a456bf319)、[TLA2528_OPMODE_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a91acfd4efd27094fcfb916feccc4b015)、[TLA2528_PIN_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9ad10b98f7287caa3740ec0484486f4279)、[TLA2528_GPIO_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a89a004cea9236921bcfea27c06aeaf97)、[TLA2528_GPO_DRIVE_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a48cb070073272a65483e143cb6cd8272)、[TLA2528_GPO_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a4e7b693eb7e3da74e959f17e830bc6c6)、[TLA2528_GPI_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a014b2bd57485c9e584b246fbed5de08d)、[TLA2528_SEQUENCE_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a6f088dfa8d06cf8a96a8193dcf1bf9ff)、[TLA2528_CHANNEL_SEL](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a24b8cd6ae27a07c61b2be03077d89e60)、[TLA2528_AUTO_SEQ_CH_SEL](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a6f1a9f0518122ccd3a00ed536d98e2f3)。

TLA2528 寄存器映射（Register Mapping）。

<a id="r_ga73edc358e1817027d25c3d199d544080"></a>

```c
enum tla2528_general_cfg { TLA2528_CNVST = BIT(3) , TLA2528_CH_RST = BIT(2) , TLA2528_CAL = BIT(1) , TLA2528_RST = BIT(0) }
```

相关声明：[tla2528_general_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ga73edc358e1817027d25c3d199d544080)、[TLA2528_CNVST](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gga73edc358e1817027d25c3d199d544080a11bca954934aea902a80ac4b64feb074)、[TLA2528_CH_RST](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gga73edc358e1817027d25c3d199d544080a011bdd0a4e78c7828034aac791b8b9c6)、[TLA2528_CAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gga73edc358e1817027d25c3d199d544080a5adafc7f3aeea41172dd96044a6e35b6)、[TLA2528_RST](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gga73edc358e1817027d25c3d199d544080ac3003bc8d725922136668beaeb32e702)。

TLA2528 的 `GENERAL_CFG` 寄存器位映射（Bit Mapping）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 50.2\_函数（Functions）

<a id="r_ga0d998ab336bf29c30628caaa48fe5d5e"></a>

```c
int tla2528_register_write (const struct device *dev, enum tla2528_reg reg, uint8_t data)
```

相关声明：[tla2528_register_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ga0d998ab336bf29c30628caaa48fe5d5e)、[device](../device_reference/P002_设备对象结构.md)、[tla2528_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gae9ef53f1a7533dcce0125a0f81e3d2f9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 TLA2528 的指定寄存器（Register）。

<a id="r_gaa36c93d66658ab5c93eb081173365ef9"></a>

```c
int tla2528_register_read (const struct device *dev, enum tla2528_reg reg, uint8_t *data)
```

相关声明：[tla2528_register_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gaa36c93d66658ab5c93eb081173365ef9)、[device](../device_reference/P002_设备对象结构.md)、[tla2528_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gae9ef53f1a7533dcce0125a0f81e3d2f9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 TLA2528 的指定寄存器（Register）。

<a id="r_ga55308097dd5342c3185da1fd2470bbd6"></a>

```c
int tla2528_register_set_bits (const struct device *dev, enum tla2528_reg reg, uint8_t bits)
```

相关声明：[tla2528_register_set_bits](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ga55308097dd5342c3185da1fd2470bbd6)、[device](../device_reference/P002_设备对象结构.md)、[tla2528_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gae9ef53f1a7533dcce0125a0f81e3d2f9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 TLA2528 寄存器中的指定位（Bits）置位。

<a id="r_ga12fd943038f1f0e80335795cb3e7ad2f"></a>

```c
int tla2528_register_clear_bits (const struct device *dev, enum tla2528_reg reg, uint8_t bits)
```

相关声明：[tla2528_register_clear_bits](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ga12fd943038f1f0e80335795cb3e7ad2f)、[device](../device_reference/P002_设备对象结构.md)、[tla2528_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gae9ef53f1a7533dcce0125a0f81e3d2f9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 TLA2528 寄存器中的指定位（Bits）清零。

<a id="r_ga8791c5e15519904399d15d9e82b4388b"></a>

```c
int tla2528_read_adc_data (const struct device *dev, uint16_t *data)
```

相关声明：[tla2528_read_adc_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ga8791c5e15519904399d15d9e82b4388b)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从 TLA2528 读取一个模数转换器（ADC）数据样本。

<a id="r_ga9b02417b0ef92c150f6dc55afe27cdb2"></a>

```c
struct k_mutex * tla2528_get_lock (const struct device *dev)
```

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[tla2528_get_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ga9b02417b0ef92c150f6dc55afe27cdb2)、[device](../device_reference/P002_设备对象结构.md)。

获取 TLA2528 的互斥锁（Mutex Lock）。


## 50.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/mutex.h](../userspace_sync_reference/P006_用户模式互斥量头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P868_tla2528.h_源码浏览.md)
- [tla2528_reg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gae9ef53f1a7533dcce0125a0f81e3d2f9)
- [TLA2528_SYSTEM_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a698cea620265b7a897caa24931da6d73)
- [TLA2528_GENERAL_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a2822fdf57a7ae72ca67ce1bd038d7beb)
- [TLA2528_DATA_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9aa3feb424e3b88176f9ec57c1e06891bc)
- [TLA2528_OSR_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9ac07d4692c36eb4031122425a456bf319)
- [TLA2528_OPMODE_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a91acfd4efd27094fcfb916feccc4b015)
- [TLA2528_PIN_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9ad10b98f7287caa3740ec0484486f4279)
- [TLA2528_GPIO_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a89a004cea9236921bcfea27c06aeaf97)
- [TLA2528_GPO_DRIVE_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a48cb070073272a65483e143cb6cd8272)
- [TLA2528_GPO_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a4e7b693eb7e3da74e959f17e830bc6c6)
- [TLA2528_GPI_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a014b2bd57485c9e584b246fbed5de08d)
- [TLA2528_SEQUENCE_CFG](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a6f088dfa8d06cf8a96a8193dcf1bf9ff)
- [TLA2528_CHANNEL_SEL](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a24b8cd6ae27a07c61b2be03077d89e60)
- [TLA2528_AUTO_SEQ_CH_SEL](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ggae9ef53f1a7533dcce0125a0f81e3d2f9a6f1a9f0518122ccd3a00ed536d98e2f3)
- [tla2528_general_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ga73edc358e1817027d25c3d199d544080)
- [TLA2528_CNVST](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gga73edc358e1817027d25c3d199d544080a11bca954934aea902a80ac4b64feb074)
- [TLA2528_CH_RST](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gga73edc358e1817027d25c3d199d544080a011bdd0a4e78c7828034aac791b8b9c6)
- [TLA2528_CAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gga73edc358e1817027d25c3d199d544080a5adafc7f3aeea41172dd96044a6e35b6)
- [TLA2528_RST](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gga73edc358e1817027d25c3d199d544080ac3003bc8d725922136668beaeb32e702)
- [tla2528_register_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ga0d998ab336bf29c30628caaa48fe5d5e)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [tla2528_register_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#gaa36c93d66658ab5c93eb081173365ef9)
- [tla2528_register_set_bits](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ga55308097dd5342c3185da1fd2470bbd6)
- [tla2528_register_clear_bits](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ga12fd943038f1f0e80335795cb3e7ad2f)
- [tla2528_read_adc_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ga8791c5e15519904399d15d9e82b4388b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [tla2528_get_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__tla2528.html#ga9b02417b0ef92c150f6dc55afe27cdb2)

<a id="header-details"></a>

---

[上一章](P049_zephyr__sys__sys_getopt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P051_zephyr__net__tls_credentials.h_文件参考.md)
