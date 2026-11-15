---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-93
title: smbus_dt_spec_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsmbus__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第93章\_smbus\_dt\_spec\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsmbus__dt__spec.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

完整的系统管理总线（SMBus）设备树（DT）信息。

```c
#include <zephyr/drivers/smbus.h>
```

<a id="details"></a>

完整的系统管理总线（SMBus）设备树（DT）信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 93.1\_数据成员（Data Fields）

<a id="r_a2b34afb2bc5d55382bc11e0a5ee72684"></a>

```c
const struct device * bus
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[bus](#a2b34afb2bc5d55382bc11e0a5ee72684)。

SMBus 总线。

<a id="r_a0f6080e33e04405a42e9d29118512d08"></a>

```c
uint16_t addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[addr](#a0f6080e33e04405a42e9d29118512d08)。

SMBus 外设的地址。

## 93.2\_详细说明（Detailed Documentation）

<a id="a0f6080e33e04405a42e9d29118512d08"></a>

### `addr`

```c
uint16_t smbus_dt_spec::addr
```

SMBus 外设的地址。

<a id="a2b34afb2bc5d55382bc11e0a5ee72684"></a>

### `bus`

```c
const struct device* smbus_dt_spec::bus
```

SMBus 总线。

本数据类型文档由以下文件生成：

- `zephyr/drivers/smbus.h`

## 93.3\_原页交叉引用（Cross References）

- [zephyr/drivers/smbus.h](https://docs.zephyrproject.org/latest/doxygen/html/smbus_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P092_smbus_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P094_swdp_api_结构体.md)
