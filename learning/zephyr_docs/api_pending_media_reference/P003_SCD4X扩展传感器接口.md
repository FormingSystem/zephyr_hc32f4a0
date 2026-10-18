---
id: learning.zephyr-docs.api-pending-media-reference.page-3
title: SCD4X扩展传感器接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_SCD4X扩展传感器接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

> 译注：本页正文已译完，但下列原始图片文件仍未取得，完整交付状态保持待完成。原始地址保留在文末[缺失媒体清单](../MISSING_MEDIA.md)。 本页公式直接采用官方 HTML 图片替代文本（alt）中的 LaTeX 排版；它不代表已经下载到原始 PNG，也不是对原图的重绘。原始 alt、公式和文件地址见[公式来源记录](formula-sources.json)。

Sensirion SCD4X 二氧化碳（CO2）传感器。

<a id="details"></a>

Sensirion SCD4X 二氧化碳（CO2）传感器。

<a id="header-files"></a>
<a id="files"></a>

## 3.1\_文件（Files）

<a id="r_scd4x_2Eh"></a>

```c
file scd4x.h
```

相关声明：[scd4x.h](../api_file_service_reference/P048_zephyr__drivers__sensor__scd4x.h_文件参考.md)。

SCD4X传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.2\_枚举（Enumerations）

<a id="r_ga8cbb7f3f4cad13f36cd454073e9d344d"></a>

```c
enum sensor_attribute_scd4x { SENSOR_ATTR_SCD4X_TEMPERATURE_OFFSET = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_SCD4X_SENSOR_ALTITUDE , SENSOR_ATTR_SCD4X_AMBIENT_PRESSURE , SENSOR_ATTR_SCD4X_AUTOMATIC_CALIB_ENABLE , SENSOR_ATTR_SCD4X_SELF_CALIB_INITIAL_PERIOD , SENSOR_ATTR_SCD4X_SELF_CALIB_STANDARD_PERIOD }
```

