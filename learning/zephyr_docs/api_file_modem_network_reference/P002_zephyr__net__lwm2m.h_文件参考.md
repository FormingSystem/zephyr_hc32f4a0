---
id: learning.zephyr-docs.api-file-modem-network-reference.page-2
title: zephyr__net__lwm2m.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_net\_\_lwm2m.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

轻量级M2M（LwM2M）的高层API。

<a id="details"></a>

```c
#include <time.h>
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/sys/mutex.h>
#include <zephyr/net/coap.h>
#include <zephyr/net/lwm2m_path.h>
```

查看此文件的源码。

轻量级机器到机器通信（LwM2M）高层 API。本头文件定义 LwM2M 高层接口（High-level Interface）。注意（Note）：实现假定已启用 UDP 模块。更多信息参见技术规范（Technical Specification）`OMA-TS-LightweightM2M_Core-V1_1_1-20190617-A`。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_lwm2m_5Fobj_5Fpath"></a>

```c
struct lwm2m_obj_path
```

相关声明：[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

轻量级M2M（LwM2M）的对象路径结构。

<a id="r_lwm2m_5Fctx"></a>

```c
struct lwm2m_ctx
```

相关声明：[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

用于维护单个轻量级M2M（LwM2M）连接信息的上下文结构。

<a id="r_lwm2m_5Ftime_5Fseries_5Felem"></a>

```c
struct lwm2m_time_series_elem
```

相关声明：[lwm2m_time_series_elem](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md)。

轻量级M2M（LwM2M）的时间序列数据结构。

<a id="r_lwm2m_5Fobjlnk"></a>

```c
struct lwm2m_objlnk
```

相关声明：[lwm2m_objlnk](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md)。

轻量级M2M（LwM2M）的对象链接（Objlnk）资源类型结构。

<a id="r_lwm2m_5Fres_5Fitem"></a>

```c
struct lwm2m_res_item
```

相关声明：[lwm2m_res_item](../network_application_model_reference/P050_lwm2m_res_item_结构体.md)。

轻量级M2M（LwM2M）的资源项结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga34febb0c6fb1c68b0963a6e4dd721763"></a>

```c
#define LWM2M_OBJLNK_MAX_ID USHRT_MAX
```

相关声明：[LWM2M_OBJLNK_MAX_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga34febb0c6fb1c68b0963a6e4dd721763)。

对象链接（Objlnk）资源字段的最大值。

<a id="r_ga12c2e0af3d3fc6dd5785e08c0d831a67"></a>

```c
#define LWM2M_RES_DATA_READ_ONLY 0
```

相关声明：[LWM2M_RES_DATA_READ_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga12c2e0af3d3fc6dd5785e08c0d831a67)。

资源只读值位（Resource Read-only Value Bit）。

<a id="r_ga1bfa5b7d83e3560828a1fb61a4d07355"></a>

```c
#define LWM2M_RES_DATA_FLAG_RO BIT(LWM2M_RES_DATA_READ_ONLY)
```

相关声明：[LWM2M_RES_DATA_FLAG_RO](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1bfa5b7d83e3560828a1fb61a4d07355)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[LWM2M_RES_DATA_READ_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga12c2e0af3d3fc6dd5785e08c0d831a67)。

资源只读标志（Resource Read-only Flag）。

<a id="r_ga49f4117dfec8cd1abe9f827e235f55b0"></a>

```c
#define LWM2M_HAS_RES_FLAG(res, f)
```

相关声明：[LWM2M_HAS_RES_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga49f4117dfec8cd1abe9f827e235f55b0)。

读取资源标志（Resource Flags）的辅助宏。

<a id="r_ga3a3669237762fa8c23686e5e00b7809f"></a>

```c
#define LWM2M_RD_CLIENT_FLAG_BOOTSTRAP BIT(0)
```

相关声明：[LWM2M_RD_CLIENT_FLAG_BOOTSTRAP](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3a3669237762fa8c23686e5e00b7809f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

在当前会话（Session）中运行引导过程（Bootstrap Procedure）。

<a id="r_gab97329844cd411195add5d72ad6aa4b7"></a>

```c
#define LWM2M_MAX_PATH_STR_SIZE sizeof("/65535/65535/65535/65535")
```

相关声明：[LWM2M_MAX_PATH_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab97329844cd411195add5d72ad6aa4b7)。

LwM2M 路径（Path）的最大长度。

<a id="define-members-0"></a>

### 由 OMA 为 LwM2M 技术规范管理的 LwM2M 对象（LwM2M Objects managed by OMA for LwM2M tech specification.）

此范围内的对象（Objects）标识符（IDs）为 `0–1023`。

<a id="r_ga785e4a647a2cf93194a249537223ab0f"></a>

```c
#define LWM2M_OBJECT_SECURITY_ID 0
```

相关声明：[LWM2M_OBJECT_SECURITY_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga785e4a647a2cf93194a249537223ab0f)。

安全对象（Security Object）。

<a id="r_gace7b2f0a1f97b6e99c0958a8382ca0d2"></a>

```c
#define LWM2M_OBJECT_SERVER_ID 1
```

相关声明：[LWM2M_OBJECT_SERVER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gace7b2f0a1f97b6e99c0958a8382ca0d2)。

服务器对象（Server Object）。

<a id="r_gaa8387c8838f952c7c60602e2952c7f55"></a>

```c
#define LWM2M_OBJECT_ACCESS_CONTROL_ID 2
```

相关声明：[LWM2M_OBJECT_ACCESS_CONTROL_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaa8387c8838f952c7c60602e2952c7f55)。

访问控制对象（Access Control Object）。

<a id="r_ga699f585b320ab5b259d4fb2bda10eb78"></a>

```c
#define LWM2M_OBJECT_DEVICE_ID 3
```

相关声明：[LWM2M_OBJECT_DEVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga699f585b320ab5b259d4fb2bda10eb78)。

设备对象。

<a id="r_ga73db8616cc7dbbd04267d97a743b8ec0"></a>

```c
#define LWM2M_OBJECT_CONNECTIVITY_MONITORING_ID 4
```

相关声明：[LWM2M_OBJECT_CONNECTIVITY_MONITORING_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga73db8616cc7dbbd04267d97a743b8ec0)。

连接监测对象（Connectivity Monitoring Object）。

<a id="r_ga442cc51c7d0807a752ce4affe9221c5b"></a>

```c
#define LWM2M_OBJECT_FIRMWARE_ID 5
```

相关声明：[LWM2M_OBJECT_FIRMWARE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga442cc51c7d0807a752ce4affe9221c5b)。

固件对象（Firmware Object）。

<a id="r_ga1046ec68deab3d812d7e5921fb718028"></a>

```c
#define LWM2M_OBJECT_LOCATION_ID 6
```

相关声明：[LWM2M_OBJECT_LOCATION_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1046ec68deab3d812d7e5921fb718028)。

位置对象（Location Object）。

<a id="r_gaa6c374c401dd36b6e121ac48c91ca9cf"></a>

```c
#define LWM2M_OBJECT_CONNECTIVITY_STATISTICS_ID 7
```

相关声明：[LWM2M_OBJECT_CONNECTIVITY_STATISTICS_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaa6c374c401dd36b6e121ac48c91ca9cf)。

连接统计对象（Connectivity Statistics Object）。

<a id="r_gac2d140b4a36d6010fe93bca443a658c0"></a>

```c
#define LWM2M_OBJECT_SOFTWARE_MANAGEMENT_ID 9
```

相关声明：[LWM2M_OBJECT_SOFTWARE_MANAGEMENT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac2d140b4a36d6010fe93bca443a658c0)。

软件管理对象（Software Management Object）。

<a id="r_ga4b4ce912a4554923974461ea3c76007e"></a>

```c
#define LWM2M_OBJECT_PORTFOLIO_ID 16
```

相关声明：[LWM2M_OBJECT_PORTFOLIO_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4b4ce912a4554923974461ea3c76007e)。

信息组合对象（Portfolio Object）。

<a id="r_ga85eabde1900ef052064d34cf5e3a4afe"></a>

```c
#define LWM2M_OBJECT_BINARYAPPDATACONTAINER_ID 19
```

相关声明：[LWM2M_OBJECT_BINARYAPPDATACONTAINER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga85eabde1900ef052064d34cf5e3a4afe)。

二进制应用数据容器对象（Binary App Data Container Object）。

<a id="r_ga4f0455fb0271c2fcbb7dadb944431ff0"></a>

```c
#define LWM2M_OBJECT_EVENT_LOG_ID 20
```

相关声明：[LWM2M_OBJECT_EVENT_LOG_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4f0455fb0271c2fcbb7dadb944431ff0)。

事件日志对象（Event Log Object）。

<a id="r_gab13a1600a662ed1dbd8845c6d7d4549a"></a>

```c
#define LWM2M_OBJECT_OSCORE_ID 21
```

相关声明：[LWM2M_OBJECT_OSCORE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab13a1600a662ed1dbd8845c6d7d4549a)。

受限 RESTful 环境对象安全（OSCORE）对象。

<a id="r_ga3505e9ddcd54afe86e8bd5fbc03fb565"></a>

```c
#define LWM2M_OBJECT_GATEWAY_ID 25
```

相关声明：[LWM2M_OBJECT_GATEWAY_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3505e9ddcd54afe86e8bd5fbc03fb565)。

网关对象（Gateway Object）。

<a id="define-members-1"></a>

### 由第三方标准制定方提供的 LwM2M 对象（LwM2M Objects produced by 3rd party Standards Development）

组织（Organizations）。

参见 [OMA 轻量级机器到机器通信（LwM2M）对象与资源注册表（Object and Resource Registry）原链接](http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html)。译注：核验时，旧链接已重定向至 OMA 规范总入口；当前官方注册表位于 [LwM2M Objects](https://www.openmobilealliance.org/specifications/registries/objects/)，其中保留对象标识符分类及注册表入口。

<a id="r_gaeef485c23d306c93fc0f45dd58766ad9"></a>

```c
#define IPSO_OBJECT_GENERIC_SENSOR_ID 3300
```

相关声明：[IPSO_OBJECT_GENERIC_SENSOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeef485c23d306c93fc0f45dd58766ad9)。

IPSO 通用传感器对象（Generic Sensor Object）。

<a id="r_ga3b0c046d93c7bcee9d4da121dd574ff0"></a>

```c
#define IPSO_OBJECT_TEMP_SENSOR_ID 3303
```

相关声明：[IPSO_OBJECT_TEMP_SENSOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3b0c046d93c7bcee9d4da121dd574ff0)。

IPSO 温度传感器对象（Temperature Sensor Object）。

<a id="r_ga8075d8b7eb3b4c98f621efef673bb11f"></a>

```c
#define IPSO_OBJECT_HUMIDITY_SENSOR_ID 3304
```

相关声明：[IPSO_OBJECT_HUMIDITY_SENSOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga8075d8b7eb3b4c98f621efef673bb11f)。

IPSO 湿度传感器对象（Humidity Sensor Object）。

<a id="r_ga56ebac5260ee467b3763abe49ff3b8ff"></a>

```c
#define IPSO_OBJECT_LIGHT_CONTROL_ID 3311
```

相关声明：[IPSO_OBJECT_LIGHT_CONTROL_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga56ebac5260ee467b3763abe49ff3b8ff)。

IPSO 灯光控制对象（Light Control Object）。

<a id="r_ga0b3b9db806e5fe47cc08de34b5fb35fe"></a>

```c
#define IPSO_OBJECT_ACCELEROMETER_ID 3313
```

相关声明：[IPSO_OBJECT_ACCELEROMETER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga0b3b9db806e5fe47cc08de34b5fb35fe)。

IPSO 加速度计对象（Accelerometer Object）。

<a id="r_ga6abcf3c5cf5001a4fdb7915336325ce1"></a>

```c
#define IPSO_OBJECT_MAGNETOMETER_ID 3314
```

相关声明：[IPSO_OBJECT_MAGNETOMETER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6abcf3c5cf5001a4fdb7915336325ce1)。

IPSO 磁力计对象（Magnetometer Object）。

<a id="r_ga270a1b5a576d72099287633b32ce909f"></a>

```c
#define IPSO_OBJECT_VOLTAGE_SENSOR_ID 3316
```

相关声明：[IPSO_OBJECT_VOLTAGE_SENSOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga270a1b5a576d72099287633b32ce909f)。

IPSO 电压传感器对象（Voltage Sensor Object）。

<a id="r_gae511fd54112829e63c691776750893c2"></a>

```c
#define IPSO_OBJECT_CURRENT_SENSOR_ID 3317
```

相关声明：[IPSO_OBJECT_CURRENT_SENSOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae511fd54112829e63c691776750893c2)。

IPSO 电流传感器对象（Current Sensor Object）。

<a id="r_ga752f81e91d0965a50ecfb0679bdea6ba"></a>

```c
#define IPSO_OBJECT_PRESSURE_ID 3323
```

相关声明：[IPSO_OBJECT_PRESSURE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga752f81e91d0965a50ecfb0679bdea6ba)。

IPSO 压力传感器对象（Pressure Sensor Object）。

<a id="r_ga46075c78a3cd73f3313abf5ffeca697b"></a>

```c
#define IPSO_OBJECT_TIME_ID 3333
```

相关声明：[IPSO_OBJECT_TIME_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga46075c78a3cd73f3313abf5ffeca697b)。

IPSO 时间对象（Time Object）。

<a id="r_ga15d664ddbfbf4d5b25dde34a5c650e6b"></a>

```c
#define IPSO_OBJECT_BUZZER_ID 3338
```

相关声明：[IPSO_OBJECT_BUZZER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga15d664ddbfbf4d5b25dde34a5c650e6b)。

IPSO 蜂鸣器对象（Buzzer Object）。

<a id="r_ga6c7bd5880fa22050748c2cb01981cbcb"></a>

```c
#define IPSO_OBJECT_TIMER_ID 3340
```

相关声明：[IPSO_OBJECT_TIMER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6c7bd5880fa22050748c2cb01981cbcb)。

IPSO 定时器对象（Timer Object）。

<a id="r_ga776a6a5e1eab3a8de0a39382f94b663a"></a>

```c
#define IPSO_OBJECT_ONOFF_SWITCH_ID 3342
```

相关声明：[IPSO_OBJECT_ONOFF_SWITCH_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga776a6a5e1eab3a8de0a39382f94b663a)。

IPSO 通断开关对象（On/Off Switch Object）。

<a id="r_ga6e3119bc8f0b9143ab384e82a5bccf7c"></a>

```c
#define IPSO_OBJECT_PUSH_BUTTON_ID 3347
```

相关声明：[IPSO_OBJECT_PUSH_BUTTON_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6e3119bc8f0b9143ab384e82a5bccf7c)。

IPSO 按钮对象（Push Button Object）。

<a id="r_gacdd09a26ce52f36c644a89a8b89f7d32"></a>

```c
#define UCIFI_OBJECT_BATTERY_ID 3411
```

相关声明：[UCIFI_OBJECT_BATTERY_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gacdd09a26ce52f36c644a89a8b89f7d32)。

uCIFI 电池对象（Battery Object）。

<a id="r_ga21f6bc6255f5f5ed28881fa797d026ca"></a>

```c
#define IPSO_OBJECT_FILLING_LEVEL_SENSOR_ID 3435
```

相关声明：[IPSO_OBJECT_FILLING_LEVEL_SENSOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga21f6bc6255f5f5ed28881fa797d026ca)。

IPSO 填充液位传感器对象（Filling Level Sensor Object）。

<a id="define-members-2"></a>

### 用于“可用电源”资源的电源类型（Power source types used for the "Available Power Sources" resource of）

LwM2M 设备对象（Device Object）的 `3/0/6`。

<a id="r_gae154ca2e54ec7759dd43f2a7a275077e"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_DC_POWER 0
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_DC_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae154ca2e54ec7759dd43f2a7a275077e)。

直流电源（DC Power）。

<a id="r_ga04ca8ac536eed7d411c1b1ea2b2a59ac"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_BAT_INT 1
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_BAT_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga04ca8ac536eed7d411c1b1ea2b2a59ac)。

内部电池（Internal Battery）。

<a id="r_gaf12052f903a688712928d036b782f621"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_BAT_EXT 2
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_BAT_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf12052f903a688712928d036b782f621)。

外部电池（External Battery）。

<a id="r_ga10c4633c97881ca7d87c748aaeec68c9"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_FUEL_CELL 3
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_FUEL_CELL](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga10c4633c97881ca7d87c748aaeec68c9)。

