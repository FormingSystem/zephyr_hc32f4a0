---
id: learning.zephyr-docs.api-source-reference.page-292
title: gnss_emul.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gnss__emul_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第292章\_gnss\_emul.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gnss__emul_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gnss__emul_8h.html)。

## 292.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="adevice_8h_html"></a>
<a id="agnss_8h_html"></a>
<a id="agnss__emul_8h_html_a42f9dcdcc01e72d4d5d602aaf5f5a110"></a>
<a id="agnss__emul_8h_html_a49059255c56cae6e9e774f66f74ff659"></a>
<a id="agnss__emul_8h_html_a6616b032895a90cfe1e8128108bf051b"></a>
<a id="agnss__emul_8h_html_a9a94d20cae75b015b5903ace386ceeb8"></a>
<a id="agnss__emul_8h_html_ad81023468758a4a07a69a0509e002b10"></a>
<a id="agroup__gnss__interface_html_ga731907f9ae501909bf26ecae5441a5ce"></a>
<a id="agroup__gnss__interface_html_gadb734bb12433276d3014e08a1d21bb18"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructdevice_html"></a>
<a id="astructgnss__info_html"></a>
<a id="astructnavigation__data_html"></a>

```c
/*
 * Copyright (c) 2025 Embeint Pty Ltd
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_DRIVERS_GNSS_GNSS_EMUL_H_
#define ZEPHYR_DRIVERS_GNSS_GNSS_EMUL_H_

#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/drivers/gnss.h>

void gnss_emul_clear_data(const struct device *dev);

void gnss_emul_set_data(const struct device *dev, const struct navigation_data *nav,
                        const struct gnss_info *info, int64_t boot_realtime_ms);

int gnss_emul_get_fix_rate(const struct device *dev, uint32_t *fix_interval_ms);

int gnss_emul_get_navigation_mode(const struct device *dev, enum gnss_navigation_mode *mode);

int gnss_emul_get_enabled_systems(const struct device *dev, gnss_systems_t *systems);

#endif /* ZEPHYR_DRIVERS_GNSS_GNSS_EMUL_H_ */
```

## 292.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Embeint Pty Ltd。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 63 行

头文件保护宏（Header guard）标记：`ZEPHYR_DRIVERS_GNSS_GNSS_EMUL_H_`。

## 292.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gnss__emul_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/gnss.h](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h.html)
- [gnss_emul_clear_data](https://docs.zephyrproject.org/latest/doxygen/html/gnss__emul_8h.html#a9a94d20cae75b015b5903ace386ceeb8)
- [device](../device_reference/P002_设备对象结构.md)
- [gnss_emul_set_data](https://docs.zephyrproject.org/latest/doxygen/html/gnss__emul_8h.html#a6616b032895a90cfe1e8128108bf051b)
- [navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)
- [gnss_info](../sensor_navigation_model_reference/P012_gnss_info_结构体.md)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [gnss_emul_get_fix_rate](https://docs.zephyrproject.org/latest/doxygen/html/gnss__emul_8h.html#a49059255c56cae6e9e774f66f74ff659)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [gnss_emul_get_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/gnss__emul_8h.html#ad81023468758a4a07a69a0509e002b10)
- [gnss_navigation_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#gadb734bb12433276d3014e08a1d21bb18)
- [gnss_emul_get_enabled_systems](https://docs.zephyrproject.org/latest/doxygen/html/gnss__emul_8h.html#a42f9dcdcc01e72d4d5d602aaf5f5a110)
- [gnss_systems_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gnss__interface.html#ga731907f9ae501909bf26ecae5441a5ce)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [gnss.h](https://docs.zephyrproject.org/latest/doxygen/html/gnss_8h.html)

---

[上一章](P291_gnss.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P293_gnss_publish.h_源码浏览.md)
