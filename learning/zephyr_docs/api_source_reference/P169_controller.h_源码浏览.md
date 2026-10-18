---
id: learning.zephyr-docs.api-source-reference.page-169
title: controller.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2controller_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第169章\_controller.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2controller_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2controller_8h.html)。

## 169.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00040"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="foldopen00182"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="foldopen00215"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="foldopen00232"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="foldopen00255"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="foldopen00278"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="foldopen00304"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="foldopen00330"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="foldopen00339"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00348"></a>
<a id="l00350"></a>
<a id="l00352"></a>
<a id="l00354"></a>
<a id="l00356"></a>
<a id="l00358"></a>
<a id="l00360"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="foldopen00375"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adrivers_2pcie_2pcie_8h_html"></a>
<a id="agroup__pcie__controller__interface__backend_html_ga3241acc7de4af2b73cf3f47a25349109"></a>
<a id="agroup__pcie__controller__interface__backend_html_ga62ce18e7495256c148168b773eabd37d"></a>
<a id="agroup__pcie__controller__interface__backend_html_ga709ecedbd0585b4eb17fc2f5923a8f61"></a>
<a id="agroup__pcie__controller__interface__backend_html_ga75910ea4255a740b57e35a596a90b7bb"></a>
<a id="agroup__pcie__controller__interface__backend_html_gaa16b59c39f273a654b72d9e209f3ba2e"></a>
<a id="agroup__pcie__controller__interface__backend_html_gaa9d5bd27c841e36f65e65dec0b057e9a"></a>
<a id="agroup__pcie__controller__interface__backend_html_gab144356b1c3ec3754aae0008634f2d2f"></a>
<a id="agroup__pcie__controller__interface__backend_html_gac3d0f7e90bcc30996ce23324d2d7356a"></a>
<a id="agroup__pcie__controller__interface_html_ga1d978b8075191d6e571349684c731a43"></a>
<a id="agroup__pcie__controller__interface_html_ga1de030e2e8b07509d75de5a348297f42"></a>
<a id="agroup__pcie__controller__interface_html_ga5cfe01762e5af8dc0cc5fbd550ff7e74"></a>
<a id="agroup__pcie__controller__interface_html_ga69493e7da12c4c2d95f506ecf86e7dfe"></a>
<a id="agroup__pcie__controller__interface_html_gae6fa104ea2cc85912ebb1cfe0a1a3ddf"></a>
<a id="agroup__pcie__controller__interface_html_gae7c109ca138adfd906fef5b6f3dca385"></a>
<a id="agroup__pcie__host__interface_html_gaf9748042a4f3c8d912d19df1ccf737fb"></a>
<a id="agroup__pcie__host__msi__interface_html_ga9ede6a7a472ee62f0975256a1b5f1231"></a>
<a id="agroup__sys__io__apis_html_ga7bcfa789a44940bccc5b9b98642744b0"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="amsi_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructpcie__ctrl__config_html"></a>
<a id="astructpcie__ctrl__config_html_a1a59bec03927f2c6b5fd0aed8c36e6b4"></a>
<a id="astructpcie__ctrl__config_html_a3de0f32aaf3ddb377897974dfdfe67bd"></a>
<a id="astructpcie__ctrl__config_html_a45f9fa1124aa64bbfd7ff2c5519cbb4b"></a>
<a id="astructpcie__ctrl__config_html_a4a620f03546490b65ba4d097329928e8"></a>
<a id="astructpcie__ctrl__config_html_a6881d50254b57164f546af66e2773d13"></a>
<a id="astructpcie__ctrl__config_html_a90e48aaca78a8284caa449ee3972d87b"></a>
<a id="astructpcie__ctrl__config_html_ace0b3505edc0aff3678a91b630244963"></a>
<a id="astructpcie__ctrl__config_html_adb1b8ed76f3f994f2da72c8e8b40d4f0"></a>
<a id="astructpcie__ctrl__config_html_ae3dd8d3d72a1597ee135b49e46e31bec"></a>
<a id="astructpcie__ctrl__driver__api_html"></a>
<a id="astructpcie__ctrl__driver__api_html_a1263e43fa575cc76a48bcd463b84e3a6"></a>
<a id="astructpcie__ctrl__driver__api_html_a20c1faf02c71e88da165c889550a76ae"></a>
<a id="astructpcie__ctrl__driver__api_html_a46191bf9aad7ab7ac1319918873b8b29"></a>
<a id="astructpcie__ctrl__driver__api_html_a46fa0fd3a759fe2dc960546b49c53979"></a>
<a id="astructpcie__ctrl__driver__api_html_a5d7687cd738bd86a785fc281781d2759"></a>
<a id="astructpcie__ctrl__driver__api_html_a71a4d13492bb3098bdb2c0e0ff7b94cf"></a>

