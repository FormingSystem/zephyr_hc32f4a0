---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-4
title: Intel I_O APIC中断控制器（Interrupt Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__intel__ioapic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_Intel I\_O APIC中断控制器（Interrupt Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__intel__ioapic.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Intel I/O APIC 中断控制器的设备树标志。

<a id="details"></a>

Intel 输入输出高级可编程中断控制器（I/O APIC）的设备树标志（Devicetree Flags），用于兼容标识为 `intel,ioapic` 的中断控制器，描述触发方式、极性和投递模式（Trigger, Polarity and Delivery Mode）。各标志按位或组合，构成中断感知字段（Interrupt Sense Field）；`IRQ_TYPE_LOWEST_*` 和 `IRQ_TYPE_FIXED_*` 宏提供常见情况的现成组合。原始示例如下。

```c
&some_device {
        interrupts = <17 IRQ_TYPE_LOWEST_LEVEL_LOW 3>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_intel-ioapic_2Eh"></a>

```c
file intel-ioapic.h
```

相关声明：[intel-ioapic.h](https://docs.zephyrproject.org/latest/doxygen/html/intel-ioapic_8h.html)。

Intel输入输出高级可编程中断控制器（I/O APIC）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_ga296e915831223a614a6ea87dbe7735e7"></a>

```c
#define IRQ_TYPE_LEVEL 0x00008000
```

相关声明：[IRQ_TYPE_LEVEL](#ga296e915831223a614a6ea87dbe7735e7)。

电平触发中断（Level-Triggered Interrupt）。

<a id="r_gaff68b0efbc719bc28f0d56c9ba8607bc"></a>

```c
#define IRQ_TYPE_EDGE 0x00000000
```

相关声明：[IRQ_TYPE_EDGE](#gaff68b0efbc719bc28f0d56c9ba8607bc)。

边沿触发中断（Edge-Triggered Interrupt）。

<a id="r_ga76dfa18a4a8be7f8b930115b7a9ffc93"></a>

```c
#define IRQ_TYPE_LOW 0x00002000
```

相关声明：[IRQ_TYPE_LOW](#ga76dfa18a4a8be7f8b930115b7a9ffc93)。

低电平有效极性（Active-low Polarity）。

<a id="r_gaeb89171ec61787d7a3ced80b30af4359"></a>

```c
#define IRQ_TYPE_HIGH 0x00000000
```

相关声明：[IRQ_TYPE_HIGH](#gaeb89171ec61787d7a3ced80b30af4359)。

高电平有效极性（Active-high Polarity）。

<a id="r_ga0c6b1b5a78c465e429a9a5633601d231"></a>

```c
#define IRQ_DELIVERY_LOWEST 0x00000100
```

相关声明：[IRQ_DELIVERY_LOWEST](#ga0c6b1b5a78c465e429a9a5633601d231)。

最低优先级投递模式（Lowest-priority Delivery Mode）。

<a id="r_ga19034e9b2fe534947855ad074cd5962b"></a>

```c
#define IRQ_DELIVERY_FIXED 0x00000000
```

相关声明：[IRQ_DELIVERY_FIXED](#ga19034e9b2fe534947855ad074cd5962b)。

固定投递模式（Fixed Delivery Mode），适用于所有 CPU。

<a id="r_ga980bab4b0502b138f5fa8af9ca9833b4"></a>

```c
#define IRQ_TYPE_LOWEST_EDGE_RISING (IRQ_DELIVERY_LOWEST | IRQ_TYPE_EDGE | IRQ_TYPE_HIGH)
```

相关声明：[IRQ_TYPE_LOWEST_EDGE_RISING](#ga980bab4b0502b138f5fa8af9ca9833b4)、[IRQ_DELIVERY_LOWEST](#ga0c6b1b5a78c465e429a9a5633601d231)、[IRQ_TYPE_EDGE](#gaff68b0efbc719bc28f0d56c9ba8607bc)、[IRQ_TYPE_HIGH](#gaeb89171ec61787d7a3ced80b30af4359)。

最低优先级投递（Lowest-priority Delivery），边沿触发，上升沿。

<a id="r_ga5a136f30dc5cb9f1b696751903b3fadd"></a>

```c
#define IRQ_TYPE_LOWEST_EDGE_FALLING (IRQ_DELIVERY_LOWEST | IRQ_TYPE_EDGE | IRQ_TYPE_LOW)
```

相关声明：[IRQ_TYPE_LOWEST_EDGE_FALLING](#ga5a136f30dc5cb9f1b696751903b3fadd)、[IRQ_DELIVERY_LOWEST](#ga0c6b1b5a78c465e429a9a5633601d231)、[IRQ_TYPE_EDGE](#gaff68b0efbc719bc28f0d56c9ba8607bc)、[IRQ_TYPE_LOW](#ga76dfa18a4a8be7f8b930115b7a9ffc93)。

最低优先级投递（Lowest-priority Delivery），边沿触发，下降沿。

<a id="r_ga9083a377fa943731dc24733933bae5d6"></a>

```c
#define IRQ_TYPE_LOWEST_LEVEL_HIGH (IRQ_DELIVERY_LOWEST | IRQ_TYPE_LEVEL | IRQ_TYPE_HIGH)
```

相关声明：[IRQ_TYPE_LOWEST_LEVEL_HIGH](#ga9083a377fa943731dc24733933bae5d6)、[IRQ_DELIVERY_LOWEST](#ga0c6b1b5a78c465e429a9a5633601d231)、[IRQ_TYPE_LEVEL](#ga296e915831223a614a6ea87dbe7735e7)、[IRQ_TYPE_HIGH](#gaeb89171ec61787d7a3ced80b30af4359)。

最低优先级投递（Lowest-priority Delivery），电平触发，高电平有效。

<a id="r_ga15c26d56a818f5340c36117a429282a8"></a>

```c
#define IRQ_TYPE_LOWEST_LEVEL_LOW (IRQ_DELIVERY_LOWEST | IRQ_TYPE_LEVEL | IRQ_TYPE_LOW)
```

相关声明：[IRQ_TYPE_LOWEST_LEVEL_LOW](#ga15c26d56a818f5340c36117a429282a8)、[IRQ_DELIVERY_LOWEST](#ga0c6b1b5a78c465e429a9a5633601d231)、[IRQ_TYPE_LEVEL](#ga296e915831223a614a6ea87dbe7735e7)、[IRQ_TYPE_LOW](#ga76dfa18a4a8be7f8b930115b7a9ffc93)。

最低优先级投递（Lowest-priority Delivery），电平触发，低电平有效。

<a id="r_gaf1a9700940385a6aa6c9ff93fa834436"></a>

```c
#define IRQ_TYPE_FIXED_EDGE_RISING (IRQ_DELIVERY_FIXED | IRQ_TYPE_EDGE | IRQ_TYPE_HIGH)
```

相关声明：[IRQ_TYPE_FIXED_EDGE_RISING](#gaf1a9700940385a6aa6c9ff93fa834436)、[IRQ_DELIVERY_FIXED](#ga19034e9b2fe534947855ad074cd5962b)、[IRQ_TYPE_EDGE](#gaff68b0efbc719bc28f0d56c9ba8607bc)、[IRQ_TYPE_HIGH](#gaeb89171ec61787d7a3ced80b30af4359)。

固定投递（Fixed Delivery），边沿触发，上升沿。

<a id="r_ga7f62c57495f357ec336cba12f1a12d61"></a>

```c
#define IRQ_TYPE_FIXED_EDGE_FALLING (IRQ_DELIVERY_FIXED | IRQ_TYPE_EDGE | IRQ_TYPE_LOW)
```

相关声明：[IRQ_TYPE_FIXED_EDGE_FALLING](#ga7f62c57495f357ec336cba12f1a12d61)、[IRQ_DELIVERY_FIXED](#ga19034e9b2fe534947855ad074cd5962b)、[IRQ_TYPE_EDGE](#gaff68b0efbc719bc28f0d56c9ba8607bc)、[IRQ_TYPE_LOW](#ga76dfa18a4a8be7f8b930115b7a9ffc93)。

固定投递（Fixed Delivery），边沿触发，下降沿。

<a id="r_ga9a2bb018c589784edf36b204ba2daf48"></a>

```c
#define IRQ_TYPE_FIXED_LEVEL_HIGH (IRQ_DELIVERY_FIXED | IRQ_TYPE_LEVEL | IRQ_TYPE_HIGH)
```

相关声明：[IRQ_TYPE_FIXED_LEVEL_HIGH](#ga9a2bb018c589784edf36b204ba2daf48)、[IRQ_DELIVERY_FIXED](#ga19034e9b2fe534947855ad074cd5962b)、[IRQ_TYPE_LEVEL](#ga296e915831223a614a6ea87dbe7735e7)、[IRQ_TYPE_HIGH](#gaeb89171ec61787d7a3ced80b30af4359)。

固定投递（Fixed Delivery），电平触发，高电平有效。

<a id="r_gab570a690df9e89e8a38e257ce32e9801"></a>

```c
#define IRQ_TYPE_FIXED_LEVEL_LOW (IRQ_DELIVERY_FIXED | IRQ_TYPE_LEVEL | IRQ_TYPE_LOW)
```

相关声明：[IRQ_TYPE_FIXED_LEVEL_LOW](#gab570a690df9e89e8a38e257ce32e9801)、[IRQ_DELIVERY_FIXED](#ga19034e9b2fe534947855ad074cd5962b)、[IRQ_TYPE_LEVEL](#ga296e915831223a614a6ea87dbe7735e7)、[IRQ_TYPE_LOW](#ga76dfa18a4a8be7f8b930115b7a9ffc93)。

固定投递（Fixed Delivery），电平触发，低电平有效。

## 4.3\_详细说明（Detailed Documentation）

<a id="ga19034e9b2fe534947855ad074cd5962b"></a>

### `IRQ_DELIVERY_FIXED`

```c
#define IRQ_DELIVERY_FIXED 0x00000000
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

