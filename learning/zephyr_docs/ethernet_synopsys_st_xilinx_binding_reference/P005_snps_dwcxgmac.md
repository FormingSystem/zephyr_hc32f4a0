---
id: learning.zephyr-docs.ethernet-synopsys-st-xilinx-binding-reference.page-5
title: snps_dwcxgmac
kind: reference
status: maintained
domains: [zephyr, devicetree, ethernet]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/ethernet/snps,dwcxgmac.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第5章\_snps_dwcxgmac

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/ethernet/snps,dwcxgmac.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="snps-dwcxgmac"></a>
<a id="dtbinding-snps-dwcxgmac"></a>
<a id="std-dtcompatible-snps-dwcxgmac"></a>

兼容字符串（Compatible String）：`snps,dwcxgmac`。厂商：[ Synopsys, Inc. ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-snps)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=snps,dwcxgmac)。

驱动源码（Driver Source）：[drivers/ethernet/dwc_xgmac/eth_dwc_xgmac.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/dwc_xgmac/eth_dwc_xgmac.c)。

<a id="description"></a>

Synopsys DesignWareCore XGMAC。

译注：官方读请求限制说明使用 `WR_OSR_LMT + 1`，可编程突发长度说明列出 `4,5,16,32,64,128,256`，接收阈值说明使用 `11`。这些文字与属性表中的默认值／合法值分别照录，不擅自改成其他寄存器名、数值或进制。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 5.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `max-frame-size` | `int` | 最大以太网帧长度（Maximum Ethernet Frame Size）。硬件当前支持标准帧和巨帧（Jumbo Frame，最大16KB），通常XGMAC会拒绝超过 `max-frame-size` 的帧。默认1518字节，对应常见IEEE 802.3以太网帧：14字节MAC首部、1500字节最大传输单元（MTU）和4字节帧校验序列（FCS），合计1518字节。；默认值：`1518` |
| `max-speed` | `int` | 设备支持的最大速率（Maximum Speed），单位Mbit/s。XGMAC驱动支持10、100、1000和2500Mbit/s。默认值1000允许驱动配置10与100Mbit/s速率。2500Mbit/s仅能配合软物理编码子层（Soft Physical Coding Sublayer，Soft PCS）使用；选择此速率时，驱动假定Soft PCS通过GMII连接到XGMAC，因此必须将 `phy-connection-type` 选为 `gmii`。；默认值：`1000`；合法值：`10, 100, 1000, 2500` |
| `tx-fifo-size` | `int` | 指定MAC传输层（MAC Transaction Layer，MTL）发送先进先出队列（Transmit FIFO）的大小。；默认值：`32768`；合法值：`1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144` |
| `rx-fifo-size` | `int` | 指定MAC传输层（MTL）接收先进先出队列（Receive FIFO）的大小。；默认值：`32768`；合法值：`1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144` |
| `num-dma-ch` | `int` | **必需**。直接存储器访问（DMA）通道数量，范围1～8。 |
| `num-tx-queues` | `int` | **必需**。硬件发送队列（TX Queue）数量，范围1～8。 |
| `num-rx-queues` | `int` | **必需**。硬件接收队列（RX Queue）数量，范围1～8。 |
| `num-tc` | `int` | 流量类别（Traffic Class）数量，范围1～7。；默认值：`1` |
| `full-duplex-mode-en` | `boolean` | **必需**。将MAC通信模式设置为全双工模式（Full-Duplex Mode）。 |
| `wr-osr-lmt` | `int` | AXI最大未完成写请求限制（Maximum Write Outstanding Request Limit），限制AXI写接口上未完成请求的最大数量。最大未完成请求数为 `WR_OSR_LMT + 1`。；默认值：`31` |
| `rd-osr-lmt` | `int` | AXI最大未完成读请求限制（Maximum Read Outstanding Request Limit），限制AXI读接口上未完成请求的最大数量。原文给出的最大未完成请求数公式为 `WR_OSR_LMT + 1`。；默认值：`31` |
| `pbl` | `int` | 可编程突发长度（Programmable Burst Length，PBL）取值范围：4、5、16、32、64、128、256。；默认值：`32` |
| `edma-tdps` | `int` | 发送描述符预取阈值（TX Descriptor Pre-Fetch Threshold）。控制描述符缓存中触发DMA预取TxDMA描述符的阈值。对于所有TxDMA通道，只要该通道缓存中的描述符数量小于或等于设定阈值，DMA引擎就发起描述符获取请求。每个描述符为16字节。取值0、1、2、3、4、5。；默认值：`1` |
| `edma-rdps` | `int` | 接收描述符预取阈值（RX Descriptor Pre-Fetch Threshold）。控制描述符缓存中触发DMA预取RxDMA描述符的阈值。对于所有RxDMA通道，只要该通道缓存中的描述符数量小于或等于设定阈值，DMA引擎就发起描述符获取请求。每个描述符为16字节。取值0、1、2、3、4、5。；默认值：`1` |
| `pblx8` | `boolean` | 8倍PBL模式（8xPBL Mode）。设为真时，PBL值乘以8，因此DMA根据PBL值以8、16、32、64、128或256个传输节拍（Beat）传输数据。 |
| `ubl` | `boolean` | AXI未定义突发长度（Undefined Burst Length）。1：AXI主设备可执行小于或等于已启用最大允许突发长度的突发传输；0：AXI主设备按 `BLEN256`、`BLEN128`、`BLEN64`、`BLEN32`、`BLEN16`、`BLEN8` 或 `BLEN4` 字段指定的固定突发长度传输。 |
| `blen4` | `boolean` | AXI突发长度4（Burst Length 4）。启用此项且禁用 `mixed_burst` 时，AXI主设备可在AXI接口上选择长度4。启用 `mixed_burst` 时，启用此字段不起作用。 |
| `blen8` | `boolean` | AXI突发长度8（Burst Length 8）。启用此项且禁用 `mixed_burst` 时，AXI主设备可在AXI接口上选择长度8。启用 `mixed_burst` 时，启用此字段不起作用。 |
| `blen16` | `boolean` | AXI突发长度16（Burst Length 16）。启用此项且禁用 `mixed_burst` 时，AXI主设备可在AXI接口上选择长度16。启用 `mixed_burst` 时，启用此字段不起作用。 |
| `blen32` | `boolean` | AXI突发长度32（Burst Length 32）。启用此项且禁用 `mixed_burst` 时，AXI主设备可在AXI接口上选择长度32。启用 `mixed_burst` 时，启用此字段不起作用。 |
| `blen64` | `boolean` | AXI突发长度64（Burst Length 64）。启用此项且禁用 `mixed_burst` 时，AXI主设备可在AXI接口上选择长度64。启用 `mixed_burst` 时，启用此字段不起作用。 |
| `blen128` | `boolean` | AXI突发长度128（Burst Length 128）。启用此项且禁用 `mixed_burst` 时，AXI主设备可在AXI接口上选择长度128。启用 `mixed_burst` 时，启用此字段不起作用。 |
| `blen256` | `boolean` | AXI突发长度256（Burst Length 256）。启用此项且禁用 `mixed_burst` 时，AXI主设备可在AXI接口上选择长度256。启用 `mixed_burst` 时，启用此字段不起作用。 |
| `aal` | `boolean` | 地址对齐节拍（Address-Aligned Beats）。启用后，AXI主设备在读写通道上执行地址对齐的突发传输。 |
| `eame` | `boolean` | 增强地址模式使能（Enhanced Address Mode Enable）。DMA主设备启用40位或48位寻址的增强地址模式；DMA引擎根据配置使用40位或48位地址。 |
| `dma-ch-mss` | `int` | 最大分段长度（Maximum Segment Size，MSS）：对发送包分段时必须使用的最大分段长度。仅在启用TSE时有效。；默认值：`4096` |
| `dma-ch-tdrl` | `int` | 发送描述符环长度（Transmit Descriptor Ring Length），设置循环描述符环中的最大发送描述符数量，上限16384。；默认值：`512` |
| `dma-ch-rdrl` | `int` | 接收描述符环长度（Receive Descriptor Ring Length），设置循环描述符环中的最大接收描述符数量，上限16384。；默认值：`512` |
| `dma-ch-rbsz` | `int` | 接收缓冲区大小（Receive Buffer Size），单位字节。软件分配该缓冲区以存储接收DMA传输到主机内存的包，上限16K字节。启用首部分离时，此大小适用于载荷缓冲区（Payload Buffer）。；默认值：`16383` |
| `dma-ch-arbs` | `int` | 备用接收缓冲区大小（Alternate Receive Buffer Size，ARBS）。未启用首部分离（Split Header，SPH）时，非零ARBS表示缓冲区1的大小，单位字节；启用首部分离时，ARBS表示首部数据缓冲区大小。数据总线宽度为64位或128位时，备用缓冲区上限分别为1016或1008字节。`ARBS=0` 时，接收缓冲区1与2均根据RBSZ字段确定大小。数据总线宽度为64位或128位时，ARBS字段宽度分别为7位或6位。；默认值：`0` |
| `dma-ch-rxpbl` | `int` | 接收可编程突发长度（Receive Programmable Burst Length），表示一次DMA数据传输中的最大节拍数（Beat Count）。；默认值：`32` |
| `dma-ch-txpbl` | `int` | 发送可编程突发长度（Transmit Programmable Burst Length），表示一次DMA数据传输中的最大节拍数（Beat Count）。；默认值：`32` |
| `dma-ch-sph` | `boolean` | 首部与载荷分离（Header-Payload Split）。设置后，DMA在接收路径中将首部写到缓冲区地址1（Buffer Address1），将载荷写到缓冲区地址2（Buffer Address2）指向的缓冲区。软件必须确保首部能放入接收缓冲区；若首部长于接收缓冲区，DMA不会分离首部和载荷。 |
| `dma-ch-edse` | `boolean` | 增强描述符使能（Enhanced Descriptor Enable）。设置后，对应通道使用增强描述符。 |
| `dma-ch-tse` | `boolean` | TCP分段使能（TCP Segmentation Enabled，TSE）。设置后，DMA对该通道中的包执行TCP分段；仅处理发送普通描述符（TX Normal Descriptor）中设置了TSE的包。 |
| `dma-ch-osp` | `boolean` | 处理第二个包（Operate on Second Packet）。设置后，指示DMA在结束第一个包的描述符之前就开始处理发送数据中的第二个包。 |
| `mtl-raa` | `boolean` | 接收仲裁算法（Receive Arbitration Algorithm）：0为严格优先级（Strict Priority，SP），1为加权严格优先级（Weighted Strict Priority，WSP）。 |
| `mtl-etsalg` | `int` | 增强传输选择（Enhanced Transmission Selection，ETS）算法。对于传输选择算法（Transmission Selection Algorithm，TSA）设为ETS的流量类别，选择所用算法：0为加权轮询（Weighted Round Robin，WRR），1为加权公平排队（Weighted Fair Queuing，WFQ），2为亏空加权轮询（Deficit Weighted Round Robin，DWRR）。；默认值：`0` |
| `rxq-dyn-dma-en` | `int` | 启用接收队列的动态DMA通道选择（Dynamic DMA Channel Selection）。该字段每个位对应一个队列，共8个队列。；默认值：`1` |
| `rxq-dma-ch-sel` | `uint8-array` | 接收队列映射的DMA通道（DMA Channel Mapping），范围0～7。启用 `rxQ-DynDma-En` 时此字段无效。；默认值：`[0, 1, 2, 3, 4, 5, 6, 7]` |
| `txq-size` | `uint8-array` | 分配的发送队列大小，以256字节为单位，公式为 `(txQ-size + 1) x 256`。取值范围0～7。；默认值：`[127]` |
| `map-queue-tc` | `uint8-array` | 队列到流量类别的映射（Queue to Traffic Class Mapping），范围0～7。；默认值：`[0]` |
| `tx-threshold-ctrl` | `uint8-array` | 发送阈值控制（Transmit Threshold Control）。控制MTL发送队列阈值；队列内包大小大于阈值时开始发送，长度小于阈值的完整包也会发送。仅在禁用发送存储转发（Transmit Store and Forward）时使用。范围0～7，对应：0为64，1保留，2为96，3为128，4为192，5为256，6为384，7为512。；默认值：`[0]` |
| `rx-threshold-ctrl` | `uint8-array` | 当MTL接收队列内包大小大于阈值时，将接收到的包传给应用或DMA；长度小于阈值的完整包也会自动传送。若配置的接收队列大小为128字节，原文所写的值 `11` 不适用。此字段仅在RSF位为0时有效；RSF为1时忽略。范围0～3，对应：0为64，1保留，2为96，3为128。；默认值：`[0]` |
| `rxq-size` | `uint8-array` | 接收队列大小（Receive Queue Size），以256字节为单位，公式为 `(rxQ-size + 1) x 256`。取值范围0～127。；默认值：`[127]` |
| `tx-store-fwrd-en` | `int` | 发送存储转发（Transmit Store and Forward）。设置后，完整包驻留于MTL发送队列时才开始发送。每个位对应一个队列，共8个队列。；默认值：`255` |
| `hfc-en` | `int` | 启用硬件流量控制（Hardware Flow Control）。设置后，启用基于接收队列填充程度（Fill Level）的流控信号操作。每个位对应一个队列，共8个队列。；默认值：`0` |
| `cs-error-pkt-drop-dis` | `int` | 禁止丢弃TCP/IP校验和错误包（TCP/IP Checksum Error Packets）。每个位对应一个队列，共8个队列。；默认值：`0` |
| `rx-store-fwrd-en` | `int` | 接收存储转发（Receive Store and Forward）。设置后，DWC_xgmac仅在完整包已写入接收队列后才读取它。每个位对应一个队列，共8个队列。；默认值：`255` |
| `fep-en` | `int` | 转发错误包（Forward Error Packets）。设置后，除过短错误包（Runt Error Packets）外，所有包都转发给应用或DMA。每个位对应一个队列，共8个队列。；默认值：`0` |
| `fup-en` | `int` | 转发尺寸过小但有效的包（Forward Undersized Good Packets）。设置后，接收队列转发这些包。每个位对应一个队列，共8个队列。；默认值：`0` |
| `priorities-map-tc` | `array` | 映射到流量类别的优先级（Priorities Mapped to Traffic Class）。收到基于优先级的流量控制包（Priority Flow Control，PFC），且包中的优先级与本字段配置相符时，此字段决定是否在指定暂停时间内阻止关联流量类别的发送队列发送。取值范围0～7，数组最多8项；原例为 `<0,1,2,3,4,5,6,7>`。；默认值：`[0]` |
| `tx-sel-algorithm` | `uint8-array` | 传输选择算法（Transmission Selection Algorithm），为此流量类别指定算法：0为严格优先级（Strict Priority），1为基于信用的整形器（Credit-Based Shaper），2为增强传输选择（Enhanced Transmission Selection）。；默认值：`[0]` |
| `jumbo-pkt-en` | `boolean` | 巨帧使能（Jumbo Packet Enable）。设置后，MAC允许9018字节的巨帧，带VLAN标签时允许9022字节，且不会在接收包状态中报告超大包错误（Giant Packet Error）。 |
| `gaint-pkt-size-limit` | `int` | 超大包长度限制（Giant Packet Size Limit），单位字节。接收包长度超过此字段时，MAC判定为超大包。配置值必须大于或等于1518字节，其他值均按1518字节处理。；默认值：`9018` |
| `resets` | `phandle-array` | 复位信息（Reset Information） |
| `reset-names` | `string-array` | 各个复位的名称 |
| `phy-handle` | `phandle` | 指向物理层设备（Physical Layer Device，PHY）节点的引用。 |
| `phy-connection-type` | `string` | 以太网介质访问控制器（Ethernet MAC）与PHY之间的接口连接类型（Interface Connection Type）。；合法值：`mii, rmii, gmii, rgmii, rgmii-id, rgmii-txid, rgmii-rxid, tbi, rtbi, smii, sgmii, rev-mii, xgmii, moca, qsgmii, trgmii, internal` |
| `ptp-clock` | `phandle` | 对应的精确时间协议时钟设备（Precision Time Protocol Clock，PTP Clock）。 |
| `local-mac-address` | `uint8-array` | 分配给网络设备的MAC地址（MAC Address）。 |
| `zephyr,random-mac-address` | `boolean` | 使用驱动初始化时生成的随机MAC地址（Random MAC Address）。选择此方式后重启开发板，通信对端的地址解析协议缓存（Address Resolution Protocol Cache，ARP Cache）可能保留旧MAC，导致通信问题和延迟；Linux对端可用原文命令 `ip neigh flush all` 清除ARP缓存。组织唯一标识符（Organizationally Unique Identifier，OUI）字节如何处理取决于驱动。设置此属性后，忽略 `local-mac-address` 的所有设置。 |
| `zephyr,mac-address-prefix` | `uint8-array` | 静态分配的MAC地址前缀（MAC Address Prefix）。可与 `zephyr,random-mac-address` 或非易失性存储单元（NVMEM Cell）组合，例如用于设置OUI。 |
| `nvmem-cell-names` | `string-array` | 各 `nvmem-cells` 条目的名称（Cell Names）。 |
| `nvmem-cells` | `phandle-array` | NVMEM数据单元的节点引用列表（Phandle List）。 |

