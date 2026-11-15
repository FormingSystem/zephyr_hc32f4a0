---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-2
title: 当前时间服务（Current Time Service，CTS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_当前时间服务（Current Time Service，CTS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

当前时间服务（Current Time Service，CTS）

<a id="details"></a>

当前时间服务（Current Time Service，CTS）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fcts_5Ftime_5Fformat"></a>

```c
struct bt_cts_time_format
```

相关声明：[bt_cts_time_format](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md)。

当前时间服务（Current Time Service）的数据格式，详细信息参见相应规范。

<a id="r_bt_5Fcts_5Flocal_5Ftime"></a>

```c
struct bt_cts_local_time
```

相关声明：[bt_cts_local_time](../bluetooth_service_model_reference/P064_bt_cts_local_time_结构体.md)。

CTS 本地时间信息（Local Time Information）。

<a id="r_bt_5Fcts_5Fcb"></a>

```c
struct bt_cts_cb
```

相关声明：[bt_cts_cb](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md)。

当前时间服务（Current Time Service，CTS）的回调结构体。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga7c8b0c61c584e34e270d6bc4ec1b3734"></a>

```c
#define BT_CTS_ATT_ERR_VALUES_IGNORED 0x80U
```

相关声明：[BT_CTS_ATT_ERR_VALUES_IGNORED](#ga7c8b0c61c584e34e270d6bc4ec1b3734)。

当前时间服务（CTS）写入操作中因忽略值而返回的 ATT 错误码。

<a id="r_ga5881ae83724a7934105e808e95a8e880"></a>

```c
#define BT_CTS_FRACTION_256_MAX_VALUE 255U
```

相关声明：[BT_CTS_FRACTION_256_MAX_VALUE](#ga5881ae83724a7934105e808e95a8e880)。

CTS 时间格式中以 1/256 秒为单位的小数秒字段（Fractions Field）的最大值。

<a id="r_ga38e3b4fec488ba4bcfcff097c752c32f"></a>

```c
#define BT_CTS_TIMEZONE_DEFAULT_VALUE -128
```

相关声明：[BT_CTS_TIMEZONE_DEFAULT_VALUE](#ga38e3b4fec488ba4bcfcff097c752c32f)。

表示时区未知的默认时区偏移值（Timezone Offset Value），按 15 分钟递增。

<a id="r_ga8899d79ef736989a3ae4137430492ad6"></a>

```c
#define BT_CTS_TIMEZONE_INCREMENT_MIN 15U
```

相关声明：[BT_CTS_TIMEZONE_INCREMENT_MIN](#ga8899d79ef736989a3ae4137430492ad6)。

时区偏移增量（Timezone Offset Increment），单位为分钟。

<a id="r_ga9edfc5a1b76923d87c97145ec934bc63"></a>

```c
#define BT_CTS_DST_INCREMENT_MIN 15U
```

相关声明：[BT_CTS_DST_INCREMENT_MIN](#ga9edfc5a1b76923d87c97145ec934bc63)。

夏令时偏移增量（DST Offset Increment），单位为分钟。

<a id="r_ga07b7421ed77c307503e154c5823ab32d"></a>

```c
#define BT_CTS_TIMEZONE_MIN -48
```

相关声明：[BT_CTS_TIMEZONE_MIN](#ga07b7421ed77c307503e154c5823ab32d)。

最小有效时区偏移（Timezone Offset），以 15 分钟为单位；`-48` 表示 UTC−12:00。

<a id="r_ga204f8d7595bd169f4e547e66b8ca36b4"></a>

```c
#define BT_CTS_TIMEZONE_MAX 56
```

相关声明：[BT_CTS_TIMEZONE_MAX](#ga204f8d7595bd169f4e547e66b8ca36b4)。

最大有效时区偏移（Timezone Offset），以 15 分钟为单位；`56` 表示 UTC+14:00。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.3\_枚举（Enumerations）

<a id="r_gaea1ec94140fa450b8493540c1ec2511a"></a>

```c
enum bt_cts_dst_offset { BT_CTS_DST_OFFSET_STANDARD_TIME = 0 , BT_CTS_DST_OFFSET_HALF_HOUR_DAYLIGHT_TIME = 2 , BT_CTS_DST_OFFSET_DAYLIGHT_TIME = 4 , BT_CTS_DST_OFFSET_DOUBLE_DAYLIGHT_TIME = 8 , BT_CTS_DST_OFFSET_UNKNOWN = 255 }
```

相关声明：[bt_cts_dst_offset](#gaea1ec94140fa450b8493540c1ec2511a)、[BT_CTS_DST_OFFSET_STANDARD_TIME](#ggaea1ec94140fa450b8493540c1ec2511aa5930b4efad215cbbc9b4ee228b0fa6e7)、[BT_CTS_DST_OFFSET_HALF_HOUR_DAYLIGHT_TIME](#ggaea1ec94140fa450b8493540c1ec2511aa15f4c91e1aafa7f504aa7b3d3d483399)、[BT_CTS_DST_OFFSET_DAYLIGHT_TIME](#ggaea1ec94140fa450b8493540c1ec2511aad06c4f3f138df8ed4ce74e37da8ab522)、[BT_CTS_DST_OFFSET_DOUBLE_DAYLIGHT_TIME](#ggaea1ec94140fa450b8493540c1ec2511aa904121f94516e39ce44b8f8031ad14fe)、[BT_CTS_DST_OFFSET_UNKNOWN](#ggaea1ec94140fa450b8493540c1ec2511aa9050e0cb7ecf9ab006a44646b1c16eb2)。

规范定义的夏令时偏移量（Daylight Saving Time，DST Offsets）。

<a id="r_gacc2bf34a4dcd8faf7956b0ff246e4cf7"></a>

```c
enum bt_cts_update_reason { BT_CTS_UPDATE_REASON_UNKNOWN = 0 , BT_CTS_UPDATE_REASON_MANUAL = BIT(0) , BT_CTS_UPDATE_REASON_EXTERNAL_REF = BIT(1) , BT_CTS_UPDATE_REASON_TIME_ZONE_CHANGE = BIT(2) , BT_CTS_UPDATE_REASON_DAYLIGHT_SAVING = BIT(3) }
```

相关声明：[bt_cts_update_reason](#gacc2bf34a4dcd8faf7956b0ff246e4cf7)、[BT_CTS_UPDATE_REASON_UNKNOWN](#ggacc2bf34a4dcd8faf7956b0ff246e4cf7ab196da4c0761eacbc80db5cd59482309)、[BT_CTS_UPDATE_REASON_MANUAL](#ggacc2bf34a4dcd8faf7956b0ff246e4cf7af8282fe3f18a5555c1ffa767384a9f83)、[BT_CTS_UPDATE_REASON_EXTERNAL_REF](#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a56967059590b25812f7ae098bb21653a)、[BT_CTS_UPDATE_REASON_TIME_ZONE_CHANGE](#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a2e842670bcdf69184948d33fc3418d9f)、[BT_CTS_UPDATE_REASON_DAYLIGHT_SAVING](#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a82443c4229393642ac9f9aae165f0b0c)。

规范定义的 CTS 时间更新原因位（Time Update Reason Bits）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_ga26e1e7bb9fcd4d723cdc3458743da5a0"></a>

```c
int bt_cts_init (const struct bt_cts_cb *cb)
```

相关声明：[bt_cts_init](#ga26e1e7bb9fcd4d723cdc3458743da5a0)、[bt_cts_cb](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md)。

应在应用初始化（Application Init）时调用此 API。

<a id="r_ga0a1eac245cf4b9d0dd07cfe45f133513"></a>

```c
int bt_cts_send_notification (enum bt_cts_update_reason reason)
```

相关声明：[bt_cts_send_notification](#ga0a1eac245cf4b9d0dd07cfe45f133513)、[bt_cts_update_reason](#gacc2bf34a4dcd8faf7956b0ff246e4cf7)。

通知所有已连接且启用了 CTS 的客户端（Clients）。

<a id="r_ga07893fdc07e448608cde663f3a54d587"></a>

```c
int bt_cts_time_to_unix_ms (const struct bt_cts_time_format *ct_time, int64_t *unix_ms)
```

相关声明：[bt_cts_time_to_unix_ms](#ga07893fdc07e448608cde663f3a54d587)、[bt_cts_time_format](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

将 CTS 格式时间转换为自纪元（Epoch）以来的毫秒数。

<a id="r_ga90e1e2859695731b0213fe3dda4c5e52"></a>

```c
int bt_cts_time_from_unix_ms (struct bt_cts_time_format *ct_time, int64_t unix_ms)
```

相关声明：[bt_cts_time_from_unix_ms](#ga90e1e2859695731b0213fe3dda4c5e52)、[bt_cts_time_format](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

将自纪元（Epoch）以来的毫秒数转换为 CTS 格式时间。

<a id="r_ga1c53d9611299fed8b6fd3fd1fe512689"></a>

```c
int bt_cts_local_time_to_ms (const struct bt_cts_local_time *local_time, int32_t *relative_ms)
```

相关声明：[bt_cts_local_time_to_ms](#ga1c53d9611299fed8b6fd3fd1fe512689)、[bt_cts_local_time](../bluetooth_service_model_reference/P064_bt_cts_local_time_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

将 CTS 本地时间（Local Time）转换为毫秒。

## 2.5\_详细说明（Detailed Documentation）

<a id="ga7c8b0c61c584e34e270d6bc4ec1b3734"></a>

### `BT_CTS_ATT_ERR_VALUES_IGNORED`

```c
#define BT_CTS_ATT_ERR_VALUES_IGNORED 0x80U
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

当前时间服务（CTS）写入操作中因忽略值而返回的 ATT 错误码。

<a id="ga9edfc5a1b76923d87c97145ec934bc63"></a>

### `BT_CTS_DST_INCREMENT_MIN`

```c
#define BT_CTS_DST_INCREMENT_MIN 15U
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

夏令时偏移增量（DST Offset Increment），单位为分钟。

<a id="ga5881ae83724a7934105e808e95a8e880"></a>

### `BT_CTS_FRACTION_256_MAX_VALUE`

```c
#define BT_CTS_FRACTION_256_MAX_VALUE 255U
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

CTS 时间格式中以 1/256 秒为单位的小数秒字段（Fractions Field）的最大值。

<a id="ga38e3b4fec488ba4bcfcff097c752c32f"></a>

### `BT_CTS_TIMEZONE_DEFAULT_VALUE`

```c
#define BT_CTS_TIMEZONE_DEFAULT_VALUE -128
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

表示时区未知的默认时区偏移值（Timezone Offset Value），按 15 分钟递增。

<a id="ga8899d79ef736989a3ae4137430492ad6"></a>

### `BT_CTS_TIMEZONE_INCREMENT_MIN`

```c
#define BT_CTS_TIMEZONE_INCREMENT_MIN 15U
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

时区偏移增量（Timezone Offset Increment），单位为分钟。

<a id="ga204f8d7595bd169f4e547e66b8ca36b4"></a>

### `BT_CTS_TIMEZONE_MAX`

```c
#define BT_CTS_TIMEZONE_MAX 56
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

最大有效时区偏移（Timezone Offset），以 15 分钟为单位；`56` 表示 UTC+14:00。

<a id="ga07b7421ed77c307503e154c5823ab32d"></a>

### `BT_CTS_TIMEZONE_MIN`

```c
#define BT_CTS_TIMEZONE_MIN -48
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

最小有效时区偏移（Timezone Offset），以 15 分钟为单位；`-48` 表示 UTC−12:00。

<a id="gaea1ec94140fa450b8493540c1ec2511a"></a>

### `bt_cts_dst_offset`

```c
enum bt_cts_dst_offset
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

规范定义的夏令时偏移量（Daylight Saving Time，DST Offsets）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CTS_DST_OFFSET_STANDARD_TIME` | 标准时间（Standard Time）。 |
| `BT_CTS_DST_OFFSET_HALF_HOUR_DAYLIGHT_TIME` | 半小时夏令时（Half-hour Daylight Saving Time）。 |
| `BT_CTS_DST_OFFSET_DAYLIGHT_TIME` | 一小时夏令时（One-hour Daylight Saving Time）。 |
| `BT_CTS_DST_OFFSET_DOUBLE_DAYLIGHT_TIME` | 两小时夏令时（Two-hour Daylight Saving Time）。 |
| `BT_CTS_DST_OFFSET_UNKNOWN` | 偏移量未知（Offset Unknown）。 |

<a id="gacc2bf34a4dcd8faf7956b0ff246e4cf7"></a>

### `bt_cts_update_reason`

```c
enum bt_cts_update_reason
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

规范定义的 CTS 时间更新原因位（Time Update Reason Bits）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_CTS_UPDATE_REASON_UNKNOWN` |  |
| `BT_CTS_UPDATE_REASON_MANUAL` |  |
| `BT_CTS_UPDATE_REASON_EXTERNAL_REF` |  |
| `BT_CTS_UPDATE_REASON_TIME_ZONE_CHANGE` |  |
| `BT_CTS_UPDATE_REASON_DAYLIGHT_SAVING` |  |

<a id="ga26e1e7bb9fcd4d723cdc3458743da5a0"></a>

### `bt_cts_init()`

```c
int bt_cts_init ( const struct bt_cts_cb * cb)
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

应在应用初始化（Application Init）时调用此 API。

在 `bt_enable` API 之前或之后调用本 API 都是安全的。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向所需回调（Callback）的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga1c53d9611299fed8b6fd3fd1fe512689"></a>

### `bt_cts_local_time_to_ms()`

```c
int bt_cts_local_time_to_ms ( const struct bt_cts_local_time * local_time, int32_t * relative_ms )
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

将 CTS 本地时间（Local Time）转换为毫秒。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] local_time` | 指向本地时间信息（Local Time Information）的指针，包含时区和夏令时（DST）偏移量。 |
| `[out] relative_ms` | 指向保存结果值的变量的指针，单位为毫秒（Milliseconds）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga0a1eac245cf4b9d0dd07cfe45f133513"></a>

### `bt_cts_send_notification()`

```c
int bt_cts_send_notification ( enum bt_cts_update_reason reason)
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

通知所有已连接且启用了 CTS 的客户端（Clients）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reason` | 要发送给客户端的更新原因（Update Reason）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga90e1e2859695731b0213fe3dda4c5e52"></a>

### `bt_cts_time_from_unix_ms()`

```c
int bt_cts_time_from_unix_ms ( struct bt_cts_time_format * ct_time, int64_t unix_ms )
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

将自纪元（Epoch）以来的毫秒数转换为 CTS 格式时间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] ct_time` | 用于存储 CTS 格式时间（Formatted Time）的指针。 |
| `[in] unix_ms` | 要转换的自纪元（Epoch）以来的毫秒数。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga07893fdc07e448608cde663f3a54d587"></a>

### `bt_cts_time_to_unix_ms()`

```c
int bt_cts_time_to_unix_ms ( const struct bt_cts_time_format * ct_time, int64_t * unix_ms )
```

```c
#include <zephyr/bluetooth/services/cts.h>
```

将 CTS 格式时间转换为自纪元（Epoch）以来的毫秒数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ct_time` | CTS 格式时间（Formatted Time）。 |
| `[out] unix_ms` | 用于存储解析得到的自纪元（Epoch）以来毫秒数的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。


## 2.6\_原页交叉引用（Cross References）

- [bt_cts_time_format](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md)
- [bt_cts_local_time](../bluetooth_service_model_reference/P064_bt_cts_local_time_结构体.md)
- [bt_cts_cb](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [zephyr/bluetooth/services/cts.h](../api_file_storage_event_reference/P004_zephyr__bluetooth__services__cts.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaea1ec94140fa450b8493540c1ec2511aa5930b4efad215cbbc9b4ee228b0fa6e7"></a>
<a id="ggaea1ec94140fa450b8493540c1ec2511aa15f4c91e1aafa7f504aa7b3d3d483399"></a>
<a id="ggaea1ec94140fa450b8493540c1ec2511aad06c4f3f138df8ed4ce74e37da8ab522"></a>
<a id="ggaea1ec94140fa450b8493540c1ec2511aa904121f94516e39ce44b8f8031ad14fe"></a>
<a id="ggaea1ec94140fa450b8493540c1ec2511aa9050e0cb7ecf9ab006a44646b1c16eb2"></a>
<a id="ggacc2bf34a4dcd8faf7956b0ff246e4cf7ab196da4c0761eacbc80db5cd59482309"></a>
<a id="ggacc2bf34a4dcd8faf7956b0ff246e4cf7af8282fe3f18a5555c1ffa767384a9f83"></a>
<a id="ggacc2bf34a4dcd8faf7956b0ff246e4cf7a56967059590b25812f7ae098bb21653a"></a>
<a id="ggacc2bf34a4dcd8faf7956b0ff246e4cf7a2e842670bcdf69184948d33fc3418d9f"></a>
<a id="ggacc2bf34a4dcd8faf7956b0ff246e4cf7a82443c4229393642ac9f9aae165f0b0c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_AFBR-S50 API主题.md) · [返回大纲](大纲.md) · [下一章](P003_桥接配置客户端模型（Bridge Configuration Client Model）.md)
