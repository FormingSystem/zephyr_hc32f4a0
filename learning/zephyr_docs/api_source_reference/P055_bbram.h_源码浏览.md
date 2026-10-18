---
id: learning.zephyr-docs.api-source-reference.page-55
title: bbram.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bbram_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_bbram.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bbram_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bbram_8h.html)。

## 55.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00037"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00083"></a>
<a id="l00087"></a>
<a id="l00091"></a>
<a id="l00095"></a>
<a id="l00099"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00108"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00227"></a>
<a id="l00228"></a>
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
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__bbram__interface__backend_html_ga1b111ae421791b9544777c1bab5e2a02"></a>
<a id="agroup__bbram__interface__backend_html_ga8b06a1b3bb9b524597804dd268904881"></a>
<a id="agroup__bbram__interface__backend_html_ga99adefcb89ab80d8b5e24b8ffad8f43e"></a>
<a id="agroup__bbram__interface__backend_html_gaa6edc8a61529edad90de2e6fff619fdf"></a>
<a id="agroup__bbram__interface__backend_html_gac23658302662587043f3587080f798fe"></a>
<a id="agroup__bbram__interface__backend_html_gacfa586f705c520a6a05638a2e289fe50"></a>
<a id="agroup__bbram__interface_html_ga08a2c565ba0ec6ac5894a718a652eec2"></a>
<a id="agroup__bbram__interface_html_ga51007eed4820aed341d20e4562607564"></a>
<a id="agroup__bbram__interface_html_ga7164969f308616696a9ab71a4d19b70b"></a>
<a id="agroup__bbram__interface_html_ga8fc2a647bda90e96f866514300180a96"></a>
<a id="agroup__bbram__interface_html_ga948ed0a7d3824f950ad46b99ba3d86f4"></a>
<a id="agroup__bbram__interface_html_ga9ef786b0fbac3f8523be2bb87b7cff7b"></a>
<a id="agroup__bbram__interface_html_gab6bdb4a1cba88ca645c256366a696bdd"></a>
<a id="agroup__bbram__interface_html_gadc0243187b853832b08af36c9baf9cb0"></a>
<a id="agroup__bbram__interface_html_gae2b89f8a44e38fe7df2219397bad139b"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructbbram__driver__api_html"></a>
<a id="astructbbram__driver__api_html_a04c9f9487d35a0c2d264d033ef266fc7"></a>
<a id="astructbbram__driver__api_html_a15809ed9c49ade6de1ddbc7e48072b12"></a>
<a id="astructbbram__driver__api_html_a4c3813853e2364109ea1b481277f2816"></a>
<a id="astructbbram__driver__api_html_a50a91db769c65d4e9dceb027c5bc956d"></a>
<a id="astructbbram__driver__api_html_a6df89dfb1ce05bc557286bc894751702"></a>
<a id="astructbbram__driver__api_html_a937578d674e8ed1e26026aea7428e616"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>

```c
/*
 * Copyright (c) 2021 Google Inc
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_BBRAM_H
#define ZEPHYR_INCLUDE_DRIVERS_BBRAM_H

#include <errno.h>

#include <zephyr/device.h>


#ifdef __cplusplus
extern "C" {
#endif


typedef int (*bbram_api_check_invalid_t)(const struct device *dev);

typedef int (*bbram_api_check_standby_power_t)(const struct device *dev);

typedef int (*bbram_api_check_power_t)(const struct device *dev);

typedef int (*bbram_api_get_size_t)(const struct device *dev, size_t *size);

typedef int (*bbram_api_read_t)(const struct device *dev, size_t offset, size_t size,
                                uint8_t *data);

typedef int (*bbram_api_write_t)(const struct device *dev, size_t offset, size_t size,
                                 const uint8_t *data);

__subsystem struct bbram_driver_api {
        bbram_api_check_invalid_t check_invalid;
        bbram_api_check_standby_power_t check_standby_power;
        bbram_api_check_power_t check_power;
        bbram_api_get_size_t get_size;
        bbram_api_read_t read;
        bbram_api_write_t write;
};


__syscall int bbram_check_invalid(const struct device *dev);

static inline int z_impl_bbram_check_invalid(const struct device *dev)
{
        const struct bbram_driver_api *api = DEVICE_API_GET(bbram, dev);

        if (!api->check_invalid) {
                return -ENOTSUP;
        }

        return api->check_invalid(dev);
}

__syscall int bbram_check_standby_power(const struct device *dev);

static inline int z_impl_bbram_check_standby_power(const struct device *dev)
{
        const struct bbram_driver_api *api = DEVICE_API_GET(bbram, dev);

        if (!api->check_standby_power) {
                return -ENOTSUP;
        }

        return api->check_standby_power(dev);
}

__syscall int bbram_check_power(const struct device *dev);

static inline int z_impl_bbram_check_power(const struct device *dev)
{
        const struct bbram_driver_api *api = DEVICE_API_GET(bbram, dev);

        if (!api->check_power) {
                return -ENOTSUP;
        }

        return api->check_power(dev);
}

__syscall int bbram_get_size(const struct device *dev, size_t *size);

static inline int z_impl_bbram_get_size(const struct device *dev, size_t *size)
{
        const struct bbram_driver_api *api = DEVICE_API_GET(bbram, dev);

        if (!api->get_size) {
                return -ENOTSUP;
        }

        return api->get_size(dev, size);
}

__syscall int bbram_read(const struct device *dev, size_t offset, size_t size,
                         uint8_t *data);

static inline int z_impl_bbram_read(const struct device *dev, size_t offset,
                                    size_t size, uint8_t *data)
{
        const struct bbram_driver_api *api = DEVICE_API_GET(bbram, dev);

        if (!api->read) {
                return -ENOTSUP;
        }

        return api->read(dev, offset, size, data);
}

__syscall int bbram_write(const struct device *dev, size_t offset, size_t size,
                          const uint8_t *data);

static inline int z_impl_bbram_write(const struct device *dev, size_t offset,
                                     size_t size, const uint8_t *data)
{
        const struct bbram_driver_api *api = DEVICE_API_GET(bbram, dev);

        if (!api->write) {
                return -ENOTSUP;
        }

        return api->write(dev, offset, size, data);
}

int bbram_emul_set_invalid(const struct device *dev, bool is_invalid);

int bbram_emul_set_standby_power_state(const struct device *dev, bool failure);

int bbram_emul_set_power_state(const struct device *dev, bool failure);

#ifdef __cplusplus
}
#endif


#include <zephyr/syscalls/bbram.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_BBRAM_H */
```

