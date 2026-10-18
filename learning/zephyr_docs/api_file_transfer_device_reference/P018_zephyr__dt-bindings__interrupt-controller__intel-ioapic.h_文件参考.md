---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-18
title: zephyr__dt-bindings__interrupt-controller__intel-ioapic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intel-ioapic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_dt-bindings\_\_interrupt-controller\_\_intel-ioapic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/intel-ioapic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Intel输入输出高级可编程中断控制器（I/O APIC）的设备树宏。

查看此文件的源码。

<a id="details"></a>

Intel输入输出高级可编程中断控制器（I/O APIC）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.1\_宏定义（Macros）

<a id="r_ga296e915831223a614a6ea87dbe7735e7"></a>

```c
#define IRQ_TYPE_LEVEL 0x00008000
```

相关声明：[IRQ_TYPE_LEVEL](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga296e915831223a614a6ea87dbe7735e7)。

电平触发中断（Level-Triggered Interrupt）。

<a id="r_gaff68b0efbc719bc28f0d56c9ba8607bc"></a>

```c
#define IRQ_TYPE_EDGE 0x00000000
```

相关声明：[IRQ_TYPE_EDGE](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaff68b0efbc719bc28f0d56c9ba8607bc)。

边沿触发中断（Edge-Triggered Interrupt）。

<a id="r_ga76dfa18a4a8be7f8b930115b7a9ffc93"></a>

```c
#define IRQ_TYPE_LOW 0x00002000
```

相关声明：[IRQ_TYPE_LOW](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga76dfa18a4a8be7f8b930115b7a9ffc93)。

低电平有效极性（Active-low Polarity）。

<a id="r_gaeb89171ec61787d7a3ced80b30af4359"></a>

```c
#define IRQ_TYPE_HIGH 0x00000000
```

相关声明：[IRQ_TYPE_HIGH](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaeb89171ec61787d7a3ced80b30af4359)。

高电平有效极性（Active-high Polarity）。

<a id="r_ga0c6b1b5a78c465e429a9a5633601d231"></a>

```c
#define IRQ_DELIVERY_LOWEST 0x00000100
```

相关声明：[IRQ_DELIVERY_LOWEST](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga0c6b1b5a78c465e429a9a5633601d231)。

最低优先级投递模式（Lowest-priority Delivery Mode）。

<a id="r_ga19034e9b2fe534947855ad074cd5962b"></a>

```c
#define IRQ_DELIVERY_FIXED 0x00000000
```

相关声明：[IRQ_DELIVERY_FIXED](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga19034e9b2fe534947855ad074cd5962b)。

固定投递模式（Fixed Delivery Mode），适用于所有 CPU。

<a id="r_ga980bab4b0502b138f5fa8af9ca9833b4"></a>

```c
#define IRQ_TYPE_LOWEST_EDGE_RISING (IRQ_DELIVERY_LOWEST | IRQ_TYPE_EDGE | IRQ_TYPE_HIGH)
```

相关声明：[IRQ_TYPE_LOWEST_EDGE_RISING](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga980bab4b0502b138f5fa8af9ca9833b4)、[IRQ_DELIVERY_LOWEST](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga0c6b1b5a78c465e429a9a5633601d231)、[IRQ_TYPE_EDGE](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaff68b0efbc719bc28f0d56c9ba8607bc)、[IRQ_TYPE_HIGH](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaeb89171ec61787d7a3ced80b30af4359)。

最低优先级投递（Lowest-priority Delivery），边沿触发，上升沿。

<a id="r_ga5a136f30dc5cb9f1b696751903b3fadd"></a>

```c
#define IRQ_TYPE_LOWEST_EDGE_FALLING (IRQ_DELIVERY_LOWEST | IRQ_TYPE_EDGE | IRQ_TYPE_LOW)
```

相关声明：[IRQ_TYPE_LOWEST_EDGE_FALLING](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga5a136f30dc5cb9f1b696751903b3fadd)、[IRQ_DELIVERY_LOWEST](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga0c6b1b5a78c465e429a9a5633601d231)、[IRQ_TYPE_EDGE](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaff68b0efbc719bc28f0d56c9ba8607bc)、[IRQ_TYPE_LOW](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga76dfa18a4a8be7f8b930115b7a9ffc93)。

最低优先级投递（Lowest-priority Delivery），边沿触发，下降沿。

<a id="r_ga9083a377fa943731dc24733933bae5d6"></a>

```c
#define IRQ_TYPE_LOWEST_LEVEL_HIGH (IRQ_DELIVERY_LOWEST | IRQ_TYPE_LEVEL | IRQ_TYPE_HIGH)
```

相关声明：[IRQ_TYPE_LOWEST_LEVEL_HIGH](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga9083a377fa943731dc24733933bae5d6)、[IRQ_DELIVERY_LOWEST](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga0c6b1b5a78c465e429a9a5633601d231)、[IRQ_TYPE_LEVEL](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga296e915831223a614a6ea87dbe7735e7)、[IRQ_TYPE_HIGH](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaeb89171ec61787d7a3ced80b30af4359)。

最低优先级投递（Lowest-priority Delivery），电平触发，高电平有效。

<a id="r_ga15c26d56a818f5340c36117a429282a8"></a>

```c
#define IRQ_TYPE_LOWEST_LEVEL_LOW (IRQ_DELIVERY_LOWEST | IRQ_TYPE_LEVEL | IRQ_TYPE_LOW)
```