燃料电池（Fuel Cell）。

<a id="r_ga72352523996e61ea93caff0bb80c42ba"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_PWR_OVER_ETH 4
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_PWR_OVER_ETH](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga72352523996e61ea93caff0bb80c42ba)。

以太网供电（Power over Ethernet）。

<a id="r_ga4877877be75d3dd3c8f600b438b7ea8e"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_USB 5
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_USB](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4877877be75d3dd3c8f600b438b7ea8e)。

通用串行总线（USB）

<a id="r_ga97b9d38ec402478f10642f1f83a4f88a"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_AC_POWER 6
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_AC_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga97b9d38ec402478f10642f1f83a4f88a)。

交流市电（AC Mains Power）。

<a id="r_gaa41ec1d2ca43e1385cfb11204aff729d"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_SOLAR 7
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_SOLAR](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaa41ec1d2ca43e1385cfb11204aff729d)。

太阳能（Solar）。

<a id="r_gae7a580aac1804abbcf3feb57a5a30a02"></a>

```c
#define LWM2M_DEVICE_PWR_SRC_TYPE_MAX 8
```

相关声明：[LWM2M_DEVICE_PWR_SRC_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae7a580aac1804abbcf3feb57a5a30a02)。

可用电源类型（Available Power Source Type）的最大值。

<a id="define-members-3"></a>

### 用于 LwM2M 设备“错误码”资源的错误码（Error codes used for the "Error Code" resource of the LwM2M Device）

对象（Object）

LwM2M 客户端可以通过 `lwm2m_device_add_err()` 函数注册以下错误码（Error Codes）之一。

<a id="r_gad54ec75eb2843d5eed199ddedca6ef4f"></a>

```c
#define LWM2M_DEVICE_ERROR_NONE 0
```

相关声明：[LWM2M_DEVICE_ERROR_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad54ec75eb2843d5eed199ddedca6ef4f)。

无错误（No Error）。

<a id="r_ga53a9ee1ae09dd32a8dc2df6018798f9f"></a>

```c
#define LWM2M_DEVICE_ERROR_LOW_POWER 1
```

相关声明：[LWM2M_DEVICE_ERROR_LOW_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga53a9ee1ae09dd32a8dc2df6018798f9f)。

电池电量低（Low Battery Power）。

<a id="r_ga33152ea4ef497b02a12d1218d470a5a6"></a>

```c
#define LWM2M_DEVICE_ERROR_EXT_POWER_SUPPLY_OFF 2
```

相关声明：[LWM2M_DEVICE_ERROR_EXT_POWER_SUPPLY_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga33152ea4ef497b02a12d1218d470a5a6)。

外部电源关闭（External Power Supply Off）。

<a id="r_ga3c1b7693167ff517c5cbd7bbdbfd1ea0"></a>

```c
#define LWM2M_DEVICE_ERROR_GPS_FAILURE 3
```

相关声明：[LWM2M_DEVICE_ERROR_GPS_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3c1b7693167ff517c5cbd7bbdbfd1ea0)。

全球定位系统（GPS）模块故障。

<a id="r_ga78048382d8bc85bbabbff58f0a9860f2"></a>

```c
#define LWM2M_DEVICE_ERROR_LOW_SIGNAL_STRENGTH 4
```

相关声明：[LWM2M_DEVICE_ERROR_LOW_SIGNAL_STRENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga78048382d8bc85bbabbff58f0a9860f2)。

接收信号强度低（Low Received Signal Strength）。

<a id="r_ga94ce0177c066dd43ef660b85afc83485"></a>

```c
#define LWM2M_DEVICE_ERROR_OUT_OF_MEMORY 5
```

相关声明：[LWM2M_DEVICE_ERROR_OUT_OF_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga94ce0177c066dd43ef660b85afc83485)。

内存不足。

<a id="r_gabcb39cd3757ea60859984f6ad0df9e31"></a>

```c
#define LWM2M_DEVICE_ERROR_SMS_FAILURE 6
```

相关声明：[LWM2M_DEVICE_ERROR_SMS_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabcb39cd3757ea60859984f6ad0df9e31)。

短信（SMS）故障。

<a id="r_ga2110d71a0c58087ff877e66b7500ba66"></a>

```c
#define LWM2M_DEVICE_ERROR_NETWORK_FAILURE 7
```

相关声明：[LWM2M_DEVICE_ERROR_NETWORK_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga2110d71a0c58087ff877e66b7500ba66)。

IP 连接故障（IP Connectivity Failure）。

<a id="r_ga77e6352eace8116576c880bf7e416ba3"></a>

```c
#define LWM2M_DEVICE_ERROR_PERIPHERAL_FAILURE 8
```

相关声明：[LWM2M_DEVICE_ERROR_PERIPHERAL_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga77e6352eace8116576c880bf7e416ba3)。

外设故障（Peripheral Malfunction）。

<a id="define-members-4"></a>

### 用于“电池状态”资源（3/0/20）的电池状态码（Battery status codes used for the "Battery Status" resource (3/0/20)）

属于 LwM2M 设备对象（Device Object）。

电池状态（Battery Status）变化时，LwM2M 客户端可以通过 `lwm2m_set_u8("3/0/20", [battery status])` 设置以下编码之一。

<a id="r_ga4329c971f95f1c345381d1c864a9f334"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_NORMAL 0
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4329c971f95f1c345381d1c864a9f334)。

电池工作正常，且未接入外部电源（Not on Power）。

<a id="r_gaf19da3a566782aeebebfb6ff110a9152"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_CHARGING 1
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_CHARGING](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf19da3a566782aeebebfb6ff110a9152)。

电池当前正在充电（Charging）。

<a id="r_ga5f7e88b52d8e6029467a2ed10585e6d4"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_CHARGE_COMP 2
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_CHARGE_COMP](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga5f7e88b52d8e6029467a2ed10585e6d4)。

电池已充满（Fully Charged），充电器仍连接。

<a id="r_gaa3f81df5e4d45838922eb20a15ee3153"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_DAMAGED 3
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_DAMAGED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaa3f81df5e4d45838922eb20a15ee3153)。

电池存在问题（Battery Problem）。

<a id="r_ga578f6446ec1b70d2a32917abf1f5aad7"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_LOW 4
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga578f6446ec1b70d2a32917abf1f5aad7)。

电池剩余电量低（Low on Charge）。

<a id="r_gacc3dfc99fc2cd9ef7048b1a0a0fd55c8"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_NOT_INST 5
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_NOT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gacc3dfc99fc2cd9ef7048b1a0a0fd55c8)。

未安装电池（Battery Not Installed）。

<a id="r_ga174e118b07982b87c6c083236b79c3b7"></a>

```c
#define LWM2M_DEVICE_BATTERY_STATUS_UNKNOWN 6
```

相关声明：[LWM2M_DEVICE_BATTERY_STATUS_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga174e118b07982b87c6c083236b79c3b7)。

无法获取电池信息（Battery Information Not Available）。

<a id="define-members-5"></a>

### LwM2M 固件更新对象的状态（LwM2M Firmware Update object states）

LwM2M 客户端或 LwM2M 固件更新对象（Firmware Update Object）使用以下编码表示 LwM2M 固件更新状态（Firmware Update State），路径为 `5/0/3`。

<a id="r_gaafff27c7165f059a969fe60fee51f683"></a>

```c
#define STATE_IDLE 0
```

相关声明：[STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaafff27c7165f059a969fe60fee51f683)。

空闲（Idle）。

<a id="r_gaeb34e88a0da4ac1274ae6b2cef010086"></a>

```c
#define STATE_DOWNLOADING 1
```

相关声明：[STATE_DOWNLOADING](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb34e88a0da4ac1274ae6b2cef010086)。

正在下载（Downloading）。

<a id="r_ga009085120be71a28c1f6ebdaf7503365"></a>

```c
#define STATE_DOWNLOADED 2
```

相关声明：[STATE_DOWNLOADED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga009085120be71a28c1f6ebdaf7503365)。

已下载（Downloaded）。

<a id="r_gaac1dab8d1ac28bf13faeee39d1df47c5"></a>

