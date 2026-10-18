---
id: learning.zephyr-docs.api-source-reference.page-166
title: devicetree.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mspi_2devicetree_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第166章\_devicetree.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mspi_2devicetree_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mspi_2devicetree_8h.html)。

## 166.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
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
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="foldopen00102"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="foldopen00126"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="foldopen00142"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="foldopen00166"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="foldopen00220"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="foldopen00233"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="foldopen00247"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="foldopen00263"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="foldopen00304"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="adrivers_2gpio_8h_html"></a>

```c
/*
 * Copyright (c) 2024, Ambiq Micro Inc. <www.ambiq.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MSPI_DEVICETREE_H_
#define ZEPHYR_INCLUDE_DRIVERS_MSPI_DEVICETREE_H_


#include <zephyr/drivers/gpio.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MSPI_DEVICE_CONFIG_DT(mspi_dev)                                                           \
        {                                                                                         \
                .ce_num               = DT_PROP_OR(mspi_dev, mspi_hardware_ce_num, 0),            \
                .freq                 = DT_PROP(mspi_dev, mspi_max_frequency),                    \
                .io_mode              = DT_ENUM_IDX_OR(mspi_dev, mspi_io_mode,                    \
                                                MSPI_IO_MODE_SINGLE),                             \
                .data_rate            = DT_ENUM_IDX_OR(mspi_dev, mspi_data_rate,                  \
                                                MSPI_DATA_RATE_SINGLE),                           \
                .cpp                  = DT_ENUM_IDX_OR(mspi_dev, mspi_cpp_mode, MSPI_CPP_MODE_0), \
                .endian               = DT_ENUM_IDX_OR(mspi_dev, mspi_endian,                     \
                                                MSPI_XFER_LITTLE_ENDIAN),                         \
                .ce_polarity          = DT_ENUM_IDX_OR(mspi_dev, mspi_ce_polarity,                \
                                                MSPI_CE_ACTIVE_LOW),                              \
                .dqs_enable           = DT_PROP(mspi_dev, mspi_dqs_enable),                       \
                .rx_dummy             = DT_PROP_OR(mspi_dev, rx_dummy, 0),                        \
                .tx_dummy             = DT_PROP_OR(mspi_dev, tx_dummy, 0),                        \
                .read_cmd             = DT_PROP_OR(mspi_dev, read_command, 0),                    \
                .write_cmd            = DT_PROP_OR(mspi_dev, write_command, 0),                   \
                .cmd_length           = DT_ENUM_IDX_OR(mspi_dev, command_length, 0),              \
                .addr_length          = DT_ENUM_IDX_OR(mspi_dev, address_length, 0),              \
                .mem_boundary         = COND_CODE_1(DT_NODE_HAS_PROP(mspi_dev, ce_break_config),  \
                                                (DT_PROP_BY_IDX(mspi_dev, ce_break_config, 0)),   \
                                                (0)),                                             \
                .time_to_break        = COND_CODE_1(DT_NODE_HAS_PROP(mspi_dev, ce_break_config),  \
                                                (DT_PROP_BY_IDX(mspi_dev, ce_break_config, 1)),   \
                                                (0)),                                             \
        }

#define MSPI_DEVICE_CONFIG_DT_INST(inst) MSPI_DEVICE_CONFIG_DT(DT_DRV_INST(inst))

#define MSPI_MEMMAP_CONFIG_DT_NO_CHECK(mspi_dev)                                                  \
        {                                                                                         \
                .enable               = DT_PROP_BY_IDX(mspi_dev, memmap_config, 0),               \
                .address_offset       = DT_PROP_BY_IDX(mspi_dev, memmap_config, 1),               \
                .size                 = DT_PROP_BY_IDX(mspi_dev, memmap_config, 2),               \
                .permission           = DT_PROP_BY_IDX(mspi_dev, memmap_config, 3),               \
        }

#define MSPI_MEMMAP_CONFIG_DT(mspi_dev)                                                           \
                COND_CODE_1(DT_NODE_HAS_PROP(mspi_dev, memmap_config),                            \
                        (MSPI_MEMMAP_CONFIG_DT_NO_CHECK(mspi_dev)),                               \
                        ({}))

#define MSPI_MEMMAP_CONFIG_DT_INST(inst) MSPI_MEMMAP_CONFIG_DT(DT_DRV_INST(inst))

#define MSPI_SCRAMBLE_CONFIG_DT_NO_CHECK(mspi_dev)                                                \
        {                                                                                         \
                .enable               = DT_PROP_BY_IDX(mspi_dev, scramble_config, 0),             \
                .address_offset       = DT_PROP_BY_IDX(mspi_dev, scramble_config, 1),             \
                .size                 = DT_PROP_BY_IDX(mspi_dev, scramble_config, 2),             \
        }

#define MSPI_SCRAMBLE_CONFIG_DT(mspi_dev)                                                         \
                COND_CODE_1(DT_NODE_HAS_PROP(mspi_dev, scramble_config),                          \
                        (MSPI_SCRAMBLE_CONFIG_DT_NO_CHECK(mspi_dev)),                             \
                        ({}))

#define MSPI_SCRAMBLE_CONFIG_DT_INST(inst) MSPI_SCRAMBLE_CONFIG_DT(DT_DRV_INST(inst))

#define MSPI_DEVICE_ID_DT(mspi_dev)                                                               \
        {                                                                                         \
                .ce                   = MSPI_DEV_CE_GPIOS_DT_SPEC_GET(mspi_dev),                  \
                .dev_idx              = DT_REG_ADDR(mspi_dev),                                    \
        }

#define MSPI_DEVICE_ID_DT_INST(inst) MSPI_DEVICE_ID_DT(DT_DRV_INST(inst))


#define MSPI_DEV_CE_GPIOS_DT_SPEC_GET(mspi_dev)                                                   \
                GPIO_DT_SPEC_GET_BY_IDX_OR(DT_BUS(mspi_dev), ce_gpios,                            \
                                           DT_REG_ADDR_RAW(mspi_dev), {})

#define MSPI_DEV_CE_GPIOS_DT_SPEC_INST_GET(inst)                                                  \
                MSPI_DEV_CE_GPIOS_DT_SPEC_GET(DT_DRV_INST(inst))


#define MSPI_CE_GPIOS_DT_SPEC_GET(node_id)                                                        \
{                                                                                                 \
        COND_CODE_1(DT_NODE_HAS_PROP(node_id, ce_gpios),                                          \
                (DT_FOREACH_PROP_ELEM_SEP(node_id, ce_gpios, GPIO_DT_SPEC_GET_BY_IDX, (,))),      \
                ())                                                                               \
}

#define MSPI_CE_GPIOS_DT_SPEC_INST_GET(inst)                                                      \
                MSPI_CE_GPIOS_DT_SPEC_GET(DT_DRV_INST(inst))

#define MSPI_CE_CONTROL_INIT(node_id, delay_)                                                     \
        {                                                                                         \
                .gpio = MSPI_DEV_CE_GPIOS_DT_SPEC_GET(node_id), .delay = (delay_),                \
        }

#define MSPI_CE_CONTROL_INIT_INST(inst, delay_) MSPI_CE_CONTROL_INIT(DT_DRV_INST(inst), delay_)

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_MSPI_DEVICETREE_H_ */
```

## 166.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024, Ambiq Micro Inc. <www.ambiq.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 332 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MSPI_DEVICETREE_H_`。

## 166.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mspi_2devicetree_8h.html)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)

---

[上一章](P165_nxp_rtxxx_dsp_ctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P167_npm10xx.h_源码浏览.md)
