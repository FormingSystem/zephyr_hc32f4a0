---
id: learning.zephyr-docs.api-source-reference.page-715
title: riscv_aia.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第715章\_riscv\_aia.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html)。

## 715.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__device__model_html_gaadf3ffb63df544eb3de356ab2c5e9e3c"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="ariscv__aia_8h_html_a05cb2cf3fbed778d8fb0f535486155ac"></a>
<a id="ariscv__aia_8h_html_a1405f722d840cbc803a7edbcc1c4c5c7"></a>
<a id="ariscv__aia_8h_html_a33533234d1b70b765c602c9416b8daee"></a>
<a id="ariscv__aia_8h_html_a3598cc5edfbd910b8cb01ffc76c8a17f"></a>
<a id="ariscv__aia_8h_html_a6d06861210dacb74fece7b13699b7327"></a>
<a id="ariscv__aia_8h_html_a778cbf67ab1c36d92a72f72599e99056"></a>
<a id="ariscv__aia_8h_html_a883c641c0c4f933f9956cca1dd058052"></a>
<a id="ariscv__aia_8h_html_abf2922519b5ec25a57ded7544c2a401c"></a>
<a id="ariscv__aia_8h_html_ac1c545848a8101e24b515a25ba76f65d"></a>
<a id="ariscv__aia_8h_html_ac58c781ce90f600f827ff7edc710dc98"></a>
<a id="ariscv__aplic_8h_html"></a>
<a id="ariscv__imsic_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_AIA_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_RISCV_AIA_H_

#include <zephyr/device.h>
#include <zephyr/types.h>
#include <zephyr/drivers/interrupt_controller/riscv_aplic.h>
#include <zephyr/drivers/interrupt_controller/riscv_imsic.h>

void riscv_aia_irq_enable(uint32_t irq);

void riscv_aia_irq_disable(uint32_t irq);

int riscv_aia_irq_is_enabled(uint32_t irq);

void riscv_aia_set_priority(uint32_t irq, uint32_t prio);

static inline const struct device *riscv_aia_get_dev(void)
{
        return DEVICE_DT_GET_ANY(riscv_aplic);
}

void riscv_aia_config_source(uint32_t irq, uint32_t mode);

#if defined(CONFIG_RISCV_APLIC_MSI) || defined(__DOXYGEN__)
void riscv_aia_route_to_hart(uint32_t irq, uint32_t hart, uint32_t eiid);

void riscv_aia_inject_msi(uint32_t hart, uint32_t eiid);
#endif /* CONFIG_RISCV_APLIC_MSI */

#if defined(CONFIG_RISCV_APLIC_DIRECT_IRQ_AFFINITY)
void riscv_aia_route_to_hart(uint32_t irq, uint32_t hart);
#endif /* CONFIG_RISCV_APLIC_DIRECT_IRQ_AFFINITY */

void riscv_aia_enable_source(uint32_t irq);

void riscv_aia_dispatch_eiid(uint32_t eiid);

#endif
```

## 715.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 98 行

条件编译配置（Configuration）标记：`CONFIG_RISCV_APLIC_MSI`。

### 注释 3：原第 108 行

条件编译配置（Configuration）标记：`CONFIG_RISCV_APLIC_DIRECT_IRQ_AFFINITY`。

## 715.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/drivers/interrupt_controller/riscv_aplic.h](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html)
- [zephyr/drivers/interrupt_controller/riscv_imsic.h](https://docs.zephyrproject.org/latest/doxygen/html/riscv__imsic_8h.html)
- [riscv_aia_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html#abf2922519b5ec25a57ded7544c2a401c)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [riscv_aia_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html#a3598cc5edfbd910b8cb01ffc76c8a17f)
- [riscv_aia_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html#ac1c545848a8101e24b515a25ba76f65d)
- [riscv_aia_set_priority](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html#a6d06861210dacb74fece7b13699b7327)
- [device](../device_reference/P002_设备对象结构.md)
- [riscv_aia_get_dev](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html#a05cb2cf3fbed778d8fb0f535486155ac)
- [DEVICE_DT_GET_ANY](../device_reference/P001_设备模型公共接口.md#gaadf3ffb63df544eb3de356ab2c5e9e3c)
- [riscv_aia_config_source](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html#a883c641c0c4f933f9956cca1dd058052)
- [riscv_aia_route_to_hart](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html#a778cbf67ab1c36d92a72f72599e99056)
- [riscv_aia_inject_msi](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html#a33533234d1b70b765c602c9416b8daee)
- [riscv_aia_enable_source](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html#ac58c781ce90f600f827ff7edc710dc98)
- [riscv_aia_dispatch_eiid](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aia_8h.html#a1405f722d840cbc803a7edbcc1c4c5c7)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [riscv_aplic.h](https://docs.zephyrproject.org/latest/doxygen/html/riscv__aplic_8h.html)
- [riscv_imsic.h](https://docs.zephyrproject.org/latest/doxygen/html/riscv__imsic_8h.html)

---

[上一章](P714_renesas_rza2m_dma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P716_riscv_aplic.h_源码浏览.md)
