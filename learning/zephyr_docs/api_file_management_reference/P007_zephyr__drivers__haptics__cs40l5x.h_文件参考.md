---
id: learning.zephyr-docs.api-file-management-reference.page-7
title: zephyr__drivers__haptics__cs40l5x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cs40l5x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_haptics\_\_cs40l5x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cs40l5x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

提供CS40L5x触觉反馈（Haptic）驱动API的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/gpio.h>
#include <zephyr/drivers/i2c.h>
#include <zephyr/drivers/spi.h>
#include <zephyr/drivers/haptics.h>
#include <zephyr/kernel.h>
#include <zephyr/logging/log_instance.h>
#include <sys/types.h>
```

查看此文件的源码。

提供CS40L5x触觉反馈（Haptic）驱动API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_cs40l5x_5Fpwle_5Fsection"></a>

```c
struct cs40l5x_pwle_section
```

相关声明：[cs40l5x_pwle_section](../hardware/P156_CS40L5x包络段结构.md)。

分段线性包络（PWLE）的区段定义。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.2\_枚举（Enumerations）

<a id="r_ga730b10a2de457f7e06374a85d049a7c2"></a>

```c
enum cs40l5x_attenuation { CS40L5X_ATTENUATION_7DB = -7 , CS40L5X_ATTENUATION_6DB , CS40L5X_ATTENUATION_5DB , CS40L5X_ATTENUATION_4DB , CS40L5X_ATTENUATION_3DB , CS40L5X_ATTENUATION_2DB , CS40L5X_ATTENUATION_1DB , CS40L5X_ATTENUATION_0DB }
```

相关声明：[cs40l5x_attenuation](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ga730b10a2de457f7e06374a85d049a7c2)、[CS40L5X_ATTENUATION_7DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2ab3c933ea4df278b7e15cca5c1770a6bd)、[CS40L5X_ATTENUATION_6DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2a25206aeedc40f970ccef2afe68b0f5dd)、[CS40L5X_ATTENUATION_5DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2a5f28e05a671f441076d80349d59088b2)、[CS40L5X_ATTENUATION_4DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2a909728ddf9276fa1bc6c8e170691f746)、[CS40L5X_ATTENUATION_3DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2aefa22f7f4da6595ef9f8c7fe7c4a0fe5)、[CS40L5X_ATTENUATION_2DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2a0a7375b14e55fcbf973cc00bc7c74276)、[CS40L5X_ATTENUATION_1DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2ab520b7031f40274fbc15306969b77b3d)、[CS40L5X_ATTENUATION_0DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2ad173893cb6c1956f2d8a65156d372a8b)。

触发式触觉效果（triggered haptic effects）的衰减选项（attenuation options）。

<a id="r_ga9661112e1203b8d1d1d8b1cc301867ba"></a>

```c
enum cs40l5x_source { CS40L5X_SOURCE_BUZ = HAPTICS_SOURCE_PRIV_START , CS40L5X_SOURCE_RTH }
```

相关声明：[cs40l5x_source](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ga9661112e1203b8d1d1d8b1cc301867ba)、[CS40L5X_SOURCE_BUZ](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga9661112e1203b8d1d1d8b1cc301867baacab632c05aee9f8ea3c8b12d51a80416)、[CS40L5X_SOURCE_RTH](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga9661112e1203b8d1d1d8b1cc301867baa6ef270b8eb732be872993c2fed6b46c4)。

触觉效果的波表源（wavetable sources）。

<a id="r_gab467d07e5366412df6da36a857bd16a3"></a>

```c
enum cs40l5x_trigger_edge { CS40L5X_RISING_EDGE , CS40L5X_FALLING_EDGE }
```

相关声明：[cs40l5x_trigger_edge](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gab467d07e5366412df6da36a857bd16a3)、[CS40L5X_RISING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ggab467d07e5366412df6da36a857bd16a3a0a0316402f70b6c90bbd87a567ab0b27)、[CS40L5X_FALLING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ggab467d07e5366412df6da36a857bd16a3a53931ab676fefc265837fa5dc2245e7b)。

边沿触发式触觉效果（edge-triggered haptic effects）的选项。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_gadbd8db2db2832e5e0fe468ce1f298b70"></a>

```c
int cs40l5x_configure_buzz (const struct device *const dev, const uint32_t frequency, const uint8_t level, const uint32_t duration)
```

相关声明：[cs40l5x_configure_buzz](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gadbd8db2db2832e5e0fe468ce1f298b70)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置用于触觉播放（Haptic Playback）的 ROM 嗡振（ROM Buzz）。

<a id="r_gac6d8832a9952f2e63ec3f5ad0fa6b057"></a>

```c
int cs40l5x_configure_trigger (const struct device *const dev, const struct gpio_dt_spec *const gpio, const enum haptics_source src, const union haptics_config *const cfg, const enum cs40l5x_attenuation attenuation, const enum cs40l5x_trigger_edge edge)
```

相关声明：[cs40l5x_configure_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gac6d8832a9952f2e63ec3f5ad0fa6b057)、[device](../device_reference/P002_设备对象结构.md)、[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga72bcc5e6627d6079f81ad8488439f7e4)、[haptics_config](../hardware/P151_触觉源配置联合体.md)、[cs40l5x_attenuation](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ga730b10a2de457f7e06374a85d049a7c2)、[cs40l5x_trigger_edge](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gab467d07e5366412df6da36a857bd16a3)。

配置边沿触发式触觉效果。

<a id="r_ga17101a4e1db6c1b97670da67f640f226"></a>

```c
int cs40l5x_upload_pcm (const struct device *const dev, const int index, const uint16_t redc, const uint16_t f0, const int8_t *const samples, const uint16_t num_samples)
```

相关声明：[cs40l5x_upload_pcm](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ga17101a4e1db6c1b97670da67f640f226)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将脉冲编码调制（PCM）效果上传到指定索引。

<a id="r_ga0283ec128debbc6ece55637e0fb79346"></a>

```c
int cs40l5x_upload_pwle (const struct device *const dev, const int index, const struct cs40l5x_pwle_section *const sections, const uint8_t num_sections)
```

相关声明：[cs40l5x_upload_pwle](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ga0283ec128debbc6ece55637e0fb79346)、[device](../device_reference/P002_设备对象结构.md)、[cs40l5x_pwle_section](../hardware/P156_CS40L5x包络段结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将分段线性包络（PWLE）效果上传到指定索引。


## 7.4\_原页交叉引用（Cross References）

- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P002_I2C驱动头文件源码.md)
- [zephyr/drivers/spi.h](../spi_driver_reference/P002_SPI驱动头文件源码.md)
- [zephyr/drivers/haptics.h](../api_source_system_reference/P013_haptics.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/logging/log_instance.h](../log_internal_reference/P004_日志实例头文件源码.md)
- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P037_cs40l5x.h_源码浏览.md)
- [cs40l5x_pwle_section](../hardware/P156_CS40L5x包络段结构.md)
- [cs40l5x_attenuation](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ga730b10a2de457f7e06374a85d049a7c2)
- [CS40L5X_ATTENUATION_7DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2ab3c933ea4df278b7e15cca5c1770a6bd)
- [CS40L5X_ATTENUATION_6DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2a25206aeedc40f970ccef2afe68b0f5dd)
- [CS40L5X_ATTENUATION_5DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2a5f28e05a671f441076d80349d59088b2)
- [CS40L5X_ATTENUATION_4DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2a909728ddf9276fa1bc6c8e170691f746)
- [CS40L5X_ATTENUATION_3DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2aefa22f7f4da6595ef9f8c7fe7c4a0fe5)
- [CS40L5X_ATTENUATION_2DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2a0a7375b14e55fcbf973cc00bc7c74276)
- [CS40L5X_ATTENUATION_1DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2ab520b7031f40274fbc15306969b77b3d)
- [CS40L5X_ATTENUATION_0DB](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga730b10a2de457f7e06374a85d049a7c2ad173893cb6c1956f2d8a65156d372a8b)
- [cs40l5x_source](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ga9661112e1203b8d1d1d8b1cc301867ba)
- [CS40L5X_SOURCE_BUZ](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga9661112e1203b8d1d1d8b1cc301867baacab632c05aee9f8ea3c8b12d51a80416)
- [CS40L5X_SOURCE_RTH](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gga9661112e1203b8d1d1d8b1cc301867baa6ef270b8eb732be872993c2fed6b46c4)
- [cs40l5x_trigger_edge](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gab467d07e5366412df6da36a857bd16a3)
- [CS40L5X_RISING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ggab467d07e5366412df6da36a857bd16a3a0a0316402f70b6c90bbd87a567ab0b27)
- [CS40L5X_FALLING_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ggab467d07e5366412df6da36a857bd16a3a53931ab676fefc265837fa5dc2245e7b)
- [cs40l5x_configure_buzz](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gadbd8db2db2832e5e0fe468ce1f298b70)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cs40l5x_configure_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#gac6d8832a9952f2e63ec3f5ad0fa6b057)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [haptics_source](https://docs.zephyrproject.org/latest/doxygen/html/group__haptics__interface.html#ga72bcc5e6627d6079f81ad8488439f7e4)
- [haptics_config](../hardware/P151_触觉源配置联合体.md)
- [cs40l5x_upload_pcm](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ga17101a4e1db6c1b97670da67f640f226)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [cs40l5x_upload_pwle](https://docs.zephyrproject.org/latest/doxygen/html/group__cs40l5x__interface.html#ga0283ec128debbc6ece55637e0fb79346)

<a id="header-details"></a>

---

[上一章](P006_zephyr__net__conn_mgr_monitor.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__gnss__rtk__decoder.h_文件参考.md)
