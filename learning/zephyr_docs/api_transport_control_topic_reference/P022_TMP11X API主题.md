---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-22
title: TMP11X API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_TMP11X API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TMP11X 温度传感器。

<a id="details"></a>

TMP11X 温度传感器。

<a id="header-files"></a>
<a id="files"></a>

## 22.1\_文件（Files）

<a id="r_tmp11x_2Eh"></a>

```c
file tmp11x.h
```

相关声明：[tmp11x.h](../api_file_transfer_device_reference/P010_zephyr__drivers__sensor__tmp11x.h_文件参考.md)。

TMP11X传感器的扩展API头文件（Extended Sensor API Header）。

```c
file tmp11x.h
```

相关声明：[tmp11x.h](../api_file_network_device_reference/P010_zephyr__dt-bindings__sensor__tmp11x.h_文件参考.md)。

the TI TMP11x temperature sensors的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 22.2\_宏定义（Macros）

<a id="r_gabb06ab7fe6ab207f5b9d77521bef218f"></a>

```c
#define EEPROM_TMP11X_SIZE (4 * sizeof(uint16_t))
```

相关声明：[EEPROM_TMP11X_SIZE](#gabb06ab7fe6ab207f5b9d77521bef218f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

TMP11X 的 EEPROM 大小。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 22.3\_枚举（Enumerations）

<a id="r_ga30cbd49ad5c7286d23453ce6f1167ee9"></a>

```c
enum sensor_attribute_tmp_11x { SENSOR_ATTR_TMP11X_ONE_SHOT_MODE = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_TMP11X_SHUTDOWN_MODE , SENSOR_ATTR_TMP11X_CONTINUOUS_CONVERSION_MODE , SENSOR_ATTR_TMP11X_ALERT_PIN_POLARITY , SENSOR_ATTR_TMP11X_ALERT_MODE , SENSOR_ATTR_TMP11X_ALERT_PIN_SELECT }
```

相关声明：[sensor_attribute_tmp_11x](#ga30cbd49ad5c7286d23453ce6f1167ee9)、[SENSOR_ATTR_TMP11X_ONE_SHOT_MODE](#gga30cbd49ad5c7286d23453ce6f1167ee9aeb6e8af036fe3a8081504b62f30fb591)、[SENSOR_ATTR_TMP11X_SHUTDOWN_MODE](#gga30cbd49ad5c7286d23453ce6f1167ee9a423099eda7d8c3cd7e3712bf9b4ce024)、[SENSOR_ATTR_TMP11X_CONTINUOUS_CONVERSION_MODE](#gga30cbd49ad5c7286d23453ce6f1167ee9a001d3256c1daf5275e414bd5a01bd8cb)、[SENSOR_ATTR_TMP11X_ALERT_PIN_POLARITY](#gga30cbd49ad5c7286d23453ce6f1167ee9aef3c616d3680cf5dcaeb11d0d28465bd)、[SENSOR_ATTR_TMP11X_ALERT_MODE](#gga30cbd49ad5c7286d23453ce6f1167ee9a0e9a99d9a93109183c503b50a60319a1)、[SENSOR_ATTR_TMP11X_ALERT_PIN_SELECT](#gga30cbd49ad5c7286d23453ce6f1167ee9a30375a1e76e090266287079e34e13c8c)。

TMP11X 自定义传感器属性（Custom Sensor Attributes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.4\_函数（Functions）

<a id="r_gae08f7c30e516b4b8f36a6ad1883830cf"></a>

```c
int tmp11x_eeprom_read (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[tmp11x_eeprom_read](#gae08f7c30e516b4b8f36a6ad1883830cf)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

从 EEPROM 读取。

<a id="r_gabc253a269051ae0aeec8061a050922c9"></a>

```c
int tmp11x_eeprom_write (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[tmp11x_eeprom_write](#gabc253a269051ae0aeec8061a050922c9)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

写入 EEPROM。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 22.5\_告警引脚支持宏（Alert Pin Support Macros）

<a id="r_ga286fd575f823c225623bf52f4261bf40"></a>

```c
#define TMP11X_ALERT_PIN_ACTIVE_LOW 0
```

相关声明：[TMP11X_ALERT_PIN_ACTIVE_LOW](#ga286fd575f823c225623bf52f4261bf40)。

告警引脚（Alert Pin）低电平有效（Active Low）。

<a id="r_ga8b05849fc60d1cc62233dadded904075"></a>

```c
#define TMP11X_ALERT_PIN_ACTIVE_HIGH 1
```

相关声明：[TMP11X_ALERT_PIN_ACTIVE_HIGH](#ga8b05849fc60d1cc62233dadded904075)。

告警引脚（Alert Pin）高电平有效（Active High）。

<a id="r_ga0edf30bedfa9d2d42dd52ba82b35d843"></a>

```c
#define TMP11X_ALERT_ALERT_MODE 0
```

相关声明：[TMP11X_ALERT_ALERT_MODE](#ga0edf30bedfa9d2d42dd52ba82b35d843)。

告警模式（Alert Mode）。

<a id="r_ga54b218592e9e084aa96b53d14f967f7e"></a>

```c
#define TMP11X_ALERT_THERM_MODE 1
```

相关声明：[TMP11X_ALERT_THERM_MODE](#ga54b218592e9e084aa96b53d14f967f7e)。

温控模式（Therm Mode）。

<a id="r_ga36f645721a0caa9587ca8a609dcba0b9"></a>

```c
#define TMP11X_ALERT_PIN_ALERT_SEL 0
```

相关声明：[TMP11X_ALERT_PIN_ALERT_SEL](#ga36f645721a0caa9587ca8a609dcba0b9)。

告警引脚（Alert Pin）反映告警标志（Alert Flags）的状态。

<a id="r_ga479cb5e12c7685c186911797698be78b"></a>

```c
#define TMP11X_ALERT_PIN_DR_SEL 1
```

相关声明：[TMP11X_ALERT_PIN_DR_SEL](#ga479cb5e12c7685c186911797698be78b)。

告警引脚（Alert Pin）反映数据就绪标志（Data Ready Flag）的状态。

## 22.6\_输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

<a id="r_ga4693b7e433f4dc51f95e11a8934643a9"></a>

```c
#define TMP11X_DT_ODR_15_5_MS 0
```

相关声明：[TMP11X_DT_ODR_15_5_MS](#ga4693b7e433f4dc51f95e11a8934643a9)。

15.5 毫秒（ms）。

<a id="r_ga17cb6c1c3e49a8da2196ae938368ecfb"></a>

```c
#define TMP11X_DT_ODR_125_MS 0x80
```

相关声明：[TMP11X_DT_ODR_125_MS](#ga17cb6c1c3e49a8da2196ae938368ecfb)。

时间：125 ms。

<a id="r_ga1a842507ebce470f3a380e1140021925"></a>

```c
#define TMP11X_DT_ODR_250_MS 0x100
```

相关声明：[TMP11X_DT_ODR_250_MS](#ga1a842507ebce470f3a380e1140021925)。

时间：250 ms。

<a id="r_gaa071b4ad7ac75ed781015b1674bf5edd"></a>

```c
#define TMP11X_DT_ODR_500_MS 0x180
```

相关声明：[TMP11X_DT_ODR_500_MS](#gaa071b4ad7ac75ed781015b1674bf5edd)。

时间：500 ms。

<a id="r_ga7e2ad50b9864468c6f00cccdab608658"></a>

```c
#define TMP11X_DT_ODR_1000_MS 0x200
```

相关声明：[TMP11X_DT_ODR_1000_MS](#ga7e2ad50b9864468c6f00cccdab608658)。

时间：1000 ms。

<a id="r_ga0f64f79e1dbbcb29ae6871380a446ca4"></a>

```c
#define TMP11X_DT_ODR_4000_MS 0x280
```

相关声明：[TMP11X_DT_ODR_4000_MS](#ga0f64f79e1dbbcb29ae6871380a446ca4)。

4000 毫秒（ms）。

<a id="r_ga29b10bb8a1070968983b72627ed4a2b3"></a>

```c
#define TMP11X_DT_ODR_8000_MS 0x300
```

相关声明：[TMP11X_DT_ODR_8000_MS](#ga29b10bb8a1070968983b72627ed4a2b3)。

8000 毫秒（ms）。

<a id="r_ga4f7689b5d4a5b72da402c3edb85f14d8"></a>

```c
#define TMP11X_DT_ODR_16000_MS 0x380
```

相关声明：[TMP11X_DT_ODR_16000_MS](#ga4f7689b5d4a5b72da402c3edb85f14d8)。

16000 毫秒（ms）。

## 22.7\_平均处理／过采样选项（Averaging/Oversampling Options）

设备树（Devicetree）属性 `oversampling` 的取值。

<a id="r_gad0340558552e92935044952ba5d1c2ac"></a>

```c
#define TMP11X_DT_OVERSAMPLING_1 0
```

相关声明：[TMP11X_DT_OVERSAMPLING_1](#gad0340558552e92935044952ba5d1c2ac)。

对 1 次转换取平均（Conversions Averaged）。

<a id="r_ga5f7db14f47703ae89bd066c71d0f8267"></a>

```c
#define TMP11X_DT_OVERSAMPLING_8 0x20
```

相关声明：[TMP11X_DT_OVERSAMPLING_8](#ga5f7db14f47703ae89bd066c71d0f8267)。

对 8 次转换取平均（Conversions Averaged）。

<a id="r_ga74cf0d96ee648e9278e241c9052c868d"></a>

```c
#define TMP11X_DT_OVERSAMPLING_32 0x40
```

相关声明：[TMP11X_DT_OVERSAMPLING_32](#ga74cf0d96ee648e9278e241c9052c868d)。

对 32 次转换取平均（Conversions Averaged）。

<a id="r_ga5736162b8a82a591c95bc40d48c96339"></a>

```c
#define TMP11X_DT_OVERSAMPLING_64 0x60
```

相关声明：[TMP11X_DT_OVERSAMPLING_64](#ga5736162b8a82a591c95bc40d48c96339)。

对 64 次转换取平均（Conversions Averaged）。

## 22.8\_详细说明（Detailed Documentation）

<a id="gabb06ab7fe6ab207f5b9d77521bef218f"></a>

### `EEPROM_TMP11X_SIZE`

```c
#define EEPROM_TMP11X_SIZE (4 * sizeof(uint16_t))
```

```c
#include <zephyr/drivers/sensor/tmp11x.h>
```

TMP11X 的 EEPROM 大小。

<a id="ga0edf30bedfa9d2d42dd52ba82b35d843"></a>

### `TMP11X_ALERT_ALERT_MODE`

```c
#define TMP11X_ALERT_ALERT_MODE 0
```

```c
#include <zephyr/drivers/sensor/tmp11x.h>
```

告警模式（Alert Mode）。

<a id="ga8b05849fc60d1cc62233dadded904075"></a>

### `TMP11X_ALERT_PIN_ACTIVE_HIGH`

```c
#define TMP11X_ALERT_PIN_ACTIVE_HIGH 1
```

```c
#include <zephyr/drivers/sensor/tmp11x.h>
```

告警引脚（Alert Pin）高电平有效（Active High）。

<a id="ga286fd575f823c225623bf52f4261bf40"></a>

### `TMP11X_ALERT_PIN_ACTIVE_LOW`

```c
#define TMP11X_ALERT_PIN_ACTIVE_LOW 0
```

```c
#include <zephyr/drivers/sensor/tmp11x.h>
```

告警引脚（Alert Pin）低电平有效（Active Low）。

<a id="ga36f645721a0caa9587ca8a609dcba0b9"></a>

### `TMP11X_ALERT_PIN_ALERT_SEL`

```c
#define TMP11X_ALERT_PIN_ALERT_SEL 0
```

```c
#include <zephyr/drivers/sensor/tmp11x.h>
```

告警引脚（Alert Pin）反映告警标志（Alert Flags）的状态。

<a id="ga479cb5e12c7685c186911797698be78b"></a>

### `TMP11X_ALERT_PIN_DR_SEL`

```c
#define TMP11X_ALERT_PIN_DR_SEL 1
```

```c
#include <zephyr/drivers/sensor/tmp11x.h>
```

告警引脚（Alert Pin）反映数据就绪标志（Data Ready Flag）的状态。

<a id="ga54b218592e9e084aa96b53d14f967f7e"></a>

### `TMP11X_ALERT_THERM_MODE`

```c
#define TMP11X_ALERT_THERM_MODE 1
```

```c
#include <zephyr/drivers/sensor/tmp11x.h>
```

温控模式（Therm Mode）。

<a id="ga7e2ad50b9864468c6f00cccdab608658"></a>

### `TMP11X_DT_ODR_1000_MS`

```c
#define TMP11X_DT_ODR_1000_MS 0x200
```

```c
#include <zephyr/dt-bindings/sensor/tmp11x.h>
```

时间：1000 ms。

<a id="ga17cb6c1c3e49a8da2196ae938368ecfb"></a>

### `TMP11X_DT_ODR_125_MS`

```c
#define TMP11X_DT_ODR_125_MS 0x80
```

```c
#include <zephyr/dt-bindings/sensor/tmp11x.h>
```

时间：125 ms。

<a id="ga4693b7e433f4dc51f95e11a8934643a9"></a>

### `TMP11X_DT_ODR_15_5_MS`

```c
#define TMP11X_DT_ODR_15_5_MS 0
```

```c
#include <zephyr/dt-bindings/sensor/tmp11x.h>
```

15.5 毫秒（ms）。

<a id="ga4f7689b5d4a5b72da402c3edb85f14d8"></a>

### `TMP11X_DT_ODR_16000_MS`

```c
#define TMP11X_DT_ODR_16000_MS 0x380
```

```c
#include <zephyr/dt-bindings/sensor/tmp11x.h>
```

16000 毫秒（ms）。

<a id="ga1a842507ebce470f3a380e1140021925"></a>

### `TMP11X_DT_ODR_250_MS`

```c
#define TMP11X_DT_ODR_250_MS 0x100
```

```c
#include <zephyr/dt-bindings/sensor/tmp11x.h>
```

时间：250 ms。

<a id="ga0f64f79e1dbbcb29ae6871380a446ca4"></a>

### `TMP11X_DT_ODR_4000_MS`

```c
#define TMP11X_DT_ODR_4000_MS 0x280
```

```c
#include <zephyr/dt-bindings/sensor/tmp11x.h>
```

4000 毫秒（ms）。

<a id="gaa071b4ad7ac75ed781015b1674bf5edd"></a>

### `TMP11X_DT_ODR_500_MS`

```c
#define TMP11X_DT_ODR_500_MS 0x180
```

```c
#include <zephyr/dt-bindings/sensor/tmp11x.h>
```

时间：500 ms。

<a id="ga29b10bb8a1070968983b72627ed4a2b3"></a>

### `TMP11X_DT_ODR_8000_MS`

```c
#define TMP11X_DT_ODR_8000_MS 0x300
```

```c
#include <zephyr/dt-bindings/sensor/tmp11x.h>
```

8000 毫秒（ms）。

<a id="gad0340558552e92935044952ba5d1c2ac"></a>

### `TMP11X_DT_OVERSAMPLING_1`

```c
#define TMP11X_DT_OVERSAMPLING_1 0
```

```c
#include <zephyr/dt-bindings/sensor/tmp11x.h>
```

对 1 次转换取平均（Conversions Averaged）。

<a id="ga74cf0d96ee648e9278e241c9052c868d"></a>

### `TMP11X_DT_OVERSAMPLING_32`

```c
#define TMP11X_DT_OVERSAMPLING_32 0x40
```

```c
#include <zephyr/dt-bindings/sensor/tmp11x.h>
```

对 32 次转换取平均（Conversions Averaged）。

<a id="ga5736162b8a82a591c95bc40d48c96339"></a>

### `TMP11X_DT_OVERSAMPLING_64`

```c
#define TMP11X_DT_OVERSAMPLING_64 0x60
```

```c
#include <zephyr/dt-bindings/sensor/tmp11x.h>
```

对 64 次转换取平均（Conversions Averaged）。

<a id="ga5f7db14f47703ae89bd066c71d0f8267"></a>

### `TMP11X_DT_OVERSAMPLING_8`

```c
#define TMP11X_DT_OVERSAMPLING_8 0x20
```

```c
#include <zephyr/dt-bindings/sensor/tmp11x.h>
```

对 8 次转换取平均（Conversions Averaged）。

<a id="ga30cbd49ad5c7286d23453ce6f1167ee9"></a>

### `sensor_attribute_tmp_11x`

```c
enum sensor_attribute_tmp_11x
```

```c
#include <zephyr/drivers/sensor/tmp11x.h>
```

TMP11X 自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_TMP11X_ONE_SHOT_MODE` | 启用省电／单次采样模式（power saving/one shot mode）。 |
| `SENSOR_ATTR_TMP11X_SHUTDOWN_MODE` | 关闭传感器（Shutdown the Sensor）。 |
| `SENSOR_ATTR_TMP11X_CONTINUOUS_CONVERSION_MODE` | 启用连续转换（Continuous Conversion）。 |
| `SENSOR_ATTR_TMP11X_ALERT_PIN_POLARITY` | 配置告警引脚极性（Alert Pin Polarity）。 |
| `SENSOR_ATTR_TMP11X_ALERT_MODE` | 配置告警模式（Alert Mode）。 |
| `SENSOR_ATTR_TMP11X_ALERT_PIN_SELECT` | 将告警引脚配置为告警（Alert）或数据就绪（DR）模式。 |

<a id="gae08f7c30e516b4b8f36a6ad1883830cf"></a>

### `tmp11x_eeprom_read()`

```c
int tmp11x_eeprom_read ( const struct device * dev, off_t offset, void * data, size_t len )
```

```c
#include <zephyr/drivers/sensor/tmp11x.h>
```

从 EEPROM 读取。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TMP11X 设备（Device）的指针。 |
| `offset` | EEPROM 中的偏移量（Offset）。 |
| `data` | 指向用于存储读取数据的缓冲区（Buffer）的指针。 |
| `len` | 要读取的数据长度（Data Length）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gabc253a269051ae0aeec8061a050922c9"></a>

### `tmp11x_eeprom_write()`

```c
int tmp11x_eeprom_write ( const struct device * dev, off_t offset, const void * data, size_t len )
```

```c
#include <zephyr/drivers/sensor/tmp11x.h>
```

写入 EEPROM。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 TMP11X 设备（Device）的指针。 |
| `offset` | EEPROM 中的偏移量（Offset）。 |
| `data` | 指向要写入的数据（Data）的指针。 |
| `len` | 要写入的数据长度（Data Length）。 |

返回（Returns）：成功时为0，失败时为负错误码。


## 22.9\_原页交叉引用（Cross References）

- [tmp11x.h](../api_file_transfer_device_reference/P010_zephyr__drivers__sensor__tmp11x.h_文件参考.md)
- [tmp11x.h](../api_file_network_device_reference/P010_zephyr__dt-bindings__sensor__tmp11x.h_文件参考.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga30cbd49ad5c7286d23453ce6f1167ee9aeb6e8af036fe3a8081504b62f30fb591"></a>
<a id="gga30cbd49ad5c7286d23453ce6f1167ee9a423099eda7d8c3cd7e3712bf9b4ce024"></a>
<a id="gga30cbd49ad5c7286d23453ce6f1167ee9a001d3256c1daf5275e414bd5a01bd8cb"></a>
<a id="gga30cbd49ad5c7286d23453ce6f1167ee9aef3c616d3680cf5dcaeb11d0d28465bd"></a>
<a id="gga30cbd49ad5c7286d23453ce6f1167ee9a0e9a99d9a93109183c503b50a60319a1"></a>
<a id="gga30cbd49ad5c7286d23453ce6f1167ee9a30375a1e76e090266287079e34e13c8c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P021_SMBus 驱动后端 API.md) · [返回大纲](大纲.md)