```c
#define STATE_UPDATING 3
```

相关声明：[STATE_UPDATING](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaac1dab8d1ac28bf13faeee39d1df47c5)。

正在更新（Updating）。

<a id="define-members-6"></a>

### LwM2M 固件更新对象的结果码（LwM2M Firmware Update object result codes）

处理固件更新后，客户端通过 `lwm2m_set_u8("5/0/5", [result code])`，使用以下结果码（Result Codes）之一设置结果。

<a id="r_ga391b47507468bbc1005903a56f80b1ea"></a>

```c
#define RESULT_DEFAULT 0
```

相关声明：[RESULT_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga391b47507468bbc1005903a56f80b1ea)。

初始值（Initial Value）。

<a id="r_ga7cc1753a05a0821f6c70dd2bccfbab5c"></a>

```c
#define RESULT_SUCCESS 1
```

相关声明：[RESULT_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7cc1753a05a0821f6c70dd2bccfbab5c)。

固件更新成功（Firmware Updated Successfully）。

<a id="r_ga829f7bc83b67dcf16ea4775addd87343"></a>

```c
#define RESULT_NO_STORAGE 2
```

相关声明：[RESULT_NO_STORAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga829f7bc83b67dcf16ea4775addd87343)。

闪存（Flash Memory）空间不足，无法存放新的固件包（Firmware Package）。

<a id="r_gab5446111a8969aa2c66dae49f04c93cf"></a>

```c
#define RESULT_OUT_OF_MEM 3
```

相关声明：[RESULT_OUT_OF_MEM](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab5446111a8969aa2c66dae49f04c93cf)。

下载过程中随机存取存储器（RAM）不足。

<a id="r_ga0655ba8c402d8b6c8bbd84fb36447bd4"></a>

```c
#define RESULT_CONNECTION_LOST 4
```

相关声明：[RESULT_CONNECTION_LOST](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga0655ba8c402d8b6c8bbd84fb36447bd4)。

下载过程中连接丢失（Connection Lost）。

<a id="r_gadfd0ac7b6a3fededa2b4471dfe52d3d2"></a>

```c
#define RESULT_INTEGRITY_FAILED 5
```

相关声明：[RESULT_INTEGRITY_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gadfd0ac7b6a3fededa2b4471dfe52d3d2)。

新下载的软件包（Package）完整性检查（Integrity Check）失败。

<a id="r_gab06dbfdac0c95f8100908a1177f3a62a"></a>

```c
#define RESULT_UNSUP_FW 6
```

相关声明：[RESULT_UNSUP_FW](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab06dbfdac0c95f8100908a1177f3a62a)。

不支持的软件包类型（Package Type）。

<a id="r_ga268204053d7e23737283523224699979"></a>

```c
#define RESULT_INVALID_URI 7
```

相关声明：[RESULT_INVALID_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga268204053d7e23737283523224699979)。

统一资源标识符（URI）无效。

<a id="r_ga2dfdd95c2c03ccca25d855b6d6f96ed3"></a>

```c
#define RESULT_UPDATE_FAILED 8
```

相关声明：[RESULT_UPDATE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga2dfdd95c2c03ccca25d855b6d6f96ed3)。

固件更新失败（Firmware Update Failed）。

<a id="r_gade3da37a44ee40292ec6344403db8d8d"></a>

```c
#define RESULT_UNSUP_PROTO 9
```

相关声明：[RESULT_UNSUP_PROTO](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gade3da37a44ee40292ec6344403db8d8d)。

不支持的协议（Protocol）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.3\_类型定义（Typedefs）

<a id="r_gae7bf50f9abf1b82b76ac3e9175e685ac"></a>

```c
typedef void(* lwm2m_socket_fault_cb_t) (int error)
```

相关声明：[lwm2m_socket_fault_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae7bf50f9abf1b82b76ac3e9175e685ac)。

遇到套接字错误（Socket Error）时调用的回调函数。

<a id="r_gad7bea67e16e1e831e0f949dbf83d5afe"></a>

```c
typedef void(* lwm2m_observe_cb_t) (enum lwm2m_observe_event event, struct lwm2m_obj_path *path, void *user_data)
```

相关声明：[lwm2m_observe_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad7bea67e16e1e831e0f949dbf83d5afe)、[lwm2m_observe_event](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac8d63952ec94ca6cfb1dbe12a6c53bfb)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

观察（Observe）回调，报告观察者（Observer）的添加与删除，以及通知的确认（ACK）与超时。

<a id="r_ga38dbaf038426efc75d889c4a0666dac9"></a>

```c
typedef void(* lwm2m_ctx_event_cb_t) (struct lwm2m_ctx *ctx, enum lwm2m_rd_client_event event)
```

相关声明：[lwm2m_ctx_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga38dbaf038426efc75d889c4a0666dac9)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[lwm2m_rd_client_event](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaca90ab8960a4ff01d44735dbc0405862)。

异步注册／发现客户端事件回调（Asynchronous RD Client Event Callback）。

<a id="r_ga92d2227f37e7d382bc4f1a7bae21b872"></a>

```c
typedef int(* lwm2m_set_sockopt_cb_t) (struct lwm2m_ctx *client_ctx)
```

相关声明：[lwm2m_set_sockopt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga92d2227f37e7d382bc4f1a7bae21b872)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

<a id="r_ga7a0bb9d5652f7f0fd0cc4a1139be6f37"></a>

