---
id: learning.zephyr-docs.api-file-display-chat-reference.page-14
title: zephyr__input__input_crsf.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_input\_\_input\_crsf.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Crossfire（CRSF）协议的定义和辅助接口。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/types.h>
```

查看此文件的源码。

Crossfire（CRSF）协议定义与辅助接口（Protocol Definitions and Helpers）。本模块提供常量、数据包类型定义、遥测负载结构以及辅助 API，用于遥控发射机与接收机采用的 CRSF（Crossfire）协议，涵盖帧布局（Frame Layout）、遥测负载格式（Telemetry Payload Formats）、遥控通道转换（RC Channel Conversions）和链路统计访问（Link Statistics Access）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_crsf_5Fpayload_5Fgps"></a>

```c
struct crsf_payload_gps
```

相关声明：[crsf_payload_gps](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md)。

GPS遥测（GPS Telemetry）载荷，类型为0x02。

<a id="r_crsf_5Fpayload_5Fbattery"></a>

```c
struct crsf_payload_battery
```

相关声明：[crsf_payload_battery](../sensor_navigation_model_reference/P005_crsf_payload_battery_结构体.md)。

电池遥测（Battery Telemetry）载荷，类型为0x08。

<a id="r_crsf_5Flink_5Fstats"></a>

```c
struct crsf_link_stats
```

相关声明：[crsf_link_stats](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md)。

链路统计信息（Link Statistics）载荷，类型为0x14。

<a id="r_crsf_5Fpayload_5Fattitude"></a>

```c
struct crsf_payload_attitude
```

相关声明：[crsf_payload_attitude](../sensor_navigation_model_reference/P004_crsf_payload_attitude_结构体.md)。

姿态遥测（Attitude Telemetry）载荷，类型为0x1E。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 遥控通道转换辅助接口（RC Channel Conversion Helpers）

CRSF 刻度（Ticks）与微秒之间的转换。

<a id="r_a97ddcbb19eb03a4d730cec4ae6040da6"></a>

```c
#define CRSF_TICKS_TO_US(x)
```

相关声明：[CRSF_TICKS_TO_US](#a97ddcbb19eb03a4d730cec4ae6040da6)。

将 CRSF 通道刻度（Channel Ticks）转换为微秒。

<a id="r_a10e14f53d05cc4e895a4089efffe69c3"></a>

```c
#define CRSF_US_TO_TICKS(x)
```

相关声明：[CRSF_US_TO_TICKS](#a10e14f53d05cc4e895a4089efffe69c3)。

将微秒转换为 CRSF 通道刻度（Channel Ticks）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.3\_枚举（Enumerations）

<a id="enum-members-0"></a>

<a id="r_a352177d3a02932443b0d2cc4db628faf"></a>

```c
enum crsf_packet_type { CRSF_TYPE_GPS = 0x02 , CRSF_TYPE_BATTERY = 0x08 , CRSF_TYPE_LINK_TX_ID = 0x0A , CRSF_TYPE_LINK_STATS = 0x14 , CRSF_TYPE_RC_CHANNELS = 0x16 , CRSF_TYPE_ATTITUDE = 0x1E , CRSF_TYPE_FLIGHT_MODE = 0x21 , CRSF_TYPE_PING_DEVICES = 0x28 , CRSF_TYPE_DEVICE_INFO = 0x29 , CRSF_TYPE_PARAMETER_SETTINGS = 0x2B , CRSF_TYPE_COMMAND = 0x32 , CRSF_TYPE_RADIO_ID = 0x3A , CRSF_TYPE_AP_CUSTOM_TELEM = 0x80 }
```

相关声明：[crsf_packet_type](#a352177d3a02932443b0d2cc4db628faf)、[CRSF_TYPE_GPS](#a352177d3a02932443b0d2cc4db628fafa4d542852dca1c165c09f6a25da5b8f78)、[CRSF_TYPE_BATTERY](#a352177d3a02932443b0d2cc4db628fafacd7c511a63096ab430a21adb1d51f968)、[CRSF_TYPE_LINK_TX_ID](#a352177d3a02932443b0d2cc4db628fafa46045337ef856c4adeff9a07ee51c487)、[CRSF_TYPE_LINK_STATS](#a352177d3a02932443b0d2cc4db628fafa7c8b088ae306fc912f12043f7bbdb44e)、[CRSF_TYPE_RC_CHANNELS](#a352177d3a02932443b0d2cc4db628fafafd5ec386a4a46942548aabd76553f8be)、[CRSF_TYPE_ATTITUDE](#a352177d3a02932443b0d2cc4db628fafa973d8c9aef67fb0ab535c110a2c783d3)、[CRSF_TYPE_FLIGHT_MODE](#a352177d3a02932443b0d2cc4db628fafa5ba4e72f3c5577ccf16712f60f888d91)、[CRSF_TYPE_PING_DEVICES](#a352177d3a02932443b0d2cc4db628fafa913488d37e7df391fb1859eca0e92f41)、[CRSF_TYPE_DEVICE_INFO](#a352177d3a02932443b0d2cc4db628fafa2ac02b4732dc0c35ab532f6fa5ea3d2b)、[CRSF_TYPE_PARAMETER_SETTINGS](#a352177d3a02932443b0d2cc4db628fafa97e0bfc9baa2fa444d72930a89c9ff03)、[CRSF_TYPE_COMMAND](#a352177d3a02932443b0d2cc4db628fafacbf77a08de27bef11b9ebb315d15a0c3)、[CRSF_TYPE_RADIO_ID](#a352177d3a02932443b0d2cc4db628fafa81ce3c65b5af1bd45a798821f557c0a2)、[CRSF_TYPE_AP_CUSTOM_TELEM](#a352177d3a02932443b0d2cc4db628fafaea2e80f7897ce58cbf3be0a7fd995364)。

CRSF 数据包（帧）类型（Packet/Frame Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.4\_函数（Functions）

<a id="r_a7bb48e231b715587daf4c7a57c0e2b8a"></a>

```c
int input_crsf_send_telemetry (const struct device *dev, uint8_t type, uint8_t *payload, size_t payload_len)
```

相关声明：[input_crsf_send_telemetry](#a7bb48e231b715587daf4c7a57c0e2b8a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送通用 CRSF 遥测帧（Telemetry Frame）。

<a id="r_acb8b2de8f49e5037f3ddacaef40f71c2"></a>

```c
struct crsf_link_stats input_crsf_get_link_stats (const struct device *dev)
```

相关声明：[crsf_link_stats](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md)、[input_crsf_get_link_stats](#acb8b2de8f49e5037f3ddacaef40f71c2)、[device](../device_reference/P002_设备对象结构.md)。

获取最新 CRSF 链路统计信息（Link Statistics）。

## 14.5\_详细说明（Detailed Documentation）

<a id="a97ddcbb19eb03a4d730cec4ae6040da6"></a>

### `CRSF_TICKS_TO_US`

```c
#define CRSF_TICKS_TO_US ( x)
```

展开值（Value）：

```c
(((x) - 992) * 5 / 8 + 1500)
```

将 CRSF 通道刻度（Channel Ticks）转换为微秒。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 以刻度（Ticks）表示的 CRSF 通道值。 |

返回（Returns）：以微秒表示的脉冲宽度（Pulse Width）。

<a id="a10e14f53d05cc4e895a4089efffe69c3"></a>

### `CRSF_US_TO_TICKS`

```c
#define CRSF_US_TO_TICKS ( x)
```

展开值（Value）：

```c
(((x) - 1500) * 8 / 5 + 992)
```

将微秒转换为 CRSF 通道刻度（Channel Ticks）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 以微秒表示的脉冲宽度（Pulse Width）。 |

返回（Returns）：以刻度（Ticks）表示的 CRSF 通道值。

<a id="a352177d3a02932443b0d2cc4db628faf"></a>

### `crsf_packet_type`

```c
enum crsf_packet_type
```

CRSF 数据包（帧）类型（Packet/Frame Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CRSF_TYPE_GPS` | GPS 遥测数据（Telemetry Data）。 |
| `CRSF_TYPE_BATTERY` | 电池遥测数据（Battery Telemetry Data）。 |
| `CRSF_TYPE_LINK_TX_ID` | 发射机链路标识符（Transmitter Link Identifier）。 |
| `CRSF_TYPE_LINK_STATS` | 链路统计信息（Link Statistics）。 |
| `CRSF_TYPE_RC_CHANNELS` | 遥控通道数据（RC Channel Data）。 |
| `CRSF_TYPE_ATTITUDE` | 姿态遥测（Attitude Telemetry）。 |
| `CRSF_TYPE_FLIGHT_MODE` | 飞行模式字符串（Flight Mode String）。 |
| `CRSF_TYPE_PING_DEVICES` | 设备发现／探测（Device Discovery / Ping）。 |
| `CRSF_TYPE_DEVICE_INFO` | 设备信息（Device Information）。 |
| `CRSF_TYPE_PARAMETER_SETTINGS` | 参数读／写（Parameter Read/Write）。 |
| `CRSF_TYPE_COMMAND` | 命令帧（Command Frame）。 |
| `CRSF_TYPE_RADIO_ID` | 无线电标识符（Radio Identifier）。 |
| `CRSF_TYPE_AP_CUSTOM_TELEM` | ArduPilot 自定义遥测（Custom Telemetry）。 |

