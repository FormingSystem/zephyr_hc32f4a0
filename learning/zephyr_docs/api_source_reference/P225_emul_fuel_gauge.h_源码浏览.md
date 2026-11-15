---
id: learning.zephyr-docs.api-source-reference.page-225
title: emul_fuel_gauge.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/emul__fuel__gauge_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第225章\_emul\_fuel\_gauge.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/emul__fuel__gauge_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/emul__fuel__gauge_8h.html)。

## 225.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00031"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00044"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="adrivers_2emul_8h_html"></a>
<a id="afuel__gauge_8h_html"></a>
<a id="agroup__fuel__gauge__emulator__backend_html_gab6493138c35191a58e6f28c24b97715e"></a>
<a id="agroup__fuel__gauge__emulator__backend_html_gaf8326331c7470b41aa542f828b20a828"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructemul_html"></a>
<a id="astructemul_html_ac7e90a7ff00a0c08836821c7d49b7dea"></a>

```c
/*
 * Copyright (c) 2023 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_EMUL_FUEL_GAUGE_H_
#define ZEPHYR_INCLUDE_DRIVERS_EMUL_FUEL_GAUGE_H_

#include <stdint.h>
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/fuel_gauge.h>

#ifdef __cplusplus
extern "C" {
#endif


__subsystem struct fuel_gauge_emul_driver_api {
        int (*set_battery_charging)(const struct emul *emul, uint32_t uV, int uA);
        int (*is_battery_cutoff)(const struct emul *emul, bool *cutoff);
};

__syscall int emul_fuel_gauge_set_battery_charging(const struct emul *target, uint32_t uV, int uA);
static inline int z_impl_emul_fuel_gauge_set_battery_charging(const struct emul *target,
                                                              uint32_t uV, int uA)
{
        const struct fuel_gauge_emul_driver_api *backend_api =
                (const struct fuel_gauge_emul_driver_api *)target->backend_api;

        if (backend_api->set_battery_charging == 0) {
                return -ENOTSUP;
        }

        return backend_api->set_battery_charging(target, uV, uA);
}

__syscall int emul_fuel_gauge_is_battery_cutoff(const struct emul *target, bool *cutoff);
static inline int z_impl_emul_fuel_gauge_is_battery_cutoff(const struct emul *target, bool *cutoff)
{
        const struct fuel_gauge_emul_driver_api *backend_api =
                (const struct fuel_gauge_emul_driver_api *)target->backend_api;

        if (backend_api->is_battery_cutoff == 0) {
                return -ENOTSUP;
        }
        return backend_api->is_battery_cutoff(target, cutoff);
}

#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/emul_fuel_gauge.h>


#endif /* ZEPHYR_INCLUDE_DRIVERS_EMUL_FUEL_GAUGE_H_*/
```

## 225.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 104 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_EMUL_FUEL_GAUGE_H_`。

## 225.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/emul__fuel__gauge_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/drivers/emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [zephyr/drivers/fuel_gauge.h](https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [emul_fuel_gauge_set_battery_charging](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__emulator__backend.html#gab6493138c35191a58e6f28c24b97715e)
- [emul](../hardware/P477_仿真器实例结构.md)
- [backend_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#ac7e90a7ff00a0c08836821c7d49b7dea)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [emul_fuel_gauge_is_battery_cutoff](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__emulator__backend.html#gaf8326331c7470b41aa542f828b20a828)
- [emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [fuel_gauge.h](https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h.html)
- [emul::backend_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#ac7e90a7ff00a0c08836821c7d49b7dea)

---

[上一章](P224_emul_bc12.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P226_emul_sensor.h_源码浏览.md)
