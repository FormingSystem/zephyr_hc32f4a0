---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-18
title: zephyr__drivers__sensor__grow_r502a.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/grow__r502a_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_drivers\_\_sensor\_\_grow\_r502a.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/grow__r502a_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Grow R502A传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

Grow R502A传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.1\_数据结构（Data Structures）

<a id="r_r502a_5Fsys_5Fparam"></a>

```c
struct r502a_sys_param
```

相关声明：[r502a_sys_param](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md)。

系统参数（System Parameter）。

<a id="r_r502a_5Ftemplate"></a>

```c
struct r502a_template
```

相关声明：[r502a_template](../sensor_navigation_model_reference/P023_r502a_template_结构体.md)。

指纹模板（Fingerprint Template）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 波特率（Baud Rates）

<a id="r_gaaab815dc7de2a1ff5596ad6fdc1e28c2"></a>

```c
#define R502A_BAUD_9600 1
```

相关声明：[R502A_BAUD_9600](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gaaab815dc7de2a1ff5596ad6fdc1e28c2)。

9600 比特每秒（bps）。

<a id="r_ga102611233e481e26c8cdafe97efe77b0"></a>

```c
#define R502A_BAUD_19200 2
```

相关声明：[R502A_BAUD_19200](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga102611233e481e26c8cdafe97efe77b0)。

19200 比特每秒（bps）。

<a id="r_gaab799d94bd0dd10ea55c47cd66ba74fb"></a>

```c
#define R502A_BAUD_38400 4
```

相关声明：[R502A_BAUD_38400](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gaab799d94bd0dd10ea55c47cd66ba74fb)。

38400 比特每秒（bps）。

<a id="r_ga19ab94871e6e51660432c29130c183fb"></a>

```c
#define R502A_BAUD_57600 6
```

相关声明：[R502A_BAUD_57600](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga19ab94871e6e51660432c29130c183fb)。

57600 比特每秒（bps）。

<a id="r_gaa0f6b1beacb3a3e57f1bd6ab3951ba6b"></a>

```c
#define R502A_BAUD_115200 12
```

相关声明：[R502A_BAUD_115200](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gaa0f6b1beacb3a3e57f1bd6ab3951ba6b)。

115200 比特每秒（bps）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 18.3\_枚举（Enumerations）

<a id="r_ga843fa88a16ab6b47c4e517ddbc01b4a8"></a>

```c
enum r502a_led_color_idx { R502A_LED_COLOR_RED = 0x01 , R502A_LED_COLOR_BLUE , R502A_LED_COLOR_PURPLE }
```

相关声明：[r502a_led_color_idx](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga843fa88a16ab6b47c4e517ddbc01b4a8)、[R502A_LED_COLOR_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga843fa88a16ab6b47c4e517ddbc01b4a8a667a844dde544590ab7b6e3defd4016c)、[R502A_LED_COLOR_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga843fa88a16ab6b47c4e517ddbc01b4a8a0685eb3e0e4de6faa0577fb5f7d0f845)、[R502A_LED_COLOR_PURPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga843fa88a16ab6b47c4e517ddbc01b4a8ad477284ea70fb76c43a386ed3537be6c)。

<a id="r_ga48154de53541aced1e78537f10f2f3d1"></a>

```c
enum r502a_sec_level { R502A_SEC_LEVEL_1 = 1 , R502A_SEC_LEVEL_2 , R502A_SEC_LEVEL_3 , R502A_SEC_LEVEL_4 , R502A_SEC_LEVEL_5 }
```

相关声明：[r502a_sec_level](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga48154de53541aced1e78537f10f2f3d1)、[R502A_SEC_LEVEL_1](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1a2220c963d396a7d6604ff0b47e3b6db7)、[R502A_SEC_LEVEL_2](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1a9fbe3bed318932b9fab282aee7e823ef)、[R502A_SEC_LEVEL_3](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1adb0e8b2e0242be58c32cf1fb8c3c00fa)、[R502A_SEC_LEVEL_4](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1a1e579d5283fb984a555f918828b3e1e9)、[R502A_SEC_LEVEL_5](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1abcb8f9a6447757b0fcb8ef4f63979dc1)。

