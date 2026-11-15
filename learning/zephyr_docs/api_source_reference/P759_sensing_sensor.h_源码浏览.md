---
id: learning.zephyr-docs.api-source-reference.page-759
title: sensing_sensor.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第759章\_sensing\_sensor.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor_8h.html)。

## 759.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="foldopen00391"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__rtio_html_ga7ff7d0337e43b0a9380bb94a4a143a47"></a>
<a id="agroup__sensing__api_html_gabc9657708851e6a744a7cd73319efe06"></a>
<a id="agroup__sensing__api_html_gac959e076fcdc105dfaac1d7a984ba293"></a>
<a id="agroup__sensing__sensor_html_ga2c5cfb298b2dfde967edfdd987115021"></a>
<a id="agroup__sensing__sensor_html_gab4c41d02b3731e5829a41e1f5f5154a5"></a>
<a id="agroup__sensing__sensor_html_gab9446a3085b6b05da448dce59db50387"></a>
<a id="agroup__sensor__interface_html_gaaa1b502bc029b10d7b23b0a25ef4e934"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="asensing_8h_html"></a>
<a id="asensor_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructrtio__iodev__api_html"></a>
<a id="astructsensing__sensor__register__info_html"></a>
<a id="astructsensing__sensor__register__info_html_a133621dcf1da9c9ffd111eeec007f220"></a>
<a id="astructsensing__sensor__register__info_html_a6300055172c8692b8313adcef5507d41"></a>
<a id="astructsensing__sensor__register__info_html_aab10e29faf4e3a6bcc33d99119bb8bc9"></a>
<a id="astructsensing__sensor__register__info_html_af87ee2748229a7f43049d058da930ce1"></a>
<a id="astructsensing__sensor__version_html"></a>

```c
/*
 * Copyright (c) 2022-2023 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SENSING_SENSING_SENSOR_H_
#define ZEPHYR_INCLUDE_SENSING_SENSING_SENSOR_H_

#include <stdbool.h>
#include <zephyr/device.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/sensing/sensing.h>


#ifdef __cplusplus
extern "C" {
#endif

struct sensing_sensor_register_info {
        uint16_t flags;

        uint16_t sample_size;

        uint8_t sensitivity_count;

        struct sensing_sensor_version version;
};


enum {
        EVENT_CONFIG_READY,
        EVENT_SENSOR_POLL,
};

enum {
        SENSOR_LATER_CFG_BIT,
        SENSOR_POLL_BIT,
};

struct sensing_connection {
        sys_snode_t snode;
        struct sensing_sensor *source;
        struct sensing_sensor *sink;
        uint32_t interval;
        int sensitivity[CONFIG_SENSING_MAX_SENSITIVITY_COUNT];
        void *data;
        uint64_t next_consume_time;
        struct sensing_callback_list *callback_list;
};

struct sensing_sensor {
        const struct device *dev;
        const struct sensing_sensor_info *info;
        const struct sensing_sensor_register_info *register_info;
        const uint16_t reporter_num;
        sys_slist_t client_list;
        uint32_t interval;
        uint8_t sensitivity_count;
        int sensitivity[CONFIG_SENSING_MAX_SENSITIVITY_COUNT];
        enum sensing_sensor_state state;
        struct rtio_iodev *iodev;
        struct k_timer timer;
        rtio_sqe_handle_t stream_sqe;
        atomic_t flag;
        struct sensing_connection *conns;
};

#define SENSING_SENSOR_INFO_NAME(node, idx)                                     \
        _CONCAT(_CONCAT(__sensing_sensor_info_, idx), DEVICE_DT_NAME_GET(node))

#define SENSING_SENSOR_INFO_DEFINE(node, idx)                           \
        const static STRUCT_SECTION_ITERABLE(sensing_sensor_info,       \
                        SENSING_SENSOR_INFO_NAME(node, idx)) = {        \
                .type = DT_PROP_BY_IDX(node, sensor_types, idx),        \
                .name = DT_NODE_FULL_NAME(node),                        \
                .friendly_name = DT_PROP(node, friendly_name),          \
                .vendor = DT_NODE_VENDOR_OR(node, NULL),                \
                .model = DT_NODE_MODEL_OR(node, NULL),                  \
                .minimal_interval = DT_PROP(node, minimal_interval),    \
        };

#define SENSING_CONNECTIONS_NAME(node)                                  \
        _CONCAT(__sensing_connections_, DEVICE_DT_NAME_GET(node))

#define SENSING_SENSOR_SOURCE_NAME(idx, node)                           \
        SENSING_SENSOR_NAME(DT_PHANDLE_BY_IDX(node, reporters, idx),    \
                DT_PROP_BY_IDX(node, reporters_index, idx))

#define SENSING_SENSOR_SOURCE_EXTERN(idx, node)                         \
extern struct sensing_sensor SENSING_SENSOR_SOURCE_NAME(idx, node);

#define SENSING_CONNECTION_INITIALIZER(source_name, cb_list_ptr)        \
{                                                                       \
        .callback_list = cb_list_ptr,                                   \
        .source = &source_name,                                         \
}

#define SENSING_CONNECTION_DEFINE(idx, node, cb_list_ptr)               \
        SENSING_CONNECTION_INITIALIZER(SENSING_SENSOR_SOURCE_NAME(idx, node), \
                                       cb_list_ptr)

#define SENSING_CONNECTIONS_DEFINE(node, num, cb_list_ptr)              \
        LISTIFY(num, SENSING_SENSOR_SOURCE_EXTERN,                      \
                                (), node)                               \
        static struct sensing_connection                                \
                        SENSING_CONNECTIONS_NAME(node)[(num)] = {       \
                LISTIFY(num, SENSING_CONNECTION_DEFINE,                 \
                                (,), node, cb_list_ptr)                 \
        };

struct sensing_submit_config {
        enum sensor_channel chan;
        const int info_index;
        const bool is_streaming;
};

extern const struct rtio_iodev_api __sensing_iodev_api;

#define SENSING_SUBMIT_CFG_NAME(node, idx)                                              \
        _CONCAT(_CONCAT(__sensing_submit_cfg_, idx), DEVICE_DT_NAME_GET(node))

#define SENSING_SENSOR_IODEV_NAME(node, idx)                                            \
        _CONCAT(_CONCAT(__sensing_iodev_, idx), DEVICE_DT_NAME_GET(node))

#define SENSING_SENSOR_IODEV_DEFINE(node, idx)                                          \
        static struct sensing_submit_config SENSING_SUBMIT_CFG_NAME(node, idx) = {      \
                .is_streaming = DT_PROP(node, stream_mode),                             \
                .info_index = idx,                                                      \
        };                                                                              \
        RTIO_IODEV_DEFINE(SENSING_SENSOR_IODEV_NAME(node, idx),                         \
                          &__sensing_iodev_api,                                         \
                          &SENSING_SUBMIT_CFG_NAME(node, idx));

#define SENSING_SENSOR_NAME(node, idx)                                  \
        _CONCAT(_CONCAT(__sensing_sensor_, idx), DEVICE_DT_NAME_GET(node))

#define SENSING_SENSOR_DEFINE(node, prop, idx, reg_ptr, cb_list_ptr)    \
        SENSING_SENSOR_INFO_DEFINE(node, idx)                           \
        SENSING_SENSOR_IODEV_DEFINE(node, idx)                          \
        STRUCT_SECTION_ITERABLE(sensing_sensor,                         \
                                SENSING_SENSOR_NAME(node, idx)) = {     \
                .dev = DEVICE_DT_GET(node),                             \
                .info = &SENSING_SENSOR_INFO_NAME(node, idx),           \
                .register_info = reg_ptr,                               \
                .reporter_num = DT_PROP_LEN_OR(node, reporters, 0),     \
                .conns = SENSING_CONNECTIONS_NAME(node),                \
                .iodev = &SENSING_SENSOR_IODEV_NAME(node, idx),         \
        };

#define SENSING_SENSORS_DEFINE(node, reg_ptr, cb_list_ptr)              \
        DT_FOREACH_PROP_ELEM_VARGS(node, sensor_types,                  \
                        SENSING_SENSOR_DEFINE, reg_ptr, cb_list_ptr)


#define SENSING_SENSORS_DT_DEFINE(node, reg_ptr, cb_list_ptr,   \
                                init_fn, pm_device,                     \
                                data_ptr, cfg_ptr, level, prio,         \
                                api_ptr, ...)                           \
        SENSOR_DEVICE_DT_DEFINE(node, init_fn, pm_device,               \
                                data_ptr, cfg_ptr, level, prio,         \
                                api_ptr, __VA_ARGS__);                  \
        SENSING_CONNECTIONS_DEFINE(node,                                \
                                   DT_PROP_LEN_OR(node, reporters, 0),  \
                                   cb_list_ptr);                        \
        SENSING_SENSORS_DEFINE(node, reg_ptr, cb_list_ptr);

#define SENSING_SENSORS_DT_INST_DEFINE(inst, ...)       \
        SENSING_SENSORS_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)

int sensing_sensor_get_reporters(
                const struct device *dev, int type,
                sensing_sensor_handle_t *reporter_handles, int max_handles);

int sensing_sensor_get_reporters_count(
                const struct device *dev, int type);

int sensing_sensor_get_state(
                const struct device *dev,
                enum sensing_sensor_state *state);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SENSING_SENSING_SENSOR_H_ */
```

