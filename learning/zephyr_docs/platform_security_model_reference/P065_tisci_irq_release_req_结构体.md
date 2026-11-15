---
id: learning.zephyr-docs.platform-security-model-reference.page-65
title: tisci_irq_release_req_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtisci__irq__release__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_tisci\_irq\_release\_req\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtisci__irq__release__req.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

释放中断外设资源（Interrupt Peripheral Resources）的请求。

```c
#include <zephyr/drivers/firmware/tisci/tisci.h>
```

<a id="details"></a>

释放中断外设资源的请求（Request）。根据所提供的有效配置释放中断外设资源。

参数（Parameters）：

- `valid_params`：定义中断路由释放参数有效性的位域，每一位对应一个字段是否有效。
- `src_id`：中断源外设的 ID。
- `src_index`：源外设内部的中断源索引。
- `dst_id`：SoC 中断路由器（IR）的设备 ID；设置 `TISCI_MSG_VALUE_RM_DST_ID_VALID` 时有效。
- `dst_host_irq`：SoC IR 输出索引；设置 `TISCI_MSG_VALUE_RM_DST_HOST_IRQ_VALID` 时有效。
- `ia_id`：中断聚合器（Interrupt aggregator）的设备 ID；设置 `TISCI_MSG_VALUE_RM_IA_ID_VALID` 时有效。
- `vint`：虚拟中断号；设置 `TISCI_MSG_VALUE_RM_VINT_VALID` 时有效。
- `global_event`：映射到中断聚合器的全局事件；设置 `TISCI_MSG_VALUE_RM_GLOBAL_EVENT_VALID` 时有效。
- `vint_status_bit_index`：虚拟中断状态位；设置 `TISCI_MSG_VALUE_RM_VINT_STATUS_BIT_INDEX_VALID` 时有效。
- `secondary_host`：次级主机值；设置 `TISCI_MSG_VALUE_RM_SECONDARY_HOST_VALID` 时有效。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_a068b9b4217d606f03898bdca2219bbf0"></a>

```c
uint32_t valid_params
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[valid_params](#a068b9b4217d606f03898bdca2219bbf0)。

<a id="r_adddef8e01c4ecd9b44327418bcc8a3ef"></a>

```c
uint16_t src_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[src_id](#adddef8e01c4ecd9b44327418bcc8a3ef)。

<a id="r_abb9cedc15e5923125e57f153ee1ed22a"></a>

```c
uint16_t src_index
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[src_index](#abb9cedc15e5923125e57f153ee1ed22a)。

<a id="r_ae646b23593b5f724fca6800c5c2e76bf"></a>

```c
uint16_t dst_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dst_id](#ae646b23593b5f724fca6800c5c2e76bf)。

<a id="r_a3643554ea453300f33806b5128cc6c0a"></a>

```c
uint16_t dst_host_irq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dst_host_irq](#a3643554ea453300f33806b5128cc6c0a)。

<a id="r_aa6c09862a5e955a5ccbb78c7df2675fa"></a>

```c
uint16_t ia_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ia_id](#aa6c09862a5e955a5ccbb78c7df2675fa)。

<a id="r_a754e7c93d218a58e2bc18fd4ec086e40"></a>

```c
uint16_t vint
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[vint](#a754e7c93d218a58e2bc18fd4ec086e40)。

<a id="r_a12eb81324f28254daece1170b1e6764d"></a>

```c
uint16_t global_event
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[global_event](#a12eb81324f28254daece1170b1e6764d)。

<a id="r_aedc07d5425720146b75b6757ca17c0d3"></a>

```c
uint8_t vint_status_bit_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[vint_status_bit_index](#aedc07d5425720146b75b6757ca17c0d3)。

<a id="r_a032e94a7d3c7384dc1f36c08b2d73e71"></a>

```c
uint8_t secondary_host
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[secondary_host](#a032e94a7d3c7384dc1f36c08b2d73e71)。

## 65.2\_详细说明（Detailed Documentation）

<a id="a3643554ea453300f33806b5128cc6c0a"></a>

### `dst_host_irq`

```c
uint16_t tisci_irq_release_req::dst_host_irq
```

<a id="ae646b23593b5f724fca6800c5c2e76bf"></a>

### `dst_id`

```c
uint16_t tisci_irq_release_req::dst_id
```

<a id="a12eb81324f28254daece1170b1e6764d"></a>

### `global_event`

```c
uint16_t tisci_irq_release_req::global_event
```

<a id="aa6c09862a5e955a5ccbb78c7df2675fa"></a>

### `ia_id`

```c
uint16_t tisci_irq_release_req::ia_id
```

<a id="a032e94a7d3c7384dc1f36c08b2d73e71"></a>

### `secondary_host`

```c
uint8_t tisci_irq_release_req::secondary_host
```

<a id="adddef8e01c4ecd9b44327418bcc8a3ef"></a>

### `src_id`

```c
uint16_t tisci_irq_release_req::src_id
```

<a id="abb9cedc15e5923125e57f153ee1ed22a"></a>

### `src_index`

```c
uint16_t tisci_irq_release_req::src_index
```

<a id="a068b9b4217d606f03898bdca2219bbf0"></a>

### `valid_params`

```c
uint32_t tisci_irq_release_req::valid_params
```

<a id="a754e7c93d218a58e2bc18fd4ec086e40"></a>

### `vint`

```c
uint16_t tisci_irq_release_req::vint
```

<a id="aedc07d5425720146b75b6757ca17c0d3"></a>

### `vint_status_bit_index`

```c
uint8_t tisci_irq_release_req::vint_status_bit_index
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/tisci/tisci.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/tisci/tisci.h](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_tisci_clock_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_tisci_irq_set_req_结构体.md)