```c
typedef bool(* lwm2m_cache_filter_cb_t) (const struct lwm2m_obj_path *path, const struct lwm2m_time_series_elem *element)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[lwm2m_cache_filter_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7a0bb9d5652f7f0fd0cc4a1139be6f37)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_time_series_elem](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md)。

用于过滤缓存时间序列样本（Cached Time Series Samples）的回调类型。

<a id="r_ga5e531aade0537eb5e3f5756e9287e384"></a>

```c
typedef void *(* lwm2m_engine_get_data_cb_t) (uint16_t obj_inst_id, uint16_t res_id, uint16_t res_inst_id, size_t *data_len)
```

相关声明：[lwm2m_engine_get_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga5e531aade0537eb5e3f5756e9287e384)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

用于获取资源缓冲区（Resource Buffer）及其长度的异步回调（Asynchronous Callback）。

<a id="r_ga3afac013b0cf731f9c86dc3791131585"></a>

```c
typedef int(* lwm2m_engine_set_data_cb_t) (uint16_t obj_inst_id, uint16_t res_id, uint16_t res_inst_id, uint8_t *data, uint16_t data_len, bool last_block, size_t total_size, size_t offset)
```

相关声明：[lwm2m_engine_set_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3afac013b0cf731f9c86dc3791131585)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

数据已写入资源缓冲区（Resource Buffer）时调用的异步回调（Asynchronous Callback）。

<a id="r_gabcbca483b310e0c4cd68aef2d9cda0bf"></a>

```c
typedef int(* lwm2m_engine_user_cb_t) (uint16_t obj_inst_id)
```

相关声明：[lwm2m_engine_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabcbca483b310e0c4cd68aef2d9cda0bf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

异步事件通知回调（Asynchronous Event Notification Callback）。

<a id="r_gaeb32bcd4981b4c7bd891f99668ebc0fe"></a>

```c
typedef int(* lwm2m_engine_execute_cb_t) (uint16_t obj_inst_id, uint8_t *args, uint16_t args_len)
```

相关声明：[lwm2m_engine_execute_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb32bcd4981b4c7bd891f99668ebc0fe)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

异步执行通知回调（Asynchronous Execute Notification Callback）。

<a id="r_gaf5394884da53edb28fe4afc92bf40e6a"></a>

```c
typedef void(* lwm2m_send_cb_t) (enum lwm2m_send_status status)
```

相关声明：[lwm2m_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf5394884da53edb28fe4afc92bf40e6a)、[lwm2m_send_status](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga20848e0942882e8c2cc40ee8a48b7bfd)。

返回发送状态（Send Status）的回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.4\_枚举（Enumerations）

<a id="r_gac8d63952ec94ca6cfb1dbe12a6c53bfb"></a>

```c
enum lwm2m_observe_event { LWM2M_OBSERVE_EVENT_OBSERVER_ADDED , LWM2M_OBSERVE_EVENT_OBSERVER_REMOVED , LWM2M_OBSERVE_EVENT_NOTIFY_ACK , LWM2M_OBSERVE_EVENT_NOTIFY_TIMEOUT }
```

相关声明：[lwm2m_observe_event](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac8d63952ec94ca6cfb1dbe12a6c53bfb)、[LWM2M_OBSERVE_EVENT_OBSERVER_ADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggac8d63952ec94ca6cfb1dbe12a6c53bfba22f4341d713417110d9866b0cbd318e3)、[LWM2M_OBSERVE_EVENT_OBSERVER_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggac8d63952ec94ca6cfb1dbe12a6c53bfbae3f4af98b52ee191229c660748c7dd6c)、[LWM2M_OBSERVE_EVENT_NOTIFY_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggac8d63952ec94ca6cfb1dbe12a6c53bfbaab4e1cf0451ba926b90ea21152cac885)、[LWM2M_OBSERVE_EVENT_NOTIFY_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggac8d63952ec94ca6cfb1dbe12a6c53bfba55494fd6e76f585894e34dc9004fbc9e)。

观察回调事件（Observe Callback Events）。

<a id="r_gaca90ab8960a4ff01d44735dbc0405862"></a>

```c
enum lwm2m_rd_client_event { LWM2M_RD_CLIENT_EVENT_NONE , LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_FAILURE , LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_COMPLETE , LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_TRANSFER_COMPLETE , LWM2M_RD_CLIENT_EVENT_REGISTRATION_FAILURE , LWM2M_RD_CLIENT_EVENT_REGISTRATION_COMPLETE , LWM2M_RD_CLIENT_EVENT_REG_TIMEOUT , LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE , LWM2M_RD_CLIENT_EVENT_DEREGISTER_FAILURE , LWM2M_RD_CLIENT_EVENT_DISCONNECT , LWM2M_RD_CLIENT_EVENT_QUEUE_MODE_RX_OFF , LWM2M_RD_CLIENT_EVENT_ENGINE_SUSPENDED , LWM2M_RD_CLIENT_EVENT_NETWORK_ERROR , LWM2M_RD_CLIENT_EVENT_REG_UPDATE , LWM2M_RD_CLIENT_EVENT_DEREGISTER , LWM2M_RD_CLIENT_EVENT_SERVER_DISABLED }
```

相关声明：[lwm2m_rd_client_event](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaca90ab8960a4ff01d44735dbc0405862)、[LWM2M_RD_CLIENT_EVENT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862aca4ebc8d550af02f1891eed1a7b1afcc)、[LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ac089b900494522de565e36d31ea3b0c4)、[LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ac30dd8520e591c8e51c74ce1a53cd524)、[LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_TRANSFER_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a7c7c3115b6ff16dfa722b6b82c2cd1bc)、[LWM2M_RD_CLIENT_EVENT_REGISTRATION_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ae89498cad338b1dc9cbd3b23838bf0b6)、[LWM2M_RD_CLIENT_EVENT_REGISTRATION_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a8994ea8c025cbbd56adcc050a7e86541)、[LWM2M_RD_CLIENT_EVENT_REG_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a90341c0d9584681f18d1cae91c9f6404)、[LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a9f53175c5e935f061a83aa1fcfe9f683)、[LWM2M_RD_CLIENT_EVENT_DEREGISTER_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a32552b56152f9a714675fc6bba3b3d5f)、[LWM2M_RD_CLIENT_EVENT_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ac6703e7d0809cc9cfcdd1cbd48e2318b)、[LWM2M_RD_CLIENT_EVENT_QUEUE_MODE_RX_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a7c7853536c452da2f74e9f43a024fcbe)、[LWM2M_RD_CLIENT_EVENT_ENGINE_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862afd4eda5dee31b18b1da5414481e33525)、[LWM2M_RD_CLIENT_EVENT_NETWORK_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862aff939a86c623ab8258c707361b95aef4)、[LWM2M_RD_CLIENT_EVENT_REG_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ab48772aeed0ead72f3a9289a618af1cd)、[LWM2M_RD_CLIENT_EVENT_DEREGISTER](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862aac3938a209800a0de0a05b21fab02c13)、[LWM2M_RD_CLIENT_EVENT_SERVER_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a873a4a3190dc7c24d2518dc8d7268763)。

LwM2M 注册／发现客户端事件（RD Client Events）。

<a id="r_ga7611c1aebb0309ee8340e06dd8ee234d"></a>

```c
enum lwm2m_socket_states { LWM2M_SOCKET_STATE_ONGOING , LWM2M_SOCKET_STATE_ONE_RESPONSE , LWM2M_SOCKET_STATE_LAST , LWM2M_SOCKET_STATE_NO_DATA }
```

相关声明：[lwm2m_socket_states](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7611c1aebb0309ee8340e06dd8ee234d)、[LWM2M_SOCKET_STATE_ONGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga7611c1aebb0309ee8340e06dd8ee234daa0f06bc70659598b0f51b3ce8094c6ab)、[LWM2M_SOCKET_STATE_ONE_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga7611c1aebb0309ee8340e06dd8ee234da76aa03f71f44096d9413b1f5718d9711)、[LWM2M_SOCKET_STATE_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga7611c1aebb0309ee8340e06dd8ee234daed676a6deffe2de7c916bb6eb2906100)、[LWM2M_SOCKET_STATE_NO_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga7611c1aebb0309ee8340e06dd8ee234da2487ae8e93929bf62fd333cd04c5b915)。

LwM2M 套接字的不同流量状态（Traffic States）。

<a id="r_ga20848e0942882e8c2cc40ee8a48b7bfd"></a>

```c
enum lwm2m_send_status { LWM2M_SEND_STATUS_SUCCESS , LWM2M_SEND_STATUS_FAILURE , LWM2M_SEND_STATUS_TIMEOUT }
```

相关声明：[lwm2m_send_status](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga20848e0942882e8c2cc40ee8a48b7bfd)、[LWM2M_SEND_STATUS_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga20848e0942882e8c2cc40ee8a48b7bfda127cca7752ab3f00d5a4705f815b14b4)、[LWM2M_SEND_STATUS_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga20848e0942882e8c2cc40ee8a48b7bfda7a7f1720f39bedba28110fad09939dcd)、[LWM2M_SEND_STATUS_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga20848e0942882e8c2cc40ee8a48b7bfda7c0144cafd4f91a76d229b40df9cb82a)。

LwM2M 发送状态（Send Status）。

<a id="r_ga11de8078091631cb88b26a9a460097ab"></a>

```c
enum lwm2m_security_mode_e { LWM2M_SECURITY_PSK = 0 , LWM2M_SECURITY_RAW_PK = 1 , LWM2M_SECURITY_CERT = 2 , LWM2M_SECURITY_NOSEC = 3 , LWM2M_SECURITY_CERT_EST = 4 }
```

相关声明：[lwm2m_security_mode_e](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga11de8078091631cb88b26a9a460097ab)、[LWM2M_SECURITY_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097aba0d4e9d5160e91fc93e062dfb812edb25)、[LWM2M_SECURITY_RAW_PK](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097aba431ac48d7f0fed72ce5ab2c8ea823716)、[LWM2M_SECURITY_CERT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097aba6eef062c9f54bc9698a050c8bb2915ba)、[LWM2M_SECURITY_NOSEC](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097abaf6bb17f06d89124076810c132005f8d7)、[LWM2M_SECURITY_CERT_EST](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097abaefb45683a68002dab267c3fb2e876824)。

LwM2M 安全对象（Security Object）定义的安全模式（Security Modes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.5\_函数（Functions）

<a id="r_gabf8726f0438477863423947a7bb77ce2"></a>

```c
int lwm2m_device_add_err (uint8_t error_code)
```

相关声明：[lwm2m_device_add_err](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabf8726f0438477863423947a7bb77ce2)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 LwM2M 设备对象（Device Object）注册新的错误码（Error Code）。

<a id="r_ga6878ea0ebb512b19a4fb0859756f51d0"></a>

```c
void lwm2m_firmware_set_write_cb (lwm2m_engine_set_data_cb_t cb)
```

相关声明：[lwm2m_firmware_set_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6878ea0ebb512b19a4fb0859756f51d0)、[lwm2m_engine_set_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3afac013b0cf731f9c86dc3791131585)。

设置固件分块传输（Firmware Block Transfer）的数据回调。

<a id="r_ga4bf0bbedf5573ac18a11ac4fced11284"></a>

```c
lwm2m_engine_set_data_cb_t lwm2m_firmware_get_write_cb (void)
```

相关声明：[lwm2m_engine_set_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3afac013b0cf731f9c86dc3791131585)、[lwm2m_firmware_get_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4bf0bbedf5573ac18a11ac4fced11284)。

获取固件分块传输写入（Firmware Block Transfer Writes）的数据回调。

<a id="r_gac4e4a819e54344657d70ec479eb6ec8d"></a>

```c
void lwm2m_firmware_set_write_cb_inst (uint16_t obj_inst_id, lwm2m_engine_set_data_cb_t cb)
```

相关声明：[lwm2m_firmware_set_write_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac4e4a819e54344657d70ec479eb6ec8d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_set_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3afac013b0cf731f9c86dc3791131585)。

设置固件分块传输（Firmware Block Transfer）的数据回调。

<a id="r_gad7334f06c3bdb14485597794a417152d"></a>

```c
lwm2m_engine_set_data_cb_t lwm2m_firmware_get_write_cb_inst (uint16_t obj_inst_id)
```

相关声明：[lwm2m_engine_set_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3afac013b0cf731f9c86dc3791131585)、[lwm2m_firmware_get_write_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad7334f06c3bdb14485597794a417152d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取固件分块传输写入（Firmware Block Transfer Writes）的数据回调。

<a id="r_ga3955dca5cd6d67807ed75e61a4d84d84"></a>

```c
void lwm2m_firmware_set_cancel_cb (lwm2m_engine_user_cb_t cb)
```

相关声明：[lwm2m_firmware_set_cancel_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3955dca5cd6d67807ed75e61a4d84d84)、[lwm2m_engine_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabcbca483b310e0c4cd68aef2d9cda0bf)。

设置固件更新取消（Firmware Update Cancel）回调。

<a id="r_ga9561c1b8407d888f6fbe1e0ceab1c235"></a>

```c
lwm2m_engine_user_cb_t lwm2m_firmware_get_cancel_cb (void)
```

相关声明：[lwm2m_engine_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabcbca483b310e0c4cd68aef2d9cda0bf)、[lwm2m_firmware_get_cancel_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9561c1b8407d888f6fbe1e0ceab1c235)。

获取固件更新取消（Firmware Update Cancel）回调。

<a id="r_gaa200b524e505f64247f1e7472c5f36d4"></a>

```c
void lwm2m_firmware_set_cancel_cb_inst (uint16_t obj_inst_id, lwm2m_engine_user_cb_t cb)
```

相关声明：[lwm2m_firmware_set_cancel_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaa200b524e505f64247f1e7472c5f36d4)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabcbca483b310e0c4cd68aef2d9cda0bf)。

设置固件更新取消（Firmware Update Cancel）的数据回调。

<a id="r_ga6f4b3e08c7e03cff4bf31e2f2999971e"></a>

```c
lwm2m_engine_user_cb_t lwm2m_firmware_get_cancel_cb_inst (uint16_t obj_inst_id)
```

相关声明：[lwm2m_engine_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabcbca483b310e0c4cd68aef2d9cda0bf)、[lwm2m_firmware_get_cancel_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6f4b3e08c7e03cff4bf31e2f2999971e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取固件更新取消（Firmware Update Cancel）回调。

<a id="r_ga61eb38e42d9e1b3f467c43a324f2fc65"></a>

```c
void lwm2m_firmware_set_update_cb (lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_firmware_set_update_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga61eb38e42d9e1b3f467c43a324f2fc65)、[lwm2m_engine_execute_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置用于处理固件更新执行事件（Firmware Update Execute Events）的数据回调。

<a id="r_ga1e4b8ba1b19ac9025dca3c4799bba84a"></a>

```c
lwm2m_engine_execute_cb_t lwm2m_firmware_get_update_cb (void)
```

相关声明：[lwm2m_engine_execute_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb32bcd4981b4c7bd891f99668ebc0fe)、[lwm2m_firmware_get_update_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1e4b8ba1b19ac9025dca3c4799bba84a)。

获取固件更新执行事件（Firmware Update Execute Events）的事件回调。

<a id="r_ga31d0f3e40b5e3d608d16a4268b2f1b29"></a>

```c
void lwm2m_firmware_set_update_cb_inst (uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_firmware_set_update_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga31d0f3e40b5e3d608d16a4268b2f1b29)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_execute_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置用于处理固件更新执行事件（Firmware Update Execute Events）的数据回调。

<a id="r_ga34995e902b63c4d7d37ebd709d88a72a"></a>

```c
lwm2m_engine_execute_cb_t lwm2m_firmware_get_update_cb_inst (uint16_t obj_inst_id)
```

相关声明：[lwm2m_engine_execute_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb32bcd4981b4c7bd891f99668ebc0fe)、[lwm2m_firmware_get_update_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga34995e902b63c4d7d37ebd709d88a72a)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取固件更新执行事件（Firmware Update Execute Events）的事件回调。

<a id="r_gac374d0559056ddb9cf43deae932fd128"></a>

```c
int lwm2m_swmgmt_set_activate_cb (uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_swmgmt_set_activate_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac374d0559056ddb9cf43deae932fd128)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_execute_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置处理软件激活请求（Software Activation Requests）的回调。

<a id="r_ga7a2b93b918257bece819dc44804f27f5"></a>

```c
int lwm2m_swmgmt_set_deactivate_cb (uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_swmgmt_set_deactivate_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7a2b93b918257bece819dc44804f27f5)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_execute_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置处理软件停用请求（Software Deactivation Requests）的回调。

<a id="r_gadfc00060c0b538ed576b5e3edd7dac80"></a>

```c
int lwm2m_swmgmt_set_install_package_cb (uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_swmgmt_set_install_package_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gadfc00060c0b538ed576b5e3edd7dac80)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_execute_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置处理软件安装请求（Software Install Requests）的回调。

<a id="r_gacf209563efdc5f3201152088c52d05c3"></a>

```c
int lwm2m_swmgmt_set_delete_package_cb (uint16_t obj_inst_id, lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_swmgmt_set_delete_package_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gacf209563efdc5f3201152088c52d05c3)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_execute_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置处理软件卸载请求（Software Uninstall Requests）的回调。

<a id="r_gab59370ce4fdc94adb4903f22ab1f95b2"></a>

```c
int lwm2m_swmgmt_set_read_package_version_cb (uint16_t obj_inst_id, lwm2m_engine_get_data_cb_t cb)
```

相关声明：[lwm2m_swmgmt_set_read_package_version_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab59370ce4fdc94adb4903f22ab1f95b2)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_get_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga5e531aade0537eb5e3f5756e9287e384)。

设置读取软件包（Software Package）的回调。

<a id="r_ga293904118f972ae387c8aa85a1028b54"></a>

```c
int lwm2m_swmgmt_set_write_package_cb (uint16_t obj_inst_id, lwm2m_engine_set_data_cb_t cb)
```

相关声明：[lwm2m_swmgmt_set_write_package_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga293904118f972ae387c8aa85a1028b54)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_set_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3afac013b0cf731f9c86dc3791131585)。

设置软件管理分块传输（Software Management Block Transfer）的数据回调。

<a id="r_ga573e128348fb2f43a33bd09332dd677f"></a>

```c
int lwm2m_swmgmt_install_completed (uint16_t obj_inst_id, int error_code)
```

相关声明：[lwm2m_swmgmt_install_completed](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga573e128348fb2f43a33bd09332dd677f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

软件管理对象实例（Software Management Object Instance）完成安装操作（Install Operation）时调用的函数。

<a id="r_ga950557bce8c510bcc8b0704e7bc4a9dc"></a>

```c
void lwm2m_event_log_set_read_log_data_cb (lwm2m_engine_get_data_cb_t cb)
```

相关声明：[lwm2m_event_log_set_read_log_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga950557bce8c510bcc8b0704e7bc4a9dc)、[lwm2m_engine_get_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga5e531aade0537eb5e3f5756e9287e384)。

设置读取日志数据（Log Data）的回调。

<a id="r_gadd163806d70713d8349a9db484ba88bf"></a>

```c
int lwm2m_update_observer_min_period (struct lwm2m_ctx *client_ctx, const struct lwm2m_obj_path *path, uint32_t period_s)
```

相关声明：[lwm2m_update_observer_min_period](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gadd163806d70713d8349a9db484ba88bf)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

更改观察者（Observer）的 `pmin` 值。

<a id="r_ga6acccbcd879901574aceab53a21800fc"></a>

```c
int lwm2m_update_observer_max_period (struct lwm2m_ctx *client_ctx, const struct lwm2m_obj_path *path, uint32_t period_s)
```

相关声明：[lwm2m_update_observer_max_period](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6acccbcd879901574aceab53a21800fc)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

更改观察者（Observer）的 `pmax` 值。

<a id="r_ga53f5b4c5967e93c7dd224fce8f416265"></a>

```c
int lwm2m_create_object_inst (const struct lwm2m_obj_path *path)
```

相关声明：[lwm2m_create_object_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga53f5b4c5967e93c7dd224fce8f416265)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

创建 LwM2M 对象实例（Object Instance）。

<a id="r_gaf921d4bc96090ef8735d90d173feab94"></a>

```c
int lwm2m_delete_object_inst (const struct lwm2m_obj_path *path)
```

相关声明：[lwm2m_delete_object_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf921d4bc96090ef8735d90d173feab94)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

删除 LwM2M 对象实例（Object Instance）。

<a id="r_ga9a0cdcc9fc6d37462eddeb54e5d1f87a"></a>

```c
void lwm2m_registry_lock (void)
```

相关声明：[lwm2m_registry_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9a0cdcc9fc6d37462eddeb54e5d1f87a)。

为当前线程锁定注册表（Registry）。

<a id="r_gab09b62982c34887cdd16c30659d3349a"></a>

```c
void lwm2m_registry_unlock (void)
```

相关声明：[lwm2m_registry_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab09b62982c34887cdd16c30659d3349a)。

解锁之前通过 `lwm2m_registry_lock()` 锁定的注册表（Registry）。

<a id="r_gaaef33bdf3f48fd91abdb50db4d5460f9"></a>

```c
int lwm2m_set_opaque (const struct lwm2m_obj_path *path, const char *data_ptr, uint16_t data_len)
```

相关声明：[lwm2m_set_opaque](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaaef33bdf3f48fd91abdb50db4d5460f9)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置资源（实例）值（Resource/Instance Value），类型为不透明缓冲区（Opaque Buffer）。

<a id="r_ga7217f33bf705011d91ba66c86a4d5747"></a>

```c
int lwm2m_set_string (const struct lwm2m_obj_path *path, const char *data_ptr)
```

相关声明：[lwm2m_set_string](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7217f33bf705011d91ba66c86a4d5747)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

设置资源（实例）值（Resource/Instance Value），类型为字符串（String）。

<a id="r_ga1aa3ff424b7190d0fbd9366626b2685c"></a>

```c
int lwm2m_set_u8 (const struct lwm2m_obj_path *path, uint8_t value)
```

相关声明：[lwm2m_set_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1aa3ff424b7190d0fbd9366626b2685c)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置资源（实例）值（Resource/Instance Value），类型为 `u8`。

<a id="r_ga1f06bb65571efee18db5d061f95399c3"></a>

```c
int lwm2m_set_u16 (const struct lwm2m_obj_path *path, uint16_t value)
```

相关声明：[lwm2m_set_u16](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1f06bb65571efee18db5d061f95399c3)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置资源（实例）值（Resource/Instance Value），类型为 `u16`。

<a id="r_ga9481e570b121404dc1be1ce23d904894"></a>

```c
int lwm2m_set_u32 (const struct lwm2m_obj_path *path, uint32_t value)
```

相关声明：[lwm2m_set_u32](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9481e570b121404dc1be1ce23d904894)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置资源（实例）值（Resource/Instance Value），类型为 `u32`。

<a id="r_ga37261a4b9e54eab3d1d855a084d082aa"></a>

```c
int lwm2m_set_s8 (const struct lwm2m_obj_path *path, int8_t value)
```

相关声明：[lwm2m_set_s8](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga37261a4b9e54eab3d1d855a084d082aa)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

设置资源（实例）值（Resource/Instance Value），类型为 `s8`。

<a id="r_gad548ffedcb8328b23eb32476a97be6ee"></a>

```c
int lwm2m_set_s16 (const struct lwm2m_obj_path *path, int16_t value)
```

相关声明：[lwm2m_set_s16](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad548ffedcb8328b23eb32476a97be6ee)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

设置资源（实例）值（Resource/Instance Value），类型为 `s16`。

<a id="r_ga327e086959fc5649a5ef14f1f2943e88"></a>

```c
int lwm2m_set_s32 (const struct lwm2m_obj_path *path, int32_t value)
```

相关声明：[lwm2m_set_s32](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga327e086959fc5649a5ef14f1f2943e88)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置资源（实例）值（Resource/Instance Value），类型为 `s32`。

<a id="r_ga18fcee379640c0dda32d6e3d14827260"></a>

```c
int lwm2m_set_s64 (const struct lwm2m_obj_path *path, int64_t value)
```

相关声明：[lwm2m_set_s64](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga18fcee379640c0dda32d6e3d14827260)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

设置资源（实例）值（Resource/Instance Value），类型为 `s64`。

<a id="r_ga9ef21d06bef8a97b7666c0aa7fa753b4"></a>

```c
int lwm2m_set_bool (const struct lwm2m_obj_path *path, bool value)
```

相关声明：[lwm2m_set_bool](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9ef21d06bef8a97b7666c0aa7fa753b4)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置资源（实例）值（Resource/Instance Value），类型为布尔值（Bool）。

<a id="r_ga3386d3f2ad8d9713fc2283ed6921c2fc"></a>

```c
int lwm2m_set_f64 (const struct lwm2m_obj_path *path, const double value)
```

相关声明：[lwm2m_set_f64](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3386d3f2ad8d9713fc2283ed6921c2fc)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

设置资源（实例）值（Resource/Instance Value），类型为双精度浮点数（Double）。

<a id="r_ga04a18bd8a4eeea41a47803c16567d67b"></a>

```c
int lwm2m_set_objlnk (const struct lwm2m_obj_path *path, const struct lwm2m_objlnk *value)
```

相关声明：[lwm2m_set_objlnk](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga04a18bd8a4eeea41a47803c16567d67b)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_objlnk](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md)。

设置资源（实例）值（Resource/Instance Value），类型为对象链接（Objlnk）。

<a id="r_ga7194ad24842e35130d8af7f5104c0844"></a>

```c
int lwm2m_set_time (const struct lwm2m_obj_path *path, time_t value)
```

相关声明：[lwm2m_set_time](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7194ad24842e35130d8af7f5104c0844)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

设置资源（实例）值（Resource/Instance Value），类型为时间（Time）。

<a id="r_ga41b673986e11748b2ded8e1f8f05e0a7"></a>

```c
int lwm2m_set_bulk (const struct lwm2m_res_item res_list[], size_t res_list_size)
```

相关声明：[lwm2m_set_bulk](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga41b673986e11748b2ded8e1f8f05e0a7)、[lwm2m_res_item](../network_application_model_reference/P050_lwm2m_res_item_结构体.md)。

设置多个资源（实例）值（Resource/Instance Values）。

<a id="r_gae245a9a1d9456af7e6283b1074944606"></a>

```c
int lwm2m_get_opaque (const struct lwm2m_obj_path *path, void *buf, uint16_t buflen)
```

相关声明：[lwm2m_get_opaque](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae245a9a1d9456af7e6283b1074944606)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取资源（实例）值（Resource/Instance Value），类型为不透明缓冲区（Opaque Buffer）。

<a id="r_ga20fc58b25468bf309175db59d67b820b"></a>

```c
int lwm2m_get_string (const struct lwm2m_obj_path *path, void *str, uint16_t buflen)
```

相关声明：[lwm2m_get_string](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga20fc58b25468bf309175db59d67b820b)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取资源（实例）值（Resource/Instance Value），类型为字符串（String）。

<a id="r_gac56e804962e529799c771d81ac1fd027"></a>

```c
int lwm2m_get_u8 (const struct lwm2m_obj_path *path, uint8_t *value)
```

相关声明：[lwm2m_get_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac56e804962e529799c771d81ac1fd027)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取资源（实例）值（Resource/Instance Value），类型为 `u8`。

<a id="r_ga1b96848f96bdab9939bb2619d3e1059b"></a>

```c
int lwm2m_get_u16 (const struct lwm2m_obj_path *path, uint16_t *value)
```

相关声明：[lwm2m_get_u16](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1b96848f96bdab9939bb2619d3e1059b)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取资源（实例）值（Resource/Instance Value），类型为 `u16`。

<a id="r_ga0bc84cb39a7a537925ec7d62e54b8b48"></a>

```c
int lwm2m_get_u32 (const struct lwm2m_obj_path *path, uint32_t *value)
```

相关声明：[lwm2m_get_u32](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga0bc84cb39a7a537925ec7d62e54b8b48)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取资源（实例）值（Resource/Instance Value），类型为 `u32`。

<a id="r_ga12817bfbf0a0cbb742568ee974a1c337"></a>

```c
int lwm2m_get_s8 (const struct lwm2m_obj_path *path, int8_t *value)
```

相关声明：[lwm2m_get_s8](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga12817bfbf0a0cbb742568ee974a1c337)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

获取资源（实例）值（Resource/Instance Value），类型为 `s8`。

<a id="r_ga2426db6720b3f3e15e63022cabae5ece"></a>

```c
int lwm2m_get_s16 (const struct lwm2m_obj_path *path, int16_t *value)
```

相关声明：[lwm2m_get_s16](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga2426db6720b3f3e15e63022cabae5ece)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

获取资源（实例）值（Resource/Instance Value），类型为 `s16`。

<a id="r_ga99d7189efa25881dbcddd99e2a795f1b"></a>

```c
int lwm2m_get_s32 (const struct lwm2m_obj_path *path, int32_t *value)
```

相关声明：[lwm2m_get_s32](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga99d7189efa25881dbcddd99e2a795f1b)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

获取资源（实例）值（Resource/Instance Value），类型为 `s32`。

<a id="r_gaaffe06ca9ee5302fb6e26164f250653e"></a>

```c
int lwm2m_get_s64 (const struct lwm2m_obj_path *path, int64_t *value)
```

相关声明：[lwm2m_get_s64](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaaffe06ca9ee5302fb6e26164f250653e)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

获取资源（实例）值（Resource/Instance Value），类型为 `s64`。

<a id="r_gafdc72844ce0ca417e297d76288155aa4"></a>

```c
int lwm2m_get_bool (const struct lwm2m_obj_path *path, bool *value)
```

相关声明：[lwm2m_get_bool](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gafdc72844ce0ca417e297d76288155aa4)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

获取资源（实例）值（Resource/Instance Value），类型为布尔值（Bool）。

<a id="r_ga03b72e96a67fcbf85feb5bf0b9df81ce"></a>

```c
int lwm2m_get_f64 (const struct lwm2m_obj_path *path, double *value)
```

相关声明：[lwm2m_get_f64](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga03b72e96a67fcbf85feb5bf0b9df81ce)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

获取资源（实例）值（Resource/Instance Value），类型为双精度浮点数（Double）。

<a id="r_ga4de941c36cf678e12da6e05c378a92e5"></a>

```c
int lwm2m_get_objlnk (const struct lwm2m_obj_path *path, struct lwm2m_objlnk *buf)
```

相关声明：[lwm2m_get_objlnk](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4de941c36cf678e12da6e05c378a92e5)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_objlnk](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md)。

获取资源（实例）值（Resource/Instance Value），类型为对象链接（Objlnk）。

<a id="r_ga2e1d41866b5ea35c5aa29bca9bb43812"></a>

```c
int lwm2m_get_time (const struct lwm2m_obj_path *path, time_t *buf)
```

相关声明：[lwm2m_get_time](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga2e1d41866b5ea35c5aa29bca9bb43812)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)。

获取资源（实例）值（Resource/Instance Value），类型为时间（Time）。

<a id="r_gaf33bd6a527b6d399f3d92b666ac77dfb"></a>

```c
int lwm2m_register_read_callback (const struct lwm2m_obj_path *path, lwm2m_engine_get_data_cb_t cb)
```

相关声明：[lwm2m_register_read_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf33bd6a527b6d399f3d92b666ac77dfb)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_engine_get_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga5e531aade0537eb5e3f5756e9287e384)。

设置资源（实例）读取回调（Read Callback）。

<a id="r_ga6f775837e07ba9b0032be8917a593e16"></a>

```c
int lwm2m_register_pre_write_callback (const struct lwm2m_obj_path *path, lwm2m_engine_get_data_cb_t cb)
```

相关声明：[lwm2m_register_pre_write_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6f775837e07ba9b0032be8917a593e16)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_engine_get_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga5e531aade0537eb5e3f5756e9287e384)。

设置资源（实例）写入前回调（Pre-write Callback）。

<a id="r_gad6e5fd4815f409ad59ad631b03199333"></a>

```c
int lwm2m_register_validate_callback (const struct lwm2m_obj_path *path, lwm2m_engine_set_data_cb_t cb)
```

相关声明：[lwm2m_register_validate_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad6e5fd4815f409ad59ad631b03199333)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_engine_set_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3afac013b0cf731f9c86dc3791131585)。

设置资源（实例）校验回调（Validation Callback）。

<a id="r_ga3dd8b38e797173dae902404fb5b7a3f4"></a>

```c
int lwm2m_register_post_write_callback (const struct lwm2m_obj_path *path, lwm2m_engine_set_data_cb_t cb)
```

相关声明：[lwm2m_register_post_write_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3dd8b38e797173dae902404fb5b7a3f4)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_engine_set_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3afac013b0cf731f9c86dc3791131585)。

设置资源（实例）写入后回调（Post-write Callback）。

<a id="r_ga29cc5cdd697e94d7379b1fb178487916"></a>

```c
int lwm2m_register_exec_callback (const struct lwm2m_obj_path *path, lwm2m_engine_execute_cb_t cb)
```

相关声明：[lwm2m_register_exec_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga29cc5cdd697e94d7379b1fb178487916)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_engine_execute_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb32bcd4981b4c7bd891f99668ebc0fe)。

设置资源执行事件回调（Resource Execute Event Callback）。

<a id="r_ga346d547e02bd53ee83f83b2248449e98"></a>

```c
int lwm2m_register_create_callback (uint16_t obj_id, lwm2m_engine_user_cb_t cb)
```

相关声明：[lwm2m_register_create_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga346d547e02bd53ee83f83b2248449e98)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabcbca483b310e0c4cd68aef2d9cda0bf)。

设置对象实例创建事件回调（Object Instance Create Event Callback）。

<a id="r_ga92d7e6d81ef674a6c311e1717c6bf373"></a>

```c
int lwm2m_register_delete_callback (uint16_t obj_id, lwm2m_engine_user_cb_t cb)
```

相关声明：[lwm2m_register_delete_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga92d7e6d81ef674a6c311e1717c6bf373)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[lwm2m_engine_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabcbca483b310e0c4cd68aef2d9cda0bf)。

设置对象实例删除事件回调（Object Instance Delete Event Callback）。

<a id="r_ga56a2aecd38baedb5dc17258610c4780d"></a>

```c
int lwm2m_set_res_buf (const struct lwm2m_obj_path *path, void *buffer_ptr, uint16_t buffer_len, uint16_t data_len, uint8_t data_flags)
```

相关声明：[lwm2m_set_res_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga56a2aecd38baedb5dc17258610c4780d)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为资源（Resource）设置数据缓冲区（Data Buffer）。

<a id="r_ga0f2b115d231bea6622135d72b51f55ca"></a>

```c
int lwm2m_set_res_data_len (const struct lwm2m_obj_path *path, uint16_t data_len)
```

相关声明：[lwm2m_set_res_data_len](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga0f2b115d231bea6622135d72b51f55ca)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

更新资源（Resource）的数据大小（Data Size）。

<a id="r_gac0b6669d8a19b03eb8b08cbbcdb0c192"></a>

```c
int lwm2m_get_res_buf (const struct lwm2m_obj_path *path, void **buffer_ptr, uint16_t *buffer_len, uint16_t *data_len, uint8_t *data_flags)
```

相关声明：[lwm2m_get_res_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac0b6669d8a19b03eb8b08cbbcdb0c192)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取资源（Resource）的数据缓冲区（Data Buffer）。

<a id="r_gac69c40474180fe14c3761185b2db1c0c"></a>

```c
int lwm2m_create_res_inst (const struct lwm2m_obj_path *path)
```

相关声明：[lwm2m_create_res_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac69c40474180fe14c3761185b2db1c0c)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

创建资源实例（Resource Instance）。

<a id="r_gacfeb63db0423e6730ffaa826a87eb262"></a>

```c
int lwm2m_delete_res_inst (const struct lwm2m_obj_path *path)
```

相关声明：[lwm2m_delete_res_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gacfeb63db0423e6730ffaa826a87eb262)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

删除资源实例（Resource Instance）。

<a id="r_gab45cebf6f0b6b70974367ca453d16aeb"></a>

```c
int lwm2m_update_device_service_period (uint32_t period_ms)
```

相关声明：[lwm2m_update_device_service_period](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab45cebf6f0b6b70974367ca453d16aeb)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

更新设备服务（Device Service）的周期（Period）。

<a id="r_ga1065c729d5caa8ca13de7766fce77953"></a>

```c
bool lwm2m_path_is_observed (const struct lwm2m_obj_path *path)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[lwm2m_path_is_observed](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1065c729d5caa8ca13de7766fce77953)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

检查路径（Path）是否正在被观察（Observed）。

<a id="r_ga077e1abd612d31dd33fab52b7d205c39"></a>

```c
int lwm2m_engine_stop (struct lwm2m_ctx *client_ctx)
```

相关声明：[lwm2m_engine_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga077e1abd612d31dd33fab52b7d205c39)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

停止 LwM2M 引擎（Engine）。

<a id="r_ga9f72fbd0163b15c48ea09cf7d511e444"></a>

```c
int lwm2m_engine_start (struct lwm2m_ctx *client_ctx)
```

相关声明：[lwm2m_engine_start](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9f72fbd0163b15c48ea09cf7d511e444)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

启动 LwM2M 引擎（Engine）。

<a id="r_ga919c7d6f418cda99c77fdaf54ae1a7b0"></a>

```c
void lwm2m_acknowledge (struct lwm2m_ctx *client_ctx)
```

相关声明：[lwm2m_acknowledge](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga919c7d6f418cda99c77fdaf54ae1a7b0)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

使用空确认（Empty ACK）确认当前处理的请求（Request）。

<a id="r_ga9dfd46b8a535b1f28e644dc18f57fd79"></a>

```c
int lwm2m_rd_client_start (struct lwm2m_ctx *client_ctx, const char *ep_name, uint32_t flags, lwm2m_ctx_event_cb_t event_cb, lwm2m_observe_cb_t observe_cb)
```

相关声明：[lwm2m_rd_client_start](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9dfd46b8a535b1f28e644dc18f57fd79)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)、[lwm2m_ctx_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga38dbaf038426efc75d889c4a0666dac9)、[lwm2m_observe_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad7bea67e16e1e831e0f949dbf83d5afe)。

