---
id: learning.zephyr-docs.api-source-reference.page-223
title: emul_bbram.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/emul__bbram_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第223章\_emul\_bbram.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/emul__bbram_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/emul__bbram_8h.html)。

## 223.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00026"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00044"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
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
<a id="foldopen00083"></a>
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
<a id="l00102"></a>
<a id="l00103"></a>
<a id="adrivers_2emul_8h_html"></a>
<a id="agroup__bbram__emulator__backend_html_ga92942f1ebe6905ad3cfe389824af5914"></a>
<a id="agroup__bbram__emulator__backend_html_gaeff1fa9acd765323778c42a4c3424c0b"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructemul_html"></a>
<a id="astructemul_html_a82f3fcaf221cd329ef1b6cb93cc7c8e6"></a>
<a id="astructemul_html_ac7e90a7ff00a0c08836821c7d49b7dea"></a>

```c
/*
 * Copyright 2024 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef INCLUDE_ZEPHYR_DRIVERS_EMUL_BBRAM_H_
#define INCLUDE_ZEPHYR_DRIVERS_EMUL_BBRAM_H_

#include <zephyr/drivers/emul.h>

#include <stdint.h>



__subsystem struct emul_bbram_driver_api {
        int (*set_data)(const struct emul *target, size_t offset, size_t count,
                        const uint8_t *data);
        int (*get_data)(const struct emul *target, size_t offset, size_t count, uint8_t *data);
};


static inline int emul_bbram_backend_set_data(const struct emul *target, size_t offset,
                                              size_t count, const uint8_t *data)
{
        if (target == NULL || target->backend_api == NULL) {
                return -ENOTSUP;
        }

        struct emul_bbram_driver_api *api = (struct emul_bbram_driver_api *)target->backend_api;

        if (api->set_data == NULL) {
                return -ENOTSUP;
        }

        return api->set_data(target, offset, count, data);
}

static inline int emul_bbram_backend_get_data(const struct emul *target, size_t offset,
                                              size_t count, uint8_t *data)
{
        if (target == NULL || target->backend_api == NULL) {
                return -ENOTSUP;
        }

        struct emul_bbram_driver_api *api = (struct emul_bbram_driver_api *)target->backend_api;

        if (api->get_data == NULL) {
                return -ENOTSUP;
        }

        return api->get_data(target, offset, count, data);
}


#endif /* INCLUDE_ZEPHYR_DRIVERS_EMUL_BBRAM_H_ */
```

## 223.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 103 行

头文件保护宏（Header guard）标记：`INCLUDE_ZEPHYR_DRIVERS_EMUL_BBRAM_H_`。

## 223.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/emul__bbram_8h.html)
- [zephyr/drivers/emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [emul_bbram_backend_set_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__emulator__backend.html#gaeff1fa9acd765323778c42a4c3424c0b)
- [emul](../hardware/P477_仿真器实例结构.md)
- [data](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#a82f3fcaf221cd329ef1b6cb93cc7c8e6)
- [backend_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#ac7e90a7ff00a0c08836821c7d49b7dea)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [emul_bbram_backend_get_data](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__emulator__backend.html#ga92942f1ebe6905ad3cfe389824af5914)
- [emul.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2emul_8h.html)
- [emul::data](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#a82f3fcaf221cd329ef1b6cb93cc7c8e6)
- [emul::backend_api](https://docs.zephyrproject.org/latest/doxygen/html/structemul.html#ac7e90a7ff00a0c08836821c7d49b7dea)

---

[上一章](P222_emsdp-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P224_emul_bc12.h_源码浏览.md)
