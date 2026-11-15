---
id: learning.zephyr-docs.api-source-reference.page-379
title: input_crsf.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第379章\_input\_crsf.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html)。

## 379.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00121"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00158"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="foldopen00180"></a>
<a id="l00180"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="adevice_8h_html"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628faf"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafa2ac02b4732dc0c35ab532f6fa5ea3d2b"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafa46045337ef856c4adeff9a07ee51c487"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafa4d542852dca1c165c09f6a25da5b8f78"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafa5ba4e72f3c5577ccf16712f60f888d91"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafa7c8b088ae306fc912f12043f7bbdb44e"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafa81ce3c65b5af1bd45a798821f557c0a2"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafa913488d37e7df391fb1859eca0e92f41"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafa973d8c9aef67fb0ab535c110a2c783d3"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafa97e0bfc9baa2fa444d72930a89c9ff03"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafacbf77a08de27bef11b9ebb315d15a0c3"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafacd7c511a63096ab430a21adb1d51f968"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafaea2e80f7897ce58cbf3be0a7fd995364"></a>
<a id="ainput__crsf_8h_html_a352177d3a02932443b0d2cc4db628fafafd5ec386a4a46942548aabd76553f8be"></a>
<a id="ainput__crsf_8h_html_a7bb48e231b715587daf4c7a57c0e2b8a"></a>
<a id="ainput__crsf_8h_html_acb8b2de8f49e5037f3ddacaef40f71c2"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructcrsf__link__stats_html"></a>
<a id="astructcrsf__link__stats_html_a03786e5e70c07ea29e45d781374c783e"></a>
<a id="astructcrsf__link__stats_html_a17f459d371712bdc98ff1cb4097078ac"></a>
<a id="astructcrsf__link__stats_html_a511eab5e2715a7801737a872070dc464"></a>
<a id="astructcrsf__link__stats_html_a7b64694ea1180b538de7b20c349053bf"></a>
<a id="astructcrsf__link__stats_html_a94001c4fa56a67453dffaa6b2332714a"></a>
<a id="astructcrsf__link__stats_html_a985cc7785aea619a5c6fc0a01f4a51e9"></a>
<a id="astructcrsf__link__stats_html_a9afe00cdbc866e8ad01583fb3a8c01f5"></a>
<a id="astructcrsf__link__stats_html_ab00ec240186f2e3967f27a878f3189cc"></a>
<a id="astructcrsf__link__stats_html_ac32c03eff5b5722dae1fab83bba82cae"></a>
<a id="astructcrsf__link__stats_html_af30d3bf98388e9b59692e190b32ec34f"></a>
<a id="astructcrsf__payload__attitude_html"></a>
<a id="astructcrsf__payload__attitude_html_a72273cb8a6eed97f5656e0dee23aef14"></a>
<a id="astructcrsf__payload__attitude_html_a7e745fcb15244c9619486d344436a6be"></a>
<a id="astructcrsf__payload__attitude_html_adbc100ab349999d3b34d4934994f3c40"></a>
<a id="astructcrsf__payload__battery_html"></a>
<a id="astructcrsf__payload__battery_html_a09e735b8d23408c8280a7804dbb606ff"></a>
<a id="astructcrsf__payload__battery_html_a23c069f3185633447dc60b3bacd82f5f"></a>
<a id="astructcrsf__payload__battery_html_a245c82fbe1a42795d54589869909ad31"></a>
<a id="astructcrsf__payload__battery_html_a612773b4ce7a0e46213a5a1e2f1b72a0"></a>
<a id="astructcrsf__payload__gps_html"></a>
<a id="astructcrsf__payload__gps_html_a55c48a2ba2206b2031743823dee8f26b"></a>
<a id="astructcrsf__payload__gps_html_a5f150bbfb8bba875bb93bf53be3e46ac"></a>
<a id="astructcrsf__payload__gps_html_a649b54ebbde44a496a2ce5354d7905e9"></a>
<a id="astructcrsf__payload__gps_html_a8c71400a0707f52a36edec98437a7ff8"></a>
<a id="astructcrsf__payload__gps_html_ab716fc23f202bdda1c710640937f6439"></a>
<a id="astructcrsf__payload__gps_html_abd1ed4c7d07b652f9d051a14e8ffbb0e"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2026 CogniPilot Foundation
 * Copyright (c) 2026 NXP Semiconductors
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_INPUT_INPUT_CRSF_H_
#define ZEPHYR_INCLUDE_INPUT_INPUT_CRSF_H_

#include <zephyr/device.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

enum crsf_packet_type {
        CRSF_TYPE_GPS = 0x02,

        CRSF_TYPE_BATTERY = 0x08,

        CRSF_TYPE_LINK_TX_ID = 0x0A,

        CRSF_TYPE_LINK_STATS = 0x14,

        CRSF_TYPE_RC_CHANNELS = 0x16,

        CRSF_TYPE_ATTITUDE = 0x1E,

        CRSF_TYPE_FLIGHT_MODE = 0x21,

