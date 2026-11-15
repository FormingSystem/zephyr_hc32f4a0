---
id: learning.zephyr-docs.flash-reference.page-26
title: I2C目标EEPROM头文件源码
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/i2c_2target_2eeprom_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_I2C目标EEPROM头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/i2c_2target_2eeprom_8h_source.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。原网页省略了用于生成接口文档的部分注释，因此原行号会跳跃；这里的“全部可见代码”不等于包含所有文档注释的原始文件。接口说明、参数与返回值见[对应头文件参考](P025_I2C目标EEPROM头文件参考.md)及[本册大纲](大纲.md)。

## 26.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00026"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="agroup__i2c__eeprom__target__api_html_ga1543dbc12e26df856eac01b1a686d7c5"></a>
<a id="agroup__i2c__eeprom__target__api_html_ga3da67a267034e3b90c1a7c84588c3839"></a>
<a id="agroup__i2c__eeprom__target__api_html_ga72b88bc1df1ec097ed677f94e9dad875"></a>
<a id="agroup__i2c__eeprom__target__api_html_ga769f4b319013956d58fdc56d378519aa"></a>
<a id="agroup__i2c__eeprom__target__api_html_ga802f5d779e9a837a81b8b617037dfce8"></a>
<a id="agroup__i2c__eeprom__target__api_html_ga8c2d7c18fcec4ce2241850f031966a89"></a>
<a id="agroup__i2c__eeprom__target__api_html_gaab87512e92f7f50b93019c5f9255c4a7"></a>
<a id="agroup__i2c__eeprom__target__api_html_gad562c9ac13d3fa7a7b43c1d8ba415f11"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>

```c


/*
 * Copyright (c) 2017 BayLibre, SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DRIVERS_I2C_TARGET_EEPROM_H_
#define ZEPHYR_INCLUDE_DRIVERS_I2C_TARGET_EEPROM_H_

#include <stddef.h>
#include <sys/types.h>


typedef void (*eeprom_target_changed_handler_t)(const struct device *dev, void *user_data);

void eeprom_target_set_changed_callback(const struct device *dev,
                                        eeprom_target_changed_handler_t handler,
                                        void *user_data);

size_t eeprom_target_get_size(const struct device *dev);

int eeprom_target_read_data(const struct device *dev, off_t offset,
                            void *data, size_t len);

int eeprom_target_write_data(const struct device *dev, off_t offset,
                             const void *data, size_t len);

static inline __deprecated int eeprom_target_program(const struct device *dev,
                                                     const uint8_t *eeprom_data,
                                                     unsigned int length)
{
        return eeprom_target_write_data(dev, 0, eeprom_data, length);
}

static inline int eeprom_target_read(const struct device *dev, uint8_t *eeprom_data,
                                     unsigned int offset)
{
        return eeprom_target_read_data(dev, offset, eeprom_data, 1);
}

int eeprom_target_set_addr(const struct device *dev, uint8_t addr);


#endif /* ZEPHYR_INCLUDE_DRIVERS_I2C_TARGET_EEPROM_H_ */
```

## 26.2\_可见注释译文（Comments）

1. 版权为2017年BayLibre, SAS；许可证为Apache-2.0。法律署名按原样保留。

2. 结束ZEPHYR_INCLUDE_DRIVERS_I2C_TARGET_EEPROM_H_头文件包含保护（Header Include Guard）。

## 26.3\_源码跟踪译注

> 译注——目标角色与兼容包装：这里的I²C（Inter-Integrated Circuit）接口描述本机作为EEPROM目标端，和EEPROM控制器侧驱动不同。已弃用的eeprom_target_program固定从偏移0写入；eeprom_target_read包装为指定偏移的单字节读取。当前运行时改地址实现依赖CONFIG_I2C_EEPROM_TARGET_RUNTIME_ADDR，不能只凭无条件函数声明假定链接时可用。完整说明见[I2C目标EEPROM接口](../hardware/P313_I2CEEPROM目标接口.md)。

仓库相对定位：[include/zephyr/drivers/i2c/target/eeprom.h](../../../include/zephyr/drivers/i2c/target/eeprom.h)；本次核对的[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/i2c/target/eeprom.h)摘要见[来源记录](../SOURCES.md)。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致；不能把这种一致性推广到以后滚动更新的main。

本批未构建、烧录、擦写或实板运行；代码阅读和文档核验不代表硬件操作通过。

## 26.4\_原页交叉引用（Cross References）

- [查看此文件参考说明](P025_I2C目标EEPROM头文件参考.md)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [eeprom_target_changed_handler_t](../hardware/P313_I2CEEPROM目标接口.md#ga769f4b319013956d58fdc56d378519aa)
- [device](../device_reference/P002_设备对象结构.md)
- [eeprom_target_set_changed_callback](../hardware/P313_I2CEEPROM目标接口.md#gaab87512e92f7f50b93019c5f9255c4a7)
- [eeprom_target_get_size](../hardware/P313_I2CEEPROM目标接口.md#ga3da67a267034e3b90c1a7c84588c3839)
- [eeprom_target_read_data](../hardware/P313_I2CEEPROM目标接口.md#ga1543dbc12e26df856eac01b1a686d7c5)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [eeprom_target_write_data](../hardware/P313_I2CEEPROM目标接口.md#gad562c9ac13d3fa7a7b43c1d8ba415f11)
- [eeprom_target_program](../hardware/P313_I2CEEPROM目标接口.md#ga8c2d7c18fcec4ce2241850f031966a89)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [eeprom_target_read](../hardware/P313_I2CEEPROM目标接口.md#ga72b88bc1df1ec097ed677f94e9dad875)
- [eeprom_target_set_addr](../hardware/P313_I2CEEPROM目标接口.md#ga802f5d779e9a837a81b8b617037dfce8)

---

[上一章](P025_I2C目标EEPROM头文件参考.md) · [返回大纲](大纲.md)
