---
id: learning.zephyr-docs.api-source-reference.page-883
title: ubx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ubx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第883章\_ubx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ubx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ubx_8h.html)。

## 883.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00090"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="aatomic_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__modem__ubx_html_ga0fd0def90f6304e679c4123e3c8d0c3f"></a>
<a id="agroup__modem__ubx_html_ga4e459f955e34c9059702c3d7f9794948"></a>
<a id="agroup__modem__ubx_html_ga68210f4afd5880c532d82fd0bac1d933"></a>
<a id="agroup__modem__ubx_html_ga770650b055fd597f000a1d4f9daaf712"></a>
<a id="agroup__modem__ubx_html_gae0bfe22e7e8d7d38ae9f41648f7fcfda"></a>
<a id="agroup__modem__ubx_html_gaf49363fb4decb4656566b508a061212f"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amodem_2ubx_2protocol_8h_html"></a>
<a id="apipe_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructk__work_html"></a>
<a id="astructmodem__ubx__config_html"></a>
<a id="astructmodem__ubx__config_html_a08ba4ac10872f451a302fcbc04a04253"></a>
<a id="astructmodem__ubx__config_html_a19f107638346a44bddc73045f595ec98"></a>
<a id="astructmodem__ubx__config_html_a75237681e1c9bf094b347e71e1ad823e"></a>
<a id="astructmodem__ubx__config_html_a75634cde7a69ef78ea0370f423307a0e"></a>
<a id="astructmodem__ubx__config_html_a7ac0f254167c3197366b210bef2ac75d"></a>
<a id="astructmodem__ubx__config_html_acac2ab2800443c4f60cbf5df9ca8cd5e"></a>
<a id="astructmodem__ubx__match_html"></a>
<a id="astructmodem__ubx__match_html_a657d7961121ed1860635df96597b88b8"></a>
<a id="astructmodem__ubx__match_html_aba64a4f7825a1f3b3cbee6f3473d7f74"></a>
<a id="astructmodem__ubx__script_html"></a>
<a id="astructmodem__ubx__script_html_a033047efbf34102985fad507711905ec"></a>
<a id="astructmodem__ubx__script_html_a041de757b5fb26f1cdfb89cb19610f11"></a>
<a id="astructmodem__ubx__script_html_a0f8ffa1d60333e14af7e91d472824e47"></a>
<a id="astructmodem__ubx__script_html_a1e91925ba17f30685db67d4f326d2f31"></a>
<a id="astructmodem__ubx__script_html_a4910a3551004f19249c66a5b695795ce"></a>
<a id="astructmodem__ubx__script_html_a716f90ed421af01c829cb716d94a9a76"></a>
<a id="astructmodem__ubx__script_html_a90d08ee6c3832f3d0198cea0aa7b3b8d"></a>
<a id="astructmodem__ubx__script_html_a9882eb3b10b9739c916f5317fda412ea"></a>
<a id="astructmodem__ubx__script_html_ab91b22317aa1cfb36f7c24de2b425137"></a>
<a id="astructmodem__ubx_html"></a>
<a id="astructmodem__ubx_html_a0489f188b1dcdd54ba756ad821c62db5"></a>
<a id="astructmodem__ubx_html_a0bc3ee485c2e6f63727efae5b61a64ac"></a>
<a id="astructmodem__ubx_html_a1b853c80109313feaebfb8cdb24b950c"></a>
<a id="astructmodem__ubx_html_a337b4afe37e031ecd563572951be9412"></a>
<a id="astructmodem__ubx_html_a4add513db024eb040de858e8901bc017"></a>
<a id="astructmodem__ubx_html_a639183a5a24d953015df30f64b2f1c85"></a>
<a id="astructmodem__ubx_html_a914c78bb7d0dcf5edf5f08273c6078df"></a>
<a id="astructmodem__ubx_html_a98b8d6b02acbfa564b510b6f7c9908d5"></a>
<a id="astructmodem__ubx_html_ac9a3b4009eabeb92e2e3cff093d74d2c"></a>
<a id="astructmodem__ubx_html_ad98fcc4a93781ff5cd5406cb0560c849"></a>
<a id="astructmodem__ubx_html_adfd9249b1f72aae1f2b9818cbf0de640"></a>
<a id="astructmodem__ubx_html_ae5c5914a3c88b908e80646d71ada7bfe"></a>
<a id="astructmodem__ubx_html_ae7182d2345bcd3585828f0f48d42321a"></a>
<a id="astructmodem__ubx_html_aeeb735c338ed161d7eddeaa561cca5d9"></a>
<a id="astructubx__frame__match_html"></a>
<a id="astructubx__frame_html"></a>

