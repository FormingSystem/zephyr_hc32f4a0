---
id: learning.zephyr-docs.api-source-reference.page-328
title: i2c_emul.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/i2c__emul_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第328章\_i2c\_emul.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/i2c__emul_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/i2c__emul_8h.html)。

## 328.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2emul_8h_html"></a>
<a id="adrivers_2i2c_8h_html"></a>
<a id="agroup__i2c__emul__interface_html_ga1b27ff11534eeac47cf50ffb2a1c7cca"></a>
<a id="agroup__i2c__emul__interface_html_ga92851f09c23531bbaea25301dc2607ce"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructemul_html"></a>
<a id="astructi2c__emul__api_html"></a>
<a id="astructi2c__emul__api_html_af155e9e2145597c9ca14473ddf01d48f"></a>
<a id="astructi2c__emul_html"></a>
<a id="astructi2c__emul_html_a33461303343c3f513a87f1783491324a"></a>
<a id="astructi2c__emul_html_a72324f94030625a8be49101f49875a7a"></a>
<a id="astructi2c__emul_html_a7e6f7e6e69064df666584027c94bf98c"></a>
<a id="astructi2c__emul_html_a8d3924790bd825afe41095bfdf0087eb"></a>
<a id="astructi2c__emul_html_abf57cb711e20ab11aa5af247ccc652b2"></a>
<a id="astructi2c__msg_html"></a>

```c


/*
 * Copyright 2020 Google LLC
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DRIVERS_I2C_I2C_EMUL_H_
#define ZEPHYR_INCLUDE_DRIVERS_I2C_I2C_EMUL_H_

#include <zephyr/device.h>
#include <zephyr/drivers/emul.h>
#include <zephyr/drivers/i2c.h>
#include <zephyr/sys/slist.h>
#include <zephyr/types.h>


#ifdef __cplusplus
extern "C" {
#endif

struct i2c_msg;
struct i2c_emul_api;

struct i2c_emul {
        sys_snode_t node;

        const struct emul *target;

        const struct i2c_emul_api *api;

        struct i2c_emul_api *mock_api;

        uint16_t addr;
};

typedef int (*i2c_emul_transfer_t)(const struct emul *target, struct i2c_msg *msgs, int num_msgs,
                                   int addr);

int i2c_emul_register(const struct device *dev, struct i2c_emul *emul);

struct i2c_emul_api {
        i2c_emul_transfer_t transfer;
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_I2C_I2C_EMUL_H_ */
```

## 328.2\_可见注释译文（Comments）

### 注释 1：原第 8 行

版权（Copyright）：2020 Google LLC。

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 98 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_I2C_I2C_EMUL_H_`。

## 328.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/i2c__emul_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P001_I2C驱动头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [i2c_msg](../hardware/P307_I2C消息结构.md)
- [i2c_emul_api](../hardware/P317_I2C模拟函数表.md)
- [i2c_emul](../hardware/P316_I2C模拟设备节点.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](https://docs.zephyrproject.org/latest/doxygen/html/structi2c__emul.html#a72324f94030625a8be49101f49875a7a)
- [emul](../hardware/P477_仿真器实例结构.md)
- [target](https://docs.zephyrproject.org/latest/doxygen/html/structi2c__emul.html#a33461303343c3f513a87f1783491324a)
- [api](https://docs.zephyrproject.org/latest/doxygen/html/structi2c__emul.html#a7e6f7e6e69064df666584027c94bf98c)
- [mock_api](https://docs.zephyrproject.org/latest/doxygen/html/structi2c__emul.html#abf57cb711e20ab11aa5af247ccc652b2)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [addr](https://docs.zephyrproject.org/latest/doxygen/html/structi2c__emul.html#a8d3924790bd825afe41095bfdf0087eb)
- [i2c_emul_transfer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__emul__interface.html#ga1b27ff11534eeac47cf50ffb2a1c7cca)
- [i2c_emul_register](https://docs.zephyrproject.org/latest/doxygen/html/group__i2c__emul__interface.html#ga92851f09c23531bbaea25301dc2607ce)
- [device](../device_reference/P002_设备对象结构.md)
- [transfer](https://docs.zephyrproject.org/latest/doxygen/html/structi2c__emul__api.html#af155e9e2145597c9ca14473ddf01d48f)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [i2c.h](../i2c_driver_reference/P001_I2C驱动头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [i2c_emul_api::transfer](https://docs.zephyrproject.org/latest/doxygen/html/structi2c__emul__api.html#af155e9e2145597c9ca14473ddf01d48f)
- [i2c_emul::target](https://docs.zephyrproject.org/latest/doxygen/html/structi2c__emul.html#a33461303343c3f513a87f1783491324a)
- [i2c_emul::node](https://docs.zephyrproject.org/latest/doxygen/html/structi2c__emul.html#a72324f94030625a8be49101f49875a7a)
- [i2c_emul::api](https://docs.zephyrproject.org/latest/doxygen/html/structi2c__emul.html#a7e6f7e6e69064df666584027c94bf98c)
- [i2c_emul::addr](https://docs.zephyrproject.org/latest/doxygen/html/structi2c__emul.html#a8d3924790bd825afe41095bfdf0087eb)
- [i2c_emul::mock_api](https://docs.zephyrproject.org/latest/doxygen/html/structi2c__emul.html#abf57cb711e20ab11aa5af247ccc652b2)

---

[上一章](P327_stm32.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P329_i2c_nrfx_twim.h_源码浏览.md)
