---
id: learning.zephyr-docs.api-source-supplement-reference.page-3
title: addresses.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/addresses_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_addresses.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/addresses_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/addresses_8h.html)。

## 3.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
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
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="foldopen00155"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="foldopen00168"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__i3c__addresses_html_ga3dc021699fc489995b0bbe299753a33e"></a>
<a id="agroup__i3c__addresses_html_ga85a120abff94213b57ce4912f58d5ed8"></a>
<a id="agroup__i3c__addresses_html_gaacbed5bbaae3b36d6f3ba175074aecd0"></a>
<a id="agroup__i3c__addresses_html_gac976f542afb29d2360fc2c8d797dbac5"></a>
<a id="agroup__i3c__addresses_html_gad5fc6b00171a4fdf76de20e6da3fbb32"></a>
<a id="agroup__i3c__addresses_html_gad7eddb7aebf337a31f336ccf3f78cad1"></a>
<a id="agroup__i3c__addresses_html_gadc2539a0b8793ec5b5ff34e57e68fb60"></a>
<a id="agroup__i3c__addresses_html_gae10e6aba3335b78a2be728a5f495b436"></a>
<a id="agroup__i3c__addresses_html_gae4eb7e22abde57c9bcfdc8407c0da68d"></a>
<a id="agroup__i3c__addresses_html_gaf2be07d40d885f60997b5eb5edcf910f"></a>
<a id="agroup__i3c__addresses_html_gaf384836871625543aaa3f087e688f1b4"></a>
<a id="agroup__i3c__addresses_html_ggaacbed5bbaae3b36d6f3ba175074aecd0a0af543ae2b67f2e8055d496689437d45"></a>
<a id="agroup__i3c__addresses_html_ggaacbed5bbaae3b36d6f3ba175074aecd0a2093cda582c682b292deb065956ca280"></a>
<a id="agroup__i3c__addresses_html_ggaacbed5bbaae3b36d6f3ba175074aecd0a38b0fd286477bcc936132c25d787749a"></a>
<a id="agroup__i3c__addresses_html_ggaacbed5bbaae3b36d6f3ba175074aecd0a847927f32a28341e0d356c9ec1ccfb2e"></a>
<a id="agroup__i3c__addresses_html_ggaacbed5bbaae3b36d6f3ba175074aecd0ac8d91073cf590626b58bbf5f5b8d9c55"></a>
<a id="agroup__sys-util_html_ga2f660aa23a5dbc0f4b8df48b4302b8c3"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructi3c__addr__slots_html"></a>
<a id="astructi3c__addr__slots_html_a8117bc5c9b55bb074a845f8a4fe405fb"></a>
<a id="astructi3c__dev__list_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright 2022 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_I3C_ADDRESSES_H_
#define ZEPHYR_INCLUDE_DRIVERS_I3C_ADDRESSES_H_


#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif

#define I3C_BROADCAST_ADDR                      0x7E

#define I3C_MAX_ADDR                            0x7F

struct i3c_dev_list;

enum i3c_addr_slot_status {
        I3C_ADDR_SLOT_STATUS_FREE = 0U,

        I3C_ADDR_SLOT_STATUS_RSVD,

        I3C_ADDR_SLOT_STATUS_I3C_DEV,

        I3C_ADDR_SLOT_STATUS_I2C_DEV,

        I3C_ADDR_SLOT_STATUS_MASK = 0x03U,
};

struct i3c_addr_slots {
        /* 2 bits per slot */
        unsigned long slots[((I3C_MAX_ADDR + 1) * 2) / BITS_PER_LONG];
};

int i3c_addr_slots_init(const struct device *dev);

void i3c_addr_slots_set(struct i3c_addr_slots *slots,
                        uint8_t dev_addr,
                        enum i3c_addr_slot_status status);

enum i3c_addr_slot_status i3c_addr_slots_status(struct i3c_addr_slots *slots,
                                                uint8_t dev_addr);

