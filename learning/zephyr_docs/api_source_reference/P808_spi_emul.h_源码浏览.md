---
id: learning.zephyr-docs.api-source-reference.page-808
title: spi_emul.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/spi__emul_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第808章\_spi\_emul.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/spi__emul_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/spi__emul_8h.html)。

## 808.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2emul_8h_html"></a>
<a id="adrivers_2spi_8h_html"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="agroup__spi__emul__interface_html_ga034da8d578cd4facdff61ce3afb19487"></a>
<a id="agroup__spi__emul__interface_html_ga6c782e1c480a9bf4640c82360e562703"></a>
<a id="agroup__spi__emul__interface_html_ga8b872edd18ec2911618919cc68229362"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructemul_html"></a>
<a id="astructspi__buf__set_html"></a>
<a id="astructspi__config_html"></a>
<a id="astructspi__emul__api_html"></a>
<a id="astructspi__emul__api_html_a357c2c19a5d6eb7a14d895eb9b042085"></a>
<a id="astructspi__emul_html"></a>
<a id="astructspi__emul_html_a371b2447cf16752c191cc5a0aff26a57"></a>
<a id="astructspi__emul_html_a4c49c2c9966eec74a9d010d22176bdd1"></a>
<a id="astructspi__emul_html_a4d174e7170a21e2f53c49e0da096a93e"></a>
<a id="astructspi__emul_html_a81450c3d7701c20da8d945e390e7cd33"></a>
<a id="astructspi__emul_html_a96649e8ea8360ad07ebbd721f999b0e7"></a>

```c
/*
 * Copyright 2020 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SPI_SPI_EMUL_H_
#define ZEPHYR_INCLUDE_DRIVERS_SPI_SPI_EMUL_H_

#include <zephyr/device.h>
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/spi.h>
#include <zephyr/sys/slist.h>
#include <zephyr/types.h>



#ifdef __cplusplus
extern "C" {
#endif

struct spi_msg;
struct spi_emul_api;

struct spi_emul {
        sys_snode_t node;

        const struct emul *target;

        const struct spi_emul_api *api;

        struct spi_emul_api *mock_api;

        uint16_t chipsel;
};

typedef int (*spi_emul_io_t)(const struct emul *target, const struct spi_config *config,
                             const struct spi_buf_set *tx_bufs, const struct spi_buf_set *rx_bufs);

int spi_emul_register(const struct device *dev, struct spi_emul *emul);

struct spi_emul_api {
        spi_emul_io_t io;
};

uint32_t spi_emul_get_config(const struct device *dev);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_SPI_SPI_EMUL_H_ */
```

## 808.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2020 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 109 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SPI_SPI_EMUL_H_`。

## 808.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/spi__emul_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [zephyr/drivers/spi.h](../spi_driver_reference/P001_SPI驱动头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [spi_emul_api](../hardware/P328_SPI模拟函数表.md)
- [spi_emul](../hardware/P327_SPI模拟器结构.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a4c49c2c9966eec74a9d010d22176bdd1)
- [emul](../hardware/P477_仿真器实例结构.md)
- [target](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a371b2447cf16752c191cc5a0aff26a57)
- [api](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a96649e8ea8360ad07ebbd721f999b0e7)
- [mock_api](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a4d174e7170a21e2f53c49e0da096a93e)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [chipsel](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a81450c3d7701c20da8d945e390e7cd33)
- [spi_emul_io_t](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga034da8d578cd4facdff61ce3afb19487)
- [spi_config](../hardware/P320_SPI控制器配置结构.md)
- [spi_buf_set](../hardware/P323_SPI缓冲区集合结构.md)
- [spi_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga6c782e1c480a9bf4640c82360e562703)
- [device](../device_reference/P002_设备对象结构.md)
- [io](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul__api.html#a357c2c19a5d6eb7a14d895eb9b042085)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [spi_emul_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__emul__interface.html#ga8b872edd18ec2911618919cc68229362)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [spi.h](../spi_driver_reference/P001_SPI驱动头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [spi_emul_api::io](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul__api.html#a357c2c19a5d6eb7a14d895eb9b042085)
- [spi_emul::target](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a371b2447cf16752c191cc5a0aff26a57)
- [spi_emul::node](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a4c49c2c9966eec74a9d010d22176bdd1)
- [spi_emul::mock_api](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a4d174e7170a21e2f53c49e0da096a93e)
- [spi_emul::chipsel](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a81450c3d7701c20da8d945e390e7cd33)
- [spi_emul::api](https://docs.zephyrproject.org/latest/doxygen/html/structspi__emul.html#a96649e8ea8360ad07ebbd721f999b0e7)

---

[上一章](P807_sparse.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P809_ssd16xx.h_源码浏览.md)
