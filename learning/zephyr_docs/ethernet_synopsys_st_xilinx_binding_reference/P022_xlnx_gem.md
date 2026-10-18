---
id: learning.zephyr-docs.ethernet-synopsys-st-xilinx-binding-reference.page-22
title: xlnx_gem
kind: reference
status: maintained
domains: [zephyr, devicetree, ethernet]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/ethernet/xlnx,gem.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第22章\_xlnx_gem

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/ethernet/xlnx,gem.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="xlnx-gem"></a>
<a id="dtbinding-xlnx-gem"></a>
<a id="std-dtcompatible-xlnx-gem"></a>

兼容字符串（Compatible String）：`xlnx,gem`。厂商：[ Xilinx ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-xlnx)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=xlnx,gem)。

驱动源码（Driver Source）：[drivers/ethernet/eth_xlnx_gem_priv.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ethernet/eth_xlnx_gem_priv.h)。

<a id="description"></a>

Xilinx GEM以太网控制器（Ethernet Controller）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 22.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `phy-handle` | `phandle` | **必需**。指向物理层设备（Physical Layer Device，PHY）节点的引用。 |
| `clock-frequency` | `int` | **必需**。指定用于产生GEM发送时钟（TX Clock）的基准时钟频率；通过CRL_APB中对应GEM时钟控制寄存器的两个分频器进行分频。GEM发送时钟频率由PHY报告的当前链路速率决定，并在运行时调整。因此，此项必须设置为为对应GEM提供发送时钟的锁相环（PLL）频率；默认是I/O PLL。 |
| `handle-rx-in-isr` | `boolean` | 将接收帧中断处理移到中断服务程序（Interrupt Service Routine，ISR）上下文，包括把包数据从DMA转移到网络包缓冲区，以及随后将接收包递交给网络协议栈。由于大量接收数据时ISR执行时长难以预测，接收中断通常延后到系统工作队列（System Work Queue）上下文中处理。 |
| `handle-tx-in-workq` | `boolean` | 将帧发送完成中断处理移到系统工作队列（System Work Queue）上下文。默认在ISR上下文中处理发送完成，因为只涉及有限次数的内存访问。若当前系统中任何组件会在系统工作队列上下文中触发发送包，则**不能使用此选项**。 |
| `amba-ahb-burst-length` | `int` | **必需**。DMA操作的AMBA先进高性能总线（Advanced High-Performance Bus，AHB）突发长度（Burst Length）。；合法值：`1, 4, 8, 16` |
| `hw-rx-buffer-size` | `int` | **必需**。硬件接收缓冲区大小（Hardware RX Buffer Size），可在1kB至8kB之间调整，默认应使用完整8kB。；合法值：`0, 1, 2, 3` |
| `hw-rx-buffer-offset` | `int` | **必需**。硬件接收包缓冲区中的数据偏移（Data Offset），单位字节，有效范围0～3。 |
| `hw-tx-buffer-size-full` | `boolean` | 设置后，硬件发送数据缓冲区使用全部可用4kB；未设置时限制为2kB。 |
| `rx-buffer-descriptors` | `int` | **必需**。接收缓冲区描述符环（RX Buffer Descriptor Ring）分配的描述符数量，必须小于或等于255。 |
| `rx-buffer-size` | `int` | **必需**。每个接收数据缓冲区的大小，必须为8的倍数，最大有效值16320；小于64的值没有实际用途。 |
| `tx-buffer-descriptors` | `int` | **必需**。发送缓冲区描述符环（TX Buffer Descriptor Ring）分配的描述符数量，必须小于或等于255。 |
| `tx-buffer-size` | `int` | **必需**。每个发送数据缓冲区的大小，最大有效值16380；小于64的值没有实际用途。 |
| `ignore-ipg-rxer` | `boolean` | 可选功能标志：忽略帧间间隔（Inter-Packet Gap，IPG）中的 `rx_er`。设置后，`rx_dv` 为低时，`rx_er` 不影响GEM工作。以半双工模式使用RGMII封装（Wrapper）时设置此项。 |
| `disable-reject-nsp` | `boolean` | 可选功能标志：接收异常前导码（Bad Preamble）。设置后，不拒绝前导码非标准的帧。 |
| `ipg-stretch` | `boolean` | 可选功能标志：启用帧间间隔延长（IPG Stretch）。设置后，可使用IPG延长寄存器，根据前一帧长度将发送IPG增加到96位时间（Bit Times）以上。 |
| `sgmii-mode` | `boolean` | 可选功能标志：启用串行千兆介质独立接口（Serial Gigabit Media Independent Interface，SGMII）模式。改变自动协商通告及链路伙伴能力寄存器的行为，以满足SGMII要求，并把链路定时器时长从10ms缩短至1.6ms。 |
| `disable-reject-fcs-crc-errors` | `boolean` | 可选功能标志：禁止拒绝帧校验序列／循环冗余校验（FCS/CRC）错误帧。设置后不拒绝这些帧，但仍收集错误FCS帧的FCS错误统计，并在帧的DMA描述符中记录FCS状态。正常运行时不应启用。 |
| `rx-halfdup-while-tx` | `boolean` | 可选功能标志：在半双工（Half-Duplex）模式发送期间允许接收帧。 |
| `disable-rx-checksum-offload` | `boolean` | 禁止将接收IPv4／IPv6／TCP／UDP校验和处理卸载到硬件（RX Checksum Offload）。校验和卸载默认启用；QEMU目标未模拟硬件校验和卸载，因此会自动禁用，无需显式设置此标志。 |
| `disable-tx-checksum-offload` | `boolean` | 禁止将发送IPv4／IPv6／TCP／UDP校验和处理卸载到硬件（TX Checksum Offload）。校验和卸载默认启用；QEMU目标未模拟硬件校验和卸载，因此会自动禁用，无需显式设置此标志。 |
| `disable-pause-copy` | `boolean` | 可选功能标志：不将接收到的暂停帧（Pause Frame）复制到内存。设置后，无论复制全部帧位的状态如何、是否出现哈希匹配或类型标识匹配，均不把暂停帧复制到内存；但若找到目标地址匹配，仍会复制该暂停帧。收到的有效暂停帧仍会增加暂停统计，并按要求暂停帧发送。 |
| `discard-rx-fcs` | `boolean` | 可选功能标志：移除接收帧的帧校验序列（FCS）。设置后，写入内存的帧不包含末尾4字节FCS，所报告帧长度也减少4字节。 |
| `discard-rx-length-errors` | `boolean` | 可选功能标志：丢弃长度字段错误帧（Length Field Error）。设置后，若实际测得帧长小于提取的长度字段，即非VLAN标签帧的第13和14字节所表示的长度，则丢弃。仅适用于长度字段小于 `0x0600` 的帧。 |
| `pause-frame` | `boolean` | 可选功能标志：启用暂停（Pause）。设置后，在收到非零802.3经典暂停帧且尚未协商PFC时暂停发送。 |
| `tbi` | `boolean` | 可选功能标志：启用十位接口（Ten-Bit Interface，TBI），以TBI代替GMII／MII接口。 |
| `ext-address-match` | `boolean` | 可选功能标志：启用外部地址匹配（External Address Match），可通过外部地址匹配接口将帧复制到内存。 |
| `long-frame-rx-support` | `boolean` | 可选功能标志：允许接收1536字节帧。通常GEM会拒绝所有超过1518字节的帧。 |
| `unicast-hash` | `boolean` | 可选功能标志：启用单播哈希（Unicast Hash）。当目标地址的6位哈希结果指向哈希寄存器中已置位的位时，接受该单播帧。 |
| `multicast-hash` | `boolean` | 可选功能标志：启用多播哈希（Multicast Hash）。当目标地址的6位哈希结果指向哈希寄存器中已置位的位时，接受该多播帧。 |
| `reject-broadcast` | `boolean` | 可选功能标志：拒绝广播帧（Broadcast Frames），即目标地址为全1广播地址的帧。 |
| `discard-non-vlan` | `boolean` | 可选功能标志：丢弃非虚拟局域网（VLAN）帧，仅将带VLAN标签的帧交给地址匹配逻辑。 |
| `discard-rx-frame-ahb-unavail` | `boolean` | 可选功能标志：没有可用AHB资源时丢弃接收包。 |
| `ahb-packet-endian-swap` | `boolean` | 可选功能标志：将AHB包数据字节序（Endianness）交换为大端（Big-Endian）；未设置时数据为小端（Little-Endian）。 |
| `ahb-md-endian-swap` | `boolean` | 可选功能标志：将AHB管理描述符数据字节序（Endianness）交换为大端（Big-Endian）；未设置时数据为小端（Little-Endian）。 |
| `phy-connection-type` | `string` | 以太网介质访问控制器（Ethernet MAC）与PHY之间的接口连接类型（Interface Connection Type）。；合法值：`mii, rmii, gmii, rgmii, rgmii-id, rgmii-txid, rgmii-rxid, tbi, rtbi, smii, sgmii, rev-mii, xgmii, moca, qsgmii, trgmii, internal` |
| `ptp-clock` | `phandle` | 对应的精确时间协议时钟设备（Precision Time Protocol Clock，PTP Clock）。 |
| `local-mac-address` | `uint8-array` | 分配给网络设备的MAC地址（MAC Address）。 |
| `zephyr,random-mac-address` | `boolean` | 使用驱动初始化时生成的随机MAC地址（Random MAC Address）。选择此方式后重启开发板，通信对端的地址解析协议缓存（Address Resolution Protocol Cache，ARP Cache）可能保留旧MAC，导致通信问题和延迟；Linux对端可用原文命令 `ip neigh flush all` 清除ARP缓存。组织唯一标识符（Organizationally Unique Identifier，OUI）字节如何处理取决于驱动。设置此属性后，忽略 `local-mac-address` 的所有设置。 |
| `zephyr,mac-address-prefix` | `uint8-array` | 静态分配的MAC地址前缀（MAC Address Prefix）。可与 `zephyr,random-mac-address` 或非易失性存储单元（NVMEM Cell）组合，例如用于设置OUI。 |
| `nvmem-cell-names` | `string-array` | 各 `nvmem-cells` 条目的名称（Cell Names）。 |
| `nvmem-cells` | `phandle-array` | NVMEM数据单元的节点引用列表（Phandle List）。 |

本页没有已弃用的节点专用属性。

## 22.2\_基础属性

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

## Linux通信对端ARP缓存清理原命令

```sh
ip neigh flush all
```

## 22.3\_寄存器块命名原例

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

[上一章](P021_xlnx_axi-ethernet-1.00.a.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P023_zephyr_cdc-ecm-ethernet.md)
