---
id: learning.zephyr-docs.api-file-clock-network-reference.page-29
title: zephyr__drivers__sensor__veml7700.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/veml7700_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_drivers\_\_sensor\_\_veml7700.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/veml7700_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 29.1\_宏定义（Macros）

<a id="r_ac67394dec210f9c64ae0f25bc24b2b4d"></a>

```c
#define VEML7700_ALS_GAIN_ELEM_COUNT 4
```

相关声明：[VEML7700_ALS_GAIN_ELEM_COUNT](#ac67394dec210f9c64ae0f25bc24b2b4d)。

enum veml7700_als_gain 中枚举项（Enumerators）的数量。

<a id="r_ab3f2271ebacc28dc6b846f696a26e9c0"></a>

```c
#define VEML7700_ALS_IT_ELEM_COUNT 6
```

相关声明：[VEML7700_ALS_IT_ELEM_COUNT](#ab3f2271ebacc28dc6b846f696a26e9c0)。

enum veml7700_als_it 中枚举项（Enumerators）的数量。

<a id="r_a69af2a92e4e816f269d98e86ffe522b8"></a>

```c
#define VEML7700_ALS_INT_LOW_MASK BIT(15)
```

相关声明：[VEML7700_ALS_INT_LOW_MASK](#a69af2a92e4e816f269d98e86ffe522b8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

检查下阈值中断标志（Low Threshold Interrupt Flag）的位掩码。

<a id="r_a4af944750098802779ef6d018ed1aa7b"></a>

```c
#define VEML7700_ALS_INT_HIGH_MASK BIT(14)
```

相关声明：[VEML7700_ALS_INT_HIGH_MASK](#a4af944750098802779ef6d018ed1aa7b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

检查上阈值中断标志（High Threshold Interrupt Flag）的位掩码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 29.2\_枚举（Enumerations）

<a id="r_ad4a2d50801f3f4d2e1390e6c5dac565d"></a>

```c
enum veml7700_als_gain { VEML7700_ALS_GAIN_1 = 0x00 , VEML7700_ALS_GAIN_2 = 0x01 , VEML7700_ALS_GAIN_1_8 = 0x02 , VEML7700_ALS_GAIN_1_4 = 0x03 }
```

相关声明：[veml7700_als_gain](#ad4a2d50801f3f4d2e1390e6c5dac565d)、[VEML7700_ALS_GAIN_1](#ad4a2d50801f3f4d2e1390e6c5dac565da32ee11119f685ae203e9c69e7246c722)、[VEML7700_ALS_GAIN_2](#ad4a2d50801f3f4d2e1390e6c5dac565da8053068f9d24805ce24f4fcead41bac2)、[VEML7700_ALS_GAIN_1_8](#ad4a2d50801f3f4d2e1390e6c5dac565da9a675080f74e21da950bacd74d3880cb)、[VEML7700_ALS_GAIN_1_4](#ad4a2d50801f3f4d2e1390e6c5dac565da276d18739e9bfe76c5bf91750c051cfd)。

VEML7700 环境光测量（Ambient Light Measurements）的增益选项（Gain Options）。

<a id="r_a0a65ceba1f3f7b25309033a8e6c3384b"></a>

```c
enum veml7700_als_it { VEML7700_ALS_IT_25 , VEML7700_ALS_IT_50 , VEML7700_ALS_IT_100 , VEML7700_ALS_IT_200 , VEML7700_ALS_IT_400 , VEML7700_ALS_IT_800 }
```

相关声明：[veml7700_als_it](#a0a65ceba1f3f7b25309033a8e6c3384b)、[VEML7700_ALS_IT_25](#a0a65ceba1f3f7b25309033a8e6c3384ba59491f48a2563a32c23d87608a5c289a)、[VEML7700_ALS_IT_50](#a0a65ceba1f3f7b25309033a8e6c3384baf7677738fb31f8b76f374ddcb8529c55)、[VEML7700_ALS_IT_100](#a0a65ceba1f3f7b25309033a8e6c3384ba297e6e0e46f719b15e235bdaf312c27c)、[VEML7700_ALS_IT_200](#a0a65ceba1f3f7b25309033a8e6c3384bae52d52519dd988fd096a7e27470d8f65)、[VEML7700_ALS_IT_400](#a0a65ceba1f3f7b25309033a8e6c3384ba7a1da11c0773ef10cd2f0302c2bf0f7a)、[VEML7700_ALS_IT_800](#a0a65ceba1f3f7b25309033a8e6c3384ba8e8c54868774a5bd634b6deba30256c2)。

VEML7700 环境光测量（Ambient Light Measurements）的积分时间选项（Integration Time Options）。

<a id="r_a1f84fa22aa00479b23ada96982aa0146"></a>

```c
enum veml7700_int_mode { VEML7700_INT_DISABLED = 0xFF , VEML7700_ALS_PERS_1 = 0x00 , VEML7700_ALS_PERS_2 = 0x01 , VEML7700_ALS_PERS_4 = 0x02 , VEML7700_ALS_PERS_8 = 0x03 }
```

相关声明：[veml7700_int_mode](#a1f84fa22aa00479b23ada96982aa0146)、[VEML7700_INT_DISABLED](#a1f84fa22aa00479b23ada96982aa0146a81b919fc1c21b8202a76013a8229534f)、[VEML7700_ALS_PERS_1](#a1f84fa22aa00479b23ada96982aa0146a111482232b5fa120313fe9f3beae0f59)、[VEML7700_ALS_PERS_2](#a1f84fa22aa00479b23ada96982aa0146aed9dbc590b13588f802335329b1fef2a)、[VEML7700_ALS_PERS_4](#a1f84fa22aa00479b23ada96982aa0146a5a8ddd8d08092ded93e07ce64f78a9c2)、[VEML7700_ALS_PERS_8](#a1f84fa22aa00479b23ada96982aa0146a01121c07606684416e34746df20334b5)。

VEML7700 环境光（ALS）中断持续性保护计数选项（Persistence Protect Number Options）。

<a id="r_a26c425381bfcb7f264c79d505d900442"></a>

```c
enum sensor_attribute_veml7700 { SENSOR_ATTR_VEML7700_GAIN = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_VEML7700_ITIME , SENSOR_ATTR_VEML7700_INT_MODE }
```

相关声明：[sensor_attribute_veml7700](#a26c425381bfcb7f264c79d505d900442)、[SENSOR_ATTR_VEML7700_GAIN](#a26c425381bfcb7f264c79d505d900442adfd7b70862fbf124dae9404711360bac)、[SENSOR_ATTR_VEML7700_ITIME](#a26c425381bfcb7f264c79d505d900442a0d87dcb30a761c3c9eb1dbd102617153)、[SENSOR_ATTR_VEML7700_INT_MODE](#a26c425381bfcb7f264c79d505d900442a7e1a16c7cfe7c5267e573b683a817b95)。

VEML7700 专用传感器属性（Sensor Attributes）。

<a id="r_a2680058e5ede3f8c76e191e19ef68936"></a>

```c
enum sensor_channel_veml7700 { SENSOR_CHAN_VEML7700_RAW_COUNTS = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_VEML7700_WHITE_RAW_COUNTS , SENSOR_CHAN_VEML7700_INTERRUPT }
```

相关声明：[sensor_channel_veml7700](#a2680058e5ede3f8c76e191e19ef68936)、[SENSOR_CHAN_VEML7700_RAW_COUNTS](#a2680058e5ede3f8c76e191e19ef68936aeb3a68fec9edb12d314f6aba43389421)、[SENSOR_CHAN_VEML7700_WHITE_RAW_COUNTS](#a2680058e5ede3f8c76e191e19ef68936a658e0bf9672adbc81aa80d3fd44b6627)、[SENSOR_CHAN_VEML7700_INTERRUPT](#a2680058e5ede3f8c76e191e19ef68936a059f5aef8916164ccab1c2239e7f2465)。

VEML7700 专用传感器通道（Sensor Channels）。

## 29.3\_详细说明（Detailed Documentation）

<a id="ac67394dec210f9c64ae0f25bc24b2b4d"></a>

### `VEML7700_ALS_GAIN_ELEM_COUNT`

```c
#define VEML7700_ALS_GAIN_ELEM_COUNT 4
```

enum veml7700_als_gain 中枚举项（Enumerators）的数量。

<a id="a4af944750098802779ef6d018ed1aa7b"></a>

### `VEML7700_ALS_INT_HIGH_MASK`

```c
#define VEML7700_ALS_INT_HIGH_MASK BIT(14)
```

检查上阈值中断标志（High Threshold Interrupt Flag）的位掩码。

参见 SENSOR_ATTR_VEML7700_INT_MODE 和 SENSOR_CHAN_VEML7700_INTERRUPT。

<a id="a69af2a92e4e816f269d98e86ffe522b8"></a>

### `VEML7700_ALS_INT_LOW_MASK`

```c
#define VEML7700_ALS_INT_LOW_MASK BIT(15)
```

检查下阈值中断标志（Low Threshold Interrupt Flag）的位掩码。

参见 SENSOR_ATTR_VEML7700_INT_MODE 和 SENSOR_CHAN_VEML7700_INTERRUPT。

<a id="ab3f2271ebacc28dc6b846f696a26e9c0"></a>

### `VEML7700_ALS_IT_ELEM_COUNT`

```c
#define VEML7700_ALS_IT_ELEM_COUNT 6
```

enum veml7700_als_it 中枚举项（Enumerators）的数量。

<a id="a26c425381bfcb7f264c79d505d900442"></a>

### `sensor_attribute_veml7700`

```c
enum sensor_attribute_veml7700
```

VEML7700 专用传感器属性（Sensor Attributes）。

配置阈值窗口上下限（Threshold Window，ALS_WH 和 ALS_WL）时，使用通用属性 SENSOR_ATTR_UPPER_THRESH 和 SENSOR_ATTR_LOWER_THRESH，并提供 16 位无符号整数值。两个阈值均以勒克斯（Lux）为单位，由驱动转换为传感器兼容的值。转换依赖当前增益（Gain）及积分时间（Integration Time）设置，因此改变其中任一项通常需要更新阈值窗口。为向传感器写入正确的阈值，应在改变增益或积分时间之后再更新阈值。

所有属性（Attributes）都必须针对 SENSOR_CHAN_LIGHT 通道设置。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_VEML7700_GAIN` | 环境光测量（ALS Measurements）的增益设置（ALS_GAIN）。属性值使用 enum veml7700_als_gain。 |
| `SENSOR_ATTR_VEML7700_ITIME` | 环境光测量（ALS Measurements）的积分时间设置（ALS_IT）。属性值使用 enum veml7700_als_it。 |
| `SENSOR_ATTR_VEML7700_INT_MODE` | 启用或禁用环境光中断（ALS Interrupt，ALS_INT_EN 和 ALS_PERS）。VEML7700 没有中断引脚（Interrupt Pin），因此此驱动没有实现任何异步通知机制。此类通知需要周期性查询传感器的中断状态，再根据状态触发事件。用户须自行在 SENSOR_CHAN_VEML7700_INTERRUPT 通道上使用 sensor_channel_fetch_chan()，或使用 sensor_channel_fetch()，手动查询中断状态。属性值使用 enum veml7700_int_mode。 |

<a id="a2680058e5ede3f8c76e191e19ef68936"></a>

### `sensor_channel_veml7700`

```c
enum sensor_channel_veml7700
```

VEML7700 专用传感器通道（Sensor Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_VEML7700_RAW_COUNTS` | 原始环境光传感器值通道（Raw ALS Sensor Values）。此通道表示传感器 ALS 寄存器提供的原始测量计数（Raw Measurement Counts），可用于估算处理中断所需的上下阈值窗口属性（Threshold Window Attributes）。不能显式采集此通道。其值通过 SENSOR_CHAN_LIGHT 隐式采集。尝试以此枚举值为参数调用 sensor_channel_fetch_chan() 会返回 -ENOTSUP。 |
| `SENSOR_CHAN_VEML7700_WHITE_RAW_COUNTS` | 白光传感器值通道（White Light Sensor Values）。此通道为传感器的白光通道计数（White Channel Count）输出。白光通道可用于修正 750～800 nm 光谱范围内红外成分较强的光源。 |
| `SENSOR_CHAN_VEML7700_INTERRUPT` | 此通道用于查询环境光中断状态（ALS Interrupt State，ALS_INT）。要让此通道提供有意义的数据，必须通过自定义传感器属性 SENSOR_ATTR_VEML7700_INT_MODE 启用环境光中断模式（ALS Interrupt Mode）。传感器在读取中断状态后会复位该状态。 |

<a id="ad4a2d50801f3f4d2e1390e6c5dac565d"></a>

### `veml7700_als_gain`

```c
enum veml7700_als_gain
```

VEML7700 环境光测量（Ambient Light Measurements）的增益选项（Gain Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VEML7700_ALS_GAIN_1` |  |
| `VEML7700_ALS_GAIN_2` |  |
| `VEML7700_ALS_GAIN_1_8` |  |
| `VEML7700_ALS_GAIN_1_4` |  |

<a id="a0a65ceba1f3f7b25309033a8e6c3384b"></a>

### `veml7700_als_it`

```c
enum veml7700_als_it
```

VEML7700 环境光测量（Ambient Light Measurements）的积分时间选项（Integration Time Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VEML7700_ALS_IT_25` |  |
| `VEML7700_ALS_IT_50` |  |
| `VEML7700_ALS_IT_100` |  |
| `VEML7700_ALS_IT_200` |  |
| `VEML7700_ALS_IT_400` |  |
| `VEML7700_ALS_IT_800` |  |

<a id="a1f84fa22aa00479b23ada96982aa0146"></a>

### `veml7700_int_mode`

```c
enum veml7700_int_mode
```

VEML7700 环境光（ALS）中断持续性保护计数选项（Persistence Protect Number Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VEML7700_INT_DISABLED` |  |
| `VEML7700_ALS_PERS_1` |  |
| `VEML7700_ALS_PERS_2` |  |
| `VEML7700_ALS_PERS_4` |  |
| `VEML7700_ALS_PERS_8` |  |


## 29.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_device_reference/P054_veml7700.h_源码浏览.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SENSOR_ATTR_UPPER_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b)
- [SENSOR_ATTR_LOWER_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa)
- [SENSOR_CHAN_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a26c425381bfcb7f264c79d505d900442adfd7b70862fbf124dae9404711360bac"></a>
<a id="a26c425381bfcb7f264c79d505d900442a0d87dcb30a761c3c9eb1dbd102617153"></a>
<a id="a26c425381bfcb7f264c79d505d900442a7e1a16c7cfe7c5267e573b683a817b95"></a>
<a id="a2680058e5ede3f8c76e191e19ef68936aeb3a68fec9edb12d314f6aba43389421"></a>
<a id="a2680058e5ede3f8c76e191e19ef68936a658e0bf9672adbc81aa80d3fd44b6627"></a>
<a id="a2680058e5ede3f8c76e191e19ef68936a059f5aef8916164ccab1c2239e7f2465"></a>
<a id="ad4a2d50801f3f4d2e1390e6c5dac565da32ee11119f685ae203e9c69e7246c722"></a>
<a id="ad4a2d50801f3f4d2e1390e6c5dac565da8053068f9d24805ce24f4fcead41bac2"></a>
<a id="ad4a2d50801f3f4d2e1390e6c5dac565da9a675080f74e21da950bacd74d3880cb"></a>
<a id="ad4a2d50801f3f4d2e1390e6c5dac565da276d18739e9bfe76c5bf91750c051cfd"></a>
<a id="a0a65ceba1f3f7b25309033a8e6c3384ba59491f48a2563a32c23d87608a5c289a"></a>
<a id="a0a65ceba1f3f7b25309033a8e6c3384baf7677738fb31f8b76f374ddcb8529c55"></a>
<a id="a0a65ceba1f3f7b25309033a8e6c3384ba297e6e0e46f719b15e235bdaf312c27c"></a>
<a id="a0a65ceba1f3f7b25309033a8e6c3384bae52d52519dd988fd096a7e27470d8f65"></a>
<a id="a0a65ceba1f3f7b25309033a8e6c3384ba7a1da11c0773ef10cd2f0302c2bf0f7a"></a>
<a id="a0a65ceba1f3f7b25309033a8e6c3384ba8e8c54868774a5bd634b6deba30256c2"></a>
<a id="a1f84fa22aa00479b23ada96982aa0146a81b919fc1c21b8202a76013a8229534f"></a>
<a id="a1f84fa22aa00479b23ada96982aa0146a111482232b5fa120313fe9f3beae0f59"></a>
<a id="a1f84fa22aa00479b23ada96982aa0146aed9dbc590b13588f802335329b1fef2a"></a>
<a id="a1f84fa22aa00479b23ada96982aa0146a5a8ddd8d08092ded93e07ce64f78a9c2"></a>
<a id="a1f84fa22aa00479b23ada96982aa0146a01121c07606684416e34746df20334b5"></a>

---

[上一章](P028_zephyr__bluetooth__audio__vcp.h_文件参考.md) · [返回大纲](大纲.md)
