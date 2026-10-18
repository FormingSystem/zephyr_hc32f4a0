---
id: learning.zephyr-docs.api-source-supplement-reference.page-141
title: pcie_ep.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第141章\_pcie\_ep.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html)。

## 141.1\_原始可见代码（Source Code）

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
<a id="foldopen00023"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00037"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00067"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00123"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00153"></a>
<a id="foldopen00154"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00169"></a>
<a id="foldopen00170"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00200"></a>
<a id="foldopen00201"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00220"></a>
<a id="foldopen00221"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00238"></a>
<a id="foldopen00239"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00260"></a>
<a id="foldopen00261"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00294"></a>
<a id="foldopen00295"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__pcie__interface__backend_html_ga0f1a5b8996bc38843d58111fd4ed2358"></a>
<a id="agroup__pcie__interface__backend_html_ga18f49605c9f9dc21b0fc2f8dc4329c4b"></a>
<a id="agroup__pcie__interface__backend_html_ga5cfa1468780b4e37120d76b156892b3f"></a>
<a id="agroup__pcie__interface__backend_html_gaa7231fbcd7efca29778b13ee608001cf"></a>
<a id="agroup__pcie__interface__backend_html_gadfb660fc4b986e8c2cf553fca0f38ac9"></a>
<a id="agroup__pcie__interface__backend_html_gadfc3c945b5c3dacb1e382d89a5b865ce"></a>
<a id="agroup__pcie__interface__backend_html_gaf930f31c5b6e0e37fe6ca72db9dc1b42"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="ainit_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="apcie__ep_8h_html_a07ee4ed9ceb42462c95da8bbf3dfc8f7"></a>
<a id="apcie__ep_8h_html_a4e9cc8364703bb58e96642d1250dc410"></a>
<a id="apcie__ep_8h_html_a7b0f0f4693b7d11b973bfd62ac1b35cd"></a>
<a id="apcie__ep_8h_html_a7b0f0f4693b7d11b973bfd62ac1b35cda2c60bd39ac112aad31d1299900f0795a"></a>
<a id="apcie__ep_8h_html_a7b0f0f4693b7d11b973bfd62ac1b35cda532057b4dab53d2e86701394ead62ea7"></a>
<a id="apcie__ep_8h_html_a7b0f0f4693b7d11b973bfd62ac1b35cda6dcb2d2f5ad3624bda5ca25d2e38a47a"></a>
<a id="apcie__ep_8h_html_a7b0f0f4693b7d11b973bfd62ac1b35cda7d94ae3f1fbdd486102559a450f01dee"></a>
<a id="apcie__ep_8h_html_a7bcff5f22fd32e0b2c3c3c509038b2db"></a>
<a id="apcie__ep_8h_html_a7c450e4f9d65aade3f912b72b38ed04d"></a>
<a id="apcie__ep_8h_html_a8d3f4de13956fbd7ed71acbd387f781a"></a>
<a id="apcie__ep_8h_html_aa7c51648c5a1663dd4dec689727a510b"></a>
<a id="apcie__ep_8h_html_aa7c51648c5a1663dd4dec689727a510ba13da19c9fa1732e72fa8add58da33ebb"></a>
<a id="apcie__ep_8h_html_aa7c51648c5a1663dd4dec689727a510ba52b8bd55168f44c7c4a6a3d36824d286"></a>
<a id="apcie__ep_8h_html_aa7c51648c5a1663dd4dec689727a510ba5312fb052e8dafaab224a4b554292e74"></a>
<a id="apcie__ep_8h_html_aba0e572125869b246d4968ee164f3800"></a>
<a id="apcie__ep_8h_html_aba0e572125869b246d4968ee164f3800a267b658ad2587fd0d57664197daeb318"></a>
<a id="apcie__ep_8h_html_aba0e572125869b246d4968ee164f3800a55cad2c5812c9c7c14476ff000199ad4"></a>
<a id="apcie__ep_8h_html_aba0e572125869b246d4968ee164f3800ad90da0a62096ef8a4fc7d230afd0d44d"></a>
<a id="apcie__ep_8h_html_ac7e46d51c49ce6cb6b0c7ad7f8010292"></a>
<a id="apcie__ep_8h_html_acd2605f2fb5676ded5f125712681d458"></a>
<a id="apcie__ep_8h_html_acd2605f2fb5676ded5f125712681d458a4c419a2c450c4d954c3768631870480a"></a>
<a id="apcie__ep_8h_html_acd2605f2fb5676ded5f125712681d458af2c2a8166d85d21e036a4a2015df803e"></a>
<a id="apcie__ep_8h_html_acfe495f60e94341e88cc267a879918fc"></a>
<a id="apcie__ep_8h_html_ad35d42579500a959bb3275cd65b04a42"></a>
<a id="apcie__ep_8h_html_aec421e689d4d72b0bf8a34fe8303b103"></a>
<a id="apcie__ep_8h_html_afcde72dd6977ee7de9ebf4146113f912"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructpcie__ep__driver__api_html"></a>
<a id="astructpcie__ep__driver__api_html_a603366158e0204896380425461cdbbcc"></a>
<a id="astructpcie__ep__driver__api_html_a7ca1ee31f72b14db3acf2a0f5b0aab9c"></a>
<a id="astructpcie__ep__driver__api_html_a9a63bde4308d3d0dc86d0ed7d19cc192"></a>
<a id="astructpcie__ep__driver__api_html_aaae0fe7f4d58da035289da02e0d33111"></a>
<a id="astructpcie__ep__driver__api_html_abdc6da0a251d4281bfe8533b8be6a66f"></a>
<a id="astructpcie__ep__driver__api_html_ac1c11775d08023e1d9c3ad9b46d77785"></a>
<a id="astructpcie__ep__driver__api_html_af651a646631e13fc0e4989cea4df9735"></a>

