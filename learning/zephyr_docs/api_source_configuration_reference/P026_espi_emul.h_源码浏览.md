---
id: learning.zephyr-docs.api-source-configuration-reference.page-26
title: espi_emul.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/espi__emul_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_espi\_emul.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/espi__emul_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/espi__emul_8h.html)。

## 26.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00117"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00128"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a2b0530c13706c66229d35977c6553db9"></a>
<a id="adrivers_2emul_8h_html"></a>
<a id="aespi_8h_html"></a>
<a id="agroup__espi__emul__interface_html_ga06c214788ceff221e776394318517f91"></a>
<a id="agroup__espi__emul__interface_html_ga16c67d1d52f94b7062144e2c2f45d15a"></a>
<a id="agroup__espi__emul__interface_html_ga2abff7d857738254cc4a8a939264924f"></a>
<a id="agroup__espi__emul__interface_html_ga375d2f3d386a835b627cf26745bc77c3"></a>
<a id="agroup__espi__emul__interface_html_ga67deaf77a17682671ec28488ed3113fc"></a>
<a id="agroup__espi__emul__interface_html_gaa9e27e6a744a73a13415e01fa2c09bca"></a>
<a id="agroup__espi__emul__interface_html_gaa9f83b27986b700d629188522850fab3"></a>
<a id="agroup__espi__emul__interface_html_gaaccb8ef6060c0477151001af52310769"></a>
<a id="agroup__espi__emul__interface_html_gab1068f48bf931fbc86668fb9108e07c7"></a>
<a id="agroup__espi__interface_html_gab65a0951a8912d9de398cfec0aef7d35"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructemul__espi__device__api_html"></a>
<a id="astructemul__espi__device__api_html_a85353662a3279444ed2a78f39b49cc3c"></a>
<a id="astructemul__espi__device__api_html_a9d1ceef7587374ab99853eb1ab0040c4"></a>
<a id="astructemul__espi__device__api_html_a9f74d3b4f647bfb756fdf92851a64f86"></a>
<a id="astructemul__espi__driver__api_html"></a>
<a id="astructemul__espi__driver__api_html_a77f9c77cbd2c66e0f8871f94deb7c154"></a>
<a id="astructemul__espi__driver__api_html_a829c405693c4ef7f558004bc8106342b"></a>
<a id="astructemul__espi__driver__api_html_ac7523c429bc75a99d20a87243b9d1195"></a>
<a id="astructemul_html"></a>
<a id="astructespi__driver__api_html"></a>
<a id="astructespi__emul_html"></a>
<a id="astructespi__emul_html_a1c80c40cdc25bb5440d57c3aef7379eb"></a>
<a id="astructespi__emul_html_a27aa4069611f537b470a9c64d7913c91"></a>
<a id="astructespi__emul_html_a29554137c4ef3fbf4f7a087d01602adb"></a>
<a id="astructespi__emul_html_a495cddd3fc6300f2c7eb3e98caafecd5"></a>
<a id="astructespi__event_html"></a>

```c
/*
 * Copyright 2020 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_ESPI_SPI_EMUL_H_
#define ZEPHYR_INCLUDE_DRIVERS_ESPI_SPI_EMUL_H_

#include <zephyr/device.h>
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/espi.h>
#include <zephyr/sys/slist.h>
#include <zephyr/types.h>


#ifdef __cplusplus
extern "C" {
#endif

#define EMUL_ESPI_HOST_CHIPSEL 0

struct espi_emul;

typedef int (*emul_espi_api_set_vw)(const struct emul *target, enum espi_vwire_signal vw,
                                    uint8_t level);

typedef int (*emul_espi_api_get_vw)(const struct emul *target, enum espi_vwire_signal vw,
                                    uint8_t *level);

typedef uintptr_t (*emul_espi_api_get_acpi_shm)(const struct emul *target);

typedef struct espi_emul *(*emul_find_emul)(const struct device *dev, unsigned int chipsel);

typedef int (*emul_trigger_event)(const struct device *dev, struct espi_event *evt);

struct emul_espi_device_api {
        emul_espi_api_set_vw set_vw;
        emul_espi_api_get_vw get_vw;
#if defined(CONFIG_ESPI_PERIPHERAL_ACPI_SHM_REGION) || defined(__DOXYGEN__)
        emul_espi_api_get_acpi_shm get_acpi_shm;
#endif
};

struct espi_emul {
        sys_snode_t node;
        const struct emul *target;
        const struct emul_espi_device_api *api;
        uint16_t chipsel;
};

__subsystem struct emul_espi_driver_api {
        /* The struct espi_driver_api has to be first in
         * struct emul_espi_driver_api to make pointer casting working
         */
        struct espi_driver_api espi_api;
        /* The rest, emulator specific functions */
        emul_trigger_event trigger_event;
        emul_find_emul find_emul;
};

DEVICE_API_EXTENDS(emul_espi, espi, espi_api);

int espi_emul_register(const struct device *dev, struct espi_emul *emul);

int emul_espi_host_send_vw(const struct device *espi_dev, enum espi_vwire_signal vw, uint8_t level);

int emul_espi_host_port80_write(const struct device *espi_dev, uint32_t data);

uintptr_t emul_espi_host_get_acpi_shm(const struct device *espi_dev);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_ESPI_SPI_EMUL_H_ */
```

