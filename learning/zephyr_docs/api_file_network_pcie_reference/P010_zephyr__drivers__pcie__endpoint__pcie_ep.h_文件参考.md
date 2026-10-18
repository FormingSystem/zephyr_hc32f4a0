---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-10
title: zephyr__drivers__pcie__endpoint__pcie_ep.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_drivers\_\_pcie\_\_endpoint\_\_pcie\_ep.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

PCIe端点（EP）驱动的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/init.h>
#include <zephyr/kernel.h>
#include <stdint.h>
```

查看此文件的源码。

PCIe端点（EP）驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_pcie_5Fep_5Fdriver_5Fapi"></a>

```c
struct pcie_ep_driver_api
```

相关声明：[pcie_ep_driver_api](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md)。

驱动操作（Driver Operations）：PCIe端点（Endpoint）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.2\_类型定义（Typedefs）

<a id="r_afcde72dd6977ee7de9ebf4146113f912"></a>

```c
typedef void(* pcie_ep_reset_callback_t) (void *arg)
```

相关声明：[pcie_ep_reset_callback_t](#afcde72dd6977ee7de9ebf4146113f912)。

PCIe 复位中断（PCIe Reset Interrupts）的回调 API。

<a id="r_gaf930f31c5b6e0e37fe6ca72db9dc1b42"></a>

```c
typedef int(* pcie_ep_api_conf_read) (const struct device *dev, uint32_t offset, uint32_t *data)
```

相关声明：[pcie_ep_api_conf_read](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#gaf930f31c5b6e0e37fe6ca72db9dc1b42)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取配置空间（Configuration Space）的 PCIe EP API 函数类型定义。

<a id="r_gadfc3c945b5c3dacb1e382d89a5b865ce"></a>

```c
typedef void(* pcie_ep_api_conf_write) (const struct device *dev, uint32_t offset, uint32_t data)
```

相关声明：[pcie_ep_api_conf_write](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#gadfc3c945b5c3dacb1e382d89a5b865ce)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

写入配置空间（Configuration Space）的 PCIe EP API 函数类型定义。

<a id="r_gadfb660fc4b986e8c2cf553fca0f38ac9"></a>

```c
typedef int(* pcie_ep_api_map_addr) (const struct device *dev, uint64_t pcie_addr, uint64_t *mapped_addr, uint32_t size, enum pcie_ob_mem_type ob_mem_type)
```

相关声明：[pcie_ep_api_map_addr](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#gadfb660fc4b986e8c2cf553fca0f38ac9)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_ob_mem_type](#aa7c51648c5a1663dd4dec689727a510b)。

映射主机地址（Host Address）的 PCIe EP API 函数类型定义。

<a id="r_gaa7231fbcd7efca29778b13ee608001cf"></a>

```c
typedef void(* pcie_ep_api_unmap_addr) (const struct device *dev, uint64_t mapped_addr)
```

相关声明：[pcie_ep_api_unmap_addr](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#gaa7231fbcd7efca29778b13ee608001cf)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

取消主机地址映射（Unmap Host Address）的 PCIe EP API 函数类型定义。

<a id="r_ga18f49605c9f9dc21b0fc2f8dc4329c4b"></a>

```c
typedef int(* pcie_ep_api_raise_irq) (const struct device *dev, enum pci_ep_irq_type irq_type, uint32_t irq_num)
```

相关声明：[pcie_ep_api_raise_irq](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#ga18f49605c9f9dc21b0fc2f8dc4329c4b)、[device](../device_reference/P002_设备对象结构.md)、[pci_ep_irq_type](#aba0e572125869b246d4968ee164f3800)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向主机（Host）触发中断的 PCIe EP API 函数类型定义。

<a id="r_ga0f1a5b8996bc38843d58111fd4ed2358"></a>

```c
typedef int(* pcie_ep_api_register_reset_cb) (const struct device *dev, enum pcie_reset reset, pcie_ep_reset_callback_t cb, void *arg)
```

相关声明：[pcie_ep_api_register_reset_cb](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#ga0f1a5b8996bc38843d58111fd4ed2358)、[device](../device_reference/P002_设备对象结构.md)、[pcie_reset](#a7b0f0f4693b7d11b973bfd62ac1b35cd)、[pcie_ep_reset_callback_t](#afcde72dd6977ee7de9ebf4146113f912)。

注册复位回调（Reset Callback）的 PCIe EP API 函数类型定义。

<a id="r_ga5cfa1468780b4e37120d76b156892b3f"></a>

```c
typedef int(* pcie_ep_api_dma_xfer) (const struct device *dev, uint64_t mapped_addr, uintptr_t local_addr, uint32_t size, enum xfer_direction dir)
```

相关声明：[pcie_ep_api_dma_xfer](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#ga5cfa1468780b4e37120d76b156892b3f)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[xfer_direction](#acd2605f2fb5676ded5f125712681d458)。

使用系统 DMA 传输数据的 PCIe EP API 函数类型定义。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.3\_枚举（Enumerations）

<a id="r_aa7c51648c5a1663dd4dec689727a510b"></a>

```c
enum pcie_ob_mem_type { PCIE_OB_ANYMEM , PCIE_OB_LOWMEM , PCIE_OB_HIGHMEM }
```

相关声明：[pcie_ob_mem_type](#aa7c51648c5a1663dd4dec689727a510b)、[PCIE_OB_ANYMEM](#aa7c51648c5a1663dd4dec689727a510ba52b8bd55168f44c7c4a6a3d36824d286)、[PCIE_OB_LOWMEM](#aa7c51648c5a1663dd4dec689727a510ba5312fb052e8dafaab224a4b554292e74)、[PCIE_OB_HIGHMEM](#aa7c51648c5a1663dd4dec689727a510ba13da19c9fa1732e72fa8add58da33ebb)。

PCIe 出站内存地址范围类型（Outbound Memory Address Range Type）。

<a id="r_aba0e572125869b246d4968ee164f3800"></a>

```c
enum pci_ep_irq_type { PCIE_EP_IRQ_LEGACY , PCIE_EP_IRQ_MSI , PCIE_EP_IRQ_MSIX }
```

相关声明：[pci_ep_irq_type](#aba0e572125869b246d4968ee164f3800)、[PCIE_EP_IRQ_LEGACY](#aba0e572125869b246d4968ee164f3800ad90da0a62096ef8a4fc7d230afd0d44d)、[PCIE_EP_IRQ_MSI](#aba0e572125869b246d4968ee164f3800a267b658ad2587fd0d57664197daeb318)、[PCIE_EP_IRQ_MSIX](#aba0e572125869b246d4968ee164f3800a55cad2c5812c9c7c14476ff000199ad4)。

向主机（Host）发出的中断类型（Interrupt Type）。

<a id="r_acd2605f2fb5676ded5f125712681d458"></a>

```c
enum xfer_direction { HOST_TO_DEVICE , DEVICE_TO_HOST }
```

相关声明：[xfer_direction](#acd2605f2fb5676ded5f125712681d458)、[HOST_TO_DEVICE](#acd2605f2fb5676ded5f125712681d458af2c2a8166d85d21e036a4a2015df803e)、[DEVICE_TO_HOST](#acd2605f2fb5676ded5f125712681d458a4c419a2c450c4d954c3768631870480a)。

主机（Host）与端点设备（Endpoint Device）之间的数据传输方向（Data Transfer Direction）。

<a id="r_a7b0f0f4693b7d11b973bfd62ac1b35cd"></a>

```c
enum pcie_reset { PCIE_PERST , PCIE_PERST_INB , PCIE_FLR , PCIE_RESET_MAX }
```

相关声明：[pcie_reset](#a7b0f0f4693b7d11b973bfd62ac1b35cd)、[PCIE_PERST](#a7b0f0f4693b7d11b973bfd62ac1b35cda532057b4dab53d2e86701394ead62ea7)、[PCIE_PERST_INB](#a7b0f0f4693b7d11b973bfd62ac1b35cda7d94ae3f1fbdd486102559a450f01dee)、[PCIE_FLR](#a7b0f0f4693b7d11b973bfd62ac1b35cda6dcb2d2f5ad3624bda5ca25d2e38a47a)、[PCIE_RESET_MAX](#a7b0f0f4693b7d11b973bfd62ac1b35cda2c60bd39ac112aad31d1299900f0795a)。

PCIe 复位中断类型（PCIe Reset Interrupt Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.4\_函数（Functions）

<a id="r_ad35d42579500a959bb3275cd65b04a42"></a>

```c
static int pcie_ep_conf_read (const struct device *dev, uint32_t offset, uint32_t *data)
```

相关声明：[pcie_ep_conf_read](#ad35d42579500a959bb3275cd65b04a42)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取 PCIe 端点配置空间（PCIe EP Configuration Space）。

<a id="r_a8d3f4de13956fbd7ed71acbd387f781a"></a>

```c
static void pcie_ep_conf_write (const struct device *dev, uint32_t offset, uint32_t data)
```

相关声明：[pcie_ep_conf_write](#a8d3f4de13956fbd7ed71acbd387f781a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

写入 PCIe 端点配置空间（PCIe EP Configuration Space）。

<a id="r_a7bcff5f22fd32e0b2c3c3c509038b2db"></a>

```c
static int pcie_ep_map_addr (const struct device *dev, uint64_t pcie_addr, uint64_t *mapped_addr, uint32_t size, enum pcie_ob_mem_type ob_mem_type)
```

相关声明：[pcie_ep_map_addr](#a7bcff5f22fd32e0b2c3c3c509038b2db)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_ob_mem_type](#aa7c51648c5a1663dd4dec689727a510b)。

将主机内存缓冲区（Host Memory Buffer）映射到 PCIe 出站区域（Outbound Region）。

<a id="r_a07ee4ed9ceb42462c95da8bbf3dfc8f7"></a>

```c
static void pcie_ep_unmap_addr (const struct device *dev, uint64_t mapped_addr)
```

相关声明：[pcie_ep_unmap_addr](#a07ee4ed9ceb42462c95da8bbf3dfc8f7)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

移除到 PCIe 出站区域（Outbound Region）的映射。

<a id="r_aec421e689d4d72b0bf8a34fe8303b103"></a>

```c
static int pcie_ep_raise_irq (const struct device *dev, enum pci_ep_irq_type irq_type, uint32_t irq_num)
```

相关声明：[pcie_ep_raise_irq](#aec421e689d4d72b0bf8a34fe8303b103)、[device](../device_reference/P002_设备对象结构.md)、[pci_ep_irq_type](#aba0e572125869b246d4968ee164f3800)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向主机（Host）发出中断（Interrupt）。

<a id="r_a4e9cc8364703bb58e96642d1250dc410"></a>

```c
static int pcie_ep_register_reset_cb (const struct device *dev, enum pcie_reset reset, pcie_ep_reset_callback_t cb, void *arg)
```

相关声明：[pcie_ep_register_reset_cb](#a4e9cc8364703bb58e96642d1250dc410)、[device](../device_reference/P002_设备对象结构.md)、[pcie_reset](#a7b0f0f4693b7d11b973bfd62ac1b35cd)、[pcie_ep_reset_callback_t](#afcde72dd6977ee7de9ebf4146113f912)。

为复位中断（Reset Interrupts）注册回调函数（Callback Function）。

<a id="r_a7c450e4f9d65aade3f912b72b38ed04d"></a>

```c
static int pcie_ep_dma_xfer (const struct device *dev, uint64_t mapped_addr, uintptr_t local_addr, uint32_t size, const enum xfer_direction dir)
```

相关声明：[pcie_ep_dma_xfer](#a7c450e4f9d65aade3f912b72b38ed04d)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[xfer_direction](#acd2605f2fb5676ded5f125712681d458)。

使用系统直接内存访问（System DMA），在已映射的主机内存与设备内存之间传输数据。

<a id="r_ac7e46d51c49ce6cb6b0c7ad7f8010292"></a>

```c
int pcie_ep_xfer_data_memcpy (const struct device *dev, uint64_t pcie_addr, uintptr_t *local_addr, uint32_t size, enum pcie_ob_mem_type ob_mem_type, enum xfer_direction dir)
```

相关声明：[pcie_ep_xfer_data_memcpy](#ac7e46d51c49ce6cb6b0c7ad7f8010292)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_ob_mem_type](#aa7c51648c5a1663dd4dec689727a510b)、[xfer_direction](#acd2605f2fb5676ded5f125712681d458)。

使用 `memcpy` 传输数据（Data Transfer）。

<a id="r_acfe495f60e94341e88cc267a879918fc"></a>

```c
int pcie_ep_xfer_data_dma (const struct device *dev, uint64_t pcie_addr, uintptr_t *local_addr, uint32_t size, enum pcie_ob_mem_type ob_mem_type, enum xfer_direction dir)
```

相关声明：[pcie_ep_xfer_data_dma](#acfe495f60e94341e88cc267a879918fc)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_ob_mem_type](#aa7c51648c5a1663dd4dec689727a510b)、[xfer_direction](#acd2605f2fb5676ded5f125712681d458)。

使用系统直接内存访问（System DMA）传输数据。

## 10.5\_详细说明（Detailed Documentation）

<a id="afcde72dd6977ee7de9ebf4146113f912"></a>

### `pcie_ep_reset_callback_t`

```c
typedef void(* pcie_ep_reset_callback_t) (void *arg)
```

PCIe 复位中断（PCIe Reset Interrupts）的回调 API。

这些回调在中断上下文（Interrupt Context）中执行，因此只能使用可安全用于中断的 API（Interrupt-safe APIs）。通过 `pcie_ep_register_reset_cb` 注册回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `arg` | 注册时提供的指针，稍后作为参数传回回调函数（Callback Function）。 |

<a id="aba0e572125869b246d4968ee164f3800"></a>

### `pci_ep_irq_type`

```c
enum pci_ep_irq_type
```

向主机（Host）发出的中断类型（Interrupt Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PCIE_EP_IRQ_LEGACY` | 发出传统中断（Legacy Interrupt）。 |
| `PCIE_EP_IRQ_MSI` | 发出消息信号中断（MSI Interrupt）。 |
| `PCIE_EP_IRQ_MSIX` | 发出 MSI-X 中断（MSIX Interrupt）。 |