<a id="acb8b2de8f49e5037f3ddacaef40f71c2"></a>

### `input_crsf_get_link_stats()`

```c
struct crsf_link_stats input_crsf_get_link_stats ( const struct device * dev)
```

获取最新 CRSF 链路统计信息（Link Statistics）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 CRSF 输入设备（Input Device）的指针。 |

返回（Returns）：当前链路统计结构（Link Statistics Structure）。

<a id="a7bb48e231b715587daf4c7a57c0e2b8a"></a>

### `input_crsf_send_telemetry()`

```c
int input_crsf_send_telemetry ( const struct device * dev, uint8_t type, uint8_t * payload, size_t payload_len )
```

发送通用 CRSF 遥测帧（Telemetry Frame）。

复制该帧并异步发送（Asynchronous Transmission）；本函数不等待发送完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 CRSF 输入设备（Input Device）的指针。 |
| `type` | 数据包类型（Packet Type），参见 crsf_packet_type。 |
| `payload` | 指向负载缓冲区（Payload Buffer）的指针。 |
| `payload_len` | 负载长度（Payload Length），单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 帧已进入发送队列（Queued for Transmission）。 |
| `-EINVAL` | 负载过大，或者负载为 NULL 但长度非零。 |
| `-EBUSY` | 上一帧仍在发送（Being Transmitted）。 |
| `<0` | uart_tx() 返回的其他负 errno 错误码。 |


