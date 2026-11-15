---
id: learning.zephyr-docs.hardware.dacmain-0
title: DAC主头文件
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dac_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第837章\_DAC主头文件

原文：[dac_8h](https://docs.zephyrproject.org/latest/doxygen/html/dac_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/dac.h` 是数模转换器（Digital-to-Analog Converter，DAC）驱动应用程序接口（Application Programming Interface，API）的主头文件。原页列出的包含项为：

```c
#include <zephyr/device.h>
#include <zephyr/syscalls/dac.h>
```

前者提供设备接口，后者提供DAC系统调用（System Call）相关声明。[源码页](P838_DAC主头文件源码.md)保留可见实现；参数、返回值及完整用例见[DAC接口](P822_数模转换器接口.md)。

## 837.1\_数据结构

| 结构 | 用途 |
| --- | --- |
| `struct dac_channel_cfg` | 指定DAC通道配置（Channel Configuration），见[字段参考](P825_DAC通道配置结构.md) |
| `struct dac_dt_spec` | 保存设备树（Devicetree）指定的DAC通道信息，见[字段参考](P826_DAC设备树规格结构.md) |
| `struct dac_driver_api` | DAC驱动操作（Driver Operations）结构，见[驱动接口结构](P827_DAC驱动接口结构.md) |

## 837.2\_设备树与广播宏

下表保留原页全部14个宏。节点参数 `node_id` 是设备树节点标识符（Node Identifier）；`name` 为通道名称，`idx` 为属性中的通道索引，`inst` 为 `DT_DRV_COMPAT` 对应的实例编号，`default_value` 为回退值（Fallback Value）。

| 宏及参数 | 中文说明 |
| --- | --- |
| [`DAC_CHANNEL_BROADCAST`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gabeb2cf325aec36624a013ee91a377b35) | 编码 `0xFF`，供支持广播（Broadcast）的DAC使用的通道标识 |
| `DAC_CHANNEL_CFG_DT(node_id)` | 从指定设备树节点获取DAC通道配置 |
| `DAC_DT_SPEC_GET_BY_NAME(node_id, name)` | 按名称从设备树取得DAC输入输出通道（I/O Channel）信息 |
| `DAC_DT_SPEC_GET_BY_NAME_OR(node_id, name, default_value)` | 按名称获取，增加默认回退值 |
| `DAC_DT_SPEC_INST_GET_BY_NAME(inst, name)` | 从 `DT_DRV_COMPAT` 对应的设备树实例按名称获取通道信息 |
| `DAC_DT_SPEC_INST_GET_BY_NAME_OR(inst, name, default_value)` | 按实例及名称获取，增加默认回退值 |
| `DAC_DT_SPEC_GET_BY_IDX(node_id, idx)` | 按索引从设备树获取通道信息 |
| `DAC_DT_SPEC_GET_BY_IDX_OR(node_id, idx, default_value)` | 按索引获取，增加默认回退值 |
| `DAC_DT_SPEC_INST_GET_BY_IDX(inst, idx)` | 从 `DT_DRV_COMPAT` 对应的设备树实例按索引获取通道信息 |
| `DAC_DT_SPEC_INST_GET_BY_IDX_OR(inst, idx, default_value)` | 按实例及索引获取，增加默认回退值 |
| `DAC_DT_SPEC_GET(node_id)` | 等价于 `DAC_DT_SPEC_GET_BY_IDX(node_id, 0)` |
| `DAC_DT_SPEC_GET_OR(node_id, default_value)` | 等价于 `DAC_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)` |
| `DAC_DT_SPEC_INST_GET(inst)` | 等价于 `DAC_DT_SPEC_INST_GET_BY_IDX(inst, 0)` |
| `DAC_DT_SPEC_INST_GET_OR(inst, default_value)` | 原摘要写为等价于 `DAC_DT_SPEC_INST_GET_BY_IDX_OR(inst, 0, default)`；实际回退参数名为 `default_value` |

最后一项的参数名矛盾已在[接口译注](P822_数模转换器接口.md)中说明。广播标识只用于写接口，配置和获取宏的约束也见该接口页。

## 837.3\_函数指针类型

```c
typedef int (*dac_api_channel_setup)(const struct device *dev,
                                     const struct dac_channel_cfg *channel_cfg);
typedef int (*dac_api_write_value)(const struct device *dev,
                                   uint8_t channel, uint32_t value);
typedef int (*dac_x_to_raw_fn)(uint32_t ref_mv, uint8_t resolution,
                              uint32_t *valp);
```

[`dac_api_channel_setup`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface__backend.html#ga48651a0355b893551661297cb2d5e483) 定义通道配置函数类型；[`dac_api_write_value`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface__backend.html#gacde710d856a65d8961c339fc8b7a41a3) 定义设置写请求的函数类型，均用于[驱动实现接口](P823_DAC驱动实现接口.md)。[`dac_x_to_raw_fn`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga227ead59c9e4ea4b43b69b2bdd5af6c9) 定义从指定输入单位转换为DAC原始码值（Raw DAC Value）的函数类型。

## 837.4\_通道操作与就绪检查

```c
int dac_channel_setup(const struct device *dev,
                      const struct dac_channel_cfg *channel_cfg);
static inline int dac_channel_setup_dt(const struct dac_dt_spec *spec);
int dac_write_value(const struct device *dev, uint8_t channel, uint32_t value);
static inline int dac_write_value_dt(const struct dac_dt_spec *spec,
                                     uint32_t value);
static inline bool dac_is_ready_dt(const struct dac_dt_spec *spec);
```

[`dac_channel_setup()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gab8be77003ba8fd7225c0808f95602a56) 配置DAC通道，[`dac_channel_setup_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gadde628b52a3579003f63b2480ac9254b) 使用设备树规格结构完成配置。[`dac_write_value()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga437a6f6b2402cf2e2a2a689429663b4e) 向通道写入单个值，[`dac_write_value_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga7ebbb348211b82e84f49f6dad7e28cbf) 根据设备树规格写入单值。[`dac_is_ready_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga85babfb832acef6dc31c1af7d212f8f8) 验证DAC设备是否就绪（Ready）。

## 837.5\_电压转换函数

```c
static inline int dac_millivolts_to_raw(uint32_t ref_mv, uint8_t resolution,
                                       uint32_t *valp);
static inline int dac_microvolts_to_raw(uint32_t ref_mv, uint8_t resolution,
                                       uint32_t *valp);
static inline int dac_x_to_raw_dt_chan(dac_x_to_raw_fn conv_func,
                                       const struct dac_dt_spec *spec,
                                       uint32_t *valp);
static inline int dac_millivolts_to_raw_dt(const struct dac_dt_spec *spec,
                                          uint32_t *valp);
static inline int dac_microvolts_to_raw_dt(const struct dac_dt_spec *spec,
                                          uint32_t *valp);
```

[`dac_millivolts_to_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gaa266992a47b299804d37d713229eef42) 将毫伏（Millivolt，mV）换算为原始码值，[`dac_microvolts_to_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#gacea77754e7d0ae6e244f14b7ab05e086) 将微伏（Microvolt，µV）换算为原始码值。对应的两个 `_dt` 函数使用 `struct dac_dt_spec` 中保存的信息完成换算。

[`dac_x_to_raw_dt_chan()`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga450f0f61564dfc503872a96e6eaac604) 的原摘要写为“将DAC原始值转换为任意输出单位”。**译注：实际实现向 `conv_func` 提供参考电压、分辨率和输入值，转换方向由 [`dac_x_to_raw_fn`](https://docs.zephyrproject.org/latest/doxygen/html/group__dac__interface.html#ga227ead59c9e4ea4b43b69b2bdd5af6c9) 定义为物理电压到原始码值。**原摘要方向与实现不一致，详见[接口说明与译注](P822_数模转换器接口.md)。

---

[上一章：SiliconLabsVDAC常量源码](P836_SiliconLabsVDAC常量源码.md) · [下一章：DAC主头文件源码](P838_DAC主头文件源码.md) · [返回大纲](大纲.md)