```c


/*
 * Copyright (c) 2021 BayLibre, SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DRIVERS_PCIE_CONTROLLERS_H_
#define ZEPHYR_INCLUDE_DRIVERS_PCIE_CONTROLLERS_H_

#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/drivers/pcie/pcie.h>

#ifdef CONFIG_PCIE_MSI
#include <zephyr/drivers/pcie/msi.h>
#endif


#ifdef __cplusplus
extern "C" {
#endif


typedef uint32_t (*pcie_ctrl_conf_read_t)(const struct device *dev, pcie_bdf_t bdf,
                                          unsigned int reg);

typedef void (*pcie_ctrl_conf_write_t)(const struct device *dev, pcie_bdf_t bdf,
                                          unsigned int reg, uint32_t data);

typedef bool (*pcie_ctrl_region_allocate_t)(const struct device *dev, pcie_bdf_t bdf,
                                            bool mem, bool mem64, size_t bar_size,
                                            uintptr_t *bar_bus_addr);

typedef bool (*pcie_ctrl_region_get_allocate_base_t)(const struct device *dev, pcie_bdf_t bdf,
                                                     bool mem, bool mem64, size_t align,
                                                     uintptr_t *bar_base_addr);

typedef bool (*pcie_ctrl_region_translate_t)(const struct device *dev, pcie_bdf_t bdf,
                                             bool mem, bool mem64, uintptr_t bar_bus_addr,
                                             uintptr_t *bar_addr);

#ifdef CONFIG_PCIE_MSI
typedef uint8_t (*pcie_ctrl_msi_device_setup_t)(const struct device *dev, unsigned int priority,
                                                msi_vector_t *vectors, uint8_t n_vector);
#endif

uint32_t pcie_generic_ctrl_conf_read(mm_reg_t cfg_addr, pcie_bdf_t bdf, unsigned int reg);


void pcie_generic_ctrl_conf_write(mm_reg_t cfg_addr, pcie_bdf_t bdf,
                                  unsigned int reg, uint32_t data);

void pcie_generic_ctrl_enumerate(const struct device *dev, pcie_bdf_t bdf_start);

__subsystem struct pcie_ctrl_driver_api {
        pcie_ctrl_conf_read_t conf_read;
        pcie_ctrl_conf_write_t conf_write;
        pcie_ctrl_region_allocate_t region_allocate;
        pcie_ctrl_region_get_allocate_base_t region_get_allocate_base;
        pcie_ctrl_region_translate_t region_translate;
#if defined(CONFIG_PCIE_MSI) || defined(__DOXYGEN__)
        pcie_ctrl_msi_device_setup_t msi_device_setup;
#endif
};


static inline uint32_t pcie_ctrl_conf_read(const struct device *dev, pcie_bdf_t bdf,
                                           unsigned int reg)
{
        return DEVICE_API_GET(pcie_ctrl, dev)->conf_read(dev, bdf, reg);
}

static inline void pcie_ctrl_conf_write(const struct device *dev, pcie_bdf_t bdf,
                                        unsigned int reg, uint32_t data)
{
        DEVICE_API_GET(pcie_ctrl, dev)->conf_write(dev, bdf, reg, data);
}

static inline bool pcie_ctrl_region_allocate(const struct device *dev, pcie_bdf_t bdf,
                                             bool mem, bool mem64, size_t bar_size,
                                             uintptr_t *bar_bus_addr)
{
        return DEVICE_API_GET(pcie_ctrl, dev)->region_allocate(dev, bdf, mem, mem64, bar_size,
                                                               bar_bus_addr);
}

static inline bool pcie_ctrl_region_get_allocate_base(const struct device *dev, pcie_bdf_t bdf,
                                                      bool mem, bool mem64, size_t align,
                                                      uintptr_t *bar_base_addr)
{
        return DEVICE_API_GET(pcie_ctrl, dev)->region_get_allocate_base(dev, bdf, mem, mem64, align,
                                                                        bar_base_addr);
}

static inline bool pcie_ctrl_region_translate(const struct device *dev, pcie_bdf_t bdf,
                                          bool mem, bool mem64, uintptr_t bar_bus_addr,
                                          uintptr_t *bar_addr)
{
        const struct pcie_ctrl_driver_api *api = DEVICE_API_GET(pcie_ctrl, dev);

        if (!api->region_translate) {
                *bar_addr = bar_bus_addr;
                return true;
        } else {
                return api->region_translate(dev, bdf, mem, mem64, bar_bus_addr, bar_addr);
        }
}

#if defined(CONFIG_PCIE_MSI) || defined(__DOXYGEN__)
static inline uint8_t pcie_ctrl_msi_device_setup(const struct device *dev, unsigned int priority,
                                                 msi_vector_t *vectors, uint8_t n_vector)
{
        return DEVICE_API_GET(pcie_ctrl, dev)->msi_device_setup(dev, priority, vectors, n_vector);
}
#endif

struct pcie_ctrl_config {
#if defined(CONFIG_PCIE_MSI) || defined(__DOXYGEN__)
        const struct device *msi_parent;
#endif
        uintptr_t cfg_addr;
        size_t cfg_size;
        size_t ranges_count;
        struct {
                uint32_t flags;
                uintptr_t pcie_bus_addr;
                uintptr_t host_map_addr;
                size_t map_length;
        } ranges[];
};

#define PCIE_RANGE_FORMAT(node_id, idx)                                                 \
{                                                                                       \
        .flags = DT_RANGES_CHILD_BUS_FLAGS_BY_IDX(node_id, idx),                        \
        .pcie_bus_addr = DT_RANGES_CHILD_BUS_ADDRESS_BY_IDX(node_id, idx),              \
        .host_map_addr = DT_RANGES_PARENT_BUS_ADDRESS_BY_IDX(node_id, idx),             \
        .map_length = DT_RANGES_LENGTH_BY_IDX(node_id, idx),                            \
},

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_PCIE_CONTROLLERS_H_ */
```

