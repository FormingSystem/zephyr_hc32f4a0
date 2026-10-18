---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-15
title: espi_saf_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structespi__saf__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_espi\_saf\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structespi__saf__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

eSPI从设备附属闪存（SAF）的配置参数。

```c
#include <zephyr/drivers/espi_saf.h>
```

<a id="details"></a>

eSPI从设备附属闪存（SAF）的配置参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_ab07ab3b33980f6865cbadbbcb5e203c0"></a>

```c
uint8_t nflash_devices
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nflash_devices](#ab07ab3b33980f6865cbadbbcb5e203c0)。

<a id="r_a20da4ce3549c53adb038dab7a5bed8a8"></a>

```c
struct espi_saf_hw_cfg hwcfg
```

相关声明：[hwcfg](#a20da4ce3549c53adb038dab7a5bed8a8)。

<a id="r_a99d90bcf04f3f09ac5fb739b390a42c8"></a>

```c
struct espi_saf_flash_cfg * flash_cfgs
```

相关声明：[flash_cfgs](#a99d90bcf04f3f09ac5fb739b390a42c8)。

## 15.2\_详细说明（Detailed Documentation）

<a id="a99d90bcf04f3f09ac5fb739b390a42c8"></a>

### `flash_cfgs`

```c
struct espi_saf_flash_cfg* espi_saf_cfg::flash_cfgs
```

<a id="a20da4ce3549c53adb038dab7a5bed8a8"></a>

### `hwcfg`

```c
struct espi_saf_hw_cfg espi_saf_cfg::hwcfg
```

<a id="ab07ab3b33980f6865cbadbbcb5e203c0"></a>

### `nflash_devices`

```c
uint8_t espi_saf_cfg::nflash_devices
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/espi_saf.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/drivers/espi_saf.h](https://docs.zephyrproject.org/latest/doxygen/html/espi__saf_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_espi_request_packet_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_espi_saf_driver_api_结构体.md)
