---
id: learning.zephyr-docs.api-file-runtime-reference.page-62
title: zephyr__drivers__spi_emul.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/spi__emul_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_zephyr\_\_drivers\_\_spi\_emul.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/spi__emul_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SPI仿真驱动（Emulation Drivers）的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/spi.h>
#include <zephyr/sys/slist.h>
#include <zephyr/types.h>
```

查看此文件的源码。

SPI仿真驱动（Emulation Drivers）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 62.1\_数据结构（Data Structures）

<a id="r_spi_5Femul"></a>

```c
struct spi_emul
```

相关声明：[spi_emul](../hardware/P327_SPI模拟器结构.md)。

SPI设备仿真器链表（Linked List）中的节点。

<a id="r_spi_5Femul_5Fapi"></a>

```c
struct spi_emul_api
```

相关声明：[spi_emul_api](../hardware/P328_SPI模拟函数表.md)。

仿真器（Emulator）API的定义。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 62.2\_类型定义（Typedefs）

<a id="r_ga034da8d578cd4facdff61ce3afb19487"></a>

```c
typedef int(* spi_emul_io_t) (const struct emul *target, const struct spi_config *config, const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs)
```

相关声明：[spi_emul_io_t](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga034da8d578cd4facdff61ce3afb19487)、[emul](../hardware/P477_仿真器实例结构.md)、[spi_config](../hardware/P320_SPI控制器配置结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)、[spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)。

将 SPI 消息（Messages）传递给仿真器（Emulator）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 62.3\_函数（Functions）

<a id="r_ga6c782e1c480a9bf4640c82360e562703"></a>

```c
int spi_emul_register (const struct device *dev, struct spi_emul *emul)
```

相关声明：[spi_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga6c782e1c480a9bf4640c82360e562703)、[device](../device_reference/P002_设备对象结构.md)、[spi_emul](../hardware/P327_SPI模拟器结构.md)、[emul](../hardware/P477_仿真器实例结构.md)。

在控制器（Controller）上注册仿真设备（Emulated Device）。

<a id="r_ga8b872edd18ec2911618919cc68229362"></a>

```c
uint32_t spi_emul_get_config (const struct device *dev)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[spi_emul_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga8b872edd18ec2911618919cc68229362)、[device](../device_reference/P002_设备对象结构.md)。

提供后门接口（Back Door），允许仿真器（Emulator）获取主机配置（Host Configuration）。


## 62.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/emul.h](../api_source_runtime_reference/P013_emul.h_源码浏览.md)
- [zephyr/drivers/spi.h](../spi_driver_reference/P002_SPI驱动头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P808_spi_emul.h_源码浏览.md)
- [spi_emul](../hardware/P327_SPI模拟器结构.md)
- [spi_emul_api](../hardware/P328_SPI模拟函数表.md)
- [spi_emul_io_t](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga034da8d578cd4facdff61ce3afb19487)
- [emul](../hardware/P477_仿真器实例结构.md)
- [spi_config](../hardware/P320_SPI控制器配置结构.md)
- [spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)
- [spi_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga6c782e1c480a9bf4640c82360e562703)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [spi_emul_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga8b872edd18ec2911618919cc68229362)

<a id="header-details"></a>

---

[上一章](P061_zephyr__dt-bindings__gpio__snps-designware-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P063_zephyr__mgmt__mcumgr__grp__stat_mgmt__stat_mgmt.h_文件参考.md)
