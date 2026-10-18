---
id: learning.zephyr-docs.platform-security-model-reference.page-26
title: pcie_ctrl_config_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpcie__ctrl__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_pcie\_ctrl\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpcie__ctrl__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

描述支持PCI Express控制器API（Controller API）的设备的结构。

```c
#include <zephyr/drivers/pcie/controller.h>
```

<a id="details"></a>

描述支持PCI Express控制器API（Controller API）的设备的结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

<a id="r_a6881d50254b57164f546af66e2773d13"></a>

```c
const struct device * msi_parent
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[msi_parent](#a6881d50254b57164f546af66e2773d13)。

消息信号中断（MSI）父设备。

<a id="r_a3de0f32aaf3ddb377897974dfdfe67bd"></a>

```c
uintptr_t cfg_addr
```

相关声明：[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[cfg_addr](#a3de0f32aaf3ddb377897974dfdfe67bd)。

配置空间（configuration space）的物理地址。

<a id="r_adb1b8ed76f3f994f2da72c8e8b40d4f0"></a>

```c
size_t cfg_size
```

相关声明：[cfg_size](#adb1b8ed76f3f994f2da72c8e8b40d4f0)。

配置空间的物理大小。

<a id="r_a4a620f03546490b65ba4d097329928e8"></a>

```c
size_t ranges_count
```

相关声明：[ranges_count](#a4a620f03546490b65ba4d097329928e8)。

基地址寄存器（BAR）区域地址转换范围的数量。

```c
struct {
```

<a id="r_ab7e9052a2877e8c2f1823f2661de29f5"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#a90e48aaca78a8284caa449ee3972d87b)。

《PCI 总线与 IEEE Std 1275-1994 的绑定（PCI Bus Binding to IEEE Std 1275-1994）》中定义的标志。

<a id="r_aad8d81d90a9bfaa9d638c1d34817a3dc"></a>

```c
uintptr_t pcie_bus_addr
```

相关声明：[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[pcie_bus_addr](#a45f9fa1124aa64bbfd7ff2c5519cbb4b)。

相对于区域起点、以总线为参照的偏移量。

<a id="r_a9caf0c35549be1d591d712c24dbc023e"></a>

```c
uintptr_t host_map_addr
```

相关声明：[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[host_map_addr](#ace0b3505edc0aff3678a91b630244963)。

相对于区域起点、以 CPU 为参照的偏移量。

<a id="r_a894c4785bce386c2c9ece086754056fc"></a>

```c
size_t map_length
```

相关声明：[map_length](#ae3dd8d3d72a1597ee135b49e46e31bec)。

区域大小。

<a id="r_a1a59bec03927f2c6b5fd0aed8c36e6b4"></a>

```c
} ranges []
```

相关声明：[ranges](#a1a59bec03927f2c6b5fd0aed8c36e6b4)。

BAR 区域地址转换范围表。

## 26.2\_详细说明（Detailed Documentation）

<a id="a3de0f32aaf3ddb377897974dfdfe67bd"></a>

### `cfg_addr`

```c
uintptr_t pcie_ctrl_config::cfg_addr
```

配置空间（configuration space）的物理地址。

<a id="adb1b8ed76f3f994f2da72c8e8b40d4f0"></a>

### `cfg_size`

```c
size_t pcie_ctrl_config::cfg_size
```

配置空间的物理大小。

<a id="a90e48aaca78a8284caa449ee3972d87b"></a>

### `flags`

```c
uint32_t pcie_ctrl_config::flags
```

《PCI 总线与 IEEE Std 1275-1994 的绑定（PCI Bus Binding to IEEE Std 1275-1994）》中定义的标志。

<a id="ace0b3505edc0aff3678a91b630244963"></a>

### `host_map_addr`

```c
uintptr_t pcie_ctrl_config::host_map_addr
```

相对于区域起点、以 CPU 为参照的偏移量。

<a id="ae3dd8d3d72a1597ee135b49e46e31bec"></a>

### `map_length`

```c
size_t pcie_ctrl_config::map_length
```

区域大小。

<a id="a6881d50254b57164f546af66e2773d13"></a>

### `msi_parent`

```c
const struct device* pcie_ctrl_config::msi_parent
```

消息信号中断（MSI）父设备。

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_PCIE_MSI`。

<a id="a45f9fa1124aa64bbfd7ff2c5519cbb4b"></a>

### `pcie_bus_addr`

```c
uintptr_t pcie_ctrl_config::pcie_bus_addr
```

相对于区域起点、以总线为参照的偏移量。

<a id="a1a59bec03927f2c6b5fd0aed8c36e6b4"></a>

### `[struct]`

```c
struct { ... } pcie_ctrl_config::ranges[]
```

BAR 区域地址转换范围表。

<a id="a4a620f03546490b65ba4d097329928e8"></a>

### `ranges_count`

```c
size_t pcie_ctrl_config::ranges_count
```

基地址寄存器（BAR）区域地址转换范围的数量。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pcie/controller.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pcie/controller.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2pcie_2controller_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [CONFIG_PCIE_MSI](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_MSI)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_pcie_bar_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_pcie_ctrl_driver_api_结构体.md)