相关声明：[sensor_attribute_scd4x](#ga8cbb7f3f4cad13f36cd454073e9d344d)、[SENSOR_ATTR_SCD4X_TEMPERATURE_OFFSET](#gga8cbb7f3f4cad13f36cd454073e9d344daa8c54289d95f79519831458018ccb4ba)、[SENSOR_ATTR_SCD4X_SENSOR_ALTITUDE](#gga8cbb7f3f4cad13f36cd454073e9d344dac2697f0466ec1822fbfe82e7b5d6287e)、[SENSOR_ATTR_SCD4X_AMBIENT_PRESSURE](#gga8cbb7f3f4cad13f36cd454073e9d344daa6a806666dcb476b83c1affb15c2964c)、[SENSOR_ATTR_SCD4X_AUTOMATIC_CALIB_ENABLE](#gga8cbb7f3f4cad13f36cd454073e9d344dae61b7281c3d3135bc1557e970d6b2b14)、[SENSOR_ATTR_SCD4X_SELF_CALIB_INITIAL_PERIOD](#gga8cbb7f3f4cad13f36cd454073e9d344da8dccaa05552bbc5b9c474cbaa65ed7b0)、[SENSOR_ATTR_SCD4X_SELF_CALIB_STANDARD_PERIOD](#gga8cbb7f3f4cad13f36cd454073e9d344dac54720c5cb0dce105986b8b6c7b0ea8a)。

SCD4X 的自定义传感器属性（Custom Sensor Attributes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.3\_函数（Functions）

<a id="r_ga9c7260e275f85836ea717186ff8aa796"></a>

```c
int scd4x_forced_recalibration (const struct device *dev, uint16_t target_concentration, uint16_t *frc_correction)
```

相关声明：[scd4x_forced_recalibration](#ga9c7260e275f85836ea717186ff8aa796)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

执行强制重新校准（Forced Recalibration）。

<a id="r_ga076766c7322d9b050acf5963ceba718a"></a>

```c
int scd4x_self_test (const struct device *dev)
```

相关声明：[scd4x_self_test](#ga076766c7322d9b050acf5963ceba718a)、[device](../device_reference/P002_设备对象结构.md)。

执行自检（Self Test）。

<a id="r_ga91f055d3b7a4c8c70c30982cf0ceff9c"></a>

```c
int scd4x_persist_settings (const struct device *dev)
```

相关声明：[scd4x_persist_settings](#ga91f055d3b7a4c8c70c30982cf0ceff9c)、[device](../device_reference/P002_设备对象结构.md)。

执行自检（Self Test）。

<a id="r_gaa501b89af4dbed0dc9be5d1bc1742c99"></a>

```c
int scd4x_factory_reset (const struct device *dev)
```

相关声明：[scd4x_factory_reset](#gaa501b89af4dbed0dc9be5d1bc1742c99)、[device](../device_reference/P002_设备对象结构.md)。

执行出厂复位（Factory Reset）。

## 3.4\_详细说明（Detailed Documentation）

<a id="ga8cbb7f3f4cad13f36cd454073e9d344d"></a>

### `sensor_attribute_scd4x`

```c
enum sensor_attribute_scd4x
```

```c
#include <zephyr/drivers/sensor/scd4x.h>
```

SCD4X 的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_SCD4X_TEMPERATURE_OFFSET` | 温度偏移（Temperature Offset），范围为 0–20 °C。 |
| `SENSOR_ATTR_SCD4X_SENSOR_ALTITUDE` | 传感器海拔高度（Altitude），范围为 0–3000 m。 |
| `SENSOR_ATTR_SCD4X_AMBIENT_PRESSURE` | 环境气压（Ambient Pressure），单位为 hPa，范围为 700–1200 hPa。 |
| `SENSOR_ATTR_SCD4X_AUTOMATIC_CALIB_ENABLE` | 自动校准使能（Automatic Calibration Enable）：1 为启用，0 为禁用；默认启用。 |
| `SENSOR_ATTR_SCD4X_SELF_CALIB_INITIAL_PERIOD` | 自动自校准修正（Automatic Self Calibration Correction）的初始周期，单位为小时。允许值为 4 小时的整数倍，默认值为 44。 |
| `SENSOR_ATTR_SCD4X_SELF_CALIB_STANDARD_PERIOD` | 自动自校准修正（Automatic Self Calibration Correction）的标准周期，单位为小时。允许值为 4 小时的整数倍，默认值为 156。 |

**SENSOR_ATTR_SCD4X_TEMPERATURE_OFFSET 的原始公式：**

$$
T_{offset\_actual} = T_{scd4x} - T_{reference} + T_{offset\_previous}
$$


<a id="gaa501b89af4dbed0dc9be5d1bc1742c99"></a>

### `scd4x_factory_reset()`

```c
int scd4x_factory_reset ( const struct device * dev)
```

```c
#include <zephyr/drivers/sensor/scd4x.h>
```

执行出厂复位（Factory Reset）。

`perform_factory_reset` 命令重置电可擦可编程只读存储器（EEPROM）中保存的全部配置设置，并清除强制重新校准（FRC）和自动自校准（ASC）算法历史记录。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga9c7260e275f85836ea717186ff8aa796"></a>

### `scd4x_forced_recalibration()`

```c
int scd4x_forced_recalibration ( const struct device * dev, uint16_t target_concentration, uint16_t * frc_correction )
```

```c
#include <zephyr/drivers/sensor/scd4x.h>
```

执行强制重新校准（Forced Recalibration）。

在二氧化碳（CO2）浓度均匀且恒定的环境中，使 SCD4x 在工作模式下运行至少 3 分钟，否则重新校准（Recalibration）会失败。执行强制重新校准（FRC）序列时，传感器必须使用应用所需的工作电压。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `target_concentration` | 参考二氧化碳浓度（Reference CO2 Concentration）。 |
| `frc_correction` | 此前相对于目标浓度的差值（Previous Differences）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga91f055d3b7a4c8c70c30982cf0ceff9c"></a>

### `scd4x_persist_settings()`

> 译注：原页此函数的简述写作“执行自检”，而详细说明介绍配置持久保存；此处分别保留原文，不将它改写成 `scd4x_self_test()`。

```c
int scd4x_persist_settings ( const struct device * dev)
```

```c
#include <zephyr/drivers/sensor/scd4x.h>
```

执行自检（Self Test）。

可使用 `persist_settings` 命令保存当前配置。只有在确实需要持久保存（Persistence），并且实际修改了配置时，才应发送此命令。EEPROM 保证至少可承受 2000 次写入周期（Write Cycles）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga076766c7322d9b050acf5963ceba718a"></a>

### `scd4x_self_test()`

```c
int scd4x_self_test ( const struct device * dev)
```

```c
#include <zephyr/drivers/sensor/scd4x.h>
```

执行自检（Self Test）。

`self_test` 命令可用作生产线末端测试（End-of-line Test），检查传感器功能。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。


## 3.5\_原页交叉引用（Cross References）

- [scd4x.h](../api_file_service_reference/P048_zephyr__drivers__sensor__scd4x.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8cbb7f3f4cad13f36cd454073e9d344daa8c54289d95f79519831458018ccb4ba"></a>
<a id="gga8cbb7f3f4cad13f36cd454073e9d344dac2697f0466ec1822fbfe82e7b5d6287e"></a>
<a id="gga8cbb7f3f4cad13f36cd454073e9d344daa6a806666dcb476b83c1affb15c2964c"></a>
<a id="gga8cbb7f3f4cad13f36cd454073e9d344dae61b7281c3d3135bc1557e970d6b2b14"></a>
<a id="gga8cbb7f3f4cad13f36cd454073e9d344da8dccaa05552bbc5b9c474cbaa65ed7b0"></a>
<a id="gga8cbb7f3f4cad13f36cd454073e9d344dac54720c5cb0dce105986b8b6c7b0ea8a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

## 原图文件缺项

- [form_0.png](https://docs.zephyrproject.org/latest/doxygen/html/form_0.png)：原件尚未取得。


---

[上一章](P002_BMP581扩展传感器接口.md) · [返回大纲](大纲.md)
