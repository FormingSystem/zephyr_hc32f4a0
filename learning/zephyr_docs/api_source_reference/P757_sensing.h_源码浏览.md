---
id: learning.zephyr-docs.api-source-reference.page-757
title: sensing.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensing_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第757章\_sensing.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sensing_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sensing_8h.html)。

## 757.1\_原始可见代码（Source Code）

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
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00061"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00071"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="foldopen00105"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="foldopen00167"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00192"></a>
<a id="foldopen00196"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="foldopen00206"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__sensing__api_html_ga4218453664fee0aa61697018e3193e7a"></a>
<a id="agroup__sensing__api_html_ga4399f2e03d4d9444045b705b13cb6dfd"></a>
<a id="agroup__sensing__api_html_ga46591a2d29f5b5e160a72bbe289884ab"></a>
<a id="agroup__sensing__api_html_ga5440a8914b664209d62388183b3c89ea"></a>
<a id="agroup__sensing__api_html_ga69d2ae9f45215742654bfc7e4676e6f2"></a>
<a id="agroup__sensing__api_html_ga8e427d28efc492f15d762af3308d78cd"></a>
<a id="agroup__sensing__api_html_ga98e49ea0e84e93867df20033d01ee66c"></a>
<a id="agroup__sensing__api_html_gabc9657708851e6a744a7cd73319efe06"></a>
<a id="agroup__sensing__api_html_gac959e076fcdc105dfaac1d7a984ba293"></a>
<a id="agroup__sensing__api_html_gaf3b6c66c2db12115f3ebec0cdba32e86"></a>
<a id="agroup__sensing__api_html_gaf4037066c9a7a9f3eb1c79a4d8ae0920"></a>
<a id="agroup__sensing__api_html_gga69d2ae9f45215742654bfc7e4676e6f2a072ff2aa9640503bfd8cbc8f7d271980"></a>
<a id="agroup__sensing__api_html_gga69d2ae9f45215742654bfc7e4676e6f2a2ccb8b476935ce27b2eedbb889e25476"></a>
<a id="agroup__sensing__api_html_gga69d2ae9f45215742654bfc7e4676e6f2a8c9870b1303008b45e2caeb33f5c44a3"></a>
<a id="agroup__sensing__api_html_gga69d2ae9f45215742654bfc7e4676e6f2abc39825a643b9d1452162f057f79774b"></a>
<a id="agroup__sensing__api_html_ggabc9657708851e6a744a7cd73319efe06a735fe339796ea7b4d2387d931382ce93"></a>
<a id="agroup__sensing__api_html_ggabc9657708851e6a744a7cd73319efe06af23a28e861a8fa2d49b18a0fbe62600e"></a>
<a id="asensing__datatypes_8h_html"></a>
<a id="asensing__sensor__types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructdevice_html"></a>
<a id="astructsensing__callback__list_html"></a>
<a id="astructsensing__callback__list_html_a43504dbe7d484f0d0e7d33b8bb6318d4"></a>
<a id="astructsensing__callback__list_html_a7d0d7c878e338f19fd48c66cda9d04fc"></a>
<a id="astructsensing__sensor__config_html"></a>
<a id="astructsensing__sensor__config_html_a7512f7254f6960ed398150db23868965"></a>
<a id="astructsensing__sensor__config_html_a9bdf50a1018d6d9426efd991d05bf72b"></a>
<a id="astructsensing__sensor__config_html_ac4389c439db16cb25a2e622baf0aeb9b"></a>
<a id="astructsensing__sensor__config_html_acc1270dbe02ff6324e0f66acbde8ce33"></a>
<a id="astructsensing__sensor__config_html_af9d2ee27b3a04fd65baa1d1d0cb2badc"></a>
<a id="astructsensing__sensor__info_html"></a>
<a id="astructsensing__sensor__info_html_a085e8c00586c61245b822c7ea9db9c98"></a>
<a id="astructsensing__sensor__info_html_a5b2ddf0829031098301e244f60741f2b"></a>
<a id="astructsensing__sensor__info_html_a6b20ad8747a95cf1dc7346374de6b855"></a>
<a id="astructsensing__sensor__info_html_aa3e056ad9c52c3388e049b08d0844b49"></a>
<a id="astructsensing__sensor__info_html_ac7b4f33115f7a7a24095ca90b1e7acfe"></a>
<a id="astructsensing__sensor__info_html_ace77ba2ab5d5eee7c4e385fc2ea74ee8"></a>
<a id="astructsensing__sensor__version_html"></a>
<a id="astructsensing__sensor__version_html_a0023cbb5114f4a3d3a1cf388e5034cfc"></a>
<a id="astructsensing__sensor__version_html_a10fe885cd0cd9a6a5209308e188def3d"></a>
<a id="astructsensing__sensor__version_html_a668f5d23171c38e1cc13a4221e639815"></a>
<a id="astructsensing__sensor__version_html_a8d41ea3c181c7062aa8f76b17c652b41"></a>
<a id="astructsensing__sensor__version_html_ad7275123dd08f06ee0307325c8f5fb37"></a>

