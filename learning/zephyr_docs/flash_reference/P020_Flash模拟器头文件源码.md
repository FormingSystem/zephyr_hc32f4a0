---
id: learning.zephyr-docs.flash-reference.page-20
title: Flash模拟器头文件源码
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/flash__simulator_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_Flash模拟器头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/flash__simulator_8h_source.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。原网页省略了用于生成接口文档的部分注释，因此原行号会跳跃；这里的“全部可见代码”不等于包含所有文档注释的原始文件。接口说明、参数与返回值见[对应头文件参考](P017_Flash模拟器接口.md)及[本册大纲](大纲.md)。

## 20.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00023"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="adevice_8h_html"></a>
<a id="aflash__simulator_8h_html_a0ba212692f650a34238b0f2763a541c7"></a>
<a id="aflash__simulator_8h_html_a24b9919bf5776683d1890c46ed961bd5"></a>
<a id="aflash__simulator_8h_html_a71cca7b794f8e9402d81491c7e93cc3f"></a>
<a id="aflash__simulator_8h_html_a860ecc612edda863f4f86ec690bec979"></a>
<a id="aflash__simulator_8h_html_ac944ca905ff40848d2a566e45e446096"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructflash__simulator__cb_html"></a>
<a id="astructflash__simulator__cb_html_a62ae850896b86b36cd5c478c8bfc614b"></a>
<a id="astructflash__simulator__cb_html_a70774e9972fe53c2c6fd13cfb0797de1"></a>
<a id="astructflash__simulator__params_html"></a>
<a id="astructflash__simulator__params_html_a36ce56491f38836e9cf3f797cf6117e2"></a>
<a id="astructflash__simulator__params_html_a4159a11d6b52a5afc8a98eda6a1f6de6"></a>
<a id="astructflash__simulator__params_html_a4c9c5d6c1a9876044e05457353e0bb46"></a>
<a id="astructflash__simulator__params_html_a7a4c60e8a1d7f3c4761cc8d58e2d1fc1"></a>
<a id="astructflash__simulator__params_html_a84d687fd28d14b59019ee0e881c1ff0e"></a>
<a id="astructflash__simulator__params_html_ab30c470b8f3638bba19ee5dae2bddb68"></a>

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DRIVERS_FLASH_FLASH_SIMULATOR_H_
#define ZEPHYR_INCLUDE_DRIVERS_FLASH_FLASH_SIMULATOR_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/device.h>
#include <zephyr/types.h>
#include <sys/types.h>


struct flash_simulator_params {
        size_t memory_size;
        size_t base_offset;
        size_t erase_unit;
        size_t prog_unit;
        bool explicit_erase;
        uint8_t erase_value;
};

typedef int (*flash_simulator_write_byte_cb_t)(const struct device *dev,
                                               off_t offset,
                                               uint8_t data);

typedef int (*flash_simulator_erase_unit_cb_t)(const struct device *dev, off_t unit_offset);

struct flash_simulator_cb {
        flash_simulator_write_byte_cb_t write_byte;
        flash_simulator_erase_unit_cb_t erase_unit;
};

__syscall const struct flash_simulator_params *flash_simulator_get_params(const struct device *dev);

__syscall void flash_simulator_set_callbacks(const struct device *dev,
                                             const struct flash_simulator_cb *cb);

__syscall void *flash_simulator_get_memory(const struct device *dev,
                                           size_t *mock_size);
#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/flash_simulator.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_FLASH_FLASH_SIMULATOR_H_ */
```

## 20.2\_可见注释译文（Comments）

1. 版权为2021年Nordic Semiconductor ASA；许可证为Apache-2.0。法律署名按原样保留。

2. 结束ZEPHYR_INCLUDE_DRIVERS_FLASH_FLASH_SIMULATOR_H_头文件包含保护（Header Include Guard）。

## 20.3\_源码跟踪译注

> 译注——回调与缓冲区：write_byte返回将写入的字节值，负值表示错误；erase_unit回调负责实际模拟擦除，成功返回0。当前设置函数保存回调结构指针而不复制内容，结构须在使用期间有效。get_params在未启用CONFIG_FLASH_SIMULATOR_CALLBACKS时返回NULL；get_memory要求mock_size指向有效输出变量。详细边界见[模拟器API](P017_Flash模拟器接口.md)。

仓库相对定位：[include/zephyr/drivers/flash/flash_simulator.h](../../../include/zephyr/drivers/flash/flash_simulator.h)；本次核对的[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash/flash_simulator.h)摘要见[来源记录](../SOURCES.md)。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致；不能把这种一致性推广到以后滚动更新的main。

本批未构建、烧录、擦写或实板运行；代码阅读和文档核验不代表硬件操作通过。

## 20.4\_原页交叉引用（Cross References）

- [查看此文件参考说明](P017_Flash模拟器接口.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [flash_simulator_params](P018_Flash模拟器参数.md)
- [memory_size](P018_Flash模拟器参数.md#a4c9c5d6c1a9876044e05457353e0bb46)
- [base_offset](P018_Flash模拟器参数.md#a4159a11d6b52a5afc8a98eda6a1f6de6)
- [erase_unit](P018_Flash模拟器参数.md#a84d687fd28d14b59019ee0e881c1ff0e)
- [prog_unit](P018_Flash模拟器参数.md#a7a4c60e8a1d7f3c4761cc8d58e2d1fc1)
- [explicit_erase](P018_Flash模拟器参数.md#ab30c470b8f3638bba19ee5dae2bddb68)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [erase_value](P018_Flash模拟器参数.md#a36ce56491f38836e9cf3f797cf6117e2)
- [flash_simulator_write_byte_cb_t](P017_Flash模拟器接口.md#a860ecc612edda863f4f86ec690bec979)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [flash_simulator_erase_unit_cb_t](P017_Flash模拟器接口.md#a24b9919bf5776683d1890c46ed961bd5)
- [flash_simulator_cb](P019_Flash模拟器回调.md)
- [write_byte](P019_Flash模拟器回调.md#a62ae850896b86b36cd5c478c8bfc614b)
- [erase_unit](P019_Flash模拟器回调.md#a70774e9972fe53c2c6fd13cfb0797de1)
- [flash_simulator_get_params](P017_Flash模拟器接口.md#ac944ca905ff40848d2a566e45e446096)
- [flash_simulator_set_callbacks](P017_Flash模拟器接口.md#a0ba212692f650a34238b0f2763a541c7)
- [flash_simulator_get_memory](P017_Flash模拟器接口.md#a71cca7b794f8e9402d81491c7e93cc3f)

---

[上一章](P019_Flash模拟器回调.md) · [返回大纲](大纲.md) · [下一章](P021_EEPROM公共头文件参考.md)
