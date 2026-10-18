---
id: learning.zephyr-docs.api-file-secure-value-reference.page-7
title: zephyr__drivers__sensor__adxl355.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2adxl355_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_sensor\_\_adxl355.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2adxl355_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ADXL355传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

查看此文件的源码。

ADXL355传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.1\_枚举（Enumerations）

<a id="r_ad190bda5a5b7f000f18217e440dec339"></a>

```c
enum sensor_attribute_adxl355 { SENSOR_ATTR_ADXL355_FIFO_WATERMARK = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_ADXL355_HPF_CORNER , SENSOR_ATTR_ADXL355_EXT_CLK , SENSOR_ATTR_ADXL355_EXT_SYNC , SENSOR_ATTR_ADXL355_I2C_HS , SENSOR_ATTR_ADXL355_INT_POL , SENSOR_ATTR_ADXL355_ACTIVITY_THRESHOLD , SENSOR_ATTR_ADXL355_ACTIVITY_COUNT , SENSOR_ATTR_ADXL355_ACTIVITY_ENABLE_X , SENSOR_ATTR_ADXL355_ACTIVITY_ENABLE_Y , SENSOR_ATTR_ADXL355_ACTIVITY_ENABLE_Z }
```

相关声明：[sensor_attribute_adxl355](#ad190bda5a5b7f000f18217e440dec339)、[SENSOR_ATTR_ADXL355_FIFO_WATERMARK](#ad190bda5a5b7f000f18217e440dec339a29ab68b2e0a9d5da8f199f4230aa2da4)、[SENSOR_ATTR_ADXL355_HPF_CORNER](#ad190bda5a5b7f000f18217e440dec339aa6e09fcf2e1d9246131fb073102f2910)、[SENSOR_ATTR_ADXL355_EXT_CLK](#ad190bda5a5b7f000f18217e440dec339aca592c0fb22cdbcaee3dd2430a89b86a)、[SENSOR_ATTR_ADXL355_EXT_SYNC](#ad190bda5a5b7f000f18217e440dec339a31382cdfb0c8bdd53d751963369f6513)、[SENSOR_ATTR_ADXL355_I2C_HS](#ad190bda5a5b7f000f18217e440dec339a3019a85f1b9140183b0828bce880e135)、[SENSOR_ATTR_ADXL355_INT_POL](#ad190bda5a5b7f000f18217e440dec339aa360b397ff2481990de5539a57d1d5b1)、[SENSOR_ATTR_ADXL355_ACTIVITY_THRESHOLD](#ad190bda5a5b7f000f18217e440dec339ab36a1a7882eab44068415987cdd9cba0)、[SENSOR_ATTR_ADXL355_ACTIVITY_COUNT](#ad190bda5a5b7f000f18217e440dec339a2995af56d1ef452dd42af8067f1adabb)、[SENSOR_ATTR_ADXL355_ACTIVITY_ENABLE_X](#ad190bda5a5b7f000f18217e440dec339aa1bf3df312ad99dda6ab287e9721d204)、[SENSOR_ATTR_ADXL355_ACTIVITY_ENABLE_Y](#ad190bda5a5b7f000f18217e440dec339aaf4d32dbdcde408a509b34879b5dcd9d)、[SENSOR_ATTR_ADXL355_ACTIVITY_ENABLE_Z](#ad190bda5a5b7f000f18217e440dec339ae231fca40be03b9c58ac2d3478613be0)。

ADXL355 专用传感器属性（Sensor Attributes）。

<a id="r_a6498239a85e4c619fb5528cadad96971"></a>

```c
enum adxl355_hpf_corner { ADXL355_HPF_OFF = 0 , ADXL355_HPF_24_7e_4 , ADXL355_HPF_6_208e_4 , ADXL355_HPF_1_5545e_4 , ADXL355_HPF_0_3862e_4 , ADXL355_HPF_0_0954e_4 , ADXL355_HPF_0_0238e_4 }
```

相关声明：[adxl355_hpf_corner](#a6498239a85e4c619fb5528cadad96971)、[ADXL355_HPF_OFF](#a6498239a85e4c619fb5528cadad96971a99bdaed9763b2c657b82e54541bba6e8)、[ADXL355_HPF_24_7e_4](#a6498239a85e4c619fb5528cadad96971aaa3b1f4d2bc701cb1a4f0b4b35d84ddb)、[ADXL355_HPF_6_208e_4](#a6498239a85e4c619fb5528cadad96971af5d79bd4e1b5ae046779bc68e4babb9d)、[ADXL355_HPF_1_5545e_4](#a6498239a85e4c619fb5528cadad96971a1b6ffbf7871d7038a78121d9420426b6)、[ADXL355_HPF_0_3862e_4](#a6498239a85e4c619fb5528cadad96971a0f2746f5506b676c9f69b671fb0a3429)、[ADXL355_HPF_0_0954e_4](#a6498239a85e4c619fb5528cadad96971a6eab109143243d22a2f7d4d46e9f6a5f)、[ADXL355_HPF_0_0238e_4](#a6498239a85e4c619fb5528cadad96971aee4bd287abcace67b08c9c661319a324)。

ADXL355 高通滤波器截止频率选项（High Pass Filter Corner Frequency Options）。

## 7.2\_详细说明（Detailed Documentation）

<a id="a6498239a85e4c619fb5528cadad96971"></a>

### `adxl355_hpf_corner`

```c
enum adxl355_hpf_corner
```

ADXL355 高通滤波器截止频率选项（High Pass Filter Corner Frequency Options）。

这些选项对应设备树（DT）绑定中的高通滤波器（HPF）截止频率设置值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ADXL355_HPF_OFF` | 高通滤波器（High-pass Filter）禁用。 |
| `ADXL355_HPF_24_7e_4` | 高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 24.7e-4 倍。 |
| `ADXL355_HPF_6_208e_4` | 高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 6.208e-4 倍。 |
| `ADXL355_HPF_1_5545e_4` | 高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 1.5545e-4 倍。 |
| `ADXL355_HPF_0_3862e_4` | 高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 0.3862e-4 倍。 |
| `ADXL355_HPF_0_0954e_4` | 高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 0.0954e-4 倍。 |
| `ADXL355_HPF_0_0238e_4` | 高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 0.0238e-4 倍。 |

<a id="ad190bda5a5b7f000f18217e440dec339"></a>

### `sensor_attribute_adxl355`

```c
enum sensor_attribute_adxl355
```

ADXL355 专用传感器属性（Sensor Attributes）。

这些属性扩展标准 `sensor_attribute` 枚举，以支持 ADXL355 专用配置选项（Configuration Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_ADXL355_FIFO_WATERMARK` | 先进先出缓冲区水位（FIFO Watermark Level）。 |
| `SENSOR_ATTR_ADXL355_HPF_CORNER` | 高通滤波器截止频率（Highpass Filter Corner）。 |
| `SENSOR_ATTR_ADXL355_EXT_CLK` | 外部时钟设置（External Clock Setting）。 |
| `SENSOR_ATTR_ADXL355_EXT_SYNC` | 外部同步设置（External Sync Setting）。 |
| `SENSOR_ATTR_ADXL355_I2C_HS` | I2C 高速模式（High Speed Mode）。 |
| `SENSOR_ATTR_ADXL355_INT_POL` | 中断极性（Interrupt Polarity）。 |
| `SENSOR_ATTR_ADXL355_ACTIVITY_THRESHOLD` | 活动检测阈值（Activity Threshold）。 |
| `SENSOR_ATTR_ADXL355_ACTIVITY_COUNT` | 活动检测计数（Activity Count）。 |
| `SENSOR_ATTR_ADXL355_ACTIVITY_ENABLE_X` | X 轴活动检测使能（Activity Enable）。 |
| `SENSOR_ATTR_ADXL355_ACTIVITY_ENABLE_Y` | Y 轴活动检测使能（Activity Enable）。 |
| `SENSOR_ATTR_ADXL355_ACTIVITY_ENABLE_Z` | Z 轴活动检测使能（Activity Enable）。 |


## 7.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [zephyr/dt-bindings/sensor/adxl355.h](../api_source_reference/P201_adxl355.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P172_adxl355.h_源码浏览.md)
- [sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a6498239a85e4c619fb5528cadad96971a99bdaed9763b2c657b82e54541bba6e8"></a>
<a id="a6498239a85e4c619fb5528cadad96971aaa3b1f4d2bc701cb1a4f0b4b35d84ddb"></a>
<a id="a6498239a85e4c619fb5528cadad96971af5d79bd4e1b5ae046779bc68e4babb9d"></a>
<a id="a6498239a85e4c619fb5528cadad96971a1b6ffbf7871d7038a78121d9420426b6"></a>
<a id="a6498239a85e4c619fb5528cadad96971a0f2746f5506b676c9f69b671fb0a3429"></a>
<a id="a6498239a85e4c619fb5528cadad96971a6eab109143243d22a2f7d4d46e9f6a5f"></a>
<a id="a6498239a85e4c619fb5528cadad96971aee4bd287abcace67b08c9c661319a324"></a>
<a id="ad190bda5a5b7f000f18217e440dec339a29ab68b2e0a9d5da8f199f4230aa2da4"></a>
<a id="ad190bda5a5b7f000f18217e440dec339aa6e09fcf2e1d9246131fb073102f2910"></a>
<a id="ad190bda5a5b7f000f18217e440dec339aca592c0fb22cdbcaee3dd2430a89b86a"></a>
<a id="ad190bda5a5b7f000f18217e440dec339a31382cdfb0c8bdd53d751963369f6513"></a>
<a id="ad190bda5a5b7f000f18217e440dec339a3019a85f1b9140183b0828bce880e135"></a>
<a id="ad190bda5a5b7f000f18217e440dec339aa360b397ff2481990de5539a57d1d5b1"></a>
<a id="ad190bda5a5b7f000f18217e440dec339ab36a1a7882eab44068415987cdd9cba0"></a>
<a id="ad190bda5a5b7f000f18217e440dec339a2995af56d1ef452dd42af8067f1adabb"></a>
<a id="ad190bda5a5b7f000f18217e440dec339aa1bf3df312ad99dda6ab287e9721d204"></a>
<a id="ad190bda5a5b7f000f18217e440dec339aaf4d32dbdcde408a509b34879b5dcd9d"></a>
<a id="ad190bda5a5b7f000f18217e440dec339ae231fca40be03b9c58ac2d3478613be0"></a>

---

[上一章](P006_zephyr__drivers__regulator__max20362.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__authentication__fido2__fido2_transport.h_文件参考.md)
