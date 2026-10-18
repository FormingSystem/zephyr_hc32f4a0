---
id: learning.zephyr-docs.modem-wireless-model-reference.page-43
title: modem_backend_uart_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__uart.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_modem\_backend\_uart\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__uart.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/backend/uart.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_a26f3331f0ae7d9384f369ae50694090d"></a>

```c
const struct device * uart
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[uart](#a26f3331f0ae7d9384f369ae50694090d)。

<a id="r_abdf5e8696db6f2732359000abbd60dca"></a>

```c
const struct gpio_dt_spec * dtr_gpio
```

相关声明：[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[dtr_gpio](#abdf5e8696db6f2732359000abbd60dca)。

<a id="r_af7e0483a6398b6893ac4693e2bc12f31"></a>

```c
struct modem_pipe pipe
```

相关声明：[pipe](#af7e0483a6398b6893ac4693e2bc12f31)。

<a id="r_a369c5fd2072e42f5eedfe03a5d312ec6"></a>

```c
struct k_work_delayable receive_ready_work
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[receive_ready_work](#a369c5fd2072e42f5eedfe03a5d312ec6)。

<a id="r_aafd345ff47cc51a9e1100604a51f6b2d"></a>

```c
struct k_work transmit_idle_work
```

相关声明：[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[transmit_idle_work](#aafd345ff47cc51a9e1100604a51f6b2d)。

```c
union {
```

<a id="r_a5714fa979ef657ec90604d684ee26d7b"></a>

```c
struct modem_backend_uart_isr isr
```

相关声明：[modem_backend_uart_isr](P047_modem_backend_uart_isr_结构体.md)、[isr](#a812165945d6a4aba4fd6bc5ba26b3082)。

<a id="r_a99f45ff6970a36b74dd6d49a4e1dbb21"></a>

```c
struct modem_backend_uart_async async
```

相关声明：[modem_backend_uart_async](P044_modem_backend_uart_async_结构体.md)、[async](#a387327d6378834136fe6a0e80cec7337)。

<a id="r_aa0880365ddedbc3e9ee3bc37a70a740e"></a>

```c
};
```

## 43.2\_详细说明（Detailed Documentation）

<a id="aa0880365ddedbc3e9ee3bc37a70a740e"></a>

### `[union]`

```c
union { ... } modem_backend_uart
```

<a id="a387327d6378834136fe6a0e80cec7337"></a>

### `async`

```c
struct modem_backend_uart_async modem_backend_uart::async
```

<a id="abdf5e8696db6f2732359000abbd60dca"></a>

### `dtr_gpio`

```c
const struct gpio_dt_spec* modem_backend_uart::dtr_gpio
```

<a id="a812165945d6a4aba4fd6bc5ba26b3082"></a>

### `isr`

```c
struct modem_backend_uart_isr modem_backend_uart::isr
```

<a id="af7e0483a6398b6893ac4693e2bc12f31"></a>

### `pipe`

```c
struct modem_pipe modem_backend_uart::pipe
```

<a id="a369c5fd2072e42f5eedfe03a5d312ec6"></a>

### `receive_ready_work`

```c
struct k_work_delayable modem_backend_uart::receive_ready_work
```

<a id="aafd345ff47cc51a9e1100604a51f6b2d"></a>

### `transmit_idle_work`

```c
struct k_work modem_backend_uart::transmit_idle_work
```

<a id="a26f3331f0ae7d9384f369ae50694090d"></a>

### `uart`

```c
const struct device* modem_backend_uart::uart
```

本数据类型文档由以下文件生成：

- `zephyr/modem/backend/uart.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/modem/backend/uart.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2uart_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [modem_backend_uart_isr](P047_modem_backend_uart_isr_结构体.md)
- [modem_backend_uart_async](P044_modem_backend_uart_async_结构体.md)
- [modem_backend_uart](P043_modem_backend_uart_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_modem_backend_tty_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_modem_backend_uart_async_结构体.md)
