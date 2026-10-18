---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-14
title: 多位串行外设接口（MSPI）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_多位串行外设接口（MSPI）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）控制器接口。

<a id="details"></a>

多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）控制器接口。自 Zephyr 3.7 起提供；API 版本为 0.9.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 14.1\_主题（Topics）

<a id="r_mspi_5Fconfigure_5Fapi"></a>

相关声明：[MSPI 配置 API（MSPI Configure API）](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html)。

MSPI 配置 API（MSPI Configure API）

<a id="r_mspi_5Fdevicetree"></a>

相关声明：[MSPI 设备树相关宏](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html)。

MSPI 设备树相关宏

<a id="r_mspi_5Finterface_5Fbackend"></a>

相关声明：[MSPI 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html)。

<a id="r_mspi_5Femul_5Finterface"></a>

相关声明：[MSPI 仿真接口（MSPI Emulation Interface）](../hardware/P487_MSPI总线仿真接口.md)。

MSPI 仿真接口（MSPI Emulation Interface）

<a id="r_mspi_5Ftransfer_5Fapi"></a>

相关声明：[MSPI 传输 API（MSPI Transfer API）](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__transfer__api.html)。

MSPI 传输 API（MSPI Transfer API）

<a id="r_mspi_5Fcallback_5Fapi"></a>

相关声明：[MSPI 回调 API（MSPI callback API）](../api_protocol_topic_reference/P037_MSPI 回调 API（MSPI callback API）.md)。

MSPI 回调 API（MSPI callback API）

<a id="r_mspi_5Futil"></a>

