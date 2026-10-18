---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-6
title: zephyr__drivers__fpga.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fpga_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr__drivers__fpga.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fpga_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P006_zephyr__drivers__fpga.h_头文件参考.md)。

## 6.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00034"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00047"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00092"></a>
<a id="l00096"></a>
<a id="l00100"></a>
<a id="l00104"></a>
<a id="l00108"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00117"></a>
<a id="foldopen00126"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="foldopen00148"></a>
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
<a id="l00158"></a>
<a id="foldopen00169"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="foldopen00189"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="foldopen00210"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="foldopen00229"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__fpga__interface__backend_html_ga02d71e7a82f446220d67664d4cc7a5c9"></a>
<a id="agroup__fpga__interface__backend_html_ga24fd6ce4832b960b79914f42010774aa"></a>
<a id="agroup__fpga__interface__backend_html_ga3c53b90b9d0b50c44c01a534c61e9212"></a>
<a id="agroup__fpga__interface__backend_html_ga872a8d75bb46de50a41b56170804ed27"></a>
<a id="agroup__fpga__interface__backend_html_ga9860c64bbc2cfb89df9b51da655691b6"></a>
<a id="agroup__fpga__interface__backend_html_gaf3e8ea5d443fd09352e2b63f82a459be"></a>
<a id="agroup__fpga__interface_html_ga0bbacdfdac79bace1786bb2a1627bb1e"></a>
<a id="agroup__fpga__interface_html_ga1a1e78a46df9f4bd374cf5ecc2449360"></a>
<a id="agroup__fpga__interface_html_ga1cace6c7cc44705bf861d7aa5e863e16"></a>
<a id="agroup__fpga__interface_html_gaa161c7a7006db24793c1a1ecdea25b5c"></a>
<a id="agroup__fpga__interface_html_gab41c04907be508f62e8df813d633b34b"></a>
<a id="agroup__fpga__interface_html_gab887999e8728bcc335a784afbdbbee8f"></a>
<a id="agroup__fpga__interface_html_gad9093bd96c6a62cd958718d1e01e3f37"></a>
<a id="agroup__fpga__interface_html_gadfc8d6c24cb1b1640393017a462011c9"></a>
<a id="agroup__fpga__interface_html_gga0bbacdfdac79bace1786bb2a1627bb1ea46571663477ca2df50b24cf93a5e2441"></a>
<a id="agroup__fpga__interface_html_gga0bbacdfdac79bace1786bb2a1627bb1eac1b036277b07dfdef1dd1c3e1a299131"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructfpga__driver__api_html"></a>
<a id="astructfpga__driver__api_html_a0dedc3ce6e6ac23b9907af1ebbddaa56"></a>
<a id="astructfpga__driver__api_html_a1a56d32b7e1c9931b7ddca9f802baecc"></a>
<a id="astructfpga__driver__api_html_a89de57caf9882098e9c5f42f35bff2a3"></a>
<a id="astructfpga__driver__api_html_aa2107eb303cc2e538441ba1058630ab4"></a>
<a id="astructfpga__driver__api_html_ab3b316a07f35610b5bb00cd6c89fa0f1"></a>
<a id="astructfpga__driver__api_html_aee587fbff9464efc2ab64c6187346d28"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2021 Antmicro <www.antmicro.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FPGA_H_
#define ZEPHYR_INCLUDE_DRIVERS_FPGA_H_

#include <errno.h>

#include <zephyr/types.h>
#include <zephyr/sys/util.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


enum FPGA_status {
        FPGA_STATUS_INACTIVE,
        FPGA_STATUS_ACTIVE
};


typedef enum FPGA_status (*fpga_api_get_status)(const struct device *dev);

typedef int (*fpga_api_load)(const struct device *dev, uint32_t *image_ptr,
                             uint32_t img_size);

typedef int (*fpga_api_reset)(const struct device *dev);

typedef int (*fpga_api_on)(const struct device *dev);

typedef int (*fpga_api_off)(const struct device *dev);

typedef const char *(*fpga_api_get_info)(const struct device *dev);

__subsystem struct fpga_driver_api {
        fpga_api_get_status get_status;
        fpga_api_reset reset;
        fpga_api_load load;
        fpga_api_on on;
        fpga_api_off off;
        fpga_api_get_info get_info;
};


static inline enum FPGA_status fpga_get_status(const struct device *dev)
{
        const struct fpga_driver_api *api = DEVICE_API_GET(fpga, dev);

        if (api->get_status == NULL) {
                /* assume it can never be reprogrammed if it
                 * doesn't support the get_status callback
                 */
                return FPGA_STATUS_INACTIVE;
        }

        return api->get_status(dev);
}

