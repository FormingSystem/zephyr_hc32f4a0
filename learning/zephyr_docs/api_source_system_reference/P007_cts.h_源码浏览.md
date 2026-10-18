---
id: learning.zephyr-docs.api-source-system-reference.page-7
title: cts.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cts_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_cts.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cts_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cts_8h.html)。

## 7.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00095"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00120"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00128"></a>
<a id="l00128"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="agroup__bt__cts_html_ga07893fdc07e448608cde663f3a54d587"></a>
<a id="agroup__bt__cts_html_ga0a1eac245cf4b9d0dd07cfe45f133513"></a>
<a id="agroup__bt__cts_html_ga1c53d9611299fed8b6fd3fd1fe512689"></a>
<a id="agroup__bt__cts_html_ga26e1e7bb9fcd4d723cdc3458743da5a0"></a>
<a id="agroup__bt__cts_html_ga90e1e2859695731b0213fe3dda4c5e52"></a>
<a id="agroup__bt__cts_html_gacc2bf34a4dcd8faf7956b0ff246e4cf7"></a>
<a id="agroup__bt__cts_html_gaea1ec94140fa450b8493540c1ec2511a"></a>
<a id="agroup__bt__cts_html_ggacc2bf34a4dcd8faf7956b0ff246e4cf7a2e842670bcdf69184948d33fc3418d9f"></a>
<a id="agroup__bt__cts_html_ggacc2bf34a4dcd8faf7956b0ff246e4cf7a56967059590b25812f7ae098bb21653a"></a>
<a id="agroup__bt__cts_html_ggacc2bf34a4dcd8faf7956b0ff246e4cf7a82443c4229393642ac9f9aae165f0b0c"></a>
<a id="agroup__bt__cts_html_ggacc2bf34a4dcd8faf7956b0ff246e4cf7ab196da4c0761eacbc80db5cd59482309"></a>
<a id="agroup__bt__cts_html_ggacc2bf34a4dcd8faf7956b0ff246e4cf7af8282fe3f18a5555c1ffa767384a9f83"></a>
<a id="agroup__bt__cts_html_ggaea1ec94140fa450b8493540c1ec2511aa15f4c91e1aafa7f504aa7b3d3d483399"></a>
<a id="agroup__bt__cts_html_ggaea1ec94140fa450b8493540c1ec2511aa5930b4efad215cbbc9b4ee228b0fa6e7"></a>
<a id="agroup__bt__cts_html_ggaea1ec94140fa450b8493540c1ec2511aa904121f94516e39ce44b8f8031ad14fe"></a>
<a id="agroup__bt__cts_html_ggaea1ec94140fa450b8493540c1ec2511aa9050e0cb7ecf9ab006a44646b1c16eb2"></a>
<a id="agroup__bt__cts_html_ggaea1ec94140fa450b8493540c1ec2511aad06c4f3f138df8ed4ce74e37da8ab522"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructbt__cts__cb_html"></a>
<a id="astructbt__cts__cb_html_a1dd6b251b07537e81c010f654721cbf4"></a>
<a id="astructbt__cts__cb_html_a306e843a06337a12832a5463ce6d1b43"></a>
<a id="astructbt__cts__cb_html_a32da52541c84f0116b5001b4fb07c3a8"></a>
<a id="astructbt__cts__cb_html_accf7eb6620ae0f4b9693d238ecdde5b3"></a>
<a id="astructbt__cts__cb_html_ae4a374f95870bfa21b8c1d87e832fe48"></a>
<a id="astructbt__cts__local__time_html"></a>
<a id="astructbt__cts__local__time_html_abea48dd1a2e6426e19508ec124009c05"></a>
<a id="astructbt__cts__local__time_html_ac567357a4f8e2eebd1a03c2c182281c5"></a>
<a id="astructbt__cts__time__format_html"></a>
<a id="astructbt__cts__time__format_html_a079a1c49698b6e9cb84291acdd1cf687"></a>
<a id="astructbt__cts__time__format_html_a299d6432d9b44b0de0be9c130733eb69"></a>
<a id="astructbt__cts__time__format_html_a3482e00650e9e9a63816709c82a1aa07"></a>
<a id="astructbt__cts__time__format_html_a408a2b777d10b536dbdfeca1b8335e6b"></a>
<a id="astructbt__cts__time__format_html_ab592c89e81e5cb43724affd3ce2b5768"></a>
<a id="astructbt__cts__time__format_html_ad5ab55fcb3e1dbaa73ba4ecb78d6b47e"></a>
<a id="astructbt__cts__time__format_html_ae0ccd07b2a280888f3881f0d2fc2add6"></a>
<a id="astructbt__cts__time__format_html_ae696cbbd3a785c1df6d54ce771f1d7a2"></a>
<a id="astructbt__cts__time__format_html_af601779a164440fe95c0dcbd7a3d7e60"></a>