## 759.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022-2023 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 439 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SENSING_SENSING_SENSOR_H_`。

## 759.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [zephyr/sensing/sensing.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing_8h.html)
- [sensing_sensor_register_info](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [flags](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md#a6300055172c8692b8313adcef5507d41)
- [sample_size](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md#a133621dcf1da9c9ffd111eeec007f220)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sensitivity_count](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md#aab10e29faf4e3a6bcc33d99119bb8bc9)
- [sensing_sensor_version](../sensor_navigation_model_reference/P032_sensing_sensor_version_结构体.md)
- [version](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md#af87ee2748229a7f43049d058da930ce1)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [sensing_sensor_state](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gabc9657708851e6a744a7cd73319efe06)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [rtio_sqe_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga7ff7d0337e43b0a9380bb94a4a143a47)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)
- [rtio_iodev_api](../rtio_model_reference/P004_RTIO设备函数表.md)
- [sensing_sensor_get_reporters](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#gab4c41d02b3731e5829a41e1f5f5154a5)
- [device](../device_reference/P002_设备对象结构.md)
- [sensing_sensor_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#gac959e076fcdc105dfaac1d7a984ba293)
- [sensing_sensor_get_reporters_count](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#ga2c5cfb298b2dfde967edfdd987115021)
- [sensing_sensor_get_state](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__sensor.html#gab9446a3085b6b05da448dce59db50387)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [sensing.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing_8h.html)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensing_sensor_register_info::sample_size](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md#a133621dcf1da9c9ffd111eeec007f220)
- [sensing_sensor_register_info::flags](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md#a6300055172c8692b8313adcef5507d41)
- [sensing_sensor_register_info::sensitivity_count](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md#aab10e29faf4e3a6bcc33d99119bb8bc9)
- [sensing_sensor_register_info::version](../sensor_navigation_model_reference/P027_sensing_sensor_register_info_结构体.md#af87ee2748229a7f43049d058da930ce1)

---

[上一章](P758_sensing_datatypes.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P760_sensing_sensor_types.h_源码浏览.md)