```c


/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright 2020 Broadcom
 *
 */
#ifndef ZEPHYR_INCLUDE_DRIVERS_PCIE_EP_H_
#define ZEPHYR_INCLUDE_DRIVERS_PCIE_EP_H_

#include <zephyr/device.h>
#include <zephyr/init.h>
#include <zephyr/kernel.h>
#include <stdint.h>

enum pcie_ob_mem_type {
        PCIE_OB_ANYMEM,
        PCIE_OB_LOWMEM,
        PCIE_OB_HIGHMEM,
};

enum pci_ep_irq_type {
        PCIE_EP_IRQ_LEGACY,
        PCIE_EP_IRQ_MSI,
        PCIE_EP_IRQ_MSIX,
};

enum xfer_direction {
        HOST_TO_DEVICE,
        DEVICE_TO_HOST,
};

enum pcie_reset {
        PCIE_PERST,
        PCIE_PERST_INB,
        PCIE_FLR,
        PCIE_RESET_MAX
};


typedef void (*pcie_ep_reset_callback_t)(void *arg);


typedef int (*pcie_ep_api_conf_read)(const struct device *dev, uint32_t offset,
                                     uint32_t *data);

typedef void (*pcie_ep_api_conf_write)(const struct device *dev, uint32_t offset,
                                       uint32_t data);

typedef int (*pcie_ep_api_map_addr)(const struct device *dev, uint64_t pcie_addr,
                                    uint64_t *mapped_addr, uint32_t size,
                                    enum pcie_ob_mem_type ob_mem_type);

typedef void (*pcie_ep_api_unmap_addr)(const struct device *dev, uint64_t mapped_addr);

typedef int (*pcie_ep_api_raise_irq)(const struct device *dev,
                                     enum pci_ep_irq_type irq_type,
                                     uint32_t irq_num);

typedef int (*pcie_ep_api_register_reset_cb)(const struct device *dev,
                                             enum pcie_reset reset,
                                             pcie_ep_reset_callback_t cb, void *arg);

typedef int (*pcie_ep_api_dma_xfer)(const struct device *dev, uint64_t mapped_addr,
                                    uintptr_t local_addr, uint32_t size,
                                    enum xfer_direction dir);

__subsystem struct pcie_ep_driver_api {
        pcie_ep_api_conf_read conf_read;
        pcie_ep_api_conf_write conf_write;
        pcie_ep_api_map_addr map_addr;
        pcie_ep_api_unmap_addr unmap_addr;
        pcie_ep_api_raise_irq raise_irq;
        pcie_ep_api_register_reset_cb register_reset_cb;
        pcie_ep_api_dma_xfer dma_xfer;
};



static inline int pcie_ep_conf_read(const struct device *dev,
                                    uint32_t offset, uint32_t *data)
{
        return DEVICE_API_GET(pcie_ep, dev)->conf_read(dev, offset, data);
}


static inline void pcie_ep_conf_write(const struct device *dev,
                                      uint32_t offset, uint32_t data)
{
        DEVICE_API_GET(pcie_ep, dev)->conf_write(dev, offset, data);
}


static inline int pcie_ep_map_addr(const struct device *dev,
                                   uint64_t pcie_addr,
                                   uint64_t *mapped_addr, uint32_t size,
                                   enum pcie_ob_mem_type ob_mem_type)
{
        return DEVICE_API_GET(pcie_ep, dev)->map_addr(dev, pcie_addr, mapped_addr, size,
                                                      ob_mem_type);
}


static inline void pcie_ep_unmap_addr(const struct device *dev,
                                      uint64_t mapped_addr)
{
        DEVICE_API_GET(pcie_ep, dev)->unmap_addr(dev, mapped_addr);
}


static inline int pcie_ep_raise_irq(const struct device *dev,
                                    enum pci_ep_irq_type irq_type,
                                    uint32_t irq_num)
{
        return DEVICE_API_GET(pcie_ep, dev)->raise_irq(dev, irq_type, irq_num);
}


static inline int pcie_ep_register_reset_cb(const struct device *dev,
                                            enum pcie_reset reset,
                                            pcie_ep_reset_callback_t cb,
                                            void *arg)
{
        const struct pcie_ep_driver_api *api = DEVICE_API_GET(pcie_ep, dev);

        if (api->register_reset_cb) {
                return api->register_reset_cb(dev, reset, cb, arg);
        }

        return -ENOTSUP;
}


static inline int pcie_ep_dma_xfer(const struct device *dev,
                                   uint64_t mapped_addr,
                                   uintptr_t local_addr, uint32_t size,
                                   const enum xfer_direction dir)
{
        const struct pcie_ep_driver_api *api = DEVICE_API_GET(pcie_ep, dev);

        if (api->dma_xfer) {
                return api->dma_xfer(dev, mapped_addr, local_addr, size, dir);
        }

        return -ENOTSUP;
}

int pcie_ep_xfer_data_memcpy(const struct device *dev, uint64_t pcie_addr,
                             uintptr_t *local_addr, uint32_t size,
                             enum pcie_ob_mem_type ob_mem_type,
                             enum xfer_direction dir);

int pcie_ep_xfer_data_dma(const struct device *dev, uint64_t pcie_addr,
                          uintptr_t *local_addr, uint32_t size,
                          enum pcie_ob_mem_type ob_mem_type,
                          enum xfer_direction dir);

#endif /* ZEPHYR_INCLUDE_DRIVERS_PCIE_EP_H_ */
```

