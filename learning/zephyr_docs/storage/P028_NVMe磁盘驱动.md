---
id: learning.zephyr-docs.storage.diskmore-0
title: NVMe磁盘驱动
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/services/storage/disk/nvme.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第28章\_NVMe磁盘驱动

原文：[NVMe](https://docs.zephyrproject.org/latest/services/storage/disk/nvme.html)。读取日期：2026-10-13，`latest`。

**非易失性存储器高速接口（Non-Volatile Memory Express，NVMe）**是一种标准化的逻辑设备接口，用于通过 **高速外围组件互连（PCI Express，PCIe）**总线呈现存储设备。

Zephyr 支持 NVMe 控制器和磁盘。磁盘通过其提供的[磁盘访问接口（Disk Access API）](https://docs.zephyrproject.org/latest/services/storage/disk/access.html#disk-access-api)访问，因此也可以通过[文件系统接口（File System API）](https://docs.zephyrproject.org/latest/services/storage/file_system/index.html#file-system-api)使用。

## 28.1\_驱动设计

驱动主要分为三部分：

| 部分 | 源码 | 职责 |
| --- | --- | --- |
| NVMe 控制器（Controller） | [`nvme_controller.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/nvme_controller.c) | 设备驱动的根，创建驱动实例 |
| NVMe 命令（Command） | [`nvme_cmd.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/nvme_cmd.c) | 与控制器及其呈现的命名空间通信的通用逻辑 |
| NVMe 命名空间（Namespace） | [`nvme_namespace.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/nvme_namespace.c) | 处理实际命名空间，也就是磁盘 |

**设备树源文件（Devicetree Source，DTS）**只描述 NVMe 控制器，不描述它的各个命名空间。命名空间部分通过 [`drivers/disk/nvme/nvme_disk.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/disk/nvme/nvme_disk.c) 实现的磁盘访问接口，使应用能够访问每个磁盘。

若一个控制器提供多个命名空间，可以调整 [`CONFIG_NVME_MAX_NAMESPACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVME_MAX_NAMESPACES)，提高内置支持的命名空间数量。

每个磁盘通过对应 `disk_info` 结构中的名称区分，该名称继承自所属命名空间。磁盘命名形式为 `nvme<k>n<n>`，其中 `k` 是控制器编号，`n` 是命名空间编号。通常系统只接入一个 NVMe 磁盘时，呈现的磁盘名为 `nvme0n0`。

## 28.2\_设备树配置

提供 NVMe 磁盘的开发板应给出**设备树覆盖文件（Devicetree Overlay）**，以便在 Zephyr 中启用它：

其中 `VENDOR_ID` 和 `DEVICE_ID` 分别是所接 NVMe 控制器的厂商标识和设备标识。

```dts
#include <zephyr/dt-bindings/pcie/pcie.h>
/ {
    pcie0 {
        nvme0: nvme0 {
            compatible = "nvme-controller";
            vendor-id = <VENDOR_ID>;
            device-id = <DEVICE_ID>;
            status = "okay";
        };
    };
};
```

## 28.3\_配置选项

| 配置项 | 用途 |
| --- | --- |
| [`CONFIG_NVME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVME) | 启用 NVMe 支持 |
| [`CONFIG_NVME_MAX_NAMESPACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVME_MAX_NAMESPACES) | 配置支持的命名空间数量 |

NVMe 要求目标支持 PCIe 的**多向量消息信号中断扩展（Multi-vector Message Signaled Interrupts Extended，MSI-X）**，否则不能正常工作。

## 28.4\_数据缓冲区对齐要求

NVMe 规范要求数据缓冲区地址按**双字（Double Word，dword）**对齐，即 **4 字节对齐**。在为用户进程管理虚拟内存及动态分配的操作系统中，这通常不成问题；但在 Zephyr 中，缓冲区地址一旦直接映射到物理内存，就需要特别注意。

原文当前要求调用者自行确保传给磁盘读写函数 [`disk_access_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#ga5152825bf2a70902e65dbc596a944a1b) 和 [`disk_access_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html#gaa0495600320a71ea9e861fcf19da7184) 的缓冲区地址满足 4 字节对齐。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：安全存储服务](P021_安全存储服务.md) · [本模块主线目录](../reading/storage.md) · [全部主线](../reading/README.md) · [下一篇：VirtIO块设备驱动](P029_VirtIO块设备驱动.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：PSA存储条目元数据](P027_PSA存储条目元数据.md) · [下一章：VirtIO块设备驱动](P029_VirtIO块设备驱动.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