## 14.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P379_input_crsf.h_源码浏览.md)
- [crsf_payload_gps](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md)
- [crsf_payload_battery](../sensor_navigation_model_reference/P005_crsf_payload_battery_结构体.md)
- [crsf_link_stats](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md)
- [crsf_payload_attitude](../sensor_navigation_model_reference/P004_crsf_payload_attitude_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uart_tx()](../hardware/P334_UART异步接口.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a352177d3a02932443b0d2cc4db628fafa4d542852dca1c165c09f6a25da5b8f78"></a>
<a id="a352177d3a02932443b0d2cc4db628fafacd7c511a63096ab430a21adb1d51f968"></a>
<a id="a352177d3a02932443b0d2cc4db628fafa46045337ef856c4adeff9a07ee51c487"></a>
<a id="a352177d3a02932443b0d2cc4db628fafa7c8b088ae306fc912f12043f7bbdb44e"></a>
<a id="a352177d3a02932443b0d2cc4db628fafafd5ec386a4a46942548aabd76553f8be"></a>
<a id="a352177d3a02932443b0d2cc4db628fafa973d8c9aef67fb0ab535c110a2c783d3"></a>
<a id="a352177d3a02932443b0d2cc4db628fafa5ba4e72f3c5577ccf16712f60f888d91"></a>
<a id="a352177d3a02932443b0d2cc4db628fafa913488d37e7df391fb1859eca0e92f41"></a>
<a id="a352177d3a02932443b0d2cc4db628fafa2ac02b4732dc0c35ab532f6fa5ea3d2b"></a>
<a id="a352177d3a02932443b0d2cc4db628fafa97e0bfc9baa2fa444d72930a89c9ff03"></a>
<a id="a352177d3a02932443b0d2cc4db628fafacbf77a08de27bef11b9ebb315d15a0c3"></a>
<a id="a352177d3a02932443b0d2cc4db628fafa81ce3c65b5af1bd45a798821f557c0a2"></a>
<a id="a352177d3a02932443b0d2cc4db628fafaea2e80f7897ce58cbf3be0a7fd995364"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_zephyr__dt-bindings__clock__imx_ccm_rev3.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__irq_multilevel.h_文件参考.md)
