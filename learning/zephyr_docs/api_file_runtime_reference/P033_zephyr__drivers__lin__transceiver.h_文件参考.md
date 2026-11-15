---
id: learning.zephyr-docs.api-file-runtime-reference.page-33
title: zephyr__drivers__lin__transceiver.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lin_2transceiver_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_zephyr\_\_drivers\_\_lin\_\_transceiver.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lin_2transceiver_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LIN收发器（Transceiver）的驱动API。

<a id="details"></a>

```c
#include <zephyr/drivers/lin.h>
#include <zephyr/device.h>
```

查看此文件的源码。

局部互连网络收发器驱动 API（LIN Transceiver Driver API）。本文件包含 LIN 收发器通信（Transceiver Communication）的定义和 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 33.1\_函数（Functions）

<a id="r_ga8a81eb11fe36f6a1a4db51015367ed36"></a>

```c
static int lin_transceiver_enable (const struct device *dev, uint8_t flags)
```

相关声明：[lin_transceiver_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__transceiver.html#ga8a81eb11fe36f6a1a4db51015367ed36)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

启用 LIN 收发器（Transceiver）。

<a id="r_ga898972c2e62cd45e53a901801502b2f9"></a>

```c
static int lin_transceiver_disable (const struct device *dev)
```

相关声明：[lin_transceiver_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__transceiver.html#ga898972c2e62cd45e53a901801502b2f9)、[device](../device_reference/P002_设备对象结构.md)。

禁用 LIN 收发器（Transceiver）。


## 33.2\_原页交叉引用（Cross References）

- [zephyr/drivers/lin.h](../peripheral_bus_storage_source_reference/P007_zephyr__drivers__lin.h_头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P439_transceiver.h_源码浏览.md)
- [lin_transceiver_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__transceiver.html#ga8a81eb11fe36f6a1a4db51015367ed36)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [lin_transceiver_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__transceiver.html#ga898972c2e62cd45e53a901801502b2f9)

<a id="header-details"></a>

---

[上一章](P032_zephyr__bluetooth__mesh__large_comp_data_cli.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P034_zephyr__drivers__sensor__max30210.h_文件参考.md)
