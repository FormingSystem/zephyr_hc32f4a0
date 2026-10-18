---
id: learning.zephyr-docs.api-source-reference.page-50
title: backend.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/backend_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_backend.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/backend_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/backend_8h.html)。

## 50.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
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
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00061"></a>
<a id="l00061"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="agroup__ec__host__cmd__interface__backend_html_ga1097b2148a5e7e6bf9f2a67e54dd5ba5"></a>
<a id="agroup__ec__host__cmd__interface__backend_html_ga12574d2eff8f07fd36967ccbc7600e1c"></a>
<a id="agroup__ec__host__cmd__interface__backend_html_ga32d7a58724694ab753efbf7f81e8d940"></a>
<a id="agroup__ec__host__cmd__interface__backend_html_ga558b7690dad9a9a5eb8771fcfeba3b63"></a>
<a id="agroup__ec__host__cmd__interface__backend_html_ga811b9c355942811f0fee22c1fa8a5787"></a>
<a id="agroup__ec__host__cmd__interface__backend_html_ga892fec4587de508805fdf5ace9dd1050"></a>
<a id="agroup__ec__host__cmd__interface__backend_html_gaa4562dd46503cf8844a546b102ce01e9"></a>
<a id="agroup__ec__host__cmd__interface__backend_html_gaba4d3e1fd2b723448be2cb4b7f6293ac"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructec__host__cmd__backend__api_html"></a>
<a id="astructec__host__cmd__backend__api_html_ae2619efe5d809f7aa51252727b1a05c4"></a>
<a id="astructec__host__cmd__backend__api_html_afed14f2aa633e836c90c8c559a9fe7bb"></a>
<a id="astructec__host__cmd__backend_html"></a>
<a id="astructec__host__cmd__backend_html_a57236d69bdc9a99b1cb3acbac0be275b"></a>
<a id="astructec__host__cmd__backend_html_aadf44f4eff331abeca40bc0f69bc173d"></a>
<a id="astructec__host__cmd__rx__ctx_html"></a>
<a id="astructec__host__cmd__rx__ctx_html_a2db5dc5740436c8e0e232b959472ed0f"></a>
<a id="astructec__host__cmd__rx__ctx_html_ae9f1c0c78d27dd5aa9bf47c56452a75a"></a>
<a id="astructec__host__cmd__rx__ctx_html_afcae3b7881f1c8634bb3ac1315111294"></a>
<a id="astructec__host__cmd__tx__buf_html"></a>
<a id="astructec__host__cmd__tx__buf_html_a0f115f85bd271fa0defec1a2fc461d4c"></a>
<a id="astructec__host__cmd__tx__buf_html_a6444723bccc196fb9792e95957bd98a5"></a>
<a id="astructec__host__cmd__tx__buf_html_afaff8fbcb798a0445b029db1cedb6fd1"></a>
<a id="astructgpio__dt__spec_html"></a>

```c
/*
 * Copyright (c) 2020 Google LLC.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_EC_HOST_CMD_BACKEND_H_
#define ZEPHYR_INCLUDE_MGMT_EC_HOST_CMD_BACKEND_H_


#include <zephyr/sys/__assert.h>
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/kernel.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

struct ec_host_cmd_backend {
        const struct ec_host_cmd_backend_api *api;
        void *ctx;
};

struct ec_host_cmd_rx_ctx {
        uint8_t *buf;
        size_t len;
        size_t len_max;
};

struct ec_host_cmd_tx_buf {
        void *buf;
        size_t len;
        size_t len_max;
};

typedef int (*ec_host_cmd_backend_api_init)(const struct ec_host_cmd_backend *backend,
                                            struct ec_host_cmd_rx_ctx *rx_ctx,
                                            struct ec_host_cmd_tx_buf *tx);

typedef int (*ec_host_cmd_backend_api_send)(const struct ec_host_cmd_backend *backend);

struct ec_host_cmd_backend_api {
        ec_host_cmd_backend_api_init init;
        ec_host_cmd_backend_api_send send;
};

struct ec_host_cmd_backend *ec_host_cmd_backend_get_espi(const struct device *dev);

struct ec_host_cmd_backend *ec_host_cmd_backend_get_shi_npcx(void);

struct ec_host_cmd_backend *ec_host_cmd_backend_get_shi_ite(void);

struct ec_host_cmd_backend *ec_host_cmd_backend_get_uart(const struct device *dev);

struct ec_host_cmd_backend *ec_host_cmd_backend_get_spi(struct gpio_dt_spec *cs);

void ec_host_cmd_backend_usb_trigger_event(void);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_EC_HOST_CMD_EC_HOST_CMD_BACKEND_H_ */
```