本页没有已弃用的节点专用属性。

## 5.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

涉及中断（Interrupt）、时钟（Clock）、直接存储器访问（Direct Memory Access，DMA）、输入输出（Input/Output，I/O）、邮箱（Mailbox，MBOX）、处理器间消息（Inter-Processor Messaging，IPM）、电源域（Power Domain）及硬件自旋锁（Hardware Spinlock）。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。给出寻址设备所需的信息，具体含义随设备及 `compatible` 而变化。通常是一组地址与长度对，每对称为寄存器块（Register Block），数值通常写为十六进制。参见规范v0.4第2.3.6节及[重要属性](../devicetree/P003_语法与结构.md#dt-important-props) |
| `interrupts` | `array` | **必需**。设备产生的中断，编码为一个或多个中断说明符；格式由设备在中断树中的位置决定，具有相同 `interrupt-parent` 的设备使用相同格式；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `reg-names` | `string-array` | 为 `reg` 中每个寄存器块提供可选名称；原始例子及逐项说明见本层表后 |
| `ranges` | `compound` | 定义总线子地址空间与总线节点父地址空间之间的映射或转换。通常为空，或由子总线地址、父总线地址、长度三元组组成。**空属性表示两侧地址空间相同、不需要转换；总线节点没有此属性则认为子、父地址空间之间不存在映射**。参见规范v0.4第2.3.8节 |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts`；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点；中断（Interrupt）及中断映射见《设备树规范》v0.4第2.4节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者（Clock Provider）信息，通常应遵守[dt-schema时钟绑定约定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml) |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的名称；通用说明称其为可选名称，是否必须填写以本层的必需标记为准 |
| `#address-cells` | `int` | 子节点 `reg` 地址字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `#size-cells` | `int` | 子节点 `reg` 大小字段所用的 `<u32>` 单元数量；`<u32>` 为32位无符号单元，参见《设备树规范》v0.4第2.3.5节 |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
| `dmas` | `phandle-array` | 与设备相关的 DMA 通道说明符 |
| `dma-names` | `string-array` | `dmas` 中各 DMA 通道说明符的可选名称 |
| `dma-ranges` | `compound` | 定义总线物理地址空间与其父总线物理地址空间之间的映射或转换，见规范 v0.4 第 2.3.9 节 |
| `io-channels` | `phandle-array` | 与设备相关的 I/O 通道说明符 |
| `io-channel-names` | `string-array` | `io-channels` 中各通道说明符的可选名称 |
| `mboxes` | `phandle-array` | 与设备相关的邮箱/IPM 通道说明符 |
| `mbox-names` | `string-array` | `mboxes` 中各邮箱说明符的可选名称 |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁（Hardware Spinlock）标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |
| `zephyr,deferred-init` | `boolean` | 延迟初始化（Deferred Initialization）：启动时不自动初始化设备，应由应用使用 `device_init()` 手动初始化 |
| `wakeup-source` | `boolean` | 标记设备可用作唤醒源（Wakeup Source）。设置该属性后，设备中会设置专门标志，通知系统此设备有唤醒能力。唤醒功能默认禁用，即中断不会唤醒系统；必要时可在运行期间启用 |
| `zephyr,pm-device-runtime-auto` | `boolean` | 初始化函数执行后，自动为设备配置运行时电源管理（Runtime Power Management） |
| `zephyr,disabling-power-states` | `phandles` | 会关闭该设备电源的电源状态（Power State）列表 |

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

## 以太网帧组成原式

```text
Ethernet Frame [ 14 MAC HEADER | 1500 MTU | 4 FCS ] = 1518 bytes
```

## 队列阈值编码原表 43

```text
      0: 64
      1: reserved
      2: 96
      3: 128
      4: 192
      5: 256
      6: 384
      7: 512
```

## 队列阈值编码原表 44

```text
      0: 64
      1: reserved
      2: 96
      3: 128
```

## 流量类别优先级映射原例

```dts
<0,1,2,3,4,5,6,7>
```

## Linux通信对端ARP缓存清理原命令

```sh
ip neigh flush all
```

## 5.3\_寄存器块命名原例

以下设备树源码（Devicetree Source，DTS）演示 `reg-names` 命名；`uart` 指通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）。

```dts
  / {
       soc {
           #address-cells = <1>;
           #size-cells = <1>;

           uart@1000 {
               reg = <0x1000 0x2000>, <0x3000 0x4000>;
               reg-names = "foo", "bar";
           };
       };
  };
```

`uart@1000` 节点有两个寄存器块（Register Block）：一个基址为 `0x1000`、大小为 `0x2000`、名称为 `foo`；另一个基址为 `0x3000`、大小为 `0x4000`、名称为 `bar`。

---

[上一章](P004_snps_designware-ethernet.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_snps_dwmac-ptp-clock.md)