相关声明：[IRQ_TYPE_LOWEST_LEVEL_LOW](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga15c26d56a818f5340c36117a429282a8)、[IRQ_DELIVERY_LOWEST](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga0c6b1b5a78c465e429a9a5633601d231)、[IRQ_TYPE_LEVEL](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga296e915831223a614a6ea87dbe7735e7)、[IRQ_TYPE_LOW](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga76dfa18a4a8be7f8b930115b7a9ffc93)。

最低优先级投递（Lowest-priority Delivery），电平触发，低电平有效。

<a id="r_gaf1a9700940385a6aa6c9ff93fa834436"></a>

```c
#define IRQ_TYPE_FIXED_EDGE_RISING (IRQ_DELIVERY_FIXED | IRQ_TYPE_EDGE | IRQ_TYPE_HIGH)
```

相关声明：[IRQ_TYPE_FIXED_EDGE_RISING](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaf1a9700940385a6aa6c9ff93fa834436)、[IRQ_DELIVERY_FIXED](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga19034e9b2fe534947855ad074cd5962b)、[IRQ_TYPE_EDGE](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaff68b0efbc719bc28f0d56c9ba8607bc)、[IRQ_TYPE_HIGH](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaeb89171ec61787d7a3ced80b30af4359)。

固定投递（Fixed Delivery），边沿触发，上升沿。

<a id="r_ga7f62c57495f357ec336cba12f1a12d61"></a>

```c
#define IRQ_TYPE_FIXED_EDGE_FALLING (IRQ_DELIVERY_FIXED | IRQ_TYPE_EDGE | IRQ_TYPE_LOW)
```

相关声明：[IRQ_TYPE_FIXED_EDGE_FALLING](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga7f62c57495f357ec336cba12f1a12d61)、[IRQ_DELIVERY_FIXED](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga19034e9b2fe534947855ad074cd5962b)、[IRQ_TYPE_EDGE](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaff68b0efbc719bc28f0d56c9ba8607bc)、[IRQ_TYPE_LOW](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga76dfa18a4a8be7f8b930115b7a9ffc93)。

固定投递（Fixed Delivery），边沿触发，下降沿。

<a id="r_ga9a2bb018c589784edf36b204ba2daf48"></a>

```c
#define IRQ_TYPE_FIXED_LEVEL_HIGH (IRQ_DELIVERY_FIXED | IRQ_TYPE_LEVEL | IRQ_TYPE_HIGH)
```

相关声明：[IRQ_TYPE_FIXED_LEVEL_HIGH](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga9a2bb018c589784edf36b204ba2daf48)、[IRQ_DELIVERY_FIXED](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga19034e9b2fe534947855ad074cd5962b)、[IRQ_TYPE_LEVEL](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga296e915831223a614a6ea87dbe7735e7)、[IRQ_TYPE_HIGH](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaeb89171ec61787d7a3ced80b30af4359)。

固定投递（Fixed Delivery），电平触发，高电平有效。

<a id="r_gab570a690df9e89e8a38e257ce32e9801"></a>

```c
#define IRQ_TYPE_FIXED_LEVEL_LOW (IRQ_DELIVERY_FIXED | IRQ_TYPE_LEVEL | IRQ_TYPE_LOW)
```

相关声明：[IRQ_TYPE_FIXED_LEVEL_LOW](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gab570a690df9e89e8a38e257ce32e9801)、[IRQ_DELIVERY_FIXED](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga19034e9b2fe534947855ad074cd5962b)、[IRQ_TYPE_LEVEL](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga296e915831223a614a6ea87dbe7735e7)、[IRQ_TYPE_LOW](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga76dfa18a4a8be7f8b930115b7a9ffc93)。

固定投递（Fixed Delivery），电平触发，低电平有效。


## 18.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P040_intel-ioapic.h_源码浏览.md)
- [IRQ_TYPE_LEVEL](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga296e915831223a614a6ea87dbe7735e7)
- [IRQ_TYPE_EDGE](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaff68b0efbc719bc28f0d56c9ba8607bc)
- [IRQ_TYPE_LOW](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga76dfa18a4a8be7f8b930115b7a9ffc93)
- [IRQ_TYPE_HIGH](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaeb89171ec61787d7a3ced80b30af4359)
- [IRQ_DELIVERY_LOWEST](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga0c6b1b5a78c465e429a9a5633601d231)
- [IRQ_DELIVERY_FIXED](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga19034e9b2fe534947855ad074cd5962b)
- [IRQ_TYPE_LOWEST_EDGE_RISING](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga980bab4b0502b138f5fa8af9ca9833b4)
- [IRQ_TYPE_LOWEST_EDGE_FALLING](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga5a136f30dc5cb9f1b696751903b3fadd)
- [IRQ_TYPE_LOWEST_LEVEL_HIGH](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga9083a377fa943731dc24733933bae5d6)
- [IRQ_TYPE_LOWEST_LEVEL_LOW](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga15c26d56a818f5340c36117a429282a8)
- [IRQ_TYPE_FIXED_EDGE_RISING](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gaf1a9700940385a6aa6c9ff93fa834436)
- [IRQ_TYPE_FIXED_EDGE_FALLING](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga7f62c57495f357ec336cba12f1a12d61)
- [IRQ_TYPE_FIXED_LEVEL_HIGH](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#ga9a2bb018c589784edf36b204ba2daf48)
- [IRQ_TYPE_FIXED_LEVEL_LOW](../api_security_memory_topic_reference/P004_Intel I_O APIC中断控制器（Interrupt Controller）.md#gab570a690df9e89e8a38e257ce32e9801)

<a id="header-details"></a>

---

[上一章](P017_zephyr__drivers__bluetooth__hci_nxp_setup.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__dt-bindings__pwm__it51xxx_pwm.h_文件参考.md)