## 169.2\_可见注释译文（Comments）

### 注释 1：原第 8 行

版权（Copyright）：© 2021 BayLibre, SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 391 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PCIE_CONTROLLERS_H_`。

## 169.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2controller_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/pcie/pcie.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h.html)
- [zephyr/drivers/pcie/msi.h](https://docs.zephyrproject.org/latest/doxygen/html/msi_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pcie_ctrl_conf_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gac3d0f7e90bcc30996ce23324d2d7356a)
- [device](../device_reference/P002_设备对象结构.md)
- [pcie_bdf_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__interface.html#gaf9748042a4f3c8d912d19df1ccf737fb)
- [pcie_ctrl_conf_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga3241acc7de4af2b73cf3f47a25349109)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [pcie_ctrl_region_allocate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga62ce18e7495256c148168b773eabd37d)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [pcie_ctrl_region_get_allocate_base_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gaa9d5bd27c841e36f65e65dec0b057e9a)
- [pcie_ctrl_region_translate_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gab144356b1c3ec3754aae0008634f2d2f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [msi_vector_t](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__host__msi__interface.html#ga9ede6a7a472ee62f0975256a1b5f1231)
- [pcie_generic_ctrl_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#gaa16b59c39f273a654b72d9e209f3ba2e)
- [mm_reg_t](../device_reference/P017_系统IO公共接口.md#ga7bcfa789a44940bccc5b9b98642744b0)
- [pcie_generic_ctrl_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga709ecedbd0585b4eb17fc2f5923a8f61)
- [pcie_generic_ctrl_enumerate](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface__backend.html#ga75910ea4255a740b57e35a596a90b7bb)
- [pcie_ctrl_driver_api](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md)
- [conf_read](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md#a20c1faf02c71e88da165c889550a76ae)
- [conf_write](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md#a46fa0fd3a759fe2dc960546b49c53979)
- [region_allocate](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md#a46191bf9aad7ab7ac1319918873b8b29)
- [region_get_allocate_base](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md#a5d7687cd738bd86a785fc281781d2759)
- [region_translate](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md#a71a4d13492bb3098bdb2c0e0ff7b94cf)
- [msi_device_setup](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md#a1263e43fa575cc76a48bcd463b84e3a6)
- [pcie_ctrl_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga1d978b8075191d6e571349684c731a43)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [pcie_ctrl_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga5cfe01762e5af8dc0cc5fbd550ff7e74)
- [pcie_ctrl_region_allocate](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga1de030e2e8b07509d75de5a348297f42)
- [pcie_ctrl_region_get_allocate_base](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#gae7c109ca138adfd906fef5b6f3dca385)
- [pcie_ctrl_region_translate](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#gae6fa104ea2cc85912ebb1cfe0a1a3ddf)
- [pcie_ctrl_msi_device_setup](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__controller__interface.html#ga69493e7da12c4c2d95f506ecf86e7dfe)
- [pcie_ctrl_config](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md)
- [msi_parent](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a6881d50254b57164f546af66e2773d13)
- [cfg_addr](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a3de0f32aaf3ddb377897974dfdfe67bd)
- [cfg_size](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#adb1b8ed76f3f994f2da72c8e8b40d4f0)
- [ranges_count](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a4a620f03546490b65ba4d097329928e8)
- [flags](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a90e48aaca78a8284caa449ee3972d87b)
- [pcie_bus_addr](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a45f9fa1124aa64bbfd7ff2c5519cbb4b)
- [host_map_addr](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#ace0b3505edc0aff3678a91b630244963)
- [map_length](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#ae3dd8d3d72a1597ee135b49e46e31bec)
- [ranges](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a1a59bec03927f2c6b5fd0aed8c36e6b4)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [pcie.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2pcie_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [msi.h](https://docs.zephyrproject.org/latest/doxygen/html/msi_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [pcie_ctrl_config::ranges](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a1a59bec03927f2c6b5fd0aed8c36e6b4)
- [pcie_ctrl_config::cfg_addr](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a3de0f32aaf3ddb377897974dfdfe67bd)
- [pcie_ctrl_config::pcie_bus_addr](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a45f9fa1124aa64bbfd7ff2c5519cbb4b)
- [pcie_ctrl_config::ranges_count](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a4a620f03546490b65ba4d097329928e8)
- [pcie_ctrl_config::msi_parent](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a6881d50254b57164f546af66e2773d13)
- [pcie_ctrl_config::flags](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#a90e48aaca78a8284caa449ee3972d87b)
- [pcie_ctrl_config::host_map_addr](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#ace0b3505edc0aff3678a91b630244963)
- [pcie_ctrl_config::cfg_size](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#adb1b8ed76f3f994f2da72c8e8b40d4f0)
- [pcie_ctrl_config::map_length](../platform_security_model_reference/P026_pcie_ctrl_config_结构体.md#ae3dd8d3d72a1597ee135b49e46e31bec)
- [pcie_ctrl_driver_api::msi_device_setup](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md#a1263e43fa575cc76a48bcd463b84e3a6)
- [pcie_ctrl_driver_api::conf_read](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md#a20c1faf02c71e88da165c889550a76ae)
- [pcie_ctrl_driver_api::region_allocate](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md#a46191bf9aad7ab7ac1319918873b8b29)
- [pcie_ctrl_driver_api::conf_write](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md#a46fa0fd3a759fe2dc960546b49c53979)
- [pcie_ctrl_driver_api::region_get_allocate_base](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md#a5d7687cd738bd86a785fc281781d2759)
- [pcie_ctrl_driver_api::region_translate](../platform_security_model_reference/P027_pcie_ctrl_driver_api_结构体.md#a71a4d13492bb3098bdb2c0e0ff7b94cf)

---

[上一章](P168_cap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P170_atmel_sam_supc.h_源码浏览.md)