## 141.2\_可见注释译文（Comments）

### 注释 1：原第 8 行

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

版权（Copyright）：2020 Broadcom。

### 注释 2：原第 354 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_PCIE_EP_H_`。

## 141.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/init.h](../device_reference/P009_系统初始化头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [pcie_ob_mem_type](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aa7c51648c5a1663dd4dec689727a510b)
- [PCIE_OB_ANYMEM](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aa7c51648c5a1663dd4dec689727a510ba52b8bd55168f44c7c4a6a3d36824d286)
- [PCIE_OB_LOWMEM](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aa7c51648c5a1663dd4dec689727a510ba5312fb052e8dafaab224a4b554292e74)
- [PCIE_OB_HIGHMEM](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aa7c51648c5a1663dd4dec689727a510ba13da19c9fa1732e72fa8add58da33ebb)
- [pci_ep_irq_type](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aba0e572125869b246d4968ee164f3800)
- [PCIE_EP_IRQ_LEGACY](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aba0e572125869b246d4968ee164f3800ad90da0a62096ef8a4fc7d230afd0d44d)
- [PCIE_EP_IRQ_MSI](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aba0e572125869b246d4968ee164f3800a267b658ad2587fd0d57664197daeb318)
- [PCIE_EP_IRQ_MSIX](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aba0e572125869b246d4968ee164f3800a55cad2c5812c9c7c14476ff000199ad4)
- [xfer_direction](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#acd2605f2fb5676ded5f125712681d458)
- [HOST_TO_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#acd2605f2fb5676ded5f125712681d458af2c2a8166d85d21e036a4a2015df803e)
- [DEVICE_TO_HOST](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#acd2605f2fb5676ded5f125712681d458a4c419a2c450c4d954c3768631870480a)
- [pcie_reset](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a7b0f0f4693b7d11b973bfd62ac1b35cd)
- [PCIE_PERST](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a7b0f0f4693b7d11b973bfd62ac1b35cda532057b4dab53d2e86701394ead62ea7)
- [PCIE_PERST_INB](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a7b0f0f4693b7d11b973bfd62ac1b35cda7d94ae3f1fbdd486102559a450f01dee)
- [PCIE_FLR](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a7b0f0f4693b7d11b973bfd62ac1b35cda6dcb2d2f5ad3624bda5ca25d2e38a47a)
- [PCIE_RESET_MAX](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a7b0f0f4693b7d11b973bfd62ac1b35cda2c60bd39ac112aad31d1299900f0795a)
- [pcie_ep_reset_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#afcde72dd6977ee7de9ebf4146113f912)
- [pcie_ep_api_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#gaf930f31c5b6e0e37fe6ca72db9dc1b42)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [pcie_ep_api_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#gadfc3c945b5c3dacb1e382d89a5b865ce)
- [pcie_ep_api_map_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#gadfb660fc4b986e8c2cf553fca0f38ac9)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [pcie_ep_api_unmap_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#gaa7231fbcd7efca29778b13ee608001cf)
- [pcie_ep_api_raise_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#ga18f49605c9f9dc21b0fc2f8dc4329c4b)
- [pcie_ep_api_register_reset_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#ga0f1a5b8996bc38843d58111fd4ed2358)
- [pcie_ep_api_dma_xfer](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#ga5cfa1468780b4e37120d76b156892b3f)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [pcie_ep_driver_api](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md)
- [conf_read](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#aaae0fe7f4d58da035289da02e0d33111)
- [conf_write](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#af651a646631e13fc0e4989cea4df9735)
- [map_addr](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#a7ca1ee31f72b14db3acf2a0f5b0aab9c)
- [unmap_addr](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#a603366158e0204896380425461cdbbcc)
- [raise_irq](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#a9a63bde4308d3d0dc86d0ed7d19cc192)
- [register_reset_cb](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#ac1c11775d08023e1d9c3ad9b46d77785)
- [dma_xfer](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#abdc6da0a251d4281bfe8533b8be6a66f)
- [pcie_ep_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#ad35d42579500a959bb3275cd65b04a42)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [pcie_ep_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a8d3f4de13956fbd7ed71acbd387f781a)
- [pcie_ep_map_addr](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a7bcff5f22fd32e0b2c3c3c509038b2db)
- [pcie_ep_unmap_addr](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a07ee4ed9ceb42462c95da8bbf3dfc8f7)
- [pcie_ep_raise_irq](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aec421e689d4d72b0bf8a34fe8303b103)
- [pcie_ep_register_reset_cb](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a4e9cc8364703bb58e96642d1250dc410)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [pcie_ep_dma_xfer](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a7c450e4f9d65aade3f912b72b38ed04d)
- [pcie_ep_xfer_data_memcpy](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#ac7e46d51c49ce6cb6b0c7ad7f8010292)
- [pcie_ep_xfer_data_dma](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#acfe495f60e94341e88cc267a879918fc)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [init.h](../device_reference/P009_系统初始化头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [pcie_ep_driver_api::unmap_addr](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#a603366158e0204896380425461cdbbcc)
- [pcie_ep_driver_api::map_addr](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#a7ca1ee31f72b14db3acf2a0f5b0aab9c)
- [pcie_ep_driver_api::raise_irq](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#a9a63bde4308d3d0dc86d0ed7d19cc192)
- [pcie_ep_driver_api::conf_read](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#aaae0fe7f4d58da035289da02e0d33111)
- [pcie_ep_driver_api::dma_xfer](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#abdc6da0a251d4281bfe8533b8be6a66f)
- [pcie_ep_driver_api::register_reset_cb](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#ac1c11775d08023e1d9c3ad9b46d77785)
- [pcie_ep_driver_api::conf_write](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md#af651a646631e13fc0e4989cea4df9735)

---

[上一章](P140_paj7620.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P142_phy.h_源码浏览.md)
