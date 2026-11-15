---
id: learning.zephyr-docs.platform-security-model-reference.page-66
title: tisci_irq_set_req_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtisci__irq__set__req.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_tisci\_irq\_set\_req\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtisci__irq__set__req.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设置中断路由（Interrupt Route）的请求。

```c
#include <zephyr/drivers/firmware/tisci/tisci.h>
```

<a id="details"></a>

设置中断路由（Interrupt route）的请求。根据所提供的有效配置，配置中断子系统内的外设。

参数（Parameters）：

- `valid_params`：定义中断路由设置参数有效性的位域，每一位对应一个字段是否有效。
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

## 66.1\_数据成员（Data Fields）

<a id="r_ac5dddf4f1bc933e82eb7dfdfdfb35307"></a>

```c
uint32_t valid_params
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[valid_params](#ac5dddf4f1bc933e82eb7dfdfdfb35307)。

<a id="r_af1c6cc734902f14d51ff46c971c1a576"></a>

```c
uint16_t src_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[src_id](#af1c6cc734902f14d51ff46c971c1a576)。

<a id="r_a290247006f410254d3a4dbcdefc0ba75"></a>

```c
uint16_t src_index
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[src_index](#a290247006f410254d3a4dbcdefc0ba75)。

<a id="r_a2a17ba4d83290d1ca8ae8bf39760a31a"></a>

```c
uint16_t dst_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dst_id](#a2a17ba4d83290d1ca8ae8bf39760a31a)。

<a id="r_a1b01430d7e9140891589f0e48e79590a"></a>

```c
uint16_t dst_host_irq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dst_host_irq](#a1b01430d7e9140891589f0e48e79590a)。

<a id="r_a2b8fd0bc0825d47fba8c961f68fcaef4"></a>

```c
uint16_t ia_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ia_id](#a2b8fd0bc0825d47fba8c961f68fcaef4)。

<a id="r_a2e3dd0054d9d0b029a6821f4df0af4ea"></a>

```c
uint16_t vint
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[vint](#a2e3dd0054d9d0b029a6821f4df0af4ea)。

<a id="r_ab5f9849aef439771e81daf6a98303d17"></a>

```c
uint16_t global_event
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[global_event](#ab5f9849aef439771e81daf6a98303d17)。

<a id="r_a94ad73384be1f64054829a32ad70b066"></a>

```c
uint8_t vint_status_bit_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[vint_status_bit_index](#a94ad73384be1f64054829a32ad70b066)。

<a id="r_ad122a8cf2af3f3df9615c3ca70ed3b06"></a>

```c
uint8_t secondary_host
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[secondary_host](#ad122a8cf2af3f3df9615c3ca70ed3b06)。

## 66.2\_详细说明（Detailed Documentation）

<a id="a1b01430d7e9140891589f0e48e79590a"></a>

### `dst_host_irq`

```c
uint16_t tisci_irq_set_req::dst_host_irq
```

<a id="a2a17ba4d83290d1ca8ae8bf39760a31a"></a>

### `dst_id`

```c
uint16_t tisci_irq_set_req::dst_id
```

<a id="ab5f9849aef439771e81daf6a98303d17"></a>

### `global_event`

```c
uint16_t tisci_irq_set_req::global_event
```

<a id="a2b8fd0bc0825d47fba8c961f68fcaef4"></a>

### `ia_id`

```c
uint16_t tisci_irq_set_req::ia_id
```

<a id="ad122a8cf2af3f3df9615c3ca70ed3b06"></a>

### `secondary_host`

```c
uint8_t tisci_irq_set_req::secondary_host
```

<a id="af1c6cc734902f14d51ff46c971c1a576"></a>

### `src_id`

```c
uint16_t tisci_irq_set_req::src_id
```

<a id="a290247006f410254d3a4dbcdefc0ba75"></a>

### `src_index`

```c
uint16_t tisci_irq_set_req::src_index
```

<a id="ac5dddf4f1bc933e82eb7dfdfdfb35307"></a>

### `valid_params`

```c
uint32_t tisci_irq_set_req::valid_params
```

<a id="a2e3dd0054d9d0b029a6821f4df0af4ea"></a>

### `vint`

```c
uint16_t tisci_irq_set_req::vint
```

<a id="a94ad73384be1f64054829a32ad70b066"></a>

### `vint_status_bit_index`

```c
uint8_t tisci_irq_set_req::vint_status_bit_index
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/firmware/tisci/tisci.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/drivers/firmware/tisci/tisci.h](https://docs.zephyrproject.org/latest/doxygen/html/tisci_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_tisci_irq_release_req_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_tisci_msg_fwl_owner_结构体.md)
