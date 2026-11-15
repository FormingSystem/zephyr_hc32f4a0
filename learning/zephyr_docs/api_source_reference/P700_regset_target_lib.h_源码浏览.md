---
id: learning.zephyr-docs.api-source-reference.page-700
title: regset_target_lib.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第700章\_regset\_target\_lib.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h.html)。

## 700.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="foldopen00146"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="foldopen00153"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="foldopen00159"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="foldopen00171"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="aregset__target__lib_8h_html_a746682f1490935846f189fddae22f4ac"></a>
<a id="aregset__target__lib_8h_html_aab1502efe79713b23cc9b66add677c1a"></a>
<a id="aregset__target__lib_8h_html_ace6db98c44d46daff92c8d7f29fd4f54"></a>
<a id="aregset__target__lib_8h_html_ad92d2e54bdf7426ea49cea95930fa142"></a>
<a id="aregset__target__lib_8h_html_ae9e6dd062981be4f7c429ffb12452745"></a>
<a id="aregset__target__lib_8h_html_af4882a009f613f2adccabd25019ee44a"></a>
<a id="aregset__target__lib_8h_html_afb1e7a6fe4e25d22f335c00da29c2378"></a>
<a id="aregset__target__lib_8h_html_aff17ae03f428fd989be2b108f87d3f49"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructi2c__dt__spec_html"></a>
<a id="astructi2c__dt__spec_html_a85242ab56b1e8633b7001353990392fa"></a>
<a id="astructi2c__target__config_html"></a>
<a id="astructi2c__target__driver__api_html"></a>
<a id="astructregset__target__lib__config_html"></a>
<a id="astructregset__target__lib__data_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright (c) 2017 BayLibre, SAS
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_I2C_TARGET_REGSET_TARGET_LIB_H_
#define ZEPHYR_INCLUDE_DRIVERS_I2C_TARGET_REGSET_TARGET_LIB_H_

#include <stddef.h>
#include <sys/types.h>

typedef void (*regset_target_lib_changed_handler_t)(const struct device *dev, void *user_data);

struct regset_target_lib_data {
        const struct device *dev;
        struct i2c_target_config config;
        uint32_t buffer_idx;
        uint32_t idx_write_cnt;
        regset_target_lib_changed_handler_t changed_handler;
        void *changed_handler_data;
        bool changed;
};

struct regset_target_lib_config {
        struct i2c_dt_spec bus;
        uint32_t buffer_size;
        uint8_t *buffer;
        uint8_t address_width;
        bool auto_register;
};

void regset_target_lib_set_changed_callback(const struct device *dev,
                                            regset_target_lib_changed_handler_t handler,
                                            void *user_data);

size_t regset_target_lib_get_size(const struct device *dev);

int regset_target_lib_read_data(const struct device *dev, off_t offset,
                                void *data, size_t len);

int regset_target_lib_write_data(const struct device *dev, off_t offset,
                                 const void *data, size_t len);

int regset_target_lib_set_addr(const struct device *dev, uint8_t addr);

extern const struct i2c_target_driver_api regset_target_api;

int regset_target_lib_init(const struct device *dev);

#define REGSET_TARGET_LIB_STRUCT_CHECK(config, data)                            \
        BUILD_ASSERT(offsetof(config, regset_cfg) == 0,                         \
                     "struct regset_target_lib_config must be placed first");   \
        BUILD_ASSERT(offsetof(data, regset_data) == 0,                          \
                     "struct regset_target_lib_data must be placed first")

#define REGSET_TARGET_LIB_DT_BUILD_ASSERT(node_id)                                              \
        BUILD_ASSERT(DT_PROP(node_id, size) <= (1 << DT_PROP_OR(node_id, address_width, 8)),    \
                     "size must be <= than 2^address_width");

#define REGSET_TARGET_LIB_DT_INST_BUILD_ASSERT(inst)            \
        REGSET_TARGET_LIB_DT_BUILD_ASSERT(DT_DRV_INST(inst))

#define REGSET_TARGET_LIB_DT_CONFIG_INIT(node_id)               \
{                                                               \
        .bus = I2C_DT_SPEC_GET(node_id),                        \
        .buffer_size = DT_PROP(node_id, size),                  \
        .buffer = (uint8_t[DT_PROP(node_id, size)]) {},         \
        .address_width = DT_PROP_OR(node_id, address_width, 8), \
        .auto_register = DT_PROP(node_id, auto_register),       \
}

#define REGSET_TARGET_LIB_DT_INST_CONFIG_INIT(inst) \
        REGSET_TARGET_LIB_DT_CONFIG_INIT(DT_DRV_INST(inst))

#endif /* ZEPHYR_INCLUDE_DRIVERS_I2C_TARGET_REGSET_TARGET_LIB_H_ */
```

## 700.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright (c) 2017 BayLibre, SAS。

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 174 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_I2C_TARGET_REGSET_TARGET_LIB_H_`。

## 700.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [regset_target_lib_changed_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h.html#ae9e6dd062981be4f7c429ffb12452745)
- [device](../device_reference/P002_设备对象结构.md)
- [regset_target_lib_data](../system_service_model_reference/P076_regset_target_lib_data_结构体.md)
- [i2c_target_config](../hardware/P309_I2C目标配置.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [regset_target_lib_config](../system_service_model_reference/P075_regset_target_lib_config_结构体.md)
- [i2c_dt_spec](../hardware/P306_I2C设备树描述.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [regset_target_lib_set_changed_callback](https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h.html#ad92d2e54bdf7426ea49cea95930fa142)
- [regset_target_lib_get_size](https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h.html#ace6db98c44d46daff92c8d7f29fd4f54)
- [regset_target_lib_read_data](https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h.html#aff17ae03f428fd989be2b108f87d3f49)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [regset_target_lib_write_data](https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h.html#a746682f1490935846f189fddae22f4ac)
- [regset_target_lib_set_addr](https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h.html#aab1502efe79713b23cc9b66add677c1a)
- [addr](../hardware/P306_I2C设备树描述.md#a85242ab56b1e8633b7001353990392fa)
- [i2c_target_driver_api](../hardware/P315_I2C目标驱动函数表.md)
- [regset_target_api](https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h.html#af4882a009f613f2adccabd25019ee44a)
- [regset_target_lib_init](https://docs.zephyrproject.org/latest/doxygen/html/regset__target__lib_8h.html#afb1e7a6fe4e25d22f335c00da29c2378)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [i2c_dt_spec::addr](../hardware/P306_I2C设备树描述.md#a85242ab56b1e8633b7001353990392fa)

---

[上一章](P699_regions.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P701_regulator.h_源码浏览.md)