```c
/*
 * Copyright (c) 2024 Croxel Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_CTS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_CTS_H_


#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_CTS_ATT_ERR_VALUES_IGNORED 0x80U

#define BT_CTS_FRACTION_256_MAX_VALUE 255U

#define BT_CTS_TIMEZONE_DEFAULT_VALUE -128

#define BT_CTS_TIMEZONE_INCREMENT_MIN 15U

#define BT_CTS_DST_INCREMENT_MIN 15U

#define BT_CTS_TIMEZONE_MIN -48

#define BT_CTS_TIMEZONE_MAX 56

enum bt_cts_dst_offset {
        BT_CTS_DST_OFFSET_STANDARD_TIME = 0,
        BT_CTS_DST_OFFSET_HALF_HOUR_DAYLIGHT_TIME = 2,
        BT_CTS_DST_OFFSET_DAYLIGHT_TIME = 4,
        BT_CTS_DST_OFFSET_DOUBLE_DAYLIGHT_TIME = 8,
        BT_CTS_DST_OFFSET_UNKNOWN = 255,
};

enum bt_cts_update_reason {
        /* Unknown reason of update no bit is set */
        BT_CTS_UPDATE_REASON_UNKNOWN = 0,
        /* When time is changed manually e.g. through UI */
        BT_CTS_UPDATE_REASON_MANUAL = BIT(0),
        /* If time is changed through external reference */
        BT_CTS_UPDATE_REASON_EXTERNAL_REF = BIT(1),
        /* time changed due to timezone adjust */
        BT_CTS_UPDATE_REASON_TIME_ZONE_CHANGE = BIT(2),
        /* time changed due to dst offset change */
        BT_CTS_UPDATE_REASON_DAYLIGHT_SAVING = BIT(3),
};

struct bt_cts_time_format {
        uint16_t year;
        uint8_t mon;
        uint8_t mday;
        uint8_t hours;
        uint8_t min;
        uint8_t sec;
        uint8_t wday;
        uint8_t fractions256;
        uint8_t reason;
} __packed;

struct bt_cts_local_time {
        int8_t timezone_offset;
        enum bt_cts_dst_offset dst_offset;
};

struct bt_cts_cb {
        void (*notification_changed)(bool enabled);

        int (*cts_time_write)(struct bt_cts_time_format *cts_time);

        int (*fill_current_cts_time)(struct bt_cts_time_format *cts_time);

        int (*cts_local_time_write)(const struct bt_cts_local_time *cts_local_time);

        int (*fill_current_cts_local_time)(struct bt_cts_local_time *local_time);
};

int bt_cts_init(const struct bt_cts_cb *cb);

int bt_cts_send_notification(enum bt_cts_update_reason reason);

int bt_cts_time_to_unix_ms(const struct bt_cts_time_format *ct_time, int64_t *unix_ms);

int bt_cts_time_from_unix_ms(struct bt_cts_time_format *ct_time, int64_t unix_ms);

int bt_cts_local_time_to_ms(const struct bt_cts_local_time *local_time, int32_t *relative_ms);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_CTS_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Croxel Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 79 行

更新原因未知（Unknown Reason of Update），不设置任何位。

### 注释 3：原第 81 行

手动更改时间（Time）时，例如通过用户界面（UI）更改。

### 注释 4：原第 83 行

通过外部参考（External Reference）更改时间时。

### 注释 5：原第 85 行

因时区调整（Timezone Adjustment）而更改时间。

### 注释 6：原第 87 行

因夏令时偏移（DST Offset）变化而更改时间。

### 注释 7：原第 244 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_CTS_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cts_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [bt_cts_dst_offset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#gaea1ec94140fa450b8493540c1ec2511a)
- [BT_CTS_DST_OFFSET_STANDARD_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ggaea1ec94140fa450b8493540c1ec2511aa5930b4efad215cbbc9b4ee228b0fa6e7)
- [BT_CTS_DST_OFFSET_HALF_HOUR_DAYLIGHT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ggaea1ec94140fa450b8493540c1ec2511aa15f4c91e1aafa7f504aa7b3d3d483399)
- [BT_CTS_DST_OFFSET_DAYLIGHT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ggaea1ec94140fa450b8493540c1ec2511aad06c4f3f138df8ed4ce74e37da8ab522)
- [BT_CTS_DST_OFFSET_DOUBLE_DAYLIGHT_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ggaea1ec94140fa450b8493540c1ec2511aa904121f94516e39ce44b8f8031ad14fe)
- [BT_CTS_DST_OFFSET_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ggaea1ec94140fa450b8493540c1ec2511aa9050e0cb7ecf9ab006a44646b1c16eb2)
- [bt_cts_update_reason](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#gacc2bf34a4dcd8faf7956b0ff246e4cf7)
- [BT_CTS_UPDATE_REASON_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ggacc2bf34a4dcd8faf7956b0ff246e4cf7ab196da4c0761eacbc80db5cd59482309)
- [BT_CTS_UPDATE_REASON_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ggacc2bf34a4dcd8faf7956b0ff246e4cf7af8282fe3f18a5555c1ffa767384a9f83)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_CTS_UPDATE_REASON_EXTERNAL_REF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a56967059590b25812f7ae098bb21653a)
- [BT_CTS_UPDATE_REASON_TIME_ZONE_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a2e842670bcdf69184948d33fc3418d9f)
- [BT_CTS_UPDATE_REASON_DAYLIGHT_SAVING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a82443c4229393642ac9f9aae165f0b0c)
- [bt_cts_time_format](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [year](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#ad5ab55fcb3e1dbaa73ba4ecb78d6b47e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mon](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#a079a1c49698b6e9cb84291acdd1cf687)
- [mday](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#a408a2b777d10b536dbdfeca1b8335e6b)
- [hours](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#ab592c89e81e5cb43724affd3ce2b5768)
- [min](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#a299d6432d9b44b0de0be9c130733eb69)
- [sec](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#ae0ccd07b2a280888f3881f0d2fc2add6)
- [wday](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#ae696cbbd3a785c1df6d54ce771f1d7a2)
- [fractions256](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#af601779a164440fe95c0dcbd7a3d7e60)
- [reason](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#a3482e00650e9e9a63816709c82a1aa07)
- [bt_cts_local_time](../bluetooth_service_model_reference/P064_bt_cts_local_time_结构体.md)
- [int8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#accbd6432732c88ad6adc5365800433b6)
- [timezone_offset](../bluetooth_service_model_reference/P064_bt_cts_local_time_结构体.md#abea48dd1a2e6426e19508ec124009c05)
- [dst_offset](../bluetooth_service_model_reference/P064_bt_cts_local_time_结构体.md#ac567357a4f8e2eebd1a03c2c182281c5)
- [bt_cts_cb](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md)
- [notification_changed](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md#accf7eb6620ae0f4b9693d238ecdde5b3)
- [cts_time_write](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md#a1dd6b251b07537e81c010f654721cbf4)
- [fill_current_cts_time](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md#ae4a374f95870bfa21b8c1d87e832fe48)
- [cts_local_time_write](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md#a32da52541c84f0116b5001b4fb07c3a8)
- [fill_current_cts_local_time](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md#a306e843a06337a12832a5463ce6d1b43)
- [bt_cts_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ga26e1e7bb9fcd4d723cdc3458743da5a0)
- [bt_cts_send_notification](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ga0a1eac245cf4b9d0dd07cfe45f133513)
- [bt_cts_time_to_unix_ms](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ga07893fdc07e448608cde663f3a54d587)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [bt_cts_time_from_unix_ms](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ga90e1e2859695731b0213fe3dda4c5e52)
- [bt_cts_local_time_to_ms](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html#ga1c53d9611299fed8b6fd3fd1fe512689)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [bt_cts_cb::cts_time_write](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md#a1dd6b251b07537e81c010f654721cbf4)
- [bt_cts_cb::fill_current_cts_local_time](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md#a306e843a06337a12832a5463ce6d1b43)
- [bt_cts_cb::cts_local_time_write](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md#a32da52541c84f0116b5001b4fb07c3a8)
- [bt_cts_cb::notification_changed](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md#accf7eb6620ae0f4b9693d238ecdde5b3)
- [bt_cts_cb::fill_current_cts_time](../bluetooth_service_model_reference/P063_bt_cts_cb_结构体.md#ae4a374f95870bfa21b8c1d87e832fe48)
- [bt_cts_local_time::timezone_offset](../bluetooth_service_model_reference/P064_bt_cts_local_time_结构体.md#abea48dd1a2e6426e19508ec124009c05)
- [bt_cts_local_time::dst_offset](../bluetooth_service_model_reference/P064_bt_cts_local_time_结构体.md#ac567357a4f8e2eebd1a03c2c182281c5)
- [bt_cts_time_format::mon](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#a079a1c49698b6e9cb84291acdd1cf687)
- [bt_cts_time_format::min](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#a299d6432d9b44b0de0be9c130733eb69)
- [bt_cts_time_format::reason](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#a3482e00650e9e9a63816709c82a1aa07)
- [bt_cts_time_format::mday](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#a408a2b777d10b536dbdfeca1b8335e6b)
- [bt_cts_time_format::hours](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#ab592c89e81e5cb43724affd3ce2b5768)
- [bt_cts_time_format::year](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#ad5ab55fcb3e1dbaa73ba4ecb78d6b47e)
- [bt_cts_time_format::sec](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#ae0ccd07b2a280888f3881f0d2fc2add6)
- [bt_cts_time_format::wday](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#ae696cbbd3a785c1df6d54ce771f1d7a2)
- [bt_cts_time_format::fractions256](../bluetooth_service_model_reference/P065_bt_cts_time_format_结构体.md#af601779a164440fe95c0dcbd7a3d7e60)

---

[上一章](P006_coap_client.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_digilent-pmod.h_源码浏览.md)