<a id="aa7c51648c5a1663dd4dec689727a510b"></a>

### `pcie_ob_mem_type`

```c
enum pcie_ob_mem_type
```

PCIe 出站内存地址范围类型（Outbound Memory Address Range Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PCIE_OB_ANYMEM` | 位于任意地址范围的 PCIe 出站窗口（OB Window）。 |
| `PCIE_OB_LOWMEM` | 位于 32 位地址范围内的 PCIe 出站窗口（OB Window）。 |
| `PCIE_OB_HIGHMEM` | 位于 32 位地址范围以上的 PCIe 出站窗口（OB Window）。 |

<a id="a7b0f0f4693b7d11b973bfd62ac1b35cd"></a>

### `pcie_reset`

```c
enum pcie_reset
```

PCIe 复位中断类型（PCIe Reset Interrupt Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PCIE_PERST` | 冷复位（Cold Reset）。 |
| `PCIE_PERST_INB` | 带内热复位（Inband Hot Reset）。 |
| `PCIE_FLR` | 功能级复位（Functional Level Reset）。 |
| `PCIE_RESET_MAX` | PCIe 复位类型数量（Number of PCIe Reset Types）。 |

<a id="acd2605f2fb5676ded5f125712681d458"></a>

### `xfer_direction`

```c
enum xfer_direction
```

