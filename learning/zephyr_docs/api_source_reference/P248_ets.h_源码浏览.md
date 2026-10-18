---
id: learning.zephyr-docs.api-source-reference.page-248
title: ets.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ets_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第248章\_ets.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ets_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ets_8h.html)。

## 248.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="foldopen00176"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="foldopen00183"></a>
<a id="l00183"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="agroup__bt__ets_html_ga23455566e363b7b54b4d71b56e982322"></a>
<a id="agroup__bt__ets_html_ga37a169057efc9b463ad531fd1f131fff"></a>
<a id="agroup__bt__ets_html_ga4f3d175e71ef213ae5d16b2b853f9481"></a>
<a id="agroup__bt__ets_html_ga59747d0fe1a33f5c84040d90dbbf6f6d"></a>
<a id="agroup__bt__ets_html_ga8cd79739c350f266b134a26b0b0ec7fc"></a>
<a id="agroup__bt__ets_html_gae1a76312c1c6bc31443860dd10ab0a54"></a>
<a id="agroup__bt__ets_html_gga23455566e363b7b54b4d71b56e982322a5a83f42c780a6c87682f6c0406d64316"></a>
<a id="agroup__bt__ets_html_gga23455566e363b7b54b4d71b56e982322a882686a57199a753b2e40cc5abc9f298"></a>
<a id="agroup__bt__ets_html_gga23455566e363b7b54b4d71b56e982322aad9a457744816e678c27d1366bf04f9e"></a>
<a id="agroup__bt__ets_html_gga23455566e363b7b54b4d71b56e982322af31989dd56bfdaf185ffe2dbdcab34cb"></a>
<a id="agroup__bt__ets_html_gga37a169057efc9b463ad531fd1f131fffa06532377ea56330ecdcfdc0b25dd594f"></a>
<a id="agroup__bt__ets_html_gga37a169057efc9b463ad531fd1f131fffa9dc1f1f12a97cb23ec4051138f559817"></a>
<a id="agroup__bt__ets_html_gga37a169057efc9b463ad531fd1f131fffab3deb6e75d374b4766acdbac0e87e54e"></a>
<a id="agroup__bt__ets_html_gga37a169057efc9b463ad531fd1f131fffadac86ed9c0c2424fee546a78e143eced"></a>
<a id="alib_2libc_2minimal_2include_2time_8h_html_a99ef1cb2c789827dd5db3886dccf9067"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructbt__ets__cb_html"></a>
<a id="astructbt__ets__cb_html_a02ffefc1a0092104a56e0f8b2be70c86"></a>
<a id="astructbt__ets__cb_html_a38d749d841a076ec3ff8277a78331a8b"></a>
<a id="astructbt__ets__cb_html_a48c36b23cec3f07a5e63d07ca083e276"></a>
<a id="astructbt__ets__cb_html_a82c2a9f55d6d31d1ce87df01e84b6d5f"></a>
<a id="astructbt__ets__elapsed__time_html"></a>
<a id="astructbt__ets__elapsed__time_html_a026b22dc6d130c32ab80357bcb51f83f"></a>
<a id="astructbt__ets__elapsed__time_html_a0e5ba7c5d8aafff23a01f7b0d5f4c075"></a>
<a id="astructbt__ets__elapsed__time_html_a60181194e382ea490ddcc1118bc463f7"></a>
<a id="astructbt__ets__elapsed__time_html_af2ec700659c1db49ae66f8ed31f20c90"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Dipak Shetty
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_ETS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_ETS_H_


#include <stdint.h>
#include <stdbool.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_ets_elapsed_time {
        uint8_t flags;
        uint8_t time_value[6];
        uint8_t time_sync_src;
        int8_t tz_dst_offset;
} __packed;


#define BT_ETS_FLAG_TICK_COUNTER BIT(0)

#define BT_ETS_FLAG_UTC BIT(1)

#define BT_ETS_FLAG_RESOLUTION_MASK (BIT(2) | BIT(3))

#define BT_ETS_FLAG_TZ_DST_USED BIT(4)

#define BT_ETS_FLAG_CURRENT_TIMELINE BIT(5)

#define BT_ETS_FLAG_RESERVED_MASK (BIT(6) | BIT(7))


enum bt_ets_time_resolution {
        BT_ETS_RESOLUTION_1_SEC = 0,
        BT_ETS_RESOLUTION_100_MS = 1,
        BT_ETS_RESOLUTION_1_MS = 2,
        BT_ETS_RESOLUTION_100_US = 3,
};


#define BT_ETS_TIME_SOURCE_UNKNOWN          0
#define BT_ETS_TIME_SOURCE_NTP              1
#define BT_ETS_TIME_SOURCE_GPS              2
#define BT_ETS_TIME_SOURCE_RADIO            3
#define BT_ETS_TIME_SOURCE_MANUAL           4
#define BT_ETS_TIME_SOURCE_ATOMIC           5
#define BT_ETS_TIME_SOURCE_CELLULAR         6
#define BT_ETS_TIME_SOURCE_NOT_SYNCHRONIZED 7


enum bt_ets_write_result {
        BT_ETS_WRITE_SUCCESS = 0,
        BT_ETS_WRITE_TIME_SOURCE_TOO_LOW = 1,
        BT_ETS_WRITE_OUT_OF_RANGE = 2,
        BT_ETS_WRITE_INCORRECT_FORMAT = 3,
};

