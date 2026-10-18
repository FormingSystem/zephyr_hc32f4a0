---
id: learning.zephyr-docs.api-protocol-topic-reference.page-60
title: STM32 SDMMC API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__sdmmc__disk__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_STM32 SDMMC API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__stm32__sdmmc__disk__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STM32 SDMMC 控制器（Controller）。

<a id="details"></a>

STM32 SDMMC 控制器（Controller）。

<a id="header-files"></a>
<a id="files"></a>

## 60.1\_文件（Files）

<a id="r_sdmmc_5Fstm32_2Eh"></a>

```c
file sdmmc_stm32.h
```

相关声明：[sdmmc_stm32.h](../api_file_configuration_reference/P066_zephyr__drivers__disk__sdmmc_stm32.h_文件参考.md)。

STM32 SDMMC扩展磁盘（Disk）API的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 60.2\_函数（Functions）

<a id="r_gadfccc3613153a85f5b14d3b600220e42"></a>

```c
void stm32_sdmmc_get_card_cid (const struct device *dev, uint32_t cid[4])
```

相关声明：[stm32_sdmmc_get_card_cid](#gadfccc3613153a85f5b14d3b600220e42)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 SD/MMC 卡获取卡标识信息（Card Identification，CID）。

<a id="r_ga391e478b31cbe349faea2f531a0c1935"></a>

```c
void stm32_sdmmc_get_card_csd (const struct device *dev, uint32_t csd[4])
```

相关声明：[stm32_sdmmc_get_card_csd](#ga391e478b31cbe349faea2f531a0c1935)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 SD/MMC 卡获取卡特定数据信息（Card Specific Data，CSD）。

## 60.3\_详细说明（Detailed Documentation）

<a id="gadfccc3613153a85f5b14d3b600220e42"></a>

### `stm32_sdmmc_get_card_cid()`

```c
void stm32_sdmmc_get_card_cid ( const struct device * dev, uint32_t cid[4] )
```

```c
#include <zephyr/drivers/disk/sdmmc_stm32.h>
```

从 SD/MMC 卡获取卡标识信息（Card Identification，CID）。

此函数从设备初始化期间填充的内部硬件抽象层（HAL）SD/MMC 结构体复制卡标识数据（Card Identification Data，CID）。它不检查卡当前是否存在或其当前状态。如果初始化后卡被移除，或者初始化失败，返回的 CID 可能已经过时或全部为零。

调用方有责任在调用此函数之前确认卡存在且已初始化，例如调用 `disk_access_status`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向表示 SD/MMC 卡的设备结构体的指针。 |
| `cid` | 指向用于存储 CID 数据的数组的指针。 |

<a id="ga391e478b31cbe349faea2f531a0c1935"></a>

### `stm32_sdmmc_get_card_csd()`

```c
void stm32_sdmmc_get_card_csd ( const struct device * dev, uint32_t csd[4] )
```

```c
#include <zephyr/drivers/disk/sdmmc_stm32.h>
```

从 SD/MMC 卡获取卡特定数据信息（Card Specific Data，CSD）。

此函数从设备初始化期间填充的内部硬件抽象层（HAL）SD/MMC 结构体复制卡专用数据（Card Specific Data，CSD）。它不检查卡当前是否存在或其当前状态。如果初始化后卡被移除，或者初始化失败，返回的 CSD 可能已经过时或全部为零。

调用方有责任在调用此函数之前确认卡存在且已初始化，例如调用 `disk_access_status`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向表示 SD/MMC 卡的设备结构体的指针。 |
| `csd` | 指向用于存储 CSD 数据的数组的指针。 |


## 60.4\_原页交叉引用（Cross References）

- [sdmmc_stm32.h](../api_file_configuration_reference/P066_zephyr__drivers__disk__sdmmc_stm32.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [disk_access_status](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gac5348a854fe68a607672118c91346133)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P059_Wi-Fi 扫描配置（Scanning configuration）.md) · [返回大纲](大纲.md) · [下一章](P061_TLE9104 API主题.md)