主机（Host）与端点设备（Endpoint Device）之间的数据传输方向（Data Transfer Direction）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HOST_TO_DEVICE` | 从主机读取（Read from Host）。 |
| `DEVICE_TO_HOST` | 写入主机（Write to Host）。 |

<a id="ad35d42579500a959bb3275cd65b04a42"></a>

### `pcie_ep_conf_read()`

```c
int pcie_ep_conf_read ( const struct device * dev, uint32_t offset, uint32_t * data )
```

声明属性：`inline`、`static`。

读取 PCIe 端点配置空间（PCIe EP Configuration Space）。

本 API 读取端点（EP）自身的配置空间（Configuration Space）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `offset` | 配置空间内的偏移量（Offset）。 |
| `data` | 指向从该偏移位置读取的数据的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="a8d3f4de13956fbd7ed71acbd387f781a"></a>

### `pcie_ep_conf_write()`

```c
void pcie_ep_conf_write ( const struct device * dev, uint32_t offset, uint32_t data )
```

声明属性：`inline`、`static`。

写入 PCIe 端点配置空间（PCIe EP Configuration Space）。

本 API 写入端点（EP）自身的配置空间（Configuration Space）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `offset` | 配置空间内的偏移量（Offset）。 |
| `data` | 要写入该偏移位置的数据。 |

<a id="a7c450e4f9d65aade3f912b72b38ed04d"></a>

### `pcie_ep_dma_xfer()`

```c
int pcie_ep_dma_xfer ( const struct device * dev, uint64_t mapped_addr, uintptr_t local_addr, uint32_t size, const enum xfer_direction dir )
```

声明属性：`inline`、`static`。

使用系统直接内存访问（System DMA），在已映射的主机内存与设备内存之间传输数据。

“系统 DMA”（System DMA）用于说明，此处指的不是专用“PCIe DMA”，而是不能直接理解 PCIe 地址、使用已映射主机内存（Mapped Host Memory）的 DMA。

如果端点设备（EP Device）中存在 DMA 控制器，可使用本 API，通过 DMA 在已映射主机内存，即出站内存（Outbound Memory），与端点设备本地内存之间传输数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mapped_addr` | 已映射主机内存地址（Mapped Host Memory Address）。 |
| `local_addr` | 设备内存地址（Device Memory Address）。 |
| `size` | DMA 传输长度（Transfer Length），以字节为单位。 |
| `dir` | DMA 传输方向（Transfer Direction）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="a7bcff5f22fd32e0b2c3c3c509038b2db"></a>

