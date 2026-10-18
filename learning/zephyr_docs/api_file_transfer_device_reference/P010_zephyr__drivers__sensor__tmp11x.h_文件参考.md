---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-10
title: zephyr__drivers__sensor__tmp11x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2tmp11x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_drivers\_\_sensor\_\_tmp11x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2tmp11x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TMP11X传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/sensor.h>
#include <sys/types.h>
```

查看此文件的源码。

TMP11X传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="r_gabb06ab7fe6ab207f5b9d77521bef218f"></a>

```c
#define EEPROM_TMP11X_SIZE (4 * sizeof(uint16_t))
```

相关声明：[EEPROM_TMP11X_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gabb06ab7fe6ab207f5b9d77521bef218f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

TMP11X 的 EEPROM 大小。

<a id="define-members-0"></a>

### 告警引脚支持宏（Alert Pin Support Macros）

<a id="r_ga286fd575f823c225623bf52f4261bf40"></a>

```c
#define TMP11X_ALERT_PIN_ACTIVE_LOW 0
```

相关声明：[TMP11X_ALERT_PIN_ACTIVE_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga286fd575f823c225623bf52f4261bf40)。

告警引脚（Alert Pin）低电平有效（Active Low）。

<a id="r_ga8b05849fc60d1cc62233dadded904075"></a>

```c
#define TMP11X_ALERT_PIN_ACTIVE_HIGH 1
```

相关声明：[TMP11X_ALERT_PIN_ACTIVE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga8b05849fc60d1cc62233dadded904075)。

告警引脚（Alert Pin）高电平有效（Active High）。

<a id="r_ga0edf30bedfa9d2d42dd52ba82b35d843"></a>

```c
#define TMP11X_ALERT_ALERT_MODE 0
```

相关声明：[TMP11X_ALERT_ALERT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga0edf30bedfa9d2d42dd52ba82b35d843)。

告警模式（Alert Mode）。

<a id="r_ga54b218592e9e084aa96b53d14f967f7e"></a>

```c
#define TMP11X_ALERT_THERM_MODE 1
```

相关声明：[TMP11X_ALERT_THERM_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga54b218592e9e084aa96b53d14f967f7e)。

温控模式（Therm Mode）。

<a id="r_ga36f645721a0caa9587ca8a609dcba0b9"></a>

```c
#define TMP11X_ALERT_PIN_ALERT_SEL 0
```

相关声明：[TMP11X_ALERT_PIN_ALERT_SEL](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga36f645721a0caa9587ca8a609dcba0b9)。

告警引脚（Alert Pin）反映告警标志（Alert Flags）的状态。

<a id="r_ga479cb5e12c7685c186911797698be78b"></a>

```c
#define TMP11X_ALERT_PIN_DR_SEL 1
```

相关声明：[TMP11X_ALERT_PIN_DR_SEL](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga479cb5e12c7685c186911797698be78b)。

告警引脚（Alert Pin）反映数据就绪标志（Data Ready Flag）的状态。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.2\_枚举（Enumerations）

<a id="r_ga30cbd49ad5c7286d23453ce6f1167ee9"></a>

```c
enum sensor_attribute_tmp_11x { SENSOR_ATTR_TMP11X_ONE_SHOT_MODE = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_TMP11X_SHUTDOWN_MODE , SENSOR_ATTR_TMP11X_CONTINUOUS_CONVERSION_MODE , SENSOR_ATTR_TMP11X_ALERT_PIN_POLARITY , SENSOR_ATTR_TMP11X_ALERT_MODE , SENSOR_ATTR_TMP11X_ALERT_PIN_SELECT }
```

相关声明：[sensor_attribute_tmp_11x](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga30cbd49ad5c7286d23453ce6f1167ee9)、[SENSOR_ATTR_TMP11X_ONE_SHOT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gga30cbd49ad5c7286d23453ce6f1167ee9aeb6e8af036fe3a8081504b62f30fb591)、[SENSOR_ATTR_TMP11X_SHUTDOWN_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gga30cbd49ad5c7286d23453ce6f1167ee9a423099eda7d8c3cd7e3712bf9b4ce024)、[SENSOR_ATTR_TMP11X_CONTINUOUS_CONVERSION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gga30cbd49ad5c7286d23453ce6f1167ee9a001d3256c1daf5275e414bd5a01bd8cb)、[SENSOR_ATTR_TMP11X_ALERT_PIN_POLARITY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gga30cbd49ad5c7286d23453ce6f1167ee9aef3c616d3680cf5dcaeb11d0d28465bd)、[SENSOR_ATTR_TMP11X_ALERT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gga30cbd49ad5c7286d23453ce6f1167ee9a0e9a99d9a93109183c503b50a60319a1)、[SENSOR_ATTR_TMP11X_ALERT_PIN_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gga30cbd49ad5c7286d23453ce6f1167ee9a30375a1e76e090266287079e34e13c8c)。

TMP11X 自定义传感器属性（Custom Sensor Attributes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.3\_函数（Functions）

<a id="r_gae08f7c30e516b4b8f36a6ad1883830cf"></a>

```c
int tmp11x_eeprom_read (const struct device *dev, off_t offset, void *data, size_t len)
```

相关声明：[tmp11x_eeprom_read](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gae08f7c30e516b4b8f36a6ad1883830cf)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

从 EEPROM 读取。

<a id="r_gabc253a269051ae0aeec8061a050922c9"></a>

```c
int tmp11x_eeprom_write (const struct device *dev, off_t offset, const void *data, size_t len)
```

相关声明：[tmp11x_eeprom_write](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gabc253a269051ae0aeec8061a050922c9)、[device](../device_reference/P002_设备对象结构.md)、[off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)。

写入 EEPROM。


## 10.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P182_tmp11x.h_源码浏览.md)
- [EEPROM_TMP11X_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gabb06ab7fe6ab207f5b9d77521bef218f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [TMP11X_ALERT_PIN_ACTIVE_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga286fd575f823c225623bf52f4261bf40)
- [TMP11X_ALERT_PIN_ACTIVE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga8b05849fc60d1cc62233dadded904075)
- [TMP11X_ALERT_ALERT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga0edf30bedfa9d2d42dd52ba82b35d843)
- [TMP11X_ALERT_THERM_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga54b218592e9e084aa96b53d14f967f7e)
- [TMP11X_ALERT_PIN_ALERT_SEL](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga36f645721a0caa9587ca8a609dcba0b9)
- [TMP11X_ALERT_PIN_DR_SEL](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga479cb5e12c7685c186911797698be78b)
- [sensor_attribute_tmp_11x](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#ga30cbd49ad5c7286d23453ce6f1167ee9)
- [SENSOR_ATTR_TMP11X_ONE_SHOT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gga30cbd49ad5c7286d23453ce6f1167ee9aeb6e8af036fe3a8081504b62f30fb591)
- [SENSOR_ATTR_TMP11X_SHUTDOWN_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gga30cbd49ad5c7286d23453ce6f1167ee9a423099eda7d8c3cd7e3712bf9b4ce024)
- [SENSOR_ATTR_TMP11X_CONTINUOUS_CONVERSION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gga30cbd49ad5c7286d23453ce6f1167ee9a001d3256c1daf5275e414bd5a01bd8cb)
- [SENSOR_ATTR_TMP11X_ALERT_PIN_POLARITY](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gga30cbd49ad5c7286d23453ce6f1167ee9aef3c616d3680cf5dcaeb11d0d28465bd)
- [SENSOR_ATTR_TMP11X_ALERT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gga30cbd49ad5c7286d23453ce6f1167ee9a0e9a99d9a93109183c503b50a60319a1)
- [SENSOR_ATTR_TMP11X_ALERT_PIN_SELECT](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gga30cbd49ad5c7286d23453ce6f1167ee9a30375a1e76e090266287079e34e13c8c)
- [tmp11x_eeprom_read](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gae08f7c30e516b4b8f36a6ad1883830cf)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a98a5cc5f4a350bf5652565021a2f239f)
- [tmp11x_eeprom_write](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp11x__interface.html#gabc253a269051ae0aeec8061a050922c9)

<a id="header-details"></a>

---

[上一章](P009_zephyr__drivers__sensor__icm566xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__drivers__mfd__ds3231.h_文件参考.md)
