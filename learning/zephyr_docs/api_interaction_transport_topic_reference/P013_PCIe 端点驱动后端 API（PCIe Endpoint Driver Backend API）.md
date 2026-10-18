---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-13
title: PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_PCIe 端点驱动后端 API（PCIe Endpoint Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现 PCIe 端点（Endpoint，EP）驱动所需的 API 类型定义、回调签名（Callback Signature）及其他辅助接口。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.1\_数据结构（Data Structures）

<a id="r_pcie_5Fep_5Fdriver_5Fapi"></a>

```c
struct pcie_ep_driver_api
```

相关声明：[pcie_ep_driver_api](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md)。

驱动操作（Driver Operations）：PCIe端点（Endpoint）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 13.2\_类型定义（Typedefs）

<a id="r_gaf930f31c5b6e0e37fe6ca72db9dc1b42"></a>

```c
typedef int(* pcie_ep_api_conf_read) (const struct device *dev, uint32_t offset, uint32_t *data)
```

相关声明：[pcie_ep_api_conf_read](#gaf930f31c5b6e0e37fe6ca72db9dc1b42)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取配置空间（Configuration Space）的 PCIe EP API 函数类型定义。

<a id="r_gadfc3c945b5c3dacb1e382d89a5b865ce"></a>

```c
typedef void(* pcie_ep_api_conf_write) (const struct device *dev, uint32_t offset, uint32_t data)
```

相关声明：[pcie_ep_api_conf_write](#gadfc3c945b5c3dacb1e382d89a5b865ce)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

写入配置空间（Configuration Space）的 PCIe EP API 函数类型定义。

<a id="r_gadfb660fc4b986e8c2cf553fca0f38ac9"></a>

```c
typedef int(* pcie_ep_api_map_addr) (const struct device *dev, uint64_t pcie_addr, uint64_t *mapped_addr, uint32_t size, enum pcie_ob_mem_type ob_mem_type)
```

相关声明：[pcie_ep_api_map_addr](#gadfb660fc4b986e8c2cf553fca0f38ac9)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pcie_ob_mem_type](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aa7c51648c5a1663dd4dec689727a510b)。

映射主机地址（Host Address）的 PCIe EP API 函数类型定义。

<a id="r_gaa7231fbcd7efca29778b13ee608001cf"></a>

```c
typedef void(* pcie_ep_api_unmap_addr) (const struct device *dev, uint64_t mapped_addr)
```

相关声明：[pcie_ep_api_unmap_addr](#gaa7231fbcd7efca29778b13ee608001cf)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

取消主机地址映射（Unmap Host Address）的 PCIe EP API 函数类型定义。

<a id="r_ga18f49605c9f9dc21b0fc2f8dc4329c4b"></a>

```c
typedef int(* pcie_ep_api_raise_irq) (const struct device *dev, enum pci_ep_irq_type irq_type, uint32_t irq_num)
```

相关声明：[pcie_ep_api_raise_irq](#ga18f49605c9f9dc21b0fc2f8dc4329c4b)、[device](../device_reference/P002_设备对象结构.md)、[pci_ep_irq_type](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aba0e572125869b246d4968ee164f3800)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向主机（Host）触发中断的 PCIe EP API 函数类型定义。

<a id="r_ga0f1a5b8996bc38843d58111fd4ed2358"></a>

```c
typedef int(* pcie_ep_api_register_reset_cb) (const struct device *dev, enum pcie_reset reset, pcie_ep_reset_callback_t cb, void *arg)
```

相关声明：[pcie_ep_api_register_reset_cb](#ga0f1a5b8996bc38843d58111fd4ed2358)、[device](../device_reference/P002_设备对象结构.md)、[pcie_reset](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a7b0f0f4693b7d11b973bfd62ac1b35cd)、[pcie_ep_reset_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#afcde72dd6977ee7de9ebf4146113f912)。

注册复位回调（Reset Callback）的 PCIe EP API 函数类型定义。

<a id="r_ga5cfa1468780b4e37120d76b156892b3f"></a>

```c
typedef int(* pcie_ep_api_dma_xfer) (const struct device *dev, uint64_t mapped_addr, uintptr_t local_addr, uint32_t size, enum xfer_direction dir)
```

相关声明：[pcie_ep_api_dma_xfer](#ga5cfa1468780b4e37120d76b156892b3f)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[xfer_direction](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#acd2605f2fb5676ded5f125712681d458)。

使用系统 DMA 传输数据的 PCIe EP API 函数类型定义。

## 13.3\_详细说明（Detailed Documentation）

<a id="gaf930f31c5b6e0e37fe6ca72db9dc1b42"></a>

### `pcie_ep_api_conf_read`

```c
typedef int(* pcie_ep_api_conf_read) (const struct device *dev, uint32_t offset, uint32_t *data)
```

```c
#include <zephyr/drivers/pcie/endpoint/pcie_ep.h>
```

读取配置空间（Configuration Space）的 PCIe EP API 函数类型定义。

参数说明参见 `pcie_ep_conf_read()`。

<a id="gadfc3c945b5c3dacb1e382d89a5b865ce"></a>

### `pcie_ep_api_conf_write`

```c
typedef void(* pcie_ep_api_conf_write) (const struct device *dev, uint32_t offset, uint32_t data)
```

```c
#include <zephyr/drivers/pcie/endpoint/pcie_ep.h>
```

写入配置空间（Configuration Space）的 PCIe EP API 函数类型定义。

参数说明参见 `pcie_ep_conf_write()`。

<a id="ga5cfa1468780b4e37120d76b156892b3f"></a>

### `pcie_ep_api_dma_xfer`

```c
typedef int(* pcie_ep_api_dma_xfer) (const struct device *dev, uint64_t mapped_addr, uintptr_t local_addr, uint32_t size, enum xfer_direction dir)
```

```c
#include <zephyr/drivers/pcie/endpoint/pcie_ep.h>
```

使用系统 DMA 传输数据的 PCIe EP API 函数类型定义。

参数说明参见 `pcie_ep_dma_xfer()`。

<a id="gadfb660fc4b986e8c2cf553fca0f38ac9"></a>

### `pcie_ep_api_map_addr`

```c
typedef int(* pcie_ep_api_map_addr) (const struct device *dev, uint64_t pcie_addr, uint64_t *mapped_addr, uint32_t size, enum pcie_ob_mem_type ob_mem_type)
```

```c
#include <zephyr/drivers/pcie/endpoint/pcie_ep.h>
```

映射主机地址（Host Address）的 PCIe EP API 函数类型定义。

参数说明参见 `pcie_ep_map_addr()`。

<a id="ga18f49605c9f9dc21b0fc2f8dc4329c4b"></a>

### `pcie_ep_api_raise_irq`

```c
typedef int(* pcie_ep_api_raise_irq) (const struct device *dev, enum pci_ep_irq_type irq_type, uint32_t irq_num)
```

```c
#include <zephyr/drivers/pcie/endpoint/pcie_ep.h>
```

向主机（Host）触发中断的 PCIe EP API 函数类型定义。

参数说明参见 `pcie_ep_raise_irq()`。

<a id="ga0f1a5b8996bc38843d58111fd4ed2358"></a>

### `pcie_ep_api_register_reset_cb`

```c
typedef int(* pcie_ep_api_register_reset_cb) (const struct device *dev, enum pcie_reset reset, pcie_ep_reset_callback_t cb, void *arg)
```

```c
#include <zephyr/drivers/pcie/endpoint/pcie_ep.h>
```

注册复位回调（Reset Callback）的 PCIe EP API 函数类型定义。

参数说明参见 `pcie_ep_register_reset_cb()`。

<a id="gaa7231fbcd7efca29778b13ee608001cf"></a>

### `pcie_ep_api_unmap_addr`

```c
typedef void(* pcie_ep_api_unmap_addr) (const struct device *dev, uint64_t mapped_addr)
```

```c
#include <zephyr/drivers/pcie/endpoint/pcie_ep.h>
```

取消主机地址映射（Unmap Host Address）的 PCIe EP API 函数类型定义。

参数说明参见 `pcie_ep_unmap_addr()`。


## 13.4\_原页交叉引用（Cross References）

- [pcie_ep_driver_api](../platform_security_model_reference/P029_pcie_ep_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [pcie_ob_mem_type](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aa7c51648c5a1663dd4dec689727a510b)
- [pci_ep_irq_type](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aba0e572125869b246d4968ee164f3800)
- [pcie_reset](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a7b0f0f4693b7d11b973bfd62ac1b35cd)
- [pcie_ep_reset_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#afcde72dd6977ee7de9ebf4146113f912)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [xfer_direction](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#acd2605f2fb5676ded5f125712681d458)
- [zephyr/drivers/pcie/endpoint/pcie_ep.h](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html)
- [pcie_ep_conf_read()](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#ad35d42579500a959bb3275cd65b04a42)
- [pcie_ep_conf_write()](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a8d3f4de13956fbd7ed71acbd387f781a)
- [pcie_ep_dma_xfer()](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a7c450e4f9d65aade3f912b72b38ed04d)
- [pcie_ep_map_addr()](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a7bcff5f22fd32e0b2c3c3c509038b2db)
- [pcie_ep_raise_irq()](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#aec421e689d4d72b0bf8a34fe8303b103)
- [pcie_ep_register_reset_cb()](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a4e9cc8364703bb58e96642d1250dc410)
- [pcie_ep_unmap_addr()](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h.html#a07ee4ed9ceb42462c95da8bbf3dfc8f7)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P012_应用接收端（Application sinks）.md) · [返回大纲](大纲.md) · [下一章](P014_PCIe 虚拟通道（Virtual Channel）主机接口.md)