        CRSF_TYPE_PING_DEVICES = 0x28,

        CRSF_TYPE_DEVICE_INFO = 0x29,

        CRSF_TYPE_PARAMETER_SETTINGS = 0x2B,

        CRSF_TYPE_COMMAND = 0x32,

        CRSF_TYPE_RADIO_ID = 0x3A,

        CRSF_TYPE_AP_CUSTOM_TELEM = 0x80
};

struct crsf_payload_gps {
        int32_t lat;

        int32_t lon;

        uint16_t speed;

        uint16_t heading;

        uint16_t altitude;

        uint8_t satellites;
} __packed;

struct crsf_payload_battery {
        uint16_t voltage_dV;

        uint16_t current_dA;

        uint8_t capacity_mah[3];

        uint8_t remaining_pct;
} __packed;

struct crsf_link_stats {
        uint8_t uplink_rssi_1;

        uint8_t uplink_rssi_2;

        uint8_t uplink_link_quality;

        int8_t uplink_snr;

        uint8_t active_antenna;

        uint8_t rf_mode;

        uint8_t tx_power;

        uint8_t downlink_rssi;

        uint8_t downlink_link_quality;

        int8_t downlink_snr;
} __packed;


#define CRSF_TICKS_TO_US(x) (((x) - 992) * 5 / 8 + 1500)

#define CRSF_US_TO_TICKS(x) (((x) - 1500) * 8 / 5 + 992)


struct crsf_payload_attitude {
        int16_t pitch_rad;

        int16_t roll_rad;

        int16_t yaw_rad;
} __packed;

int input_crsf_send_telemetry(const struct device *dev, uint8_t type, uint8_t *payload,
                              size_t payload_len);

struct crsf_link_stats input_crsf_get_link_stats(const struct device *dev);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_INPUT_INPUT_CRSF_H_ */
```

## 379.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 CogniPilot Foundation。

版权（Copyright）：© 2026 NXP Semiconductors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 225 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_INPUT_INPUT_CRSF_H_`。