安全级别（Security Level）。

<a id="r_ga3298eb4d591ba56131bae8137888dcd8"></a>

```c
enum r502a_data_len { R502A_PKG_LEN_32 , R502A_PKG_LEN_64 , R502A_PKG_LEN_128 , R502A_PKG_LEN_256 }
```

相关声明：[r502a_data_len](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga3298eb4d591ba56131bae8137888dcd8)、[R502A_PKG_LEN_32](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga3298eb4d591ba56131bae8137888dcd8a6be1d185636994b69006b14188d003cf)、[R502A_PKG_LEN_64](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga3298eb4d591ba56131bae8137888dcd8a61ab7cac6d6613f3465157f1ee09b2ee)、[R502A_PKG_LEN_128](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga3298eb4d591ba56131bae8137888dcd8ad5a47c82dd3733cad5a2da69f33735fe)、[R502A_PKG_LEN_256](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga3298eb4d591ba56131bae8137888dcd8a4fa6ae11c8e8f44101a729c4149a1101)。

数据包长度。

<a id="r_ga16242f27a53b430ea3cf165fbc7ce70b"></a>

```c
enum r502a_sys_param_set { R502A_BAUD_RATE = 4 , R502A_SECURITY_LEVEL , R502A_DATA_PKG_LEN }
```

相关声明：[r502a_sys_param_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga16242f27a53b430ea3cf165fbc7ce70b)、[R502A_BAUD_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga16242f27a53b430ea3cf165fbc7ce70bacef6f845b078fffb0f5f10a93cba3721)、[R502A_SECURITY_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga16242f27a53b430ea3cf165fbc7ce70ba2795f5eb1ee8feeba7f57d0bdc4ec519)、[R502A_DATA_PKG_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga16242f27a53b430ea3cf165fbc7ce70baa356f4aea69d118b8283d347b816bca1)。

系统参数集（System Parameter Set）。

<a id="r_ga8ff24814059dda20e6b36fe8cc0be30c"></a>

```c
enum sensor_channel_grow_r502a { SENSOR_CHAN_FINGERPRINT = SENSOR_CHAN_PRIV_START }
```

相关声明：[sensor_channel_grow_r502a](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga8ff24814059dda20e6b36fe8cc0be30c)、[SENSOR_CHAN_FINGERPRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2)。

Grow R502A 自定义传感器通道（Custom Sensor Channels）。

<a id="r_ga721dcba985d9010bb1f48e82b0027eb4"></a>

```c
enum sensor_trigger_type_grow_r502a { SENSOR_TRIG_TOUCH = SENSOR_TRIG_PRIV_START }
```

相关声明：[sensor_trigger_type_grow_r502a](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga721dcba985d9010bb1f48e82b0027eb4)、[SENSOR_TRIG_TOUCH](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4)。

Grow R502A 自定义触发器类型（Custom Trigger Types）。

<a id="r_ga638da7a83d9339b17e5d9c8ce92b684b"></a>

```c
enum sensor_attribute_grow_r502a { SENSOR_ATTR_R502A_CAPTURE = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_R502A_TEMPLATE_CREATE , SENSOR_ATTR_R502A_RECORD_ADD , SENSOR_ATTR_R502A_RECORD_FIND , SENSOR_ATTR_R502A_RECORD_DEL , SENSOR_ATTR_R502A_RECORD_FREE_IDX , SENSOR_ATTR_R502A_RECORD_EMPTY , SENSOR_ATTR_R502A_RECORD_LOAD , SENSOR_ATTR_R502A_COMPARE , SENSOR_ATTR_R502A_SYS_PARAM }
```

