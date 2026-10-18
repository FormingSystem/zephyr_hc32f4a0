---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-22
title: zephyr__drivers__ps2.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ps2_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr__drivers__ps2.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ps2_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P022_zephyr__drivers__ps2.h_头文件参考.md)。

## 22.1\_原始可见代码（Source Code）

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
<a id="l00037"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00051"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__ps2__interface__backend_html_ga3d5a1b7e613e0e2b1a28689b9ab52ca5"></a>
<a id="agroup__ps2__interface__backend_html_ga7fb2edbebe2523efde6c7f73bffb850a"></a>
<a id="agroup__ps2__interface__backend_html_gaaa51cb5cf5f5d7560c35374561746f6d"></a>
<a id="agroup__ps2__interface__backend_html_gaad5d2a31e2f4768953b6d611364e748c"></a>
<a id="agroup__ps2__interface__backend_html_gaf7a935b2e1debd819792dbb02bd84ee2"></a>
<a id="agroup__ps2__interface_html_ga8d6da9b966432defb0cd482003c11f15"></a>
<a id="agroup__ps2__interface_html_ga9568487018f4ef972eb463ea2098e254"></a>
<a id="agroup__ps2__interface_html_gab91b1efe1f07d409607922f4eb87b221"></a>
<a id="agroup__ps2__interface_html_gad7cf29301681fac0d2a359d425a13b5f"></a>
<a id="agroup__ps2__interface_html_gade1a470c3583e465d6a8f24a28611397"></a>
<a id="agroup__ps2__interface_html_gae291cb991ae9525552fdb52c2fa4ac5e"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructps2__driver__api_html"></a>
<a id="astructps2__driver__api_html_a485227d96921b73da2041225535be74c"></a>
<a id="astructps2__driver__api_html_ab0cdb648761d2de1f1d1b719f9b94005"></a>
<a id="astructps2__driver__api_html_abe4d10c3ad967796943d95f75c659d4d"></a>
<a id="astructps2__driver__api_html_abfaf41cc47cabb2d1710584586e5b93c"></a>
<a id="astructps2__driver__api_html_add947b91f9ca9bac20fac2fbb47b87e4"></a>

```c
/*
 * Copyright (c) 2019 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_PS2_H_
#define ZEPHYR_INCLUDE_DRIVERS_PS2_H_

#include <errno.h>
#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef void (*ps2_callback_t)(const struct device *dev, uint8_t data);


typedef int (*ps2_config_t)(const struct device *dev,
                            ps2_callback_t callback_isr);

typedef int (*ps2_read_t)(const struct device *dev, uint8_t *value);

typedef int (*ps2_write_t)(const struct device *dev, uint8_t value);

typedef int (*ps2_disable_callback_t)(const struct device *dev);

typedef int (*ps2_enable_callback_t)(const struct device *dev);

__subsystem struct ps2_driver_api {
        ps2_config_t config;
        ps2_read_t read;
        ps2_write_t write;
        ps2_disable_callback_t disable_callback;
        ps2_enable_callback_t enable_callback;
};


__syscall int ps2_config(const struct device *dev,
                         ps2_callback_t callback_isr);

static inline int z_impl_ps2_config(const struct device *dev,
                                    ps2_callback_t callback_isr)
{
        return DEVICE_API_GET(ps2, dev)->config(dev, callback_isr);
}

__syscall int ps2_write(const struct device *dev, uint8_t value);

static inline int z_impl_ps2_write(const struct device *dev, uint8_t value)
{
        return DEVICE_API_GET(ps2, dev)->write(dev, value);
}

__syscall int ps2_read(const struct device *dev,  uint8_t *value);

static inline int z_impl_ps2_read(const struct device *dev, uint8_t *value)
{
        return DEVICE_API_GET(ps2, dev)->read(dev, value);
}

__syscall int ps2_enable_callback(const struct device *dev);

static inline int z_impl_ps2_enable_callback(const struct device *dev)
{
        const struct ps2_driver_api *api = DEVICE_API_GET(ps2, dev);

        if (api->enable_callback == NULL) {
                return -ENOSYS;
        }

        return api->enable_callback(dev);
}

__syscall int ps2_disable_callback(const struct device *dev);

static inline int z_impl_ps2_disable_callback(const struct device *dev)
{
        const struct ps2_driver_api *api = DEVICE_API_GET(ps2, dev);

        if (api->disable_callback == NULL) {
                return -ENOSYS;
        }

        return api->disable_callback(dev);
}

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/ps2.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_PS2_H_ */
```

## 22.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 195 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PS2_H_`。

## 22.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P022_zephyr__drivers__ps2.h_头文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [ps2_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gad7cf29301681fac0d2a359d425a13b5f)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [ps2_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#ga7fb2edbebe2523efde6c7f73bffb850a)
- [ps2_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#ga3d5a1b7e613e0e2b1a28689b9ab52ca5)
- [ps2_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaf7a935b2e1debd819792dbb02bd84ee2)
- [ps2_disable_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaaa51cb5cf5f5d7560c35374561746f6d)
- [ps2_enable_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaad5d2a31e2f4768953b6d611364e748c)
- [ps2_driver_api](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md)
- [config](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md#abe4d10c3ad967796943d95f75c659d4d)
- [read](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md#abfaf41cc47cabb2d1710584586e5b93c)
- [write](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md#add947b91f9ca9bac20fac2fbb47b87e4)
- [disable_callback](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md#a485227d96921b73da2041225535be74c)
- [enable_callback](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md#ab0cdb648761d2de1f1d1b719f9b94005)
- [ps2_config](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#ga8d6da9b966432defb0cd482003c11f15)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ps2_write](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gae291cb991ae9525552fdb52c2fa4ac5e)
- [ps2_read](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gab91b1efe1f07d409607922f4eb87b221)
- [ps2_enable_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#ga9568487018f4ef972eb463ea2098e254)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [ps2_disable_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface.html#gade1a470c3583e465d6a8f24a28611397)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [ps2_driver_api::disable_callback](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md#a485227d96921b73da2041225535be74c)
- [ps2_driver_api::enable_callback](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md#ab0cdb648761d2de1f1d1b719f9b94005)
- [ps2_driver_api::config](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md#abe4d10c3ad967796943d95f75c659d4d)
- [ps2_driver_api::read](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md#abfaf41cc47cabb2d1710584586e5b93c)
- [ps2_driver_api::write](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md#add947b91f9ca9bac20fac2fbb47b87e4)

---

[上一章](P021_zephyr__drivers__peci.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__drivers__psi5__psi5.h_头文件源码.md)