## 379.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [crsf_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628faf)
- [CRSF_TYPE_GPS](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafa4d542852dca1c165c09f6a25da5b8f78)
- [CRSF_TYPE_BATTERY](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafacd7c511a63096ab430a21adb1d51f968)
- [CRSF_TYPE_LINK_TX_ID](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafa46045337ef856c4adeff9a07ee51c487)
- [CRSF_TYPE_LINK_STATS](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafa7c8b088ae306fc912f12043f7bbdb44e)
- [CRSF_TYPE_RC_CHANNELS](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafafd5ec386a4a46942548aabd76553f8be)
- [CRSF_TYPE_ATTITUDE](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafa973d8c9aef67fb0ab535c110a2c783d3)
- [CRSF_TYPE_FLIGHT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafa5ba4e72f3c5577ccf16712f60f888d91)
- [CRSF_TYPE_PING_DEVICES](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafa913488d37e7df391fb1859eca0e92f41)
- [CRSF_TYPE_DEVICE_INFO](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafa2ac02b4732dc0c35ab532f6fa5ea3d2b)
- [CRSF_TYPE_PARAMETER_SETTINGS](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafa97e0bfc9baa2fa444d72930a89c9ff03)
- [CRSF_TYPE_COMMAND](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafacbf77a08de27bef11b9ebb315d15a0c3)
- [CRSF_TYPE_RADIO_ID](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafa81ce3c65b5af1bd45a798821f557c0a2)
- [CRSF_TYPE_AP_CUSTOM_TELEM](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a352177d3a02932443b0d2cc4db628fafaea2e80f7897ce58cbf3be0a7fd995364)
- [crsf_payload_gps](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [lat](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md#a5f150bbfb8bba875bb93bf53be3e46ac)
- [lon](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md#ab716fc23f202bdda1c710640937f6439)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [speed](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md#abd1ed4c7d07b652f9d051a14e8ffbb0e)
- [heading](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md#a649b54ebbde44a496a2ce5354d7905e9)
- [altitude](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md#a55c48a2ba2206b2031743823dee8f26b)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [satellites](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md#a8c71400a0707f52a36edec98437a7ff8)
- [crsf_payload_battery](../sensor_navigation_model_reference/P005_crsf_payload_battery_结构体.md)
- [voltage_dV](../sensor_navigation_model_reference/P005_crsf_payload_battery_结构体.md#a245c82fbe1a42795d54589869909ad31)
- [current_dA](../sensor_navigation_model_reference/P005_crsf_payload_battery_结构体.md#a09e735b8d23408c8280a7804dbb606ff)
- [capacity_mah](../sensor_navigation_model_reference/P005_crsf_payload_battery_结构体.md#a612773b4ce7a0e46213a5a1e2f1b72a0)
- [remaining_pct](../sensor_navigation_model_reference/P005_crsf_payload_battery_结构体.md#a23c069f3185633447dc60b3bacd82f5f)
- [crsf_link_stats](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md)
- [uplink_rssi_1](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a03786e5e70c07ea29e45d781374c783e)
- [uplink_rssi_2](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a9afe00cdbc866e8ad01583fb3a8c01f5)
- [uplink_link_quality](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#ab00ec240186f2e3967f27a878f3189cc)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uplink_snr](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a985cc7785aea619a5c6fc0a01f4a51e9)
- [active_antenna](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#ac32c03eff5b5722dae1fab83bba82cae)
- [rf_mode](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a17f459d371712bdc98ff1cb4097078ac)
- [tx_power](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a94001c4fa56a67453dffaa6b2332714a)
- [downlink_rssi](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a511eab5e2715a7801737a872070dc464)
- [downlink_link_quality](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a7b64694ea1180b538de7b20c349053bf)
- [downlink_snr](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#af30d3bf98388e9b59692e190b32ec34f)
- [crsf_payload_attitude](../sensor_navigation_model_reference/P004_crsf_payload_attitude_结构体.md)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [pitch_rad](../sensor_navigation_model_reference/P004_crsf_payload_attitude_结构体.md#a72273cb8a6eed97f5656e0dee23aef14)
- [roll_rad](../sensor_navigation_model_reference/P004_crsf_payload_attitude_结构体.md#adbc100ab349999d3b34d4934994f3c40)
- [yaw_rad](../sensor_navigation_model_reference/P004_crsf_payload_attitude_结构体.md#a7e745fcb15244c9619486d344436a6be)
- [input_crsf_send_telemetry](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#a7bb48e231b715587daf4c7a57c0e2b8a)
- [device](../device_reference/P002_设备对象结构.md)
- [input_crsf_get_link_stats](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h.html#acb8b2de8f49e5037f3ddacaef40f71c2)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [crsf_link_stats::uplink_rssi_1](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a03786e5e70c07ea29e45d781374c783e)
- [crsf_link_stats::rf_mode](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a17f459d371712bdc98ff1cb4097078ac)
- [crsf_link_stats::downlink_rssi](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a511eab5e2715a7801737a872070dc464)
- [crsf_link_stats::downlink_link_quality](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a7b64694ea1180b538de7b20c349053bf)
- [crsf_link_stats::tx_power](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a94001c4fa56a67453dffaa6b2332714a)
- [crsf_link_stats::uplink_snr](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a985cc7785aea619a5c6fc0a01f4a51e9)
- [crsf_link_stats::uplink_rssi_2](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#a9afe00cdbc866e8ad01583fb3a8c01f5)
- [crsf_link_stats::uplink_link_quality](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#ab00ec240186f2e3967f27a878f3189cc)
- [crsf_link_stats::active_antenna](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#ac32c03eff5b5722dae1fab83bba82cae)
- [crsf_link_stats::downlink_snr](../sensor_navigation_model_reference/P003_crsf_link_stats_结构体.md#af30d3bf98388e9b59692e190b32ec34f)
- [crsf_payload_attitude::pitch_rad](../sensor_navigation_model_reference/P004_crsf_payload_attitude_结构体.md#a72273cb8a6eed97f5656e0dee23aef14)
- [crsf_payload_attitude::yaw_rad](../sensor_navigation_model_reference/P004_crsf_payload_attitude_结构体.md#a7e745fcb15244c9619486d344436a6be)
- [crsf_payload_attitude::roll_rad](../sensor_navigation_model_reference/P004_crsf_payload_attitude_结构体.md#adbc100ab349999d3b34d4934994f3c40)
- [crsf_payload_battery::current_dA](../sensor_navigation_model_reference/P005_crsf_payload_battery_结构体.md#a09e735b8d23408c8280a7804dbb606ff)
- [crsf_payload_battery::remaining_pct](../sensor_navigation_model_reference/P005_crsf_payload_battery_结构体.md#a23c069f3185633447dc60b3bacd82f5f)
- [crsf_payload_battery::voltage_dV](../sensor_navigation_model_reference/P005_crsf_payload_battery_结构体.md#a245c82fbe1a42795d54589869909ad31)
- [crsf_payload_battery::capacity_mah](../sensor_navigation_model_reference/P005_crsf_payload_battery_结构体.md#a612773b4ce7a0e46213a5a1e2f1b72a0)
- [crsf_payload_gps::altitude](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md#a55c48a2ba2206b2031743823dee8f26b)
- [crsf_payload_gps::lat](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md#a5f150bbfb8bba875bb93bf53be3e46ac)
- [crsf_payload_gps::heading](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md#a649b54ebbde44a496a2ce5354d7905e9)
- [crsf_payload_gps::satellites](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md#a8c71400a0707f52a36edec98437a7ff8)
- [crsf_payload_gps::lon](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md#ab716fc23f202bdda1c710640937f6439)
- [crsf_payload_gps::speed](../sensor_navigation_model_reference/P006_crsf_payload_gps_结构体.md#abd1ed4c7d07b652f9d051a14e8ffbb0e)

---

[上一章](P378_input_analog_axis_settings.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P380_input_hid.h_源码浏览.md)