相关声明：[MSPI 工具（Mspi_util）](../api_topic_reference/P053_MSPI 工具（Mspi_util）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 14.2\_文件（Files）

<a id="r_mspi_2Eh"></a>

```c
file mspi.h
```

相关声明：[mspi.h](../peripheral_bus_storage_header_reference/P017_zephyr__drivers__mspi.h_头文件参考.md)。

多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）驱动API的主头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.3\_枚举（Enumerations）

<a id="r_ga3f211cd81e05cb9ee073a2722f6b22d8"></a>

```c
enum mspi_op_mode { MSPI_OP_MODE_CONTROLLER = 0 , MSPI_OP_MODE_PERIPHERAL = 1 }
```

相关声明：[mspi_op_mode](#ga3f211cd81e05cb9ee073a2722f6b22d8)、[MSPI_OP_MODE_CONTROLLER](#gga3f211cd81e05cb9ee073a2722f6b22d8a6a862f1d9931725be7789bd982d2937a)、[MSPI_OP_MODE_PERIPHERAL](#gga3f211cd81e05cb9ee073a2722f6b22d8a11af11e286399c7e2f1fbcadca44ea83)。

MSPI 工作模式（Operational mode）。

<a id="r_ga20e348d7a9f1f9b32078a3bf6c4e82b9"></a>

```c
enum mspi_duplex { MSPI_HALF_DUPLEX = 0 , MSPI_FULL_DUPLEX = 1 }
```

相关声明：[mspi_duplex](#ga20e348d7a9f1f9b32078a3bf6c4e82b9)、[MSPI_HALF_DUPLEX](#gga20e348d7a9f1f9b32078a3bf6c4e82b9ac05ddc8ca44f1c70d3c3748e21fe80d3)、[MSPI_FULL_DUPLEX](#gga20e348d7a9f1f9b32078a3bf6c4e82b9a13a3f16c4273ca6f28671663d0ecf33c)。

MSPI 双工模式（Duplex mode）。

<a id="r_ga904dfc1c800fb9832f7c6200f767f9a5"></a>

```c
enum mspi_io_mode { MSPI_IO_MODE_SINGLE = 0 , MSPI_IO_MODE_DUAL = 1 , MSPI_IO_MODE_DUAL_1_1_2 = 2 , MSPI_IO_MODE_DUAL_1_2_2 = 3 , MSPI_IO_MODE_QUAD = 4 , MSPI_IO_MODE_QUAD_1_1_4 = 5 , MSPI_IO_MODE_QUAD_1_4_4 = 6 , MSPI_IO_MODE_OCTAL = 7 , MSPI_IO_MODE_OCTAL_1_1_8 = 8 , MSPI_IO_MODE_OCTAL_1_8_8 = 9 , MSPI_IO_MODE_HEX = 10 , MSPI_IO_MODE_HEX_8_8_16 = 11 , MSPI_IO_MODE_HEX_8_16_16 = 12 , MSPI_IO_MODE_MAX }
```

相关声明：[mspi_io_mode](#ga904dfc1c800fb9832f7c6200f767f9a5)、[MSPI_IO_MODE_SINGLE](#gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd)、[MSPI_IO_MODE_DUAL](#gga904dfc1c800fb9832f7c6200f767f9a5a9826a30dc94c734cdad9f91148cb8673)、[MSPI_IO_MODE_DUAL_1_1_2](#gga904dfc1c800fb9832f7c6200f767f9a5a8225b99a3943f35b1c713af462a2d5da)、[MSPI_IO_MODE_DUAL_1_2_2](#gga904dfc1c800fb9832f7c6200f767f9a5aaee80ab69881b09ec6b85dbaaa9e8663)、[MSPI_IO_MODE_QUAD](#gga904dfc1c800fb9832f7c6200f767f9a5af65a413ec9c72d6c7acf5154a618870a)、[MSPI_IO_MODE_QUAD_1_1_4](#gga904dfc1c800fb9832f7c6200f767f9a5abe9925279cee8433d2b11cc3614c5a5a)、[MSPI_IO_MODE_QUAD_1_4_4](#gga904dfc1c800fb9832f7c6200f767f9a5a1b3112af8589ef5e2493fc6545c4945a)、[MSPI_IO_MODE_OCTAL](#gga904dfc1c800fb9832f7c6200f767f9a5ac79eb0c07038226a74411ca211d9b725)、[MSPI_IO_MODE_OCTAL_1_1_8](#gga904dfc1c800fb9832f7c6200f767f9a5ac70792100fe11a07c020c9825c1cdfbf)、[MSPI_IO_MODE_OCTAL_1_8_8](#gga904dfc1c800fb9832f7c6200f767f9a5a1d6b2be620bf17c4daecad66ba011573)、[MSPI_IO_MODE_HEX](#gga904dfc1c800fb9832f7c6200f767f9a5a1882d6c9772a1fa1e9e255fe3883d86b)、[MSPI_IO_MODE_HEX_8_8_16](#gga904dfc1c800fb9832f7c6200f767f9a5ade6a4a01f3281e5331b3e16f1222eb02)、[MSPI_IO_MODE_HEX_8_16_16](#gga904dfc1c800fb9832f7c6200f767f9a5a49283124787af5787d64c71bf38e3caa)、[MSPI_IO_MODE_MAX](#gga904dfc1c800fb9832f7c6200f767f9a5a9f726ce3043c03703d48bcdc45edcbdb)。

MSPI I/O 模式能力。`1_4_4` 等后缀表示命令、地址和数据阶段分别使用的线路数量。

<a id="r_gaa2131d9846bbfd74488a6ae1c2003e68"></a>

```c
enum mspi_data_rate { MSPI_DATA_RATE_SINGLE = 0 , MSPI_DATA_RATE_S_S_D = 1 , MSPI_DATA_RATE_S_D_D = 2 , MSPI_DATA_RATE_DUAL = 3 , MSPI_DATA_RATE_MAX }
```

相关声明：[mspi_data_rate](#gaa2131d9846bbfd74488a6ae1c2003e68)、[MSPI_DATA_RATE_SINGLE](#ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0)、[MSPI_DATA_RATE_S_S_D](#ggaa2131d9846bbfd74488a6ae1c2003e68a388bbd530a438507dbfa9208ec1ebf39)、[MSPI_DATA_RATE_S_D_D](#ggaa2131d9846bbfd74488a6ae1c2003e68a8cea9da4829a0769e3be8b8a32b79984)、[MSPI_DATA_RATE_DUAL](#ggaa2131d9846bbfd74488a6ae1c2003e68a96f82a24b684a7debe0ac32070fa53bc)、[MSPI_DATA_RATE_MAX](#ggaa2131d9846bbfd74488a6ae1c2003e68a51f3574f42456a11cc3fcd17c1195dd9)。

MSPI 数据速率能力。`SINGLE` 表示所有阶段均采用单数据速率（Single data rate）。

<a id="r_ga704e4d3759d3261b4468e9d9900e578c"></a>

```c
enum mspi_cpp_mode { MSPI_CPP_MODE_0 = 0 , MSPI_CPP_MODE_1 = 1 , MSPI_CPP_MODE_2 = 2 , MSPI_CPP_MODE_3 = 3 }
```

相关声明：[mspi_cpp_mode](#ga704e4d3759d3261b4468e9d9900e578c)、[MSPI_CPP_MODE_0](#gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90)、[MSPI_CPP_MODE_1](#gga704e4d3759d3261b4468e9d9900e578ca8c93d56778ea1cbf901db1a4b9fee870)、[MSPI_CPP_MODE_2](#gga704e4d3759d3261b4468e9d9900e578cabbde8c1ad9a5a8a9a3ca4ce33e2c0705)、[MSPI_CPP_MODE_3](#gga704e4d3759d3261b4468e9d9900e578ca415e431b25ac4a12f35b139ccb77ba48)。

MSPI 极性与相位模式（Polarity & Phase Modes）。

<a id="r_ga3625cde1379e66cb66a8cb3803ab2e44"></a>

```c
enum mspi_endian { MSPI_XFER_LITTLE_ENDIAN = 0 , MSPI_XFER_BIG_ENDIAN = 1 }
```

相关声明：[mspi_endian](#ga3625cde1379e66cb66a8cb3803ab2e44)、[MSPI_XFER_LITTLE_ENDIAN](#gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345)、[MSPI_XFER_BIG_ENDIAN](#gga3625cde1379e66cb66a8cb3803ab2e44a08e9349361779ce246bb7da6a1f3012d)。

MSPI 字节序（Endianness）。

<a id="r_ga283275f86fe186f4b5e30110ae0d506b"></a>

```c
enum mspi_ce_polarity { MSPI_CE_ACTIVE_LOW = 0 , MSPI_CE_ACTIVE_HIGH = 1 }
```

相关声明：[mspi_ce_polarity](#ga283275f86fe186f4b5e30110ae0d506b)、[MSPI_CE_ACTIVE_LOW](#gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae)、[MSPI_CE_ACTIVE_HIGH](#gga283275f86fe186f4b5e30110ae0d506ba375e0b870800e0982b3715417e109a22)。

MSPI 片选使能（Chip enable）极性。

<a id="r_ga4cd05950729893e08ef0d4a12e2242d5"></a>

```c
enum mspi_bus_event { MSPI_BUS_RESET = 0 , MSPI_BUS_ERROR = 1 , MSPI_BUS_XFER_COMPLETE = 2 , MSPI_BUS_TIMEOUT = 3 , MSPI_BUS_EVENT_MAX }
```

相关声明：[mspi_bus_event](#ga4cd05950729893e08ef0d4a12e2242d5)、[MSPI_BUS_RESET](#gga4cd05950729893e08ef0d4a12e2242d5afb1c2030d871cbbaa4341df7989a5a64)、[MSPI_BUS_ERROR](#gga4cd05950729893e08ef0d4a12e2242d5aeeaf87802ecc90ada4c39f65fc0e8af0)、[MSPI_BUS_XFER_COMPLETE](#gga4cd05950729893e08ef0d4a12e2242d5ad47099019f15f97d83bc6435e5e76a61)、[MSPI_BUS_TIMEOUT](#gga4cd05950729893e08ef0d4a12e2242d5a9c538a902c3e5fa1086c0f0fcee4b7e6)、[MSPI_BUS_EVENT_MAX](#gga4cd05950729893e08ef0d4a12e2242d5a325aa40170de5621e89aa2def557f85a)。

MSPI 总线事件。

<a id="r_gab33e9840b0937c944f4e1a2525534cb1"></a>

```c
enum mspi_bus_event_cb_mask { MSPI_BUS_NO_CB = 0 , MSPI_BUS_RESET_CB = BIT(0) , MSPI_BUS_ERROR_CB = BIT(1) , MSPI_BUS_XFER_COMPLETE_CB = BIT(2) , MSPI_BUS_TIMEOUT_CB = BIT(3) }
```

相关声明：[mspi_bus_event_cb_mask](#gab33e9840b0937c944f4e1a2525534cb1)、[MSPI_BUS_NO_CB](#ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277)、[MSPI_BUS_RESET_CB](#ggab33e9840b0937c944f4e1a2525534cb1a63fb981aab764d752c1166fc112094a1)、[MSPI_BUS_ERROR_CB](#ggab33e9840b0937c944f4e1a2525534cb1a5cff8419a9236cc835a62b124debe498)、[MSPI_BUS_XFER_COMPLETE_CB](#ggab33e9840b0937c944f4e1a2525534cb1aa315ad9c5ba56979914b21208920aad7)、[MSPI_BUS_TIMEOUT_CB](#ggab33e9840b0937c944f4e1a2525534cb1af587e68d07441f3262ab164f48e783c0)。

MSPI 总线事件回调掩码。这是初步列表，与 `mspi_bus_event` 相同。

<a id="r_ga116259bbb1d12a10c2ba9e6051f2f000"></a>

```c
enum mspi_xfer_mode { MSPI_PIO , MSPI_DMA }
```

相关声明：[mspi_xfer_mode](#ga116259bbb1d12a10c2ba9e6051f2f000)、[MSPI_PIO](#gga116259bbb1d12a10c2ba9e6051f2f000abea5c6920a3e81fe332c2a76e4d838a1)、[MSPI_DMA](#gga116259bbb1d12a10c2ba9e6051f2f000a5a7235fe9c633206906d76d329f623a8)。

MSPI 传输模式。

<a id="r_ga632af162124ca2959a21ca3759e1cc9e"></a>

```c
enum mspi_xfer_priority { MSPI_XFER_PRIORITY_LOW , MSPI_XFER_PRIORITY_MEDIUM , MSPI_XFER_PRIORITY_HIGH }
```

相关声明：[mspi_xfer_priority](#ga632af162124ca2959a21ca3759e1cc9e)、[MSPI_XFER_PRIORITY_LOW](#gga632af162124ca2959a21ca3759e1cc9ea31222dc35adf9bed70571b9b640aca97)、[MSPI_XFER_PRIORITY_MEDIUM](#gga632af162124ca2959a21ca3759e1cc9ea66753cdf13762a1dd995638ff71544e0)、[MSPI_XFER_PRIORITY_HIGH](#gga632af162124ca2959a21ca3759e1cc9ea3004e6ae8226294b669f2207e928f928)。

MSPI 传输优先级（Priority）。这是通常与 DMA 配合使用的初步优先级列表。

<a id="r_ga498f10591acf5dc7ec88e0aa98e537d6"></a>

```c
enum mspi_xfer_direction { MSPI_RX , MSPI_TX }
```

相关声明：[mspi_xfer_direction](#ga498f10591acf5dc7ec88e0aa98e537d6)、[MSPI_RX](#gga498f10591acf5dc7ec88e0aa98e537d6a044160eb569add203f06d963f57d3541)、[MSPI_TX](#gga498f10591acf5dc7ec88e0aa98e537d6a213d4457305ab45d31b9c06ec85d2b8a)。

MSPI 传输方向。

<a id="r_ga71c447d059acf7a8055c380243f3a647"></a>

```c
enum mspi_dev_cfg_mask { MSPI_DEVICE_CONFIG_NONE = 0 , MSPI_DEVICE_CONFIG_CE_NUM = BIT(0) , MSPI_DEVICE_CONFIG_FREQUENCY = BIT(1) , MSPI_DEVICE_CONFIG_IO_MODE = BIT(2) , MSPI_DEVICE_CONFIG_DATA_RATE = BIT(3) , MSPI_DEVICE_CONFIG_CPP = BIT(4) , MSPI_DEVICE_CONFIG_ENDIAN = BIT(5) , MSPI_DEVICE_CONFIG_CE_POL = BIT(6) , MSPI_DEVICE_CONFIG_DQS = BIT(7) , MSPI_DEVICE_CONFIG_RX_DUMMY = BIT(8) , MSPI_DEVICE_CONFIG_TX_DUMMY = BIT(9) , MSPI_DEVICE_CONFIG_READ_CMD = BIT(10) , MSPI_DEVICE_CONFIG_WRITE_CMD = BIT(11) , MSPI_DEVICE_CONFIG_CMD_LEN = BIT(12) , MSPI_DEVICE_CONFIG_ADDR_LEN = BIT(13) , MSPI_DEVICE_CONFIG_MEM_BOUND = BIT(14) , MSPI_DEVICE_CONFIG_BREAK_TIME = BIT(15) , MSPI_DEVICE_CONFIG_ALL = BIT_MASK(16) }
```

相关声明：[mspi_dev_cfg_mask](#ga71c447d059acf7a8055c380243f3a647)、[MSPI_DEVICE_CONFIG_NONE](#gga71c447d059acf7a8055c380243f3a647acc1d59bd6682933d364f060f31f26878)、[MSPI_DEVICE_CONFIG_CE_NUM](#gga71c447d059acf7a8055c380243f3a647a4a476e51f0d3613aab1bc9c1b335bab2)、[MSPI_DEVICE_CONFIG_FREQUENCY](#gga71c447d059acf7a8055c380243f3a647a135b081210bd5aabf5b610fe90212809)、[MSPI_DEVICE_CONFIG_IO_MODE](#gga71c447d059acf7a8055c380243f3a647a4aba5c75b43e1a87c66e940069b5b27f)、[MSPI_DEVICE_CONFIG_DATA_RATE](#gga71c447d059acf7a8055c380243f3a647a0e954604ea419f6a4fdea59e620bdcd9)、[MSPI_DEVICE_CONFIG_CPP](#gga71c447d059acf7a8055c380243f3a647a0d7032e045c80ca266e98f8c6684af65)、[MSPI_DEVICE_CONFIG_ENDIAN](#gga71c447d059acf7a8055c380243f3a647aba8ef6308b3e06a2ace1cc0f225d66ca)、[MSPI_DEVICE_CONFIG_CE_POL](#gga71c447d059acf7a8055c380243f3a647a51f46405fe8923a8b0c39bc2aad1ba0b)、[MSPI_DEVICE_CONFIG_DQS](#gga71c447d059acf7a8055c380243f3a647a56ceb1ba2a93a626623a13f148282537)、[MSPI_DEVICE_CONFIG_RX_DUMMY](#gga71c447d059acf7a8055c380243f3a647a13385127a309507ff01559122e03623a)、[MSPI_DEVICE_CONFIG_TX_DUMMY](#gga71c447d059acf7a8055c380243f3a647a60b857bd38b0cced89462771edccd9f5)、[MSPI_DEVICE_CONFIG_READ_CMD](#gga71c447d059acf7a8055c380243f3a647ae7c13ba10174e6f3f90161af69890872)、[MSPI_DEVICE_CONFIG_WRITE_CMD](#gga71c447d059acf7a8055c380243f3a647a99f486fd1f01684ac232d503af1abf2b)、[MSPI_DEVICE_CONFIG_CMD_LEN](#gga71c447d059acf7a8055c380243f3a647a1a2e21a3cbf0ee42977cc8a43efd3fac)、[MSPI_DEVICE_CONFIG_ADDR_LEN](#gga71c447d059acf7a8055c380243f3a647aa2ba135123fe9c89ce50fd86dfea759b)、[MSPI_DEVICE_CONFIG_MEM_BOUND](#gga71c447d059acf7a8055c380243f3a647ad07911eacaa2bde26a497c391e5c9946)、[MSPI_DEVICE_CONFIG_BREAK_TIME](#gga71c447d059acf7a8055c380243f3a647acdea4576df8e6d7d48cc289305237120)、[MSPI_DEVICE_CONFIG_ALL](#gga71c447d059acf7a8055c380243f3a647a67ae821a16a6280aca165ebf67bd2489)。

MSPI 控制器设备特定配置掩码。

<a id="r_gac127ef78c7b66c7eebe03782abf08c40"></a>

```c
enum mspi_memmap_permit { MSPI_MEMMAP_READ_WRITE = 0 , MSPI_MEMMAP_READ_ONLY = 1 }
```

相关声明：[mspi_memmap_permit](#gac127ef78c7b66c7eebe03782abf08c40)、[MSPI_MEMMAP_READ_WRITE](#ggac127ef78c7b66c7eebe03782abf08c40a5e34cb52b8e8475f9457a9cab7a424ed)、[MSPI_MEMMAP_READ_ONLY](#ggac127ef78c7b66c7eebe03782abf08c40aacecd5fab6e2ed50be75d882eaadadd6)。

MSPI 内存映射访问权限（Access permissions）。

## 14.4\_详细说明（Detailed Documentation）

<a id="ga4cd05950729893e08ef0d4a12e2242d5"></a>

### `mspi_bus_event`

```c
enum mspi_bus_event
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 总线事件。

这是初步的事件列表，欢迎社区继续补充。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_BUS_RESET` |  |
| `MSPI_BUS_ERROR` |  |
| `MSPI_BUS_XFER_COMPLETE` |  |
| `MSPI_BUS_TIMEOUT` | 请求或传输（xfer）超时时。 |
| `MSPI_BUS_EVENT_MAX` |  |

<a id="gab33e9840b0937c944f4e1a2525534cb1"></a>

### `mspi_bus_event_cb_mask`

```c
enum mspi_bus_event_cb_mask
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 总线事件回调掩码。这是初步列表，与 `mspi_bus_event` 相同。

欢迎社区继续补充。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_BUS_NO_CB` |  |
| `MSPI_BUS_RESET_CB` |  |
| `MSPI_BUS_ERROR_CB` |  |
| `MSPI_BUS_XFER_COMPLETE_CB` |  |
| `MSPI_BUS_TIMEOUT_CB` |  |

<a id="ga283275f86fe186f4b5e30110ae0d506b"></a>

### `mspi_ce_polarity`

```c
enum mspi_ce_polarity
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 片选使能（Chip enable）极性。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_CE_ACTIVE_LOW` |  |
| `MSPI_CE_ACTIVE_HIGH` |  |

<a id="ga704e4d3759d3261b4468e9d9900e578c"></a>

### `mspi_cpp_mode`

```c
enum mspi_cpp_mode
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 极性与相位模式（Polarity & Phase Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_CPP_MODE_0` |  |
| `MSPI_CPP_MODE_1` |  |
| `MSPI_CPP_MODE_2` |  |
| `MSPI_CPP_MODE_3` |  |

<a id="gaa2131d9846bbfd74488a6ae1c2003e68"></a>

### `mspi_data_rate`

```c
enum mspi_data_rate
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 数据速率能力。`SINGLE` 表示所有阶段均采用单数据速率（Single data rate）。

`DUAL` 表示所有阶段都采用双倍数据率（dual data rate）。`S_S_D` 表示命令和地址阶段采用单倍数据率，数据阶段采用双倍数据率。`S_D_D` 表示命令阶段采用单倍数据率，地址和数据阶段采用双倍数据率。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_DATA_RATE_SINGLE` |  |
| `MSPI_DATA_RATE_S_S_D` |  |
| `MSPI_DATA_RATE_S_D_D` |  |
| `MSPI_DATA_RATE_DUAL` |  |
| `MSPI_DATA_RATE_MAX` |  |

<a id="ga71c447d059acf7a8055c380243f3a647"></a>

### `mspi_dev_cfg_mask`

```c
enum mspi_dev_cfg_mask
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 控制器设备特定配置掩码。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_DEVICE_CONFIG_NONE` |  |
| `MSPI_DEVICE_CONFIG_CE_NUM` |  |
| `MSPI_DEVICE_CONFIG_FREQUENCY` |  |
| `MSPI_DEVICE_CONFIG_IO_MODE` |  |
| `MSPI_DEVICE_CONFIG_DATA_RATE` |  |
| `MSPI_DEVICE_CONFIG_CPP` |  |
| `MSPI_DEVICE_CONFIG_ENDIAN` |  |
| `MSPI_DEVICE_CONFIG_CE_POL` |  |
| `MSPI_DEVICE_CONFIG_DQS` |  |
| `MSPI_DEVICE_CONFIG_RX_DUMMY` |  |
| `MSPI_DEVICE_CONFIG_TX_DUMMY` |  |
| `MSPI_DEVICE_CONFIG_READ_CMD` |  |
| `MSPI_DEVICE_CONFIG_WRITE_CMD` |  |
| `MSPI_DEVICE_CONFIG_CMD_LEN` |  |
| `MSPI_DEVICE_CONFIG_ADDR_LEN` |  |
| `MSPI_DEVICE_CONFIG_MEM_BOUND` |  |
| `MSPI_DEVICE_CONFIG_BREAK_TIME` |  |
| `MSPI_DEVICE_CONFIG_ALL` |  |

<a id="ga20e348d7a9f1f9b32078a3bf6c4e82b9"></a>

### `mspi_duplex`

```c
enum mspi_duplex
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 双工模式（Duplex mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_HALF_DUPLEX` |  |
| `MSPI_FULL_DUPLEX` |  |

<a id="ga3625cde1379e66cb66a8cb3803ab2e44"></a>

### `mspi_endian`

```c
enum mspi_endian
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 字节序（Endianness）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_XFER_LITTLE_ENDIAN` |  |
| `MSPI_XFER_BIG_ENDIAN` |  |

<a id="ga904dfc1c800fb9832f7c6200f767f9a5"></a>

### `mspi_io_mode`

```c
enum mspi_io_mode
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI I/O 模式能力。`1_4_4` 等后缀表示命令、地址和数据阶段分别使用的线路数量。

没有后缀的模式在所有阶段使用相同数量的信号线。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_IO_MODE_SINGLE` |  |
| `MSPI_IO_MODE_DUAL` |  |
| `MSPI_IO_MODE_DUAL_1_1_2` |  |
| `MSPI_IO_MODE_DUAL_1_2_2` |  |
| `MSPI_IO_MODE_QUAD` |  |
| `MSPI_IO_MODE_QUAD_1_1_4` |  |
| `MSPI_IO_MODE_QUAD_1_4_4` |  |
| `MSPI_IO_MODE_OCTAL` |  |
| `MSPI_IO_MODE_OCTAL_1_1_8` |  |
| `MSPI_IO_MODE_OCTAL_1_8_8` |  |
| `MSPI_IO_MODE_HEX` |  |
| `MSPI_IO_MODE_HEX_8_8_16` |  |
| `MSPI_IO_MODE_HEX_8_16_16` |  |
| `MSPI_IO_MODE_MAX` |  |

<a id="gac127ef78c7b66c7eebe03782abf08c40"></a>

### `mspi_memmap_permit`

```c
enum mspi_memmap_permit
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 内存映射访问权限（Access permissions）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_MEMMAP_READ_WRITE` | 允许对内存映射区域（memory-mapped region）进行读写访问。 |
| `MSPI_MEMMAP_READ_ONLY` | 仅允许读取内存映射区域。 |

<a id="ga3f211cd81e05cb9ee073a2722f6b22d8"></a>

### `mspi_op_mode`

```c
enum mspi_op_mode
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 工作模式（Operational mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_OP_MODE_CONTROLLER` |  |
| `MSPI_OP_MODE_PERIPHERAL` |  |

<a id="ga498f10591acf5dc7ec88e0aa98e537d6"></a>

### `mspi_xfer_direction`

```c
enum mspi_xfer_direction
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 传输方向。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_RX` |  |
| `MSPI_TX` |  |

<a id="ga116259bbb1d12a10c2ba9e6051f2f000"></a>

### `mspi_xfer_mode`

```c
enum mspi_xfer_mode
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 传输模式。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_PIO` |  |
| `MSPI_DMA` |  |

<a id="ga632af162124ca2959a21ca3759e1cc9e"></a>

### `mspi_xfer_priority`

```c
enum mspi_xfer_priority
```

```c
#include <zephyr/drivers/mspi.h>
```

MSPI 传输优先级（Priority）。这是通常与 DMA 配合使用的初步优先级列表。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MSPI_XFER_PRIORITY_LOW` |  |
| `MSPI_XFER_PRIORITY_MEDIUM` |  |
| `MSPI_XFER_PRIORITY_HIGH` |  |


## 14.5\_原页交叉引用（Cross References）

- [MSPI 配置 API（MSPI Configure API）](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__configure__api.html)
- [MSPI 设备树相关宏](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__devicetree.html)
- [MSPI 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface__backend.html)
- [MSPI 仿真接口（MSPI Emulation Interface）](../hardware/P487_MSPI总线仿真接口.md)
- [MSPI 传输 API（MSPI Transfer API）](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__transfer__api.html)
- [MSPI 回调 API（MSPI callback API）](../api_protocol_topic_reference/P037_MSPI 回调 API（MSPI callback API）.md)
- [MSPI 工具（Mspi_util）](../api_topic_reference/P053_MSPI 工具（Mspi_util）.md)
- [mspi.h](../peripheral_bus_storage_header_reference/P017_zephyr__drivers__mspi.h_头文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga4cd05950729893e08ef0d4a12e2242d5afb1c2030d871cbbaa4341df7989a5a64"></a>
<a id="gga4cd05950729893e08ef0d4a12e2242d5aeeaf87802ecc90ada4c39f65fc0e8af0"></a>
<a id="gga4cd05950729893e08ef0d4a12e2242d5ad47099019f15f97d83bc6435e5e76a61"></a>
<a id="gga4cd05950729893e08ef0d4a12e2242d5a9c538a902c3e5fa1086c0f0fcee4b7e6"></a>
<a id="gga4cd05950729893e08ef0d4a12e2242d5a325aa40170de5621e89aa2def557f85a"></a>
<a id="ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277"></a>
<a id="ggab33e9840b0937c944f4e1a2525534cb1a63fb981aab764d752c1166fc112094a1"></a>
<a id="ggab33e9840b0937c944f4e1a2525534cb1a5cff8419a9236cc835a62b124debe498"></a>
<a id="ggab33e9840b0937c944f4e1a2525534cb1aa315ad9c5ba56979914b21208920aad7"></a>
<a id="ggab33e9840b0937c944f4e1a2525534cb1af587e68d07441f3262ab164f48e783c0"></a>
<a id="gga283275f86fe186f4b5e30110ae0d506bab36e66d82b05449ed6ce5b6ebc8e2bae"></a>
<a id="gga283275f86fe186f4b5e30110ae0d506ba375e0b870800e0982b3715417e109a22"></a>
<a id="gga704e4d3759d3261b4468e9d9900e578cac1c3516819a027f50941e435f54fba90"></a>
<a id="gga704e4d3759d3261b4468e9d9900e578ca8c93d56778ea1cbf901db1a4b9fee870"></a>
<a id="gga704e4d3759d3261b4468e9d9900e578cabbde8c1ad9a5a8a9a3ca4ce33e2c0705"></a>
<a id="gga704e4d3759d3261b4468e9d9900e578ca415e431b25ac4a12f35b139ccb77ba48"></a>
<a id="ggaa2131d9846bbfd74488a6ae1c2003e68a0e0a4b9bfda5f88df8a2fae13281e5e0"></a>
<a id="ggaa2131d9846bbfd74488a6ae1c2003e68a388bbd530a438507dbfa9208ec1ebf39"></a>
<a id="ggaa2131d9846bbfd74488a6ae1c2003e68a8cea9da4829a0769e3be8b8a32b79984"></a>
<a id="ggaa2131d9846bbfd74488a6ae1c2003e68a96f82a24b684a7debe0ac32070fa53bc"></a>
<a id="ggaa2131d9846bbfd74488a6ae1c2003e68a51f3574f42456a11cc3fcd17c1195dd9"></a>
<a id="gga71c447d059acf7a8055c380243f3a647acc1d59bd6682933d364f060f31f26878"></a>
<a id="gga71c447d059acf7a8055c380243f3a647a4a476e51f0d3613aab1bc9c1b335bab2"></a>
<a id="gga71c447d059acf7a8055c380243f3a647a135b081210bd5aabf5b610fe90212809"></a>
<a id="gga71c447d059acf7a8055c380243f3a647a4aba5c75b43e1a87c66e940069b5b27f"></a>
<a id="gga71c447d059acf7a8055c380243f3a647a0e954604ea419f6a4fdea59e620bdcd9"></a>
<a id="gga71c447d059acf7a8055c380243f3a647a0d7032e045c80ca266e98f8c6684af65"></a>
<a id="gga71c447d059acf7a8055c380243f3a647aba8ef6308b3e06a2ace1cc0f225d66ca"></a>
<a id="gga71c447d059acf7a8055c380243f3a647a51f46405fe8923a8b0c39bc2aad1ba0b"></a>
<a id="gga71c447d059acf7a8055c380243f3a647a56ceb1ba2a93a626623a13f148282537"></a>
<a id="gga71c447d059acf7a8055c380243f3a647a13385127a309507ff01559122e03623a"></a>
<a id="gga71c447d059acf7a8055c380243f3a647a60b857bd38b0cced89462771edccd9f5"></a>
<a id="gga71c447d059acf7a8055c380243f3a647ae7c13ba10174e6f3f90161af69890872"></a>
<a id="gga71c447d059acf7a8055c380243f3a647a99f486fd1f01684ac232d503af1abf2b"></a>
<a id="gga71c447d059acf7a8055c380243f3a647a1a2e21a3cbf0ee42977cc8a43efd3fac"></a>
<a id="gga71c447d059acf7a8055c380243f3a647aa2ba135123fe9c89ce50fd86dfea759b"></a>
<a id="gga71c447d059acf7a8055c380243f3a647ad07911eacaa2bde26a497c391e5c9946"></a>
<a id="gga71c447d059acf7a8055c380243f3a647acdea4576df8e6d7d48cc289305237120"></a>
<a id="gga71c447d059acf7a8055c380243f3a647a67ae821a16a6280aca165ebf67bd2489"></a>
<a id="gga20e348d7a9f1f9b32078a3bf6c4e82b9ac05ddc8ca44f1c70d3c3748e21fe80d3"></a>
<a id="gga20e348d7a9f1f9b32078a3bf6c4e82b9a13a3f16c4273ca6f28671663d0ecf33c"></a>
<a id="gga3625cde1379e66cb66a8cb3803ab2e44acdde9f8c7517e287e2066c394593d345"></a>
<a id="gga3625cde1379e66cb66a8cb3803ab2e44a08e9349361779ce246bb7da6a1f3012d"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5a63cf9def8dea959ebfb0f5f19c9235bd"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5a9826a30dc94c734cdad9f91148cb8673"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5a8225b99a3943f35b1c713af462a2d5da"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5aaee80ab69881b09ec6b85dbaaa9e8663"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5af65a413ec9c72d6c7acf5154a618870a"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5abe9925279cee8433d2b11cc3614c5a5a"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5a1b3112af8589ef5e2493fc6545c4945a"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5ac79eb0c07038226a74411ca211d9b725"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5ac70792100fe11a07c020c9825c1cdfbf"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5a1d6b2be620bf17c4daecad66ba011573"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5a1882d6c9772a1fa1e9e255fe3883d86b"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5ade6a4a01f3281e5331b3e16f1222eb02"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5a49283124787af5787d64c71bf38e3caa"></a>
<a id="gga904dfc1c800fb9832f7c6200f767f9a5a9f726ce3043c03703d48bcdc45edcbdb"></a>
<a id="ggac127ef78c7b66c7eebe03782abf08c40a5e34cb52b8e8475f9457a9cab7a424ed"></a>
<a id="ggac127ef78c7b66c7eebe03782abf08c40aacecd5fab6e2ed50be75d882eaadadd6"></a>
<a id="gga3f211cd81e05cb9ee073a2722f6b22d8a6a862f1d9931725be7789bd982d2937a"></a>
<a id="gga3f211cd81e05cb9ee073a2722f6b22d8a11af11e286399c7e2f1fbcadca44ea83"></a>
<a id="gga498f10591acf5dc7ec88e0aa98e537d6a044160eb569add203f06d963f57d3541"></a>
<a id="gga498f10591acf5dc7ec88e0aa98e537d6a213d4457305ab45d31b9c06ec85d2b8a"></a>
<a id="gga116259bbb1d12a10c2ba9e6051f2f000abea5c6920a3e81fe332c2a76e4d838a1"></a>
<a id="gga116259bbb1d12a10c2ba9e6051f2f000a5a7235fe9c633206906d76d329f623a8"></a>
<a id="gga632af162124ca2959a21ca3759e1cc9ea31222dc35adf9bed70571b9b640aca97"></a>
<a id="gga632af162124ca2959a21ca3759e1cc9ea66753cdf13762a1dd995638ff71544e0"></a>
<a id="gga632af162124ca2959a21ca3759e1cc9ea3004e6ae8226294b669f2207e928f928"></a>

---

[上一章](P013_MMC56X3 API主题.md) · [返回大纲](大纲.md) · [下一章](P015_MTCH9010 API主题.md)