### `pcie_ep_map_addr()`

```c
int pcie_ep_map_addr ( const struct device * dev, uint64_t pcie_addr, uint64_t * mapped_addr, uint32_t size, enum pcie_ob_mem_type ob_mem_type )
```

声明属性：`inline`、`static`。

将主机内存缓冲区（Host Memory Buffer）映射到 PCIe 出站区域（Outbound Region）。

本 API 将主机内存缓冲区（Host Memory Buffer）映射到 PCIe 出站区域（Outbound Region）。如果 SoC 支持多个出站区域，由端点驱动（EP Driver）负责通过这些区域管理多个映射。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pcie_addr` | 要映射的主机内存缓冲区地址（Host Memory Buffer Address）。 |
| `mapped_addr` | 映射后的 PCIe 出站区域地址（Outbound Region Address）。 |
| `size` | 主机内存缓冲区大小（Host Memory Buffer Size），以字节为单位。 |
| `ob_mem_type` | 提示应使用低地址或高地址出站区域（Lowmem/Highmem Outbound Region）。当总线主设备（Bus Master）无法生成超过 32 位的地址时，这一提示尤其有用，此时必须使用低地址出站区域（Lowmem）。 |

**返回（Returns）**：返回值（Returns）：已映射大小（Mapped Size）。如果小于请求大小，则请求方必须先完成已映射部分的数据传输，再次调用同一 API 映射主机缓冲区中尚未映射的部分；映射对齐要求（Mapping Alignment Requirements）可能导致这种情况。失败时返回负 `errno` 错误码。

<a id="aec421e689d4d72b0bf8a34fe8303b103"></a>

### `pcie_ep_raise_irq()`

```c
int pcie_ep_raise_irq ( const struct device * dev, enum pci_ep_irq_type irq_type, uint32_t irq_num )
```

声明属性：`inline`、`static`。

向主机（Host）发出中断（Interrupt）。

本 API 向主机（Host）发出中断（Interrupt）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `irq_type` | 要发出的中断类型（Interrupt Type）：传统中断（Legacy）、MSI 或 MSI-X。 |
| `irq_num` | MSI 或 MSI-X 中断编号（Interrupt Number）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="a4e9cc8364703bb58e96642d1250dc410"></a>

### `pcie_ep_register_reset_cb()`

```c
int pcie_ep_register_reset_cb ( const struct device * dev, enum pcie_reset reset, pcie_ep_reset_callback_t cb, void * arg )
```

声明属性：`inline`、`static`。

为复位中断（Reset Interrupts）注册回调函数（Callback Function）。

如果设备处理复位中断（Reset Interrupts），可使用本 API 注册回调函数（Callback Function）；该函数将在对应 PCIe 复位处理程序中执行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `reset` | 复位中断类型（Reset Interrupt Type）。 |
| `cb` | 要注册的回调函数（Callback Function）。 |
| `arg` | 要传回回调函数（Callback Function）的参数。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="a07ee4ed9ceb42462c95da8bbf3dfc8f7"></a>

### `pcie_ep_unmap_addr()`

```c
void pcie_ep_unmap_addr ( const struct device * dev, uint64_t mapped_addr )
```

声明属性：`inline`、`static`。

移除到 PCIe 出站区域（Outbound Region）的映射。

本 API 移除到 PCIe 出站区域（Outbound Region）的映射。通过传入已映射的出站区域地址，确定要解除映射的区域。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `mapped_addr` | PCIe 出站区域地址（Outbound Region Address）。 |

<a id="acfe495f60e94341e88cc267a879918fc"></a>

### `pcie_ep_xfer_data_dma()`

```c
int pcie_ep_xfer_data_dma ( const struct device * dev, uint64_t pcie_addr, uintptr_t * local_addr, uint32_t size, enum pcie_ob_mem_type ob_mem_type, enum xfer_direction dir )
```

使用系统直接内存访问（System DMA）传输数据。

通过 PCIe 出站内存（Outbound Memory）使用系统 DMA（System DMA）传输数据的辅助 API。本 API 基于 `pcie_ep_xfer_data_memcpy`，但使用系统 DMA 替代 `memcpy`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pcie_addr` | 主机内存缓冲区地址（Host Memory Buffer Address）。 |
| `local_addr` | 本地内存缓冲区地址（Local Memory Buffer Address）。 |
| `size` | 数据传输大小（Data Transfer Size），以字节为单位。 |
| `ob_mem_type` | 提示应使用低地址或高地址出站区域（Lowmem/Highmem Outbound Region），取值为 `PCIE_OB_LOWMEM`、`PCIE_OB_HIGHMEM` 或 `PCIE_OB_ANYMEM`。 |
| `dir` | 数据传输方向（Data Transfer Direction）：`HOST_TO_DEVICE` 或 `DEVICE_TO_HOST`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ac7e46d51c49ce6cb6b0c7ad7f8010292"></a>

