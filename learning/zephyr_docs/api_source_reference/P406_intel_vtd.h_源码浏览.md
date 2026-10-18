---
id: learning.zephyr-docs.api-source-reference.page-406
title: intel_vtd.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第406章\_intel\_vtd.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html)。

## 406.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
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
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00086"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="foldopen00151"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="foldopen00166"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="foldopen00181"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="foldopen00187"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__pcie__host__msi__interface_html_ga9ede6a7a472ee62f0975256a1b5f1231"></a>
<a id="aintel__vtd_8h_html_a0118f224100f721a508ce00c3ae99698"></a>
<a id="aintel__vtd_8h_html_a06190d6273d0adeb92e9e4e4fa79d9b4"></a>
<a id="aintel__vtd_8h_html_a0a2e483fe9159a46d6265b257841f43a"></a>
<a id="aintel__vtd_8h_html_a214bd683e7331adbe5afbca41e3a6bc9"></a>
<a id="aintel__vtd_8h_html_a342e4745949ed1bd50b4d51de482be57"></a>
<a id="aintel__vtd_8h_html_a3bded96a42bec41476ff6bc9f75676b4"></a>
<a id="aintel__vtd_8h_html_a3cc5ff5183e80aeb18115d8b5a541546"></a>
<a id="aintel__vtd_8h_html_a4645558c4f9e461e86e6d0caf96311ad"></a>
<a id="aintel__vtd_8h_html_a622083e8841c3899ca7b7156f526581f"></a>
<a id="aintel__vtd_8h_html_a63733309814847ba4204776e8ace9a85"></a>
<a id="aintel__vtd_8h_html_a76d5a655a925c9ec9536e6c906c2192e"></a>
<a id="aintel__vtd_8h_html_a82018e41e5bbb12f98c16b0d416596fe"></a>
<a id="aintel__vtd_8h_html_a87b1cea7c86d724da0c379bfd3742879"></a>
<a id="aintel__vtd_8h_html_a944bfa2dc643fd3ff182eee12d836ae5"></a>
<a id="aintel__vtd_8h_html_aadb69e257884026693109510e20dc2b4"></a>
<a id="aintel__vtd_8h_html_ab067e306959a0774ee5e896eafab2132"></a>
<a id="aintel__vtd_8h_html_ab7b8ad9dbee740c9e97021853f1131fc"></a>
<a id="aintel__vtd_8h_html_ae81918a2c81e03cc4e02603781e8ca21"></a>
<a id="aintel__vtd_8h_html_af3ddf5e22fcb4956e4887e1982fae28e"></a>
<a id="aintel__vtd_8h_html_afefa59b2064053d90445127da9b64bfb"></a>
<a id="amsi_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructvtd__driver__api_html"></a>
<a id="astructvtd__driver__api_html_a03236811cfc87b4653ba1a2f53bc50a1"></a>
<a id="astructvtd__driver__api_html_a3177c806bd86ebe4dc6c94141c9d5f04"></a>
<a id="astructvtd__driver__api_html_a39157ec0077a20a900bbe19f3cc8d1b1"></a>
<a id="astructvtd__driver__api_html_a97f93762584ea000a149ded0d726a993"></a>
<a id="astructvtd__driver__api_html_aac4ab98b9bf8a557cec22c685433888c"></a>
<a id="astructvtd__driver__api_html_ac03cd6690017568b51d1b4bedd1fea09"></a>
<a id="astructvtd__driver__api_html_ac2fbdcfe7bcb0c9ef548aefe1c80b96b"></a>
<a id="astructvtd__driver__api_html_ac67dacb59216e44e55c832a26b87854f"></a>
<a id="astructvtd__driver__api_html_acc5af4aaaeed8abb8768d21767c67c58"></a>
<a id="astructvtd__driver__api_html_adf1c688b60ef445581dee2344a48c8b6"></a>

