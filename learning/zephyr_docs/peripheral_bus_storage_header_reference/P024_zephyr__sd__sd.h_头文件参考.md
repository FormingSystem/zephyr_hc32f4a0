---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-24
title: zephyr__sd__sd.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_zephyr\_\_sd\_\_sd.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全数字（SD）子系统的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/sdhc.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

安全数字（SD）子系统的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 24.1\_数据结构（Data Structures）

<a id="r_sdio_5Ffunc"></a>

```c
struct sdio_func
```

相关声明：[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)。

SDIO功能（Function）的定义。

<a id="r_sd_5Fcard"></a>

```c
struct sd_card
```

相关声明：[sd_card](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md)。

SD卡（SD Card）结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 24.2\_枚举（Enumerations）

<a id="r_a52167aac735d93085a5eebc6f50e1bba"></a>

```c
enum card_status { CARD_UNINITIALIZED = 0 , CARD_ERROR = 1 , CARD_INITIALIZED = 2 }
```

相关声明：[card_status](#a52167aac735d93085a5eebc6f50e1bba)、[CARD_UNINITIALIZED](#a52167aac735d93085a5eebc6f50e1bbaaa059e919850b36b85ebe33a07050e453)、[CARD_ERROR](#a52167aac735d93085a5eebc6f50e1bbaa5458e6fab05f8c1afbe7d191eb489e5e)、[CARD_INITIALIZED](#a52167aac735d93085a5eebc6f50e1bbaa839d17bb0bee41a125a617683bce17c9)。

卡状态。

<a id="r_aee707e2ff5691dbdefd9341a18de7b14"></a>

```c
enum card_type { CARD_SDMMC = 0 , CARD_SDIO = 1 , CARD_COMBO = 2 , CARD_MMC = 3 }
```

相关声明：[card_type](#aee707e2ff5691dbdefd9341a18de7b14)、[CARD_SDMMC](#aee707e2ff5691dbdefd9341a18de7b14a8b26749346e26d9257cd53c48a68eda4)、[CARD_SDIO](#aee707e2ff5691dbdefd9341a18de7b14a5afc0338b5a0541bb34f1a5b67139b6b)、[CARD_COMBO](#aee707e2ff5691dbdefd9341a18de7b14ad527710e81e76e0938689015c2013090)、[CARD_MMC](#aee707e2ff5691dbdefd9341a18de7b14a868625c31f4384780de3992d78b93345)。

卡类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.3\_函数（Functions）

<a id="r_ac02b6fe46112b8b891e9713ef24bd131"></a>

```c
int sd_init (const struct device *sdhc_dev, struct sd_card *card)
```

相关声明：[sd_init](#ac02b6fe46112b8b891e9713ef24bd131)、[device](../device_reference/P002_设备对象结构.md)、[sd_card](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md)。

初始化 SD 设备。

<a id="r_aed46c9c492c5c6434a6ae4d6151ac7d3"></a>

```c
bool sd_is_card_present (const struct device *sdhc_dev)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[sd_is_card_present](#aed46c9c492c5c6434a6ae4d6151ac7d3)、[device](../device_reference/P002_设备对象结构.md)。

检查 SD 插槽中是否有卡。

## 24.4\_详细说明（Detailed Documentation）

<a id="a52167aac735d93085a5eebc6f50e1bba"></a>

### `card_status`

```c
enum card_status
```

卡状态。

供子系统内部使用。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CARD_UNINITIALIZED` | 卡尚未初始化。 |
| `CARD_ERROR` | 卡处于错误状态。 |
| `CARD_INITIALIZED` | 卡处于有效状态。 |

<a id="aee707e2ff5691dbdefd9341a18de7b14"></a>

### `card_type`

```c
enum card_type
```

卡类型。

供子系统内部使用。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CARD_SDMMC` | SD 存储卡（Memory card）。 |
| `CARD_SDIO` | SD I/O 卡。 |
| `CARD_COMBO` | SD 存储与 I/O 组合卡。 |
| `CARD_MMC` | MMC 存储卡。 |

<a id="ac02b6fe46112b8b891e9713ef24bd131"></a>

### `sd_init()`

```c
int sd_init ( const struct device * sdhc_dev, struct sd_card * card )
```

初始化 SD 设备。

初始化 SD 设备以供子系统使用。调用后，仅需 SD 卡结构体即可访问此卡。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sdhc_dev` | 此卡对应的 SD 主机控制器设备。 |
| `card` | 此卡对应的 SD 卡结构体。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 卡已初始化。 |
| `-ETIMEDOUT` | 卡初始化超时。 |
| `-EBUSY` | 卡忙。 |
| `-EIO` | 启动卡时发生 I/O 错误。 |

<a id="aed46c9c492c5c6434a6ae4d6151ac7d3"></a>

### `sd_is_card_present()`

```c
bool sd_is_card_present ( const struct device * sdhc_dev)
```

检查 SD 插槽中是否有卡。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sdhc_dev` | 要检查卡是否存在的 SD 主机控制器。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 存在卡。 |
| `false` | 不存在卡。 |


## 24.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/sdhc.h](https://docs.zephyrproject.org/latest/doxygen/html/sdhc_8h_source.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/sd_8h_source.html)
- [sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)
- [sd_card](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [true](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a52167aac735d93085a5eebc6f50e1bbaaa059e919850b36b85ebe33a07050e453"></a>
<a id="a52167aac735d93085a5eebc6f50e1bbaa5458e6fab05f8c1afbe7d191eb489e5e"></a>
<a id="a52167aac735d93085a5eebc6f50e1bbaa839d17bb0bee41a125a617683bce17c9"></a>
<a id="aee707e2ff5691dbdefd9341a18de7b14a8b26749346e26d9257cd53c48a68eda4"></a>
<a id="aee707e2ff5691dbdefd9341a18de7b14a5afc0338b5a0541bb34f1a5b67139b6b"></a>
<a id="aee707e2ff5691dbdefd9341a18de7b14ad527710e81e76e0938689015c2013090"></a>
<a id="aee707e2ff5691dbdefd9341a18de7b14a868625c31f4384780de3992d78b93345"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P023_zephyr__drivers__psi5__psi5.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_zephyr__drivers__sdhc.h_头文件参考.md)
