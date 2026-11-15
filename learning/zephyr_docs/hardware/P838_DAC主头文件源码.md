---
id: learning.zephyr-docs.hardware.dacmain-1
title: DAC主头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dac_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第838章\_DAC主头文件源码

原文：[dac_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/dac_8h_source.html)。读取日期：2026-10-13，`latest`。

文件 `zephyr/drivers/dac.h` 声明并实现数模转换器（Digital-to-Analog Converter，DAC）的部分通用应用程序接口（Application Programming Interface，API）。网页的文件文档入口对应[主头文件参考](P837_DAC主头文件.md)，公共接口、参数及错误码见[DAC接口](P822_数模转换器接口.md)。

## 838.1\_声明与设备树辅助宏

以下说明用于阅读原始代码。头文件保护宏（Header Guard）防止重复包含；`extern "C"` 保留C++环境中的C语言链接（C Linkage）。通道配置、设备树规格和驱动函数指针分别存放在 [`dac_channel_cfg`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__channel__cfg.html)、[`dac_dt_spec`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__dt__spec.html)、[`dac_driver_api`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__driver__api.html) 三个结构中。

源码页还展示了三个设备树（Devicetree）辅助宏，它们未单独列入公共接口摘要：

| 辅助宏 | 源码中的作用 |
| --- | --- |
| `DAC_DT_SPEC_STRUCT(ctlr, output)` | 使用控制器节点 `ctlr` 和输出编号 `output` 生成规格结构初始化器（Initializer），取得设备指针、通道编号及可用的子节点配置 |
| `DAC_CHANNEL_DT_NODE(ctlr, output)` | 通过 `DT_CHILD_BY_UNIT_ADDR_INT`，以输出编号作为单元地址（Unit Address）查找控制器子节点 |
| `DAC_CHANNEL_CFG_FROM_DT_NODE(node_id)` | 仅在节点存在时填入配置存在标志、通道配置以及 `zephyr,vref-mv` 参考电压；该电压属性缺省值为0 |

这些宏以及全部公共获取宏的标识符和展开式都保留在下方。按索引读取时，若说明单元（Specifier Cell）没有 `output`，源码使用输出编号0。

## 838.2\_驱动分派与有效性判断