固定投递模式（Fixed Delivery Mode），适用于所有 CPU。

<a id="ga0c6b1b5a78c465e429a9a5633601d231"></a>

### `IRQ_DELIVERY_LOWEST`

```c
#define IRQ_DELIVERY_LOWEST 0x00000100
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

最低优先级投递模式（Lowest-priority Delivery Mode）。

<a id="gaff68b0efbc719bc28f0d56c9ba8607bc"></a>

### `IRQ_TYPE_EDGE`

```c
#define IRQ_TYPE_EDGE 0x00000000
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

边沿触发中断（Edge-Triggered Interrupt）。

<a id="ga7f62c57495f357ec336cba12f1a12d61"></a>

### `IRQ_TYPE_FIXED_EDGE_FALLING`

```c
#define IRQ_TYPE_FIXED_EDGE_FALLING (IRQ_DELIVERY_FIXED | IRQ_TYPE_EDGE | IRQ_TYPE_LOW)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

固定投递（Fixed Delivery），边沿触发，下降沿。

<a id="gaf1a9700940385a6aa6c9ff93fa834436"></a>

### `IRQ_TYPE_FIXED_EDGE_RISING`

```c
#define IRQ_TYPE_FIXED_EDGE_RISING (IRQ_DELIVERY_FIXED | IRQ_TYPE_EDGE | IRQ_TYPE_HIGH)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

