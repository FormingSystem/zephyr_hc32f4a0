---
id: learning.zephyr-docs.device-power-control-model-reference.page-97
title: usb_hub_descriptor_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusb__hub__descriptor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第97章\_usb\_hub\_descriptor\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusb__hub__descriptor.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB集线器描述符（Hub Descriptor）。

```c
#include <zephyr/usb/class/usb_hub.h>
```

<a id="details"></a>

USB 集线器描述符（Hub Descriptor），参见规范表 11-13。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 97.1\_数据成员（Data Fields）

<a id="r_afeed7baf0d900ac0bcaac30afe65ee40"></a>

```c
uint8_t bDescLength
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescLength](#afeed7baf0d900ac0bcaac30afe65ee40)。

描述符长度。

<a id="r_a2e62093b8304fe73becf63e8aa782c07"></a>

```c
uint8_t bDescriptorType
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bDescriptorType](#a2e62093b8304fe73becf63e8aa782c07)。

描述符类型。

<a id="r_af3d2523eaa7a4bd827105d9b61dcc8f0"></a>

```c
uint8_t bNbrPorts
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bNbrPorts](#af3d2523eaa7a4bd827105d9b61dcc8f0)。

面向下游端口（Downstream facing ports）的数量。

<a id="r_a1023ff5e3940284d86cf50fa25790ffe"></a>

```c
uint16_t wHubCharacteristics
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[wHubCharacteristics](#a1023ff5e3940284d86cf50fa25790ffe)。

集线器特性位图（Hub characteristics bitmap）。

<a id="r_ac4ef3bbf42df2e2caf582b566181a6a3"></a>

```c
uint8_t bPwrOn2PwrGood
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bPwrOn2PwrGood](#ac4ef3bbf42df2e2caf582b566181a6a3)。

从上电到电源就绪（Power-good）的时间，以 2 ms 为单位。

<a id="r_a59dc42682121858aaeafac01deccd4e2"></a>

```c
uint8_t bHubContrCurrent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bHubContrCurrent](#a59dc42682121858aaeafac01deccd4e2)。

集线器控制器所需的最大电流，单位为 mA。

## 97.2\_详细说明（Detailed Documentation）

<a id="afeed7baf0d900ac0bcaac30afe65ee40"></a>

### `bDescLength`

```c
uint8_t usb_hub_descriptor::bDescLength
```

描述符长度。

<a id="a2e62093b8304fe73becf63e8aa782c07"></a>

### `bDescriptorType`

```c
uint8_t usb_hub_descriptor::bDescriptorType
```

描述符类型。

<a id="a59dc42682121858aaeafac01deccd4e2"></a>

### `bHubContrCurrent`

```c
uint8_t usb_hub_descriptor::bHubContrCurrent
```

集线器控制器所需的最大电流，单位为 mA。

<a id="af3d2523eaa7a4bd827105d9b61dcc8f0"></a>

### `bNbrPorts`

```c
uint8_t usb_hub_descriptor::bNbrPorts
```

面向下游端口（Downstream facing ports）的数量。

<a id="ac4ef3bbf42df2e2caf582b566181a6a3"></a>

### `bPwrOn2PwrGood`

```c
uint8_t usb_hub_descriptor::bPwrOn2PwrGood
```

从上电到电源就绪（Power-good）的时间，以 2 ms 为单位。

<a id="a1023ff5e3940284d86cf50fa25790ffe"></a>

### `wHubCharacteristics`

```c
uint16_t usb_hub_descriptor::wHubCharacteristics
```

集线器特性位图（Hub characteristics bitmap）。

本数据类型文档由以下文件生成：

- `zephyr/usb/class/usb_hub.h`

## 97.3\_原页交叉引用（Cross References）

- [zephyr/usb/class/usb_hub.h](https://docs.zephyrproject.org/latest/doxygen/html/usb__hub_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P096_tmc6460_field_结构体.md) · [返回大纲](大纲.md) · [下一章](P098_usb_hub_port_status_结构体.md)
