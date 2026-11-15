---
id: learning.zephyr-docs.kconfig-reference.page-76
title: "`drivers/disk`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第76章\_`drivers/disk`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/disk` 的 35 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DISK_DRIVERS"></a>

## 76.1 `CONFIG_DISK_DRIVERS`

**提示（Prompt）**：磁盘驱动（Disk Drivers）

**说明（Help）**

磁盘驱动（Disk Driver）配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_DISK_ACCESS
```

**定义位置（Location）**：[`drivers/disk/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISK_ACCESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISK_ACCESS)。

<a id="CONFIG_DISK_DRIVER_FLASH"></a>

## 76.2 `CONFIG_DISK_DRIVER_FLASH`

**提示（Prompt）**：闪存（Flash）

**说明（Help）**

使用闪存设备（Flash Device）承载文件系统（File System）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_FLASH_DISK_ENABLED && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH
CONFIG_FLASH_MAP
```

**定义位置（Location）**：[`drivers/disk/Kconfig.flash:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.flash#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH)、[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)。

<a id="CONFIG_DISK_DRIVER_FTL"></a>

## 76.3 `CONFIG_DISK_DRIVER_FTL`

**提示（Prompt）**：闪存转换层（Flash Translation Layer，FTL）

**说明（Help）**

启用用于 NAND 闪存的闪存转换层（Flash Translation Layer）磁盘驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZEPHYR_DHARA_MODULE && DT_HAS_ZEPHYR_FTL_DHARA_ENABLED && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FLASH
CONFIG_FLASH_MAP
CONFIG_FLASH_EX_OP_ENABLED
```

**定义位置（Location）**：[`drivers/disk/Kconfig.ftl:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.ftl#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_DHARA_MODULE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_DHARA_MODULE)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH)、[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_FLASH_EX_OP_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_EX_OP_ENABLED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_DHARA_MODULE`。

<a id="CONFIG_DISK_DRIVER_LOOPBACK"></a>

## 76.4 `CONFIG_DISK_DRIVER_LOOPBACK`

**提示（Prompt）**：回环磁盘（Loopback Disk）

**说明（Help）**

允许将文件内容挂载（Mount）为一个独立磁盘。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM && CONFIG_DISK_DRIVERS
```

**定义位置（Location）**：[`drivers/disk/Kconfig.loopback:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.loopback#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FILE_SYSTEM)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_DISK_DRIVER_MEMC_RAM"></a>

## 76.5 `CONFIG_DISK_DRIVER_MEMC_RAM`

**提示（Prompt）**：MEMC RAM 磁盘（RAM Disk）

**说明（Help）**

通过内存控制器（MEMC）子系统 API 访问外部 RAM 设备的磁盘驱动。扇区（Sector）读写操作被转换为对关联 MEMC 设备的 `memc_read()` / `memc_write()` 调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_MEMC_RAM_DISK_ENABLED && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MEMC
```

**定义位置（Location）**：[`drivers/disk/Kconfig.memc_ram:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.memc_ram#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_MEMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC)。

<a id="CONFIG_DISK_DRIVER_MMC"></a>

## 76.6 `CONFIG_DISK_DRIVER_MMC`

**提示（Prompt）**：MMC 卡驱动

**说明（Help）**

MMC 卡驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_MMC_DISK_ENABLED && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/disk/Kconfig.mmc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.mmc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_DISK_DRIVER_RAM"></a>

## 76.7 `CONFIG_DISK_DRIVER_RAM`

**提示（Prompt）**：RAM 磁盘（RAM Disk）

**说明（Help）**

使用 RAM 缓冲区（Buffer）模拟存储磁盘。此选项可用于测试文件系统（File System）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_RAM_DISK_ENABLED && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/disk/Kconfig.ram:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.ram#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_DISK_DRIVER_SDMMC"></a>

## 76.8 `CONFIG_DISK_DRIVER_SDMMC`

**提示（Prompt）**：SDMMC 卡驱动

**说明（Help）**

