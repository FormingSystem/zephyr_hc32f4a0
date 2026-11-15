---
id: learning.zephyr-docs.api-source-reference.page-224
title: emul_bc12.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/emul__bc12_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第224章\_emul\_bc12.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/emul__bc12_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/emul__bc12_8h.html)。

## 224.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00029"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00042"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
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
<a id="l00096"></a>
<a id="l00097"></a>
<a id="adrivers_2emul_8h_html"></a>
<a id="agroup__b12__emulator__backend_html_gaa71771a3199aef043fe313f09f3bb4f2"></a>
<a id="agroup__b12__emulator__backend_html_gaca0e62f2f8a5ec3135523fa3a1308034"></a>
<a id="agroup__b12__interface_html_ga9ae800d490c2cbd3234a81c503649bdb"></a>
<a id="astructemul_html"></a>
<a id="astructemul_html_ac7e90a7ff00a0c08836821c7d49b7dea"></a>
<a id="ausb__bc12_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_USB_EMUL_BC12_H_
#define ZEPHYR_INCLUDE_DRIVERS_USB_EMUL_BC12_H_

#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/usb/usb_bc12.h>

#ifdef __cplusplus
extern "C" {
#endif


__subsystem struct bc12_emul_driver_api {
        int (*set_charging_partner)(const struct emul *emul, enum bc12_type partner_type);
        int (*set_pd_partner)(const struct emul *emul, bool connected);
};

static inline int bc12_emul_set_charging_partner(const struct emul *target,
                                                 enum bc12_type partner_type)
{
        const struct bc12_emul_driver_api *backend_api =
                (const struct bc12_emul_driver_api *)target->backend_api;

        return backend_api->set_charging_partner(target, partner_type);
}

static inline int bc12_emul_set_pd_partner(const struct emul *target, bool connected)
{
        const struct bc12_emul_driver_api *backend_api =
                (const struct bc12_emul_driver_api *)target->backend_api;

        return backend_api->set_pd_partner(target, connected);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_USB_EMUL_BC12_H_ */
```

## 224.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 97 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_USB_EMUL_BC12_H_`。

## 224.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/emul__bc12_8h.html)
- [zephyr/drivers/emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [zephyr/drivers/usb/usb_bc12.h](https://docs.zephyrproject.org/latest/doxygen/html/usb__bc12_8h.html)
- [bc12_type](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__interface.html#ga9ae800d490c2cbd3234a81c503649bdb)
- [bc12_emul_set_charging_partner](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__emulator__backend.html#gaca0e62f2f8a5ec3135523fa3a1308034)
- [emul](../hardware/P477_仿真器实例结构.md)
- [backend_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#ac7e90a7ff00a0c08836821c7d49b7dea)
- [bc12_emul_set_pd_partner](https://docs.zephyrproject.org/latest/doxygen/html/group__b12__emulator__backend.html#gaa71771a3199aef043fe313f09f3bb4f2)
- [emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [emul::backend_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#ac7e90a7ff00a0c08836821c7d49b7dea)
- [usb_bc12.h](https://docs.zephyrproject.org/latest/doxygen/html/usb__bc12_8h.html)

---

[上一章](P223_emul_bbram.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P225_emul_fuel_gauge.h_源码浏览.md)
