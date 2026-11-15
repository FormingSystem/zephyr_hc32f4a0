---
id: learning.zephyr-docs.api-source-reference.page-157
title: devicetree.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2i3c_2devicetree_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第157章\_devicetree.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2i3c_2devicetree_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2i3c_2devicetree_8h.html)。

## 157.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00052"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00133"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="foldopen00162"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="foldopen00203"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="foldopen00215"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="foldopen00232"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="foldopen00242"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="foldopen00254"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="foldopen00271"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="adevice_8h_html"></a>
<a id="adevicetree_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright 2022 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_I3C_DEVICETREE_H_
#define ZEPHYR_INCLUDE_DRIVERS_I3C_DEVICETREE_H_


#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif

#define I3C_DEVICE_ID_DT(node_id)                                       \
        {                                                               \
                .pid = ((uint64_t)DT_PROP_BY_IDX(node_id, reg, 1) << 32)\
                       | DT_PROP_BY_IDX(node_id, reg, 2),               \
        }

#define I3C_DEVICE_ID_DT_INST(inst)                                     \
        I3C_DEVICE_ID_DT(DT_DRV_INST(inst))


#define I3C_SUPPORTS_SETAASA            BIT(0)
#define I3C_V1P0_SUPPORT                BIT(1)



#define I3C_CONTROLLER_FLAG_DISABLE_BUS_INIT            BIT(0)
#define I3C_CONTROLLER_FLAG_DISABLE_HJ_AT_INIT          BIT(1)


#define I3C_CONTROLLER_CONFIG_FLAGS_DT_INST(inst)                                       \
        (FIELD_PREP(I3C_CONTROLLER_FLAG_DISABLE_BUS_INIT,                               \
                    DT_INST_PROP(inst, disable_bus_init)) |                             \
         FIELD_PREP(I3C_CONTROLLER_FLAG_DISABLE_HJ_AT_INIT,                             \
                    DT_INST_PROP(inst, disable_hj_at_init)))

#define I3C_DEVICE_DESC_DT(node_id)                                                                \
        {                                                                                          \
                .bus = DEVICE_DT_GET(DT_BUS(node_id)),                                             \
                .dev = DEVICE_DT_GET(node_id),                                                     \
                .static_addr = DT_PROP_BY_IDX(node_id, reg, 0),                                    \
                .pid = ((uint64_t)DT_PROP_BY_IDX(node_id, reg, 1) << 32) |                         \
                       DT_PROP_BY_IDX(node_id, reg, 2),                                            \
                .init_dynamic_addr = DT_PROP_OR(node_id, assigned_address, 0),                     \
                .flags = FIELD_PREP(I3C_SUPPORTS_SETAASA, DT_PROP(node_id, supports_setaasa)) |    \
                         FIELD_PREP(I3C_V1P0_SUPPORT, DT_PROP(node_id, v1p0_support)),             \
        },

#define I3C_DEVICE_DESC_DT_INST(inst)                                   \
        I3C_DEVICE_DESC_DT(DT_DRV_INST(inst))

#define I3C_DEVICE_DESC_DT_FILTERED(node_id)                            \
        COND_CODE_0(DT_PROP_BY_IDX(node_id, reg, 1),                    \
                    (), (I3C_DEVICE_DESC_DT(node_id)))

#define I3C_DEVICE_ARRAY_DT(node_id)                                    \
        {                                                               \
                DT_FOREACH_CHILD_STATUS_OKAY(                           \
                        node_id,                                        \
                        I3C_DEVICE_DESC_DT_FILTERED)                    \
        }

#define I3C_DEVICE_ARRAY_DT_INST(inst)                                  \
        I3C_DEVICE_ARRAY_DT(DT_DRV_INST(inst))

#define I3C_DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, level, \
                             prio, api, ...)                            \
        DEVICE_DT_DEFINE(node_id, init_fn, pm, data, config, level,     \
                         prio, api, __VA_ARGS__)

#define I3C_DEVICE_DT_INST_DEFINE(inst, ...)                            \
        I3C_DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)

#define I3C_I2C_DEVICE_DESC_DT(node_id)                                 \
        {                                                               \
                .bus = DEVICE_DT_GET(DT_BUS(node_id)),                  \
                .addr = DT_PROP_BY_IDX(node_id, reg, 0),                \
                .lvr = DT_PROP_BY_IDX(node_id, reg, 2),                 \
        },

#define I3C_I2C_DEVICE_DESC_DT_INST(inst) \
        I3C_I2C_DEVICE_DESC_DT(DT_DRV_INST(inst))


#define I3C_I2C_DEVICE_DESC_DT_FILTERED(node_id)                        \
        COND_CODE_0(DT_PROP_BY_IDX(node_id, reg, 1),                    \
                    (I3C_I2C_DEVICE_DESC_DT(node_id)), ())

#define I3C_I2C_DEVICE_ARRAY_DT(node_id)                                \
        {                                                               \
                DT_FOREACH_CHILD_STATUS_OKAY(                           \
                        node_id,                                        \
                        I3C_I2C_DEVICE_DESC_DT_FILTERED)                \
        }

#define I3C_I2C_DEVICE_ARRAY_DT_INST(inst)                              \
        I3C_I2C_DEVICE_ARRAY_DT(DT_DRV_INST(inst))

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_I3C_DEVICETREE_H_ */
```

## 157.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 282 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_I3C_DEVICETREE_H_`。

## 157.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2i3c_2devicetree_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P156_protocol.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P158_mdio.h_源码浏览.md)