bool i3c_addr_slots_is_free(struct i3c_addr_slots *slots,
                            uint8_t dev_addr);

uint8_t i3c_addr_slots_next_free_find(struct i3c_addr_slots *slots, uint8_t start_addr);

static inline void i3c_addr_slots_mark_free(struct i3c_addr_slots *addr_slots,
                                            uint8_t addr)
{
        i3c_addr_slots_set(addr_slots, addr,
                           I3C_ADDR_SLOT_STATUS_FREE);
}

static inline void i3c_addr_slots_mark_rsvd(struct i3c_addr_slots *addr_slots,
                                            uint8_t addr)
{
        i3c_addr_slots_set(addr_slots, addr,
                           I3C_ADDR_SLOT_STATUS_RSVD);
}

static inline void i3c_addr_slots_mark_i3c(struct i3c_addr_slots *addr_slots,
                                           uint8_t addr)
{
        i3c_addr_slots_set(addr_slots, addr,
                           I3C_ADDR_SLOT_STATUS_I3C_DEV);
}

static inline void i3c_addr_slots_mark_i2c(struct i3c_addr_slots *addr_slots,
                                           uint8_t addr)
{
        i3c_addr_slots_set(addr_slots, addr,
                           I3C_ADDR_SLOT_STATUS_I2C_DEV);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_I3C_ADDRESSES_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 59 行

每个槽位（Slot）占 2 位。

### 注释 3：原第 183 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_I3C_ADDRESSES_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/addresses_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [i3c_dev_list](../hardware/P403_I3C已知设备列表.md)
- [i3c_addr_slot_status](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gaacbed5bbaae3b36d6f3ba175074aecd0)
- [I3C_ADDR_SLOT_STATUS_FREE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0a847927f32a28341e0d356c9ec1ccfb2e)
- [I3C_ADDR_SLOT_STATUS_RSVD](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0a0af543ae2b67f2e8055d496689437d45)
- [I3C_ADDR_SLOT_STATUS_I3C_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0a38b0fd286477bcc936132c25d787749a)
- [I3C_ADDR_SLOT_STATUS_I2C_DEV](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0ac8d91073cf590626b58bbf5f5b8d9c55)
- [I3C_ADDR_SLOT_STATUS_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ggaacbed5bbaae3b36d6f3ba175074aecd0a2093cda582c682b292deb065956ca280)
- [i3c_addr_slots](../hardware/P384_I3C地址槽结构.md)
- [slots](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__addr__slots.html#a8117bc5c9b55bb074a845f8a4fe405fb)
- [I3C_MAX_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ga85a120abff94213b57ce4912f58d5ed8)
- [BITS_PER_LONG](../util_reference/P001_通用工具公共接口.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)
- [i3c_addr_slots_init](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gaf2be07d40d885f60997b5eb5edcf910f)
- [device](../device_reference/P002_设备对象结构.md)
- [i3c_addr_slots_set](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gae4eb7e22abde57c9bcfdc8407c0da68d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [i3c_addr_slots_status](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#ga3dc021699fc489995b0bbe299753a33e)
- [i3c_addr_slots_is_free](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gadc2539a0b8793ec5b5ff34e57e68fb60)
- [i3c_addr_slots_next_free_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gad7eddb7aebf337a31f336ccf3f78cad1)
- [i3c_addr_slots_mark_free](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gaf384836871625543aaa3f087e688f1b4)
- [i3c_addr_slots_mark_rsvd](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gac976f542afb29d2360fc2c8d797dbac5)
- [i3c_addr_slots_mark_i3c](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gae10e6aba3335b78a2be728a5f495b436)
- [i3c_addr_slots_mark_i2c](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__addresses.html#gad5fc6b00171a4fdf76de20e6da3fbb32)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [i3c_addr_slots::slots](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__addr__slots.html#a8117bc5c9b55bb074a845f8a4fe405fb)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P002_addr_types.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_aead.h_源码浏览.md)
