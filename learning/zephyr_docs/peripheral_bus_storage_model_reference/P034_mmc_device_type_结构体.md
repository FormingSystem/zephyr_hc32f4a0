---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-34
title: mmc_device_type_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmmc__device__type.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_mmc\_device\_type\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmmc__device__type.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

多媒体卡（MMC）的设备类型。

```c
#include <zephyr/sd/sd_spec.h>
```

<a id="details"></a>

MMC 设备类型（Device Type），编码在 `EXT_CSD` 中。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_ab19f29678c18ba8740758ca136fd7744"></a>

```c
bool MMC_HS400_DDR_1200MV
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[MMC_HS400_DDR_1200MV](#ab19f29678c18ba8740758ca136fd7744)。

<a id="r_a24bee6ea4bd6d209b53b05fb9e040b38"></a>

```c
bool MMC_HS400_DDR_1800MV
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[MMC_HS400_DDR_1800MV](#a24bee6ea4bd6d209b53b05fb9e040b38)。

<a id="r_aaa7bb99717ecde9e6cf265a6c5bb33f0"></a>

```c
bool MMC_HS200_SDR_1200MV
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[MMC_HS200_SDR_1200MV](#aaa7bb99717ecde9e6cf265a6c5bb33f0)。

<a id="r_a7027fdec8b21be17a2ba97b2b19a13da"></a>

```c
bool MMC_HS200_SDR_1800MV
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[MMC_HS200_SDR_1800MV](#a7027fdec8b21be17a2ba97b2b19a13da)。

<a id="r_a65bc5ecdb11da48c08a06d4c5c386590"></a>

```c
bool MMC_HS_DDR_1200MV
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[MMC_HS_DDR_1200MV](#a65bc5ecdb11da48c08a06d4c5c386590)。

<a id="r_a5d338770aca6d893e094f57211b0339e"></a>

```c
bool MMC_HS_DDR_1800MV
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[MMC_HS_DDR_1800MV](#a5d338770aca6d893e094f57211b0339e)。

<a id="r_a3f4bbe853ef59313a84acb5737cafdf4"></a>

```c
bool MMC_HS_52_DV
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[MMC_HS_52_DV](#a3f4bbe853ef59313a84acb5737cafdf4)。

<a id="r_a12bb36ef4914b9182f08c4310c85d70d"></a>

```c
bool MMC_HS_26_DV
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[MMC_HS_26_DV](#a12bb36ef4914b9182f08c4310c85d70d)。

## 34.2\_详细说明（Detailed Documentation）

<a id="aaa7bb99717ecde9e6cf265a6c5bb33f0"></a>

### `MMC_HS200_SDR_1200MV`

```c
bool mmc_device_type::MMC_HS200_SDR_1200MV
```

<a id="a7027fdec8b21be17a2ba97b2b19a13da"></a>

### `MMC_HS200_SDR_1800MV`

```c
bool mmc_device_type::MMC_HS200_SDR_1800MV
```

<a id="ab19f29678c18ba8740758ca136fd7744"></a>

### `MMC_HS400_DDR_1200MV`

```c
bool mmc_device_type::MMC_HS400_DDR_1200MV
```

<a id="a24bee6ea4bd6d209b53b05fb9e040b38"></a>

### `MMC_HS400_DDR_1800MV`

```c
bool mmc_device_type::MMC_HS400_DDR_1800MV
```

<a id="a12bb36ef4914b9182f08c4310c85d70d"></a>

### `MMC_HS_26_DV`

```c
bool mmc_device_type::MMC_HS_26_DV
```

<a id="a3f4bbe853ef59313a84acb5737cafdf4"></a>

### `MMC_HS_52_DV`

```c
bool mmc_device_type::MMC_HS_52_DV
```

<a id="a65bc5ecdb11da48c08a06d4c5c386590"></a>

### `MMC_HS_DDR_1200MV`

```c
bool mmc_device_type::MMC_HS_DDR_1200MV
```

<a id="a5d338770aca6d893e094f57211b0339e"></a>

### `MMC_HS_DDR_1800MV`

```c
bool mmc_device_type::MMC_HS_DDR_1800MV
```

本数据类型文档由以下文件生成：

- `zephyr/sd/sd_spec.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/sd/sd_spec.h](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_memc_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_mmc_ext_csd_结构体.md)