### `pcie_ep_xfer_data_memcpy()`

```c
int pcie_ep_xfer_data_memcpy ( const struct device * dev, uint64_t pcie_addr, uintptr_t * local_addr, uint32_t size, enum pcie_ob_mem_type ob_mem_type, enum xfer_direction dir )
```

使用 `memcpy` 传输数据（Data Transfer）。

通过 PCIe 出站内存（Outbound Memory）使用 `memcpy` 传输数据的辅助 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `pcie_addr` | 主机内存缓冲区地址（Host Memory Buffer Address）。 |
| `local_addr` | 本地内存缓冲区地址（Local Memory Buffer Address）。 |
| `size` | 数据传输大小（Data Transfer Size），以字节为单位。 |
| `ob_mem_type` | 提示应使用低地址或高地址出站区域（Lowmem/Highmem Outbound Region），取值为 `PCIE_OB_LOWMEM`、`PCIE_OB_HIGHMEM` 或 `PCIE_OB_ANYMEM`。如果总线主设备（Bus Master）无法生成超过 32 位的地址，应使用 `PCIE_OB_LOWMEM`。 |
| `dir` | 数据传输方向（Data Transfer Direction）：`HOST_TO_DEVICE` 或 `DEVICE_TO_HOST`。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。


## 10.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/init.h](../device_reference/P010_系统初始化头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P141_pcie_ep.h_源码浏览.md)
- [pcie_ep_driver_api](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md)
- [pcie_ep_api_conf_read](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#gaf930f31c5b6e0e37fe6ca72db9dc1b42)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pcie_ep_api_conf_write](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#gadfc3c945b5c3dacb1e382d89a5b865ce)
- [pcie_ep_api_map_addr](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#gadfb660fc4b986e8c2cf553fca0f38ac9)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [pcie_ep_api_unmap_addr](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#gaa7231fbcd7efca29778b13ee608001cf)
- [pcie_ep_api_raise_irq](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#ga18f49605c9f9dc21b0fc2f8dc4329c4b)
- [pcie_ep_api_register_reset_cb](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#ga0f1a5b8996bc38843d58111fd4ed2358)
- [pcie_ep_api_dma_xfer](../api_interaction_transport_topic_reference/P013_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）.md#ga5cfa1468780b4e37120d76b156892b3f)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="aba0e572125869b246d4968ee164f3800ad90da0a62096ef8a4fc7d230afd0d44d"></a>
<a id="aba0e572125869b246d4968ee164f3800a267b658ad2587fd0d57664197daeb318"></a>
<a id="aba0e572125869b246d4968ee164f3800a55cad2c5812c9c7c14476ff000199ad4"></a>
<a id="aa7c51648c5a1663dd4dec689727a510ba52b8bd55168f44c7c4a6a3d36824d286"></a>
<a id="aa7c51648c5a1663dd4dec689727a510ba5312fb052e8dafaab224a4b554292e74"></a>
<a id="aa7c51648c5a1663dd4dec689727a510ba13da19c9fa1732e72fa8add58da33ebb"></a>
<a id="a7b0f0f4693b7d11b973bfd62ac1b35cda532057b4dab53d2e86701394ead62ea7"></a>
<a id="a7b0f0f4693b7d11b973bfd62ac1b35cda7d94ae3f1fbdd486102559a450f01dee"></a>
<a id="a7b0f0f4693b7d11b973bfd62ac1b35cda6dcb2d2f5ad3624bda5ca25d2e38a47a"></a>
<a id="a7b0f0f4693b7d11b973bfd62ac1b35cda2c60bd39ac112aad31d1299900f0795a"></a>
<a id="acd2605f2fb5676ded5f125712681d458af2c2a8166d85d21e036a4a2015df803e"></a>
<a id="acd2605f2fb5676ded5f125712681d458a4c419a2c450c4d954c3768631870480a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_zephyr__net__net_pkt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__drivers__misc__renesas_rx_dtc__renesas_rx_dtc.h_文件参考.md)