```c
/*
 * Copyright (c) 2022-2023 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SENSING_SENSING_H_
#define ZEPHYR_INCLUDE_SENSING_SENSING_H_


#include <zephyr/sensing/sensing_datatypes.h>
#include <zephyr/sensing/sensing_sensor_types.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

struct sensing_sensor_version {
        union {
                uint32_t value;
                struct {
                        uint8_t major;
                        uint8_t minor;
                        uint8_t hotfix;
                        uint8_t build;
                };
        };
};

#define SENSING_SENSOR_VERSION(_major, _minor, _hotfix, _build)         \
                                (FIELD_PREP(GENMASK(31, 24), _major) |  \
                                 FIELD_PREP(GENMASK(23, 16), _minor) |  \
                                 FIELD_PREP(GENMASK(15, 8), _hotfix) |  \
                                 FIELD_PREP(GENMASK(7, 0), _build))


#define SENSING_SENSOR_FLAG_REPORT_ON_EVENT                     BIT(0)

#define SENSING_SENSOR_FLAG_REPORT_ON_CHANGE                    BIT(1)


#define SENSING_SENSITIVITY_INDEX_ALL -1

enum sensing_sensor_state {
        SENSING_SENSOR_STATE_READY = 0,
        SENSING_SENSOR_STATE_OFFLINE = 1,
};

enum sensing_sensor_attribute {
        SENSING_SENSOR_ATTRIBUTE_INTERVAL = 0,

        SENSING_SENSOR_ATTRIBUTE_SENSITIVITY = 1,

        SENSING_SENSOR_ATTRIBUTE_LATENCY = 2,

        SENSING_SENSOR_ATTRIBUTE_MAX,
};

typedef void *sensing_sensor_handle_t;

typedef void (*sensing_data_event_t)(
                sensing_sensor_handle_t handle,
                const void *buf,
                void *context);

struct sensing_sensor_info {
        const char *name;

        const char *friendly_name;

        const char *vendor;

        const char *model;

        const int32_t type;

        const uint32_t minimal_interval;
};


struct sensing_callback_list {
        sensing_data_event_t on_data_event;
        void *context;
};

struct sensing_sensor_config {
        enum sensing_sensor_attribute attri;

        int8_t data_field;

        union {
                uint32_t interval;

                uint32_t sensitivity;

                uint64_t latency;
        };
};

int sensing_get_sensors(int *num_sensors, const struct sensing_sensor_info **info);

int sensing_open_sensor(
                const struct sensing_sensor_info *info,
                struct sensing_callback_list *cb_list,
                sensing_sensor_handle_t *handle);

int sensing_open_sensor_by_dt(
                const struct device *dev, struct sensing_callback_list *cb_list,
                sensing_sensor_handle_t *handle);

int sensing_close_sensor(
                sensing_sensor_handle_t *handle);

int sensing_set_config(
                sensing_sensor_handle_t handle,
                struct sensing_sensor_config *configs, int count);

int sensing_get_config(
                sensing_sensor_handle_t handle,
                struct sensing_sensor_config *configs, int count);

const struct sensing_sensor_info *sensing_get_sensor_info(
                sensing_sensor_handle_t handle);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_SENSING_SENSING_H_ */
```

## 757.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022-2023 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 333 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SENSING_SENSING_H_`。