## 55.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Google Inc。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 285 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_BBRAM_H`。

## 55.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bbram_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [bbram_api_check_invalid_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#gac23658302662587043f3587080f798fe)
- [device](../device_reference/P002_设备对象结构.md)
- [bbram_api_check_standby_power_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#ga99adefcb89ab80d8b5e24b8ffad8f43e)
- [bbram_api_check_power_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#gaa6edc8a61529edad90de2e6fff619fdf)
- [bbram_api_get_size_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#gacfa586f705c520a6a05638a2e289fe50)
- [bbram_api_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#ga8b06a1b3bb9b524597804dd268904881)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [bbram_api_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html#ga1b111ae421791b9544777c1bab5e2a02)
- [bbram_driver_api](../driver_model_reference/P024_电池备份RAM驱动接口.md)
- [check_invalid](../driver_model_reference/P024_电池备份RAM驱动接口.md#a04c9f9487d35a0c2d264d033ef266fc7)
- [check_standby_power](../driver_model_reference/P024_电池备份RAM驱动接口.md#a4c3813853e2364109ea1b481277f2816)
- [check_power](../driver_model_reference/P024_电池备份RAM驱动接口.md#a6df89dfb1ce05bc557286bc894751702)
- [get_size](../driver_model_reference/P024_电池备份RAM驱动接口.md#a15809ed9c49ade6de1ddbc7e48072b12)
- [read](../driver_model_reference/P024_电池备份RAM驱动接口.md#a50a91db769c65d4e9dceb027c5bc956d)
- [write](../driver_model_reference/P024_电池备份RAM驱动接口.md#a937578d674e8ed1e26026aea7428e616)
- [bbram_check_invalid](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga7164969f308616696a9ab71a4d19b70b)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [bbram_check_standby_power](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga948ed0a7d3824f950ad46b99ba3d86f4)
- [bbram_check_power](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga8fc2a647bda90e96f866514300180a96)
- [bbram_get_size](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#gab6bdb4a1cba88ca645c256366a696bdd)
- [bbram_read](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga9ef786b0fbac3f8523be2bb87b7cff7b)
- [bbram_write](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga51007eed4820aed341d20e4562607564)
- [bbram_emul_set_invalid](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#gae2b89f8a44e38fe7df2219397bad139b)
- [bbram_emul_set_standby_power_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga08a2c565ba0ec6ac5894a718a652eec2)
- [bbram_emul_set_power_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#gadc0243187b853832b08af36c9baf9cb0)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [bbram_driver_api::check_invalid](../driver_model_reference/P024_电池备份RAM驱动接口.md#a04c9f9487d35a0c2d264d033ef266fc7)
- [bbram_driver_api::get_size](../driver_model_reference/P024_电池备份RAM驱动接口.md#a15809ed9c49ade6de1ddbc7e48072b12)
- [bbram_driver_api::check_standby_power](../driver_model_reference/P024_电池备份RAM驱动接口.md#a4c3813853e2364109ea1b481277f2816)
- [bbram_driver_api::read](../driver_model_reference/P024_电池备份RAM驱动接口.md#a50a91db769c65d4e9dceb027c5bc956d)
- [bbram_driver_api::check_power](../driver_model_reference/P024_电池备份RAM驱动接口.md#a6df89dfb1ce05bc557286bc894751702)
- [bbram_driver_api::write](../driver_model_reference/P024_电池备份RAM驱动接口.md#a937578d674e8ed1e26026aea7428e616)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)

---

[上一章](P054_basicmath_f16.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P056_bcm2712-pinctrl.h_源码浏览.md)
