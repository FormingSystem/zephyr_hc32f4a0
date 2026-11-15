---
id: learning.zephyr-docs.api-file-configuration-reference.page-70
title: zephyr__display__ssd16xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ssd16xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_zephyr\_\_display\_\_ssd16xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ssd16xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SSD16XX扩展显示（Display）API的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/display.h>
```

查看此文件的源码。

SSD16XX扩展显示（Display）API的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 70.1\_枚举（Enumerations）

<a id="r_gaf3596acb60f20fbecef01e82672ea765"></a>

```c
enum ssd16xx_ram { SSD16XX_RAM_BLACK = 0 , SSD16XX_RAM_RED }
```

相关声明：[ssd16xx_ram](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html#gaf3596acb60f20fbecef01e82672ea765)、[SSD16XX_RAM_BLACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html#ggaf3596acb60f20fbecef01e82672ea765ae3ae0ce9601034f1030f7114dcfedab0)、[SSD16XX_RAM_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html#ggaf3596acb60f20fbecef01e82672ea765a54fddbd6e9f2207ff228ccfcde65f466)。

直接 RAM 访问（Direct RAM Access）使用的 SSD16xx RAM 类型（RAM Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 70.2\_函数（Functions）

<a id="r_ga876bae07401b2ccc3889414706ae4d97"></a>

```c
int ssd16xx_read_ram (const struct device *dev, enum ssd16xx_ram ram_type, const uint16_t x, const uint16_t y, const struct display_buffer_descriptor *desc, void *buf)
```

相关声明：[ssd16xx_read_ram](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html#ga876bae07401b2ccc3889414706ae4d97)、[device](../device_reference/P002_设备对象结构.md)、[ssd16xx_ram](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html#gaf3596acb60f20fbecef01e82672ea765)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)。

直接从 SSD16xx 显示控制器（Display Controller）的内部 RAM 读取数据。


## 70.3\_原页交叉引用（Cross References）

- [zephyr/drivers/display.h](../api_source_supplement_reference/P041_display.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P809_ssd16xx.h_源码浏览.md)
- [ssd16xx_ram](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html#gaf3596acb60f20fbecef01e82672ea765)
- [SSD16XX_RAM_BLACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html#ggaf3596acb60f20fbecef01e82672ea765ae3ae0ce9601034f1030f7114dcfedab0)
- [SSD16XX_RAM_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html#ggaf3596acb60f20fbecef01e82672ea765a54fddbd6e9f2207ff228ccfcde65f466)
- [ssd16xx_read_ram](https://docs.zephyrproject.org/latest/doxygen/html/group__ssd16xx__interface.html#ga876bae07401b2ccc3889414706ae4d97)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [display_buffer_descriptor](../hardware/P215_显示缓冲区描述符.md)

<a id="header-details"></a>

---

[上一章](P069_zephyr__mgmt__ec_host_cmd__simulator.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P071_zephyr__dt-bindings__pinctrl__stm32-pinctrl-common.h_文件参考.md)