## 757.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sensing_8h.html)
- [zephyr/sensing/sensing_datatypes.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing__datatypes_8h.html)
- [zephyr/sensing/sensing_sensor_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor__types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [sensing_sensor_version](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [value](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md#a0023cbb5114f4a3d3a1cf388e5034cfc)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [major](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md#ad7275123dd08f06ee0307325c8f5fb37)
- [minor](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md#a8d41ea3c181c7062aa8f76b17c652b41)
- [hotfix](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md#a10fe885cd0cd9a6a5209308e188def3d)
- [build](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md#a668f5d23171c38e1cc13a4221e639815)
- [sensing_sensor_state](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gabc9657708851e6a744a7cd73319efe06)
- [SENSING_SENSOR_STATE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ggabc9657708851e6a744a7cd73319efe06a735fe339796ea7b4d2387d931382ce93)
- [SENSING_SENSOR_STATE_OFFLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ggabc9657708851e6a744a7cd73319efe06af23a28e861a8fa2d49b18a0fbe62600e)
- [sensing_sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga69d2ae9f45215742654bfc7e4676e6f2)
- [SENSING_SENSOR_ATTRIBUTE_INTERVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gga69d2ae9f45215742654bfc7e4676e6f2a8c9870b1303008b45e2caeb33f5c44a3)
- [SENSING_SENSOR_ATTRIBUTE_SENSITIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gga69d2ae9f45215742654bfc7e4676e6f2abc39825a643b9d1452162f057f79774b)
- [SENSING_SENSOR_ATTRIBUTE_LATENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gga69d2ae9f45215742654bfc7e4676e6f2a2ccb8b476935ce27b2eedbb889e25476)
- [SENSING_SENSOR_ATTRIBUTE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gga69d2ae9f45215742654bfc7e4676e6f2a072ff2aa9640503bfd8cbc8f7d271980)
- [sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)
- [sensing_data_event_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga5440a8914b664209d62388183b3c89ea)
- [sensing_sensor_info](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md)
- [name](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md#ac7b4f33115f7a7a24095ca90b1e7acfe)
- [friendly_name](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md#aa3e056ad9c52c3388e049b08d0844b49)
- [vendor](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md#a085e8c00586c61245b822c7ea9db9c98)
- [model](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md#ace77ba2ab5d5eee7c4e385fc2ea74ee8)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [type](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md#a6b20ad8747a95cf1dc7346374de6b855)
- [minimal_interval](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md#a5b2ddf0829031098301e244f60741f2b)
- [sensing_callback_list](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md)
- [on_data_event](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md#a7d0d7c878e338f19fd48c66cda9d04fc)
- [context](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md#a43504dbe7d484f0d0e7d33b8bb6318d4)
- [sensing_sensor_config](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md)
- [attri](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#a9bdf50a1018d6d9426efd991d05bf72b)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [data_field](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#ac4389c439db16cb25a2e622baf0aeb9b)
- [interval](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#a7512f7254f6960ed398150db23868965)
- [sensitivity](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#acc1270dbe02ff6324e0f66acbde8ce33)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [latency](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#af9d2ee27b3a04fd65baa1d1d0cb2badc)
- [sensing_get_sensors](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gaf3b6c66c2db12115f3ebec0cdba32e86)
- [sensing_open_sensor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga8e427d28efc492f15d762af3308d78cd)
- [sensing_open_sensor_by_dt](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga4218453664fee0aa61697018e3193e7a)
- [device](../device_reference/P002_设备对象结构.md)
- [sensing_close_sensor](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga98e49ea0e84e93867df20033d01ee66c)
- [sensing_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga46591a2d29f5b5e160a72bbe289884ab)
- [sensing_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gaf4037066c9a7a9f3eb1c79a4d8ae0920)
- [sensing_get_sensor_info](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga4399f2e03d4d9444045b705b13cb6dfd)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [sensing_datatypes.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing__datatypes_8h.html)
- [sensing_sensor_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor__types_8h.html)
- [sensing_callback_list::context](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md#a43504dbe7d484f0d0e7d33b8bb6318d4)
- [sensing_callback_list::on_data_event](../sensor_navigation_model_reference/P024_sensing_callback_list_结构体.md#a7d0d7c878e338f19fd48c66cda9d04fc)
- [sensing_sensor_config::interval](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#a7512f7254f6960ed398150db23868965)
- [sensing_sensor_config::attri](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#a9bdf50a1018d6d9426efd991d05bf72b)
- [sensing_sensor_config::data_field](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#ac4389c439db16cb25a2e622baf0aeb9b)
- [sensing_sensor_config::sensitivity](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#acc1270dbe02ff6324e0f66acbde8ce33)
- [sensing_sensor_config::latency](../sensor_navigation_model_reference/P025_sensing_sensor_config_结构体.md#af9d2ee27b3a04fd65baa1d1d0cb2badc)
- [sensing_sensor_info::vendor](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md#a085e8c00586c61245b822c7ea9db9c98)
- [sensing_sensor_info::minimal_interval](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md#a5b2ddf0829031098301e244f60741f2b)
- [sensing_sensor_info::type](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md#a6b20ad8747a95cf1dc7346374de6b855)
- [sensing_sensor_info::friendly_name](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md#aa3e056ad9c52c3388e049b08d0844b49)
- [sensing_sensor_info::name](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md#ac7b4f33115f7a7a24095ca90b1e7acfe)
- [sensing_sensor_info::model](../sensor_navigation_model_reference/P026_sensing_sensor_info_结构体.md#ace77ba2ab5d5eee7c4e385fc2ea74ee8)
- [sensing_sensor_version::value](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md#a0023cbb5114f4a3d3a1cf388e5034cfc)
- [sensing_sensor_version::hotfix](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md#a10fe885cd0cd9a6a5209308e188def3d)
- [sensing_sensor_version::build](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md#a668f5d23171c38e1cc13a4221e639815)
- [sensing_sensor_version::minor](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md#a8d41ea3c181c7062aa8f76b17c652b41)
- [sensing_sensor_version::major](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md#ad7275123dd08f06ee0307325c8f5fb37)

---

[上一章](P756_semtech-sx1509b.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P758_sensing_datatypes.h_源码浏览.md)