SDMMC 卡驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ZEPHYR_SDMMC_DISK_ENABLED || DT_HAS_ST_STM32_SDMMC_ENABLED) && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/disk/Kconfig.sdmmc:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.sdmmc#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_DISK_DRIVER_VIRTIO_BLK"></a>

## 76.9 `CONFIG_DISK_DRIVER_VIRTIO_BLK`

**提示（Prompt）**：VIRTIO 块磁盘（Block Disk）驱动

**说明（Help）**

启用 VIRTIO 块设备（Block Device）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_VIRTIO_BLK_ENABLED && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_VIRTIO
```

**定义位置（Location）**：[`drivers/disk/Kconfig.virtio_blk:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.virtio_blk#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_VIRTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIRTIO)。

<a id="CONFIG_DISK_FTL_GC_RATIO"></a>

## 76.10 `CONFIG_DISK_FTL_GC_RATIO`

**提示（Prompt）**：垃圾回收比率（Garbage Collection Ratio）

**说明（Help）**

自动回收（Automatic Collection）启用时，垃圾回收操作与实际写入操作的比率。较小的值可使输入/输出（I/O）更快、更可预测，但代价是容量降低。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISK_DRIVER_FTL && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
15
```

**定义位置（Location）**：[`drivers/disk/Kconfig.ftl:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.ftl#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存转换层（Flash Translation Layer，FTL）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_FTL`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_FTL)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_DISK_FTL_SUPPORT_CONCURRENT_ACCESS"></a>

## 76.11 `CONFIG_DISK_FTL_SUPPORT_CONCURRENT_ACCESS`

**提示（Prompt）**：支持并发访问（Concurrent Access）

**说明（Help）**

启用磁盘并发访问（Concurrent Access）支持，允许多个线程同时访问磁盘。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISK_DRIVER_FTL && CONFIG_DISK_DRIVERS
```

**定义位置（Location）**：[`drivers/disk/Kconfig.ftl:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.ftl#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存转换层（Flash Translation Layer，FTL）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_FTL`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_FTL)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_DISK_RAM_DECOMPRESS"></a>

## 76.12 `CONFIG_DISK_RAM_DECOMPRESS`

**提示（Prompt）**：解压初始 RAM 磁盘（initrd）

**说明（Help）**

在将初始 RAM 磁盘（initrd）用作 RAM 磁盘（RAM Disk）之前，先对其解压。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISK_DRIVER_RAM && CONFIG_DISK_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_RAM_LZ4_DECOMPRESSOR
```

**定义位置（Location）**：[`drivers/disk/Kconfig.ram:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.ram#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → RAM 磁盘（RAM Disk）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_RAM`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_RAM)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_RAM_LZ4_DECOMPRESSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RAM_LZ4_DECOMPRESSOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_RAM_LZ4_DECOMPRESSOR`。

<a id="CONFIG_DISK_VIRTIO_BLK_MAX_SEGMENTS"></a>

## 76.13 `CONFIG_DISK_VIRTIO_BLK_MAX_SEGMENTS`

**提示（Prompt）**：每个 VIRTIO 块请求的最大分散/聚集数据段（Scatter-Gather Data Segment）数量

**说明（Help）**

单个块请求（Block Request）可携带的最大分散/聚集数据段（Scatter-Gather Data Segment）数量。这是数据段数量的预算，并非最终的虚拟队列（Virtqueue）大小。驱动同一时刻只保留一个在途请求（In-Flight Request），并将 `(MAX_SEGMENTS + 2)` 向上取整到 2 的幂，作为请求虚拟队列的大小；额外的两个描述符（Descriptor）分别保存请求头和状态字节。因此，默认值 `14` 对应具有 16 个条目的虚拟队列，最大值对应具有 256 个条目的虚拟队列。此设置限制单次传输可具有的物理内存碎片程度；超过限制后，驱动会将其拆分为多个设备请求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MMU && CONFIG_DISK_DRIVER_VIRTIO_BLK && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
14
```

**取值范围（Ranges）**

```text
[1, 254]
```

**定义位置（Location）**：[`drivers/disk/Kconfig.virtio_blk:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.virtio_blk#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → VIRTIO 块磁盘（Block Disk）驱动