static inline int fpga_reset(const struct device *dev)
{
        const struct fpga_driver_api *api = DEVICE_API_GET(fpga, dev);

        if (api->reset == NULL) {
                return -ENOTSUP;
        }

        return api->reset(dev);
}

static inline int fpga_load(const struct device *dev, uint32_t *image_ptr,
                            uint32_t img_size)
{
        const struct fpga_driver_api *api = DEVICE_API_GET(fpga, dev);

        if (api->load == NULL) {
                return -ENOTSUP;
        }

        return api->load(dev, image_ptr, img_size);
}

static inline int fpga_on(const struct device *dev)
{
        const struct fpga_driver_api *api = DEVICE_API_GET(fpga, dev);

        if (api->on == NULL) {
                return -ENOTSUP;
        }

        return api->on(dev);
}

#define FPGA_GET_INFO_DEFAULT "n/a"

static inline const char *fpga_get_info(const struct device *dev)
{
        const struct fpga_driver_api *api = DEVICE_API_GET(fpga, dev);

        if (api->get_info == NULL) {
                return FPGA_GET_INFO_DEFAULT;
        }

        return api->get_info(dev);
}

static inline int fpga_off(const struct device *dev)
{
        const struct fpga_driver_api *api = DEVICE_API_GET(fpga, dev);

        if (api->off == NULL) {
                return -ENOTSUP;
        }

        return api->off(dev);
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_FPGA_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Antmicro <www.antmicro.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 131 行

如果不支持 `get_status` 回调，则假定它永远不能重新配置（Reprogram）。

### 注释 3：原第 246 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FPGA_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P006_zephyr__drivers__fpga.h_头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [FPGA_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga0bbacdfdac79bace1786bb2a1627bb1e)
- [FPGA_STATUS_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gga0bbacdfdac79bace1786bb2a1627bb1ea46571663477ca2df50b24cf93a5e2441)
- [FPGA_STATUS_ACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gga0bbacdfdac79bace1786bb2a1627bb1eac1b036277b07dfdef1dd1c3e1a299131)
- [fpga_api_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga02d71e7a82f446220d67664d4cc7a5c9)
- [device](../device_reference/P002_设备对象结构.md)
- [fpga_api_load](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga9860c64bbc2cfb89df9b51da655691b6)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [fpga_api_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga3c53b90b9d0b50c44c01a534c61e9212)
- [fpga_api_on](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#gaf3e8ea5d443fd09352e2b63f82a459be)
- [fpga_api_off](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga872a8d75bb46de50a41b56170804ed27)
- [fpga_driver_api](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md)
- [get_status](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md#aee587fbff9464efc2ab64c6187346d28)
- [reset](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md#ab3b316a07f35610b5bb00cd6c89fa0f1)
- [load](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md#a1a56d32b7e1c9931b7ddca9f802baecc)
- [on](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md#a0dedc3ce6e6ac23b9907af1ebbddaa56)
- [off](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md#a89de57caf9882098e9c5f42f35bff2a3)
- [fpga_api_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga24fd6ce4832b960b79914f42010774aa)
- [get_info](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md#aa2107eb303cc2e538441ba1058630ab4)
- [fpga_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga1a1e78a46df9f4bd374cf5ecc2449360)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [fpga_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gadfc8d6c24cb1b1640393017a462011c9)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [fpga_load](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#ga1cace6c7cc44705bf861d7aa5e863e16)
- [fpga_on](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gad9093bd96c6a62cd958718d1e01e3f37)
- [fpga_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gab887999e8728bcc335a784afbdbbee8f)
- [FPGA_GET_INFO_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gab41c04907be508f62e8df813d633b34b)
- [fpga_off](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html#gaa161c7a7006db24793c1a1ecdea25b5c)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [fpga_driver_api::on](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md#a0dedc3ce6e6ac23b9907af1ebbddaa56)
- [fpga_driver_api::load](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md#a1a56d32b7e1c9931b7ddca9f802baecc)
- [fpga_driver_api::off](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md#a89de57caf9882098e9c5f42f35bff2a3)
- [fpga_driver_api::get_info](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md#aa2107eb303cc2e538441ba1058630ab4)
- [fpga_driver_api::reset](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md#ab3b316a07f35610b5bb00cd6c89fa0f1)
- [fpga_driver_api::get_status](../peripheral_bus_storage_model_reference/P018_fpga_driver_api_结构体.md#aee587fbff9464efc2ab64c6187346d28)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P005_zephyr__drivers__espi_saf.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__lin.h_头文件源码.md)
