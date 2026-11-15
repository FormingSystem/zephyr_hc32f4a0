---
id: learning.zephyr-docs.hardware.reginternal-5
title: NXP带隙缓冲器绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/regulator/nxp,spc-bandgap-buffer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第651章\_NXP带隙缓冲器绑定

<a id="dtbinding-nxp-spc-bandgap-buffer"></a>

原文：[nxp,spc-bandgap-buffer](https://docs.zephyrproject.org/latest/build/dts/api/bindings/regulator/nxp,spc-bandgap-buffer.html)。读取日期：2026-10-13，`latest`。

`nxp,spc-bandgap-buffer` 是设备树绑定（Devicetree Binding），描述NXP Semiconductors的SPC模块带缓冲的带隙输出（Buffered Bandgap Output）。SPC为原文中的硬件模块名称。

驱动为 [`drivers/regulator/regulator_nxp_spc_bandgap.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/regulator_nxp_spc_bandgap.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,spc-bandgap-buffer)。

## 651.1\_节点专用属性

本页 `int` 为整数，`string` 为字符串，`boolean` 为布尔属性，`array` 为数值数组，`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明单元数组，`string-array` 为字符串数组。电压的 `microvolt` 单位为微伏（Microvolt，µV），电流的 `microamp` 单位为微安（Microampere，µA），时间的 `us` 单位为微秒（Microsecond，µs），温度的 `kelvin` 单位为开尔文（Kelvin，K）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `regulator-always-on` | `boolean` | 稳压器始终开启，不应被禁用 |
| `regulator-boot-on` | `boolean` | 引导加载器（Bootloader）／固件已启用稳压器，预期引导加载器会让它保持开启。若没有保持开启，操作系统（Operating System，OS）应在启动时打开它，但不应阻止之后关闭。本属性仅用于软件无法读取稳压器状态的设备 |

原页没有列出已弃用的节点专用属性或通用基础属性，也未把上述属性标为必需。



---

[上一章：Infineon自主模拟参考电压绑定](P650_Infineon自主模拟参考电压绑定.md) · [下一章：NXP参考电压绑定](P652_NXP参考电压绑定.md) · [返回大纲](大纲.md)
