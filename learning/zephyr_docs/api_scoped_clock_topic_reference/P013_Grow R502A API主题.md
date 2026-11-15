---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-13
title: Grow R502A API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_Grow R502A API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__grow__r502a__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HZ-Grow GROW_R502A 指纹传感器（Fingerprint sensor）。

<a id="details"></a>

HZ-Grow GROW_R502A 指纹传感器（Fingerprint sensor）。

<a id="header-files"></a>
<a id="files"></a>

## 13.1\_文件（Files）

<a id="r_grow_5Fr502a_2Eh"></a>

```c
file grow_r502a.h
```

相关声明：[grow_r502a.h](../api_file_protocol_service_reference/P018_zephyr__drivers__sensor__grow_r502a.h_文件参考.md)。

Grow R502A传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.2\_数据结构（Data Structures）

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

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.3\_枚举（Enumerations）

<a id="r_ga843fa88a16ab6b47c4e517ddbc01b4a8"></a>

```c
enum r502a_led_color_idx { R502A_LED_COLOR_RED = 0x01 , R502A_LED_COLOR_BLUE , R502A_LED_COLOR_PURPLE }
```

相关声明：[r502a_led_color_idx](#ga843fa88a16ab6b47c4e517ddbc01b4a8)、[R502A_LED_COLOR_RED](#gga843fa88a16ab6b47c4e517ddbc01b4a8a667a844dde544590ab7b6e3defd4016c)、[R502A_LED_COLOR_BLUE](#gga843fa88a16ab6b47c4e517ddbc01b4a8a0685eb3e0e4de6faa0577fb5f7d0f845)、[R502A_LED_COLOR_PURPLE](#gga843fa88a16ab6b47c4e517ddbc01b4a8ad477284ea70fb76c43a386ed3537be6c)。

<a id="r_ga48154de53541aced1e78537f10f2f3d1"></a>

```c
enum r502a_sec_level { R502A_SEC_LEVEL_1 = 1 , R502A_SEC_LEVEL_2 , R502A_SEC_LEVEL_3 , R502A_SEC_LEVEL_4 , R502A_SEC_LEVEL_5 }
```

相关声明：[r502a_sec_level](#ga48154de53541aced1e78537f10f2f3d1)、[R502A_SEC_LEVEL_1](#gga48154de53541aced1e78537f10f2f3d1a2220c963d396a7d6604ff0b47e3b6db7)、[R502A_SEC_LEVEL_2](#gga48154de53541aced1e78537f10f2f3d1a9fbe3bed318932b9fab282aee7e823ef)、[R502A_SEC_LEVEL_3](#gga48154de53541aced1e78537f10f2f3d1adb0e8b2e0242be58c32cf1fb8c3c00fa)、[R502A_SEC_LEVEL_4](#gga48154de53541aced1e78537f10f2f3d1a1e579d5283fb984a555f918828b3e1e9)、[R502A_SEC_LEVEL_5](#gga48154de53541aced1e78537f10f2f3d1abcb8f9a6447757b0fcb8ef4f63979dc1)。

安全级别（Security Level）。

<a id="r_ga3298eb4d591ba56131bae8137888dcd8"></a>

```c
enum r502a_data_len { R502A_PKG_LEN_32 , R502A_PKG_LEN_64 , R502A_PKG_LEN_128 , R502A_PKG_LEN_256 }
```

相关声明：[r502a_data_len](#ga3298eb4d591ba56131bae8137888dcd8)、[R502A_PKG_LEN_32](#gga3298eb4d591ba56131bae8137888dcd8a6be1d185636994b69006b14188d003cf)、[R502A_PKG_LEN_64](#gga3298eb4d591ba56131bae8137888dcd8a61ab7cac6d6613f3465157f1ee09b2ee)、[R502A_PKG_LEN_128](#gga3298eb4d591ba56131bae8137888dcd8ad5a47c82dd3733cad5a2da69f33735fe)、[R502A_PKG_LEN_256](#gga3298eb4d591ba56131bae8137888dcd8a4fa6ae11c8e8f44101a729c4149a1101)。

数据包长度。

<a id="r_ga16242f27a53b430ea3cf165fbc7ce70b"></a>

```c
enum r502a_sys_param_set { R502A_BAUD_RATE = 4 , R502A_SECURITY_LEVEL , R502A_DATA_PKG_LEN }
```

相关声明：[r502a_sys_param_set](#ga16242f27a53b430ea3cf165fbc7ce70b)、[R502A_BAUD_RATE](#gga16242f27a53b430ea3cf165fbc7ce70bacef6f845b078fffb0f5f10a93cba3721)、[R502A_SECURITY_LEVEL](#gga16242f27a53b430ea3cf165fbc7ce70ba2795f5eb1ee8feeba7f57d0bdc4ec519)、[R502A_DATA_PKG_LEN](#gga16242f27a53b430ea3cf165fbc7ce70baa356f4aea69d118b8283d347b816bca1)。

系统参数集（System Parameter Set）。

<a id="r_ga8ff24814059dda20e6b36fe8cc0be30c"></a>

```c
enum sensor_channel_grow_r502a { SENSOR_CHAN_FINGERPRINT = SENSOR_CHAN_PRIV_START }
```

相关声明：[sensor_channel_grow_r502a](#ga8ff24814059dda20e6b36fe8cc0be30c)、[SENSOR_CHAN_FINGERPRINT](#gga8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2)。

Grow R502A 自定义传感器通道（Custom Sensor Channels）。

<a id="r_ga721dcba985d9010bb1f48e82b0027eb4"></a>

```c
enum sensor_trigger_type_grow_r502a { SENSOR_TRIG_TOUCH = SENSOR_TRIG_PRIV_START }
```

相关声明：[sensor_trigger_type_grow_r502a](#ga721dcba985d9010bb1f48e82b0027eb4)、[SENSOR_TRIG_TOUCH](#gga721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4)。

Grow R502A 自定义触发器类型（Custom Trigger Types）。

<a id="r_ga638da7a83d9339b17e5d9c8ce92b684b"></a>

```c
enum sensor_attribute_grow_r502a { SENSOR_ATTR_R502A_CAPTURE = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_R502A_TEMPLATE_CREATE , SENSOR_ATTR_R502A_RECORD_ADD , SENSOR_ATTR_R502A_RECORD_FIND , SENSOR_ATTR_R502A_RECORD_DEL , SENSOR_ATTR_R502A_RECORD_FREE_IDX , SENSOR_ATTR_R502A_RECORD_EMPTY , SENSOR_ATTR_R502A_RECORD_LOAD , SENSOR_ATTR_R502A_COMPARE , SENSOR_ATTR_R502A_SYS_PARAM }
```

相关声明：[sensor_attribute_grow_r502a](#ga638da7a83d9339b17e5d9c8ce92b684b)、[SENSOR_ATTR_R502A_CAPTURE](#gga638da7a83d9339b17e5d9c8ce92b684baa499ad10253a3f3e1ad571c3a149dadd)、[SENSOR_ATTR_R502A_TEMPLATE_CREATE](#gga638da7a83d9339b17e5d9c8ce92b684ba773495d23834e9fd2eb9ee02909be965)、[SENSOR_ATTR_R502A_RECORD_ADD](#gga638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb)、[SENSOR_ATTR_R502A_RECORD_FIND](#gga638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922)、[SENSOR_ATTR_R502A_RECORD_DEL](#gga638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef)、[SENSOR_ATTR_R502A_RECORD_FREE_IDX](#gga638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df)、[SENSOR_ATTR_R502A_RECORD_EMPTY](#gga638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b)、[SENSOR_ATTR_R502A_RECORD_LOAD](#gga638da7a83d9339b17e5d9c8ce92b684ba2edb55a7c3ece4a382d19a951f5cbe13)、[SENSOR_ATTR_R502A_COMPARE](#gga638da7a83d9339b17e5d9c8ce92b684ba7258864588bd700f50f9572d5532c689)、[SENSOR_ATTR_R502A_SYS_PARAM](#gga638da7a83d9339b17e5d9c8ce92b684ba8e7d9545ee722f94e33af5335b52f3e0)。

Grow R502A 自定义传感器属性（Custom Sensor Attributes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.4\_函数（Functions）

<a id="r_ga3dbc5cd5f5295741e99735ec0279b48d"></a>

```c
int r502a_read_sys_param (const struct device *dev, struct r502a_sys_param *val)
```

相关声明：[r502a_read_sys_param](#ga3dbc5cd5f5295741e99735ec0279b48d)、[device](../device_reference/P002_设备对象结构.md)、[r502a_sys_param](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md)。

读取系统参数（System Parameters）。

<a id="r_gad16b787e54f20627c4bf15b1732c05ae"></a>

```c
int fps_upload_char_buf (const struct device *dev, struct r502a_template *temp)
```

相关声明：[fps_upload_char_buf](#gad16b787e54f20627c4bf15b1732c05ae)、[device](../device_reference/P002_设备对象结构.md)、[r502a_template](../sensor_navigation_model_reference/P023_r502a_template_结构体.md)。

上传指纹模板（Finger Template）。

<a id="r_ga3b6f1ea1024c0d855a7bbf05f79c19c8"></a>

```c
int fps_download_char_buf (const struct device *dev, uint8_t char_buf_id, const struct r502a_template *temp)
```

相关声明：[fps_download_char_buf](#ga3b6f1ea1024c0d855a7bbf05f79c19c8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[r502a_template](../sensor_navigation_model_reference/P023_r502a_template_结构体.md)。

下载指纹模板（Finger Template）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 13.5\_波特率（Baud Rates）

<a id="r_gaaab815dc7de2a1ff5596ad6fdc1e28c2"></a>

```c
#define R502A_BAUD_9600 1
```

相关声明：[R502A_BAUD_9600](#gaaab815dc7de2a1ff5596ad6fdc1e28c2)。

9600 比特每秒（bps）。

<a id="r_ga102611233e481e26c8cdafe97efe77b0"></a>

```c
#define R502A_BAUD_19200 2
```

相关声明：[R502A_BAUD_19200](#ga102611233e481e26c8cdafe97efe77b0)。

19200 比特每秒（bps）。

<a id="r_gaab799d94bd0dd10ea55c47cd66ba74fb"></a>

```c
#define R502A_BAUD_38400 4
```

相关声明：[R502A_BAUD_38400](#gaab799d94bd0dd10ea55c47cd66ba74fb)。

38400 比特每秒（bps）。

<a id="r_ga19ab94871e6e51660432c29130c183fb"></a>

```c
#define R502A_BAUD_57600 6
```

相关声明：[R502A_BAUD_57600](#ga19ab94871e6e51660432c29130c183fb)。

57600 比特每秒（bps）。

<a id="r_gaa0f6b1beacb3a3e57f1bd6ab3951ba6b"></a>

```c
#define R502A_BAUD_115200 12
```

相关声明：[R502A_BAUD_115200](#gaa0f6b1beacb3a3e57f1bd6ab3951ba6b)。

115200 比特每秒（bps）。

## 13.6\_详细说明（Detailed Documentation）

<a id="gaa0f6b1beacb3a3e57f1bd6ab3951ba6b"></a>

### `R502A_BAUD_115200`

```c
#define R502A_BAUD_115200 12
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

115200 比特每秒（bps）。

<a id="ga102611233e481e26c8cdafe97efe77b0"></a>

### `R502A_BAUD_19200`

```c
#define R502A_BAUD_19200 2
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

19200 比特每秒（bps）。

<a id="gaab799d94bd0dd10ea55c47cd66ba74fb"></a>

### `R502A_BAUD_38400`

```c
#define R502A_BAUD_38400 4
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

38400 比特每秒（bps）。

<a id="ga19ab94871e6e51660432c29130c183fb"></a>

### `R502A_BAUD_57600`

```c
#define R502A_BAUD_57600 6
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

57600 比特每秒（bps）。

<a id="gaaab815dc7de2a1ff5596ad6fdc1e28c2"></a>

### `R502A_BAUD_9600`

```c
#define R502A_BAUD_9600 1
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

9600 比特每秒（bps）。

<a id="ga3298eb4d591ba56131bae8137888dcd8"></a>

### `r502a_data_len`

```c
enum r502a_data_len
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

数据包长度。

此枚举列出传感器与主机通信时支持的所有数据包长度（Data Packet Lengths）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `R502A_PKG_LEN_32` | 32 字节（Bytes）。 |
| `R502A_PKG_LEN_64` | 64 字节（Bytes）。 |
| `R502A_PKG_LEN_128` | 128 字节（Bytes）。 |
| `R502A_PKG_LEN_256` | 256 字节（Bytes）。 |

<a id="ga843fa88a16ab6b47c4e517ddbc01b4a8"></a>

### `r502a_led_color_idx`

```c
enum r502a_led_color_idx
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `R502A_LED_COLOR_RED` |  |
| `R502A_LED_COLOR_BLUE` |  |
| `R502A_LED_COLOR_PURPLE` |  |

<a id="ga48154de53541aced1e78537f10f2f3d1"></a>

### `r502a_sec_level`

```c
enum r502a_sec_level
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

安全级别（Security Level）。

此枚举列出支持的所有安全级别（Security Levels），用于控制指纹匹配（Fingerprint Matching）的匹配阈值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `R502A_SEC_LEVEL_1` | 级别 1（Level 1），安全性最低。 |
| `R502A_SEC_LEVEL_2` | 级别 2（Level 2）。 |
| `R502A_SEC_LEVEL_3` | 级别 3（Level 3）。 |
| `R502A_SEC_LEVEL_4` | 级别 4（Level 4）。 |
| `R502A_SEC_LEVEL_5` | 级别 5（Level 5），安全性最高。 |

<a id="ga16242f27a53b430ea3cf165fbc7ce70b"></a>

### `r502a_sys_param_set`

```c
enum r502a_sys_param_set
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

系统参数集（System Parameter Set）。

此枚举列出全部可设置的系统参数（System Parameters）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `R502A_BAUD_RATE` | 波特率（Baud rate）。 |
| `R502A_SECURITY_LEVEL` | 安全级别（Security Level）。 |
| `R502A_DATA_PKG_LEN` | 数据包长度（Data Package Length）。 |

<a id="ga638da7a83d9339b17e5d9c8ce92b684b"></a>

### `sensor_attribute_grow_r502a`

```c
enum sensor_attribute_grow_r502a
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

Grow R502A 自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_R502A_CAPTURE` | 采集指纹，并将特征文件（Feature File）存储到 RAM 缓冲区 char_buf_1 和 char_buf_2。 |
| `SENSOR_ATTR_R502A_TEMPLATE_CREATE` | 根据 RAM 缓冲区 char_buf_1 与 char_buf_2 中的特征文件（Feature Files）创建模板（Template），并将模板数据写回这两个 RAM 缓冲区。 |
| `SENSOR_ATTR_R502A_RECORD_ADD` | 向传感器记录存储区（Record Storage）添加模板（Template）。sensor_value.val1 是模板在传感器设备闪存中的存储记录索引（Record Index）。 |
| `SENSOR_ATTR_R502A_RECORD_FIND` | 在记录存储区（Record Storage）中查找请求的数据。sensor_value.val1 为匹配的记录索引（Record Index）；sensor_value.val2 为匹配得分（Matching Score）。 |
| `SENSOR_ATTR_R502A_RECORD_DEL` | 从记录存储区（Record Storage）删除指定数据。sensor_value.val1 为待删除记录的起始索引（Start Index）；sensor_value.val2 为待删除记录数量。 |
| `SENSOR_ATTR_R502A_RECORD_FREE_IDX` | 获取记录存储区（Record Storage）中可用于存储数据的位置。 |
| `SENSOR_ATTR_R502A_RECORD_EMPTY` | 清空存储记录（Storage Record）。 |
| `SENSOR_ATTR_R502A_RECORD_LOAD` | 将模板（Template）从存储区加载到传感器的 RAM 缓冲区。sensor_value.val1 为要加载到设备内部 RAM 缓冲区的记录起始索引（Record Start Index）。 |
| `SENSOR_ATTR_R502A_COMPARE` | 传感器 RAM 缓冲区中存储的模板数据（Template Data）。sensor_value.val1 为匹配结果（Match Result），即 R502A_FINGER_MATCH_FOUND 或 R502A_FINGER_MATCH_NOT_FOUND；sensor_value.val2 为匹配得分（Matching Score）。 |
| `SENSOR_ATTR_R502A_SYS_PARAM` | 设置设备的系统参数（System Parameters）。sensor_value.val1 为枚举 r502a_sys_param_set 中的参数编号；sensor_value.val2 为要写入相应参数的内容。 |

<a id="ga8ff24814059dda20e6b36fe8cc0be30c"></a>

### `sensor_channel_grow_r502a`

```c
enum sensor_channel_grow_r502a
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

Grow R502A 自定义传感器通道（Custom Sensor Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_FINGERPRINT` | 指纹模板数量（Fingerprint Template Count），用于录入（Enrolling）和搜索的标识编号。 |

<a id="ga721dcba985d9010bb1f48e82b0027eb4"></a>

### `sensor_trigger_type_grow_r502a`

```c
enum sensor_trigger_type_grow_r502a
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

Grow R502A 自定义触发器类型（Custom Trigger Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_TRIG_TOUCH` | 检测到触摸（Touch）时触发触发器（Trigger）。 |

<a id="ga3b6f1ea1024c0d855a7bbf05f79c19c8"></a>

### `fps_download_char_buf()`

```c
int fps_download_char_buf ( const struct device * dev, uint8_t char_buf_id, const struct r502a_template * temp )
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

下载指纹模板（Finger Template）。

此函数从传感器下载指纹模板（Fingerprint Template）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `char_buf_id` | 字符缓冲区标识符（Character Buffer ID），为 1 或 2。 |
| `temp` | 指向模板结构体（Template Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-errno` | 失败时返回负错误码。 |

<a id="gad16b787e54f20627c4bf15b1732c05ae"></a>

### `fps_upload_char_buf()`

```c
int fps_upload_char_buf ( const struct device * dev, struct r502a_template * temp )
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

上传指纹模板（Finger Template）。

此函数将指纹模板（Fingerprint Template）上传到传感器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `temp` | 指向模板结构体（Template Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-errno` | 失败时返回负错误码。 |

<a id="ga3dbc5cd5f5295741e99735ec0279b48d"></a>

### `r502a_read_sys_param()`

```c
int r502a_read_sys_param ( const struct device * dev, struct r502a_sys_param * val )
```

```c
#include <zephyr/drivers/sensor/grow_r502a.h>
```

读取系统参数（System Parameters）。

此函数从传感器读取系统参数（System Parameters）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `val` | 指向系统参数结构体（System Parameter Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-errno` | 失败时返回负错误码。 |


## 13.7\_原页交叉引用（Cross References）

- [grow_r502a.h](../api_file_protocol_service_reference/P018_zephyr__drivers__sensor__grow_r502a.h_文件参考.md)
- [r502a_sys_param](../sensor_navigation_model_reference/P022_r502a_sys_param_结构体.md)
- [r502a_template](../sensor_navigation_model_reference/P023_r502a_template_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [sensor_value.val2](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#a91f81bd0f5da69084cf3c629fde68a1b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga3298eb4d591ba56131bae8137888dcd8a6be1d185636994b69006b14188d003cf"></a>
<a id="gga3298eb4d591ba56131bae8137888dcd8a61ab7cac6d6613f3465157f1ee09b2ee"></a>
<a id="gga3298eb4d591ba56131bae8137888dcd8ad5a47c82dd3733cad5a2da69f33735fe"></a>
<a id="gga3298eb4d591ba56131bae8137888dcd8a4fa6ae11c8e8f44101a729c4149a1101"></a>
<a id="gga843fa88a16ab6b47c4e517ddbc01b4a8a667a844dde544590ab7b6e3defd4016c"></a>
<a id="gga843fa88a16ab6b47c4e517ddbc01b4a8a0685eb3e0e4de6faa0577fb5f7d0f845"></a>
<a id="gga843fa88a16ab6b47c4e517ddbc01b4a8ad477284ea70fb76c43a386ed3537be6c"></a>
<a id="gga48154de53541aced1e78537f10f2f3d1a2220c963d396a7d6604ff0b47e3b6db7"></a>
<a id="gga48154de53541aced1e78537f10f2f3d1a9fbe3bed318932b9fab282aee7e823ef"></a>
<a id="gga48154de53541aced1e78537f10f2f3d1adb0e8b2e0242be58c32cf1fb8c3c00fa"></a>
<a id="gga48154de53541aced1e78537f10f2f3d1a1e579d5283fb984a555f918828b3e1e9"></a>
<a id="gga48154de53541aced1e78537f10f2f3d1abcb8f9a6447757b0fcb8ef4f63979dc1"></a>
<a id="gga16242f27a53b430ea3cf165fbc7ce70bacef6f845b078fffb0f5f10a93cba3721"></a>
<a id="gga16242f27a53b430ea3cf165fbc7ce70ba2795f5eb1ee8feeba7f57d0bdc4ec519"></a>
<a id="gga16242f27a53b430ea3cf165fbc7ce70baa356f4aea69d118b8283d347b816bca1"></a>
<a id="gga638da7a83d9339b17e5d9c8ce92b684baa499ad10253a3f3e1ad571c3a149dadd"></a>
<a id="gga638da7a83d9339b17e5d9c8ce92b684ba773495d23834e9fd2eb9ee02909be965"></a>
<a id="gga638da7a83d9339b17e5d9c8ce92b684ba21f7eeb2a0f277f65eb36c389fbb28eb"></a>
<a id="gga638da7a83d9339b17e5d9c8ce92b684baea17f5a55989ccfbbc946ec0283a2922"></a>
<a id="gga638da7a83d9339b17e5d9c8ce92b684ba316c52d77ed8be366c5a2736d93da1ef"></a>
<a id="gga638da7a83d9339b17e5d9c8ce92b684bac485d08e7a02d6c21fd428b9d846e9df"></a>
<a id="gga638da7a83d9339b17e5d9c8ce92b684bad40eb32ad584064c261e666712f97e7b"></a>
<a id="gga638da7a83d9339b17e5d9c8ce92b684ba2edb55a7c3ece4a382d19a951f5cbe13"></a>
<a id="gga638da7a83d9339b17e5d9c8ce92b684ba7258864588bd700f50f9572d5532c689"></a>
<a id="gga638da7a83d9339b17e5d9c8ce92b684ba8e7d9545ee722f94e33af5335b52f3e0"></a>
<a id="gga8ff24814059dda20e6b36fe8cc0be30ca51abf7335f93117c01052a641a5f5cf2"></a>
<a id="gga721dcba985d9010bb1f48e82b0027eb4a5cf35bed5ff3c6f55b00f19cde2fc0e4"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_FT8xx 参考 API.md) · [返回大纲](大纲.md) · [下一章](P014_LIS2DUX12 API主题.md)
