---
id: learning.zephyr-docs.api-connection-topic-reference.page-13
title: MDIO 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_MDIO 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现管理数据输入／输出（MDIO）驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.1\_数据结构（Data Structures）

<a id="r_mdio_5Fdriver_5Fapi"></a>

```c
struct mdio_driver_api
```

相关声明：[mdio_driver_api](../network_service_model_reference/P030_mdio_driver_api_结构体.md)。

驱动操作（Driver Operations）：管理数据输入输出（MDIO）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 13.2\_类型定义（Typedefs）

<a id="r_gadd83bf9b8e4b4bd7189bc0b814c1f535"></a>

```c
typedef int(* mdio_api_read_t) (const struct device *dev, uint8_t prtad, uint8_t regad, uint16_t *data)
```

相关声明：[mdio_api_read_t](#gadd83bf9b8e4b4bd7189bc0b814c1f535)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从 MDIO 总线读取数据。

<a id="r_ga09e5f0532a3d88249ee6e852be45e434"></a>

```c
typedef int(* mdio_api_write_t) (const struct device *dev, uint8_t prtad, uint8_t regad, uint16_t data)
```

相关声明：[mdio_api_write_t](#ga09e5f0532a3d88249ee6e852be45e434)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 MDIO 总线写入数据。

<a id="r_gaba3f545bba5aa028f50c4a7f6e43abd0"></a>

```c
typedef int(* mdio_api_read_c45_t) (const struct device *dev, uint8_t prtad, uint8_t devad, uint16_t regad, uint16_t *data)
```

相关声明：[mdio_api_read_c45_t](#gaba3f545bba5aa028f50c4a7f6e43abd0)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过第 45 条款访问方式（Clause 45 access）从 MDIO 总线读取数据。

<a id="r_ga98d32453b4b8ec4abb36113c54711570"></a>

```c
typedef int(* mdio_api_write_c45_t) (const struct device *dev, uint8_t prtad, uint8_t devad, uint16_t regad, uint16_t data)
```

相关声明：[mdio_api_write_c45_t](#ga98d32453b4b8ec4abb36113c54711570)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 Clause 45 访问方式向 MDIO 总线写入数据。

## 13.3\_详细说明（Detailed Documentation）

<a id="gaba3f545bba5aa028f50c4a7f6e43abd0"></a>

### `mdio_api_read_c45_t`

```c
typedef int(* mdio_api_read_c45_t) (const struct device *dev, uint8_t prtad, uint8_t devad, uint16_t regad, uint16_t *data)
```

```c
#include <zephyr/drivers/mdio.h>
```

通过第 45 条款访问方式（Clause 45 access）从 MDIO 总线读取数据。

参数说明参见 `mdio_read_c45()`。

<a id="gadd83bf9b8e4b4bd7189bc0b814c1f535"></a>

### `mdio_api_read_t`

```c
typedef int(* mdio_api_read_t) (const struct device *dev, uint8_t prtad, uint8_t regad, uint16_t *data)
```

```c
#include <zephyr/drivers/mdio.h>
```

从 MDIO 总线读取数据。

参数说明参见 `mdio_read()`。

<a id="ga98d32453b4b8ec4abb36113c54711570"></a>

### `mdio_api_write_c45_t`

```c
typedef int(* mdio_api_write_c45_t) (const struct device *dev, uint8_t prtad, uint8_t devad, uint16_t regad, uint16_t data)
```

```c
#include <zephyr/drivers/mdio.h>
```

通过 Clause 45 访问方式向 MDIO 总线写入数据。

参数说明参见 `mdio_write_c45()`。

<a id="ga09e5f0532a3d88249ee6e852be45e434"></a>

### `mdio_api_write_t`

```c
typedef int(* mdio_api_write_t) (const struct device *dev, uint8_t prtad, uint8_t regad, uint16_t data)
```

```c
#include <zephyr/drivers/mdio.h>
```

向 MDIO 总线写入数据。

参数说明参见 `mdio_write()`。


## 13.4\_原页交叉引用（Cross References）

- [mdio_driver_api](../network_service_model_reference/P030_mdio_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/drivers/mdio.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mdio_8h.html)
- [mdio_read_c45()](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#ga93e360a1201c2bb1ddd33b94e6fce619)
- [mdio_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#gae056ee61011eb6e8d68254680f918434)
- [mdio_write_c45()](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#gad8868e94f7335fea3cd9fea338ef9bd5)
- [mdio_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#ga6a18c3d67c6dc7ef1f3f0e3780015d48)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P012_LPS22HH API主题.md) · [返回大纲](大纲.md) · [下一章](P014_组播监听发现（Multicast Listener Discovery）的API。.md)
