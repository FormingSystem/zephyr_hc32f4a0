---
id: learning.zephyr-docs.api-file-display-chat-reference.page-8
title: zephyr__drivers__sensor__pac194x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2pac194x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_drivers\_\_sensor\_\_pac194x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2pac194x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PAC194x/PAC195x传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

PAC194x/PAC195x传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.1\_枚举（Enumerations）

<a id="r_a119223e5e57d28e8ee975e6f0c627f6d"></a>

```c
enum pac194x_sensor_attribute { SENSOR_ATTR_SAMPLING_FREQUENCY_RAW = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_CHANNEL_ENABLED , SENSOR_ATTR_REFRESH_MODE , SENSOR_ATTR_FORCE_REFRESH_CMD }
```

相关声明：[pac194x_sensor_attribute](#a119223e5e57d28e8ee975e6f0c627f6d)、[SENSOR_ATTR_SAMPLING_FREQUENCY_RAW](#a119223e5e57d28e8ee975e6f0c627f6da5d1a3c0a86875f1ce67f58bede680978)、[SENSOR_ATTR_CHANNEL_ENABLED](#a119223e5e57d28e8ee975e6f0c627f6da639b059f70abf5295cb1a776d2effc35)、[SENSOR_ATTR_REFRESH_MODE](#a119223e5e57d28e8ee975e6f0c627f6da2197461f74e4d431203ed90d53f728af)、[SENSOR_ATTR_FORCE_REFRESH_CMD](#a119223e5e57d28e8ee975e6f0c627f6da5d77ba482c0b209d90a2d3821e0cba0a)。

PAC194x/PAC195x 支持的附加属性（Additional Attributes）。

<a id="r_a5afa72a5a4776bfc5cb1de7ebc34d8b8"></a>

```c
enum pac194x_sensor_attr_refresh_mode { PAC194X_SENSOR_ATTR_REFRESH_MODE_AUTO_NOWAIT = 0 , PAC194X_SENSOR_ATTR_REFRESH_MODE_AUTO_WAIT , PAC194X_SENSOR_ATTR_REFRESH_MODE_MANUAL }
```

相关声明：[pac194x_sensor_attr_refresh_mode](#a5afa72a5a4776bfc5cb1de7ebc34d8b8)、[PAC194X_SENSOR_ATTR_REFRESH_MODE_AUTO_NOWAIT](#a5afa72a5a4776bfc5cb1de7ebc34d8b8a2ad743bc87c2d60cb57b518572f705ef)、[PAC194X_SENSOR_ATTR_REFRESH_MODE_AUTO_WAIT](#a5afa72a5a4776bfc5cb1de7ebc34d8b8aa1138d9659366ce41650feab2667f0e9)、[PAC194X_SENSOR_ATTR_REFRESH_MODE_MANUAL](#a5afa72a5a4776bfc5cb1de7ebc34d8b8a1310e23c91fd6d704fe81976c6b99722)。

PAC194x/PAC195x 的刷新模式（Refresh Modes）。

<a id="r_a9619b72cfd939cc5258190b74dcae45b"></a>

```c
enum pac194x_sensor_attr_force_refresh_cmd { PAC194X_SENSOR_ATTR_FORCE_REFRESH_CMD_SINGLE = 0 , PAC194X_SENSOR_ATTR_FORCE_REFRESH_CMD_ALL }
```

相关声明：[pac194x_sensor_attr_force_refresh_cmd](#a9619b72cfd939cc5258190b74dcae45b)、[PAC194X_SENSOR_ATTR_FORCE_REFRESH_CMD_SINGLE](#a9619b72cfd939cc5258190b74dcae45bacb7d11a1fe0a0cb37914f4cd95ce831c)、[PAC194X_SENSOR_ATTR_FORCE_REFRESH_CMD_ALL](#a9619b72cfd939cc5258190b74dcae45bad23909c12ce704554e7d01b28b8ec90e)。

PAC194x/PAC195x 的刷新命令（Refresh Commands）。

<a id="r_a2b9354bda1109b1ec8aec0ca9186bdb8"></a>

```c
enum pac194x_sensor_channel { PAC194X_CHAN_VBUS1 = SENSOR_CHAN_PRIV_START , PAC194X_CHAN_VBUS2 , PAC194X_CHAN_VBUS3 , PAC194X_CHAN_VBUS4 , PAC194X_CHAN_CURR1 , PAC194X_CHAN_CURR2 , PAC194X_CHAN_CURR3 , PAC194X_CHAN_CURR4 , PAC194X_CHAN_ACC1 , PAC194X_CHAN_ACC2 , PAC194X_CHAN_ACC3 , PAC194X_CHAN_ACC4 , PAC194X_CHAN_ACC1_AVG , PAC194X_CHAN_ACC2_AVG , PAC194X_CHAN_ACC3_AVG , PAC194X_CHAN_ACC4_AVG , PAC194X_CHAN_ACC_COUNT }
```

相关声明：[pac194x_sensor_channel](#a2b9354bda1109b1ec8aec0ca9186bdb8)、[PAC194X_CHAN_VBUS1](#a2b9354bda1109b1ec8aec0ca9186bdb8a7b714424f79c81a3119183fea0ad7bcb)、[PAC194X_CHAN_VBUS2](#a2b9354bda1109b1ec8aec0ca9186bdb8a9931cb81752155124a3124ffd8fd3f77)、[PAC194X_CHAN_VBUS3](#a2b9354bda1109b1ec8aec0ca9186bdb8a3651dcbf7d0262771759842f21fd6f0a)、[PAC194X_CHAN_VBUS4](#a2b9354bda1109b1ec8aec0ca9186bdb8a8639fb10fac0f1a790fdbe04d878ddf8)、[PAC194X_CHAN_CURR1](#a2b9354bda1109b1ec8aec0ca9186bdb8a6605924cab5e13820e5cda6d1039979c)、[PAC194X_CHAN_CURR2](#a2b9354bda1109b1ec8aec0ca9186bdb8a699ee047ecbf816f007481e6b2815c17)、[PAC194X_CHAN_CURR3](#a2b9354bda1109b1ec8aec0ca9186bdb8a26d8b7485f134c7c2443ea03abf86114)、[PAC194X_CHAN_CURR4](#a2b9354bda1109b1ec8aec0ca9186bdb8a82a790a07118384e4febb97ccf9eb9f2)、[PAC194X_CHAN_ACC1](#a2b9354bda1109b1ec8aec0ca9186bdb8a58b5fec061288a124d39d6239b3655c4)、[PAC194X_CHAN_ACC2](#a2b9354bda1109b1ec8aec0ca9186bdb8a394cb086702e3866b95b6dc347331844)、[PAC194X_CHAN_ACC3](#a2b9354bda1109b1ec8aec0ca9186bdb8a13864722afc165c0c0a9115c0c260e7f)、[PAC194X_CHAN_ACC4](#a2b9354bda1109b1ec8aec0ca9186bdb8a410ef24a717418ccc370b832a857f670)、[PAC194X_CHAN_ACC1_AVG](#a2b9354bda1109b1ec8aec0ca9186bdb8add481f935d48cd5ec0e7f4a123027566)、[PAC194X_CHAN_ACC2_AVG](#a2b9354bda1109b1ec8aec0ca9186bdb8ac030c9b9bc87b2d74db3a8d5ac06b7f9)、[PAC194X_CHAN_ACC3_AVG](#a2b9354bda1109b1ec8aec0ca9186bdb8a1cba241c6d61e3ee52299afd2911bbde)、[PAC194X_CHAN_ACC4_AVG](#a2b9354bda1109b1ec8aec0ca9186bdb8a9fd2d197e3221cb7d3c6d51496a7f1ae)、[PAC194X_CHAN_ACC_COUNT](#a2b9354bda1109b1ec8aec0ca9186bdb8a716a9d838bc7d779a8fb18722ac7d8e3)。

PAC194x/PAC195x 支持的附加通道（Additional Channels）。

## 8.2\_详细说明（Detailed Documentation）

<a id="a9619b72cfd939cc5258190b74dcae45b"></a>

### `pac194x_sensor_attr_force_refresh_cmd`

```c
enum pac194x_sensor_attr_force_refresh_cmd
```

PAC194x/PAC195x 的刷新命令（Refresh Commands）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PAC194X_SENSOR_ATTR_FORCE_REFRESH_CMD_SINGLE` | 仅刷新单个 PAC 设备（Refresh a Single Device）。 |
| `PAC194X_SENSOR_ATTR_FORCE_REFRESH_CMD_ALL` | 一次刷新 I2C 总线上的全部 PAC 设备。 |

<a id="a5afa72a5a4776bfc5cb1de7ebc34d8b8"></a>

### `pac194x_sensor_attr_refresh_mode`

```c
enum pac194x_sensor_attr_refresh_mode
```

PAC194x/PAC195x 的刷新模式（Refresh Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PAC194X_SENSOR_ATTR_REFRESH_MODE_AUTO_NOWAIT` | sample_fetch 为非阻塞操作（Non-blocking）。从 ACC 寄存器采集样本后调用刷新（Refresh）。 |
| `PAC194X_SENSOR_ATTR_REFRESH_MODE_AUTO_WAIT` | sample_fetch 为阻塞操作（Blocking）。在采集样本前调用刷新（Refresh），函数至少等待 1 ms，使数据能够被访问。 |
| `PAC194X_SENSOR_ATTR_REFRESH_MODE_MANUAL` | sample_fetch 为非阻塞操作（Non-blocking），不会自动调用刷新（Refresh）。用户负责发送适当的 REFRESH 命令。 |

<a id="a119223e5e57d28e8ee975e6f0c627f6d"></a>

### `pac194x_sensor_attribute`

```c
enum pac194x_sensor_attribute
```

PAC194x/PAC195x 支持的附加属性（Additional Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_SAMPLING_FREQUENCY_RAW` | 以原始格式（RAW Format）表示的采样频率（Sampling Frequency）。 |
| `SENSOR_ATTR_CHANNEL_ENABLED` | 启用／禁用指定通道（Channel）。 |
| `SENSOR_ATTR_REFRESH_MODE` | PAC 刷新模式（Refresh Mode）。 |
| `SENSOR_ATTR_FORCE_REFRESH_CMD` | 命令：强制刷新 PAC 累积数据（Accumulated Data）。 |

<a id="a2b9354bda1109b1ec8aec0ca9186bdb8"></a>

### `pac194x_sensor_channel`

```c
enum pac194x_sensor_channel
```

PAC194x/PAC195x 支持的附加通道（Additional Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PAC194X_CHAN_VBUS1` | 通道 1：电压传感器（Voltage Sensor）。 |
| `PAC194X_CHAN_VBUS2` | 通道 2：电压传感器（Voltage Sensor）。 |
| `PAC194X_CHAN_VBUS3` | 通道 3：电压传感器（Voltage Sensor）。 |
| `PAC194X_CHAN_VBUS4` | 通道 4：电压传感器（Voltage Sensor）。 |
| `PAC194X_CHAN_CURR1` | 通道 1：电流传感器（Current Sensor）。 |
| `PAC194X_CHAN_CURR2` | 通道 2：电流传感器（Current Sensor）。 |
| `PAC194X_CHAN_CURR3` | 通道 3：电流传感器（Current Sensor）。 |
| `PAC194X_CHAN_CURR4` | 通道 4：电流传感器（Current Sensor）。 |
| `PAC194X_CHAN_ACC1` | 通道 1：累加器原始值（Accumulator RAW Value）。 |
| `PAC194X_CHAN_ACC2` | 通道 2：累加器原始值（Accumulator RAW Value）。 |
| `PAC194X_CHAN_ACC3` | 通道 3：累加器原始值（Accumulator RAW Value）。 |
| `PAC194X_CHAN_ACC4` | 通道 4：累加器原始值（Accumulator RAW Value）。 |
| `PAC194X_CHAN_ACC1_AVG` | 通道 1：累加器在 SAMPLE_COUNT 个样本上的平均值（Accumulator AVG Value）。 |
| `PAC194X_CHAN_ACC2_AVG` | 通道 2：累加器在 SAMPLE_COUNT 个样本上的平均值（Accumulator AVG Value）。 |
| `PAC194X_CHAN_ACC3_AVG` | 通道 3：累加器在 SAMPLE_COUNT 个样本上的平均值（Accumulator AVG Value）。 |
| `PAC194X_CHAN_ACC4_AVG` | 通道 4：累加器在 SAMPLE_COUNT 个样本上的平均值（Accumulator AVG Value）。 |
| `PAC194X_CHAN_ACC_COUNT` | 自上次 REFRESH 以来的累加器样本数（Accumulator SAMPLE_COUNT）。 |


## 8.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P181_pac194x.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a9619b72cfd939cc5258190b74dcae45bacb7d11a1fe0a0cb37914f4cd95ce831c"></a>
<a id="a9619b72cfd939cc5258190b74dcae45bad23909c12ce704554e7d01b28b8ec90e"></a>
<a id="a5afa72a5a4776bfc5cb1de7ebc34d8b8a2ad743bc87c2d60cb57b518572f705ef"></a>
<a id="a5afa72a5a4776bfc5cb1de7ebc34d8b8aa1138d9659366ce41650feab2667f0e9"></a>
<a id="a5afa72a5a4776bfc5cb1de7ebc34d8b8a1310e23c91fd6d704fe81976c6b99722"></a>
<a id="a119223e5e57d28e8ee975e6f0c627f6da5d1a3c0a86875f1ce67f58bede680978"></a>
<a id="a119223e5e57d28e8ee975e6f0c627f6da639b059f70abf5295cb1a776d2effc35"></a>
<a id="a119223e5e57d28e8ee975e6f0c627f6da2197461f74e4d431203ed90d53f728af"></a>
<a id="a119223e5e57d28e8ee975e6f0c627f6da5d77ba482c0b209d90a2d3821e0cba0a"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a7b714424f79c81a3119183fea0ad7bcb"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a9931cb81752155124a3124ffd8fd3f77"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a3651dcbf7d0262771759842f21fd6f0a"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a8639fb10fac0f1a790fdbe04d878ddf8"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a6605924cab5e13820e5cda6d1039979c"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a699ee047ecbf816f007481e6b2815c17"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a26d8b7485f134c7c2443ea03abf86114"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a82a790a07118384e4febb97ccf9eb9f2"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a58b5fec061288a124d39d6239b3655c4"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a394cb086702e3866b95b6dc347331844"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a13864722afc165c0c0a9115c0c260e7f"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a410ef24a717418ccc370b832a857f670"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8add481f935d48cd5ec0e7f4a123027566"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8ac030c9b9bc87b2d74db3a8d5ac06b7f9"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a1cba241c6d61e3ee52299afd2911bbde"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a9fd2d197e3221cb7d3c6d51496a7f1ae"></a>
<a id="a2b9354bda1109b1ec8aec0ca9186bdb8a716a9d838bc7d779a8fb18722ac7d8e3"></a>

---

[上一章](P007_zephyr__drivers__sensor__max30009.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__drivers__video.h_文件参考.md)
