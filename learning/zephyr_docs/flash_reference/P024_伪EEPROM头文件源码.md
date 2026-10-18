---
id: learning.zephyr-docs.flash-reference.page-24
title: 伪EEPROM头文件源码
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/eeprom__fake_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_伪EEPROM头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/eeprom__fake_8h_source.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。原网页省略了用于生成接口文档的部分注释，因此原行号会跳跃；这里的“全部可见代码”不等于包含所有文档注释的原始文件。接口说明、参数与返回值见[对应头文件参考](P023_伪EEPROM头文件参考.md)及[本册大纲](大纲.md)。

## 24.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="aeeprom_8h_html"></a>
<a id="agroup__eeprom__fake_html_ga0afb1c3d28fe1f0883c7a7c744edc5d8"></a>
<a id="agroup__eeprom__fake_html_ga2484447bd0c4d5d43a56fd42a893de61"></a>
<a id="agroup__eeprom__fake_html_ga6238da3c648ca23d4be16853feee071d"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2022 Vestas Wind Systems A/S
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_EEPROM_EEPROM_FAKE_H_
#define ZEPHYR_INCLUDE_DRIVERS_EEPROM_EEPROM_FAKE_H_

#include <zephyr/drivers/eeprom.h>
#include <zephyr/fff.h>

#ifdef __cplusplus
extern "C" {
#endif


DECLARE_FAKE_VALUE_FUNC(int, fake_eeprom_read, const struct device *, off_t, void *, size_t);

DECLARE_FAKE_VALUE_FUNC(int, fake_eeprom_write, const struct device *, off_t, const void *, size_t);

DECLARE_FAKE_VALUE_FUNC(size_t, fake_eeprom_size, const struct device *);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_EEPROM_EEPROM_FAKE_H_ */
```

## 24.2\_可见注释译文（Comments）

1. 版权为2022年Vestas Wind Systems A/S；许可证为Apache-2.0。法律署名按原样保留。

2. 结束ZEPHYR_INCLUDE_DRIVERS_EEPROM_EEPROM_FAKE_H_头文件包含保护（Header Include Guard）。

## 24.3\_源码跟踪译注

> 译注——伪函数声明：DECLARE_FAKE_VALUE_FUNC由伪函数框架（Fake Function Framework，FFF）生成伪函数及其控制对象声明。源页保留宏调用，API页面则显示展开后的函数签名。控制对象通常使用函数名加_fake，可记录参数和调用次数，并通过custom_fake提供行为；默认读取填零、默认写入不形成可读回内容，详见[伪EEPROM接口](../hardware/P051_伪EEPROM接口.md)与[头文件参考](P023_伪EEPROM头文件参考.md)。

仓库相对定位：[include/zephyr/drivers/eeprom/eeprom_fake.h](../../../include/zephyr/drivers/eeprom/eeprom_fake.h)；本次核对的[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/eeprom/eeprom_fake.h)摘要见[来源记录](../SOURCES.md)。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致；不能把这种一致性推广到以后滚动更新的main。

本批未构建、烧录、擦写或实板运行；代码阅读和文档核验不代表硬件操作通过。

## 24.4\_原页交叉引用（Cross References）

- [查看此文件参考说明](P023_伪EEPROM头文件参考.md)
- [zephyr/drivers/eeprom.h](P021_EEPROM公共头文件参考.md)
- [fake_eeprom_read](../hardware/P051_伪EEPROM接口.md#ga6238da3c648ca23d4be16853feee071d)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [fake_eeprom_write](../hardware/P051_伪EEPROM接口.md#ga2484447bd0c4d5d43a56fd42a893de61)
- [fake_eeprom_size](../hardware/P051_伪EEPROM接口.md#ga0afb1c3d28fe1f0883c7a7c744edc5d8)

---

[上一章](P023_伪EEPROM头文件参考.md) · [返回大纲](大纲.md) · [下一章](P025_I2C目标EEPROM头文件参考.md)
