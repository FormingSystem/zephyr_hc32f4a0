---
id: learning.zephyr-docs.api-source-reference.page-813
title: st87mxx_app_services.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/st87mxx__app__services_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第813章\_st87mxx\_app\_services.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/st87mxx__app__services_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/st87mxx__app__services_8h.html)。

## 813.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00047"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00089"></a>
<a id="l00098"></a>
<a id="l00102"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00149"></a>
<a id="l00153"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="agroup__st87mxx__interface_html_ga2227c0f901ef6acc105f7a823f014958"></a>
<a id="agroup__st87mxx__interface_html_ga36695a0b14a8ac128692a3a543a2e1b1"></a>
<a id="agroup__st87mxx__interface_html_ga462eeda7a3702664f9c8d80a7d780c64"></a>
<a id="agroup__st87mxx__interface_html_ga48d42b0ba645e8caa53b49e4842c1276"></a>
<a id="agroup__st87mxx__interface_html_ga64d19b3167aae5fd3b4a372222534e23"></a>
<a id="agroup__st87mxx__interface_html_ga6c28c45f3910a0e33a8026fc87133247"></a>
<a id="agroup__st87mxx__interface_html_ga92a4c4d49be58a5d8c3db059116cd38e"></a>
<a id="agroup__st87mxx__interface_html_gae459a9137139217ee997b7e48fcc30f6"></a>
<a id="agroup__st87mxx__interface_html_gaea2db4c02a45f514f14c2f2913a36915"></a>
<a id="agroup__st87mxx__interface_html_gaf711155377231afc1ad969cb397818cd"></a>
<a id="agroup__st87mxx__interface_html_gafefe0b51707586c520dd966c4a271fa1"></a>
<a id="agroup__st87mxx__interface_html_gga6c28c45f3910a0e33a8026fc87133247a39c735505f4fa4307deb793b94bd9afd"></a>
<a id="agroup__st87mxx__interface_html_gga6c28c45f3910a0e33a8026fc87133247a3c18e0c0869544db9a5560cc9e9a7bcd"></a>
<a id="agroup__st87mxx__interface_html_gga6c28c45f3910a0e33a8026fc87133247a64e359521503413db7129baff95a5a7d"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructst87mxx__wifiscan__params_html"></a>
<a id="astructst87mxx__wifiscan__params_html_a0164e513719020494343e3dd0c36dd44"></a>
<a id="astructst87mxx__wifiscan__params_html_a12e93569611996ca3e14906f1cc2103c"></a>
<a id="astructst87mxx__wifiscan__params_html_a19622385234cf2d09ef29c4b478e9d3d"></a>
<a id="astructst87mxx__wifiscan__params_html_a8f3c22343e1cbdc1f35f98456e0d98fb"></a>

```c
/*
 * Copyright (c) 2026 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef STM87MXX_APP_SRV_H
#define STM87MXX_APP_SRV_H



#define APP_MDM_CMD_TIMEOUT                     K_SECONDS(180)



#define GNSS_NB_MAX_POSITION                    100
#define GNSS_CONSTELLATION_ID                   0
#define GNSS_FORMAT_TYPE                        0

#define GNSS_FORMAT_ST_POSITION                 1
#define GNSS_FORMAT_ST_ACCURACY                 0
#define GNSS_FORMAT_ST_SATELLITES               0
#define GNSS_FORMAT_ST_ORIENTATION              0

#define GNSS_NMEA_GPGGA                         1
#define GNSS_NMEA_GPGSA                         0
#define GNSS_NMEA_GPGSV                         0
#define GNSS_NMEA_GPGLL                         1
#define GNSS_NMEA_GPRMC                         0
#define GNSS_NMEA_GPVTG                         1



#define URC_MODE                1
#define HOPPING_TIME    1024
#define ANT_SEL                 1



typedef enum {
        SEQUENCE_NONE           = 0,
        SEQUENCE_ONGOING        = 1,
        SEQUENCE_TIMED_OUT      = 2
} sequence_state;

typedef void (st87mxx_get_beacon_data_callback_t) (char const * const string);

typedef struct {
        char *channel_list;
        uint32_t nb_scan_iterations;
        st87mxx_get_beacon_data_callback_t *get_beacon_data_callback_func;
        uint32_t timeout;
} st87mxx_wifiscan_params;


void st87mxx_app_services_init(void);

typedef void (st87mxx_get_pos_callback_t) (char const *const string);

int st87mxx_gnss_getfix(uint32_t nb_position,
        st87mxx_get_pos_callback_t *get_pos_callback_func, uint32_t timeout);

void st87mxx_gnss_stop(void);

int st87mxx_wifiscan(st87mxx_wifiscan_params *wscan_params);

void st87mxx_wifiscan_stop(void);

typedef void (st87mxx_get_rssi_callback_t) (char const *const string);

int st87mxx_getrssi(st87mxx_get_rssi_callback_t *get_rssi_callback_func);

sequence_state st87mxx_app_services_getstate(void);


#endif /* STM87MXX_APP_SRV_H */
```