启动 LwM2M 注册／发现客户端（Registration/Discovery Client，RD Client）。

<a id="r_gafd87e5d975c4d88973ac3e95e4d156ac"></a>

```c
int lwm2m_rd_client_stop (struct lwm2m_ctx *client_ctx, lwm2m_ctx_event_cb_t event_cb, bool deregister)
```

相关声明：[lwm2m_rd_client_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gafd87e5d975c4d88973ac3e95e4d156ac)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[lwm2m_ctx_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga38dbaf038426efc75d889c4a0666dac9)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

停止 LwM2M RD 客户端，执行注销（De-register）。

<a id="r_ga1a4dadb822a8241c5bdf339c21cc57a4"></a>

```c
int lwm2m_engine_pause (void)
```

相关声明：[lwm2m_engine_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1a4dadb822a8241c5bdf339c21cc57a4)。

挂起 LwM2M 引擎线程（Engine Thread）。

<a id="r_ga178fea0407a5e98c4f5d5ad69688853a"></a>

```c
int lwm2m_engine_resume (void)
```

相关声明：[lwm2m_engine_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga178fea0407a5e98c4f5d5ad69688853a)。

恢复 LwM2M 引擎线程（Engine Thread）。

<a id="r_gab4ec7a22d01259b6ba9d3a7b6681e6f0"></a>