固定投递（Fixed Delivery），边沿触发，上升沿。

<a id="ga9a2bb018c589784edf36b204ba2daf48"></a>

### `IRQ_TYPE_FIXED_LEVEL_HIGH`

```c
#define IRQ_TYPE_FIXED_LEVEL_HIGH (IRQ_DELIVERY_FIXED | IRQ_TYPE_LEVEL | IRQ_TYPE_HIGH)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

固定投递（Fixed Delivery），电平触发，高电平有效。

<a id="gab570a690df9e89e8a38e257ce32e9801"></a>

### `IRQ_TYPE_FIXED_LEVEL_LOW`

```c
#define IRQ_TYPE_FIXED_LEVEL_LOW (IRQ_DELIVERY_FIXED | IRQ_TYPE_LEVEL | IRQ_TYPE_LOW)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

固定投递（Fixed Delivery），电平触发，低电平有效。

<a id="gaeb89171ec61787d7a3ced80b30af4359"></a>

### `IRQ_TYPE_HIGH`

```c
#define IRQ_TYPE_HIGH 0x00000000
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

高电平有效极性（Active-high Polarity）。

<a id="ga296e915831223a614a6ea87dbe7735e7"></a>

### `IRQ_TYPE_LEVEL`

```c
#define IRQ_TYPE_LEVEL 0x00008000
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

电平触发中断（Level-Triggered Interrupt）。

<a id="ga76dfa18a4a8be7f8b930115b7a9ffc93"></a>

### `IRQ_TYPE_LOW`

```c
#define IRQ_TYPE_LOW 0x00002000
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

低电平有效极性（Active-low Polarity）。

<a id="ga5a136f30dc5cb9f1b696751903b3fadd"></a>

### `IRQ_TYPE_LOWEST_EDGE_FALLING`

```c
#define IRQ_TYPE_LOWEST_EDGE_FALLING (IRQ_DELIVERY_LOWEST | IRQ_TYPE_EDGE | IRQ_TYPE_LOW)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

最低优先级投递（Lowest-priority Delivery），边沿触发，下降沿。

<a id="ga980bab4b0502b138f5fa8af9ca9833b4"></a>

### `IRQ_TYPE_LOWEST_EDGE_RISING`

```c
#define IRQ_TYPE_LOWEST_EDGE_RISING (IRQ_DELIVERY_LOWEST | IRQ_TYPE_EDGE | IRQ_TYPE_HIGH)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

最低优先级投递（Lowest-priority Delivery），边沿触发，上升沿。

<a id="ga9083a377fa943731dc24733933bae5d6"></a>

### `IRQ_TYPE_LOWEST_LEVEL_HIGH`

```c
#define IRQ_TYPE_LOWEST_LEVEL_HIGH (IRQ_DELIVERY_LOWEST | IRQ_TYPE_LEVEL | IRQ_TYPE_HIGH)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

最低优先级投递（Lowest-priority Delivery），电平触发，高电平有效。

<a id="ga15c26d56a818f5340c36117a429282a8"></a>

### `IRQ_TYPE_LOWEST_LEVEL_LOW`

```c
#define IRQ_TYPE_LOWEST_LEVEL_LOW (IRQ_DELIVERY_LOWEST | IRQ_TYPE_LEVEL | IRQ_TYPE_LOW)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/intel-ioapic.h>
```

最低优先级投递（Lowest-priority Delivery），电平触发，低电平有效。


## 4.4\_原页交叉引用（Cross References）

- [intel-ioapic.h](https://docs.zephyrproject.org/latest/doxygen/html/intel-ioapic_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P003_DHCPv4 服务器.md) · [返回大纲](大纲.md) · [下一章](P005_堆内核地址消毒器 API（Heap KASAN APIs）.md)