相关声明：[sensor_attribute_grow_r502a](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga638da7a83d9339b17e5d9c8ce92b684b)、[SENSOR_ATTR_R502A_CAPTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684baa499ad10253a3f3e1ad571c3a149dadd)、[SENSOR_ATTR_R502A_TEMPLATE_CREATE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba773495d23834e9fd2eb9ee02909be965)、[SENSOR_ATTR_R502A_RECORD_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb)、[SENSOR_ATTR_R502A_RECORD_FIND](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922)、[SENSOR_ATTR_R502A_RECORD_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef)、[SENSOR_ATTR_R502A_RECORD_FREE_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df)、[SENSOR_ATTR_R502A_RECORD_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b)、[SENSOR_ATTR_R502A_RECORD_LOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba2edb55a7c3ece4a382d19a951f5cbe13)、[SENSOR_ATTR_R502A_COMPARE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba7258864588bd700f50f9572d5532c689)、[SENSOR_ATTR_R502A_SYS_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba8e7d9545ee722f94e33af5335b52f3e0)。

Grow R502A 自定义传感器属性（Custom Sensor Attributes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.4\_函数（Functions）

<a id="r_ga3dbc5cd5f5295741e99735ec0279b48d"></a>

```c
int r502a_read_sys_param (const struct device *dev, struct r502a_sys_param *val)
```

相关声明：[r502a_read_sys_param](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga3dbc5cd5f5295741e99735ec0279b48d)、[device](../device_reference/P002_设备对象结构.md)、[r502a_sys_param](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md)。

读取系统参数（System Parameters）。

<a id="r_gad16b787e54f20627c4bf15b1732c05ae"></a>

```c
int fps_upload_char_buf (const struct device *dev, struct r502a_template *temp)
```

相关声明：[fps_upload_char_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gad16b787e54f20627c4bf15b1732c05ae)、[device](../device_reference/P002_设备对象结构.md)、[r502a_template](../sensor_navigation_model_reference/P023_r502a_template_结构体.md)。

上传指纹模板（Finger Template）。

<a id="r_ga3b6f1ea1024c0d855a7bbf05f79c19c8"></a>

```c
int fps_download_char_buf (const struct device *dev, uint8_t char_buf_id, const struct r502a_template *temp)
```

