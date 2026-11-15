---
id: learning.zephyr-docs.api-file-clock-network-reference.page-10
title: zephyr__bluetooth__services__ets.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ets_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_bluetooth\_\_services\_\_ets.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ets_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

经过时间服务（Elapsed Time Service，ETS）。

<a id="details"></a>

```c
#include <stdint.h>
#include <stdbool.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

经过时间服务（Elapsed Time Service，ETS）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

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

## 10.2\_宏定义（Macros）

<a id="r_ga4d2718c8e1dad8812b4ed6189a0759ad"></a>

```c
#define BT_ETS_SUPPORTED_FLAGS_MASK
```

相关声明：[BT_ETS_SUPPORTED_FLAGS_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga4d2718c8e1dad8812b4ed6189a0759ad)。

根据配置组合的受支持标志掩码（Supported Flags Mask）。

<a id="r_ga382c30c637d9d000f4deeda72d110fcf"></a>

```c
#define BT_ETS_CLOCK_CAPABILITIES_VALUE
```

相关声明：[BT_ETS_CLOCK_CAPABILITIES_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga382c30c637d9d000f4deeda72d110fcf)。

时钟能力（Clock Capabilities），见经过时间服务（Elapsed Time Service）第 3.1.1.3 节。

<a id="define-members-0"></a>

### 经过时间服务标志（Elapsed Time Service Flags）

经过时间服务（Elapsed Time Service）的 flags 字段位，见 GATT 规范补充（GATT Specification Supplement）第 3.82 节。



<a id="r_ga466686c78becbe5d1636e23c4ec2575f"></a>

```c
#define BT_ETS_FLAG_TICK_COUNTER BIT(0)
```

相关声明：[BT_ETS_FLAG_TICK_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga466686c78becbe5d1636e23c4ec2575f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间值（Time Value）报告计数器，即滴答计数器（Tick Counter）。

<a id="r_ga9dae75e399ec2d47960dff6f0c6b3e2e"></a>

```c
#define BT_ETS_FLAG_UTC BIT(1)
```

相关声明：[BT_ETS_FLAG_UTC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga9dae75e399ec2d47960dff6f0c6b3e2e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间为协调世界时（UTC）。

<a id="r_gaf3d42f9d026beece0fc3835611a6a7d8"></a>

```c
#define BT_ETS_FLAG_RESOLUTION_MASK (BIT(2) | BIT(3))
```

相关声明：[BT_ETS_FLAG_RESOLUTION_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gaf3d42f9d026beece0fc3835611a6a7d8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间分辨率掩码（Time Resolution Mask），位 2～3。

<a id="r_ga6103820129eff83cf96fcbdd87d86789"></a>

```c
#define BT_ETS_FLAG_TZ_DST_USED BIT(4)
```

相关声明：[BT_ETS_FLAG_TZ_DST_USED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga6103820129eff83cf96fcbdd87d86789)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使用时区／夏令时偏移（TZ/DST Offset）。

<a id="r_gab5017fd35ce24de74367a17e4285ffc6"></a>

```c
#define BT_ETS_FLAG_CURRENT_TIMELINE BIT(5)
```

相关声明：[BT_ETS_FLAG_CURRENT_TIMELINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gab5017fd35ce24de74367a17e4285ffc6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时间戳（Time Stamp）来自当前时间线（Timeline）。

<a id="r_ga72cbad8715c21a8d646baed8a3cc930a"></a>

```c
#define BT_ETS_FLAG_RESERVED_MASK (BIT(6) | BIT(7))
```

相关声明：[BT_ETS_FLAG_RESERVED_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga72cbad8715c21a8d646baed8a3cc930a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

保留位（Reserved Bits），位 6～7。

<a id="define-members-1"></a>

### 时间源值（Time Source Values）

时间同步源值（Time Synchronization Source Values），见 GATT 规范补充（GATT Specification Supplement）第 3.243 节。



<a id="r_ga66de6bff35685c94e123431121bf6677"></a>

```c
#define BT_ETS_TIME_SOURCE_UNKNOWN 0
```

相关声明：[BT_ETS_TIME_SOURCE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga66de6bff35685c94e123431121bf6677)。

未知时间源（Unknown Time Source）。

<a id="r_ga06c21bd4308205da2a2eab127ba21500"></a>

```c
#define BT_ETS_TIME_SOURCE_NTP 1
```

相关声明：[BT_ETS_TIME_SOURCE_NTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga06c21bd4308205da2a2eab127ba21500)。

网络时间协议（Network Time Protocol，NTP）。

<a id="r_ga5850868097b7faa89d53a7d766b01c99"></a>

```c
#define BT_ETS_TIME_SOURCE_GPS 2
```

相关声明：[BT_ETS_TIME_SOURCE_GPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga5850868097b7faa89d53a7d766b01c99)。

全球定位系统／全球导航卫星系统（GPS/GNSS）。

<a id="r_ga45dc79325782b18b35ee3b3c9bce65f5"></a>

```c
#define BT_ETS_TIME_SOURCE_RADIO 3
```

相关声明：[BT_ETS_TIME_SOURCE_RADIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga45dc79325782b18b35ee3b3c9bce65f5)。

无线电授时信号（Radio Time Signal）。

<a id="r_ga0ce9342cad48aa0322bc22d4702140ec"></a>

```c
#define BT_ETS_TIME_SOURCE_MANUAL 4
```

相关声明：[BT_ETS_TIME_SOURCE_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga0ce9342cad48aa0322bc22d4702140ec)。

手动设置（Manually Set）。

<a id="r_gaf1c612931d585b871ed1247053dcfb32"></a>

```c
#define BT_ETS_TIME_SOURCE_ATOMIC 5
```

相关声明：[BT_ETS_TIME_SOURCE_ATOMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gaf1c612931d585b871ed1247053dcfb32)。

原子钟（Atomic Clock）。

<a id="r_ga1e49632311f61a9c84aa57e19e36a251"></a>

```c
#define BT_ETS_TIME_SOURCE_CELLULAR 6
```

相关声明：[BT_ETS_TIME_SOURCE_CELLULAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga1e49632311f61a9c84aa57e19e36a251)。

蜂窝网络（Cellular Network）。

<a id="r_ga68f12eb3ad367b2541fbb220e4e4e5d2"></a>

```c
#define BT_ETS_TIME_SOURCE_NOT_SYNCHRONIZED 7
```

相关声明：[BT_ETS_TIME_SOURCE_NOT_SYNCHRONIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga68f12eb3ad367b2541fbb220e4e4e5d2)。

未同步（Not Synchronized）。

<a id="define-members-2"></a>

### 时钟状态标志（Clock Status Flags）

时钟状态标志（Clock Status Flags），见经过时间服务（Elapsed Time Service）第 3.1.1.2 节。



<a id="r_ga5a9da9483136ef7e346d86a1fec61556"></a>

```c
#define BT_ETS_CLOCK_STATUS_NEEDS_SET BIT(0)
```

相关声明：[BT_ETS_CLOCK_STATUS_NEEDS_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga5a9da9483136ef7e346d86a1fec61556)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

需要设置时钟（Clock）。

<a id="r_ga8c052bfac2db437469ae0c9bc87bbc59"></a>

```c
#define BT_ETS_CLOCK_STATUS_RFU_MASK 0xFE
```

相关声明：[BT_ETS_CLOCK_STATUS_RFU_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga8c052bfac2db437469ae0c9bc87bbc59)。

时钟状态保留供未来使用的掩码（Clock Status RFU Mask），位 1～7。

<a id="define-members-3"></a>

### 时钟能力标志（Clock Capabilities Flags，经过时间服务第 3.1.1.3 节）



<a id="r_ga3798589a87c32a25069580b872b6601f"></a>

```c
#define BT_ETS_CLOCK_CAP_DST_AUTO BIT(0)
```

相关声明：[BT_ETS_CLOCK_CAP_DST_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga3798589a87c32a25069580b872b6601f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时钟自主应用夏令时规则（DST Rules）。

<a id="r_ga1aa745d31a958c79b959d75664057543"></a>

```c
#define BT_ETS_CLOCK_CAP_TZ_AUTO BIT(1)
```

相关声明：[BT_ETS_CLOCK_CAP_TZ_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga1aa745d31a958c79b959d75664057543)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

时钟自主管理时区变化（TZ Changes）。

<a id="r_gaee89c8bc0e9a0d949312dd078409f84c"></a>

```c
#define BT_ETS_CLOCK_CAP_RFU_MASK 0xFC
```

相关声明：[BT_ETS_CLOCK_CAP_RFU_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gaee89c8bc0e9a0d949312dd078409f84c)。

时钟能力保留供未来使用的掩码（Clock Capabilities RFU Mask），位 2～7。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.3\_枚举（Enumerations）

<a id="r_ga23455566e363b7b54b4d71b56e982322"></a>

```c
enum bt_ets_time_resolution { BT_ETS_RESOLUTION_1_SEC = 0 , BT_ETS_RESOLUTION_100_MS = 1 , BT_ETS_RESOLUTION_1_MS = 2 , BT_ETS_RESOLUTION_100_US = 3 }
```

相关声明：[bt_ets_time_resolution](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga23455566e363b7b54b4d71b56e982322)、[BT_ETS_RESOLUTION_1_SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga23455566e363b7b54b4d71b56e982322a882686a57199a753b2e40cc5abc9f298)、[BT_ETS_RESOLUTION_100_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga23455566e363b7b54b4d71b56e982322a5a83f42c780a6c87682f6c0406d64316)、[BT_ETS_RESOLUTION_1_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga23455566e363b7b54b4d71b56e982322aad9a457744816e678c27d1366bf04f9e)、[BT_ETS_RESOLUTION_100_US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga23455566e363b7b54b4d71b56e982322af31989dd56bfdaf185ffe2dbdcab34cb)。

flags 字段位 2～3 的时间分辨率值（Time Resolution Values）。

<a id="r_ga37a169057efc9b463ad531fd1f131fff"></a>

```c
enum bt_ets_write_result { BT_ETS_WRITE_SUCCESS = 0 , BT_ETS_WRITE_TIME_SOURCE_TOO_LOW = 1 , BT_ETS_WRITE_OUT_OF_RANGE = 2 , BT_ETS_WRITE_INCORRECT_FORMAT = 3 }
```

相关声明：[bt_ets_write_result](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga37a169057efc9b463ad531fd1f131fff)、[BT_ETS_WRITE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga37a169057efc9b463ad531fd1f131fffadac86ed9c0c2424fee546a78e143eced)、[BT_ETS_WRITE_TIME_SOURCE_TOO_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga37a169057efc9b463ad531fd1f131fffa9dc1f1f12a97cb23ec4051138f559817)、[BT_ETS_WRITE_OUT_OF_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga37a169057efc9b463ad531fd1f131fffa06532377ea56330ecdcfdc0b25dd594f)、[BT_ETS_WRITE_INCORRECT_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga37a169057efc9b463ad531fd1f131fffab3deb6e75d374b4766acdbac0e87e54e)。

write_elapsed_time 回调的写入结果码（Write Result Codes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.4\_函数（Functions）

<a id="r_gae1a76312c1c6bc31443860dd10ab0a54"></a>

```c
int bt_ets_init (const struct bt_ets_cb *cb)
```

相关声明：[bt_ets_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gae1a76312c1c6bc31443860dd10ab0a54)、[bt_ets_cb](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md)。

初始化经过时间服务（Elapsed Time Service）。

<a id="r_ga8cd79739c350f266b134a26b0b0ec7fc"></a>

```c
int bt_ets_indicate (const struct bt_ets_elapsed_time *elapsed_time, uint8_t clock_status)
```

相关声明：[bt_ets_indicate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga8cd79739c350f266b134a26b0b0ec7fc)、[bt_ets_elapsed_time](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向已订阅的客户端发送指示（Indication）。

<a id="r_ga59747d0fe1a33f5c84040d90dbbf6f6d"></a>

```c
int bt_ets_time_to_unix_ms (const struct bt_ets_elapsed_time *et_time, int64_t *unix_ms)
```

相关声明：[bt_ets_time_to_unix_ms](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga59747d0fe1a33f5c84040d90dbbf6f6d)、[bt_ets_elapsed_time](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

将 ETS 格式时间解码为自 Unix 纪元（Unix Epoch）以来的毫秒数。

<a id="r_ga4f3d175e71ef213ae5d16b2b853f9481"></a>

```c
int bt_ets_time_from_unix_ms (struct bt_ets_elapsed_time *et_time, int64_t unix_ms, uint8_t time_src, int8_t tz_dst_offset)
```

相关声明：[bt_ets_time_from_unix_ms](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga4f3d175e71ef213ae5d16b2b853f9481)、[bt_ets_elapsed_time](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)。

将 Unix 毫秒数编码为 ETS 格式时间。


## 10.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P248_ets.h_源码浏览.md)
- [bt_ets_elapsed_time](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md)
- [bt_ets_cb](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md)
- [BT_ETS_SUPPORTED_FLAGS_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga4d2718c8e1dad8812b4ed6189a0759ad)
- [BT_ETS_CLOCK_CAPABILITIES_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga382c30c637d9d000f4deeda72d110fcf)
- [BT_ETS_FLAG_TICK_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga466686c78becbe5d1636e23c4ec2575f)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_ETS_FLAG_UTC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga9dae75e399ec2d47960dff6f0c6b3e2e)
- [BT_ETS_FLAG_RESOLUTION_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gaf3d42f9d026beece0fc3835611a6a7d8)
- [BT_ETS_FLAG_TZ_DST_USED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga6103820129eff83cf96fcbdd87d86789)
- [BT_ETS_FLAG_CURRENT_TIMELINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gab5017fd35ce24de74367a17e4285ffc6)
- [BT_ETS_FLAG_RESERVED_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga72cbad8715c21a8d646baed8a3cc930a)
- [BT_ETS_TIME_SOURCE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga66de6bff35685c94e123431121bf6677)
- [BT_ETS_TIME_SOURCE_NTP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga06c21bd4308205da2a2eab127ba21500)
- [BT_ETS_TIME_SOURCE_GPS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga5850868097b7faa89d53a7d766b01c99)
- [BT_ETS_TIME_SOURCE_RADIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga45dc79325782b18b35ee3b3c9bce65f5)
- [BT_ETS_TIME_SOURCE_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga0ce9342cad48aa0322bc22d4702140ec)
- [BT_ETS_TIME_SOURCE_ATOMIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gaf1c612931d585b871ed1247053dcfb32)
- [BT_ETS_TIME_SOURCE_CELLULAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga1e49632311f61a9c84aa57e19e36a251)
- [BT_ETS_TIME_SOURCE_NOT_SYNCHRONIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga68f12eb3ad367b2541fbb220e4e4e5d2)
- [BT_ETS_CLOCK_STATUS_NEEDS_SET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga5a9da9483136ef7e346d86a1fec61556)
- [BT_ETS_CLOCK_STATUS_RFU_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga8c052bfac2db437469ae0c9bc87bbc59)
- [BT_ETS_CLOCK_CAP_DST_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga3798589a87c32a25069580b872b6601f)
- [BT_ETS_CLOCK_CAP_TZ_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga1aa745d31a958c79b959d75664057543)
- [BT_ETS_CLOCK_CAP_RFU_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gaee89c8bc0e9a0d949312dd078409f84c)
- [bt_ets_time_resolution](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga23455566e363b7b54b4d71b56e982322)
- [BT_ETS_RESOLUTION_1_SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga23455566e363b7b54b4d71b56e982322a882686a57199a753b2e40cc5abc9f298)
- [BT_ETS_RESOLUTION_100_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga23455566e363b7b54b4d71b56e982322a5a83f42c780a6c87682f6c0406d64316)
- [BT_ETS_RESOLUTION_1_MS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga23455566e363b7b54b4d71b56e982322aad9a457744816e678c27d1366bf04f9e)
- [BT_ETS_RESOLUTION_100_US](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga23455566e363b7b54b4d71b56e982322af31989dd56bfdaf185ffe2dbdcab34cb)
- [bt_ets_write_result](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga37a169057efc9b463ad531fd1f131fff)
- [BT_ETS_WRITE_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga37a169057efc9b463ad531fd1f131fffadac86ed9c0c2424fee546a78e143eced)
- [BT_ETS_WRITE_TIME_SOURCE_TOO_LOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga37a169057efc9b463ad531fd1f131fffa9dc1f1f12a97cb23ec4051138f559817)
- [BT_ETS_WRITE_OUT_OF_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga37a169057efc9b463ad531fd1f131fffa06532377ea56330ecdcfdc0b25dd594f)
- [BT_ETS_WRITE_INCORRECT_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gga37a169057efc9b463ad531fd1f131fffab3deb6e75d374b4766acdbac0e87e54e)
- [bt_ets_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gae1a76312c1c6bc31443860dd10ab0a54)
- [bt_ets_indicate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga8cd79739c350f266b134a26b0b0ec7fc)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_ets_time_to_unix_ms](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga59747d0fe1a33f5c84040d90dbbf6f6d)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [bt_ets_time_from_unix_ms](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga4f3d175e71ef213ae5d16b2b853f9481)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)

<a id="BT_ETS_FLAGS"></a>
<a id="BT_ETS_TIME_SOURCE"></a>
<a id="BT_ETS_CLOCK_STATUS"></a>
<a id="BT_ETS_CLOCK_CAPABILITIES"></a>
<a id="header-details"></a>

---

[上一章](P009_zephyr__dt-bindings__clock__esp32p4_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__dt-bindings__clock__gd32c2x1-clocks.h_文件参考.md)
