---
id: learning.zephyr-docs.kconfig-reference.page-383
title: "`subsys/mem_mgmt`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第383章\_`subsys/mem_mgmt`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/mem_mgmt` 的 14 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BACKING_STORE_CHOICE"></a>

## 383.1 `CONFIG_BACKING_STORE_CHOICE`

**提示（Prompt）**：后备存储算法（Backing store algorithms）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEMAND_PAGING
```

**默认值（Defaults）**

```text
CONFIG_BACKING_STORE_RAM
```

**可选项（Choices）**

```text
CONFIG_BACKING_STORE_CUSTOM
CONFIG_BACKING_STORE_RAM
CONFIG_BACKING_STORE_QEMU_X86_TINY_FLASH
CONFIG_BACKING_STORE_ONDEMAND_SEMIHOST
```

**定义位置（Location）**：[`subsys/mem_mgmt/demand_paging/backing_store/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/demand_paging/backing_store/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 请求分页模块（Demand Paging modules）

**配置项引用（Symbol References）**：[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_BACKING_STORE_RAM`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_BACKING_STORE_RAM)、[`CONFIG_BACKING_STORE_CUSTOM`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_BACKING_STORE_CUSTOM)、[`CONFIG_BACKING_STORE_QEMU_X86_TINY_FLASH`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_BACKING_STORE_QEMU_X86_TINY_FLASH)、[`CONFIG_BACKING_STORE_ONDEMAND_SEMIHOST`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_BACKING_STORE_ONDEMAND_SEMIHOST)。

<a id="CONFIG_BACKING_STORE_CUSTOM"></a>

## 383.2 `CONFIG_BACKING_STORE_CUSTOM`

**提示（Prompt）**：自定义后备存储实现（backing store implementation）

**说明（Help）**

由应用实现后备存储（backing store）时选择此项。由于后备存储通常高度依赖硬件，这会是常见选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BACKING_STORE_CHOICE>
```

**定义位置（Location）**：[`subsys/mem_mgmt/demand_paging/backing_store/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/demand_paging/backing_store/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 请求分页模块（Demand Paging modules） → 后备存储算法（Backing store algorithms）

**配置项引用（Symbol References）**：[`CONFIG_BACKING_STORE_CHOICE`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_BACKING_STORE_CHOICE)。

<a id="CONFIG_BACKING_STORE_ONDEMAND_SEMIHOST"></a>

## 383.3 `CONFIG_BACKING_STORE_ONDEMAND_SEMIHOST`

**提示（Prompt）**：通过半主机为按需链接器段提供后备存储

**说明（Help）**

用于对分别以 `__ondemand_func` 和 `__ondemand_rodata` 标记的代码与数据执行按需分页（on-demand paging）。通过半主机 I/O（semihosting I/O）从主机上编译生成的 `zephyr.bin` 读取所需数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEMIHOST && CONFIG_LINKER_USE_ONDEMAND_SECTION && <choice CONFIG_BACKING_STORE_CHOICE>
```

**定义位置（Location）**：[`subsys/mem_mgmt/demand_paging/backing_store/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/demand_paging/backing_store/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 请求分页模块（Demand Paging modules） → 后备存储算法（Backing store algorithms）

**配置项引用（Symbol References）**：[`CONFIG_SEMIHOST`](P032_arch_common_配置项参考.md#CONFIG_SEMIHOST)、[`CONFIG_LINKER_USE_ONDEMAND_SECTION`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_USE_ONDEMAND_SECTION)、[`CONFIG_BACKING_STORE_CHOICE`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_BACKING_STORE_CHOICE)。

<a id="CONFIG_BACKING_STORE_QEMU_X86_TINY_FLASH"></a>

## 383.4 `CONFIG_BACKING_STORE_QEMU_X86_TINY_FLASH`

**提示（Prompt）**：qemu_x86_tiny 上基于闪存的后备存储

**说明（Help）**

使用 DTS 中的 `flash` 内存区域作为请求分页（demand paging）的后备存储（backing store）。`qemu_x86_tiny.ld` 链接器脚本将启动段（boot）和固定驻留段（pinned）之外的符号放入闪存区域，从而能够测试代码和数据的请求分页机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOARD_QEMU_X86_TINY && <choice CONFIG_BACKING_STORE_CHOICE>
```

**定义位置（Location）**：[`subsys/mem_mgmt/demand_paging/backing_store/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/demand_paging/backing_store/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 请求分页模块（Demand Paging modules） → 后备存储算法（Backing store algorithms）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_QEMU_X86_TINY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_QEMU_X86_TINY)、[`CONFIG_BACKING_STORE_CHOICE`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_BACKING_STORE_CHOICE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_QEMU_X86_TINY`。

<a id="CONFIG_BACKING_STORE_RAM"></a>

## 383.5 `CONFIG_BACKING_STORE_RAM`

**提示（Prompt）**：基于 RAM 的测试后备存储（test backing store）

**说明（Help）**

使用 Zephyr 内核原本不知道的物理 RAM 页面实现后备存储（backing store），用于演示和测试请求分页（demand paging）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BACKING_STORE_CHOICE>
```

**定义位置（Location）**：[`subsys/mem_mgmt/demand_paging/backing_store/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/demand_paging/backing_store/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 请求分页模块（Demand Paging modules） → 后备存储算法（Backing store algorithms）

**配置项引用（Symbol References）**：[`CONFIG_BACKING_STORE_CHOICE`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_BACKING_STORE_CHOICE)。

<a id="CONFIG_BACKING_STORE_RAM_PAGES"></a>

## 383.6 `CONFIG_BACKING_STORE_RAM_PAGES`

**提示（Prompt）**：RAM 后备存储的页面数量

**说明（Help）**

在 RAM 中为后备存储（backing store）预留的页面数量。所有请求分页（demand paging）测试用例都假设至少有 16 页可用后备存储。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BACKING_STORE_RAM && CONFIG_DEMAND_PAGING
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/mem_mgmt/demand_paging/backing_store/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/demand_paging/backing_store/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 请求分页模块（Demand Paging modules）

**配置项引用（Symbol References）**：[`CONFIG_BACKING_STORE_RAM`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_BACKING_STORE_RAM)、[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)。

<a id="CONFIG_EVICTION_CHOICE"></a>

## 383.7 `CONFIG_EVICTION_CHOICE`

**提示（Prompt）**：页框淘汰算法（Page frame eviction algorithms）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEMAND_PAGING && CONFIG_DEMAND_PAGING
```

**默认值（Defaults）**

```text
CONFIG_EVICTION_LRU if CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING
CONFIG_EVICTION_NRU
```

**可选项（Choices）**

```text
CONFIG_EVICTION_CUSTOM
CONFIG_EVICTION_NRU
CONFIG_EVICTION_LRU
```

**定义位置（Location）**：[`subsys/mem_mgmt/demand_paging/eviction/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/demand_paging/eviction/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 请求分页模块（Demand Paging modules）

**配置项引用（Symbol References）**：[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_EVICTION_LRU`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_EVICTION_LRU)、[`CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING)、[`CONFIG_EVICTION_NRU`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_EVICTION_NRU)、[`CONFIG_EVICTION_CUSTOM`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_EVICTION_CUSTOM)。

<a id="CONFIG_EVICTION_CUSTOM"></a>

## 383.8 `CONFIG_EVICTION_CUSTOM`

**提示（Prompt）**：自定义淘汰算法（eviction algorithm）

**说明（Help）**

由应用实现淘汰算法（eviction algorithm），而不使用 Zephyr 自带算法时，选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EVICTION_CHOICE>
```

**弱选择（Implies）**

```text
CONFIG_EVICTION_TRACKING
```

**定义位置（Location）**：[`subsys/mem_mgmt/demand_paging/eviction/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/demand_paging/eviction/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 请求分页模块（Demand Paging modules） → 页框淘汰算法（Page frame eviction algorithms）

**配置项引用（Symbol References）**：[`CONFIG_EVICTION_CHOICE`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_EVICTION_CHOICE)、[`CONFIG_EVICTION_TRACKING`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_EVICTION_TRACKING)。

<a id="CONFIG_EVICTION_LRU"></a>

## 383.9 `CONFIG_EVICTION_LRU`

**提示（Prompt）**：最近最少使用页淘汰算法（Least Recently Used，LRU）

**说明（Help）**

实现最近最少使用（LRU）页淘汰算法。通过内存管理单元（MMU）保护，将页面设为不可访问，在实际使用时触发故障（fault），并利用该事件调整页面淘汰队列顺序，以跟踪使用情况。相较最近未使用（NRU）算法，它更高效：所有操作均为 `O(1)`；每次只清除一个页面的已访问标志（accessed flag），且仅在发生页面淘汰请求时执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING && <choice CONFIG_EVICTION_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_EVICTION_TRACKING
```

**定义位置（Location）**：[`subsys/mem_mgmt/demand_paging/eviction/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/demand_paging/eviction/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 请求分页模块（Demand Paging modules） → 页框淘汰算法（Page frame eviction algorithms）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING)、[`CONFIG_EVICTION_CHOICE`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_EVICTION_CHOICE)、[`CONFIG_EVICTION_TRACKING`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_EVICTION_TRACKING)。

<a id="CONFIG_EVICTION_NRU"></a>

## 383.10 `CONFIG_EVICTION_NRU`

**提示（Prompt）**：最近未使用页淘汰算法（Not Recently Used，NRU）

**说明（Help）**

实现最近未使用（NRU）页淘汰算法。周期性定时器清除所有虚拟页面的已访问状态。需要淘汰页框（page frame）时，原文按“优先级升序（ascending order of priority）”列出以下类别：

1. 最近访问过，脏页（dirty）。
2. 最近访问过，干净页（clean）。
3. 最近未访问过，脏页（dirty）。
4. 最近未访问过，干净页（clean）。

译注：列表按原文次序保留，“优先级升序”意味着不能将第一项直接理解为最先淘汰的类别。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EVICTION_CHOICE>
```

**定义位置（Location）**：[`subsys/mem_mgmt/demand_paging/eviction/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/demand_paging/eviction/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 请求分页模块（Demand Paging modules） → 页框淘汰算法（Page frame eviction algorithms）

**配置项引用（Symbol References）**：[`CONFIG_EVICTION_CHOICE`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_EVICTION_CHOICE)。

<a id="CONFIG_EVICTION_NRU_PERIOD"></a>

## 383.11 `CONFIG_EVICTION_NRU_PERIOD`

**提示（Prompt）**：判定最近访问的周期（毫秒）

**说明（Help）**

周期性定时器触发时，清除所有可换出虚拟页面的已访问状态（accessed state）。淘汰页面时，若仍带有已访问属性，则视为最近使用过（recently used）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EVICTION_NRU && CONFIG_DEMAND_PAGING
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/mem_mgmt/demand_paging/eviction/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/demand_paging/eviction/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 请求分页模块（Demand Paging modules）

**配置项引用（Symbol References）**：[`CONFIG_EVICTION_NRU`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_EVICTION_NRU)、[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)。

<a id="CONFIG_EVICTION_TRACKING"></a>

## 383.12 `CONFIG_EVICTION_TRACKING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由需要页面跟踪（page tracking）的淘汰算法选择。这些算法必须实现 `k_mem_paging_eviction_add()`、`k_mem_paging_eviction_remove()` 和 `k_mem_paging_eviction_accessed()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING && CONFIG_DEMAND_PAGING
```

**被选择（Selected by）**

```text
CONFIG_ARM64
CONFIG_X86
CONFIG_EVICTION_LRU
```

**被弱选择（Implied by）**

```text
CONFIG_EVICTION_CUSTOM
```

**定义位置（Location）**：[`subsys/mem_mgmt/demand_paging/eviction/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/demand_paging/eviction/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 请求分页模块（Demand Paging modules）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_SUPPORTS_EVICTION_TRACKING)、[`CONFIG_DEMAND_PAGING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_PAGING)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_EVICTION_LRU`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_EVICTION_LRU)、[`CONFIG_EVICTION_CUSTOM`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_EVICTION_CUSTOM)。

<a id="CONFIG_MEM_ATTR"></a>

## 383.13 `CONFIG_MEM_ATTR`

**提示（Prompt）**：内存属性管理库（Memory Attributes management library）

**说明（Help）**

启用小型库，管理设备树（DT）中具有 `zephyr,memory-attr` 属性的内存区域。该库在构建时生成这些内存区域的数组，并提供多个辅助函数（helper functions）供运行时查询。不确定时设为 `N`，以节省只读数据（RODATA）空间。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if CONFIG_ARM_MPU
```

**定义位置（Location）**：[`subsys/mem_mgmt/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)。

<a id="CONFIG_MEM_ATTR_HEAP"></a>

## 383.14 `CONFIG_MEM_ATTR_HEAP`

**提示（Prompt）**：基于内存属性的堆分配器（Memory Attributes heap allocator）

**说明（Help）**

启用基于内存属性（memory attributes）的堆分配器，从设备树（DeviceTree）定义的内存区域动态分配内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MEM_ATTR
```

**定义位置（Location）**：[`subsys/mem_mgmt/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mem_mgmt/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 内存属性管理库（Memory Attributes management library）

**配置项引用（Symbol References）**：[`CONFIG_MEM_ATTR`](P383_subsys_mem_mgmt_配置项参考.md#CONFIG_MEM_ATTR)。

<!-- kconfig-navigation -->

[上一章](P382_subsys_lorawan_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P384_subsys_mgmt_配置项参考_1.md)