```c
/*
 * Copyright (c) 2024 NXP
 * Copyright (c) 2025 Croxel Inc.
 * Copyright (c) 2025 CogniPilot Foundation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MODEM_UBX_H_
#define ZEPHYR_INCLUDE_MODEM_UBX_H_

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/sys/atomic.h>

#include <zephyr/modem/pipe.h>
#include <zephyr/modem/ubx/protocol.h>

#ifdef __cplusplus
extern "C" {
#endif


struct modem_ubx;

typedef void (*modem_ubx_match_callback)(struct modem_ubx *ubx,
                                         const struct ubx_frame *frame,
                                         size_t len,
                                         void *user_data);

struct modem_ubx_match {
        struct ubx_frame_match filter;
        modem_ubx_match_callback handler;
};

#define MODEM_UBX_MATCH_ARRAY_DEFINE(_name, ...)                                                   \
        struct modem_ubx_match _name[] = {__VA_ARGS__};

#define MODEM_UBX_MATCH_DEFINE(_class_id, _msg_id, _handler)                                       \
{                                                                                                  \
        .filter = {                                                                                \
                .class = _class_id,                                                                \
                .id = _msg_id,                                                                     \
        },                                                                                         \
        .handler = _handler,                                                                       \
}

struct modem_ubx_script {
        struct {
                const void *buf;
                uint16_t len;
        } request;
        struct {
                uint8_t *buf;
                uint16_t buf_len;
                uint16_t received_len;
        } response;
        struct modem_ubx_match match;
        uint16_t retry_count;
        k_timeout_t timeout;
};

struct modem_ubx {
        void *user_data;
        atomic_t attached;
        uint8_t *receive_buf;
        uint16_t receive_buf_size;
        uint16_t receive_buf_offset;
        struct modem_ubx_script *script;
        struct modem_pipe *pipe;
        struct k_work process_work;
        struct k_sem script_stopped_sem;
        struct k_sem script_sent_sem;
        struct k_sem script_running_sem;
        struct {
                const struct modem_ubx_match *array;
                size_t size;
        } unsol_matches;
};

struct modem_ubx_config {
        void *user_data;
        uint8_t *receive_buf;
        uint16_t receive_buf_size;
        struct {
                const struct modem_ubx_match *array;
                size_t size;
        } unsol_matches;
};

int modem_ubx_attach(struct modem_ubx *ubx, struct modem_pipe *pipe);

void modem_ubx_release(struct modem_ubx *ubx);

int modem_ubx_init(struct modem_ubx *ubx, const struct modem_ubx_config *config);

int modem_ubx_run_script(struct modem_ubx *ubx, struct modem_ubx_script *script);

int modem_ubx_run_script_for_each(struct modem_ubx *ubx, struct modem_ubx_script *script,
                                  struct ubx_frame *array, size_t array_size);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MODEM_UBX_H_ */
```

## 883.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 NXP。

版权（Copyright）：© 2025 Croxel Inc.。

