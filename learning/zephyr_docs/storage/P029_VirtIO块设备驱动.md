---
id: learning.zephyr-docs.storage.diskmore-1
title: VirtIO块设备驱动
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/services/storage/disk/virtio_blk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第29章\_VirtIO块设备驱动

原文：[VirtIO Block](https://docs.zephyrproject.org/latest/services/storage/disk/virtio_blk.html)。读取日期：2026-10-13，`latest`。

**VirtIO 虚拟设备接口（VirtIO）**是向**客户系统（Guest）**呈现虚拟设备的标准化接口，通常运行在 QEMU 等**虚拟机监控器（Hypervisor）**之下。`virtio,blk` 驱动将 VirtIO 块设备呈现为 Zephyr 磁盘，可通过[磁盘访问接口（Disk Access API）](https://docs.zephyrproject.org/latest/services/storage/disk/access.html#disk-access-api)及其上层的[文件系统接口（File System API）](https://docs.zephyrproject.org/latest/services/storage/file_system/index.html#file-system-api)访问。

驱动不依赖具体传输方式，可以不作修改地运行在 Zephyr 支持的两种 VirtIO 传输之上：**外围组件互连（Peripheral Component Interconnect，PCI）**和**内存映射输入输出（Memory-Mapped I/O，MMIO）**。详情见 [VirtIO](../hardware/P570_VirtIO虚拟设备.md)。每个已启用的 `virtio,blk` 设备树节点都会创建一个实例。

## 29.1\_驱动分层

驱动位于 [`drivers/disk/virtio_blk.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/virtio_blk.c)，建立在通用 VirtIO API 之上。`virtio,blk` 节点是 VirtIO 传输设备的子节点，通过 `DT_INST_PARENT` 获取父节点，因此同一份代码可同时用于 PCI 和 MMIO 设备。

## 29.2\_同时只处理一个请求

磁盘访问的读写 API 是同步、阻塞式接口。驱动还通过**互斥锁（Mutex）**串行化调用者，因此每台设备恰好保持一个**处理中请求（In-flight Request）**：向请求**虚拟队列（Virtqueue）**添加一条**描述符链（Descriptor Chain）**，通知设备，然后阻塞等待**信号量（Semaphore）**；完成回调在**中断上下文（Interrupt Context）**中释放该信号量。

由于没有**请求流水线（Request Pipelining）**，整个虚拟队列都用于单次请求的**分散聚集链（Scatter-Gather Chain）**。用户通过 [`CONFIG_DISK_VIRTIO_BLK_MAX_SEGMENTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISK_VIRTIO_BLK_MAX_SEGMENTS) 配置每次请求的最大数据段数。驱动把 `MAX_SEGMENTS + 2` 向上取整到 2 的幂，作为虚拟队列大小；额外两个位置留给请求头和状态字节。

## 29.3\_逻辑块大小

VirtIO 块协议始终以固定 **512 字节扇区（Sector）**寻址设备，并以该单位报告设备容量。向 `disk_access` 提供的**逻辑块大小（Logical Block Size）**则可能不同：

- 设备提供 `VIRTIO_BLK_F_BLK_SIZE` 特性时，驱动协商该特性并采用设备报告的 `blk_size`。
- 否则，回退为 [`CONFIG_DISK_VIRTIO_BLK_SECTOR_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISK_VIRTIO_BLK_SECTOR_SIZE)。

所有地址都会在内部换算为 512 字节的 VirtIO 扇区。逻辑块大小必须是 512 的整数倍；启用 [`CONFIG_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MMU) 时，还不能超过**内存管理单元（Memory Management Unit，MMU）**的页大小。不支持的取值会在初始化时被拒绝。

## 29.4\_零拷贝传输

调用者缓冲区直接交给设备，不经过**中转缓冲区（Bounce Buffer）**，实现**零拷贝（Zero Copy）**传输。

启用 [`CONFIG_MMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MMU) 时，缓冲区可能位于内核线性**随机存取存储器（Random Access Memory，RAM）**映射之外，例如 `f_mkfs()` 向下传递的线程栈工作区，而且不一定物理连续。驱动通过 `arch_page_phys_get()` 逐页遍历缓冲区，将物理地址相邻的区段合并为分散聚集段。当传输碎片数量超过允许的段数时，将其拆为多个设备请求。

## 29.5\_特性协商与错误返回

除了 `VIRTIO_BLK_F_BLK_SIZE`，驱动还协商以下特性：

| 特性 | 行为 |
| --- | --- |
| `VIRTIO_BLK_F_RO` | **只读（Read Only）**设备报告 `DISK_STATUS_WR_PROTECT`，写请求以 `-EROFS` 拒绝 |
| `VIRTIO_BLK_F_FLUSH` | `DISK_IOCTL_CTRL_SYNC` 向设备发出**刷新（Flush）**操作。若设备没有提供此特性，就没有需要刷新的**回写缓存（Writeback Cache）**；此时该控制调用作为空操作成功返回 |

若已完成请求的状态字节不是成功状态 `OK`，驱动会记录日志并将其转换为错误码：不支持的请求返回 `-ENOTSUP`，**输入输出（Input/Output，I/O）**错误返回 `-EIO`。

## 29.6\_设备树配置

`virtio,blk` 节点放在 VirtIO 传输父节点之下，必须提供供磁盘访问 API 使用的 `disk-name`。下例使用 `VIRTIOBLK0` 作为磁盘名称。以下是 PCI 传输配置：

```dts
#include <zephyr/dt-bindings/pcie/pcie.h>

/ {
    pcie0 {
        virtio-blk-pci {
            compatible = "virtio,pci";
            vendor-id = <0x1af4>;
            device-id = <0x1001>;
            interrupts = <0xb 0x0 0x0>;
            interrupt-parent = <&intc>;
            status = "okay";

            virtio_blk: virtio-blk {
                compatible = "virtio,blk";
                disk-name = "VIRTIOBLK0";
                status = "okay";
            };
        };
    };
};
```

使用 MMIO 传输时，该节点是已有 `virtio,mmio` 总线的子节点：

```dts
&virtio_mmio4 {
    status = "okay";

    virtio_blk: virtio-blk {
        compatible = "virtio,blk";
        disk-name = "VIRTIOBLK0";
        status = "okay";
    };
};
```

## 29.7\_驱动与模拟器选项

驱动相关配置如下：

| 配置项 | 用途 |
| --- | --- |
| [`CONFIG_DISK_DRIVER_VIRTIO_BLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISK_DRIVER_VIRTIO_BLK) | 启用 VirtIO 块设备驱动 |
| [`CONFIG_DISK_VIRTIO_BLK_MAX_SEGMENTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISK_VIRTIO_BLK_MAX_SEGMENTS) | 每次请求的最大数据段数 |
| [`CONFIG_DISK_VIRTIO_BLK_SECTOR_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISK_VIRTIO_BLK_SECTOR_SIZE) | 未协商设备块大小时使用的扇区大小 |

在 QEMU 开发板上启用 [`CONFIG_DISK_DRIVER_VIRTIO_BLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISK_DRIVER_VIRTIO_BLK) 时，模拟层创建一个 **原始格式后端镜像（Raw Backing Image）**，并将其连接到模拟的 `virtio-blk` 设备。PCI 传输由公共 QEMU 模拟代码接入；`qemu_cortex_a53` 开发板则将 MMIO `virtio-blk-device` 接到 `virtio-mmio-bus.4`。

相关 QEMU 配置项为 [`CONFIG_QEMU_VIRTIO_BLK_LOGICAL_BLOCK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QEMU_VIRTIO_BLK_LOGICAL_BLOCK_SIZE) 和 [`CONFIG_QEMU_VIRTIO_BLK_DISK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QEMU_VIRTIO_BLK_DISK_SIZE)，分别设置逻辑块大小和磁盘大小。

## 29.8\_限制

- 任意时刻只处理一个请求。这与磁盘访问接口的同步约定一致；原文指出，这不会使该接口调用者损失吞吐量，但驱动不提供请求流水线。
- 与 Zephyr VirtIO 子系统的其他部分一样，驱动假定具备**缓存一致性直接存储器访问（Coherent Direct Memory Access，Coherent DMA）**，不对描述符、环形队列或数据缓冲区执行缓存维护。
- 使用 MMU 时，逻辑块大小不能超过 MMU 页大小。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：NVMe磁盘驱动](P028_NVMe磁盘驱动.md) · [本模块主线目录](../reading/storage.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：NVMe磁盘驱动](P028_NVMe磁盘驱动.md) · [下一章：Virtiofs文件系统示例](P030_Virtiofs文件系统示例.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