```c
void lwm2m_rd_client_update (void)
```

相关声明：[lwm2m_rd_client_update](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab4ec7a22d01259b6ba9d3a7b6681e6f0)。

触发 LwM2M RD 客户端的注册更新（Registration Update）。

<a id="r_ga971c0636c19fe7f0a6e918622560a750"></a>

```c
char * lwm2m_path_log_buf (char *buf, struct lwm2m_obj_path *path)
```

相关声明：[lwm2m_path_log_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga971c0636c19fe7f0a6e918622560a750)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

将路径对象（Path Objects）的内容打印到日志（Log）的辅助函数。

<a id="r_ga026cc9288d2de17ec557e08b9b987ebc"></a>

```c
int lwm2m_send_cb (struct lwm2m_ctx *ctx, const struct lwm2m_obj_path path_list[], uint8_t path_list_size, lwm2m_send_cb_t reply_cb)
```

相关声明：[lwm2m_send_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga026cc9288d2de17ec557e08b9b987ebc)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[lwm2m_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf5394884da53edb28fe4afc92bf40e6a)。

<a id="r_ga896caab5473eadff860872023d13b6c0"></a>

```c
struct lwm2m_ctx * lwm2m_rd_client_ctx (void)
```

相关声明：[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)、[lwm2m_rd_client_ctx](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga896caab5473eadff860872023d13b6c0)。

<a id="r_ga6975c5c4825afaccc52741eb54aca4cb"></a>

```c
int lwm2m_enable_cache (const struct lwm2m_obj_path *path, struct lwm2m_time_series_elem *data_cache, size_t cache_len)
```

相关声明：[lwm2m_enable_cache](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6975c5c4825afaccc52741eb54aca4cb)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_time_series_elem](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md)。

<a id="r_gac4e7da0353914601c3ec101415c2e110"></a>

```c
int lwm2m_set_cache_filter (const struct lwm2m_obj_path *path, lwm2m_cache_filter_cb_t filter_cb)
```

相关声明：[lwm2m_set_cache_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac4e7da0353914601c3ec101415c2e110)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)、[lwm2m_cache_filter_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7a0bb9d5652f7f0fd0cc4a1139be6f37)。

为缓存的资源样本（Cached Resource Samples）注册过滤回调（Filtering Callback）。

<a id="r_ga00d29a0c4935fc255e74b8c22ac49de1"></a>

```c
int lwm2m_cache_free_slots_get (const struct lwm2m_obj_path *path)
```

相关声明：[lwm2m_cache_free_slots_get](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga00d29a0c4935fc255e74b8c22ac49de1)、[lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)。

返回缓存资源（Cached Resource）中的空闲槽位数（Free Slots）。

<a id="r_ga6c05640737cfc4da71841a77de128be0"></a>

```c
int lwm2m_security_mode (struct lwm2m_ctx *ctx)
```

相关声明：[lwm2m_security_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6c05640737cfc4da71841a77de128be0)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

从选定的安全对象实例（Security Object Instance）读取安全模式（Security Mode）。

<a id="r_ga956c4fc742a588b7b8b95ce8481f09bf"></a>

```c
int lwm2m_set_default_sockopt (struct lwm2m_ctx *ctx)
```

相关声明：[lwm2m_set_default_sockopt](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga956c4fc742a588b7b8b95ce8481f09bf)、[lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)。

设置数据报传输层安全（DTLS）连接的默认套接字选项（Socket Options）。

<a id="r_ga647018abc15cd65c894d9acb6c866486"></a>

```c
void lwm2m_pull_context_set_sockopt_callback (lwm2m_set_sockopt_cb_t set_sockopt_cb)
```

相关声明：[lwm2m_pull_context_set_sockopt_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga647018abc15cd65c894d9acb6c866486)、[lwm2m_set_sockopt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga92d2227f37e7d382bc4f1a7bae21b872)。

