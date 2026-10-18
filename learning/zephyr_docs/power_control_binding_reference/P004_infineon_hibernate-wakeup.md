---
id: learning.zephyr-docs.power-control-binding-reference.page-4
title: infineon_hibernate-wakeup
kind: reference
status: maintained
domains: [zephyr, devicetree, power]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/power/infineon,hibernate-wakeup.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第4章\_infineon_hibernate-wakeup

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/power/infineon,hibernate-wakeup.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="infineon-hibernate-wakeup"></a>
<a id="dtbinding-infineon-hibernate-wakeup"></a>
<a id="std-dtcompatible-infineon-hibernate-wakeup"></a>

兼容字符串（Compatible String）：`infineon,hibernate-wakeup`。厂商：[ Infineon Technologies ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-infineon)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,hibernate-wakeup)。

<a id="description"></a>

Infineon休眠／休眠RAM唤醒源配置（Hibernate/Hibernate-RAM Wakeup Source Configuration）。Infineon SoC提供专用硬件源，可从hibernate及支持时的hibernate-RAM电源模式唤醒设备。本绑定描述PIN0、PIN1、LPCOMP0、LPCOMP1、WDT和RTC闹钟这些唤醒源。

引脚到焊盘（Pin-to-pad）的映射由芯片固定，随设备而异，应查SoC数据手册或设备树。设备只使能实际使用的源，只设置适用属性；各引脚及低功耗比较器（Low-power Comparator，LPCOMP）源可独立使能，并配置为高／低逻辑电平唤醒。第一个专用引脚低电平有效的原例见下文。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 4.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `wakeup-pin0-trigger` | `string` | 使能专用唤醒PIN0作为休眠唤醒源。物理焊盘因设备而异，应查SoC设备树／数据手册；low表示低逻辑电平唤醒，high表示高电平唤醒，省略则禁用PIN0；合法值：`low, high` |
| `wakeup-pin1-trigger` | `string` | 使能专用唤醒PIN1作为休眠唤醒源。物理焊盘因设备而异，应查SoC设备树／数据手册；low表示低逻辑电平唤醒，high表示高电平唤醒，省略则禁用PIN1；合法值：`low, high` |
| `wakeup-lpcomp0-trigger` | `string` | 使能低功耗比较器0（LPCOMP0）作为休眠唤醒源。low表示低输出电平唤醒，high表示高电平唤醒，省略则禁用LPCOMP0；合法值：`low, high` |
| `wakeup-lpcomp1-trigger` | `string` | 使能低功耗比较器1（LPCOMP1）作为休眠唤醒源。low表示低输出电平唤醒，high表示高电平唤醒，省略则禁用LPCOMP1；合法值：`low, high` |
| `wakeup-wdt` | `boolean` | 使能看门狗定时器（Watchdog Timer，WDT）作为休眠唤醒源 |
| `wakeup-rtc-alarm` | `boolean` | 使能实时时钟闹钟（RTC Alarm）作为休眠唤醒源 |

本页没有已弃用的节点专用属性。

## 专用唤醒引脚原例

第一个专用引脚低电平有效（Active Low）：

```dts
  hibernate_wakeup: hibernate-wakeup {
      compatible = "infineon,hibernate-wakeup";
      wakeup-pin0-trigger = "low";
  };
```

---

[上一章](P003_infineon_cat1b-power.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_ite_it8xxx2-power-elpm.md)