```c
/*
 * Copyright (c) 2020 Intel Corporation
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTEL_VTD_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTEL_VTD_H_

#include <zephyr/drivers/pcie/msi.h>

typedef int (*vtd_alloc_entries_f)(const struct device *dev,
                                   uint8_t n_entries);

typedef uint32_t (*vtd_remap_msi_f)(const struct device *dev,
                                    msi_vector_t *vector,
                                    uint8_t n_vector);

typedef int (*vtd_remap_f)(const struct device *dev,
                           uint8_t irte_idx,
                           uint16_t vector,
                           uint32_t flags,
                           uint16_t src_id);

typedef int (*vtd_set_irte_vector_f)(const struct device *dev,
                                     uint8_t irte_idx,
                                     uint16_t vector);

typedef int (*vtd_get_irte_by_vector_f)(const struct device *dev,
                                        uint16_t vector);

typedef uint16_t (*vtd_get_irte_vector_f)(const struct device *dev,
                                          uint8_t irte_idx);

typedef int (*vtd_set_irte_irq_f)(const struct device *dev,
                                  uint8_t irte_idx,
                                  unsigned int irq);

typedef int (*vtd_get_irte_by_irq_f)(const struct device *dev,
                                     unsigned int irq);

typedef void (*vtd_set_irte_msi_f)(const struct device *dev,
                                   uint8_t irte_idx,
                                   bool msi);

typedef bool (*vtd_irte_is_msi_f)(const struct device *dev,
                                  uint8_t irte_idx);

__subsystem struct vtd_driver_api {
        vtd_alloc_entries_f allocate_entries;
        vtd_remap_msi_f remap_msi;
        vtd_remap_f remap;
        vtd_set_irte_vector_f set_irte_vector;
        vtd_get_irte_by_vector_f get_irte_by_vector;
        vtd_get_irte_vector_f get_irte_vector;
        vtd_set_irte_irq_f set_irte_irq;
        vtd_get_irte_by_irq_f get_irte_by_irq;
        vtd_set_irte_msi_f set_irte_msi;
        vtd_irte_is_msi_f irte_is_msi;
};

static inline int vtd_allocate_entries(const struct device *dev,
                                       uint8_t n_entries)
{
        return DEVICE_API_GET(vtd, dev)->allocate_entries(dev, n_entries);
}

static inline uint32_t vtd_remap_msi(const struct device *dev,
                                     msi_vector_t *vector,
                                     uint8_t n_vector)
{
        return DEVICE_API_GET(vtd, dev)->remap_msi(dev, vector, n_vector);
}

static inline int vtd_remap(const struct device *dev,
                            uint8_t irte_idx,
                            uint16_t vector,
                            uint32_t flags,
                            uint16_t src_id)
{
        return DEVICE_API_GET(vtd, dev)->remap(dev, irte_idx, vector, flags, src_id);
}

static inline int vtd_set_irte_vector(const struct device *dev,
                                      uint8_t irte_idx,
                                      uint16_t vector)
{
        return DEVICE_API_GET(vtd, dev)->set_irte_vector(dev, irte_idx, vector);
}

static inline int vtd_get_irte_by_vector(const struct device *dev,
                                         uint16_t vector)
{
        return DEVICE_API_GET(vtd, dev)->get_irte_by_vector(dev, vector);
}

static inline uint16_t vtd_get_irte_vector(const struct device *dev,
                                           uint8_t irte_idx)
{
        return DEVICE_API_GET(vtd, dev)->get_irte_vector(dev, irte_idx);
}

static inline int vtd_set_irte_irq(const struct device *dev,
                                   uint8_t irte_idx,
                                   unsigned int irq)
{
        return DEVICE_API_GET(vtd, dev)->set_irte_irq(dev, irte_idx, irq);
}

static inline int vtd_get_irte_by_irq(const struct device *dev,
                                      unsigned int irq)
{
        return DEVICE_API_GET(vtd, dev)->get_irte_by_irq(dev, irq);
}

static inline void vtd_set_irte_msi(const struct device *dev,
                                    uint8_t irte_idx,
                                    bool msi)
{
        DEVICE_API_GET(vtd, dev)->set_irte_msi(dev, irte_idx, msi);
}

static inline bool vtd_irte_is_msi(const struct device *dev,
                                   uint8_t irte_idx)
{
        return DEVICE_API_GET(vtd, dev)->irte_is_msi(dev, irte_idx);
}


#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTEL_VTD_H_ */
```

## 406.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 201 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_INTEL_VTD_H_`。