版权（Copyright）：© 2025 CogniPilot Foundation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 165 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MODEM_UBX_H_`。

## 883.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ubx_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/modem/pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h.html)
- [modem_ubx](../modem_wireless_model_reference/P061_modem_ubx_结构体.md)
- [modem_ubx_match_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#gae0bfe22e7e8d7d38ae9f41648f7fcfda)
- [ubx_frame](../sensor_navigation_model_reference/P066_ubx_frame_结构体.md)
- [modem_ubx_match](../modem_wireless_model_reference/P063_modem_ubx_match_结构体.md)
- [ubx_frame_match](../sensor_navigation_model_reference/P067_ubx_frame_match_结构体.md)
- [filter](../modem_wireless_model_reference/P063_modem_ubx_match_结构体.md#aba64a4f7825a1f3b3cbee6f3473d7f74)
- [handler](../modem_wireless_model_reference/P063_modem_ubx_match_结构体.md#a657d7961121ed1860635df96597b88b8)
- [modem_ubx_script](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md)
- [buf](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a0f8ffa1d60333e14af7e91d472824e47)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [len](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a033047efbf34102985fad507711905ec)
- [request](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#ab91b22317aa1cfb36f7c24de2b425137)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [buf_len](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a9882eb3b10b9739c916f5317fda412ea)
- [received_len](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a716f90ed421af01c829cb716d94a9a76)
- [response](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a90d08ee6c3832f3d0198cea0aa7b3b8d)
- [match](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a1e91925ba17f30685db67d4f326d2f31)
- [retry_count](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a4910a3551004f19249c66a5b695795ce)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [timeout](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a041de757b5fb26f1cdfb89cb19610f11)
- [user_data](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#ad98fcc4a93781ff5cd5406cb0560c849)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [attached](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a337b4afe37e031ecd563572951be9412)
- [receive_buf](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a0bc3ee485c2e6f63727efae5b61a64ac)
- [receive_buf_size](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a4add513db024eb040de858e8901bc017)
- [receive_buf_offset](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a639183a5a24d953015df30f64b2f1c85)
- [script](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#ac9a3b4009eabeb92e2e3cff093d74d2c)
- [pipe](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a1b853c80109313feaebfb8cdb24b950c)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [process_work](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#adfd9249b1f72aae1f2b9818cbf0de640)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [script_stopped_sem](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#ae5c5914a3c88b908e80646d71ada7bfe)
- [script_sent_sem](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a914c78bb7d0dcf5edf5f08273c6078df)
- [script_running_sem](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a0489f188b1dcdd54ba756ad821c62db5)
- [array](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#ae7182d2345bcd3585828f0f48d42321a)
- [size](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a98b8d6b02acbfa564b510b6f7c9908d5)
- [unsol_matches](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#aeeb735c338ed161d7eddeaa561cca5d9)
- [modem_ubx_config](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md)
- [user_data](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md#acac2ab2800443c4f60cbf5df9ca8cd5e)
- [receive_buf](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md#a7ac0f254167c3197366b210bef2ac75d)
- [receive_buf_size](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md#a75634cde7a69ef78ea0370f423307a0e)
- [array](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md#a75237681e1c9bf094b347e71e1ad823e)
- [size](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md#a19f107638346a44bddc73045f595ec98)
- [unsol_matches](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md#a08ba4ac10872f451a302fcbc04a04253)
- [modem_ubx_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga4e459f955e34c9059702c3d7f9794948)
- [modem_ubx_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga68210f4afd5880c532d82fd0bac1d933)
- [modem_ubx_init](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#gaf49363fb4decb4656566b508a061212f)
- [modem_ubx_run_script](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga770650b055fd597f000a1d4f9daaf712)
- [modem_ubx_run_script_for_each](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__ubx.html#ga0fd0def90f6304e679c4123e3c8d0c3f)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h.html)
- [pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [modem_ubx_config::unsol_matches](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md#a08ba4ac10872f451a302fcbc04a04253)
- [modem_ubx_config::size](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md#a19f107638346a44bddc73045f595ec98)
- [modem_ubx_config::array](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md#a75237681e1c9bf094b347e71e1ad823e)
- [modem_ubx_config::receive_buf_size](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md#a75634cde7a69ef78ea0370f423307a0e)
- [modem_ubx_config::receive_buf](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md#a7ac0f254167c3197366b210bef2ac75d)
- [modem_ubx_config::user_data](../modem_wireless_model_reference/P062_modem_ubx_config_结构体.md#acac2ab2800443c4f60cbf5df9ca8cd5e)
- [modem_ubx_match::handler](../modem_wireless_model_reference/P063_modem_ubx_match_结构体.md#a657d7961121ed1860635df96597b88b8)
- [modem_ubx_match::filter](../modem_wireless_model_reference/P063_modem_ubx_match_结构体.md#aba64a4f7825a1f3b3cbee6f3473d7f74)
- [modem_ubx_script::len](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a033047efbf34102985fad507711905ec)
- [modem_ubx_script::timeout](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a041de757b5fb26f1cdfb89cb19610f11)
- [modem_ubx_script::buf](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a0f8ffa1d60333e14af7e91d472824e47)
- [modem_ubx_script::match](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a1e91925ba17f30685db67d4f326d2f31)
- [modem_ubx_script::retry_count](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a4910a3551004f19249c66a5b695795ce)
- [modem_ubx_script::received_len](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a716f90ed421af01c829cb716d94a9a76)
- [modem_ubx_script::response](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a90d08ee6c3832f3d0198cea0aa7b3b8d)
- [modem_ubx_script::buf_len](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#a9882eb3b10b9739c916f5317fda412ea)
- [modem_ubx_script::request](../modem_wireless_model_reference/P064_modem_ubx_script_结构体.md#ab91b22317aa1cfb36f7c24de2b425137)
- [modem_ubx::script_running_sem](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a0489f188b1dcdd54ba756ad821c62db5)
- [modem_ubx::receive_buf](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a0bc3ee485c2e6f63727efae5b61a64ac)
- [modem_ubx::pipe](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a1b853c80109313feaebfb8cdb24b950c)
- [modem_ubx::attached](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a337b4afe37e031ecd563572951be9412)
- [modem_ubx::receive_buf_size](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a4add513db024eb040de858e8901bc017)
- [modem_ubx::receive_buf_offset](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a639183a5a24d953015df30f64b2f1c85)
- [modem_ubx::script_sent_sem](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a914c78bb7d0dcf5edf5f08273c6078df)
- [modem_ubx::size](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#a98b8d6b02acbfa564b510b6f7c9908d5)
- [modem_ubx::script](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#ac9a3b4009eabeb92e2e3cff093d74d2c)
- [modem_ubx::user_data](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#ad98fcc4a93781ff5cd5406cb0560c849)
- [modem_ubx::process_work](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#adfd9249b1f72aae1f2b9818cbf0de640)
- [modem_ubx::script_stopped_sem](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#ae5c5914a3c88b908e80646d71ada7bfe)
- [modem_ubx::array](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#ae7182d2345bcd3585828f0f48d42321a)
- [modem_ubx::unsol_matches](../modem_wireless_model_reference/P061_modem_ubx_结构体.md#aeeb735c338ed161d7eddeaa561cca5d9)

---

[上一章](P882_uart_pipe.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P884_udc.h_源码浏览.md)
