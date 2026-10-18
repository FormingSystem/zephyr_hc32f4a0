---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-3
title: 经过时间服务（Elapsed Time Service，ETS）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_经过时间服务（Elapsed Time Service，ETS）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_bt_5Fets_5Felapsed_5Ftime"></a>

```c
struct bt_ets_elapsed_time
```

相关声明：[bt_ets_elapsed_time](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md)。

GATT 规范补充文档（GATT Specification Supplement）第 3.82 节定义的经过时间（Elapsed Time）数据结构。

<a id="r_bt_5Fets_5Fcb"></a>

```c
struct bt_ets_cb
```

相关声明：[bt_ets_cb](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md)。

经过时间服务（Elapsed Time Service，ETS）的回调结构体。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga4d2718c8e1dad8812b4ed6189a0759ad"></a>

```c
#define BT_ETS_SUPPORTED_FLAGS_MASK
```

相关声明：[BT_ETS_SUPPORTED_FLAGS_MASK](#ga4d2718c8e1dad8812b4ed6189a0759ad)。

根据配置组合的受支持标志掩码（Supported Flags Mask）。

<a id="r_ga382c30c637d9d000f4deeda72d110fcf"></a>

```c
#define BT_ETS_CLOCK_CAPABILITIES_VALUE
```

相关声明：[BT_ETS_CLOCK_CAPABILITIES_VALUE](#ga382c30c637d9d000f4deeda72d110fcf)。

时钟能力（Clock Capabilities），见经过时间服务（Elapsed Time Service）第 3.1.1.3 节。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.3\_枚举（Enumerations）

<a id="r_ga23455566e363b7b54b4d71b56e982322"></a>

```c
enum bt_ets_time_resolution { BT_ETS_RESOLUTION_1_SEC = 0 , BT_ETS_RESOLUTION_100_MS = 1 , BT_ETS_RESOLUTION_1_MS = 2 , BT_ETS_RESOLUTION_100_US = 3 }
```

相关声明：[bt_ets_time_resolution](#ga23455566e363b7b54b4d71b56e982322)、[BT_ETS_RESOLUTION_1_SEC](#gga23455566e363b7b54b4d71b56e982322a882686a57199a753b2e40cc5abc9f298)、[BT_ETS_RESOLUTION_100_MS](#gga23455566e363b7b54b4d71b56e982322a5a83f42c780a6c87682f6c0406d64316)、[BT_ETS_RESOLUTION_1_MS](#gga23455566e363b7b54b4d71b56e982322aad9a457744816e678c27d1366bf04f9e)、[BT_ETS_RESOLUTION_100_US](#gga23455566e363b7b54b4d71b56e982322af31989dd56bfdaf185ffe2dbdcab34cb)。

flags 字段位 2～3 的时间分辨率值（Time Resolution Values）。

<a id="r_ga37a169057efc9b463ad531fd1f131fff"></a>

```c
enum bt_ets_write_result { BT_ETS_WRITE_SUCCESS = 0 , BT_ETS_WRITE_TIME_SOURCE_TOO_LOW = 1 , BT_ETS_WRITE_OUT_OF_RANGE = 2 , BT_ETS_WRITE_INCORRECT_FORMAT = 3 }
```

相关声明：[bt_ets_write_result](#ga37a169057efc9b463ad531fd1f131fff)、[BT_ETS_WRITE_SUCCESS](#gga37a169057efc9b463ad531fd1f131fffadac86ed9c0c2424fee546a78e143eced)、[BT_ETS_WRITE_TIME_SOURCE_TOO_LOW](#gga37a169057efc9b463ad531fd1f131fffa9dc1f1f12a97cb23ec4051138f559817)、[BT_ETS_WRITE_OUT_OF_RANGE](#gga37a169057efc9b463ad531fd1f131fffa06532377ea56330ecdcfdc0b25dd594f)、[BT_ETS_WRITE_INCORRECT_FORMAT](#gga37a169057efc9b463ad531fd1f131fffab3deb6e75d374b4766acdbac0e87e54e)。

write_elapsed_time 回调的写入结果码（Write Result Codes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.4\_函数（Functions）

<a id="r_gae1a76312c1c6bc31443860dd10ab0a54"></a>

```c
int bt_ets_init (const struct bt_ets_cb *cb)
```

相关声明：[bt_ets_init](#gae1a76312c1c6bc31443860dd10ab0a54)、[bt_ets_cb](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md)。

初始化经过时间服务（Elapsed Time Service）。

<a id="r_ga8cd79739c350f266b134a26b0b0ec7fc"></a>

```c
int bt_ets_indicate (const struct bt_ets_elapsed_time *elapsed_time, uint8_t clock_status)
```

相关声明：[bt_ets_indicate](#ga8cd79739c350f266b134a26b0b0ec7fc)、[bt_ets_elapsed_time](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向已订阅的客户端发送指示（Indication）。

<a id="r_ga59747d0fe1a33f5c84040d90dbbf6f6d"></a>

```c
int bt_ets_time_to_unix_ms (const struct bt_ets_elapsed_time *et_time, int64_t *unix_ms)
```

相关声明：[bt_ets_time_to_unix_ms](#ga59747d0fe1a33f5c84040d90dbbf6f6d)、[bt_ets_elapsed_time](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

将 ETS 格式时间解码为自 Unix 纪元（Unix Epoch）以来的毫秒数。

<a id="r_ga4f3d175e71ef213ae5d16b2b853f9481"></a>

```c
int bt_ets_time_from_unix_ms (struct bt_ets_elapsed_time *et_time, int64_t unix_ms, uint8_t time_src, int8_t tz_dst_offset)
```

相关声明：[bt_ets_time_from_unix_ms](#ga4f3d175e71ef213ae5d16b2b853f9481)、[bt_ets_elapsed_time](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

将 Unix 毫秒数编码为 ETS 格式时间。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 3.5\_经过时间服务标志（Elapsed Time Service Flags）

经过时间服务（Elapsed Time Service）的 flags 字段位，见 GATT 规范补充（GATT Specification Supplement）第 3.82 节。



<a id="r_ga466686c78becbe5d1636e23c4ec2575f"></a>

```c
#define BT_ETS_FLAG_TICK_COUNTER BIT(0)
```

相关声明：[BT_ETS_FLAG_TICK_COUNTER](#ga466686c78becbe5d1636e23c4ec2575f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间值（Time Value）报告计数器，即滴答计数器（Tick Counter）。

<a id="r_ga9dae75e399ec2d47960dff6f0c6b3e2e"></a>

```c
#define BT_ETS_FLAG_UTC BIT(1)
```

相关声明：[BT_ETS_FLAG_UTC](#ga9dae75e399ec2d47960dff6f0c6b3e2e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间为协调世界时（UTC）。

<a id="r_gaf3d42f9d026beece0fc3835611a6a7d8"></a>

```c
#define BT_ETS_FLAG_RESOLUTION_MASK (BIT(2) | BIT(3))
```

相关声明：[BT_ETS_FLAG_RESOLUTION_MASK](#gaf3d42f9d026beece0fc3835611a6a7d8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间分辨率掩码（Time Resolution Mask），位 2～3。

<a id="r_ga6103820129eff83cf96fcbdd87d86789"></a>

```c
#define BT_ETS_FLAG_TZ_DST_USED BIT(4)
```

相关声明：[BT_ETS_FLAG_TZ_DST_USED](#ga6103820129eff83cf96fcbdd87d86789)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使用时区／夏令时偏移（TZ/DST Offset）。

<a id="r_gab5017fd35ce24de74367a17e4285ffc6"></a>

```c
#define BT_ETS_FLAG_CURRENT_TIMELINE BIT(5)
```

相关声明：[BT_ETS_FLAG_CURRENT_TIMELINE](#gab5017fd35ce24de74367a17e4285ffc6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间戳（Time Stamp）来自当前时间线（Timeline）。

<a id="r_ga72cbad8715c21a8d646baed8a3cc930a"></a>

```c
#define BT_ETS_FLAG_RESERVED_MASK (BIT(6) | BIT(7))
```

相关声明：[BT_ETS_FLAG_RESERVED_MASK](#ga72cbad8715c21a8d646baed8a3cc930a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

保留位（Reserved Bits），位 6～7。

## 3.6\_时间源值（Time Source Values）

时间同步源值（Time Synchronization Source Values），见 GATT 规范补充（GATT Specification Supplement）第 3.243 节。



<a id="r_ga66de6bff35685c94e123431121bf6677"></a>

```c
#define BT_ETS_TIME_SOURCE_UNKNOWN 0
```

相关声明：[BT_ETS_TIME_SOURCE_UNKNOWN](#ga66de6bff35685c94e123431121bf6677)。

未知时间源（Unknown Time Source）。

<a id="r_ga06c21bd4308205da2a2eab127ba21500"></a>

```c
#define BT_ETS_TIME_SOURCE_NTP 1
```

相关声明：[BT_ETS_TIME_SOURCE_NTP](#ga06c21bd4308205da2a2eab127ba21500)。

网络时间协议（Network Time Protocol，NTP）。

<a id="r_ga5850868097b7faa89d53a7d766b01c99"></a>

```c
#define BT_ETS_TIME_SOURCE_GPS 2
```

相关声明：[BT_ETS_TIME_SOURCE_GPS](#ga5850868097b7faa89d53a7d766b01c99)。

全球定位系统／全球导航卫星系统（GPS/GNSS）。

<a id="r_ga45dc79325782b18b35ee3b3c9bce65f5"></a>

```c
#define BT_ETS_TIME_SOURCE_RADIO 3
```

相关声明：[BT_ETS_TIME_SOURCE_RADIO](#ga45dc79325782b18b35ee3b3c9bce65f5)。

无线电授时信号（Radio Time Signal）。

<a id="r_ga0ce9342cad48aa0322bc22d4702140ec"></a>

```c
#define BT_ETS_TIME_SOURCE_MANUAL 4
```

相关声明：[BT_ETS_TIME_SOURCE_MANUAL](#ga0ce9342cad48aa0322bc22d4702140ec)。

手动设置（Manually Set）。

<a id="r_gaf1c612931d585b871ed1247053dcfb32"></a>

```c
#define BT_ETS_TIME_SOURCE_ATOMIC 5
```

相关声明：[BT_ETS_TIME_SOURCE_ATOMIC](#gaf1c612931d585b871ed1247053dcfb32)。

原子钟（Atomic Clock）。

<a id="r_ga1e49632311f61a9c84aa57e19e36a251"></a>

```c
#define BT_ETS_TIME_SOURCE_CELLULAR 6
```

相关声明：[BT_ETS_TIME_SOURCE_CELLULAR](#ga1e49632311f61a9c84aa57e19e36a251)。

蜂窝网络（Cellular Network）。

<a id="r_ga68f12eb3ad367b2541fbb220e4e4e5d2"></a>

```c
#define BT_ETS_TIME_SOURCE_NOT_SYNCHRONIZED 7
```

相关声明：[BT_ETS_TIME_SOURCE_NOT_SYNCHRONIZED](#ga68f12eb3ad367b2541fbb220e4e4e5d2)。

未同步（Not Synchronized）。

## 3.7\_时钟状态标志（Clock Status Flags）

时钟状态标志（Clock Status Flags），见经过时间服务（Elapsed Time Service）第 3.1.1.2 节。



<a id="r_ga5a9da9483136ef7e346d86a1fec61556"></a>

```c
#define BT_ETS_CLOCK_STATUS_NEEDS_SET BIT(0)
```

相关声明：[BT_ETS_CLOCK_STATUS_NEEDS_SET](#ga5a9da9483136ef7e346d86a1fec61556)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

需要设置时钟（Clock）。

<a id="r_ga8c052bfac2db437469ae0c9bc87bbc59"></a>

```c
#define BT_ETS_CLOCK_STATUS_RFU_MASK 0xFE
```

相关声明：[BT_ETS_CLOCK_STATUS_RFU_MASK](#ga8c052bfac2db437469ae0c9bc87bbc59)。

时钟状态保留供未来使用的掩码（Clock Status RFU Mask），位 1～7。

## 3.8\_时钟能力标志（Clock Capabilities Flags，经过时间服务第 3.1.1.3 节）



<a id="r_ga3798589a87c32a25069580b872b6601f"></a>

```c
#define BT_ETS_CLOCK_CAP_DST_AUTO BIT(0)
```

相关声明：[BT_ETS_CLOCK_CAP_DST_AUTO](#ga3798589a87c32a25069580b872b6601f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时钟自主应用夏令时规则（DST Rules）。

<a id="r_ga1aa745d31a958c79b959d75664057543"></a>

```c
#define BT_ETS_CLOCK_CAP_TZ_AUTO BIT(1)
```

相关声明：[BT_ETS_CLOCK_CAP_TZ_AUTO](#ga1aa745d31a958c79b959d75664057543)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时钟自主管理时区变化（TZ Changes）。

<a id="r_gaee89c8bc0e9a0d949312dd078409f84c"></a>

```c
#define BT_ETS_CLOCK_CAP_RFU_MASK 0xFC
```

相关声明：[BT_ETS_CLOCK_CAP_RFU_MASK](#gaee89c8bc0e9a0d949312dd078409f84c)。

时钟能力保留供未来使用的掩码（Clock Capabilities RFU Mask），位 2～7。

## 3.9\_详细说明（Detailed Documentation）

<a id="ga3798589a87c32a25069580b872b6601f"></a>

### `BT_ETS_CLOCK_CAP_DST_AUTO`

```c
#define BT_ETS_CLOCK_CAP_DST_AUTO BIT(0)
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

时钟自主应用夏令时规则（DST Rules）。

<a id="gaee89c8bc0e9a0d949312dd078409f84c"></a>

### `BT_ETS_CLOCK_CAP_RFU_MASK`

```c
#define BT_ETS_CLOCK_CAP_RFU_MASK 0xFC
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

时钟能力保留供未来使用的掩码（Clock Capabilities RFU Mask），位 2～7。

<a id="ga1aa745d31a958c79b959d75664057543"></a>

### `BT_ETS_CLOCK_CAP_TZ_AUTO`

```c
#define BT_ETS_CLOCK_CAP_TZ_AUTO BIT(1)
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

时钟自主管理时区变化（TZ Changes）。

<a id="ga382c30c637d9d000f4deeda72d110fcf"></a>

### `BT_ETS_CLOCK_CAPABILITIES_VALUE`

```c
#define BT_ETS_CLOCK_CAPABILITIES_VALUE
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

展开值（Value）：

```c
((IS_ENABLED(CONFIG_BT_ETS_CLOCK_CAP_DST_AUTO) ? BT_ETS_CLOCK_CAP_DST_AUTO : 0) |          \
 (IS_ENABLED(CONFIG_BT_ETS_CLOCK_CAP_TZ_AUTO) ? BT_ETS_CLOCK_CAP_TZ_AUTO : 0))
```

时钟能力（Clock Capabilities），见经过时间服务（Elapsed Time Service）第 3.1.1.3 节。

<a id="ga5a9da9483136ef7e346d86a1fec61556"></a>

### `BT_ETS_CLOCK_STATUS_NEEDS_SET`

```c
#define BT_ETS_CLOCK_STATUS_NEEDS_SET BIT(0)
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

需要设置时钟（Clock）。

为 0 时，时钟（Clock）已设置。

<a id="ga8c052bfac2db437469ae0c9bc87bbc59"></a>

### `BT_ETS_CLOCK_STATUS_RFU_MASK`

```c
#define BT_ETS_CLOCK_STATUS_RFU_MASK 0xFE
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

时钟状态保留供未来使用的掩码（Clock Status RFU Mask），位 1～7。

<a id="gab5017fd35ce24de74367a17e4285ffc6"></a>

### `BT_ETS_FLAG_CURRENT_TIMELINE`

```c
#define BT_ETS_FLAG_CURRENT_TIMELINE BIT(5)
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

时间戳（Time Stamp）来自当前时间线（Timeline）。

<a id="ga72cbad8715c21a8d646baed8a3cc930a"></a>

### `BT_ETS_FLAG_RESERVED_MASK`

```c
#define BT_ETS_FLAG_RESERVED_MASK (BIT(6) | BIT(7))
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

保留位（Reserved Bits），位 6～7。

<a id="gaf3d42f9d026beece0fc3835611a6a7d8"></a>

### `BT_ETS_FLAG_RESOLUTION_MASK`

```c
#define BT_ETS_FLAG_RESOLUTION_MASK (BIT(2) | BIT(3))
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

时间分辨率掩码（Time Resolution Mask），位 2～3。

<a id="ga466686c78becbe5d1636e23c4ec2575f"></a>

### `BT_ETS_FLAG_TICK_COUNTER`

```c
#define BT_ETS_FLAG_TICK_COUNTER BIT(0)
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

时间值（Time Value）报告计数器，即滴答计数器（Tick Counter）。

为 0 时，时间值（Time Value）报告一天中的时间（Time of Day）。

<a id="ga6103820129eff83cf96fcbdd87d86789"></a>

### `BT_ETS_FLAG_TZ_DST_USED`

```c
#define BT_ETS_FLAG_TZ_DST_USED BIT(4)
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

使用时区／夏令时偏移（TZ/DST Offset）。

为 0 时，不使用偏移量（Offset）。对于节拍计数器（Tick Counter）没有意义。

<a id="ga9dae75e399ec2d47960dff6f0c6b3e2e"></a>

### `BT_ETS_FLAG_UTC`

```c
#define BT_ETS_FLAG_UTC BIT(1)
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

时间为协调世界时（UTC）。

为 0 时，时间为本地时间（Local Time）。对于节拍计数器（Tick Counter）没有意义。

<a id="ga4d2718c8e1dad8812b4ed6189a0759ad"></a>

### `BT_ETS_SUPPORTED_FLAGS_MASK`

```c
#define BT_ETS_SUPPORTED_FLAGS_MASK
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

展开值（Value）：

```c
((IS_ENABLED(CONFIG_BT_ETS_SUPPORT_TICK_COUNTER) ? BT_ETS_FLAG_TICK_COUNTER : 0) |         \
 (IS_ENABLED(CONFIG_BT_ETS_SUPPORT_UTC) ? BT_ETS_FLAG_UTC : 0) |                           \
 (IS_ENABLED(CONFIG_BT_ETS_SUPPORT_TZ_DST) ? BT_ETS_FLAG_TZ_DST_USED : 0) |                \
 (IS_ENABLED(CONFIG_BT_ETS_RESOLUTION_1_SEC)    ? 0                                        \
  : IS_ENABLED(CONFIG_BT_ETS_RESOLUTION_100_MS) ? BIT(2)                                   \
  : IS_ENABLED(CONFIG_BT_ETS_RESOLUTION_1_MS)   ? BIT(3)                                   \
  : IS_ENABLED(CONFIG_BT_ETS_RESOLUTION_100_US) ? (BIT(2) | BIT(3))                        \
                                                : 0) |                                     \
 BT_ETS_FLAG_CURRENT_TIMELINE)
```

根据配置组合的受支持标志掩码（Supported Flags Mask）。

<a id="gaf1c612931d585b871ed1247053dcfb32"></a>

### `BT_ETS_TIME_SOURCE_ATOMIC`

```c
#define BT_ETS_TIME_SOURCE_ATOMIC 5
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

原子钟（Atomic Clock）。

<a id="ga1e49632311f61a9c84aa57e19e36a251"></a>

### `BT_ETS_TIME_SOURCE_CELLULAR`

```c
#define BT_ETS_TIME_SOURCE_CELLULAR 6
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

蜂窝网络（Cellular Network）。

<a id="ga5850868097b7faa89d53a7d766b01c99"></a>

### `BT_ETS_TIME_SOURCE_GPS`

```c
#define BT_ETS_TIME_SOURCE_GPS 2
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

全球定位系统／全球导航卫星系统（GPS/GNSS）。

<a id="ga0ce9342cad48aa0322bc22d4702140ec"></a>

### `BT_ETS_TIME_SOURCE_MANUAL`

```c
#define BT_ETS_TIME_SOURCE_MANUAL 4
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

手动设置（Manually Set）。

<a id="ga68f12eb3ad367b2541fbb220e4e4e5d2"></a>

### `BT_ETS_TIME_SOURCE_NOT_SYNCHRONIZED`

```c
#define BT_ETS_TIME_SOURCE_NOT_SYNCHRONIZED 7
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

未同步（Not Synchronized）。

<a id="ga06c21bd4308205da2a2eab127ba21500"></a>

### `BT_ETS_TIME_SOURCE_NTP`

```c
#define BT_ETS_TIME_SOURCE_NTP 1
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

网络时间协议（Network Time Protocol，NTP）。

<a id="ga45dc79325782b18b35ee3b3c9bce65f5"></a>

### `BT_ETS_TIME_SOURCE_RADIO`

```c
#define BT_ETS_TIME_SOURCE_RADIO 3
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

无线电授时信号（Radio Time Signal）。

<a id="ga66de6bff35685c94e123431121bf6677"></a>

### `BT_ETS_TIME_SOURCE_UNKNOWN`

```c
#define BT_ETS_TIME_SOURCE_UNKNOWN 0
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

未知时间源（Unknown Time Source）。

<a id="ga23455566e363b7b54b4d71b56e982322"></a>

### `bt_ets_time_resolution`

```c
enum bt_ets_time_resolution
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

flags 字段位 2～3 的时间分辨率值（Time Resolution Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_ETS_RESOLUTION_1_SEC` | 分辨率（Resolution）：1 秒。 |
| `BT_ETS_RESOLUTION_100_MS` | 分辨率（Resolution）：100 毫秒。 |
| `BT_ETS_RESOLUTION_1_MS` | 分辨率（Resolution）：1 毫秒。 |
| `BT_ETS_RESOLUTION_100_US` | 分辨率（Resolution）：100 微秒。 |

<a id="ga37a169057efc9b463ad531fd1f131fff"></a>

### `bt_ets_write_result`

```c
enum bt_ets_write_result
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

write_elapsed_time 回调的写入结果码（Write Result Codes）。

这些代码表示时间写入操作（Time Write Operation）的结果，并映射到 ETS 规范定义的特定 ATT 错误响应（ATT Error Response）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_ETS_WRITE_SUCCESS` | 成功接受写入（Write Accepted）。 |
| `BT_ETS_WRITE_TIME_SOURCE_TOO_LOW` | 时间源质量（Time Source Quality）过低，以 ATT 错误码 `0x80` 拒绝写入。 |
| `BT_ETS_WRITE_OUT_OF_RANGE` | 时间值（Time Value）超出可接受范围，以 ATT 错误码 `0xFF` 拒绝写入。 |
| `BT_ETS_WRITE_INCORRECT_FORMAT` | 时间格式（Time Format）不正确，标志（Flags）不匹配，以 ATT 错误码 `0x81` 拒绝写入。 |

<a id="ga8cd79739c350f266b134a26b0b0ec7fc"></a>

### `bt_ets_indicate()`

```c
int bt_ets_indicate ( const struct bt_ets_elapsed_time * elapsed_time, uint8_t clock_status )
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

向已订阅的客户端发送指示（Indication）。

向所有已订阅客户端发送指示（Indication），携带更新后的经过时间（Elapsed Time）。当时间发生自然流逝以外的变化时，应调用本函数，例如手动调整、外部时间同步、夏令时（DST）变化或时区变化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `elapsed_time` | 要通过指示（Indication）发送的经过时间（Elapsed Time）。 |
| `clock_status` | 当前时钟状态标志（Clock Status Flags，`BT_ETS_CLOCK_STATUS`）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-ENOTCONN` | 没有已连接或已订阅的客户端（Client）时。 |
| `-errno` | 失败时返回其他负 errno 错误码。 |

<a id="gae1a76312c1c6bc31443860dd10ab0a54"></a>

### `bt_ets_init()`

```c
int bt_ets_init ( const struct bt_ets_cb * cb)
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

初始化经过时间服务（Elapsed Time Service）。

必须在初始化期间调用。可以在 `bt_enable` 之前或之后调用，但必须早于广播（Advertising）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 已设置必需回调（Mandatory Callback）的回调结构体。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `cb` 为 `NULL`，或必需回调（Mandatory Callback）为 `NULL` 时。 |

<a id="ga4f3d175e71ef213ae5d16b2b853f9481"></a>

### `bt_ets_time_from_unix_ms()`

```c
int bt_ets_time_from_unix_ms ( struct bt_ets_elapsed_time * et_time, int64_t unix_ms, uint8_t time_src, int8_t tz_dst_offset )
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

将 Unix 毫秒数编码为 ETS 格式时间。

将 Unix 时间戳（Unix Timestamp，纪元为 1970-01-01 00:00:00 UTC）转换为 ETS 时间格式。根据编译时配置（Compile-time Configuration）处理纪元转换（Unix 的 1970-01-01 转为 ETS 的 2000-01-01）、分辨率缩放（Resolution Scaling）和时区转换（Timezone Conversion）。

输入 `unix_ms` 始终采用协调世界时（UTC）。`tz_dst_offset` 参数的行为如下：

- `CONFIG_BT_ETS_SUPPORT_UTC`：时间保持为协调世界时（UTC），不进行转换。如果启用 `CONFIG_BT_ETS_SUPPORT_TZ_DST`，则存储偏移量（Offset）供客户端使用。
- 同时启用 `CONFIG_BT_ETS_SUPPORT_LOCAL_TIME` 和 `CONFIG_BT_ETS_SUPPORT_TZ_DST`：应用偏移量（Offset）将 UTC 转换为本地时间，并将偏移量存储在输出中。公式：本地时间 = UTC 时间 + 时区／夏令时偏移（TZ/DST Offset）× 15 分钟。输出中设置 `BT_ETS_FLAG_TZ_DST_USED` 标志。

输出 `et_time` 的标志（Flags）根据编译时配置（Compile-time Configuration）设置：

- 时间模式（Time Mode）：`CONFIG_BT_ETS_SUPPORT_UTC` 或 `CONFIG_BT_ETS_SUPPORT_LOCAL_TIME`。
- 分辨率（Resolution）：`CONFIG_BT_ETS_RESOLUTION_*`，可选 `1_SEC`、`100_MS`、`1_MS` 或 `100_US`。
- 始终设置 `BT_ETS_FLAG_CURRENT_TIMELINE`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `et_time` | 指向待填充 ETS 时间结构体（Time Structure）的指针。 |
| `unix_ms` | 自 Unix 纪元（1970-01-01 00:00:00 UTC）起经过的毫秒数，始终采用协调世界时（UTC）。 |
| `time_src` | 时间同步源类型（Time Synchronization Source Type），参见 `BT_ETS_TIME_SOURCE`。 |
| `tz_dst_offset` | 相对于协调世界时（UTC）的时区／夏令时偏移（TZ/DST Offset），以 15 分钟为单位，带符号。在 `LOCAL_TIME` 模式下用于将 UTC 转换为本地时间。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `et_time` 为 `NULL`，或转换后的时间早于 ETS 纪元（2000-01-01）时。 |
| `-EOVERFLOW` | 转换后的时间值超出 48 位范围时。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_ETS_HELPER_API` 时可用。

**说明（Note）**：注意（Note）：要求启用 `CONFIG_BT_ETS_SUPPORT_UTC` 或 `CONFIG_BT_ETS_SUPPORT_TZ_DST`。

<a id="ga59747d0fe1a33f5c84040d90dbbf6f6d"></a>

### `bt_ets_time_to_unix_ms()`

```c
int bt_ets_time_to_unix_ms ( const struct bt_ets_elapsed_time * et_time, int64_t * unix_ms )
```

```c
#include <zephyr/bluetooth/services/ets.h>
```

将 ETS 格式时间解码为自 Unix 纪元（Unix Epoch）以来的毫秒数。

将 ETS 时间格式转换为自 Unix 纪元（1970-01-01 00:00:00 UTC）起经过的毫秒数。根据 `et_time` 中的 `flags` 字段，处理纪元转换（ETS 使用 2000-01-01，而 Unix 使用 1970-01-01）、分辨率缩放（Resolution Scaling）和时区转换（Timezone Conversion）。

输出 `unix_ms` 始终采用协调世界时（UTC）。根据标志（Flags）按以下方式处理时区：

- `CONFIG_BT_ETS_SUPPORT_UTC`：时间已经是协调世界时（UTC），无须转换。如果设置 `BT_ETS_FLAG_TZ_DST_USED`，偏移量（Offset）仅用于提供信息。
- 同时启用 `CONFIG_BT_ETS_SUPPORT_LOCAL_TIME` 和 `CONFIG_BT_ETS_SUPPORT_TZ_DST`：如果 `et_time` 中设置了 `BT_ETS_FLAG_TZ_DST_USED`，则减去偏移量（Offset），将本地时间转换为 UTC：UTC = 本地时间 − 时区／夏令时偏移（TZ/DST Offset）× 15 分钟。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `et_time` | 要解码的 ETS 时间格式结构体（ETS Time Formatted Structure）。 |
| `unix_ms` | 用于存储自 Unix 纪元（1970-01-01 00:00:00 UTC）起经过的毫秒数的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | `et_time` 或 `unix_ms` 为 `NULL` 时。 |
| `-EOVERFLOW` | 时间值在转换期间发生溢出（Overflow）时。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_BT_ETS_HELPER_API` 时可用。

**说明（Note）**：注意（Note）：要求启用 `CONFIG_BT_ETS_SUPPORT_UTC` 或 `CONFIG_BT_ETS_SUPPORT_TZ_DST`；正确转换为 UTC 需要 UTC 模式或时区偏移信息。


## 3.10\_原页交叉引用（Cross References）

- [bt_ets_elapsed_time](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md)
- [bt_ets_cb](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [zephyr/bluetooth/services/ets.h](../api_file_clock_network_reference/P010_zephyr__bluetooth__services__ets.h_文件参考.md)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [CONFIG_BT_ETS_SUPPORT_UTC](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ETS_SUPPORT_UTC)
- [CONFIG_BT_ETS_SUPPORT_TZ_DST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ETS_SUPPORT_TZ_DST)
- [CONFIG_BT_ETS_SUPPORT_LOCAL_TIME](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ETS_SUPPORT_LOCAL_TIME)
- [CONFIG_BT_ETS_HELPER_API](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ETS_HELPER_API)

<a id="BT_ETS_FLAGS"></a>
<a id="BT_ETS_TIME_SOURCE"></a>
<a id="BT_ETS_CLOCK_STATUS"></a>
<a id="BT_ETS_CLOCK_CAPABILITIES"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__bt__ets_html_ga1aa745d31a958c79b959d75664057543"></a>
<a id="agroup__bt__ets_html_ga3798589a87c32a25069580b872b6601f"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="agroup__bt__ets_html_ga466686c78becbe5d1636e23c4ec2575f"></a>
<a id="agroup__bt__ets_html_ga6103820129eff83cf96fcbdd87d86789"></a>
<a id="agroup__bt__ets_html_ga9dae75e399ec2d47960dff6f0c6b3e2e"></a>
<a id="agroup__bt__ets_html_gab5017fd35ce24de74367a17e4285ffc6"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga23455566e363b7b54b4d71b56e982322a882686a57199a753b2e40cc5abc9f298"></a>
<a id="gga23455566e363b7b54b4d71b56e982322a5a83f42c780a6c87682f6c0406d64316"></a>
<a id="gga23455566e363b7b54b4d71b56e982322aad9a457744816e678c27d1366bf04f9e"></a>
<a id="gga23455566e363b7b54b4d71b56e982322af31989dd56bfdaf185ffe2dbdcab34cb"></a>
<a id="gga37a169057efc9b463ad531fd1f131fffadac86ed9c0c2424fee546a78e143eced"></a>
<a id="gga37a169057efc9b463ad531fd1f131fffa9dc1f1f12a97cb23ec4051138f559817"></a>
<a id="gga37a169057efc9b463ad531fd1f131fffa06532377ea56330ecdcfdc0b25dd594f"></a>
<a id="gga37a169057efc9b463ad531fd1f131fffab3deb6e75d374b4766acdbac0e87e54e"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_设备地址（Device Address）.md) · [返回大纲](大纲.md) · [下一章](P004_消息客户端设备（Messaging Client Equipment，MCE）的 OBEX 客户端.md)