## 50.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Google LLC.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 184 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_EC_HOST_CMD_EC_HOST_CMD_BACKEND_H_`。

## 50.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/backend_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [ec_host_cmd_backend](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md)
- [ec_host_cmd_backend_api](../system_service_model_reference/P009_ec_host_cmd_backend_api_结构体.md)
- [api](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md#aadf44f4eff331abeca40bc0f69bc173d)
- [ctx](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md#a57236d69bdc9a99b1cb3acbac0be275b)
- [ec_host_cmd_rx_ctx](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [buf](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md#afcae3b7881f1c8634bb3ac1315111294)
- [len](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md#ae9f1c0c78d27dd5aa9bf47c56452a75a)
- [len_max](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md#a2db5dc5740436c8e0e232b959472ed0f)
- [ec_host_cmd_tx_buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md)
- [buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md#a6444723bccc196fb9792e95957bd98a5)
- [len](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md#afaff8fbcb798a0445b029db1cedb6fd1)
- [len_max](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md#a0f115f85bd271fa0defec1a2fc461d4c)
- [ec_host_cmd_backend_api_init](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga811b9c355942811f0fee22c1fa8a5787)
- [ec_host_cmd_backend_api_send](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)
- [init](../system_service_model_reference/P009_ec_host_cmd_backend_api_结构体.md#ae2619efe5d809f7aa51252727b1a05c4)
- [send](../system_service_model_reference/P009_ec_host_cmd_backend_api_结构体.md#afed14f2aa633e836c90c8c559a9fe7bb)
- [ec_host_cmd_backend_get_espi](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga32d7a58724694ab753efbf7f81e8d940)
- [device](../device_reference/P002_设备对象结构.md)
- [ec_host_cmd_backend_get_shi_npcx](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#gaa4562dd46503cf8844a546b102ce01e9)
- [ec_host_cmd_backend_get_shi_ite](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga892fec4587de508805fdf5ace9dd1050)
- [ec_host_cmd_backend_get_uart](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga558b7690dad9a9a5eb8771fcfeba3b63)
- [ec_host_cmd_backend_get_spi](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#ga12574d2eff8f07fd36967ccbc7600e1c)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [ec_host_cmd_backend_usb_trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface__backend.html#gaba4d3e1fd2b723448be2cb4b7f6293ac)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [ec_host_cmd_backend_api::init](../system_service_model_reference/P009_ec_host_cmd_backend_api_结构体.md#ae2619efe5d809f7aa51252727b1a05c4)
- [ec_host_cmd_backend_api::send](../system_service_model_reference/P009_ec_host_cmd_backend_api_结构体.md#afed14f2aa633e836c90c8c559a9fe7bb)
- [ec_host_cmd_backend::ctx](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md#a57236d69bdc9a99b1cb3acbac0be275b)
- [ec_host_cmd_backend::api](../system_service_model_reference/P008_ec_host_cmd_backend_结构体.md#aadf44f4eff331abeca40bc0f69bc173d)
- [ec_host_cmd_rx_ctx::len_max](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md#a2db5dc5740436c8e0e232b959472ed0f)
- [ec_host_cmd_rx_ctx::len](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md#ae9f1c0c78d27dd5aa9bf47c56452a75a)
- [ec_host_cmd_rx_ctx::buf](../system_service_model_reference/P014_ec_host_cmd_rx_ctx_结构体.md#afcae3b7881f1c8634bb3ac1315111294)
- [ec_host_cmd_tx_buf::len_max](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md#a0f115f85bd271fa0defec1a2fc461d4c)
- [ec_host_cmd_tx_buf::buf](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md#a6444723bccc196fb9792e95957bd98a5)
- [ec_host_cmd_tx_buf::len](../system_service_model_reference/P015_ec_host_cmd_tx_buf_结构体.md#afaff8fbcb798a0445b029db1cedb6fd1)

---

[上一章](P049_aw9523b.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P051_bas.h_源码浏览.md)
