---
id: learning.zephyr-docs.api-file-system-device-reference.page-9
title: zephyr__drivers__mdio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mdio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_drivers\_\_mdio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mdio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

管理数据输入输出（Management Data Input/Output，MDIO）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <errno.h>
#include <zephyr/syscalls/mdio.h>
```

查看此文件的源码。

管理数据输入输出（Management Data Input/Output，MDIO）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_mdio_5Fdriver_5Fapi"></a>

```c
struct mdio_driver_api
```

相关声明：[mdio_driver_api](../network_service_model_reference/P030_mdio_driver_api_结构体.md)。

驱动操作（Driver Operations）：管理数据输入输出（MDIO）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.2\_类型定义（Typedefs）

<a id="r_gadd83bf9b8e4b4bd7189bc0b814c1f535"></a>

```c
typedef int(* mdio_api_read_t) (const struct device *dev, uint8_t prtad, uint8_t regad, uint16_t *data)
```

相关声明：[mdio_api_read_t](../api_connection_topic_reference/P013_MDIO 驱动后端 API.md#gadd83bf9b8e4b4bd7189bc0b814c1f535)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从 MDIO 总线读取数据。

<a id="r_ga09e5f0532a3d88249ee6e852be45e434"></a>

```c
typedef int(* mdio_api_write_t) (const struct device *dev, uint8_t prtad, uint8_t regad, uint16_t data)
```

相关声明：[mdio_api_write_t](../api_connection_topic_reference/P013_MDIO 驱动后端 API.md#ga09e5f0532a3d88249ee6e852be45e434)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 MDIO 总线写入数据。

<a id="r_gaba3f545bba5aa028f50c4a7f6e43abd0"></a>

```c
typedef int(* mdio_api_read_c45_t) (const struct device *dev, uint8_t prtad, uint8_t devad, uint16_t regad, uint16_t *data)
```

相关声明：[mdio_api_read_c45_t](../api_connection_topic_reference/P013_MDIO 驱动后端 API.md#gaba3f545bba5aa028f50c4a7f6e43abd0)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过第 45 条款访问方式（Clause 45 access）从 MDIO 总线读取数据。

<a id="r_ga98d32453b4b8ec4abb36113c54711570"></a>

```c
typedef int(* mdio_api_write_c45_t) (const struct device *dev, uint8_t prtad, uint8_t devad, uint16_t regad, uint16_t data)
```

相关声明：[mdio_api_write_c45_t](../api_connection_topic_reference/P013_MDIO 驱动后端 API.md#ga98d32453b4b8ec4abb36113c54711570)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 Clause 45 访问方式向 MDIO 总线写入数据。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.3\_函数（Functions）

<a id="r_gae056ee61011eb6e8d68254680f918434"></a>

```c
int mdio_read (const struct device *dev, uint8_t prtad, uint8_t regad, uint16_t *data)
```

相关声明：[mdio_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#gae056ee61011eb6e8d68254680f918434)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从管理数据输入／输出（MDIO）总线读取数据。

<a id="r_ga6a18c3d67c6dc7ef1f3f0e3780015d48"></a>

```c
int mdio_write (const struct device *dev, uint8_t prtad, uint8_t regad, uint16_t data)
```

相关声明：[mdio_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#ga6a18c3d67c6dc7ef1f3f0e3780015d48)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 MDIO 总线写入数据。

<a id="r_ga93e360a1201c2bb1ddd33b94e6fce619"></a>

```c
int mdio_read_c45 (const struct device *dev, uint8_t prtad, uint8_t devad, uint16_t regad, uint16_t *data)
```

相关声明：[mdio_read_c45](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#ga93e360a1201c2bb1ddd33b94e6fce619)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过第 45 条款访问方式（Clause 45 access）从 MDIO 总线读取数据。

<a id="r_gad8868e94f7335fea3cd9fea338ef9bd5"></a>

```c
int mdio_write_c45 (const struct device *dev, uint8_t prtad, uint8_t devad, uint16_t regad, uint16_t data)
```

相关声明：[mdio_write_c45](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#gad8868e94f7335fea3cd9fea338ef9bd5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

通过 Clause 45 访问方式向 MDIO 总线写入数据。


## 9.4\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P158_mdio.h_源码浏览.md)
- [mdio_driver_api](../network_service_model_reference/P030_mdio_driver_api_结构体.md)
- [mdio_api_read_t](../api_connection_topic_reference/P013_MDIO 驱动后端 API.md#gadd83bf9b8e4b4bd7189bc0b814c1f535)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [mdio_api_write_t](../api_connection_topic_reference/P013_MDIO 驱动后端 API.md#ga09e5f0532a3d88249ee6e852be45e434)
- [mdio_api_read_c45_t](../api_connection_topic_reference/P013_MDIO 驱动后端 API.md#gaba3f545bba5aa028f50c4a7f6e43abd0)
- [mdio_api_write_c45_t](../api_connection_topic_reference/P013_MDIO 驱动后端 API.md#ga98d32453b4b8ec4abb36113c54711570)
- [mdio_read](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#gae056ee61011eb6e8d68254680f918434)
- [mdio_write](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#ga6a18c3d67c6dc7ef1f3f0e3780015d48)
- [mdio_read_c45](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#ga93e360a1201c2bb1ddd33b94e6fce619)
- [mdio_write_c45](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface.html#gad8868e94f7335fea3cd9fea338ef9bd5)

<a id="header-details"></a>

---

[上一章](P008_zephyr__xen__dmop.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__dt-bindings__sensor__mtch9010.h_文件参考.md)
