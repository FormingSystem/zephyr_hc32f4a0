---
id: learning.zephyr-docs.platform-security-model-reference.page-55
title: shared_vector_desc_t_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structshared__vector__desc__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_shared\_vector\_desc\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structshared__vector__desc__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/interrupt_controller/intc_esp32.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_a36afb23eff0489280549ac96fea0ee41"></a>

```c
int disabled: 1
```

相关声明：[disabled](#a36afb23eff0489280549ac96fea0ee41)。

<a id="r_af868d1b2bf579938907ef07f5b15d517"></a>

```c
int source: 16
```

相关声明：[source](#af868d1b2bf579938907ef07f5b15d517)。

<a id="r_acb593daeddd30515742759a73fc7838f"></a>

```c
volatile uint32_t * statusreg
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[statusreg](#acb593daeddd30515742759a73fc7838f)。

<a id="r_a9078649e1b33c0ad3ee624789fda95cb"></a>

```c
uint32_t statusmask
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[statusmask](#a9078649e1b33c0ad3ee624789fda95cb)。

<a id="r_aa438daab7ce59980b664824142be8f84"></a>

```c
intr_handler_t isr
```

相关声明：[intr_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#a637aa0db4839d3e945e74c56e82218f2)、[isr](#aa438daab7ce59980b664824142be8f84)。

<a id="r_a4ab5f28adbb5115ca6a37a3ab6c5328e"></a>

```c
void * arg
```

相关声明：[arg](#a4ab5f28adbb5115ca6a37a3ab6c5328e)。

<a id="r_aee24289457fcde842c2b557bce5cd605"></a>

```c
struct shared_vector_desc_t * next
```

相关声明：[shared_vector_desc_t](P055_shared_vector_desc_t_结构体.md)、[next](#aee24289457fcde842c2b557bce5cd605)。

## 55.2\_详细说明（Detailed Documentation）

<a id="a4ab5f28adbb5115ca6a37a3ab6c5328e"></a>

### `arg`

```c
void* shared_vector_desc_t::arg
```

<a id="a36afb23eff0489280549ac96fea0ee41"></a>

### `disabled`

```c
int shared_vector_desc_t::disabled
```

<a id="aa438daab7ce59980b664824142be8f84"></a>

### `isr`

```c
intr_handler_t shared_vector_desc_t::isr
```

<a id="aee24289457fcde842c2b557bce5cd605"></a>

### `next`

```c
struct shared_vector_desc_t* shared_vector_desc_t::next
```

<a id="af868d1b2bf579938907ef07f5b15d517"></a>

### `source`

```c
int shared_vector_desc_t::source
```

<a id="a9078649e1b33c0ad3ee624789fda95cb"></a>

### `statusmask`

```c
uint32_t shared_vector_desc_t::statusmask
```

<a id="acb593daeddd30515742759a73fc7838f"></a>

### `statusreg`

```c
volatile uint32_t* shared_vector_desc_t::statusreg
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/interrupt_controller/intc_esp32.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/drivers/interrupt_controller/intc_esp32.h](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [intr_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/intc__esp32_8h.html#a637aa0db4839d3e945e74c56e82218f2)
- [shared_vector_desc_t](P055_shared_vector_desc_t_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_shared_irq_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_sip_svc_request_结构体.md)