**配置项引用（Symbol References）**：[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_DISK_DRIVER_VIRTIO_BLK`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_VIRTIO_BLK)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_DISK_VIRTIO_BLK_SECTOR_SIZE"></a>

## 76.14 `CONFIG_DISK_VIRTIO_BLK_SECTOR_SIZE`

**提示（Prompt）**：VIRTIO 块设备的回退逻辑块大小（Fallback Logical Block Size）

**说明（Help）**

当设备未声明 `VIRTIO_BLK_F_BLK_SIZE` 时，向磁盘访问层（Disk Access Layer）报告的逻辑块（扇区，Sector）大小。设备声明该特性时，改用设备报告的 `blk_size`，并忽略此值。此值必须是 512 的整数倍；启用 `CONFIG_MMU` 时，不得超过内存管理单元（MMU）的页大小（Page Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISK_DRIVER_VIRTIO_BLK && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[512, 4096]
```

**定义位置（Location）**：[`drivers/disk/Kconfig.virtio_blk:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.virtio_blk#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → VIRTIO 块磁盘（Block Disk）驱动

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_VIRTIO_BLK`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_VIRTIO_BLK)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_FLASHDISK_VERIFY_PAGE_LAYOUT"></a>

## 76.15 `CONFIG_FLASHDISK_VERIFY_PAGE_LAYOUT`

**提示（Prompt）**：验证闪存磁盘分区布局（Flashdisk Partition Layout）

**说明（Help）**

启用运行时检查，验证 `zephyr,flash-disk` 分区的页布局（Page Layout）约束。禁用此项可减小代码大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISK_DRIVER_FLASH && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/disk/Kconfig.flash:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.flash#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_FLASH`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_FLASH)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_LOOPBACK_DISK_SECTOR_SIZE"></a>

## 76.16 `CONFIG_LOOPBACK_DISK_SECTOR_SIZE`

**提示（Prompt）**：回环磁盘扇区大小（Loopback Disk Sector Size）

**说明（Help）**

设置通过回环方式挂载（Loopback-Mounted）的磁盘所用的扇区大小（Sector Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISK_DRIVER_LOOPBACK && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/disk/Kconfig.loopback:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.loopback#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 回环磁盘（Loopback Disk）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_LOOPBACK`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_LOOPBACK)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_MEMC_RAMDISK_INIT_PRIORITY"></a>

## 76.17 `CONFIG_MEMC_RAMDISK_INIT_PRIORITY`

**提示（Prompt）**：MEMC RAM 磁盘初始化优先级（Init Priority）

**说明（Help）**

MEMC RAM 磁盘驱动的初始化优先级（Init Priority）。数值至少应为 `CONFIG_MEMC_INIT_PRIORITY`，以确保本驱动初始化时，提供存储的 MEMC 设备已经可用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISK_DRIVER_MEMC_RAM && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_MEMC_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/disk/Kconfig.memc_ram:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.memc_ram#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MEMC RAM 磁盘（RAM Disk）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_MEMC_RAM`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_MEMC_RAM)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_MEMC_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC_INIT_PRIORITY)。

<a id="CONFIG_MMC_SUBSYS"></a>

## 76.18 `CONFIG_MMC_SUBSYS`

**提示（Prompt）**：通过 SD 子系统访问 MMC

**说明（Help）**

启用通过 SD 子系统访问 MMC 的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_MMC_DISK_ENABLED && CONFIG_DISK_DRIVER_MMC && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MMC_STACK
```

**定义位置（Location）**：[`drivers/disk/Kconfig.mmc:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.mmc#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MMC 卡驱动

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_MMC`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_MMC)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_MMC_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MMC_STACK)。

<a id="CONFIG_NVME"></a>

## 76.19 `CONFIG_NVME`

**提示（Prompt）**：NVMe 磁盘（NVMe Disk）

**说明（Help）**

系统可能通过 PCIe 连接一个或多个 NVMe 磁盘，启用此驱动即可支持它们。此驱动会启用 MSI-X 和 MSI 多向量（Multi-Vector）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NVME_CONTROLLER_ENABLED && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PCIE
CONFIG_PCIE_MSI
CONFIG_PCIE_MSI_X
CONFIG_PCIE_MSI_MULTI_VECTOR
```

**定义位置（Location）**：[`drivers/disk/nvme/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_PCIE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE)、[`CONFIG_PCIE_MSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_MSI)、[`CONFIG_PCIE_MSI_X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_MSI_X)、[`CONFIG_PCIE_MSI_MULTI_VECTOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PCIE_MSI_MULTI_VECTOR)。

<a id="CONFIG_NVME_ADMIN_ENTRIES"></a>

## 76.20 `CONFIG_NVME_ADMIN_ENTRIES`

**提示（Prompt）**：管理队列条目（Admin Queue Entry）数量

**说明（Help）**

设置分配的管理队列条目（Admin Queue Entry）数量。除非了解修改的影响，否则不要更改此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NVME && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[2, 4096]
```

**定义位置（Location）**：[`drivers/disk/nvme/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk）

**配置项引用（Symbol References）**：[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_NVME_INT_PRIORITY"></a>

## 76.21 `CONFIG_NVME_INT_PRIORITY`

**提示（Prompt）**：中断优先级。

**说明（Help）**

用于 MSI-X 生成的中断的中断优先级（Interrupt Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NVME && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/disk/nvme/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk）

**配置项引用（Symbol References）**：[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_NVME_IO_ENTRIES"></a>

## 76.22 `CONFIG_NVME_IO_ENTRIES`

**提示（Prompt）**：I/O 队列条目（IO Queue Entry）数量

**说明（Help）**

设置分配的 I/O 队列条目（IO Queue Entry）数量。除非了解修改的影响，否则不要更改此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NVME && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[2, 65536]
```

**定义位置（Location）**：[`drivers/disk/nvme/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk）

**配置项引用（Symbol References）**：[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_NVME_IO_QUEUES"></a>

## 76.23 `CONFIG_NVME_IO_QUEUES`

**提示（Prompt）**：I/O 队列（IO Queue）数量

**说明（Help）**

设置分配的 I/O 队列（I/O Queue）数量。除非了解修改的影响，否则不要更改此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NVME && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 65536]
```

**定义位置（Location）**：[`drivers/disk/nvme/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk）

**配置项引用（Symbol References）**：[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_NVME_MAX_NAMESPACES"></a>

## 76.24 `CONFIG_NVME_MAX_NAMESPACES`

**提示（Prompt）**：可分配的最大命名空间（Namespace）数量

**说明（Help）**

设置可分配的最大命名空间（Namespace）数量。运行时实际实例化的数量可能远小于此值，因此可利用此选项适当减少内存用量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NVME && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`drivers/disk/nvme/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk）

**配置项引用（Symbol References）**：[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_NVME_PRP_LIST_AMOUNT"></a>

## 76.25 `CONFIG_NVME_PRP_LIST_AMOUNT`

**提示（Prompt）**：分配的 PRP 列表（PRP List）数量

**说明（Help）**

设置预先分配的 PRP 列表（PRP List）数量。每个列表可在一条 NVMe 命令中用于寻址要读取或写入数据的内存。每个 PRP 列表占用一页大小的空间，设置数量时应谨慎，因为它们可能占用可观的内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NVME && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/disk/nvme/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk）

**配置项引用（Symbol References）**：[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_NVME_PRP_PAGE_SIZE"></a>

## 76.26 `CONFIG_NVME_PRP_PAGE_SIZE`

**提示（Prompt）**：NVMe PRP 页大小（Page Size）

**说明（Help）**

设置 PRP 页大小（Page Size）。启用内存管理单元（MMU）时，默认采用 MMU 页大小。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NVME && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_MMU_PAGE_SIZE if CONFIG_MMU
0x1000
```

**定义位置（Location）**：[`drivers/disk/nvme/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk）

**配置项引用（Symbol References）**：[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_MMU_PAGE_SIZE`](P001_kernel_配置项参考_1.md#CONFIG_MMU_PAGE_SIZE)、[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)。

<a id="CONFIG_NVME_REQUEST_TIMEOUT"></a>

## 76.27 `CONFIG_NVME_REQUEST_TIMEOUT`

**提示（Prompt）**：NVMe 请求超时时间（Request Timeout Period）

**说明（Help）**

设置等待请求成功的时间，以秒为单位。除非了解修改的影响，否则不要更改此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NVME && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[5, 120]
```

**定义位置（Location）**：[`drivers/disk/nvme/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk）

**配置项引用（Symbol References）**：[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_NVME_RETRY_COUNT"></a>

## 76.28 `CONFIG_NVME_RETRY_COUNT`

**提示（Prompt）**：重试次数（Retry Count）

**说明（Help）**

设置每个请求允许的重试次数（Retry Count）。除非了解修改的影响，否则不要更改此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NVME && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/disk/nvme/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → NVMe 磁盘（NVMe Disk）

**配置项引用（Symbol References）**：[`CONFIG_NVME`](P076_drivers_disk_配置项参考.md#CONFIG_NVME)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_SDMMC_STM32"></a>

## 76.29 `CONFIG_SDMMC_STM32`

**提示（Prompt）**：STM32 SDMMC 驱动

**说明（Help）**

通过 STM32 SDMMC 访问 SDMMC 上的文件系统（File System）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_SDMMC_ENABLED && CONFIG_DISK_DRIVER_SDMMC && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_SD if !CONFIG_SDMMC_STM32_EMMC
CONFIG_USE_STM32_HAL_SD_EX if !CONFIG_SDMMC_STM32_EMMC && CONFIG_SOC_SERIES_STM32L4X
CONFIG_USE_STM32_HAL_MMC if CONFIG_SDMMC_STM32_EMMC
CONFIG_USE_STM32_HAL_MMC_EX if CONFIG_SDMMC_STM32_EMMC && CONFIG_SOC_SERIES_STM32L4X
CONFIG_USE_STM32_LL_SDMMC
CONFIG_USE_STM32_HAL_DMA if CONFIG_SOC_SERIES_STM32L4X || CONFIG_SOC_SERIES_STM32F7X || CONFIG_SOC_SERIES_STM32F4X
CONFIG_DMA if n && (CONFIG_SOC_SERIES_STM32F4X || CONFIG_SOC_SERIES_STM32F7X || CONFIG_SOC_SERIES_STM32L4X)
CONFIG_GPIO
CONFIG_PINCTRL
CONFIG_RESET
```

**定义位置（Location）**：[`drivers/disk/Kconfig.sdmmc:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.sdmmc#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_SDMMC`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_SDMMC)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_USE_STM32_HAL_SD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_SD)、[`CONFIG_SDMMC_STM32_EMMC`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32_EMMC)、[`CONFIG_USE_STM32_HAL_SD_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_SD_EX)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_USE_STM32_HAL_MMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_MMC)、[`CONFIG_USE_STM32_HAL_MMC_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_MMC_EX)、[`CONFIG_USE_STM32_LL_SDMMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_SDMMC)、[`CONFIG_USE_STM32_HAL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32F4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F4X)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32F4X`。

<a id="CONFIG_SDMMC_STM32_CLOCK_CHECK"></a>

## 76.30 `CONFIG_SDMMC_STM32_CLOCK_CHECK`

**提示（Prompt）**：运行时 SDMMC 48 MHz 时钟检查（Runtime Clock Check）

**说明（Help）**

启用对 SDMMC 48 MHz 时钟配置的运行时检查（Runtime Check）。在某些特定情况下，此检查可能给出错误判断，此时应禁用它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDMMC_STM32 && CONFIG_DISK_DRIVER_SDMMC && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/disk/Kconfig.sdmmc:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.sdmmc#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动 → STM32 SDMMC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)、[`CONFIG_DISK_DRIVER_SDMMC`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_SDMMC)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_SDMMC_STM32_EMMC"></a>

## 76.31 `CONFIG_SDMMC_STM32_EMMC`

**提示（Prompt）**：STM32 SDMMC eMMC 模式（Mode）

**说明（Help）**

使用 eMMC 协议代替 SDIO（SD 卡）协议。两者类似，但并不完全相同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDMMC_STM32 && CONFIG_DISK_DRIVER_SDMMC && CONFIG_DISK_DRIVERS
```

**定义位置（Location）**：[`drivers/disk/Kconfig.sdmmc:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.sdmmc#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动 → STM32 SDMMC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)、[`CONFIG_DISK_DRIVER_SDMMC`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_SDMMC)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_SDMMC_STM32_HWFC"></a>

## 76.32 `CONFIG_SDMMC_STM32_HWFC`

**提示（Prompt）**：STM32 SDMMC 硬件流控（Hardware Flow Control）

**说明（Help）**

启用 SDMMC 硬件流控（Hardware Flow Control），避免 FIFO 下溢（Underrun，发送模式）和上溢（Overrun，接收模式）错误。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDMMC_STM32 && (CONFIG_SOC_SERIES_STM32H5X || CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32H7RSX || CONFIG_SOC_SERIES_STM32F7X || CONFIG_SOC_SERIES_STM32L4X || CONFIG_SOC_SERIES_STM32L5X || CONFIG_SOC_SERIES_STM32N6X) && CONFIG_DISK_DRIVER_SDMMC && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/disk/Kconfig.sdmmc:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.sdmmc#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动 → STM32 SDMMC 驱动

**配置项引用（Symbol References）**：[`CONFIG_SDMMC_STM32`](P076_drivers_disk_配置项参考.md#CONFIG_SDMMC_STM32)、[`CONFIG_SOC_SERIES_STM32H5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H5X)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32H7RSX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7RSX)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_SOC_SERIES_STM32L4X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L4X)、[`CONFIG_SOC_SERIES_STM32L5X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32L5X)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)、[`CONFIG_DISK_DRIVER_SDMMC`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_SDMMC)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32H5X`、`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32H7RSX`、`CONFIG_SOC_SERIES_STM32F7X`、`CONFIG_SOC_SERIES_STM32L4X`、`CONFIG_SOC_SERIES_STM32L5X`、`CONFIG_SOC_SERIES_STM32N6X`。

<a id="CONFIG_SDMMC_SUBSYS"></a>

## 76.33 `CONFIG_SDMMC_SUBSYS`

**提示（Prompt）**：通过 SD 子系统访问 SDMMC

**说明（Help）**

启用通过 SD 子系统访问 SDMMC 的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_SDMMC_DISK_ENABLED && CONFIG_DISK_DRIVER_SDMMC && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SDMMC_STACK
```

**定义位置（Location）**：[`drivers/disk/Kconfig.sdmmc:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.sdmmc#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_SDMMC`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_SDMMC)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_SDMMC_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SDMMC_STACK)。

<a id="CONFIG_SD_INIT_PRIORITY"></a>

## 76.34 `CONFIG_SD_INIT_PRIORITY`

原库同名定义共 2 条；本项为数据库第 16578 条记录，各定义分别保留。

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

MMC 控制器驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISK_DRIVER_MMC && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/disk/Kconfig.mmc:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.mmc#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MMC 卡驱动

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_MMC`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_MMC)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<a id="CONFIG_SD_INIT_PRIORITY--record-16579"></a>

## 76.35 `CONFIG_SD_INIT_PRIORITY`

原库同名定义共 2 条；本项为数据库第 16579 条记录，各定义分别保留。

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

SDMMC 控制器驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISK_DRIVER_SDMMC && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/disk/Kconfig.sdmmc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/Kconfig.sdmmc#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → SDMMC 卡驱动

**配置项引用（Symbol References）**：[`CONFIG_DISK_DRIVER_SDMMC`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_SDMMC)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)。

<!-- kconfig-navigation -->

[上一章](P075_drivers_debug_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P077_drivers_display_配置项参考_1.md)