相关声明：[fps_download_char_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga3b6f1ea1024c0d855a7bbf05f79c19c8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[r502a_template](../sensor_navigation_model_reference/P023_r502a_template_结构体.md)。

下载指纹模板（Finger Template）。


## 18.5\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P083_grow_r502a.h_源码浏览.md)
- [r502a_sys_param](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md)
- [r502a_template](../sensor_navigation_model_reference/P023_r502a_template_结构体.md)
- [R502A_BAUD_9600](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gaaab815dc7de2a1ff5596ad6fdc1e28c2)
- [R502A_BAUD_19200](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga102611233e481e26c8cdafe97efe77b0)
- [R502A_BAUD_38400](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gaab799d94bd0dd10ea55c47cd66ba74fb)
- [R502A_BAUD_57600](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga19ab94871e6e51660432c29130c183fb)
- [R502A_BAUD_115200](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gaa0f6b1beacb3a3e57f1bd6ab3951ba6b)
- [r502a_led_color_idx](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga843fa88a16ab6b47c4e517ddbc01b4a8)
- [R502A_LED_COLOR_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga843fa88a16ab6b47c4e517ddbc01b4a8a667a844dde544590ab7b6e3defd4016c)
- [R502A_LED_COLOR_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga843fa88a16ab6b47c4e517ddbc01b4a8a0685eb3e0e4de6faa0577fb5f7d0f845)
- [R502A_LED_COLOR_PURPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga843fa88a16ab6b47c4e517ddbc01b4a8ad477284ea70fb76c43a386ed3537be6c)
- [r502a_sec_level](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga48154de53541aced1e78537f10f2f3d1)
- [R502A_SEC_LEVEL_1](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1a2220c963d396a7d6604ff0b47e3b6db7)
- [R502A_SEC_LEVEL_2](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1a9fbe3bed318932b9fab282aee7e823ef)
- [R502A_SEC_LEVEL_3](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1adb0e8b2e0242be58c32cf1fb8c3c00fa)
- [R502A_SEC_LEVEL_4](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1a1e579d5283fb984a555f918828b3e1e9)
- [R502A_SEC_LEVEL_5](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga48154de53541aced1e78537f10f2f3d1abcb8f9a6447757b0fcb8ef4f63979dc1)
- [r502a_data_len](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga3298eb4d591ba56131bae8137888dcd8)
- [R502A_PKG_LEN_32](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga3298eb4d591ba56131bae8137888dcd8a6be1d185636994b69006b14188d003cf)
- [R502A_PKG_LEN_64](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga3298eb4d591ba56131bae8137888dcd8a61ab7cac6d6613f3465157f1ee09b2ee)
- [R502A_PKG_LEN_128](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga3298eb4d591ba56131bae8137888dcd8ad5a47c82dd3733cad5a2da69f33735fe)
- [R502A_PKG_LEN_256](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga3298eb4d591ba56131bae8137888dcd8a4fa6ae11c8e8f44101a729c4149a1101)
- [r502a_sys_param_set](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga16242f27a53b430ea3cf165fbc7ce70b)
- [R502A_BAUD_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga16242f27a53b430ea3cf165fbc7ce70bacef6f845b078fffb0f5f10a93cba3721)
- [R502A_SECURITY_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga16242f27a53b430ea3cf165fbc7ce70ba2795f5eb1ee8feeba7f57d0bdc4ec519)
- [R502A_DATA_PKG_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga16242f27a53b430ea3cf165fbc7ce70baa356f4aea69d118b8283d347b816bca1)
- [sensor_channel_grow_r502a](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga8ff24814059dda20e6b36fe8cc0be30c)
- [SENSOR_CHAN_FINGERPRINT](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2)
- [sensor_trigger_type_grow_r502a](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga721dcba985d9010bb1f48e82b0027eb4)
- [SENSOR_TRIG_TOUCH](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4)
- [sensor_attribute_grow_r502a](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga638da7a83d9339b17e5d9c8ce92b684b)
- [SENSOR_ATTR_R502A_CAPTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684baa499ad10253a3f3e1ad571c3a149dadd)
- [SENSOR_ATTR_R502A_TEMPLATE_CREATE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba773495d23834e9fd2eb9ee02909be965)
- [SENSOR_ATTR_R502A_RECORD_ADD](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb)
- [SENSOR_ATTR_R502A_RECORD_FIND](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922)
- [SENSOR_ATTR_R502A_RECORD_DEL](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef)
- [SENSOR_ATTR_R502A_RECORD_FREE_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df)
- [SENSOR_ATTR_R502A_RECORD_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b)
- [SENSOR_ATTR_R502A_RECORD_LOAD](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba2edb55a7c3ece4a382d19a951f5cbe13)
- [SENSOR_ATTR_R502A_COMPARE](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba7258864588bd700f50f9572d5532c689)
- [SENSOR_ATTR_R502A_SYS_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gga638da7a83d9339b17e5d9c8ce92b684ba8e7d9545ee722f94e33af5335b52f3e0)
- [r502a_read_sys_param](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga3dbc5cd5f5295741e99735ec0279b48d)
- [device](../device_reference/P002_设备对象结构.md)
- [fps_upload_char_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#gad16b787e54f20627c4bf15b1732c05ae)
- [fps_download_char_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html#ga3b6f1ea1024c0d855a7bbf05f79c19c8)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>

---

[上一章](P017_zephyr__net__gptp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__sensor__htu31d.h_文件参考.md)
