---
id: learning.zephyr-docs.intercore_reference.ipcguide-93
title: ICMsg消息后端
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/services/ipc/ipc_service/backends/ipc_service_icmsg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第93章\_ICMsg消息后端

原文：[ICMsg backend](https://docs.zephyrproject.org/latest/services/ipc/ipc_service/backends/ipc_service_icmsg.html)。读取日期：2026-10-13，`latest`。

核间消息（Inter Core Messaging，ICMsg）后端是较重的RPMsg静态虚拟环（Static Vrings）后端的一种轻量替代方案，以较小内存占用提供最小功能集。它建立在[单生产者单消费者数据包缓冲区（Single Producer Single Consumer Packet Buffer）](../kernel/P061_单生产者单消费者包缓冲区.md)之上。RPMsg为远程处理器消息（Remote Processor Messaging）机制。

## 93.1\_通信模型

后端使用共享内存（Shared Memory）存放数据，使用邮箱（Mailbox，MBOX）设备通知另一侧数据已写入。单个实例（Instance）只支持注册一个端点（Endpoint）；应用需要多条通信通道时，必须定义多个实例，每个实例具有独立端点。

## 93.2\_配置与缓存对齐

后端通过Kconfig与设备树（Devicetree）配置：

1. 如果至少一个核心对共享内存使用数据缓存（Data Cache），设置`dcache-alignment`。它必须取通信两侧缓存失效（Invalidation）或写回（Write-back）粒度中的最大值。两侧均未对共享内存使用数据缓存时可以省略。
2. 定义两个内存区域，分配给实例的`tx-region`和`rx-region`。区域必须互不与其他区域重叠，并且两侧域（Domain）或中央处理器（Central Processing Unit，CPU）均可访问。
3. 定义用于通知数据已写入的MBOX设备，确保另一侧能够收到信号。

**原文注意事项：**务必正确设置`dcache-alignment`。错误值可能最初没有症状，使人误以为系统正常，但迟早会出现不稳定行为。

原实例配置如下；发送（Transmit，TX）与接收（Receive，RX）区域及通道均保留原值：

```dts
reserved-memory {
   tx: memory@20070000 {
      reg = <0x20070000 0x0800>;
   };

   rx: memory@20078000 {
      reg = <0x20078000 0x0800>;
   };
};

   ipc {
      ipc0: ipc0 {
         compatible = "zephyr,ipc-icmsg";
         dcache-alignment = <32>;
         tx-region = <&tx>;
         rx-region = <&rx>;
         mboxes = <&mbox 0>, <&mbox 1>;
         mbox-names = "tx", "rx";
         status = "okay";
      };
   };
};
```

另一侧也要提供相应配置，并交换MBOX通道以及`tx-region``rx-region`内存区域。**原片段译注：**上面的设备树代码按原样保留，其中末尾额外的闭合括号缺少本片段内对应的外层起始节点；应用时需放入相符的完整设备树结构中，不能把片段边界视为完整文件。

## 93.3\_建立绑定

端点注册后，连接此IPC实例的每侧按以下步骤建立绑定（Bonding）：

1. 把魔数（Magic Number）写入自己的`tx-region`。
2. 向另一侧发送数据已写入的信号，并按超时重复发送。
3. 收到另一侧信号后，从`rx-region`读取魔数。魔数正确则绑定完成，并调用[`ipc_service_cb.bound`回调](P112_IPC服务回调结构.md)通知应用。

配套示例见[IPC服务ICMsg示例](P095_IPC服务ICMsg示例.md)。

## 93.4\_共享内存区域布局

协议使用两个共享内存区域和两个MBOX通道；每个“区域＋通道”组合负责一个方向，另一组合对称地负责反方向。以下描述其中一组，另一组相同。每实例仍仅有一个端点。

启用数据缓存时，区域必须满足缓存对齐要求；不启用缓存时，必须按4字节对齐。整个区域用作一个先进先出队列（First In, First Out，FIFO），由读写索引与数据缓冲区组成。

| 字段 | 大小，字节 | 字节序（Byte Order） | 含义 |
| --- | --- | --- | --- |
| `rd_idx` | 4 | 小端（Little-endian） | 数据字段中第一个待接收字节的索引 |
| `padding` | 取决于缓存对齐 | 不适用 | 填充，使`wr_idx`满足缓存对齐 |
| `wr_idx` | 4 | 小端 | 数据字段中最后一个传入字节之后的位置索引 |
| `data` | 直到区域末尾的全部剩余空间 | 不适用 | 存放实际传输字节的循环缓冲区（Circular Buffer） |

索引到达数据缓冲区末尾时回绕；`rd_idx == wr_idx`表示FIFO为空。FIFO容量比数据缓冲区长度少1字节。

## 93.5\_数据包布局与发送

数据包（Packet）经上述FIFO发送，若位于缓冲区末尾，一个包可以回绕存放。

| 字段 | 大小，字节 | 字节序 | 含义 |
| --- | --- | --- | --- |
| `len` | 2 | 大端（Big-endian） | 数据字段长度 |
| `reserved` | 2 | 不适用 | 供未来使用；当前协议版本必须为0 |
| `data` | `len` | 不适用 | 数据包内容 |
| `padding` | 0至3 | 不适用 | 将包总大小补齐到4字节对齐 |

发送步骤为：检查包能否放入缓冲区；从`wr_idx`开始写入数据FIFO，必要时回绕；写入新的`wr_idx`；通过MBOX通道通知接收方。

## 93.6\_初始化协议

1. 把`wr_idx`和`rd_idx`设为0。
2. 向FIFO压入一个包含魔数数据的包，内容为`45 6d 31 6c 31 4b 30 72 6e 33 6c 69 34`。此时尚不使用MBOX。
3. 初始化MBOX。
4. 按一定间隔重复发送MBOX通知，例如1毫秒（Millisecond，ms）。
5. 等待另一组共享区域与MBOX通道传来包含魔数数据的包。
6. 停止重复MBOX通知。

完成后ICMsg已绑定，可以传输数据包。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：IPC服务使用指南](P092_IPC服务使用指南.md) · [本模块主线目录](../reading/intercore_reference.md) · [全部主线](../reading/README.md) · [下一篇：ICBMsg块消息后端](P094_ICBMsg块消息后端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：IPC服务使用指南](P092_IPC服务使用指南.md) · [下一章：ICBMsg块消息后端](P094_ICBMsg块消息后端.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