为拉取上下文（Pull Context）的客户端设置 `lwm2m_ctx::set_socketoptions` 回调。


## 2.6\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/sys/mutex.h](../userspace_sync_reference/P006_用户模式互斥量头文件源码.md)
- [zephyr/net/coap.h](../api_source_transport_clock_reference/P006_coap.h_源码浏览.md)
- [zephyr/net/lwm2m_path.h](../api_source_configuration_reference/P049_lwm2m_path.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P040_lwm2m.h_源码浏览.md)
- [lwm2m_obj_path](../network_application_model_reference/P048_lwm2m_obj_path_结构体.md)
- [lwm2m_ctx](../network_application_model_reference/P047_lwm2m_ctx_结构体.md)
- [lwm2m_time_series_elem](../network_application_model_reference/P051_lwm2m_time_series_elem_结构体.md)
- [lwm2m_objlnk](../network_application_model_reference/P049_lwm2m_objlnk_结构体.md)
- [lwm2m_res_item](../network_application_model_reference/P050_lwm2m_res_item_结构体.md)
- [LWM2M_OBJLNK_MAX_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga34febb0c6fb1c68b0963a6e4dd721763)
- [LWM2M_RES_DATA_READ_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga12c2e0af3d3fc6dd5785e08c0d831a67)
- [LWM2M_RES_DATA_FLAG_RO](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1bfa5b7d83e3560828a1fb61a4d07355)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [LWM2M_HAS_RES_FLAG](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga49f4117dfec8cd1abe9f827e235f55b0)
- [LWM2M_RD_CLIENT_FLAG_BOOTSTRAP](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3a3669237762fa8c23686e5e00b7809f)
- [LWM2M_MAX_PATH_STR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab97329844cd411195add5d72ad6aa4b7)
- [LWM2M_OBJECT_SECURITY_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga785e4a647a2cf93194a249537223ab0f)
- [LWM2M_OBJECT_SERVER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gace7b2f0a1f97b6e99c0958a8382ca0d2)
- [LWM2M_OBJECT_ACCESS_CONTROL_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaa8387c8838f952c7c60602e2952c7f55)
- [LWM2M_OBJECT_DEVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga699f585b320ab5b259d4fb2bda10eb78)
- [LWM2M_OBJECT_CONNECTIVITY_MONITORING_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga73db8616cc7dbbd04267d97a743b8ec0)
- [LWM2M_OBJECT_FIRMWARE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga442cc51c7d0807a752ce4affe9221c5b)
- [LWM2M_OBJECT_LOCATION_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1046ec68deab3d812d7e5921fb718028)
- [LWM2M_OBJECT_CONNECTIVITY_STATISTICS_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaa6c374c401dd36b6e121ac48c91ca9cf)
- [LWM2M_OBJECT_SOFTWARE_MANAGEMENT_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac2d140b4a36d6010fe93bca443a658c0)
- [LWM2M_OBJECT_PORTFOLIO_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4b4ce912a4554923974461ea3c76007e)
- [LWM2M_OBJECT_BINARYAPPDATACONTAINER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga85eabde1900ef052064d34cf5e3a4afe)
- [LWM2M_OBJECT_EVENT_LOG_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4f0455fb0271c2fcbb7dadb944431ff0)
- [LWM2M_OBJECT_OSCORE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab13a1600a662ed1dbd8845c6d7d4549a)
- [LWM2M_OBJECT_GATEWAY_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3505e9ddcd54afe86e8bd5fbc03fb565)
- [http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html](http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html)
- [IPSO_OBJECT_GENERIC_SENSOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeef485c23d306c93fc0f45dd58766ad9)
- [IPSO_OBJECT_TEMP_SENSOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3b0c046d93c7bcee9d4da121dd574ff0)
- [IPSO_OBJECT_HUMIDITY_SENSOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga8075d8b7eb3b4c98f621efef673bb11f)
- [IPSO_OBJECT_LIGHT_CONTROL_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga56ebac5260ee467b3763abe49ff3b8ff)
- [IPSO_OBJECT_ACCELEROMETER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga0b3b9db806e5fe47cc08de34b5fb35fe)
- [IPSO_OBJECT_MAGNETOMETER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6abcf3c5cf5001a4fdb7915336325ce1)
- [IPSO_OBJECT_VOLTAGE_SENSOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga270a1b5a576d72099287633b32ce909f)
- [IPSO_OBJECT_CURRENT_SENSOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae511fd54112829e63c691776750893c2)
- [IPSO_OBJECT_PRESSURE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga752f81e91d0965a50ecfb0679bdea6ba)
- [IPSO_OBJECT_TIME_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga46075c78a3cd73f3313abf5ffeca697b)
- [IPSO_OBJECT_BUZZER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga15d664ddbfbf4d5b25dde34a5c650e6b)
- [IPSO_OBJECT_TIMER_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6c7bd5880fa22050748c2cb01981cbcb)
- [IPSO_OBJECT_ONOFF_SWITCH_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga776a6a5e1eab3a8de0a39382f94b663a)
- [IPSO_OBJECT_PUSH_BUTTON_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6e3119bc8f0b9143ab384e82a5bccf7c)
- [UCIFI_OBJECT_BATTERY_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gacdd09a26ce52f36c644a89a8b89f7d32)
- [IPSO_OBJECT_FILLING_LEVEL_SENSOR_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga21f6bc6255f5f5ed28881fa797d026ca)
- [LWM2M_DEVICE_PWR_SRC_TYPE_DC_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae154ca2e54ec7759dd43f2a7a275077e)
- [LWM2M_DEVICE_PWR_SRC_TYPE_BAT_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga04ca8ac536eed7d411c1b1ea2b2a59ac)
- [LWM2M_DEVICE_PWR_SRC_TYPE_BAT_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf12052f903a688712928d036b782f621)
- [LWM2M_DEVICE_PWR_SRC_TYPE_FUEL_CELL](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga10c4633c97881ca7d87c748aaeec68c9)
- [LWM2M_DEVICE_PWR_SRC_TYPE_PWR_OVER_ETH](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga72352523996e61ea93caff0bb80c42ba)
- [LWM2M_DEVICE_PWR_SRC_TYPE_USB](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4877877be75d3dd3c8f600b438b7ea8e)
- [LWM2M_DEVICE_PWR_SRC_TYPE_AC_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga97b9d38ec402478f10642f1f83a4f88a)
- [LWM2M_DEVICE_PWR_SRC_TYPE_SOLAR](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaa41ec1d2ca43e1385cfb11204aff729d)
- [LWM2M_DEVICE_PWR_SRC_TYPE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae7a580aac1804abbcf3feb57a5a30a02)
- [lwm2m_device_add_err()](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabf8726f0438477863423947a7bb77ce2)
- [LWM2M_DEVICE_ERROR_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad54ec75eb2843d5eed199ddedca6ef4f)
- [LWM2M_DEVICE_ERROR_LOW_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga53a9ee1ae09dd32a8dc2df6018798f9f)
- [LWM2M_DEVICE_ERROR_EXT_POWER_SUPPLY_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga33152ea4ef497b02a12d1218d470a5a6)
- [LWM2M_DEVICE_ERROR_GPS_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3c1b7693167ff517c5cbd7bbdbfd1ea0)
- [LWM2M_DEVICE_ERROR_LOW_SIGNAL_STRENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga78048382d8bc85bbabbff58f0a9860f2)
- [LWM2M_DEVICE_ERROR_OUT_OF_MEMORY](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga94ce0177c066dd43ef660b85afc83485)
- [LWM2M_DEVICE_ERROR_SMS_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabcb39cd3757ea60859984f6ad0df9e31)
- [LWM2M_DEVICE_ERROR_NETWORK_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga2110d71a0c58087ff877e66b7500ba66)
- [LWM2M_DEVICE_ERROR_PERIPHERAL_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga77e6352eace8116576c880bf7e416ba3)
- [LWM2M_DEVICE_BATTERY_STATUS_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4329c971f95f1c345381d1c864a9f334)
- [LWM2M_DEVICE_BATTERY_STATUS_CHARGING](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf19da3a566782aeebebfb6ff110a9152)
- [LWM2M_DEVICE_BATTERY_STATUS_CHARGE_COMP](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga5f7e88b52d8e6029467a2ed10585e6d4)
- [LWM2M_DEVICE_BATTERY_STATUS_DAMAGED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaa3f81df5e4d45838922eb20a15ee3153)
- [LWM2M_DEVICE_BATTERY_STATUS_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga578f6446ec1b70d2a32917abf1f5aad7)
- [LWM2M_DEVICE_BATTERY_STATUS_NOT_INST](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gacc3dfc99fc2cd9ef7048b1a0a0fd55c8)
- [LWM2M_DEVICE_BATTERY_STATUS_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga174e118b07982b87c6c083236b79c3b7)
- [STATE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaafff27c7165f059a969fe60fee51f683)
- [STATE_DOWNLOADING](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb34e88a0da4ac1274ae6b2cef010086)
- [STATE_DOWNLOADED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga009085120be71a28c1f6ebdaf7503365)
- [STATE_UPDATING](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaac1dab8d1ac28bf13faeee39d1df47c5)
- [RESULT_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga391b47507468bbc1005903a56f80b1ea)
- [RESULT_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7cc1753a05a0821f6c70dd2bccfbab5c)
- [RESULT_NO_STORAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga829f7bc83b67dcf16ea4775addd87343)
- [RESULT_OUT_OF_MEM](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab5446111a8969aa2c66dae49f04c93cf)
- [RESULT_CONNECTION_LOST](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga0655ba8c402d8b6c8bbd84fb36447bd4)
- [RESULT_INTEGRITY_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gadfd0ac7b6a3fededa2b4471dfe52d3d2)
- [RESULT_UNSUP_FW](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab06dbfdac0c95f8100908a1177f3a62a)
- [RESULT_INVALID_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga268204053d7e23737283523224699979)
- [RESULT_UPDATE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga2dfdd95c2c03ccca25d855b6d6f96ed3)
- [RESULT_UNSUP_PROTO](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gade3da37a44ee40292ec6344403db8d8d)
- [lwm2m_socket_fault_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae7bf50f9abf1b82b76ac3e9175e685ac)
- [lwm2m_observe_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad7bea67e16e1e831e0f949dbf83d5afe)
- [lwm2m_observe_event](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac8d63952ec94ca6cfb1dbe12a6c53bfb)
- [lwm2m_ctx_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga38dbaf038426efc75d889c4a0666dac9)
- [lwm2m_rd_client_event](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaca90ab8960a4ff01d44735dbc0405862)
- [lwm2m_set_sockopt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga92d2227f37e7d382bc4f1a7bae21b872)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [lwm2m_cache_filter_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7a0bb9d5652f7f0fd0cc4a1139be6f37)
- [lwm2m_engine_get_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga5e531aade0537eb5e3f5756e9287e384)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [lwm2m_engine_set_data_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3afac013b0cf731f9c86dc3791131585)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [lwm2m_engine_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gabcbca483b310e0c4cd68aef2d9cda0bf)
- [lwm2m_engine_execute_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaeb32bcd4981b4c7bd891f99668ebc0fe)
- [lwm2m_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf5394884da53edb28fe4afc92bf40e6a)
- [lwm2m_send_status](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga20848e0942882e8c2cc40ee8a48b7bfd)
- [LWM2M_OBSERVE_EVENT_OBSERVER_ADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggac8d63952ec94ca6cfb1dbe12a6c53bfba22f4341d713417110d9866b0cbd318e3)
- [LWM2M_OBSERVE_EVENT_OBSERVER_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggac8d63952ec94ca6cfb1dbe12a6c53bfbae3f4af98b52ee191229c660748c7dd6c)
- [LWM2M_OBSERVE_EVENT_NOTIFY_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggac8d63952ec94ca6cfb1dbe12a6c53bfbaab4e1cf0451ba926b90ea21152cac885)
- [LWM2M_OBSERVE_EVENT_NOTIFY_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggac8d63952ec94ca6cfb1dbe12a6c53bfba55494fd6e76f585894e34dc9004fbc9e)
- [LWM2M_RD_CLIENT_EVENT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862aca4ebc8d550af02f1891eed1a7b1afcc)
- [LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ac089b900494522de565e36d31ea3b0c4)
- [LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ac30dd8520e591c8e51c74ce1a53cd524)
- [LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_TRANSFER_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a7c7c3115b6ff16dfa722b6b82c2cd1bc)
- [LWM2M_RD_CLIENT_EVENT_REGISTRATION_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ae89498cad338b1dc9cbd3b23838bf0b6)
- [LWM2M_RD_CLIENT_EVENT_REGISTRATION_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a8994ea8c025cbbd56adcc050a7e86541)
- [LWM2M_RD_CLIENT_EVENT_REG_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a90341c0d9584681f18d1cae91c9f6404)
- [LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a9f53175c5e935f061a83aa1fcfe9f683)
- [LWM2M_RD_CLIENT_EVENT_DEREGISTER_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a32552b56152f9a714675fc6bba3b3d5f)
- [LWM2M_RD_CLIENT_EVENT_DISCONNECT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ac6703e7d0809cc9cfcdd1cbd48e2318b)
- [LWM2M_RD_CLIENT_EVENT_QUEUE_MODE_RX_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a7c7853536c452da2f74e9f43a024fcbe)
- [LWM2M_RD_CLIENT_EVENT_ENGINE_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862afd4eda5dee31b18b1da5414481e33525)
- [LWM2M_RD_CLIENT_EVENT_NETWORK_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862aff939a86c623ab8258c707361b95aef4)
- [LWM2M_RD_CLIENT_EVENT_REG_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862ab48772aeed0ead72f3a9289a618af1cd)
- [LWM2M_RD_CLIENT_EVENT_DEREGISTER](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862aac3938a209800a0de0a05b21fab02c13)
- [LWM2M_RD_CLIENT_EVENT_SERVER_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ggaca90ab8960a4ff01d44735dbc0405862a873a4a3190dc7c24d2518dc8d7268763)
- [lwm2m_socket_states](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7611c1aebb0309ee8340e06dd8ee234d)
- [LWM2M_SOCKET_STATE_ONGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga7611c1aebb0309ee8340e06dd8ee234daa0f06bc70659598b0f51b3ce8094c6ab)
- [LWM2M_SOCKET_STATE_ONE_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga7611c1aebb0309ee8340e06dd8ee234da76aa03f71f44096d9413b1f5718d9711)
- [LWM2M_SOCKET_STATE_LAST](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga7611c1aebb0309ee8340e06dd8ee234daed676a6deffe2de7c916bb6eb2906100)
- [LWM2M_SOCKET_STATE_NO_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga7611c1aebb0309ee8340e06dd8ee234da2487ae8e93929bf62fd333cd04c5b915)
- [LWM2M_SEND_STATUS_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga20848e0942882e8c2cc40ee8a48b7bfda127cca7752ab3f00d5a4705f815b14b4)
- [LWM2M_SEND_STATUS_FAILURE](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga20848e0942882e8c2cc40ee8a48b7bfda7a7f1720f39bedba28110fad09939dcd)
- [LWM2M_SEND_STATUS_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga20848e0942882e8c2cc40ee8a48b7bfda7c0144cafd4f91a76d229b40df9cb82a)
- [lwm2m_security_mode_e](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga11de8078091631cb88b26a9a460097ab)
- [LWM2M_SECURITY_PSK](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097aba0d4e9d5160e91fc93e062dfb812edb25)
- [LWM2M_SECURITY_RAW_PK](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097aba431ac48d7f0fed72ce5ab2c8ea823716)
- [LWM2M_SECURITY_CERT](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097aba6eef062c9f54bc9698a050c8bb2915ba)
- [LWM2M_SECURITY_NOSEC](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097abaf6bb17f06d89124076810c132005f8d7)
- [LWM2M_SECURITY_CERT_EST](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gga11de8078091631cb88b26a9a460097abaefb45683a68002dab267c3fb2e876824)
- [lwm2m_firmware_set_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6878ea0ebb512b19a4fb0859756f51d0)
- [lwm2m_firmware_get_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4bf0bbedf5573ac18a11ac4fced11284)
- [lwm2m_firmware_set_write_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac4e4a819e54344657d70ec479eb6ec8d)
- [lwm2m_firmware_get_write_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad7334f06c3bdb14485597794a417152d)
- [lwm2m_firmware_set_cancel_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3955dca5cd6d67807ed75e61a4d84d84)
- [lwm2m_firmware_get_cancel_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9561c1b8407d888f6fbe1e0ceab1c235)
- [lwm2m_firmware_set_cancel_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaa200b524e505f64247f1e7472c5f36d4)
- [lwm2m_firmware_get_cancel_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6f4b3e08c7e03cff4bf31e2f2999971e)
- [lwm2m_firmware_set_update_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga61eb38e42d9e1b3f467c43a324f2fc65)
- [lwm2m_firmware_get_update_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1e4b8ba1b19ac9025dca3c4799bba84a)
- [lwm2m_firmware_set_update_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga31d0f3e40b5e3d608d16a4268b2f1b29)
- [lwm2m_firmware_get_update_cb_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga34995e902b63c4d7d37ebd709d88a72a)
- [lwm2m_swmgmt_set_activate_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac374d0559056ddb9cf43deae932fd128)
- [lwm2m_swmgmt_set_deactivate_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7a2b93b918257bece819dc44804f27f5)
- [lwm2m_swmgmt_set_install_package_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gadfc00060c0b538ed576b5e3edd7dac80)
- [lwm2m_swmgmt_set_delete_package_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gacf209563efdc5f3201152088c52d05c3)
- [lwm2m_swmgmt_set_read_package_version_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab59370ce4fdc94adb4903f22ab1f95b2)
- [lwm2m_swmgmt_set_write_package_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga293904118f972ae387c8aa85a1028b54)
- [lwm2m_swmgmt_install_completed](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga573e128348fb2f43a33bd09332dd677f)
- [lwm2m_event_log_set_read_log_data_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga950557bce8c510bcc8b0704e7bc4a9dc)
- [lwm2m_update_observer_min_period](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gadd163806d70713d8349a9db484ba88bf)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [lwm2m_update_observer_max_period](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6acccbcd879901574aceab53a21800fc)
- [lwm2m_create_object_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga53f5b4c5967e93c7dd224fce8f416265)
- [lwm2m_delete_object_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf921d4bc96090ef8735d90d173feab94)
- [lwm2m_registry_lock](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9a0cdcc9fc6d37462eddeb54e5d1f87a)
- [lwm2m_registry_unlock](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab09b62982c34887cdd16c30659d3349a)
- [lwm2m_set_opaque](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaaef33bdf3f48fd91abdb50db4d5460f9)
- [lwm2m_set_string](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7217f33bf705011d91ba66c86a4d5747)
- [lwm2m_set_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1aa3ff424b7190d0fbd9366626b2685c)
- [lwm2m_set_u16](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1f06bb65571efee18db5d061f95399c3)
- [lwm2m_set_u32](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9481e570b121404dc1be1ce23d904894)
- [lwm2m_set_s8](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga37261a4b9e54eab3d1d855a084d082aa)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [lwm2m_set_s16](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad548ffedcb8328b23eb32476a97be6ee)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [lwm2m_set_s32](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga327e086959fc5649a5ef14f1f2943e88)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [lwm2m_set_s64](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga18fcee379640c0dda32d6e3d14827260)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [lwm2m_set_bool](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9ef21d06bef8a97b7666c0aa7fa753b4)
- [lwm2m_set_f64](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3386d3f2ad8d9713fc2283ed6921c2fc)
- [lwm2m_set_objlnk](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga04a18bd8a4eeea41a47803c16567d67b)
- [lwm2m_set_time](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7194ad24842e35130d8af7f5104c0844)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [lwm2m_set_bulk](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga41b673986e11748b2ded8e1f8f05e0a7)
- [lwm2m_get_opaque](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae245a9a1d9456af7e6283b1074944606)
- [lwm2m_get_string](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga20fc58b25468bf309175db59d67b820b)
- [lwm2m_get_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac56e804962e529799c771d81ac1fd027)
- [lwm2m_get_u16](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1b96848f96bdab9939bb2619d3e1059b)
- [lwm2m_get_u32](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga0bc84cb39a7a537925ec7d62e54b8b48)
- [lwm2m_get_s8](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga12817bfbf0a0cbb742568ee974a1c337)
- [lwm2m_get_s16](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga2426db6720b3f3e15e63022cabae5ece)
- [lwm2m_get_s32](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga99d7189efa25881dbcddd99e2a795f1b)
- [lwm2m_get_s64](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaaffe06ca9ee5302fb6e26164f250653e)
- [lwm2m_get_bool](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gafdc72844ce0ca417e297d76288155aa4)
- [lwm2m_get_f64](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga03b72e96a67fcbf85feb5bf0b9df81ce)
- [lwm2m_get_objlnk](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga4de941c36cf678e12da6e05c378a92e5)
- [lwm2m_get_time](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga2e1d41866b5ea35c5aa29bca9bb43812)
- [lwm2m_register_read_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gaf33bd6a527b6d399f3d92b666ac77dfb)
- [lwm2m_register_pre_write_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6f775837e07ba9b0032be8917a593e16)
- [lwm2m_register_validate_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad6e5fd4815f409ad59ad631b03199333)
- [lwm2m_register_post_write_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga3dd8b38e797173dae902404fb5b7a3f4)
- [lwm2m_register_exec_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga29cc5cdd697e94d7379b1fb178487916)
- [lwm2m_register_create_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga346d547e02bd53ee83f83b2248449e98)
- [lwm2m_register_delete_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga92d7e6d81ef674a6c311e1717c6bf373)
- [lwm2m_set_res_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga56a2aecd38baedb5dc17258610c4780d)
- [lwm2m_set_res_data_len](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga0f2b115d231bea6622135d72b51f55ca)
- [lwm2m_get_res_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac0b6669d8a19b03eb8b08cbbcdb0c192)
- [lwm2m_create_res_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac69c40474180fe14c3761185b2db1c0c)
- [lwm2m_delete_res_inst](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gacfeb63db0423e6730ffaa826a87eb262)
- [lwm2m_update_device_service_period](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab45cebf6f0b6b70974367ca453d16aeb)
- [lwm2m_path_is_observed](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1065c729d5caa8ca13de7766fce77953)
- [lwm2m_engine_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga077e1abd612d31dd33fab52b7d205c39)
- [lwm2m_engine_start](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9f72fbd0163b15c48ea09cf7d511e444)
- [lwm2m_acknowledge](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga919c7d6f418cda99c77fdaf54ae1a7b0)
- [lwm2m_rd_client_start](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga9dfd46b8a535b1f28e644dc18f57fd79)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [lwm2m_rd_client_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gafd87e5d975c4d88973ac3e95e4d156ac)
- [lwm2m_engine_pause](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga1a4dadb822a8241c5bdf339c21cc57a4)
- [lwm2m_engine_resume](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga178fea0407a5e98c4f5d5ad69688853a)
- [lwm2m_rd_client_update](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gab4ec7a22d01259b6ba9d3a7b6681e6f0)
- [lwm2m_path_log_buf](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga971c0636c19fe7f0a6e918622560a750)
- [lwm2m_send_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga026cc9288d2de17ec557e08b9b987ebc)
- [lwm2m_rd_client_ctx](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga896caab5473eadff860872023d13b6c0)
- [lwm2m_enable_cache](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6975c5c4825afaccc52741eb54aca4cb)
- [lwm2m_set_cache_filter](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gac4e7da0353914601c3ec101415c2e110)
- [lwm2m_cache_free_slots_get](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga00d29a0c4935fc255e74b8c22ac49de1)
- [lwm2m_security_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga6c05640737cfc4da71841a77de128be0)
- [lwm2m_set_default_sockopt](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga956c4fc742a588b7b8b95ce8481f09bf)
- [lwm2m_pull_context_set_sockopt_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga647018abc15cd65c894d9acb6c866486)
- [lwm2m_ctx::set_socketoptions](../network_application_model_reference/P047_lwm2m_ctx_结构体.md#a8714a3ee6870515631fd75e74644d39c)

<a id="header-details"></a>

---

[上一章](P001_zephyr__drivers__modem__hl78xx_apis.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__net__net_if.h_文件参考.md)
