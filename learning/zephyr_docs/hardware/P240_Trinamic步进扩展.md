---
id: learning.zephyr-docs.hardware.stepext-3
title: Trinamic步进扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第240章\_Trinamic步进扩展

原文：[group__trinamic__stepper__ctrl](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html)。读取日期：2026-10-13，`latest`。

## 240.1\_范围与版本

本页提供 Trinamic **步进控制器（Stepper Controller）**专用公共 **应用程序编程接口（Application Programming Interface，API）**，自 Zephyr 4.0 提供，本页版本为 0.9.0，头文件为 `zephyr/drivers/stepper/stepper_trinamic.h`。

配套结构为[斜坡发生器参数](P243_Trinamic斜坡发生器参数.md)和[堵转检测设置](P242_Trinamic堵转检测设置.md)。StallGuard 是器件的堵转检测功能名称，保留其英文产品术语。

## 240.2\_从设备树取得斜坡参数

以下宏从 **设备树（Devicetree，DT）**读取 **斜坡发生器（Ramp Generator）**数据，形成结构 [`tmc_ramp_generator_data`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__ramp__generator__data.html) 的初始化内容。

宏 `TMC_RAMP_DT_SPEC_GET_COMMON(node)` 读取通用部分，`node` 为 DT 节点标识符。展开式中的 [`DT_PROP`](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b) 是属性读取宏；`vstart` 至 `tzerowait` 为对应速度、加减速度与等待字段，`iholdrun` 是合并的保持/运行电流字段，完整含义见参数结构页。`TMC5XXX_IRUN`、`TMC5XXX_IHOLD`、`TMC5XXX_IHOLDDELAY` 是组合电流设置所用的辅助宏：

```c
.vstart = DT_PROP(node, vstart),                                \
.v1 = DT_PROP(node, v1),                                        \
.vmax = DT_PROP(node, vmax),                                    \
.a1 = DT_PROP(node, a1),                                        \
.amax = DT_PROP(node, amax),                                    \
.d1 = DT_PROP(node, d1),                                        \
.dmax = DT_PROP(node, dmax),                                    \
.vstop = DT_PROP(node, vstop),                                  \
.tzerowait = DT_PROP(node, tzerowait),                          \
.iholdrun = (TMC5XXX_IRUN(DT_PROP(node, irun)) |                \
             TMC5XXX_IHOLD(DT_PROP(node, ihold)) |              \
             TMC5XXX_IHOLDDELAY(DT_PROP(node, iholddelay))),
```

宏 `TMC_RAMP_DT_SPEC_GET_TMC50XX(node)` 取得 TMC50XX 参数，`node` 同样为 DT 节点标识符；它在通用字段之外加入 `vhigh` 与 `vcoolthrs`：

```c
{                                                                       \
        TMC_RAMP_DT_SPEC_GET_COMMON(node)                               \
        .vhigh = DT_PROP(node, vhigh),                                  \
        .vcoolthrs = DT_PROP(node, vcoolthrs),                          \
}
```

宏 `TMC_RAMP_DT_SPEC_GET_TMC51XX(node)` 取得 TMC51XX 参数，但这里的 `node` 是 **DT 驱动实例编号（Driver Instance Number）**。展开式用 [`DT_DRV_INST`](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1) 转成节点标识，用 [`DT_INST_PROP`](../dt_instance_reference/P001_设备树驱动实例宏.md#ga9dce2e631b2a94804e8f2bcc76c6eff8) 读取实例属性；特有字段为 `tpowerdown`、`tpwmthrs`、`tcoolthrs`、`thigh`：

```c
{                                                                       \
        TMC_RAMP_DT_SPEC_GET_COMMON(DT_DRV_INST(node))                  \
        .tpowerdown = DT_INST_PROP(node, tpowerdown),                   \
        .tpwmthrs = DT_INST_PROP(node, tpwmthrs),                       \
        .tcoolthrs = DT_INST_PROP(node, tcoolthrs),                     \
        .thigh = DT_INST_PROP(node, thigh),                             \
}
```

> 译注：三者参数虽都叫 `node`，前两者接收节点标识符，第三者接收实例编号；调用时应按各自原定义传参。通用宏展开为字段列表，两个器件宏展开为完整初始化器。

## 240.3\_配置斜坡发生器

函数 [`tmc50xx_stepper_ctrl_set_ramp()`](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga27c449d5c0bbacabae333c1356aedfd9) 配置 Trinamic 步进斜坡发生器：

```c
int tmc50xx_stepper_ctrl_set_ramp(const struct device *dev,
                                 const struct tmc_ramp_generator_data *ramp_data);
```

`dev` 指向步进电机控制器实例；`ramp_data` 指向所需斜坡参数的结构。成功返回 0；`-EIO` 表示一般输入输出错误（Input/Output Error）；`-ENOSYS` 表示设备驱动未实现（Not Implemented）。

## 240.4\_设置最大速度

```c
int tmc50xx_stepper_ctrl_set_max_velocity(const struct device *dev, uint32_t velocity);
int tmc51xx_stepper_ctrl_set_max_velocity(const struct device *dev, uint32_t velocity);
```

函数 [`tmc50xx_stepper_ctrl_set_max_velocity()`](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga3c59d8c7e49d3f5959712b23b2df47ac) 与 [`tmc51xx_stepper_ctrl_set_max_velocity()`](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#gaa2534eba96364f813617706a08ea73f7) 分别设置对应系列的步进电机最大速度。`dev` 指向步进驱动实例；`velocity` 是以 **微步/秒（Microsteps per Second）**为单位的最大速度。

两个函数成功均返回 0，`-EIO` 表示一般输入输出错误。

## 240.5\_配置StallGuard

```c
void tmc50xx_stepper_ctrl_configure_stallguard(const struct device *dev,
                                             const struct tmc_stallguard_settings *sg_settings);
void tmc51xx_stepper_ctrl_configure_stallguard(const struct device *dev,
                                             const struct tmc_stallguard_settings *sg_settings);
```

函数 [`tmc50xx_stepper_ctrl_configure_stallguard()`](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga7ef8f93f0301b2437b98eceac43407c7) 与 [`tmc51xx_stepper_ctrl_configure_stallguard()`](https://docs.zephyrproject.org/latest/doxygen/html/group__trinamic__stepper__ctrl.html#ga08b0b69ad4db741165d128cb2b2c3188) 分别配置 TMC50XX 和 TMC51XX 的 StallGuard 设置。

`dev` 指向步进电机控制器实例；`sg_settings` 指向所需 StallGuard 参数结构。两者返回类型均为 `void`，原文没有错误码返回项。

---

[上一章：TMCM3216步进扩展](P239_TMCM3216步进扩展.md) · [下一章：TMCM3216电机状态](P241_TMCM3216电机状态.md) · [返回大纲](大纲.md)
