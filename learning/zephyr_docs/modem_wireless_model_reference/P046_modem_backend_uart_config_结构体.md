---
id: learning.zephyr-docs.modem-wireless-model-reference.page-46
title: modem_backend_uart_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__uart__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_modem\_backend\_uart\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__uart__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/backend/uart.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_a4f8752a33e75164370a8eb81615c2555"></a>

```c
const struct device * uart
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[uart](#a4f8752a33e75164370a8eb81615c2555)。

<a id="r_a3dad78dbaddbdc94c57f5381d9a5c68f"></a>

```c
const struct gpio_dt_spec * dtr_gpio
```

相关声明：[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[dtr_gpio](#a3dad78dbaddbdc94c57f5381d9a5c68f)。

<a id="r_ad80a5bd5efcf37931503049ac2ba788d"></a>

```c
uint8_t * receive_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[receive_buf](#ad80a5bd5efcf37931503049ac2ba788d)。

<a id="r_a2576f671e21a1fa75163ac63ac5e56a4"></a>

```c
uint32_t receive_buf_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[receive_buf_size](#a2576f671e21a1fa75163ac63ac5e56a4)。

<a id="r_a64f82b3b4bf6d1ff6081ac075b67a0b0"></a>

```c
uint8_t * transmit_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transmit_buf](#a64f82b3b4bf6d1ff6081ac075b67a0b0)。

<a id="r_a48c4a5e9de64bcb435d9b8aea05bfd87"></a>

```c
uint32_t transmit_buf_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[transmit_buf_size](#a48c4a5e9de64bcb435d9b8aea05bfd87)。

## 46.2\_详细说明（Detailed Documentation）

<a id="a3dad78dbaddbdc94c57f5381d9a5c68f"></a>

### `dtr_gpio`

```c
const struct gpio_dt_spec* modem_backend_uart_config::dtr_gpio
```

<a id="ad80a5bd5efcf37931503049ac2ba788d"></a>

### `receive_buf`

```c
uint8_t* modem_backend_uart_config::receive_buf
```

<a id="a2576f671e21a1fa75163ac63ac5e56a4"></a>

### `receive_buf_size`

```c
uint32_t modem_backend_uart_config::receive_buf_size
```

<a id="a64f82b3b4bf6d1ff6081ac075b67a0b0"></a>

### `transmit_buf`

```c
uint8_t* modem_backend_uart_config::transmit_buf
```

<a id="a48c4a5e9de64bcb435d9b8aea05bfd87"></a>

### `transmit_buf_size`

```c
uint32_t modem_backend_uart_config::transmit_buf_size
```

<a id="a4f8752a33e75164370a8eb81615c2555"></a>

### `uart`

```c
const struct device* modem_backend_uart_config::uart
```

本数据类型文档由以下文件生成：

- `zephyr/modem/backend/uart.h`

## 46.3\_原页交叉引用（Cross References）

- [zephyr/modem/backend/uart.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2uart_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_modem_backend_uart_async_common_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_modem_backend_uart_isr_结构体.md)
