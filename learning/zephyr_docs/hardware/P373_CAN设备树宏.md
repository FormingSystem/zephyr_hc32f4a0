---
id: learning.zephyr-docs.hardware.candt-0
title: CAN设备树宏
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-can.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第373章\_CAN设备树宏

原文：[group__devicetree-can](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-can.html)。读取日期：2026-10-13，`latest`。

## 373.1\_控制器与收发器共同限制速率

本页宏来自 `zephyr/devicetree/can.h`，从设备树（Devicetree）取得控制器局域网（Controller Area Network，CAN）控制器关联收发器（Transceiver）的比特率（Bitrate）范围。

最终上限不能超过控制器上限，最终下限不能低于控制器下限。设备树中没有 CAN 收发器时，分别采用控制器自身的上限、下限。

节点可通过 `phys` 引用独立收发器节点，也可使用 `can-transceiver` 子节点。[`DT_NODE_HAS_PROP`](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692) 检查属性，[`DT_PHANDLE`](../dt_property_reference/P001_设备树属性读取宏.md#ga7bd77c49472ba4547d87f00f40fd7171) 跟随节点引用，[`DT_CHILD`](../dt_identity_reference/P001_设备树节点标识宏.md#ga88259608f4e9083ccc2e9ca5ec2c212e) 取得子节点，[`DT_PROP`](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b) 读取属性，[`DT_PROP_OR`](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f) 在属性不存在时使用默认值。[`COND_CODE_1`](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20) 选择条件分支，[`MIN`](../util_reference/P001_通用工具公共接口.md#ga3acffbd305ee72dcd4593c0d8af64a4f) 与 [`MAX`](../util_reference/P001_通用工具公共接口.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f) 取较小值和较大值。

## 373.2\_计算最高比特率

<a id="ga9c56ded2142fbd8a4a7facffd3dd549d"></a>

`DT_CAN_TRANSCEIVER_MAX_BITRATE(node_id, max)` 的 `node_id` 是控制器节点标识符，[`max`](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f) 是控制器支持的最高速率；返回控制器/收发器组合支持的最高速率。原展开式为：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node_id, phys),                                    \
            MIN(DT_PROP(DT_PHANDLE(node_id, phys), max_bitrate), max),          \
            MIN(DT_PROP_OR(DT_CHILD(node_id, can_transceiver), max_bitrate, max), max))
```

原设备树示例同时演示独立收发器节点和控制器内的收发器子节点；其中 `...` 是片段省略标记：

```dts
transceiver0: can-phy0 {
        compatible = "vnd,can-transceiver";
        max-bitrate = <1000000>;
        #phy-cells = <0>;
};

can0: can@... {
        compatible = "vnd,can-controller";
        phys = <&transceiver0>;
};

can1: can@... {
        compatible = "vnd,can-controller";

        can-transceiver {
                max-bitrate = <2000000>;
        };
};
```

`DT_NODELABEL` 按标签选取节点。以下三次调用分别得到 1 Mbit/s、2 Mbit/s，以及受控制器自身限制的 1 Mbit/s：

```c
DT_CAN_TRANSCEIVER_MAX_BITRATE(DT_NODELABEL(can0), 5000000) // 1000000
DT_CAN_TRANSCEIVER_MAX_BITRATE(DT_NODELABEL(can1), 5000000) // 2000000
DT_CAN_TRANSCEIVER_MAX_BITRATE(DT_NODELABEL(can1), 1000000) // 1000000
```

## 373.3\_计算最低比特率

<a id="ga60cb3dc5c2feb517dddcb5a57cce8a9b"></a>

`DT_CAN_TRANSCEIVER_MIN_BITRATE(node_id, min)` 的 [`min`](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d) 是控制器支持的最低速率，返回控制器/收发器组合支持的最低速率。其展开式为：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node_id, phys),                                    \
            MAX(DT_PROP_OR(DT_PHANDLE(node_id, phys), min_bitrate, 0), min),    \
            MAX(DT_PROP_OR(DT_CHILD(node_id, can_transceiver), min_bitrate, min), min))
```

原设备树给出三种情况：引用的收发器指定最低速率、子节点指定最低速率，以及子节点没有指定最低速率：

```dts
transceiver0: can-phy0 {
        compatible = "vnd,can-transceiver";
        min-bitrate = <15000>;
        max-bitrate = <1000000>;
        #phy-cells = <0>;
};

can0: can@... {
        compatible = "vnd,can-controller";
        phys = <&transceiver0>;
};

can1: can@... {
        compatible = "vnd,can-controller";

        can-transceiver {
                min-bitrate = <25000>;
                max-bitrate = <2000000>;
        };
};

can2: can@... {
        compatible = "vnd,can-controller";

        can-transceiver {
                max-bitrate = <2000000>;
        };
};
```

官方调用示例按原样保留：

```c
DT_CAN_TRANSCEIVER_MIN_BITRATE(DT_NODELABEL(can0), 10000) // 15000
DT_CAN_TRANSCEIVER_MIN_BITRATE(DT_NODELABEL(can1), 0)     // 250000
DT_CAN_TRANSCEIVER_MIN_BITRATE(DT_NODELABEL(can1), 50000) // 500000
DT_CAN_TRANSCEIVER_MIN_BITRATE(DT_NODELABEL(can2), 0)     // 0
```

> 译注：原示例第二、三行的结果注释分别写成 `250000`、`500000`，多了一个零。依据示例属性 `min-bitrate = <25000>` 和宏取 [`MAX`](../util_reference/P001_通用工具公共接口.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f) 的展开式，实际应分别为 `25000`、`50000`。第一行 `15000` 和第四行 `0` 与展开式一致。

## 373.4\_驱动实例版本

<a id="gacac28e33d8a749518485c687a563763f"></a>

`DT_INST_CAN_TRANSCEIVER_MAX_BITRATE(inst, max)` 按 `DT_DRV_COMPAT` 对应实例编号查询最高速率；[`max`](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f) 为控制器上限，返回组合上限。[`DT_DRV_INST`](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1) 将实例编号转换为节点标识符：

```c
DT_CAN_TRANSCEIVER_MAX_BITRATE(DT_DRV_INST(inst), max)
```

<a id="ga5c0b8011b5ec85dd8772f33572ae2b71"></a>

`DT_INST_CAN_TRANSCEIVER_MIN_BITRATE(inst, min)` 同样按实例查询最低速率，[`min`](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d) 为控制器下限，返回组合下限：

```c
DT_CAN_TRANSCEIVER_MIN_BITRATE(DT_DRV_INST(inst), min)
```

---

[上一章：CAN驱动公共数据](P372_CAN驱动公共数据.md) · [下一章：伪CAN控制器接口](P374_伪CAN控制器接口.md) · [返回大纲](大纲.md)