#define BT_ETS_SUPPORTED_FLAGS_MASK                                                                \
        ((IS_ENABLED(CONFIG_BT_ETS_SUPPORT_TICK_COUNTER) ? BT_ETS_FLAG_TICK_COUNTER : 0) |         \
         (IS_ENABLED(CONFIG_BT_ETS_SUPPORT_UTC) ? BT_ETS_FLAG_UTC : 0) |                           \
         (IS_ENABLED(CONFIG_BT_ETS_SUPPORT_TZ_DST) ? BT_ETS_FLAG_TZ_DST_USED : 0) |                \
         (IS_ENABLED(CONFIG_BT_ETS_RESOLUTION_1_SEC)    ? 0                                        \
          : IS_ENABLED(CONFIG_BT_ETS_RESOLUTION_100_MS) ? BIT(2)                                   \
          : IS_ENABLED(CONFIG_BT_ETS_RESOLUTION_1_MS)   ? BIT(3)                                   \
          : IS_ENABLED(CONFIG_BT_ETS_RESOLUTION_100_US) ? (BIT(2) | BIT(3))                        \
                                                        : 0) |                                     \
         BT_ETS_FLAG_CURRENT_TIMELINE)


#define BT_ETS_CLOCK_STATUS_NEEDS_SET BIT(0)
#define BT_ETS_CLOCK_STATUS_RFU_MASK  0xFE



#define BT_ETS_CLOCK_CAP_DST_AUTO BIT(0)
#define BT_ETS_CLOCK_CAP_TZ_AUTO  BIT(1)
#define BT_ETS_CLOCK_CAP_RFU_MASK 0xFC


#define BT_ETS_CLOCK_CAPABILITIES_VALUE                                                            \
        ((IS_ENABLED(CONFIG_BT_ETS_CLOCK_CAP_DST_AUTO) ? BT_ETS_CLOCK_CAP_DST_AUTO : 0) |          \
         (IS_ENABLED(CONFIG_BT_ETS_CLOCK_CAP_TZ_AUTO) ? BT_ETS_CLOCK_CAP_TZ_AUTO : 0))

struct bt_ets_cb {
        int (*read_elapsed_time)(struct bt_ets_elapsed_time *time);

        int (*read_clock_status)(uint8_t *status);

        enum bt_ets_write_result (*write_elapsed_time)(const struct bt_ets_elapsed_time *time);

        void (*indication_changed)(bool enabled);
};

int bt_ets_init(const struct bt_ets_cb *cb);

int bt_ets_indicate(const struct bt_ets_elapsed_time *elapsed_time, uint8_t clock_status);

int bt_ets_time_to_unix_ms(const struct bt_ets_elapsed_time *et_time, int64_t *unix_ms);

int bt_ets_time_from_unix_ms(struct bt_ets_elapsed_time *et_time, int64_t unix_ms, uint8_t time_src,
                             int8_t tz_dst_offset);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_ETS_H_ */
```

## 248.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Dipak Shetty。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 338 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_SERVICES_ETS_H_`。

## 248.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ets_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [bt_ets_elapsed_time](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md#a026b22dc6d130c32ab80357bcb51f83f)
- [time_value](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md#a60181194e382ea490ddcc1118bc463f7)
- [time_sync_src](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md#af2ec700659c1db49ae66f8ed31f20c90)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [tz_dst_offset](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md#a0e5ba7c5d8aafff23a01f7b0d5f4c075)
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
- [bt_ets_cb](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md)
- [read_elapsed_time](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md#a82c2a9f55d6d31d1ce87df01e84b6d5f)
- [time](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2time_8h.html#a99ef1cb2c789827dd5db3886dccf9067)
- [read_clock_status](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md#a48c36b23cec3f07a5e63d07ca083e276)
- [write_elapsed_time](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md#a02ffefc1a0092104a56e0f8b2be70c86)
- [indication_changed](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md#a38d749d841a076ec3ff8277a78331a8b)
- [bt_ets_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#gae1a76312c1c6bc31443860dd10ab0a54)
- [bt_ets_indicate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga8cd79739c350f266b134a26b0b0ec7fc)
- [bt_ets_time_to_unix_ms](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga59747d0fe1a33f5c84040d90dbbf6f6d)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [bt_ets_time_from_unix_ms](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html#ga4f3d175e71ef213ae5d16b2b853f9481)
- [bt_ets_cb::write_elapsed_time](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md#a02ffefc1a0092104a56e0f8b2be70c86)
- [bt_ets_cb::indication_changed](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md#a38d749d841a076ec3ff8277a78331a8b)
- [bt_ets_cb::read_clock_status](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md#a48c36b23cec3f07a5e63d07ca083e276)
- [bt_ets_cb::read_elapsed_time](../bluetooth_service_model_reference/P066_bt_ets_cb_结构体.md#a82c2a9f55d6d31d1ce87df01e84b6d5f)
- [bt_ets_elapsed_time::flags](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md#a026b22dc6d130c32ab80357bcb51f83f)
- [bt_ets_elapsed_time::tz_dst_offset](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md#a0e5ba7c5d8aafff23a01f7b0d5f4c075)
- [bt_ets_elapsed_time::time_value](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md#a60181194e382ea490ddcc1118bc463f7)
- [bt_ets_elapsed_time::time_sync_src](../bluetooth_service_model_reference/P067_bt_ets_elapsed_time_结构体.md#af2ec700659c1db49ae66f8ed31f20c90)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P247_ethernet_vlan.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P249_event.h_源码浏览.md)
