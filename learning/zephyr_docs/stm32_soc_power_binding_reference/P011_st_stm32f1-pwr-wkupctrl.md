---
id: learning.zephyr-docs.stm32-soc-power-binding-reference.page-11
title: st_stm32f1-pwr-wkupctrl
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/power/st,stm32f1-pwr-wkupctrl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第11章\_st_stm32f1-pwr-wkupctrl

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/power/st,stm32f1-pwr-wkupctrl.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="st-stm32f1-pwr-wkupctrl"></a>
<a id="dtbinding-st-stm32f1-pwr-wkupctrl"></a>
<a id="std-dtcompatible-st-stm32f1-pwr-wkupctrl"></a>

兼容字符串（Compatible String）：`st,stm32f1-pwr-wkupctrl`。厂商：[ STMicroelectronics ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-st)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=st,stm32f1-pwr-wkupctrl)。

<a id="description"></a>

STM32F1类唤醒引脚控制器（Wake-up Pins Controller），适用于STM32F1及其他系列中的此类控制逻辑。

STM32F1等系列将引脚使能为唤醒引脚时，会强制配置为输入下拉（Input Pull-down）模式，唤醒极性固定为上升沿检测（Rising Edge Detection）。其他一些系列可以通过软件任意配置上拉／下拉（PU/PD）及极性，此处不具备这种能力。

本绑定使用“唤醒引脚”而不是“唤醒线路”，因为这些系列的每条唤醒线路都硬连接到特定GPIO引脚，不能选择其他信号源。

<a id="examples"></a>

## 唤醒控制器原例

官方给出以下共享绑定示例。STM32WBA的线路1可由源0的PA0或源1的PB2触发；线路2仅接PC13，但flags仍须指定对应的STM32_PWR_WKUP_EVT_SRC_n。

```dts
/* Example: STM32WBA series */
power@46020800 {
  /* ...PWR properties omitted for brevity... */

  wakeup-controller {
    compatible = "st,stm32-pwr-wkupctrl";
    #address-cells = <1>;
    #size-cells = <0>;

    st,max-wkup-line-idx = <8>;
    st,has-multi-source-lines;

    wkup@1 {
      /*
       * Wake-up line 1, triggerable by two different GPIOs:
       *  - source 0: PA0
       *  - source 1: PB2
       */
      reg = <0x1>;
      wkup-gpios = <&gpioa 0 STM32_PWR_WKUP_EVT_SRC_0>,
                   <&gpiob 2 STM32_PWR_WKUP_EVT_SRC_1>;
    };

    wkup@2 {
      /*
       * Wake-up line 2, triggerable by only one GPIO: PC13.
       * Regardless, the appropriate `STM32_PWR_WKUP_EVT_SRC_n`
       * value must still be set in the `flags` cell.
       */
      reg = <0x2>;
      wkup-gpios = <&gpioc 13 STM32_PWR_WKUP_EVT_SRC_1>;
    };

    /* ...other lines omitted for brevity... */
  };
};
```

STM32F1示例不设置st,has-multi-source-lines，并用STM32_PWR_WKUP_PIN_NOT_MUXED表示硬连接。

```dts
/* Example: STM32F1 series */
pwr: power@40007000 {
  /* ...PWR properties omitted for brevity... */

  wakeup-controller {
    compatible = "st,stm32f1-pwr-wkupctrl", "st,stm32-pwr-wkupctrl";
    #address-cells = <1>;
    #size-cells = <0>;

    st,max-wkup-line-idx = <1>;
    /* Note the absence of `st,has-multi-source-lines` property... */

    wkup@1 {
      /* ...and use of the `STM32_PWR_WKUP_PIN_NOT_MUXED` value. */
      reg = <0x1>;
      wkup-gpios = <&gpioa 0 STM32_PWR_WKUP_PIN_NOT_MUXED>;
    };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 11.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `st,max-wkup-line-idx` | `int` | **必需**。SoC支持的最高唤醒线路WKUPn的索引。只统计连接到GPIO引脚、通常命名为WKUPn的线路，忽略仅连接内部信号源的线路。例如最高的GPIO连接线路为WKUP8时，应设为8 |
| `st,has-pwr-full-pupd` | `boolean` | 存在时，表示PWR能管理SoC全部GPIO引脚的内部上拉／下拉（Pull-up/Pull-down）电阻。判断依据是PWR寄存器映射中，每个GPIO端口都有一对PWR_PUCRx／PWR_PDCRx寄存器，x为A、B、C等。若某系列只有部分GPIO端口具备这些寄存器，**不得设置此属性** |

本页没有已弃用的节点专用属性。

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。唤醒线路索引（Wake-up Line Index） |
| `wkup-gpios` | `phandle-array` | 指定可触发此唤醒线路的GPIO引脚。每个条目的flags单元有特殊含义：父节点存在st,has-multi-source-lines时，它标识此GPIO对应的线路唤醒源（STM32_PWR_WKUP_EVT_SRC_n）；否则必须设为STM32_PWR_WKUP_PIN_NOT_MUXED，表示唤醒源由硬件固定连接。详情参见 `include/zephyr/dt-bindings/power/stm32_pwr.h`，不同用法见原例 |

---

[上一章](P010_st_stm32-pwr.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_st_stm32f7-pwr-wkupctrl.md)
