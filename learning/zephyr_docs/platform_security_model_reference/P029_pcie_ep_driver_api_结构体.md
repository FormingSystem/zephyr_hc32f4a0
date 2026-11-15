---
id: learning.zephyr-docs.platform-security-model-reference.page-29
title: pcie_ep_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpcie__ep__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_pcie\_ep\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpcie__ep__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：PCIe端点（Endpoint）驱动操作。

```c
#include <zephyr/drivers/pcie/endpoint/pcie_ep.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：PCIe 端点（Endpoint）驱动操作。这是每个 PCIe 端点驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_aaae0fe7f4d58da035289da02e0d33111"></a>

```c
pcie_ep_api_conf_read conf_read
```

相关声明：[pcie_ep_api_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#gaf930f31c5b6e0e37fe6ca72db9dc1b42)、[conf_read](#aaae0fe7f4d58da035289da02e0d33111)。

必需（REQ）：读取 PCIe 端点（EP）配置空间。

<a id="r_af651a646631e13fc0e4989cea4df9735"></a>

```c
pcie_ep_api_conf_write conf_write
```

相关声明：[pcie_ep_api_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#gadfc3c945b5c3dacb1e382d89a5b865ce)、[conf_write](#af651a646631e13fc0e4989cea4df9735)。

必需（REQ）：写入 PCIe 端点配置空间。

<a id="r_a7ca1ee31f72b14db3acf2a0f5b0aab9c"></a>

```c
pcie_ep_api_map_addr map_addr
```

相关声明：[pcie_ep_api_map_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#gadfb660fc4b986e8c2cf553fca0f38ac9)、[map_addr](#a7ca1ee31f72b14db3acf2a0f5b0aab9c)。

必需（REQ）：将主机内存缓冲区映射到 PCIe 出站区域（outbound region）。

<a id="r_a603366158e0204896380425461cdbbcc"></a>

```c
pcie_ep_api_unmap_addr unmap_addr
```

相关声明：[pcie_ep_api_unmap_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#gaa7231fbcd7efca29778b13ee608001cf)、[unmap_addr](#a603366158e0204896380425461cdbbcc)。

必需（REQ）：移除到 PCIe 出站区域的映射。

<a id="r_a9a63bde4308d3d0dc86d0ed7d19cc192"></a>

```c
pcie_ep_api_raise_irq raise_irq
```

相关声明：[pcie_ep_api_raise_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#ga18f49605c9f9dc21b0fc2f8dc4329c4b)、[raise_irq](#a9a63bde4308d3d0dc86d0ed7d19cc192)。

必需（REQ）：向主机触发中断。

<a id="r_ac1c11775d08023e1d9c3ad9b46d77785"></a>

```c
pcie_ep_api_register_reset_cb register_reset_cb
```

相关声明：[pcie_ep_api_register_reset_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#ga0f1a5b8996bc38843d58111fd4ed2358)、[register_reset_cb](#ac1c11775d08023e1d9c3ad9b46d77785)。

可选（OPT）：注册复位中断的回调函数。

<a id="r_abdc6da0a251d4281bfe8533b8be6a66f"></a>

```c
pcie_ep_api_dma_xfer dma_xfer
```

相关声明：[pcie_ep_api_dma_xfer](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#ga5cfa1468780b4e37120d76b156892b3f)、[dma_xfer](#abdc6da0a251d4281bfe8533b8be6a66f)。

可选（OPT）：使用系统 DMA（System DMA），在已映射的主机内存与设备内存之间传输数据。

## 29.2\_详细说明（Detailed Documentation）

<a id="aaae0fe7f4d58da035289da02e0d33111"></a>

### `conf_read`

```c
pcie_ep_api_conf_read pcie_ep_driver_api::conf_read
```

必需（REQ）：读取 PCIe 端点（EP）配置空间。

<a id="af651a646631e13fc0e4989cea4df9735"></a>

### `conf_write`

```c
pcie_ep_api_conf_write pcie_ep_driver_api::conf_write
```

必需（REQ）：写入 PCIe 端点配置空间。

<a id="abdc6da0a251d4281bfe8533b8be6a66f"></a>

### `dma_xfer`

```c
pcie_ep_api_dma_xfer pcie_ep_driver_api::dma_xfer
```

可选（OPT）：使用系统 DMA（System DMA），在已映射的主机内存与设备内存之间传输数据。

<a id="a7ca1ee31f72b14db3acf2a0f5b0aab9c"></a>

### `map_addr`

```c
pcie_ep_api_map_addr pcie_ep_driver_api::map_addr
```

必需（REQ）：将主机内存缓冲区映射到 PCIe 出站区域（outbound region）。

<a id="a9a63bde4308d3d0dc86d0ed7d19cc192"></a>

### `raise_irq`

```c
pcie_ep_api_raise_irq pcie_ep_driver_api::raise_irq
```

必需（REQ）：向主机触发中断。

<a id="ac1c11775d08023e1d9c3ad9b46d77785"></a>

### `register_reset_cb`

```c
pcie_ep_api_register_reset_cb pcie_ep_driver_api::register_reset_cb
```

可选（OPT）：注册复位中断的回调函数。

<a id="a603366158e0204896380425461cdbbcc"></a>

### `unmap_addr`

```c
pcie_ep_api_unmap_addr pcie_ep_driver_api::unmap_addr
```

必需（REQ）：移除到 PCIe 出站区域的映射。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pcie/endpoint/pcie_ep.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pcie/endpoint/pcie_ep.h](https://docs.zephyrproject.org/latest/doxygen/html/pcie__ep_8h_source.html)
- [pcie_ep_api_conf_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#gaf930f31c5b6e0e37fe6ca72db9dc1b42)
- [pcie_ep_api_conf_write](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#gadfc3c945b5c3dacb1e382d89a5b865ce)
- [pcie_ep_api_map_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#gadfb660fc4b986e8c2cf553fca0f38ac9)
- [pcie_ep_api_unmap_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#gaa7231fbcd7efca29778b13ee608001cf)
- [pcie_ep_api_raise_irq](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#ga18f49605c9f9dc21b0fc2f8dc4329c4b)
- [pcie_ep_api_register_reset_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#ga0f1a5b8996bc38843d58111fd4ed2358)
- [pcie_ep_api_dma_xfer](https://docs.zephyrproject.org/latest/doxygen/html/group__pcie__interface__backend.html#ga5cfa1468780b4e37120d76b156892b3f)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_pcie_dev_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_pcie_scan_opt_结构体.md)
