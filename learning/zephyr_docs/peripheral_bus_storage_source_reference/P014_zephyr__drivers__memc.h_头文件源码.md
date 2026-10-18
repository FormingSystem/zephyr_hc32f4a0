---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-14
title: zephyr__drivers__memc.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/memc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr__drivers__memc.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/memc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P014_zephyr__drivers__memc.h_头文件参考.md)。

## 14.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00039"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
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
<a id="l00152"></a>
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
<a id="l00166"></a>
<a id="foldopen00179"></a>
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
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
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
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a48c6030c2e7d1d05ace7c708dda11949"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__memc__interface__backend_html_ga0311584e35d2ad24e92bb9999ca76510"></a>
<a id="agroup__memc__interface__backend_html_ga1e7138177b931238a4f09a58bf4c765a"></a>
<a id="agroup__memc__interface__backend_html_ga2c33e74e81bbc4aaaef0a577737ebdcb"></a>
<a id="agroup__memc__interface__backend_html_gac495599a886be46a47dc22f6aaedcfb8"></a>
<a id="agroup__memc__interface__backend_html_gada700c92c23e9a59eea6012594e8866d"></a>
<a id="agroup__memc__interface_html_ga02bca9fd387ac26841394a73d51dbe7e"></a>
<a id="agroup__memc__interface_html_ga7b766a76f3bffe8b89eafb93c4f16cae"></a>
<a id="agroup__memc__interface_html_ga8c08116a54ccb2765822ba20ba77ed39"></a>
<a id="agroup__memc__interface_html_gac48976493664e5c68c5b6a90ae8dd960"></a>
<a id="agroup__memc__interface_html_gaf797d9df098f75ce12e69223f759364b"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astring_8h_html"></a>
<a id="astring_8h_html_af0f01bffcd16daa9143f6014d10a25ad"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructmemc__driver__api_html"></a>
<a id="astructmemc__driver__api_html_a9c6376bec867625f3569ccf2bf379a7b"></a>
<a id="astructmemc__driver__api_html_ad5ac94768979a4e6100cc26868ef14aa"></a>
<a id="astructmemc__driver__api_html_af5091fa43e0227b5038a6f7eae649e72"></a>
<a id="astructmemc__driver__api_html_af64136ddf8e8f569eaf7882e28a5f8c8"></a>
<a id="astructmemc__driver__api_html_afaf23ae48edfd05fbe3366a0750ecfdd"></a>

```c
/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MEMC_H_
#define ZEPHYR_INCLUDE_DRIVERS_MEMC_H_


#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/device.h>
#include <string.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef int (*memc_api_read)(const struct device *dev, uint32_t addr, uint8_t *data, size_t len);

typedef int (*memc_api_write)(const struct device *dev, uint32_t addr, const uint8_t *data,
                              size_t len);

typedef int (*memc_api_get_size)(const struct device *dev, uint64_t *size);

typedef int (*memc_api_read_id)(const struct device *dev, uint8_t *id, size_t len);

typedef void *(*memc_api_get_mem_base)(const struct device *dev);

__subsystem struct memc_driver_api {
        memc_api_read read;
        memc_api_write write;
        memc_api_get_mem_base get_mem_base;
        memc_api_get_size get_size;
        memc_api_read_id read_id;
};


__syscall int memc_read(const struct device *dev, uint32_t addr, uint8_t *data, size_t len);

static inline int z_impl_memc_read(const struct device *dev, uint32_t addr, uint8_t *data,
                                   size_t len)
{
        if (!DEVICE_API_IS(memc, dev)) {
                return -ENOTSUP;
        }

        const struct memc_driver_api *api = DEVICE_API_GET(memc, dev);

        if (api->get_mem_base != NULL) {
                void *base = api->get_mem_base(dev);

                if (base != NULL) {
                        memcpy(data, (const uint8_t *)base + addr, len);
                        return 0;
                }
        }

        if (api->read != NULL) {
                return api->read(dev, addr, data, len);
        }

        return -ENOTSUP;
}

__syscall int memc_write(const struct device *dev, uint32_t addr, const uint8_t *data, size_t len);

static inline int z_impl_memc_write(const struct device *dev, uint32_t addr, const uint8_t *data,
                                    size_t len)
{
        if (!DEVICE_API_IS(memc, dev)) {
                return -ENOTSUP;
        }

        const struct memc_driver_api *api = DEVICE_API_GET(memc, dev);

        if (api->get_mem_base != NULL) {
                void *base = api->get_mem_base(dev);

                if (base != NULL) {
                        memcpy((uint8_t *)base + addr, data, len);
                        return 0;
                }
        }

        if (api->write != NULL) {
                return api->write(dev, addr, data, len);
        }

        return -ENOTSUP;
}

static inline void *memc_get_mem_base(const struct device *dev)
{
        if (!DEVICE_API_IS(memc, dev)) {
                return NULL;
        }

        const struct memc_driver_api *api = DEVICE_API_GET(memc, dev);

        if (api->get_mem_base == NULL) {
                return NULL;
        }

        return api->get_mem_base(dev);
}

__syscall int memc_get_size(const struct device *dev, uint64_t *size);

static inline int z_impl_memc_get_size(const struct device *dev, uint64_t *size)
{
        if (!DEVICE_API_IS(memc, dev)) {
                return -ENOTSUP;
        }

        const struct memc_driver_api *api = DEVICE_API_GET(memc, dev);

        if (api->get_size == NULL) {
                return -ENOTSUP;
        }

        return api->get_size(dev, size);
}

__syscall int memc_read_id(const struct device *dev, uint8_t *id, size_t len);

static inline int z_impl_memc_read_id(const struct device *dev, uint8_t *id, size_t len)
{
        if (!DEVICE_API_IS(memc, dev)) {
                return -ENOTSUP;
        }

        const struct memc_driver_api *api = DEVICE_API_GET(memc, dev);

        if (api->read_id == NULL) {
                return -ENOTSUP;
        }

        return api->read_id(dev, id, len);
}


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/memc.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_MEMC_H_ */
```