## 406.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html)
- [zephyr/drivers/pcie/msi.h](https://docs.zephyrproject.org/latest/doxygen/html/msi_8h.html)
- [vtd_alloc_entries_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a3bded96a42bec41476ff6bc9f75676b4)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [vtd_remap_msi_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#aadb69e257884026693109510e20dc2b4)
- [msi_vector_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga9ede6a7a472ee62f0975256a1b5f1231)
- [vtd_remap_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#afefa59b2064053d90445127da9b64bfb)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [vtd_set_irte_vector_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a06190d6273d0adeb92e9e4e4fa79d9b4)
- [vtd_get_irte_by_vector_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a944bfa2dc643fd3ff182eee12d836ae5)
- [vtd_get_irte_vector_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#af3ddf5e22fcb4956e4887e1982fae28e)
- [vtd_set_irte_irq_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a63733309814847ba4204776e8ace9a85)
- [vtd_get_irte_by_irq_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a0a2e483fe9159a46d6265b257841f43a)
- [vtd_set_irte_msi_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a0118f224100f721a508ce00c3ae99698)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [vtd_irte_is_msi_f](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a622083e8841c3899ca7b7156f526581f)
- [vtd_driver_api](../platform_security_model_reference/P074_vtd_driver_api_结构体.md)
- [allocate_entries](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#a3177c806bd86ebe4dc6c94141c9d5f04)
- [remap_msi](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#a97f93762584ea000a149ded0d726a993)
- [remap](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#ac03cd6690017568b51d1b4bedd1fea09)
- [set_irte_vector](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#a03236811cfc87b4653ba1a2f53bc50a1)
- [get_irte_by_vector](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#a39157ec0077a20a900bbe19f3cc8d1b1)
- [get_irte_vector](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#ac67dacb59216e44e55c832a26b87854f)
- [set_irte_irq](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#acc5af4aaaeed8abb8768d21767c67c58)
- [get_irte_by_irq](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#adf1c688b60ef445581dee2344a48c8b6)
- [set_irte_msi](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#ac2fbdcfe7bcb0c9ef548aefe1c80b96b)
- [irte_is_msi](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#aac4ab98b9bf8a557cec22c685433888c)
- [vtd_allocate_entries](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a87b1cea7c86d724da0c379bfd3742879)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [vtd_remap_msi](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#ab7b8ad9dbee740c9e97021853f1131fc)
- [vtd_remap](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a3cc5ff5183e80aeb18115d8b5a541546)
- [vtd_set_irte_vector](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a342e4745949ed1bd50b4d51de482be57)
- [vtd_get_irte_by_vector](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a4645558c4f9e461e86e6d0caf96311ad)
- [vtd_get_irte_vector](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a76d5a655a925c9ec9536e6c906c2192e)
- [vtd_set_irte_irq](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#ab067e306959a0774ee5e896eafab2132)
- [vtd_get_irte_by_irq](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a214bd683e7331adbe5afbca41e3a6bc9)
- [vtd_set_irte_msi](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#ae81918a2c81e03cc4e02603781e8ca21)
- [vtd_irte_is_msi](https://docs.zephyrproject.org/latest/doxygen/html/intel__vtd_8h.html#a82018e41e5bbb12f98c16b0d416596fe)
- [msi.h](https://docs.zephyrproject.org/latest/doxygen/html/msi_8h.html)
- [vtd_driver_api::set_irte_vector](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#a03236811cfc87b4653ba1a2f53bc50a1)
- [vtd_driver_api::allocate_entries](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#a3177c806bd86ebe4dc6c94141c9d5f04)
- [vtd_driver_api::get_irte_by_vector](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#a39157ec0077a20a900bbe19f3cc8d1b1)
- [vtd_driver_api::remap_msi](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#a97f93762584ea000a149ded0d726a993)
- [vtd_driver_api::irte_is_msi](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#aac4ab98b9bf8a557cec22c685433888c)
- [vtd_driver_api::remap](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#ac03cd6690017568b51d1b4bedd1fea09)
- [vtd_driver_api::set_irte_msi](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#ac2fbdcfe7bcb0c9ef548aefe1c80b96b)
- [vtd_driver_api::get_irte_vector](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#ac67dacb59216e44e55c832a26b87854f)
- [vtd_driver_api::set_irte_irq](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#acc5af4aaaeed8abb8768d21767c67c58)
- [vtd_driver_api::get_irte_by_irq](../platform_security_model_reference/P074_vtd_driver_api_结构体.md#adf1c688b60ef445581dee2344a48c8b6)

---

[上一章](P405_intc_xmc4xxx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P407_internal_trusted_storage.h_源码浏览.md)
