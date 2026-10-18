---
id: learning.zephyr-docs.hardware.virtiohdr-1
title: VirtIO规范常量
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第594章\_VirtIO规范常量

原文：[virtio__config_8h](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/drivers/virtio/virtio_config.h` 提供基于**虚拟输入输出（Virtual I/O，VIRTIO）**规范的公共定义。原文依据 [Virtual I/O Device (VIRTIO) Version 1.3 规范草案 CSD01](https://docs.oasis-open.org/virtio/virtio/v1.3/csd01/virtio-v1.3-csd01.pdf)。

**外围组件互连（Peripheral Component Interconnect，PCI）**与**内存映射输入输出（Memory-Mapped I/O，MMIO）**是本文涉及的两类传输方式。虚拟队列由描述符表、**可用环（Available Ring）**和**已用环（Used Ring）**组成，基础说明见[VirtIO虚拟设备](P570_VirtIO虚拟设备.md)。

## 594.1\_设备状态位

以下数值是**设备状态字段（Device Status Field）**中的位位置，见规范 **2.1**。

| 宏 | 定义值 | 中文说明 |
| --- | --- | --- |
| [`DEVICE_STATUS_ACKNOWLEDGE`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a79f4e76454c62b79f8f63adbeb4db067) | `0` | 客户系统已发现并识别设备的存在 |
| [`DEVICE_STATUS_DRIVER`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a1bd93357913e45983876cd188160b0b1) | `1` | 客户驱动已准备好驱动该设备 |
| [`DEVICE_STATUS_DRIVER_OK`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#aaaf0e4541022cd8428fee351a50715cf) | `2` | 驱动已成功完成设备设置并准备就绪 |
| [`DEVICE_STATUS_FEATURES_OK`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a3534808ac9442cd8da136376d3826cff) | `3` | 驱动和设备已对协商的特性集合达成一致 |
| [`DEVICE_STATUS_NEEDS_RESET`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#ac19bebd85e291ae860efe48a30806f6c) | `6` | 设备请求复位，以从错误中恢复 |
| [`DEVICE_STATUS_FAILED`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#ab1423104e1f03023931691f0fccf770d) | `7` | 设备发生不可恢复的错误 |

## 594.2\_设备无关特性位

以下为可协商的、与设备类型无关的**特性位（Feature Bit）**位置，见规范第 **6** 章“保留特性位”。

| 宏 | 定义值 | 中文说明 |
| --- | --- | --- |
| [`VIRTIO_RING_F_INDIRECT_DESC`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#ab01a363ce20422c5d9065269fbf3eccf) | `28` | 描述符可以引用描述符表 |
| [`VIRTIO_RING_F_EVENT_IDX`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#abaad7d994ac1bb57a3bd2d058cff5c7a) | `29` | 驱动和设备使用**事件索引（Event Index）**进行通知 |
| [`VIRTIO_F_VERSION_1`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#adf75d3249c315cd2eb62c5d5dcf8b6f5) | `32` | 设备符合 Virtio 1.0 及以上版本的语义 |
| [`VIRTIO_F_ACCESS_PLATFORM`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a727adf9c6bb57e2b9697d6f881a9b648) | `33` | 设备需要平台专属处理 |

## 594.3\_环标志

原文将此组称为可用环与已用环的标志位位置，参见规范 **2.7.6** 与 **2.7.8**。宏的定义值如下。

| 宏 | 定义值 | 中文说明 |
| --- | --- | --- |
| [`VIRTQ_AVAIL_F_NO_INTERRUPT`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a1f7d7f5d8b604989da2d9d05b2005997) | `1` | 驱动请求设备不发送中断；原文的生效条件见下方译注 |
| [`VIRTQ_USED_F_NO_NOTIFY`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#ada005cf4163ae5c71d67caea8c6656d5) | `1` | 设备请求驱动抑制通知；原文的生效条件见下方译注 |

原文为上述两个标志附加的条件均为：协商了 [`VIRTIO_RING_F_EVENT_IDX`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#abaad7d994ac1bb57a3bd2d058cff5c7a) 时有效。

**译注：此条件与所引用规范不一致。**[规范 2.7.7 与 2.7.10](https://docs.oasis-open.org/virtio/virtio/v1.3/csd01/virtio-v1.3-csd01.html)规定，未协商事件索引特性时使用环的 `flags` 抑制通知；协商后应使用事件索引机制，并忽略相应标志的低位。两宏的值 `1` 是标志掩码，不能当作位编号再移位。这里保留 Zephyr 原文条件并明确差异，使用时应以规范为准。

## 594.4\_设备专属特性范围

这些常量定义设备专属特性位的两个范围，见规范 **2.2**。

| 宏 | 定义值 | 中文说明 |
| --- | --- | --- |
| [`DEV_TYPE_FEAT_RANGE_0_BEGIN`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#ad31df6cbc2435eab0f7a7da5cda7f5c3) | `0` | 第一段设备专属特性范围的起始值 |
| [`DEV_TYPE_FEAT_RANGE_0_END`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#afef88cb90d76e9550f1b2becf4cdcaac) | `23` | 第一段设备专属特性范围的结束值 |
| [`DEV_TYPE_FEAT_RANGE_1_BEGIN`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#abaf6a9556dac5a59edcb1f5daf4a36ea) | `50` | 第二段设备专属特性范围的起始值 |
| [`DEV_TYPE_FEAT_RANGE_1_END`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a811cceb8b32e5bafb9bcb3f57e26a2ab) | `127` | 第二段设备专属特性范围的结束值 |

## 594.5\_传输中断标志

规范分别在 PCI 的 **4.1.4.5 中断状态寄存器（Interrupt Status Register，ISR）状态能力**和 MMIO 的 **4.2.2 设备寄存器布局**中定义中断位。两类传输中相同位对应相同中断，因此可以共用以下定义。

| 宏 | 定义值 | 中文说明 |
| --- | --- | --- |
| [`VIRTIO_QUEUE_INTERRUPT`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a8a8e5464af12c3a17fe9dc222f9e7f5b) | `1` | 虚拟队列中有待处理的已用缓冲区 |
| [`VIRTIO_DEVICE_CONFIGURATION_INTERRUPT`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a316e58586ebbac85036da373bb5644a4) | `2` | 设备配置空间发生变化 |

## 594.6\_MMIO寄存器

以下常量给出 MMIO 寄存器的偏移量；表中含义为对应寄存器的用途，见规范 **4.2.2**。

| 宏 | 定义值 | 中文说明 |
| --- | --- | --- |
| [`VIRTIO_MMIO_MAGIC_VALUE`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#adbc4f6c0d30c76a45fdc2dabe4cd2cbb) | `0x000` | 标识 Virtio MMIO 设备的**魔数（Magic Value）** |
| [`VIRTIO_MMIO_VERSION`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#ab3b8d6bd5655e57baf01447384883076) | `0x004` | 设备提供的 Virtio 规范版本 |
| [`VIRTIO_MMIO_DEVICE_ID`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a843ffa98e22c96b9f33a0f4eb37a00cb) | `0x008` | 设备类型标识符寄存器 |
| [`VIRTIO_MMIO_VENDOR_ID`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#ae24a27c9de546c99f70992f060e4ce99) | `0x00c` | 厂商专属标识符寄存器 |
| [`VIRTIO_MMIO_DEVICE_FEATURES`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a5dd01aeb9c7de8d00b86814e1df075c1) | `0x010` | 设备特性位图的低 32 位 |
| [`VIRTIO_MMIO_DEVICE_FEATURES_SEL`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a27bbb089b991e1fa1d58b86d3cc3e266) | `0x014` | 选择设备特性字的选择器 |
| [`VIRTIO_MMIO_DRIVER_FEATURES`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a9cf63c483bba3f905802d27bdef1c405) | `0x020` | 已协商的驱动特性位图的低 32 位 |
| [`VIRTIO_MMIO_DRIVER_FEATURES_SEL`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a22773f246393c6d0eff617bcc58fb1ef) | `0x024` | 选择驱动特性字的选择器 |
| [`VIRTIO_MMIO_QUEUE_SEL`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#af06acc888e4338d9d286199d9f005380) | `0x030` | 选定供后续访问使用的虚拟队列索引 |
| [`VIRTIO_MMIO_QUEUE_SIZE_MAX`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a966b96f23d82f011b8292251f44d8b48) | `0x034` | 所选虚拟队列支持的最大队列大小 |
| [`VIRTIO_MMIO_QUEUE_SIZE`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#ae9adbc59d8d685515bd67596b425bb80) | `0x038` | 驱动为所选虚拟队列选择的大小 |
| [`VIRTIO_MMIO_QUEUE_READY`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a465c47ba6a9f60ba8ab41eeae4499463) | `0x044` | 表示驱动拥有队列的就绪标志 |
| [`VIRTIO_MMIO_QUEUE_NOTIFY`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#af33b9135a8725e32c95e412b97ecdce5) | `0x050` | 用于队列通知的**门铃寄存器（Doorbell Register）** |
| [`VIRTIO_MMIO_INTERRUPT_STATUS`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#ae8d1f2f787d1164fe9cc24b28bbc5c3c) | `0x060` | 待处理中断的汇总位 |
| [`VIRTIO_MMIO_INTERRUPT_ACK`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a2bec6b89c384b4860985d98340a540d5) | `0x064` | 中断确认寄存器 |
| [`VIRTIO_MMIO_STATUS`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a93ae0e8556428cc98d2f964eb82d3aec) | `0x070` | 设备状态 |
| [`VIRTIO_MMIO_QUEUE_DESC_LOW`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a47a92b06df621b14b67c3c45a7d3f97a) | `0x080` | 描述符表地址的低 32 位 |
| [`VIRTIO_MMIO_QUEUE_DESC_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#aa4404e6255943932d3460111008ae11d) | `0x084` | 描述符表地址的高 32 位 |
| [`VIRTIO_MMIO_QUEUE_AVAIL_LOW`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#abbfecd7e09cb3fb023e560b0ef2fed27) | `0x090` | 可用环地址的低 32 位 |
| [`VIRTIO_MMIO_QUEUE_AVAIL_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a3b6a9f0b3eb7e93b42f548e5cfe2923f) | `0x094` | 可用环地址的高 32 位 |
| [`VIRTIO_MMIO_QUEUE_USED_LOW`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a9c3a72dc51bf6a95b6b4d2169196a36e) | `0x0a0` | 已用环地址的低 32 位 |
| [`VIRTIO_MMIO_QUEUE_USED_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a241554a681b4b632095dbb1b28ec5462) | `0x0a4` | 已用环地址的高 32 位 |
| [`VIRTIO_MMIO_SHM_SEL`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a6ddda4856c222aa1205302d100dcfa9c) | `0x0ac` | 共享内存区域选择器 |
| [`VIRTIO_MMIO_SHM_LEN_LOW`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#ab5a127a0e786e7812716faa1ef27a7d0) | `0x0b0` | 共享内存长度的低 32 位 |
| [`VIRTIO_MMIO_SHM_LEN_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a9dcfe4991cca3f6ba7b5880764e75109) | `0x0b4` | 共享内存长度的高 32 位 |
| [`VIRTIO_MMIO_SHM_BASE_LOW`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a0a480f9d14c1ebf16b61c2451e631117) | `0x0b8` | 共享内存基地址的低 32 位 |
| [`VIRTIO_MMIO_SHM_BASE_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a0108a9f7bc697bc5e20dabbcf931db7e) | `0x0bc` | 共享内存基地址的高 32 位 |
| [`VIRTIO_MMIO_QUEUE_RESET`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#acdb238e4ef72f435057e225a8460abe8) | `0x0c0` | 队列复位控制寄存器 |
| [`VIRTIO_MMIO_CONFIG_GENERATION`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a8d56751604da30c6a1ba4b72c4fd6c95) | `0x0fc` | 配置空间的代次计数器（Generation Counter） |
| [`VIRTIO_MMIO_CONFIG`](https://docs.zephyrproject.org/latest/doxygen/html/virtio__config_8h.html#a56cf81f7dd4a2c3168a4df1d760190de) | `0x100` | 设备配置结构的基偏移量 |

---

[上一章：VirtIO公共头文件](P593_VirtIO公共头文件.md) · [下一章：VirtIO队列头文件](P595_VirtIO队列头文件.md) · [返回大纲](大纲.md)