## 813.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 255 行

头文件保护宏（Header guard）标记：`STM87MXX_APP_SRV_H`。

## 813.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/st87mxx__app__services_8h.html)
- [SEQUENCE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gga6c28c45f3910a0e33a8026fc87133247a64e359521503413db7129baff95a5a7d)
- [SEQUENCE_ONGOING](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gga6c28c45f3910a0e33a8026fc87133247a39c735505f4fa4307deb793b94bd9afd)
- [SEQUENCE_TIMED_OUT](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gga6c28c45f3910a0e33a8026fc87133247a3c18e0c0869544db9a5560cc9e9a7bcd)
- [sequence_state](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga6c28c45f3910a0e33a8026fc87133247)
- [st87mxx_get_beacon_data_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga36695a0b14a8ac128692a3a543a2e1b1)
- [channel_list](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md#a0164e513719020494343e3dd0c36dd44)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [nb_scan_iterations](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md#a8f3c22343e1cbdc1f35f98456e0d98fb)
- [get_beacon_data_callback_func](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md#a19622385234cf2d09ef29c4b478e9d3d)
- [timeout](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md#a12e93569611996ca3e14906f1cc2103c)
- [st87mxx_wifiscan_params](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md)
- [st87mxx_app_services_init](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga2227c0f901ef6acc105f7a823f014958)
- [st87mxx_get_pos_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga92a4c4d49be58a5d8c3db059116cd38e)
- [st87mxx_gnss_getfix](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gaf711155377231afc1ad969cb397818cd)
- [st87mxx_gnss_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gaea2db4c02a45f514f14c2f2913a36915)
- [st87mxx_wifiscan](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga48d42b0ba645e8caa53b49e4842c1276)
- [st87mxx_wifiscan_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga462eeda7a3702664f9c8d80a7d780c64)
- [st87mxx_get_rssi_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#ga64d19b3167aae5fd3b4a372222534e23)
- [st87mxx_getrssi](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gae459a9137139217ee997b7e48fcc30f6)
- [st87mxx_app_services_getstate](https://docs.zephyrproject.org/latest/doxygen/html/group__st87mxx__interface.html#gafefe0b51707586c520dd966c4a271fa1)
- [st87mxx_wifiscan_params::channel_list](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md#a0164e513719020494343e3dd0c36dd44)
- [st87mxx_wifiscan_params::timeout](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md#a12e93569611996ca3e14906f1cc2103c)
- [st87mxx_wifiscan_params::get_beacon_data_callback_func](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md#a19622385234cf2d09ef29c4b478e9d3d)
- [st87mxx_wifiscan_params::nb_scan_iterations](../modem_wireless_model_reference/P071_st87mxx_wifiscan_params_结构体.md#a8f3c22343e1cbdc1f35f98456e0d98fb)

---

[上一章](P812_st-morpho-header.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P814_stack.h_源码浏览.md)
