---
id: learning.zephyr-docs.api-source-runtime-reference.page-16
title: pcie.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2pcie_2pcie_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_pcie.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2pcie_2pcie_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2pcie_2pcie_8h.html)。

## 16.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
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
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
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
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>

```c
/*
 * Copyright (c) 2019 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PCIE_PCIE_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PCIE_PCIE_H_

/*
 * Set the device's IRQ (in devicetree, or whatever) to PCIE_IRQ_DETECT
 * if the device doesn't support MSI and we don't/can't know the wired IRQ
 * allocated by the firmware ahead of time. Use of this functionality will
 * generally also require CONFIG_DYNAMIC_INTERRUPTS.
 */

#define PCIE_IRQ_DETECT         0xFFFFFFFU

/*
 * We represent a PCI device ID as [31:16] device ID, [15:0] vendor ID. Not
 * coincidentally, this is same representation used in PCI configuration space.
 */

#define PCIE_ID_VEND_SHIFT      0U
#define PCIE_ID_VEND_MASK       0xFFFFU
#define PCIE_ID_DEV_SHIFT       16U
#define PCIE_ID_DEV_MASK                0xFFFFU

#ifdef __DTS__
#define CAST(type, v) (v)
#else
#define CAST(type, v) ((type)(v))
#endif

#define PCIE_ID(vend, dev) \
        ((((vend) & PCIE_ID_VEND_MASK) << PCIE_ID_VEND_SHIFT) | \
         (CAST(uint32_t, (dev) & PCIE_ID_DEV_MASK) << PCIE_ID_DEV_SHIFT))

#define PCIE_ID_TO_VEND(id) (((id) >> PCIE_ID_VEND_SHIFT) & PCIE_ID_VEND_MASK)
#define PCIE_ID_TO_DEV(id)  (((id) >> PCIE_ID_DEV_SHIFT) & PCIE_ID_DEV_MASK)

#define PCIE_ID_NONE PCIE_ID(0xFFFF, 0xFFFF)

#define PCIE_BDF_NONE 0xFFFFFFFFU

/*
 * Since our internal representation of bus/device/function is arbitrary,
 * we choose the same format employed in the x86 Configuration Address Port:
 *
 * [23:16] bus number, [15:11] device number, [10:8] function number
 *
 * All other bits must be zero.
 *
 * The x86 (the only arch, at present, that supports PCI) takes advantage
 * of this shared format to avoid unnecessary layers of abstraction.
 */

#define PCIE_BDF_BUS_SHIFT      16U
#define PCIE_BDF_BUS_MASK       0xFFU
#define PCIE_BDF_DEV_SHIFT      11U
#define PCIE_BDF_DEV_MASK       0x1FU
#define PCIE_BDF_FUNC_SHIFT     8U
#define PCIE_BDF_FUNC_MASK      0x7U

#define PCIE_BDF(bus, dev, func) \
        ((((bus) & PCIE_BDF_BUS_MASK) << PCIE_BDF_BUS_SHIFT) | \
         (((dev) & PCIE_BDF_DEV_MASK) << PCIE_BDF_DEV_SHIFT) | \
         (((func) & PCIE_BDF_FUNC_MASK) << PCIE_BDF_FUNC_SHIFT))

#define PCIE_BDF_TO_BUS(bdf) (((bdf) >> PCIE_BDF_BUS_SHIFT) & PCIE_BDF_BUS_MASK)
#define PCIE_BDF_TO_DEV(bdf) (((bdf) >> PCIE_BDF_DEV_SHIFT) & PCIE_BDF_DEV_MASK)

#define PCIE_BDF_TO_FUNC(bdf) \
        (((bdf) >> PCIE_BDF_FUNC_SHIFT) & PCIE_BDF_FUNC_MASK)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PCIE_PCIE_H_ */
```

## 16.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

如果设备不支持消息信号中断（MSI），且无法提前获知固件分配的有线中断（Wired IRQ），应将设备的 IRQ（在设备树或其他配置中）设为 `PCIE_IRQ_DETECT`。使用此功能通常还需要 `CONFIG_DYNAMIC_INTERRUPTS`。

### 注释 3：原第 19 行

PCI 设备标识符的表示方式为：`[31:16]` 保存设备 ID，`[15:0]` 保存厂商 ID。这与 PCI 配置空间中的表示方式相同，是有意为之。

### 注释 4：原第 46 行

总线/设备/功能号的内部表示可以自行选择，因此采用与 x86 配置地址端口（Configuration Address Port）相同的格式：

- `[23:16]`：总线编号。
- `[15:11]`：设备编号。
- `[10:8]`：功能编号。

其他所有位必须为零。x86 利用这种共同格式避免不必要的抽象层。原注释将 x86 描述为“目前唯一支持 PCI 的架构”，此处保留这一原文表述，不将其扩展为当前 Zephyr 平台支持结论。

### 注释 5：原第 76 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PCIE_PCIE_H_`。

## 16.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2pcie_2pcie_8h.html)

---

[上一章](P015_dsa_tag.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P017_esp32-touch-sensor-input.h_源码浏览.md)
