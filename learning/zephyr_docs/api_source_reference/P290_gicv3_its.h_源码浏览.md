---
id: learning.zephyr-docs.api-source-reference.page-290
title: gicv3_its.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第290章\_gicv3\_its.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html)。

## 290.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00027"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00046"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agicv3__its_8h_html_a05032faf2fdcde27760871345756d3e5"></a>
<a id="agicv3__its_8h_html_a2642c1f7ecf45d404c17cdbcd824bb45"></a>
<a id="agicv3__its_8h_html_a26bf8d071e3cb856fc81d8911e942f5a"></a>
<a id="agicv3__its_8h_html_a39f4a213de953b77615b270f3ff13832"></a>
<a id="agicv3__its_8h_html_a49dff2553cbd48edc7057157d2ecb45d"></a>
<a id="agicv3__its_8h_html_a5c50167a84a3b7d8e3cf01d226deb3d3"></a>
<a id="agicv3__its_8h_html_a6139a7f275a6016ecadcb0ee2dfcc327"></a>
<a id="agicv3__its_8h_html_ac4899e33d0636465265a3072aa5510cc"></a>
<a id="agicv3__its_8h_html_add616700e3aeee952187ef96cb2d19c9"></a>
<a id="agicv3__its_8h_html_afcd0b4735367a10465e81b46d333b06b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructits__driver__api_html"></a>
<a id="astructits__driver__api_html_a0a71be1a078b6e1a82624e0ef9a619ac"></a>
<a id="astructits__driver__api_html_aa853404a1105b0cc4d1b6c976579ae4a"></a>
<a id="astructits__driver__api_html_aa87bb10ac8f165c2acbc6033591b9aa8"></a>
<a id="astructits__driver__api_html_aec4b32cea8d6c5fa2a59d2d25e6053cf"></a>
<a id="astructits__driver__api_html_affc7190b95d16fa0223f6fd7b1ae9c14"></a>

```c
/*
 * Copyright (c) 2021 BayLibre, SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_GICV3_ITS_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_GICV3_ITS_H_

typedef unsigned int (*its_api_alloc_intid_t)(const struct device *dev);
typedef int (*its_api_setup_deviceid_t)(const struct device *dev, uint32_t device_id,
                                        unsigned int nites);
typedef int (*its_api_map_intid_t)(const struct device *dev, uint32_t device_id,
                                   uint32_t event_id, unsigned int intid);
typedef int (*its_api_send_int_t)(const struct device *dev, uint32_t device_id, uint32_t event_id);
typedef uint32_t (*its_api_get_msi_addr_t)(const struct device *dev);

__subsystem struct its_driver_api {
        its_api_alloc_intid_t alloc_intid;
        its_api_setup_deviceid_t setup_deviceid;
        its_api_map_intid_t map_intid;
        its_api_send_int_t send_int;
        its_api_get_msi_addr_t get_msi_addr;
};

static inline int its_alloc_intid(const struct device *dev)
{
        return DEVICE_API_GET(its, dev)->alloc_intid(dev);
}

static inline int its_setup_deviceid(const struct device *dev, uint32_t device_id,
                                     unsigned int nites)
{
        return DEVICE_API_GET(its, dev)->setup_deviceid(dev, device_id, nites);
}

static inline int its_map_intid(const struct device *dev, uint32_t device_id,
                                uint32_t event_id, unsigned int intid)
{
        return DEVICE_API_GET(its, dev)->map_intid(dev, device_id, event_id, intid);
}

static inline int its_send_int(const struct device *dev, uint32_t device_id, uint32_t event_id)
{
        return DEVICE_API_GET(its, dev)->send_int(dev, device_id, event_id);
}

static inline uint32_t its_get_msi_addr(const struct device *dev)
{
        return DEVICE_API_GET(its, dev)->get_msi_addr(dev);
}

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_GICV3_ITS_H_ */
```

## 290.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 BayLibre, SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 62 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_GICV3_ITS_H_`。

## 290.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html)
- [its_api_alloc_intid_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a49dff2553cbd48edc7057157d2ecb45d)
- [device](../device_reference/P002_设备对象结构.md)
- [its_api_setup_deviceid_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a39f4a213de953b77615b270f3ff13832)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [its_api_map_intid_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a2642c1f7ecf45d404c17cdbcd824bb45)
- [its_api_send_int_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a26bf8d071e3cb856fc81d8911e942f5a)
- [its_api_get_msi_addr_t](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#add616700e3aeee952187ef96cb2d19c9)
- [its_driver_api](../platform_security_model_reference/P016_its_driver_api_结构体.md)
- [alloc_intid](../platform_security_model_reference/P016_its_driver_api_结构体.md#affc7190b95d16fa0223f6fd7b1ae9c14)
- [setup_deviceid](../platform_security_model_reference/P016_its_driver_api_结构体.md#aa853404a1105b0cc4d1b6c976579ae4a)
- [map_intid](../platform_security_model_reference/P016_its_driver_api_结构体.md#a0a71be1a078b6e1a82624e0ef9a619ac)
- [send_int](../platform_security_model_reference/P016_its_driver_api_结构体.md#aec4b32cea8d6c5fa2a59d2d25e6053cf)
- [get_msi_addr](../platform_security_model_reference/P016_its_driver_api_结构体.md#aa87bb10ac8f165c2acbc6033591b9aa8)
- [its_alloc_intid](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a5c50167a84a3b7d8e3cf01d226deb3d3)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [its_setup_deviceid](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a05032faf2fdcde27760871345756d3e5)
- [its_map_intid](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#ac4899e33d0636465265a3072aa5510cc)
- [its_send_int](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#a6139a7f275a6016ecadcb0ee2dfcc327)
- [its_get_msi_addr](https://docs.zephyrproject.org/latest/doxygen/html/gicv3__its_8h.html#afcd0b4735367a10465e81b46d333b06b)
- [its_driver_api::map_intid](../platform_security_model_reference/P016_its_driver_api_结构体.md#a0a71be1a078b6e1a82624e0ef9a619ac)
- [its_driver_api::setup_deviceid](../platform_security_model_reference/P016_its_driver_api_结构体.md#aa853404a1105b0cc4d1b6c976579ae4a)
- [its_driver_api::get_msi_addr](../platform_security_model_reference/P016_its_driver_api_结构体.md#aa87bb10ac8f165c2acbc6033591b9aa8)
- [its_driver_api::send_int](../platform_security_model_reference/P016_its_driver_api_结构体.md#aec4b32cea8d6c5fa2a59d2d25e6053cf)
- [its_driver_api::alloc_intid](../platform_security_model_reference/P016_its_driver_api_结构体.md#affc7190b95d16fa0223f6fd7b1ae9c14)

---

[上一章](P289_generic_emul.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P291_gnss.h_源码浏览.md)