## 14.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 258 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MEMC_H_`。

## 14.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P014_zephyr__drivers__memc.h_头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)
- [memc_api_read](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga1e7138177b931238a4f09a58bf4c765a)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [memc_api_write](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#gac495599a886be46a47dc22f6aaedcfb8)
- [memc_api_get_size](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga2c33e74e81bbc4aaaef0a577737ebdcb)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [memc_api_read_id](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#gada700c92c23e9a59eea6012594e8866d)
- [memc_driver_api](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md)
- [read](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md#af5091fa43e0227b5038a6f7eae649e72)
- [write](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md#af64136ddf8e8f569eaf7882e28a5f8c8)
- [memc_api_get_mem_base](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface__backend.html#ga0311584e35d2ad24e92bb9999ca76510)
- [get_mem_base](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md#a9c6376bec867625f3569ccf2bf379a7b)
- [get_size](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md#ad5ac94768979a4e6100cc26868ef14aa)
- [read_id](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md#afaf23ae48edfd05fbe3366a0750ecfdd)
- [memc_read](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#ga7b766a76f3bffe8b89eafb93c4f16cae)
- [DEVICE_API_IS](../device_reference/P007_设备模型头文件参考.md#a48c6030c2e7d1d05ace7c708dda11949)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [memcpy](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#af0f01bffcd16daa9143f6014d10a25ad)
- [memc_write](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#ga8c08116a54ccb2765822ba20ba77ed39)
- [memc_get_mem_base](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#gac48976493664e5c68c5b6a90ae8dd960)
- [memc_get_size](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#ga02bca9fd387ac26841394a73d51dbe7e)
- [memc_read_id](https://docs.zephyrproject.org/latest/doxygen/html/group__memc__interface.html#gaf797d9df098f75ce12e69223f759364b)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [memc_driver_api::get_mem_base](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md#a9c6376bec867625f3569ccf2bf379a7b)
- [memc_driver_api::get_size](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md#ad5ac94768979a4e6100cc26868ef14aa)
- [memc_driver_api::read](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md#af5091fa43e0227b5038a6f7eae649e72)
- [memc_driver_api::write](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md#af64136ddf8e8f569eaf7882e28a5f8c8)
- [memc_driver_api::read_id](../peripheral_bus_storage_model_reference/P033_memc_driver_api_结构体.md#afaf23ae48edfd05fbe3366a0750ecfdd)

---

[上一章](P013_zephyr__pmci__mctp__mctp_usb.h_头文件源码.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__sd__sd_spec.h_头文件源码.md)