## 26.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2020 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 129 行

`struct espi_driver_api` 必须是 `struct emul_espi_driver_api` 的第一个成员，才能使指针类型转换正常工作。

### 注释 3：原第 133 行

其余部分是仿真器专用函数（Emulator specific functions）。

### 注释 4：原第 195 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_ESPI_SPI_EMUL_H_`。

## 26.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/espi__emul_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [zephyr/drivers/espi.h](../peripheral_bus_storage_header_reference/P004_zephyr__drivers__espi.h_头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [espi_emul](../hardware/P488_eSPI仿真器链表节点.md)
- [emul_espi_api_set_vw](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#gab1068f48bf931fbc86668fb9108e07c7)
- [emul](../hardware/P477_仿真器实例结构.md)
- [espi_vwire_signal](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__interface.html#gab65a0951a8912d9de398cfec0aef7d35)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [emul_espi_api_get_vw](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga06c214788ceff221e776394318517f91)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [emul_espi_api_get_acpi_shm](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga375d2f3d386a835b627cf26745bc77c3)
- [device](../device_reference/P002_设备对象结构.md)
- [emul_trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga2abff7d857738254cc4a8a939264924f)
- [espi_event](../peripheral_bus_storage_model_reference/P008_espi_event_结构体.md)
- [emul_espi_device_api](../hardware/P481_eSPI仿真设备API结构.md)
- [set_vw](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__device__api.html#a85353662a3279444ed2a78f39b49cc3c)
- [get_vw](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__device__api.html#a9d1ceef7587374ab99853eb1ab0040c4)
- [get_acpi_shm](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__device__api.html#a9f74d3b4f647bfb756fdf92851a64f86)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](https://docs.zephyrproject.org/latest/doxygen/html/structespi__emul.html#a495cddd3fc6300f2c7eb3e98caafecd5)
- [target](https://docs.zephyrproject.org/latest/doxygen/html/structespi__emul.html#a27aa4069611f537b470a9c64d7913c91)
- [api](https://docs.zephyrproject.org/latest/doxygen/html/structespi__emul.html#a1c80c40cdc25bb5440d57c3aef7379eb)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [chipsel](https://docs.zephyrproject.org/latest/doxygen/html/structespi__emul.html#a29554137c4ef3fbf4f7a087d01602adb)
- [emul_espi_driver_api](../hardware/P482_eSPI仿真驱动API结构.md)
- [espi_driver_api](../peripheral_bus_storage_model_reference/P007_espi_driver_api_结构体.md)
- [espi_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__driver__api.html#a829c405693c4ef7f558004bc8106342b)
- [trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__driver__api.html#a77f9c77cbd2c66e0f8871f94deb7c154)
- [emul_find_emul](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#gaa9e27e6a744a73a13415e01fa2c09bca)
- [find_emul](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__driver__api.html#ac7523c429bc75a99d20a87243b9d1195)
- [DEVICE_API_EXTENDS](../device_reference/P007_设备模型头文件参考.md#a2b0530c13706c66229d35977c6553db9)
- [espi_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#gaaccb8ef6060c0477151001af52310769)
- [emul_espi_host_send_vw](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga67deaf77a17682671ec28488ed3113fc)
- [emul_espi_host_port80_write](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#ga16c67d1d52f94b7062144e2c2f45d15a)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [emul_espi_host_get_acpi_shm](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__emul__interface.html#gaa9f83b27986b700d629188522850fab3)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [espi.h](../peripheral_bus_storage_header_reference/P004_zephyr__drivers__espi.h_头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [emul_espi_device_api::set_vw](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__device__api.html#a85353662a3279444ed2a78f39b49cc3c)
- [emul_espi_device_api::get_vw](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__device__api.html#a9d1ceef7587374ab99853eb1ab0040c4)
- [emul_espi_device_api::get_acpi_shm](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__device__api.html#a9f74d3b4f647bfb756fdf92851a64f86)
- [emul_espi_driver_api::trigger_event](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__driver__api.html#a77f9c77cbd2c66e0f8871f94deb7c154)
- [emul_espi_driver_api::espi_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__driver__api.html#a829c405693c4ef7f558004bc8106342b)
- [emul_espi_driver_api::find_emul](https://docs.zephyrproject.org/latest/doxygen/html/structemul__espi__driver__api.html#ac7523c429bc75a99d20a87243b9d1195)
- [espi_emul::api](https://docs.zephyrproject.org/latest/doxygen/html/structespi__emul.html#a1c80c40cdc25bb5440d57c3aef7379eb)
- [espi_emul::target](https://docs.zephyrproject.org/latest/doxygen/html/structespi__emul.html#a27aa4069611f537b470a9c64d7913c91)
- [espi_emul::chipsel](https://docs.zephyrproject.org/latest/doxygen/html/structespi__emul.html#a29554137c4ef3fbf4f7a087d01602adb)
- [espi_emul::node](https://docs.zephyrproject.org/latest/doxygen/html/structespi__emul.html#a495cddd3fc6300f2c7eb3e98caafecd5)

---

[上一章](P025_esp-esp32h2-intmux.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P027_ft8xx_reference_api.h_源码浏览.md)