`__subsystem` 保留驱动接口结构的子系统标记（Subsystem Annotation），`__syscall` 保留系统调用标记（System Call Annotation）。`z_impl_dac_channel_setup()` 和 `z_impl_dac_write_value()` 通过 `DEVICE_API_GET(dac, dev)` 取得驱动操作表，并分别调用 [`channel_setup`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__driver__api.html#ae3f53e7374013f2d3e95fd4452b18514) 与 [`write_value`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__driver__api.html#aac048f094c4882fb5f70e554013d00f1) 函数指针。

[`dac_channel_setup_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gadde628b52a3579003f63b2480ac9254b)、[`dac_write_value_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga7ebbb348211b82e84f49f6dad7e28cbf) 和 [`dac_x_to_raw_dt_chan()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga450f0f61564dfc503872a96e6eaac604) 都先判断 [`channel_cfg_dt_node_exists`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__dt__spec.html#a00dde7f3907771edcc07fdc060e9e944)；配置节点不存在时返回 `-ENOTSUP`。[`dac_is_ready_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga85babfb832acef6dc31c1af7d212f8f8) 则同时要求该标志为真和设备就绪（Device Ready）。

## 838.3\_电压转换实现

[`dac_millivolts_to_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gaa266992a47b299804d37d713229eef42) 与 [`dac_microvolts_to_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gacea77754e7d0ae6e244f14b7ab05e086) 使用64位无符号中间值。前者将输入左移 [`resolution`](https://docs.zephyrproject.org/latest/doxygen/html/structdac__channel__cfg.html#a4ba4f6dde3e4525e0a0e71fea5aeaef3) 位后除以以毫伏（Millivolt，mV）计的 `ref_mv`；后者还除以1000，把微伏（Microvolt，µV）输入换算到相同参考单位。整数除法行为按原C表达式保留。

两函数在结果**大于** `(1UL << resolution)` 时执行断言（Assertion） `__ASSERT`，断言消息 `conversion result is out of range` 意为“转换结果超出范围”；该分支随后写有 `return -ERANGE`。检查之后才改写 `*valp`，成功返回0。这里的比较符是原代码的 `>`，没有改成 `>=`，也没有自行增添饱和处理（Saturation）。断言是否中止执行受构建配置影响，不能把这个分支简单理解为所有配置下一定正常返回错误码。

[`dac_x_to_raw_dt_chan()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga450f0f61564dfc503872a96e6eaac604) 将设备树中的参考电压与分辨率传给 `conv_func` 并返回其结果。两个 `_to_raw_dt()` 包装函数（Wrapper）分别传入毫伏和微伏转换函数。接口注释中的方向与返回值矛盾见[对应译注](P822_数模转换器接口.md)。

## 838.4\_网页源码

以下完整保留Doxygen源码页实际展示的代码，剔除网页行号并清理行尾空白；网页隐藏的文档注释由相应中文接口参考提供。版权与许可证保留原文。

```c
/*
 * Copyright (c) 2020 Libre Solar Technologies GmbH
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_DAC_H_
#define ZEPHYR_INCLUDE_DRIVERS_DAC_H_

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


#define DAC_CHANNEL_BROADCAST   0xFF

struct dac_channel_cfg {
        uint8_t channel_id;
        uint8_t resolution;
        bool buffered: 1;
        bool internal: 1;
};

#define DAC_CHANNEL_CFG_DT(node_id) { \
        .channel_id       = DT_REG_ADDR(node_id),                      \
        .resolution       = DT_PROP_OR(node_id, zephyr_resolution, 0), \
        .buffered         = DT_PROP(node_id, zephyr_buffered),         \
        .internal         = DT_PROP(node_id, zephyr_internal),         \
}

struct dac_dt_spec {
        const struct device *dev;

        uint8_t channel_id;

        bool channel_cfg_dt_node_exists;

        struct dac_channel_cfg channel_cfg;

        uint16_t vref_mv;
};


#define DAC_DT_SPEC_STRUCT(ctlr, output) { \
                .dev = DEVICE_DT_GET(ctlr), \
                .channel_id = output, \
                DAC_CHANNEL_CFG_FROM_DT_NODE(\
                        DAC_CHANNEL_DT_NODE(ctlr, output)) \
        }

#define DAC_CHANNEL_DT_NODE(ctlr, output) \
        DT_CHILD_BY_UNIT_ADDR_INT(ctlr, output)

#define DAC_CHANNEL_CFG_FROM_DT_NODE(node_id) \
        IF_ENABLED(DT_NODE_EXISTS(node_id), \
                (.channel_cfg_dt_node_exists = true, \
                 .channel_cfg  = DAC_CHANNEL_CFG_DT(node_id), \
                 .vref_mv      = DT_PROP_OR(node_id, zephyr_vref_mv, 0),))


#define DAC_DT_SPEC_GET_BY_NAME(node_id, name) \
        DAC_DT_SPEC_STRUCT(DT_IO_CHANNELS_CTLR_BY_NAME(node_id, name), \
                           DT_IO_CHANNELS_OUTPUT_BY_NAME(node_id, name))

#define DAC_DT_SPEC_GET_BY_NAME_OR(node_id, name, default_value) \
        COND_CODE_1(DT_PROP_HAS_NAME(node_id, io_channels, name), \
                    (DAC_DT_SPEC_GET_BY_NAME(node_id, name)), (default_value))

#define DAC_DT_SPEC_INST_GET_BY_NAME(inst, name) \
        DAC_DT_SPEC_GET_BY_NAME(DT_DRV_INST(inst), name)


#define DAC_DT_SPEC_INST_GET_BY_NAME_OR(inst, name, default_value) \
        DAC_DT_SPEC_GET_BY_NAME_OR(DT_DRV_INST(inst), name, default_value)

#define DAC_DT_SPEC_GET_BY_IDX(node_id, idx) \
        DAC_DT_SPEC_STRUCT(DT_IO_CHANNELS_CTLR_BY_IDX(node_id, idx), \
                           COND_CODE_1(DT_PHA_HAS_CELL_AT_IDX(node_id, io_channels, idx, output), \
                                       (DT_IO_CHANNELS_OUTPUT_BY_IDX(node_id, idx)), \
                                       (0)))

#define DAC_DT_SPEC_GET_BY_IDX_OR(node_id, idx, default_value) \
        COND_CODE_1(DT_PROP_HAS_IDX(node_id, io_channels, idx), \
                    (DAC_DT_SPEC_GET_BY_IDX(node_id, idx)), (default_value))

#define DAC_DT_SPEC_INST_GET_BY_IDX(inst, idx) \
        DAC_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), idx)

#define DAC_DT_SPEC_INST_GET_BY_IDX_OR(inst, idx, default_value) \
        DAC_DT_SPEC_GET_BY_IDX_OR(DT_DRV_INST(inst), idx, default_value)

#define DAC_DT_SPEC_GET(node_id) DAC_DT_SPEC_GET_BY_IDX(node_id, 0)

#define DAC_DT_SPEC_GET_OR(node_id, default_value) \
        DAC_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)

#define DAC_DT_SPEC_INST_GET(inst) DAC_DT_SPEC_GET(DT_DRV_INST(inst))

#define DAC_DT_SPEC_INST_GET_OR(inst, default_value) \
        DAC_DT_SPEC_GET_OR(DT_DRV_INST(inst), default_value)


typedef int (*dac_api_channel_setup)(const struct device *dev,
                                     const struct dac_channel_cfg *channel_cfg);

typedef int (*dac_api_write_value)(const struct device *dev,
                                    uint8_t channel, uint32_t value);

__subsystem struct dac_driver_api {
        dac_api_channel_setup channel_setup;
        dac_api_write_value   write_value;
};


__syscall int dac_channel_setup(const struct device *dev,
                                const struct dac_channel_cfg *channel_cfg);

static inline int z_impl_dac_channel_setup(const struct device *dev,
                                           const struct dac_channel_cfg *channel_cfg)
{
        return DEVICE_API_GET(dac, dev)->channel_setup(dev, channel_cfg);
}

static inline int dac_channel_setup_dt(const struct dac_dt_spec *spec)
{
        if (!spec->channel_cfg_dt_node_exists) {
                return -ENOTSUP;
        }

        return dac_channel_setup(spec->dev, &spec->channel_cfg);
}

__syscall int dac_write_value(const struct device *dev, uint8_t channel,
                              uint32_t value);

static inline int z_impl_dac_write_value(const struct device *dev,
                                                uint8_t channel, uint32_t value)
{
        return DEVICE_API_GET(dac, dev)->write_value(dev, channel, value);
}

static inline int dac_write_value_dt(const struct dac_dt_spec *spec,
                                     uint32_t value)
{
        if (!spec->channel_cfg_dt_node_exists) {
                return -ENOTSUP;
        }

        return dac_write_value(spec->dev, spec->channel_id, value);
}

typedef int (*dac_x_to_raw_fn)(uint32_t ref_mv, uint8_t resolution, uint32_t *valp);

static inline int dac_millivolts_to_raw(uint32_t ref_mv, uint8_t resolution, uint32_t *valp)
{
        uint64_t dac_mv = (((uint64_t)*valp) << resolution) / (uint64_t)ref_mv;

        if (dac_mv > (1UL << resolution)) {
                __ASSERT(false, "conversion result is out of range");
                return -ERANGE;
        }

        *valp = (uint32_t)dac_mv;

        return 0;
}

static inline int dac_microvolts_to_raw(uint32_t ref_mv, uint8_t resolution, uint32_t *valp)
{
        uint64_t dac_uv = (((uint64_t)*valp) << resolution) / (uint64_t)ref_mv / (uint64_t)1000;

        if (dac_uv > (1UL << resolution)) {
                __ASSERT(false, "conversion result is out of range");
                return -ERANGE;
        }

        *valp = (uint32_t)dac_uv;

        return 0;
}

static inline int dac_x_to_raw_dt_chan(dac_x_to_raw_fn conv_func,
                                            const struct dac_dt_spec *spec,
                                            uint32_t *valp)
{
        if (!spec->channel_cfg_dt_node_exists) {
                return -ENOTSUP;
        }

        return conv_func(spec->vref_mv, spec->channel_cfg.resolution, valp);
}

static inline int dac_millivolts_to_raw_dt(const struct dac_dt_spec *spec, uint32_t *valp)
{
        return dac_x_to_raw_dt_chan(dac_millivolts_to_raw, spec, valp);
}

static inline int dac_microvolts_to_raw_dt(const struct dac_dt_spec *spec, uint32_t *valp)
{
        return dac_x_to_raw_dt_chan(dac_microvolts_to_raw, spec, valp);
}

static inline bool dac_is_ready_dt(const struct dac_dt_spec *spec)
{
        return spec->channel_cfg_dt_node_exists && device_is_ready(spec->dev);
}


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/dac.h>

#endif  /* ZEPHYR_INCLUDE_DRIVERS_DAC_H_ */
```

---

[上一章：DAC主头文件](P837_DAC主头文件.md) · [下一章：STM32模数转换器绑定](P839_STM32模数转换器绑定.md) · [返回大纲](大纲.md)
